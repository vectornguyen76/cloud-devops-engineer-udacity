These tutorials assume you are operating within an AWS [Cloud9 environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial-lambda.html), which allows you to easily create and deploy lambda functions.

## Set up deploy HelloWorldLambda in Cloud9
1. Allow Cloud9 to access the Github repo:
    ```shell
    # Generate a pair of SSH keys, if you want your Cloud9 env to be able to push changes to the Github repo
    ssh-keygen -t rsa
    # View the contents of the public key
    cat /home/ec2-user/.ssh/id_rsa.pub
    ```
    Open the Github repo https://github.com/udacityOpen the Github repo https://github.com/vectornguyen76/cloud-devops-engineer-udacity in a separate browser tab, and fork it into your account.Save the public key, content of /home/ec2-user/.ssh/id_rsa.pub file, in the Github >> Settings >> SSH & GPG keys./DevOps_Microservices in a separate browser tab, and fork it into your account.Save the public key, content of /home/ec2-user/.ssh/id_rsa.pub file, in the Github >> Settings >> SSH & GPG keys.
2. Clone the forked repo into the Cloud9 environment using:
    ```
    git clone git@github.com:vectornguyen76/cloud-devops-engineer-udacity.git
    ```
3. [Optional] Increase the Cloud9 memory limits: Run the resize.sh script present in this folder to increase the Cloud9 available-memory limits.
    ```shell
    cd cloud-devops-engineer-udacity/c4-microservice-aws-and-kubernetes/supporting-material
    # The instructor shows `cd awslambda` per hierarchy of his personal repo
    df -h
    chmod +x resize.sh
    ./resize.sh 
    df -h
    cd ..
    ```
4. Initialize a new Lambda function
    ```shell
    sam init
    ```
    <p align="center">
    <img src="https://video.udacity-data.com/topher/2021/November/61a61e9e_screenshot-2021-11-30-at-6.01.40-pm/screenshot-2021-11-30-at-6.01.40-pm.png" alt="animated" />
    </p>
    <p align="center">Prompts after executing the sam init command</p>

    <p align="center">
    <img src="https://video.udacity-data.com/topher/2021/November/61a61e09_screenshot-2021-11-30-at-6.03.55-pm/screenshot-2021-11-30-at-6.03.55-pm.png" alt="animated" />
    </p>
    <p align="center">Lambda function created after running the sam init command successfully.
    Change the directory to view the new files.</p>

5. Build the Hello World application
    ```shell
    # Check the [Application-name]/README file instructions
    cd [Application-name]
    sam build
    ```
6. Run the application locally (in Cloud9)
    ```shell
    sam local invoke
    ```
    The command will build the image locally, and run the container.
7. Deploy the application to an ECR image repository
    ```shell
    # Create a cloudformation stack to deploy the application image in the ECR image repository
    sam deploy --guided
    ```
    Provide responses the the prompts that appear next. Note: AWS has updated the behavior of this command to create an image repository in the ECR service automatically, if not already available. This command will push the the Docker image from local (Cloud9) to the ECR service.
    <p align="center">
    <img src="https://video.udacity-data.com/topher/2021/November/61a61e74_screenshot-2021-11-30-at-6.11.31-pm/screenshot-2021-11-30-at-6.11.31-pm.png" alt="animated" />
    </p>
    <p align="center">Prompts that appear after running the sam deploy --guided command</p>

    <p align="center">
    <img src="https://video.udacity-data.com/topher/2021/November/61a61f01_screenshot-2021-11-30-at-6.16.02-pm/screenshot-2021-11-30-at-6.16.02-pm.png" alt="animated" />
    </p>
    <p align="center">The sam deploy --guided command will create a Cloudformation stack comprising of an IAM role, Lambda function, and an API Gateway.</p>

8. Test: After successful execution, it will generate an API gateway endpoint URL that you can curl or paste in a browser tab to see the function output.
    ```shell
    curl [API gateway endpoint URL]
    ```
    <p align="center">
    <img src="https://video.udacity-data.com/topher/2021/November/61a61fe4_screenshot-2021-11-30-at-6.27.05-pm/screenshot-2021-11-30-at-6.27.05-pm.png" alt="animated" />
    </p>
    <p align="center">curl the API Gateway endpoint URL</p>