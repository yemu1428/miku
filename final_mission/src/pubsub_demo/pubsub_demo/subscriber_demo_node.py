import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class SubNode(Node):
    def __init__(self):
        super().__init__("subscriber_node")
        self.points=[[0,0],[2,0],[4,1],[4,3],[2,4],[0,4],[-1,2],[-1,1]]
        self.connect=[3,4,5,6,7,0,1]
