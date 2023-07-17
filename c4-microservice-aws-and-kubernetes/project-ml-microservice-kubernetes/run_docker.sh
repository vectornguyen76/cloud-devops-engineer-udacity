#!/bin/bash

image_name=project-ml-kube
image_tag=v1.0.0
container_name=project-ml-kube

# Build image and add a descriptive tag
docker build -t $image_name:$image_tag .

# List docker images
docker image list

# Run flask app
docker run --name $container_name -p 8000:80 --rm $image_name:$image_tag