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
        # Lienar X, Angular Z
        # Forward/Backward = Linear X, Turn both motors same direction
        # Turn Left/Right = Angular Z, Turn Both motors Opposite Directions
        # Stop = Linear X is 0, Angular Z is 0, stop both motors
        if msg.linear.x != 0:
            self.kit.motor1.throttle = msg.linear.x
            self.kit.motor2.throttle = msg.linear.x
            print_out = "Robot Moving"
        elif msg.angular.z != 0:
            self.kit.motor1.throttle = -msg.angular.z
            self.kit.motor2.throttle = msg.angular.z
            print_out = "Robot Rotating"
        else:
            self.kit.motor1.throttle = 0.0
            self.kit.motor2.throttle = 0.0
            print_out = "Robot Stopped"
        self.get_logger().info(print_out)

def main(args=None):
    rclpy.init(args=args)
    sub = BrzMotion()
    rclpy.spin(sub)

    sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
