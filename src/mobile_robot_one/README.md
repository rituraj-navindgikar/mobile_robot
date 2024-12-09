# **Robot Simulation and Navigation in ROS2**

This project demonstrates a mobile robot simulation in **Gazebo** integrated with **ROS 2** for navigation, SLAM, and control. The robot's simulation supports real-time visualization, teleoperation, and autonomous navigation using SLAM for mapping and localization.

---

## **Features**
- **Gazebo Simulation**  
  Launch a detailed robot simulation in a custom environment using `.world` files.
  
- **SLAM Integration**  
  Utilize `slam_toolbox` for real-time mapping and localization. Supports both mapping and localization modes.

- **Teleoperation**  
  Control the robot using `teleop_twist_keyboard` or any teleoperation method of your choice.

- **ROS 2 Controllers**  
  Configured differential drive controllers for realistic robot movement in simulation.

- **Visualization**  
  Real-time visualization of maps and robot movements using `rviz2`.

---

## **File Descriptions**

### Launch Files
1. **`gazebo_sim.launch.py`**  
   - Launches the Gazebo simulation environment with the robot and spawns the robot in the world.  
   - Command:  
     ```bash
     ros2 launch mobile_robot_one gazebo_sim.launch.py world:=src/mobile_robot_one/worlds/building_room.world
     ```

2. **`rsp.launch.py`**  
   - Starts the `robot_state_publisher` for publishing the robot's state and transforms.  
   - Command:  
     ```bash
     ros2 launch mobile_robot_one rsp.launch.py use_sim_time:=true
     ```

### Map Files
1. **`my_map_save.pgm`** and **`my_map_save.yaml`**  
   - Pre-saved map data for localization mode in SLAM.
   - The `.yaml` file specifies resolution, origin, and thresholds.

2. **SLAM Parameters**  
   - **`mapper_params_online_async.yaml`**: Configures `slam_toolbox` for mapping and localization tasks, including scan matching, loop closure, and map saving.

### Robot Configuration
1. **`my_controllers.yaml`**  
   - Configures ROS 2 controllers for differential drive:
     - Differential Drive Controller (`diff_drive_controller`)
     - Joint State Broadcaster (`joint_state_broadcaster`)

2. **URDF/Xacro Files**  
   - Robot description files (processed by `robot_state_publisher`) for the simulation.

### World Files
1. **`building_room.world`**  
   - Custom world environment for robot simulation in Gazebo.

---
You can run teleoperations to control the bot with keyboard
- Command:  
     ```bash
     ros2 run teleop_twist_keyboard teleop_twist_keyboard 
     ```
### Dependencies
- ROS 2 (Humble)
- Gazebo
- slam_toolbox
- Rviz2

  
Developed By
Rituraj Navindgikar
