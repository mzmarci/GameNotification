# WEATHER NOTIFICATION

# Weather Data Collection System

## Overview
This project is an automated weather data collection system that fetches weather data from the **OpenWeather API**, stores it in an **AWS S3 bucket**, and sends **email and SMS notifications** via **AWS SNS**. The system is triggered periodically using **AWS EventBridge** and runs serverless using **AWS Lambda**.

## Features
- Fetches weather data using OpenWeather API
- Stores weather data in an AWS S3 bucket
- Sends email and SMS notifications using AWS SNS
- Uses AWS Lambda for execution
- Automates execution via AWS EventBridge
- Deployable with **Terraform**

---

## **Architecture Diagram**


---

## **Technologies Used**
- **AWS Lambda** - Serverless compute for fetching weather data
- **AWS S3** - Storage for weather data
- **AWS EventBridge** - Scheduler for periodic execution
- **AWS SNS** - Notification service for SMS and email alerts
- **Terraform** - Infrastructure as Code for deployment
- **Python** - Weather data processing
- **OpenWeather API** - External API for weather data

---

## **Prerequisites**
1. **AWS Account** with permissions for Lambda, S3, SNS, and EventBridge
2. **Terraform Installed** ([Install Terraform](https://developer.hashicorp.com/terraform/downloads))
3. **OpenWeather API Key** ([Get API Key](https://home.openweathermap.org/api_keys))
4. **AWS CLI Installed & Configured** ([AWS CLI Setup](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html))

---

## **Setup Instructions**

STEPS ON HOW THE PROJECT WILL BE
1. Created the backend, s3 bucket, sns notification, lambda and eventbridge through terraform

2. Install Dependencies Locally
Run the following command to install the dependencies into a python directory:
pip install -r requirements.txt -t python/
This creates a folder python/ containing all the required dependencies.
Note: if you have issues installing pip on your terminal, then do the following:
-- Run:curl -O https://bootstrap.pypa.io/get-pip.py
-- Execute the script: python get-pip.py
-- Verify if PIP is installed: pip --version

3. Add Your lambda.py
Move lambda.py into the python/ directory:

4. Configure Environment Variables
Create a .env file (or use Terraform variables):
AWS_BUCKET_NAME="your-s3-bucket-name"
OPENWEATHER_API_KEY="your-api-key"
AWS_REGION="us-east-1"
SNS_TOPIC_ARN="your-sns-topic-arn"

## Deployment Using Terraform
1. Initialize Terraform : terraform init
2. Terraform plan
3. Terraform apply -auto-approve

Terraform will:

1. Create an S3 bucket
2. Deploy an AWS Lambda function
3. Configure AWS EventBridge for scheduling
4. Set up AWS SNS for notifications

# Test the Setup

# Check S3 for Weather Data
1. Go to the AWS S3 console
2. Verify that weather data files are stored in the specified bucket.

# Check Notifications
Ensure email/SMS notifications are received from AWS SNS.

# Cleanup
To destroy all AWS resources:  terraform destroy -auto-approve

# Troubleshooting
Issue	                                                                 Solution
Lambda function fails                                      	Check CloudWatch logs for errors
No notifications received	                                Verify SNS topic subscription
No data in S3	                                            Ensure API key is correct and S3 bucket exists

# License
This project is licensed under the MIT License.
---

## **Why This README?**
- **Clear structure**: Easy to follow installation, deployment, and troubleshooting.
- **Beginner-friendly**: Even someone new to AWS can set it up.
- **Comprehensive**: Covers prerequisites, Terraform setup, testing, and cleanup.

Let me know if you need modifications! 🚀


