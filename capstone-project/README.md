# Capstone Project:  CI/CD, Containerization and Kubernetes Deployment for Machine Learning
## Capstone Project Overview
In this project, I will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:
- Working in AWS
- Using Jenkins or Circle CI to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working with Ansible and CloudFormation to deploy clusters
- Building Kubernetes clusters
- Building Docker containers in pipelines

# Dev
```
bentoml serve service.py:bentoml_service --reload
```
```
curl -X POST http://localhost:3000/classify1 -H "Content-Type: application/json" -d @curl/phase-1/prob-1/payload-1.json
curl -X POST http://localhost:3000/classify2 -H "Content-Type: application/json" -d @curl/phase-1/prob-2/payload-1.json
```
# Deploy
```
bentoml build
```
```
bentoml containerize bentoml_service:latest
```
```
docker compose up
```
```
curl -X POST http://localhost/phase-1/prob-1/predict -H "Content-Type: application/json" -d @curl/phase-1/prob-1/payload-1.json
curl -X POST http://localhost/phase-1/prob-2/predict -H "Content-Type: application/json" -d @curl/phase-1/prob-2/payload-1.json
```