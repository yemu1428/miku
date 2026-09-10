import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
class SubNode(Node):
    def __init__(self):
        super().__init__("subscriber_node")
        self.points=[[0,0],[2,0],[4,1],[4,3],[2,4],[0,4],[-1,2],[-1,1]]
        self.connect=[3,4,5,6,7,0,1,2]
        self.sub=self.create_subscription(String,"pubsub_topic",self.callback,10)
        self.last_state=None
        self.vx=0.0
        self.vy=0.0
        self.get_logger().info("Subscriber节点已启动")
    def callback(self,msg):
        try:
            data=json.loads(msg.data)
        except json.JSONDecodeError:
            self.get_logger().warn("收到非法json消息，跳过")
            return
        state=data["state"]
        self.vx=data["vx"]
        self.vy=data["vy"]
        current_idx=data["current_idx"]
        next_idx=data["next_idx"]
        self.get_logger().info(f"接收成功")
        if state=="move":
            # 此处应该是一些控制小车电机转速来实现具体速度方向及大小的实际调整
            self.get_logger().info("正在前往下一个目标点")
        elif state=="arrive":
            #此处应该是控制小车电机停转的代码
            self.get_logger().info(f"============到达目标点{current_idx+1}!即将前往{next_idx+1}============")
        elif state=="finish":
            self.get_logger().info(f"================到达终点{current_idx+1}!================")
        self.last_state=state 
def main(args=None):
    rclpy.init(args=args)
    node=SubNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()
