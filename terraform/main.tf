terraform {
  required_version = ">=0.13.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
backend "s3" {
    bucket         = "galyshko-tf-state"
    key            = "terraform.tfstate"
    region         = "eu-north-1"
    dynamodb_table = "galyshko-tf-lockid"
  }

}

# Configure the AWS provider
provider "aws" {
  region = "eu-north-1"
}

resource "aws_security_group" "web_app" {
  name        = "web_app_unique"
  description = "security group for web application"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "web_app"
  }
}

resource "aws_instance" "webapp_instance" {
  ami           = "ami-0084a47cc718c111a"
  instance_type = "t3.micro"
  vpc_security_group_ids = [aws_security_group.web_app.id]

  user_data = <<-EOF
  #!/bin/bash
  curl -fsSL https://get.docker.com -o get-docker.sh
  sudo sh get-docker.sh
  sudo groupadd docker
  sudo usermod -aG docker ubuntu
  newgrp docker
  docker pull sergoo/notebook_queue_app:latest
  docker run -id sergoo/notebook_queue_app:latest
  EOF



  tags = {
    Name = "webapp_instance"
  }
}



output "instance_public_ip" {
  value     = aws_instance.webapp_instance.public_ip
  sensitive = true
}