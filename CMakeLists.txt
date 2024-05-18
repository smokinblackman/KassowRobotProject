cmake_minimum_required(VERSION 3.5)
project(kassow_realsense_integration)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(launch REQUIRED)
find_package(launch_ros REQUIRED)

add_executable(main src/main.py)
ament_target_dependencies(main rclcpp sensor_msgs cv_bridge)

install(TARGETS
  main
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
