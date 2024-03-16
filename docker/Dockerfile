FROM ros:noetic

# build pigpiod for gpio pins
RUN apt update && apt install -y \
	wget \
	unzip \
	python3-pip \
	nano \
	vim \
	ros-noetic-rqt \
	ros-noetic-rqt-graph \
	&& wget https://github.com/joan2937/pigpio/archive/master.zip \
	&& unzip master.zip \
	&& cd pigpio-master \
	&& make \
	&& sudo make install \
	&& pip install pigpio 

# apparently exposing this port helps pigpiod?
EXPOSE 8888

# sourcing ros stuff
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.bashrc \
	&& echo "source /catkin_ws/devel/setup.bash" >> /root/.bashrc

# pip installing some python packages
RUN pip install sparkfun-qwiic-icm20948 \
	evdev \
	matplotlib

ENV DISPLAY=$DISPLAY \
	QT_X11_NO_MITSHM=1

# copy in the entrypoint script
COPY ./ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
