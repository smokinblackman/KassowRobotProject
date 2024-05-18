cmake_minimum_required(VERSION 3.5)
project(kassow_realsense_integration)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(launch REQUIRED)
find_package(launch_ros REQUIRED)

# Install launch files.
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()






