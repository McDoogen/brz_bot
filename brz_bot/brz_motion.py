import rclpy
from rclpy.node import Node 

from std_msgs.msg import String # Will need to change to cmd_vel ?

class BrzMotion(Node):
    def __init__(self):
        super().__init__('brz_motion')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.topic_callback,
            10)
    
    def topic_callback(self, msg):
        self.get_logger().info(" I hear you calling!")

def main(args=None):
    rclpy.init(args=args)
    sub = BrzMotion()
    rclpy.spin(sub)

    sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
