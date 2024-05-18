# Kassow Robot and RealSense D435i Integration Project
## Setup Instructions
1. **Install necessary dependencies:**
   ```bash
   sudo apt-get install ros-<ros_distro>-realsense2-camera
Replace <ros_distro> with your ROS distribution (e.g., noetic, melodic).

Clone the repository:

bash
Copy code
git clone <repository_url>
cd KassowRobotProject
Build the ROS package:

bash
Copy code
cd ~/catkin_ws
catkin_make
source devel/setup.bash
Run the launch file:

bash
Copy code
roslaunch kassow_realsense_integration realsense_kassow.launch
Usage
Run the main Python script to start processing data from the RealSense camera:

bash
Copy code
python src/main.py
Configuration
Camera Settings
Configured in config/config.yaml:

resolution: Resolution of the camera
frame_rate: Frame rate of the camera
color_enabled: Enable color stream
depth_enabled: Enable depth stream
imu_enabled: Enable IMU
Robot Settings
Configured in config/config.yaml:

ip_address: IP address of the Kassow robot
port: Port number for connecting to the robot
joint_names: Names of the robot joints
joint_limits: Joint limits for safety
payload: Payload in kilograms
tool_center_point: Tool center point configuration
base_frame: Base frame for the robot
end_effector_frame: End-effector frame for the robot
Network Settings
Configured in config/config.yaml:

timeout: Network timeout in seconds
Logging Settings
Configured in config/config.yaml:

level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
log_to_file: Whether to log to a file
log_file_path: Path to the log file
Path Planning Settings
Configured in config/config.yaml:

algorithm: Path planning algorithm (RRT, RRT*, PRM, etc.)
max_iterations: Maximum iterations for the algorithm
goal_tolerance: Goal tolerance in meters
Safety Settings
Configured in config/config.yaml:

collision_avoidance: Enable collision avoidance
emergency_stop: Enable emergency stop
Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.