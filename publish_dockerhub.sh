#!/usr/bin/env bash
set -e

# Prompt for user inputs
read -p "Enter your Docker Hub username: " DOCKER_USER
read -sp "Enter your Docker Hub Access Token: " DOCKER_PAT
echo ""
read -p "Enter image name (default: monad-hft-node): " IMAGE_NAME
IMAGE_NAME=${IMAGE_NAME:-monad-hft-node}

read -p "Enter version tag (default: latest): " TAG
TAG=${TAG:-latest}

FULL_IMAGE="${DOCKER_USER}/${IMAGE_NAME}:${TAG}"

echo "--> Logging into Docker Hub..."
echo "$DOCKER_PAT" | docker login -u "$DOCKER_USER" --password-stdin

echo "--> Building Docker image: ${FULL_IMAGE}..."
docker build -t "$FULL_IMAGE" .

echo "--> Pushing ${FULL_IMAGE} to Docker Hub..."
docker push "$FULL_IMAGE"

echo " Successfully pushed ${FULL_IMAGE} to Docker Hub!"
