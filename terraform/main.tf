provider "aws" {
  region = "us-east-1" # Change to your desired region
}

resource "aws_instance" "ml_instance" {
  ami           = "ami-0c55b159cbfafe1f0" # Specify your desired AMI
  instance_type = "t2.micro" # Change to instance type suitable for your workload
  tags = {
    Name = "MLInstance"
  }
}

resource "aws_s3_bucket" "ml_data_bucket" {
  bucket_prefix = "ml-data-bucket"
  acl           = "private"
}

# Add more resources as needed, e.g., IAM roles, security groups, etc.
