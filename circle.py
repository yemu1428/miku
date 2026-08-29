import rclpy
from rclpy.node import Node
from geometry_msgs.msgs import Twist
class Circle(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.get_logger.info("start")
        self.publisher=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        timer_period=0.1
        self.timer=self.create_timer(timer_period,self.timer_callback)
    def timer_callback(self):
        vel_msg=Twist()
        vel_msg.linear.x=1.0
        vel_msg.angular.z=0.5
        self.publisher_.publish(vel_msg)
        self.get_logger.info("发布速度：linear.x={vel_msg.linear.x}")
def main():
    rclpy.init()
    node=Circle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()