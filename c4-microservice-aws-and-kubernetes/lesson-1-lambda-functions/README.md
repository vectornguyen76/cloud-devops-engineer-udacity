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
```
sam init
```
5. Build the Hello World application
```
# Check the [Application-name]/README file instructions
cd [Application-name]
sam build
```
6. Run the application locally (in Cloud9)
```
sam local invoke
```
The command will build the image locally, and run the container.
7. Deploy the application to an ECR image repository
```
# Create a cloudformation stack to deploy the application image in the ECR image repository
sam deploy --guided
```
8. Test: After successful execution, it will generate an API gateway endpoint URL that you can curl or paste in a browser tab to see the function output.
```
curl [API gateway endpoint URL]
```