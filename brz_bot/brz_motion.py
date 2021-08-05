import rclpy
from rclpy.node import Node 

from geometry_msgs.msg import Twist

class BrzMotion(Node):
    def __init__(self):
        super().__init__('brz_motion')
        self.subscription = self.create_subscription(
            Twist,
            'key_vel',
            self.topic_callback,
            10)
    
    def topic_callback(self, msg):
        self.get_logger().info(" I hear you calling!")
        self.get_logger().info(str(msg.linear.x))

def main(args=None):
    rclpy.init(args=args)
    sub = BrzMotion()
    rclpy.spin(sub)

    sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
