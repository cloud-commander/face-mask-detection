# 1) build: docker build -t YOURDOCKERHUB/image:latest --push .
# 2) run: docker run -it --privileged -p 8000:5000 -v /dev/bus/usb:/dev/bus/usb cloudcommanderdotnet/amd64tpuinference:latest


FROM amd64/debian:buster

RUN apt-get update && apt-get install -y wget gnupg usbutils

RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | tee /etc/apt/sources.list.d/coral-edgetpu.list
RUN wget -qO - https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

RUN apt-get update && apt-get install -y python3-pip pkg-config libedgetpu1-std python3-wget

RUN python3 -m pip install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_x86_64.whl 

RUN apt-get install -y python3-opencv python3-scipy

RUN python3 -m pip install flask Werkzeug itsdangerous \  
    && python3 -m pip install Jinja2 MarkupSafe Werkzeug imutils

RUN apt-get autoremove \
    && rm -rf /tmp/* \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /inference

ADD model /inference
ADD templates /inference/templates
ADD inference.py /inference/

ENTRYPOINT ["python3", "inference.py"]

