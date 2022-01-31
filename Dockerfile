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

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - &&  apt-get install -yq nodejs build-essential
RUN npm install -g npm
RUN npm install -g ganache-cli@6.12.1


RUN python3 -m venv /venv
RUN /venv/bin/pip install --upgrade pip

# # wheel doesn't appear to be installed by default in the arm/v7 python image
RUN python3 -m pip install --user pipx
RUN python3 -m pipx ensurepath
RUN ~/.local/bin/pipx install eth-brownie

COPY requirements.txt ./
RUN /venv/bin/pip install -r requirements.txt
