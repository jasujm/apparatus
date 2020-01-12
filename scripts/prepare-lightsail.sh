#!/bin/bash

cd

echo 'Installing packages...'
sudo yum update
sudo yum install -y docker git emacs

echo 'Preparing docker...'
sudo usermod -a -G docker ec2-user
docker run --rm hello-world
sudo chkconfig docker on

echo 'Preparing docker-compose...'
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

echo 'Cloning apparatus from GitHub...'
git clone https://github.com/jasujm/apparatus.git

echo 'All set! Checklist:'
echo '- Populate secrets and production settings for docker-compose'
echo '- Run scripts/run-apparatus.sh'
echo '- Run scripts/get-certs.sh'
