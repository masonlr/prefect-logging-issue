FROM python:3.8-slim

# Set system locale
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt update && \
    apt install -y gcc git && \
    mkdir /root/.prefect/ && \
    pip install --no-cache-dir prefect[kubernetes] && \
    apt remove -y git && \
    apt clean && apt autoremove -y && \
    rm -rf /var/lib/apt/lists/*
