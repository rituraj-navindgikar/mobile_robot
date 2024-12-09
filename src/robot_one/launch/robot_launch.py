from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node 

from ament_index_python.packages import get_package_share_directory

import xacro
import os

def generate_launch_description():
    robotXacro = 'robot_one' #given name in robot_one.xacro file
    pkg_name = 'robot_one'
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    modelFile = 'model/robot_one.xacro'
    worldFile = 'model/my_room.world'

    pathModelFile = os.path.join(get_package_share_directory(pkg_name), modelFile)
    pathWorldFile = os.path.join(get_package_share_directory(pkg_name), worldFile)
    robotDescription = xacro.process_file(pathModelFile).toxml()
    
    gazebo_ros_pkg_launch = PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'))

    gazebo_launch = IncludeLaunchDescription(gazebo_ros_pkg_launch, launch_arguments={'world':pathWorldFile}.items())

    spawnModelNode = Node(package='gazebo_ros',
                        executable='spawn_entity.py',
                        arguments=['-topic', '/robot_description', '-entity', robotXacro ,'-x', '0', '-y', '0', '-z', '0.3'],
                        output='screen')
    
    nodeRobotStatePublisher = Node(package='robot_state_publisher',
                                   executable='robot_state_publisher',
                                   output='screen',
                                   parameters=[{'robot_description':robotDescription, 'user_sim_time':True}])


    ld = LaunchDescription()

    # ld.add_action(gzserver_cmd)
    # ld.add_action(gzclient_cmd)
    ld.add_action(gazebo_launch)  
    ld.add_action(spawnModelNode)
    ld.add_action(nodeRobotStatePublisher)

    return ld



















