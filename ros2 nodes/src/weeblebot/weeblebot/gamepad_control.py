#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from mobrob_interfaces.msg import ME439WheelSpeeds
import traceback

class TeleopNode(Node):

    def __init__(self):
        super().__init__('gamepad_control')
        self.pub = self.create_publisher(ME439WheelSpeeds, 'motors_speed', 1)
        self.sub = self.create_subscription(Joy, 'gamepad', self.tank_drive, 1)

    def tank_drive(self, msg_in):
        '''
        Callback function to control motors based on joystick inputs using a tank drive scheme
        '''
        stick_LY = deadband_scale(msg_in.axes[1], low=32767, high=-32768, thresh=1000)
        stick_RY = deadband_scale(msg_in.axes[3], low=32767, high=-32768, thresh=1000)
        msg = ME439WheelSpeeds()
        # y components of joystick inputs are directly mapped to motor powers
        msg.v0 = float(stick_LY)
        msg.v1 = float(stick_RY)
        self.pub.publish(msg)

    def single_joystick(self, msg_in):
        '''
        Callback function to control motors based on joystick inputs using a single joystick scheme
        The vertical joystick axis controls speed forward/backward, while the horizontal axis controls the rate of turning
        '''
        stick_LX = deadband_scale(msg_in.axes[0], low=0, high=255)
        # (255, 255) is at the bottom right corner, so y is "flipped" but x is not
        stick_LY = deadband_scale(msg_in.axes[1])
        # y component of joystick input is used to control linear speed
        # x component of joystick input is used to control angular speed
        msg = ME439WheelSpeeds()
        msg.v0 = scale_output(stick_LY + 0.5 * stick_LX)
        msg.v1 = scale_output(stick_LY - 0.5 * stick_LX)
        self.pub.publish(msg)

    def heading_control(self, msg_in):
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
    return int(sign * (out_range * abs(val) + low))


def main(args=None):
    rclpy.init(args=args)

    gamepad_control = TeleopNode()

    rclpy.spin(gamepad_control)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gamepad_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

