#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, Float32
from motors.msg import motors_speed_msg
# from motors.dual_tb9051ftg_rpi import MAX_SPEED # MAX_SPEED is 480 (hard-coded)
# TODO: Find a way to fix the upper line
MAX_SPEED = 480
# Initialie a node to send commands
# Could use rostopic pub -r 10 /motors_speed motors/motors_speed_msg 100.0 100.0 to manually send commands
rospy.init_node('motors_command_node',anonymous=False)  # anonymous specifies no nodes with the same name

def talker_to_motors():
    pub = rospy.Publisher('motors_speed', motors_speed_msg, queue_size = 1)
    r = rospy.Rate(10)
    msg = motors_speed_msg()
    while not rospy.is_shutdown(): 
        lms = int(input('Enter wheel command left (-480 to +480) \n'))
        rms = int(input('Enter wheel command right (-480 to +480) \n'))
        # Check if there's illegal input
        # Correct any illegal inputs
        if lms < -1*MAX_SPEED:
            lms = -1*MAX_SPEED
        elif lms > MAX_SPEED:
            lms = MAX_SPEED
        if rms < -1*MAX_SPEED:
            rms = -1*MAX_SPEED
        elif rms > MAX_SPEED:
            rms = MAX_SPEED
        msg.left_motor_speed = lms
        msg.right_motor_speed = rms
        pub.publish(msg)

if __name__ == "__main__":
    try:
        talker_to_motors()
    except rospy.ROSInterruptException:
        pass