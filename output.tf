output "kinesis_arn" {
  value = aws_kinesis_stream.transaction_stream.arn
}
output "lambda_exec_role"{
    value = aws_iam_role.lambda_role.arn
}