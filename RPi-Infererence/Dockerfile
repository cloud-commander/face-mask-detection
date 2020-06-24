#Build (on x86): docker buildx build --platform linux/arm/v7 -t YOURDOCKERHUB/image:latest --push .
#Run (on Pi): docker run -t -i --privileged -p 80:5000 -v /dev/bus/usb:/dev/bus/usb cloudcommanderdotnet/rpitpuinference:latest

FROM balenalib/raspberrypi3-debian-python:3.7-latest

#downloading sources & update
RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - \
    && apt-get update 

#install libraries for camera and opencv2
RUN apt-get install -y --no-install-recommends build-essential wget  pkg-config libjpeg-dev zlib1g-dev \
    libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin libfreetype6-dev libxml2 libopenjp2-7 \
    libatlas-base-dev libjasper-dev libqtgui4 libqt4-test libavformat-dev libswscale-dev libedgetpu1-std python3-opencv python3-edgetpu 

#downloading library file & install
RUN wget https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl \ 
    && pip3 install tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl \
    && rm tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl 

#install web server python libraries
RUN python3 -m pip install flask Werkzeug itsdangerous tornado imutils \  
    && python3 -m pip install Jinja2 MarkupSafe Werkzeug 

RUN apt-get autoremove \
    && rm -rf /tmp/* \
    && rm -rf /var/lib/apt/lists/*

#opencv2 bug on arm (Undefined reference to __atomic)
ENV LD_PRELOAD "/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0"

WORKDIR /inference

ADD model /inference
ADD templates /inference/templates
ADD inference.py /inference/

ENTRYPOINT ["python3", "inference.py"]

EXPOSE 5000

#set stop signal
STOPSIGNAL SIGTERM
