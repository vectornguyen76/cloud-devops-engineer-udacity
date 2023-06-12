# Install Ansible
pip install --user ansible

https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

### Build an Ansible Inventory File
Script to Create the Initial Inventory File
```
echo "[all]" > inventory
```
Script to Query EC2 for Instances and Output to File
```
aws ec2 describe-instances --query 'Reservations[*].Instances[*].PublicIpAddress' --output text >> inventory
```

aws ec2 describe-instances --query 'Reservations[*].Instances[*].PublicIpAddress' --filters "Name=tag:Project,Values=udacity" --output text >> inventory

ansible-playbook -i inventory main.yml --private-key=my-keypair.pem