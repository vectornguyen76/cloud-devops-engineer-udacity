# Capstone Project:  CI/CD, Containerization and Kubernetes Deployment for Machine Learning
## Overview
In this project, I will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:
- Working in AWS
- Using Jenkins or Circle CI to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working with Ansible and CloudFormation to deploy clusters
- Building Kubernetes clusters
- Building Docker containers in pipelines

### Local
1. Create environment and install packages:
    ```shell
    conda create -n mlops python=3.9
    ```
    ```shell
    conda activate mlops
    ```
    ```shell
    pip install -r requirements.txt
    ```
2. Convert to bentoml model
    ```shell
    python bentoml_model.py
    ```
3. Run 
    ```shell
    bentoml serve service.py:bentoml_service --reload
    ```
4. Test
    ```shell
    curl -X POST http://localhost:3000/classify1 -H "Content-Type: application/json" -d @test/prob_1/payload-1.json
    ```
    ```shell
    curl -X POST http://localhost:3000/classify2 -H "Content-Type: application/json" -d @test/prob_2/payload-1.json
    ```

### Managing Bentos
1. Export bentoml service
    ```
    bentoml export bentoml_service:latest ./bentoml_service
    ```
2. Import bentoml service
    ```
    bentoml import ./bentoml_service-oqlrrpbfhkrraaav.bento
    ```

### Development
1. Build BentoML service
    ```
    bentoml build
    ```
    Bento is the unit of deployment in BentoML, one of the most important artifacts to keep track of in your model deployment workflow. BentoML provides CLI commands and APIs for [managing Bentos](https://docs.bentoml.com/en/latest/concepts/bento.html#managing-bentos) and moving them around, see the Managing Bentos section to learn more.
2. Generate Docker Image
    A docker image can be automatically generated from a Bento for production deployment, via the bentoml containerize CLI command:
    ```
    bentoml containerize bentoml_service:latest
    ```
    This creates a docker image that includes the Bento, and has all its dependencies installed. The docker image tag will be same as the Bento tag by default:
    ```
    docker images
    ```
3. Run the docker image to start the BentoServer:
    ```
    docker run -it --rm -p 3000:3000 bentoml_service:oqlrrpbfhkrraaav serve
    ```