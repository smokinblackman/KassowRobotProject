import os
import subprocess

def check_path_exists(path):
    if os.path.exists(path):
        print(f"[OK] Path exists: {path}")
    else:
        print(f"[MISSING] Path does not exist: {path}")

def check_ros_env_var(var_name):
    value = os.environ.get(var_name)
    if value:
        print(f"[OK] Environment variable {var_name} is set to {value}")
    else:
        print(f"[MISSING] Environment variable {var_name} is not set")

def check_ros_package(package_name):
    try:
        result = subprocess.run(['ros2', 'pkg', 'prefix', package_name], check=True, capture_output=True, text=True)
        print(f"[OK] ROS package '{package_name}' is installed at {result.stdout.strip()}")
    except subprocess.CalledProcessError:
        print(f"[MISSING] ROS package '{package_name}' is not installed")

def main():
    print("Checking paths...")
    paths_to_check = [
        "/opt/ros/humble/setup.bash",
        "/opt/ros/humble/share/launch",
        "/opt/ros/humble/share/launch_ros",
        "src/kassow_realsense_integration/CMakeLists.txt",
        "src/kassow_realsense_integration/package.xml",
        "src/kassow_realsense_integration/launch/realsense_kassow.launch"
    ]
    for path in paths_to_check:
        check_path_exists(path)
    
    print("\nChecking environment variables...")
    env_vars_to_check = [
        "CMAKE_PREFIX_PATH",
        "AMENT_PREFIX_PATH",
        "ROS_DISTRO",
        "ROS_VERSION"
    ]
    for var in env_vars_to_check:
        check_ros_env_var(var)
    
    print("\nChecking ROS packages...")
    ros_packages_to_check = [
        "ament_cmake",
        "rclcpp",
        "sensor_msgs",
        "cv_bridge",
        "launch",
        "launch_ros"
    ]
    for pkg in ros_packages_to_check:
        check_ros_package(pkg)
    
    print("\nAll checks done. Please review the output above for any missing elements.")

if __name__ == "__main__":
    main()


