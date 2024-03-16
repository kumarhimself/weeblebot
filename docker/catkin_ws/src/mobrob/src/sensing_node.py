#!/usr/bin/env python3

import numpy as np
import rospy
import traceback

# IMPORT the custom messages:
# we import it "from" the ROS package we created it in (here "me439robot") with an extension of .msg ...
# and actually import the message type by name (here "ME439SensorsRaw" and others)
from mobrob_util.msg import EncodersRaw

# Max encoder increment (full speed) - useful for eliminating errors
enc_increment_max = 1000

try:
    f = open("/dev/encoder-driver",'rb');
except Exception as e:
    print(e,file=sys.stderr)
    print("ENCODER DRIVER NOT FOUND... DID YOU FORGET TO sudo make load IT?",file=sys.stderr)
    exit()

#==============================================================================
# # Set up a system to coordinate the motor closed-loop control
#==============================================================================
#   (Motor control is not ROS-friendly using ordinary messages due to delays.)
def talker():
    # Launch a node called "sensing_and_wheel_control_node"
    rospy.init_node('sensing_node', anonymous=False)
#==============================================================================
#     # Start the loop that listens and publishes.
#==============================================================================
    # Give it an argument of the [qe0,qe1] encoders and the [mc0,mc1] motor controllers so it can update them all.
    encoder_publisher()

def readEncoders():
    bytes = f.read(8);
    leftInt = int.from_bytes(bytes[0:3],"little",signed=True)
    rightInt = int.from_bytes(bytes[4:7],"little",signed=True)
    return [leftInt,rightInt]

#==============================================================================
# # Main loop function that listens to the encoder pin, calls motor control, and publishes the sensor data
#==============================================================================
def encoder_publisher():
# Create the publisher for the topic "/sensors_data_raw", with message type "ME439SensorsRaw"
    pub_sensors = rospy.Publisher('/sensors_data_raw', EncodersRaw, queue_size=10)

    # Declare the message that will go on that topic.
    # Here we use one of the message name types we Imported, and add parentheses to call it as a function.
    # We could also put data in it right away - here initializing to zero.
    pub_sensors_message = EncodersRaw()

    [leftEnc, rightEnc] = readEncoders();
    pub_sensors_message.e1 = 0
    pub_sensors_message.e0 = 0

    while not rospy.is_shutdown():

        pub_sensors_message.e0 = leftEnc
        pub_sensors_message.e1 = rightEnc
        pub_sensors_message.t = rospy.get_rostime()

        # Publish a message to the "/sensors_data_raw" topic.
        pub_sensors.publish(pub_sensors_message)
        # Log the info (optional)
        rospy.loginfo(pub_sensors)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        traceback.print_exc()
        pass