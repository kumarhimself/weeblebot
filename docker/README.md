### Building the docker image:
After any changes, to build the Dockerfile into an image with the tag ros_image, run `sudo docker build -t ros_image . `

### Starting the docker container:
After any devices (e.g. gamepad, camera) are connected, to start a docker continer, run `sh docker_run.sh`

### Opening a new terminal in the docker container:
Open a new tab and run `sh docker_exec.sh`

### Removing an old image:
View a list of all current images to find the one to remove by running `sudo docker images`, then find the `IMAGE ID` of the image to be removed and run `sudo docker rmi <IMAGE ID>`

### Changing the commands executed on docker startup:
Edit the file `ros_entrypoint.sh` and rebuild the image from the Dockerfile. Assuming the Dockerfile is unchanged the rebuild should be pretty fast because everything else is cached.
