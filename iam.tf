resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"
  assume_role_policy = jsonencode({
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_policy" "lambda_cloudwatch" {
  name        = "LambdaCloudWatchPolicy"
  description = "IAM policy for Lambda to access Cloudwatch"
  policy      = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = "arn:aws:logs:ca-central-1:279754971650:*"
      }
    ]
  })
}

resource "aws_iam_policy" "lambda_kinesis" {
     name        = "LambdaKinesisPolicy"
     description = "IAM policy for Lambda to access Kinesis"
     policy      = jsonencode({
     Version = "2012-10-17",
     Statement = [
      {
        Effect = "Allow",
        Action = [
          "kinesis:Subscribe*",
          "kinesis:Get*",
          "kinesis:List*",
          "kinesis:Describe*"
        ],
        Resource = aws_kinesis_stream.transaction_stream.arn
      }
    ]
  })
}

resource "aws_iam_policy" "lambda_s3" {
     name        = "LambdaS3Policy"
     description = "IAM policy for Lambda to access S3"
     policy      = jsonencode({
     Version = "2012-10-17",
     Statement = [
      {
        Effect = "Allow",
        Action = [
          "s3:*",
        ],
        Resource = "${aws_s3_bucket.fraud_data.arn}/*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment_s3" {
  policy_arn = aws_iam_policy.lambda_s3.arn
  role = aws_iam_role.lambda_role.name
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment_cloudwatch" {
    policy_arn = aws_iam_policy.lambda_cloudwatch.arn
    role = aws_iam_role.lambda_role.name
  
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment_kinesis" {
    policy_arn = aws_iam_policy.lambda_kinesis.arn
    role = aws_iam_role.lambda_role.name
}