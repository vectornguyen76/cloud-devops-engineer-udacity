# Project: Operationalizing Machine Learning: Containerization and Kubernetes Deployment for Housing Price Prediction
[![vectornguyen76](https://circleci.com/gh/vectornguyen76/cloud-devops-engineer-udacity.svg?style=svg)](https://app.circleci.com/pipelines/github/vectornguyen76/cloud-devops-engineer-udacity)

## Project Overview:
The project aims to operationalize a Machine Learning Microservice API that predicts housing prices in Boston using a pre-trained sklearn model. The Flask app (app.py) serves predictions through API calls. The project focuses on containerization with Docker and deployment using Kubernetes. Additionally, the code is tested using linting and CircleCI.

## Project Tasks:
1. Test Project Code: Ensure the code passes linting tests to maintain code quality and consistency.

2. Dockerize the Application: Create a Dockerfile to containerize the Flask application, making it portable and isolated.

3. Deploy with Docker: Utilize Docker to deploy the containerized application and test the prediction functionality.

4. Improve Log Statements: Enhance the log statements in the source code for better visibility and debugging.

5. Configure Kubernetes and Create Cluster: Set up Kubernetes and create a Kubernetes cluster to manage containerized applications.

6. Deploy with Kubernetes: Utilize Kubernetes to deploy the containerized application and test prediction functionality in a distributed environment.

7. GitHub Repository and CircleCI: Upload the complete project to a GitHub repository, including CircleCI configuration for automated testing indication.

The successful completion of these tasks will demonstrate proficiency in containerization, Kubernetes deployment, and overall operationalization of a Machine Learning Microservice API.

## Setup the Environment

* Create a virtualenv with Python 3.7 and activate it. Refer to this link for help on specifying the Python version in the virtualenv. 
```bash
python3 -m pip install --user virtualenv
python3 -m virtualenv --python=python3.7.3 .devops
source .devops/bin/activate
```
* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh`

### Setting Up Docker and Kubernetes Locally and Running a Flask App in a Container

1. **Setup and Configure Docker**
   - Go to the Docker Desktop website at https://www.docker.com/products/docker-desktop/ and follow the instructions to install Docker Desktop.
   - Verify the installation by running the following command: `docker --version`.

2. **Setup and Configure Kubernetes**
   - For Windows users, the recommended way is to use Docker Desktop. Open Docker Desktop, go to Settings, navigate to Kubernetes, and check "Enable Kubernetes."
   - Verify the Kubernetes configuration by running: `kubectl version --output json`.

3. **Create Flask App in a Container**
   - Build the Docker image for the Flask app using the following command: `docker build --tag project-ml-kube:v1.0.0 .`
   - Run the container with the created image: `docker run -d --rm -p 8000:80 project-ml-kube:v1.0.0`

4. **Deploy Flask App via Kubernetes**
   - Create an environment file named `.env` that contains your Docker password with the variable `DOCKER_PASSWORD=<your-docker-hub-pw>`, then run: `source .env`.
   - Export your Docker Hub ID using: `export docker_path=<your-docker-hub-id>`.
   - Log in to Docker Hub to push the image: `echo "$DOCKER_PASSWORD" | docker login --username $docker_path --password-stdin`.
   - Tag and push the Docker image to Docker Hub: `docker image tag project-ml-kube:v1.0.0 $docker_path/project-ml-kube:v1.0.0 && docker image push $docker_path/project-ml-kube:v1.0.0`.
   - Create a Kubernetes deployment for the Flask app: `kubectl create deploy project-ml-kube --image="$docker_path/project-ml-kube:v1.0.0"`.
   - Check whether the pod is in the READY state: `kubectl get pods`.
   - Once the pod is ready, forward the port to access the Flask app locally: `kubectl port-forward deployment.apps/project-ml-kube 8000:80`.

### File Descriptions

1. **.dockerignore:** This file is used to specify which files and directories should be ignored during the `COPY` command in the Dockerfile. It helps to reduce the size of the Docker image by excluding unnecessary files.

2. **.env:** This file serves as the environment variable file containing sensitive variables, such as the Docker Hub password. It is used to store configuration data that should not be hardcoded in the code or the Dockerfile.

3. **app.py:** This file contains the API code used for predicting house pricing. It likely includes the logic and endpoints for handling predictions based on input data.

4. **Dockerfile:** The Dockerfile provides instructions to build a Docker image for the application. It includes all the necessary steps to create an environment with the required dependencies and configurations for running the app.

5. **make_prediction.sh:** This script is used to call the API and make predictions for house pricing. It likely sends appropriate requests to the running API and processes the responses.

6. **Makefile:** The Makefile is an instruction file used to automate various tasks related to the project. It typically includes commands for setting up the development environment, installing dependencies, running tests, and performing code linting.

7. **README.md:** This file contains helpful documentation and instructions for understanding and using the project. It often includes setup guidelines, usage examples, and other relevant information.

8. **requirements.txt:** This file lists all the dependencies required to run the project. It is commonly used with Python projects to specify the required packages and their versions.

9. **run_docker.sh:** This script provides a convenient way to run all the necessary steps with Docker. It likely includes commands for building the Docker image, running the container, and exposing the required ports.

10. **run_kubernetes.sh:** Similar to `run_docker.sh`, this script allows running the application with Kubernetes. It includes commands for deploying the Docker image to a Kubernetes cluster and setting up the necessary configurations.

11. **upload_docker.sh:** This script facilitates uploading the Docker image to Docker Hub, which is essential for using the image with Kubernetes. It likely includes commands for tagging and pushing the image to the Docker Hub repository.

These files collectively form the necessary components and configurations to build, deploy, and run the application using Docker and Kubernetes.