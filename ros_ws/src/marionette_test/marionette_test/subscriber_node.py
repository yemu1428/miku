import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.sub=self.create_subscription(String,'sensor_data',self.callback,10)
        self.get_logger().info("订阅节点启动成功")
        self.count=0
        self.miscount=0
        self.angle_sum=0
        self.voltage_sum=0
        self.temp_sum=0
        self.flag=False
    def angle_check(self,angle):
        if angle<-5 or angle>5:
            self.angel_state="模拟关节平衡偏差过大"
            self.flag=True
        else:
            self.angel_state="模拟关节平衡偏差正常"
    def voltage_check(self,voltage):
        if voltage<11:
            self.voltage_state="模拟能源核心电压过低"
            self.flag=True
        else:
            self.voltage_state="模拟能源核心电压正常"
    def temp_check(self,temp):
        if temp>42:
            self.temp_state="模拟能源核心温度过高"
            self.flag=True
        else:
            self.temp_state="模拟能源核心温度正常"
    def callback(self,msg):
        payload=json.loads(msg.data)
        voltage=payload["voltage"]
        angle=payload["angle"]
        temp=payload["temp"]
        self.flag=False
        self.count+=1
        self.angle_check(angle)
        self.voltage_check(voltage)
        self.temp_check(temp)
        if self.flag:
            self.miscount+=1
        self.get_logger().info(f" 第{self.count} 次前置测试：平衡偏差  {angle}°，{self.angel_state}，核心电压 {voltage}V，{self.voltage_state}，核心温度 {temp}℃，{self.temp_state}")
        if self.count==8:
            self.get_logger().info(f"前置测试完成：共收到{self.count}条有效状态")
            self.get_logger().info(f"平均平衡偏差：{self.angle_sum}°，平均核心电压：{self.voltage_sum/self.count}，平均核心温度：{self.temp_sum/self.count}")
            self.get_logger().info(f"存在风险的状态：{self.miscount}条")
            self.get_logger().info("测试数据已经记录。")
def main(args=None):
    rclpy.init(args=args)
    node=SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()