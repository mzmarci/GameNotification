resource "aws_iam_role" "lambda_execution_role" {
  name_prefix = "lambda_execution_role_"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action    = "sts:AssumeRole",
        Effect    = "Allow",
        Principal = { Service = "lambda.amazonaws.com" }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_execution_policy" {
  role       = aws_iam_role.lambda_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "weather_data_collector" {
  filename         = "${path.module}/lambda_function.zip" # Path to the zipped file
  function_name    = "FetchWeatherData"
  role             = aws_iam_role.lambda_execution_role.arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.9"
  source_code_hash = filebase64sha256("${path.module}/lambda_function.zip")

  environment {
    variables = {
      AWS_BUCKET_NAME     = aws_s3_bucket.weather_data.id
      OPENWEATHER_API_KEY = "*****" # Replace with your actual API key
      SNS_TOPIC_ARN       = aws_sns_topic.weather_notifications.arn
    }
  }
}



# resource "aws_eventbridge_rule" "schedule_rule" {
#   name                = "FetchWeatherDataRule"
#   schedule_expression = "rate(1 hour)" # Adjust schedule as needed
# }

# resource "aws_lambda_permission" "allow_eventbridge" {
#   statement_id  = "AllowExecutionFromEventBridge"
#   action        = "lambda:InvokeFunction"
#   function_name = aws_lambda_function.weather_data_collector.function_name
#   principal     = "events.amazonaws.com"
#   source_arn    = aws_eventbridge_rule.schedule_rule.arn
# }

# resource "aws_eventbridge_target" "lambda_target" {
#   rule      = aws_eventbridge_rule.schedule_rule.name
#   target_id = "FetchWeatherData"
#   arn       = aws_lambda_function.weather_data_collector.arn
# }

# resource "aws_s3_bucket" "weather_data" {
#   bucket = var.bucket_name # Replace with your bucket name
# }

# resource "aws_sns_topic" "weather_notifications" {
#   name = "WeatherNotifications"
# }
