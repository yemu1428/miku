from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(
            package="pubsub_demo",
            executable="publisher_demo_node",
            name="pub_node",
            parameters=[
                {"start_point":1},
                {"end_point":1}
            ]
        ),
        Node(
            package="pubsub_demo",
            executable="subscriber_demo_node",
            name="sub_node"
        )
    ])