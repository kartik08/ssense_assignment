resource "aws_kinesis_stream" "transaction_stream" {
  name             = "fraud-detection-stream"
  retention_period = 24
   stream_mode_details {
    stream_mode = "ON_DEMAND"
  }
  tags = {
    Environment = "test"
  }
}