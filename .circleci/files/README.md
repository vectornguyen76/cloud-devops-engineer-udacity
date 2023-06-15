### Create Stack Network, SecurityGroup and EC2 Instance
```
aws cloudformation create-stack --stack-name myEC2 --template-body file://ec2.yml  --parameters file://ec2-parameters.json --region us-east-1
```
### Delete Stack 
```
aws cloudformation delete-stack --stack-name myEC2 --region us-east-1
```
```
aws cloudformation delete-stack --stack-name myServer --region us-east-1
```