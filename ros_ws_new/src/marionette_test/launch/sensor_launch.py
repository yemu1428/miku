from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
def generate_launch_description():
    pkg_dir=get_package_share_directory('marionette_test')
    yaml_path=os.path.join(pkg_dir,'launch','params.yaml')
    return LaunchDescription([
        Node(
            package='marionette_test',
            executable='publisher',
            name='publisher_node',
            parameters=[yaml_path],
        ),
        Node(
            package='marionette_test',
            executable='subscriber',
            name='subscriber_node',
            parameters=[yaml_path]
        )
    ])