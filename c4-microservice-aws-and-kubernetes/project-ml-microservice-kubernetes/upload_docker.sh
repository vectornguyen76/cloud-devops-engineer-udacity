#!/bin/bash

image_name=project-ml-kube
image_tag=v1.0.0

# Create docker_path
docker_path=vectornguyen76

# Add variable DOCKER_PASSWORD
source .env

# Log in to Docker
echo "$DOCKER_PASSWORD" | docker login --username "$docker_path" --password-stdin

# Check if login was successful
if [ $? -eq 0 ]; then
    echo "Docker authentication successful!"
else
    echo "Docker authentication failed!"
fi

echo "Docker ID and Image: $docker_path"

docker image tag "$image_name:$image_tag" "$docker_path/$image_name:$image_tag"

# Push image to a docker repository
docker push $docker_path/$image_name:$image_tag