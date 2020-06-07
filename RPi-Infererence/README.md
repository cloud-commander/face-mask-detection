# Inference with Raspberry Pi and Google Coral Edge TPU

### Overview
This container packages all the requirements needed to perform inference using a Tensorflow Lite model trained on the Object Detection API and assumes you are making use of a Google Coral Edge TPU. 

You will also require a webcam plugged into your RPi although you can change the source to a network based camera if you wish.

### Prebuilt Container
If you wish to make use of a prebuilt Docker image then you can access it from Docker Hub using the following command
`docker pull cloudcommanderdotnet/rpitpuinference:latest`

### Running the Container
Make sure you have your webcam and Coral USB plugged in.

To run the container, enter the following command
`docker run -it -p 80:5000 -v /dev/bus/usb:/dev/bus/usb cloudcommanderdotnet/rpitpuinference:latest`

The container is started in privileged mode, all the RPi USB devices are mapped to the container and port 5000 is mapped to port 80.

Now you just have to navigate to the IP address of your RPi in a web browser to see the object detection taking place.
