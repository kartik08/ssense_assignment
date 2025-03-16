resource "aws_lambda_function" "kinesis_consumer" {
  function_name = "FraudDetectionConsumer"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
  role          = aws_iam_role.lambda_role.arn
  filename      =  "lambda_artifacts/lambda_function.zip"
  environment {
    variables = {
      KINESIS_STREAM_NAME = aws_kinesis_stream.transaction_stream.name
      S3_BUCKET_NAME = aws_s3_bucket.fraud_data.bucket
    }
  }
}
resource "aws_lambda_event_source_mapping" "kinesis_trigger" {
  event_source_arn  = aws_kinesis_stream.transaction_stream.arn
  function_name     = aws_lambda_function.kinesis_consumer.arn
  starting_position = "TRIM_HORIZON"
}