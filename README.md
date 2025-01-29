# GameNotification

This project is an alert system that sends real-time NBA game day score notifications to subscribed users via SMS/Email. It leverages Amazon SNS, AWS Lambda and Python, Amazon EvenBridge and NBA APIs to provide sports fans with up-to-date game information. The project demonstrates cloud computing principles and efficient notification mechanisms.

Project Overview
This project is a Weather Data Collection System that demonstrates core DevOps principles by combining:

External API Integration (OpenWeather API)
Cloud Storage (AWS S3)
Infrastructure as Code
Version Control (Git)
Python Development
Error Handling
Environment Management
Fetches real-time weather data for multiple cities
Displays temperature (°F), humidity, and weather conditions
Automatically stores weather data in AWS S3
Supports multiple cities tracking
Timestamps all data for historical tracking

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
