output "mlflow_instance_public_ip" {
  value = aws_instance.mlflow_instance.public_ip
}
