FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install flask mpmath
WORKDIR /workspace
ENTRYPOINT python3 Site.py
