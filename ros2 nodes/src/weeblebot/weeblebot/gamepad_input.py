#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from evdev import InputDevice, categorize, ecodes
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import traceback


class GamepadParser(Node):

    def __init__(self):
        super().__init__('gamepad_input') # start the node with a name
        self.pub = self.create_publisher(Joy, 'gamepad', 1)
        self.inputs_dict = {"ABS_X":128,"ABS_Y":128,"ABS_RX":128,"ABS_RY":128} # dict to store most recent states
        gamepad = self.get_gamepad()
        try:
            while rclpy.ok():
                for event in gamepad.read_loop():
                    if event.type != 0: # filter out type 0 (sync) events
                        event_name = ecodes.bytype[event.type][event.code] # look up the event name based on its type and code
                        if type(event_name) != str:
                            event_name = event_name[0] # some events have multiple names, just take the first
                        self.inputs_dict[event_name] = event.value # update the dict with the value
                        # print(inputs_dict)
                        gamepad_msg = Joy() # prepare a message to send
                        gamepad_msg.header.stamp = self.get_clock().now().to_msg()
                        # the two joysticks are packed in (lx, ly), (rx, ry) order
                        gamepad_msg.axes = [float(self.inputs_dict[key]) for key in ["ABS_X","ABS_Y","ABS_RX","ABS_RY"]]
                        # TODO: pack relevant button states into the message
                        self.pub.publish(gamepad_msg)
                    if not rclpy.ok():
                        break
        except KeyboardInterrupt:
            return


    def get_gamepad(self, timeout=5):
        '''
        function to initiate the bluetooth connection to an xbox controller
        '''
        for _ in range(timeout): # don't try infinitely because that's annoying
            try:
                print('attempting to connect...')
                for i in range(5): # the event number is not entirely predictable
                    print('debug')
                    gamepad = InputDevice(f'/dev/input/event{i}') # use evdev to make an inputdevice object
                    if "Xbox Wireless Controller" in gamepad.name: # filter out all other devices
                        print('success')
                        return gamepad
            except Exception as e:
                print(e)
                pass


def main(args=None):
    rclpy.init(args=args)

    gamepad_input = GamepadParser()

    rclpy.spin(gamepad_input)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gamepad_input.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
