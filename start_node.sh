#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Building the Monad-HFT-Node image..."
docker build -t monad-hft-node:latest .

echo "Starting the node..."
# Runs the container interactively, maps the port, and mounts the current directory
docker run -it --rm \
  -p 8888:8888 \
  -v $(pwd):/app \
  --name hft_node_instance \
  monad-hft-node:latest

echo "Node shut down successfully."
