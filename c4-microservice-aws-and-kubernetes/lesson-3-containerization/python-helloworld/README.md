# Exercise - Creating an EKS Cluster and Deploying an App - CLI
Before we move further, note that there are multiple ways to create/delete an AWS EKS cluster, such as:

- EKS web-console
- CloudFormation console
- EKSCTL utility - Recommended way

## Create an EKS Cluster using the EKSCTL utility
1. Create command
    Let's use eksctl and kubectl utilities to create a Kubernetes cluster in the AWS EKS. Run the following command to create the EKS cluster:
    ```
    eksctl create cluster --name eksctl-demo --region=us-east-1 [--profile <profile-name>]
    ```
2. View progress
    Go to the CloudFormation console to view progress. If you don’t see any progress, be sure that you are viewing clusters in the same region that they are being created. For example, if eksctl is using region us-east-1, you’ll need to set the region to US East (Ohio) in the dropdown menu in the upper right of the console.
    In case of issues, you can try:
    ```
    eksctl utils describe-stacks --region=us-east-1 --cluster=eksctl-demo [--profile <profile-name>]
    ```

    <p align="center">
    <img src="https://video.udacity-data.com/topher/2021/May/609913fe_screenshot-2021-05-10-at-4.37.10-pm/screenshot-2021-05-10-at-4.37.10-pm.png" alt="animated" />
    </p>
    <p align="center">Verify the region shown in the command line</p>

3. View details
    Once the status is CREATE_COMPLETE in the CloudFormation web-console, fetching the details of the newly created cluster using:
    ```
    eksctl get cluster --name=eksctl-demo --region=us-east-1 [--profile <profile-name>]
    ```
4. Deploy a Sample App
- Ensure Docker Desktop is running locally
    ```
    docker --version
    ```
- Build an image using the Dockerfile in the current directory
    ```
    docker build -t python-helloworld .
    docker images
    ```
- Run a container
    ```
    docker run -d -p 5000:5000 python-helloworld
    ```
- Check the output at http://localhost:5000/ or http://0.0.0.0:5000/ or http://127.0.0.1:5000/
    ```
    docker ps
    ```
- Now, stop the container.
- Tag locally before pushing to the Dockerhub
- We have used a sample Dockerhub profile /vectornguyen76
- Replace vectornguyen76/ with your Dockerhub profile
    ```
    docker tag python-helloworld vectornguyen76/python-helloworld:v1.0.0
    docker images
    ```
- Log into the Dockerhub from your local terminal
    ```
    docker login
    ```
- Replace vectornguyen76/ with your Dockerhub profile
    ```
    docker push vectornguyen76/python-helloworld:v1.0.0
    ```
- Check the image in your Dockerhub online at https://hub.docker.com/repository/docker/vectornguyen76/python-helloworld

Once your Docker image is publicly available, you can deploy it to the kubernetes cluster.

- Assuming the Kubernetes cluster is ready
    ```
    kubectl get nodes
    ```
- Deploy an App from the Dockerhub to the Kubernetes Cluster
    ```
    kubectl create deploy python-helloworld --image=vectornguyen76/python-helloworld:v1.0.0
    ```
- See the status
    ```
    kubectl get deploy,rs,svc,pods
    ```
- Port forward 
    ```
    kubectl port-forward pod/python-helloworld-849d85c778-jrh6l --address 0.0.0.0 5000:5000
    ```

- Access the app locally at http://127.0.0.1:5000/
    <p align="center">
    <img src="https://video.udacity-data.com/topher/2022/January/61ea9c9a_screenshot-2022-01-21-at-5.09.52-pm/screenshot-2022-01-21-at-5.09.52-pm.png" alt="animated" />
    </p>
    <p align="center">Deploying an App to the Kubernetes cluster</p>

    <p align="center">
    <img src="https://video.udacity-data.com/topher/2022/January/61ea9c73_screenshot-2022-01-21-at-5.13.34-pm/screenshot-2022-01-21-at-5.13.34-pm.png" alt="animated" />
    </p>
    <p align="center">View the output in your local browser at http://127.0.0.1:5000/</p>

5. Delete the cluster
    You can delete the cluster either from the CloudFormation web-console, or by using the EKSCTL command. Choose any one option from below:

    - From the CloudFormation web-console, select your stack and choose delete from the actions menu
    - Delete using the EKSCTL:
    ```
    eksctl delete cluster --region=us-east-1 --name=eksctl-demo [--profile <profile-name>]
    ```