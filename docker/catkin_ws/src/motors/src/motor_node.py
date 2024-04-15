#!/usr/bin/env python3
import rospy
from motors.msg import motors_speed_msg
from dual_tb9051ftg_rpi import motors, MAX_SPEED  # MAX_SPEED is 480 (hard-coded)
# Initialize the Node. This can happen here (to be executed as the script is interpreted by Python) or inside a function, but it must take place before any ROS communications take place.
rospy.init_node('motor_node', anonymous=False)

def listener():
    sub = rospy.Subscriber('motors_speed', motors_speed_msg, motor_handler)
    rospy.spin()
    
def motor_handler(msg_in):
    motors.motor1.setSpeed(msg_in.left_motor_speed)
    motors.motor2.setSpeed(msg_in.right_motor_speed)
    
if __name__ == "__main__":
    try: 
        listener()
    except rospy.ROSInterruptException: 
        motors.motor1.setSpeed(0)
        motors.motor2.setSpeed(0)
        pass
    
    motors.motor1.setSpeed(0)
    motors.motor2.setSpeed(0)