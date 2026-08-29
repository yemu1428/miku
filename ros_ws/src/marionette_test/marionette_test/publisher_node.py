import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import String
import json
class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.pub=self.create_publisher(String,'sensor_data',10)
        self.timer=self.create_timer(2.0,self.send_data)
        self.index=1
        self.max_count=8
    def send_data(self):
        angle=round(random.uniform(-7.0,7.0),2)
        voltage=round(random.uniform(10.5,12.6),2)
        temp=round(random.uniform(25.0,48.0),1)
        data={"voltage":voltage,"angle":angle,"temp":temp}
        msg=String()
        msg.data=json.dumps(data)
        self.pub.publish(msg)
        self.get_logger().info(f"已发布-->{data}")
        self.index +=1
        if self.index>self.max_count:
            self.get_logger().info("数据发送完毕")
            self.timer.cancel()
def main(args=None):
    rclpy.init(args=args)
    node=PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()


