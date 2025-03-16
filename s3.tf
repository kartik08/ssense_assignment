resource "aws_s3_bucket" "fraud_data" {
  bucket = "fraud-detection-data-kartik"
  acl    = "private"
}
resource "aws_s3_bucket_policy" "fraud_data_policy" {
  bucket = aws_s3_bucket.fraud_data.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Deny",
        Principal = "*",
        Action = "s3:*",
        Resource = [
          "${aws_s3_bucket.fraud_data.arn}/*",
          "${aws_s3_bucket.fraud_data.arn}"
        ],
        Condition = {
          Bool = {
            "aws:SecureTransport": "false"
          }
        }
      },
      {
        Effect = "Allow",
        Principal = {
          AWS = aws_iam_role.lambda_role.arn 
        },
        Action = ["s3:Get*", "s3:Put*"],
        Resource = "${aws_s3_bucket.fraud_data.arn}/*"
      }
    ]
  })
}