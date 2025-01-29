resource "aws_s3_bucket" "weather_data" {
  bucket = var.bucket_name


  tags = {
    Name        = "weather_data"
    Environment = "Dev"
    Project     = "WeatherDataCollection"
  }
}

# resource "aws_s3_bucket_acl" "weather_data_acl" {
#   bucket = aws_s3_bucket.weather_data.id
#   acl    = "private"
# }

resource "aws_s3_bucket_lifecycle_configuration" "weather-bucket" {
  bucket = aws_s3_bucket.weather_data.id

  rule {
    id     = "log"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 60
      storage_class = "GLACIER"
    }

    expiration {
      days = 365
    }
  }
}

resource "aws_s3_bucket" "versioning_bucket" {
  bucket = var.versioning_bucket
}

# resource "aws_s3_bucket_acl" "versioning_bucket_acl" {
#   bucket = aws_s3_bucket.weather_data.id
#   acl    = "private"
# }

resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.versioning_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "versioning_bucket_config" {
  bucket = aws_s3_bucket.versioning_bucket.id

  depends_on = [aws_s3_bucket_versioning.versioning]

  rule {
    id     = "log"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 60
      storage_class = "GLACIER"
    }

    expiration {
      days = 365
    }
  }
}

resource "aws_s3_bucket_public_access_block" "block_public_access" {
  bucket = aws_s3_bucket.weather_data.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
