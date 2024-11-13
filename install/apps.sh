#!/bin/bash

# Update package list and upgrade packages
sudo apt update && sudo apt upgrade -y

# Misc
sudo apt install -y webp
# sudo apt install -y vVv
# sudo apt install -y vVv
# sudo apt install -y vVv
# sudo apt install -y vVv


# Install essential packages
sudo apt install -y python3 python3-pip wget curl git imagemagick tesseract-ocr ffmpeg fonts-noto-color-emoji fonts-emojione

# Install Python packages for image processing, OCR, and emoji handling
pip3 install pillow pytesseract opencv-python emoji

# Install additional useful tools
sudo apt install -y unzip zip jq htop build-essential software-properties-common

# Optional: Add aliases to bashrc for convenience
echo "alias ll='ls -la'" >> ~/.bashrc.
echo "alias update='sudo apt update && sudo apt upgrade -y'" >> ~/.bashrc.
echo "alias install='sudo apt install -y'" >> ~/.bashrc.

# Reload bash profile to apply aliases
source ~/.bashrc

echo "Installation complete."

# apt list --installed