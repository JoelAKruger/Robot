from launch import LaunchDescription

from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="joy",
            executable="game_controller_node",
            parameters=[{
                "deadzone": 0.1,
            }]
        ),
        Node(
            package="teleop_twist_joy",
            executable="teleop_node",
            parameters=["config/drive_twist_config.yaml"],
            remappings={("cmd_vel", "drive_vel")},
        )
    ])