FROM ubuntu:latest
WORKDIR /usr/src

RUN apt-get update && apt-get -y install \
    g++ \
    gcc \
    curl \
    libffi-dev \
    libpq-dev \
    libsnappy-dev \
    libssl-dev \
    make \
    python3-dev \
    python3-pip \
    python3-venv \
    build-essential \
    &&  rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
