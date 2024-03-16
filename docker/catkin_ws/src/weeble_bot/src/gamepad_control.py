#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Joy
from motors.msg import motors_speed_msg
import traceback

rospy.init_node('control_node', anonymous=False)
pub_motors = rospy.Publisher('/motors_speed', motors_speed_msg, queue_size=1)

def listener():
    # changing the callback function passed will change the control scheme
    sub = rospy.Subscriber('gamepad', Joy, tank_drive)
    # TODO: subscribe to a topic that publishes the robot's estimated pose/heading based on sensors or dead reckoning (or both)
    rospy.spin()

def tank_drive(msg_in):
    '''
    Callback function to control motors based on joystick inputs using a tank drive scheme
    '''
    stick_LY = deadband_scale(msg_in.axes[1])
    stick_RY = deadband_scale(msg_in.axes[3])
    msg = motors_speed_msg()
    # y components of joystick inputs are directly mapped to motor powers
    msg.left_motor_speed = scale_output(stick_LY)
    msg.right_motor_speed = scale_output(stick_RY)
    pub_motors.publish(msg)

def single_joystick(msg_in):
    '''
    Callback function to control motors based on joystick inputs using a single joystick scheme
    The vertical joystick axis controls speed forward/backward, while the horizontal axis controls the rate of turning
    '''
    stick_LX = deadband_scale(msg_in.axes[0], low=0, high=255)
    # (255, 255) is at the bottom right corner, so y is "flipped" but x is not
    stick_LY = deadband_scale(msg_in.axes[1])
    # y component of joystick input is used to control linear speed
    # x component of joystick input is used to control angular speed
    msg = motors_speed_msg()
    msg.left_motor_speed = scale_output(stick_LY + 0.5 * stick_LX)
    msg.right_motor_speed = scale_output(stick_LY - 0.5 * stick_LX)
    pub_motors.publish(msg)

def heading_control(msg_in):
    '''
    Callback function to control motors based on joystick inputs by driving in whatever direction the joystick is pressed
    WIP, need to get accurate estimates of robot pose from DR and IMU (maybe filtering?)
    '''
    # TODO: implement this to run closed-loop control on the robot's estimated pose
    stick_LX = deadband_scale(msg_in.axes[0], low=0, high=255)
    stick_LY = deadband_scale(msg_in.axes[1])


def deadband_scale(val, low=255, mid=128, high=0, thresh=5):
    '''
    Utility function to implement a deadband on joystick inputs and scale inputs to a +-1 range
    '''
    centered = val - mid # center values at zero
    if abs(centered) <= thresh: # create deadband centered at zero
        return 0
    low_adj = mid - low # centered lower limit
    high_adj = high - mid # centered upper limit
    if (centered > 0 and centered <= high_adj) or (centered < 0 and centered >= high_adj):
        return centered / high_adj # normalize to a 0 - 1 scale
    else:
        return centered / low_adj # normalize to a -1 - 0 scale

def scale_output(val, low=300, high=480) -> int:
    '''
    Utility function to scale calculated motor powers to integer outputs for the motor driver node
    '''
    if val == 0: # check for deadband
        return 0
    elif val > 1: # upper saturation
        val = 1
    elif val < -1: # lower saturation
        val = -1
    out_range = high - low # scaling coef for output
    sign = 1 if val > 0 else -1 # in/out signs should match
    return int(sign * (out_range * abs(val) + low)) # cast the output to an int so ros can handle it

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

