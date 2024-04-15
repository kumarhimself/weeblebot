cd catkin_ws/src/ClonedRepos/RaspberryPiKernelEncoder
sudo make unload
sudo make load
cd ../../../..
xhost +local:root
sudo docker run --rm \
	--privileged \
	--name ros_container \
	--net=host \
	-e DISPLAY=$DISPLAY \
	-p 8888:8888 \
	-it \
	-v ./catkin_ws:/catkin_ws \
	-v /tmp/.X11-unix:/tmp.X11-unix:rw \
	ros_image bash
xhost -local:root
