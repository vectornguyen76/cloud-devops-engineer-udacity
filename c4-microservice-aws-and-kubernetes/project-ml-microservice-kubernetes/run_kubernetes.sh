#!/bin/bash

image_name=project-ml-kube
image_tag=v1.0.0
deployment_name=project-ml-kube

# This is your Docker ID/path
docker_path=vectornguyen76

# Run the Docker Hub container with kubernetes
kubectl create deploy $deployment_name --image=$docker_path/$image_name:$image_tag
# kubectl create deploy project-ml-kube --image=vectornguyen76/project-ml-kube:v1.0.0

# List kubernetes pods
kubectl get pods

# Forward the container port to a host
kubectl port-forward deployment.apps/$deployment_name --address 0.0.0.0 8000:80
# kubectl port-forward deployment.apps/project-ml-kube --address 0.0.0.0 8000:80
