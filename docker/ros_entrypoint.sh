#!/bin/bash

# exit out if something goes wrong? (i think)
set -e

# start pigpio daemon
pigpiod

# source base ros
source "/opt/ros/$ROS_DISTRO/setup.bash"

# make catkin stuff
cd /catkin_ws
catkin_make
cd ..

# source catkin packages
source "/catkin_ws/devel/setup.bash"
exec "$@"
