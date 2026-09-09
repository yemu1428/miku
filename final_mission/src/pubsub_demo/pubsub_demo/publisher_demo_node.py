import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import math
class PubNode(Node):
    def __init__(self):
        super().__init__("publisher_node")
        self.points=[[0,0],[2,0],[4,1],[4,3],[2,4],[0,4],[-1,2],[-1,1]]
        self.connect=[3,4,5,6,7,0,1]
        self.declare_parameter("start_point",1)
        self.start_point=self.get_parameter("start_point").get_parameter_value().integer_value
        self.i=self.start_point-1
        self.current_x=self.points[self.i][0]
        self.current_y=self.points[self.i][1]
        self.j=self.connect[self.i]
        self.pub=self.create_publisher(String,"pubsub_topic",10)
        self.dt=0.05
        self.timer=self.create_timer(self.dt,self.move)
    def move(self):
        target_x=self.points[self.j][0]
        target_y=self.points[self.j][1]
        dx=target_x-self.current_x
        dy=target_y-self.current_y
        distance=math.sqrt(dx**2+dy**2)
        arrive_distance=0.05
        if distance<arrive_distance:
            msg=String()
            msg.data=f"到达点{self.j+1},前往点{self.connect[self.j+1]}"
            self.pub.publish(msg)
            self.get_logger()
            self.i=self.j
            self.j=self.connect[self.j]
            self.current_x=self.points[self.i][0]
            self.current_y=self.points[self.i][1]
        else:
            vx=2*dx/distance
            vy=2*dy/distance
            self.current_x+=vx*self.dt
            self.current_y+=vy*self.dt
            self.get_logger().info(f"当前位置：x={self.current_x},y={self.current_y}")
def main(args=None):
    rclpy.init(args=args)
    node=PubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()