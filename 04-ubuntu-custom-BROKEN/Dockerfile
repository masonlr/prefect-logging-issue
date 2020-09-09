FROM ubuntu:20.04

# Set system locale
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt update && \
    apt install -y gcc git python3-pip && \
    mkdir /root/.prefect/ && \
    ln -s /usr/bin/pip3 /usr/bin/pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip install --no-cache-dir prefect[kubernetes] && \
    apt remove -y git && \
    apt clean && apt autoremove -y && \
    rm -rf /var/lib/apt/lists/*

