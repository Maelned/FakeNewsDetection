provider "aws" {
  region = "eu-west-1"
}

resource "aws_instance" "mlflow_instance" {
  ami           = "ami-0d3a2960fcac852bc"
  instance_type = "t3.micro"

  # User data script to install MLflow and necessary dependencies
  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install -y python3-pip
              pip3 install mlflow[extras]
              nohup mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root s3://your-bucket-name/mlflow/ --host 0.0.0.0 &
              EOF

  tags = {
    Name = "MLFlowInstance"
  }

  security_groups = [aws_security_group.mlflow_sg.name]
}

resource "aws_security_group" "mlflow_sg" {
  name        = "mlflow_sg"
  description = "Allow access to MLflow server"

  ingress {
    from_port   = 5000
    to_port     = 5000
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

resource "aws_s3_bucket" "mlflow_bucket" {
  bucket = "your-bucket-name"
  acl    = "private"
}
