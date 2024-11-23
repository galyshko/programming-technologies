terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
  required_version = ">= 1.0.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "web_app" {
  name        = "web_app_sg"
  description = "Allow HTTP and SSH"

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
}

resource "aws_instance" "webapp_instance" {
   ami           = "ami-06b21ccaeff8cd686"
  instance_type = "t2.micro"

  security_groups = [aws_security_group.web_app.name]

  tags = {
    Name = "web_app_instance"
  }
}

output "instance_public_ip" {
  value = aws_instance.webapp_instance.public_ip
}
