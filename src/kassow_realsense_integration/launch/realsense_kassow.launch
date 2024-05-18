import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            name='realsense2_camera',
            output='screen',
            parameters=[{
                'camera_name': 'D435',
                'depth_module.profile': '640x480x30',
                'rgb_camera.profile': '640x480x30',
            }],
        ),
        Node(
            package='kassow_driver',
            executable='kassow_driver_node',
            name='kassow_driver',
            output='screen',
            parameters=[{
                'robot_ip': '192.168.1.100',
            }],
        ),
    ])
