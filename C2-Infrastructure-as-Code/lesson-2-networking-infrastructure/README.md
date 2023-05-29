# Challenge 2 
## Project Overview
You have been tasked with creating the required Infrastructure-as-code scripts for a new cloud environment in AWS. The Lead Solutions Architect for the project sends you the following diagram.
<p align="center">
  <img src="./resource/overview.png" alt="animated" />
</p>

## ToDo
Write a CloudFormation script that:
- Creates a VPC. It will accept the IP Range -also known as CIDR block- from an input parameter
- Creates and attaches an Internet Gateway to the VPC
- Creates Two Subnets within the VPC with Name Tags to call them “Public” and “Private”. These will also need input parameters for their ranges, just like the VPC.
- The Subnet called “Public” needs to have a NAT Gateway deployed in it. This will require you to allocate an Elastic IP that you can then use to assign it to the NAT Gateway.
- The Public Subnet needs to have the MapPublicIpOnLaunch property set to true. Use this reference for help.
- The Private Subnet needs to have the MapPublicIpOnLaunch property set to false.
- Both subnets need to be /24 in size. If you need assistance with IP math, you can use a subnet calculator such as this one.
- You will need 2 Routing Tables, one named Public and the other one Private
- Assign the Public and Private Subnets to their corresponding Routing table
- Create a Route in the Public Route Table to send default traffic ( 0.0.0.0/0 ) to the Internet Gateway you created
- Create a Route in the Private Route Table to send default traffic ( 0.0.0.0/0 ) to the NAT Gateway
- Finally, once you execute this CloudFormation script, you should be able to delete it and create it again, over and over in a predictable and repeatable manner, this is the true verification of working Infrastructure-as-Code

## Helpful hints:
The numbers in the diagram below show the recommended sequence for resource creation. This is not required by CloudFormation but it helps to keep you on track and allows you to stop and verify as you go.
<p align="center">
  <img src="./resource/Helpful1.png" alt="animated" />
</p>

<p align="center">
  <img src="./resource/Helpful2.png" alt="animated" />
</p>

## Usage
### Create
Create Stack Network
```
aws cloudformation create-stack --stack-name myNetwork --template-body file://network.yml --parameters file://network-parameters.json --region us-east-1
```
### Delete 
Delete Stack Network
```
aws cloudformation delete-stack --stack-name myNetwork --region us-east-1
```
## Output
The stack details should show you the list of resources created successfully:
<p align="center">
  <img src="./resource/Output.jpg" alt="animated" />
</p>
