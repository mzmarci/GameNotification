resource "aws_sns_topic" "weather_notifications" {
  name = "WeatherNotifications"
}

resource "aws_sns_topic_subscription" "email_subscription" {
  topic_arn = aws_sns_topic.weather_notifications.arn
  protocol  = "email"
  endpoint  = var.email_address # Replace with your email
}

resource "aws_sns_topic_subscription" "sms_subscription" {
  topic_arn = aws_sns_topic.weather_notifications.arn
  protocol  = "sms"
  endpoint  = var.sms_notification # Replace with your phone number
}
