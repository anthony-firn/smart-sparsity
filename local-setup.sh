#!/bin/bash

# Update package list and install dependencies
sudo apt-get update

# Install Docker
if ! [ -x "$(command -v docker)" ]; then
    echo "Docker not found, installing..."
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
else
    echo "Docker is already installed"
fi

# Install NVIDIA Container Toolkit (if GPU is available)
if lspci | grep -i nvidia; then
    echo "NVIDIA GPU detected, installing NVIDIA Container Toolkit..."
    sudo apt-get install -y nvidia-container-toolkit
    sudo systemctl restart docker
else
    echo "No NVIDIA GPU detected, skipping NVIDIA Container Toolkit installation"
fi

# Install act
if ! [ -x "$(command -v act)" ]; then
    echo "act not found, installing..."
    curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
else
    echo "act is already installed"
fi

# Install Rust (if needed for your tests)
if ! [ -x "$(command -v rustc)" ]; then
    echo "Rust not found, installing..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source $HOME/.cargo/env
    rustup default stable
else
    echo "Rust is already installed"
fi

# Create .env file for act
echo "Creating .env file for act..."
echo "LOCAL_RUN=true" > .env

echo "Setup complete. You can now run local-test.sh to execute the tests."