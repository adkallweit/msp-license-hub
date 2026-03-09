#!/bin/bash

echo "Installing MSP License Hub"

sudo apt update
sudo apt install docker.io docker-compose git -y

git clone https://github.com/adkallweit/msp-license-hub.git

cd msp-license-hub

cp .env.example .env

echo "Edit .env with your API keys"

docker compose build

docker compose up -d
