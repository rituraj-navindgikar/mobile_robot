# **robot_one**

This ROS2 package simulates a mobile robot in Gazebo and includes support for URDF-based robot description, spawning models, and controlling the robot using teleoperation. It integrates with `robot_state_publisher` for publishing transforms and `gazebo_ros` for simulation.

---

## **Features**
- **Gazebo Integration**  
  Simulate the robot in the custom `my_room.world` environment.
  
- **Robot Description**  
  Utilize URDF/Xacro to describe the robot's physical properties, links, joints, and sensors.

- **Spawning**  
  Dynamically spawn the robot model in Gazebo using `spawn_entity.py`.

- **State Publishing**  
  Publish robot states and transforms using `robot_state_publisher`.

- **Teleoperation**  
  Control the robot using teleoperation tools like `teleop_twist_keyboard`.

---

## **File Structure**
### **Launch Files**
1. **`robot_launch.py`**  
   - Launches the Gazebo simulation with the `my_room.world` environment.
   - Spawns the robot and starts the `robot_state_publisher`.

   Command:
   ```bash
   ros2 launch robot_one robot_launch.py


Developed By
Rituraj Navindgikar
