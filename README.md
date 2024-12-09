# **Mobile Robot Simulation and Navigation**

This repository contains a complete simulation and navigation system for a mobile robot using ROS 2 and Gazebo. It focuses on providing a robust simulation environment, integrating robot descriptions, controllers, and teleoperation features.

---

## **Repository Structure**

### **1. Mobile Robot One**
This component provides a Gazebo simulation environment for a mobile robot, including:
- Custom URDF/Xacro-based robot model with physical and sensor properties.
- Gazebo world setup with realistic physics and plugins.
- ROS 2 integration for teleoperation and navigation.

For more details, visit the [Robot Simulation README](./robot_simulation/README.md).

### **2. Robot One Package**
This package is responsible for defining the robot's physical structure, controllers, and plugins required for simulation and navigation. It includes:
- Xacro and URDF files for robot description.
- Launch files for spawning the robot in Gazebo and configuring its controllers.
- Pre-configured Gazebo world files for simulation.

For more details, visit the [Robot One Package README](./robot_one/README.md).

---

developed by Rituraj Navindgikar
