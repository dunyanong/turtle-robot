from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    number_publisher_node = Node(
        package="my_py_pkg",
        executable="number_publisher",
        name="my_number_publisher",
        remappings=[
            ("number", "my_number")
        ]
        parameter=[
            {}
        ]
    )



    ld.add_action(number_publisher_node)
    return ld