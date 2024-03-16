#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from evdev import InputDevice, categorize, ecodes
import rospy
from sensor_msgs.msg import Joy
import traceback

inputs_dict = {"ABS_X":128,"ABS_Y":128,"ABS_RX":128,"ABS_RY":128} # dict to store most recent states

def get_gamepad(timeout=5):
    for _ in range(timeout): # don't try infinitely because that's annoying
        try:
            print('attempting to connect...')
            for i in range(5): # the event number is not entirely predictable
                gamepad = InputDevice(f'/dev/input/event{i}') # use evdev to make an inputdevice object
                if "PLAYSTATION(R)3 Controller" in str(gamepad) and "Motion" not in str(gamepad): # filter out all other devices
                    print('success')
                    return gamepad
        except:
            pass

def gamepad_talker():
    rospy.init_node('gamepad_node', anonymous=False) # start the node
    gamepad_pub = rospy.Publisher('/gamepad', Joy, queue_size=1) # make a publisher for controller state
    gamepad = get_gamepad()
    try:
        while not rospy.is_shutdown():
            for event in gamepad.read_loop():
                if event.type != 0: # filter out type 0 (sync) events
                    event_name = ecodes.bytype[event.type][event.code] # look up the event name based on its type and code
                    if type(event_name) != str:
                        event_name = event_name[0] # some events have multiple names, just take the first
                    inputs_dict[event_name] = event.value # update the dict with the value
                    # print(inputs_dict)
                    gamepad_msg = Joy() # prepare a message to send
                    gamepad_msg.header.stamp = rospy.get_rostime()
                    # the two joysticks are packed in (lx, ly), (rx, ry) order
                    gamepad_msg.axes = [inputs_dict[key] for key in ["ABS_X","ABS_Y","ABS_RX","ABS_RY"]]
                    # TODO: pack relevant button states into the message
                    gamepad_pub.publish(gamepad_msg)
                if rospy.is_shutdown():
                    break
    except KeyboardInterrupt:
        return
    except:
        gamepad = get_gamepad()


if __name__ == "__main__":
    try:
        gamepad_talker()
    except rospy.ROSInterruptException:
        traceback.print_exc()
        pass
