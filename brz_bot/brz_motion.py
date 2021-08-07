from adafruit_motorkit import MotorKit

# ROS Imports
import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist


class BrzMotion(Node):
    def __init__(self):
        super().__init__('brz_motion')
        self.kit = MotorKit()
        self.subscription = self.create_subscription(
            Twist,
            'key_vel',
            self.topic_callback,
            10)
        
    
    def topic_callback(self, msg):
        # TODO: Here we want to react to the velocity commands received from the key_vel topic
        # We'll receive Lienar and Angular speeds, we in turn set the motors to move accordingly. Is there already a library for this?
        print_out = f"Linear X: {msg.linear.x}, Y: {msg.linear.y}, Z: {msg.linear.z}\n"
        print_out+= f"Angular X: {msg.angular.x}, Y: {msg.angular.y}, Z: {msg.angular.z}"
        self.get_logger().info(print_out)

def main(args=None):
    rclpy.init(args=args)
    sub = BrzMotion()
    rclpy.spin(sub)

    sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
