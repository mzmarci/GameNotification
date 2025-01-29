variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
  default     = "weather-data-collection-bucket"
}

variable "versioning_bucket" {
  description = "Key versioning for S3 bucket"
  default     = "key-versioning-bucket"
}

variable "email_address" {
  description = "Email address for SNS subscription"
  default     = "****"
}

variable "sms_notification" {
  description = "SMS notification for SNS subscription"
  default     = "****"
}



