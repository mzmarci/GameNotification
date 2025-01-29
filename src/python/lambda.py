import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        self.topic_arn = os.getenv('SNS_TOPIC_ARN')
        self.s3_client = boto3.client('s3')
        self.sns_client = boto3.client('sns')

    def create_bucket_if_not_exists(self):
        """Create S3 bucket if it doesn't exist."""
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} exists.")
        except:
            print(f"Creating bucket {self.bucket_name}...")
            try:
                self.s3_client.create_bucket(Bucket=self.bucket_name)
                print(f"Successfully created bucket {self.bucket_name}.")
            except Exception as e:
                print(f"Error creating bucket: {e}")
                raise

    def fetch_weather(self, city):
        """Fetch weather data from OpenWeather API."""
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "imperial"
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def save_to_s3(self, weather_data, city):
        """Save weather data to S3 bucket with a unique filename if needed."""
        if not weather_data:
            return False

        base_file_name = f"{city}_weather.json"
        file_name = base_file_name
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        try:
            self.s3_client.head_object(Bucket=self.bucket_name, Key=base_file_name)
            # File exists; create a unique filename
            file_name = f"{city}_weather_{timestamp}.json"
        except self.s3_client.exceptions.ClientError as e:
            if e.response['Error']['Code'] != '404':
                raise

        try:
            weather_data['timestamp'] = timestamp
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(weather_data),
                ContentType='application/json'
            )
            print(f"Successfully saved data for {city} to S3 as {file_name}.")
            return file_name
        except Exception as e:
            print(f"Error saving to S3: {e}")
            return None

    def send_sns_notification(self, city, file_name):
        """Send an SNS notification about the saved weather data."""
        try:
            message = f"Weather data for {city} has been saved to S3 as {file_name}."
            self.sns_client.publish(
                TopicArn=self.topic_arn,
                Message=message,
                Subject="Weather Data Update"
            )
            print(f"Notification sent for {city}: {file_name}.")
        except Exception as e:
            print(f"Error sending notification: {e}")

    def process_city(self, city):
        """Fetch, save, and notify weather data for a specific city."""
        print(f"\nProcessing weather data for {city}...")
        weather_data = self.fetch_weather(city)
        if weather_data:
            file_name = self.save_to_s3(weather_data, city)
            if file_name:
                self.send_sns_notification(city, file_name)
        else:
            print(f"Failed to fetch weather data for {city}.")

def lambda_handler(event, context):
    """Lambda function handler."""
    dashboard = WeatherDashboard()
    dashboard.create_bucket_if_not_exists()

    # Replace with cities of your choice or retrieve from event/context
    cities = ["Philadelphia", "Seattle", "New York", "Nigeria", "London"]

    for city in cities:
        dashboard.process_city(city)

if __name__ == "__main__":
    # Local execution
    lambda_handler(None, None)






# import os
# import json
# import boto3
# import requests
# from datetime import datetime
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# class WeatherDashboard:
#     def __init__(self):
#         self.api_key = os.getenv('OPENWEATHER_API_KEY')
#         self.bucket_name = os.getenv('AWS_BUCKET_NAME')
#         self.s3_client = boto3.client('s3')

#     def create_bucket_if_not_exists(self):
#         """Create S3 bucket if it doesn't exist"""
#         try:
#             self.s3_client.head_bucket(Bucket=self.bucket_name)
#             print(f"Bucket {self.bucket_name} exists")
#         except:
#             print(f"Creating bucket {self.bucket_name}")
#         try:
#             # Simpler creation for us-east-1
#             self.s3_client.create_bucket(Bucket=self.bucket_name)
#             print(f"Successfully created bucket {self.bucket_name}")
#         except Exception as e:
#             print(f"Error creating bucket: {e}")

#     def fetch_weather(self, city):
#         """Fetch weather data from OpenWeather API"""
#         base_url = "http://api.openweathermap.org/data/2.5/weather"
#         params = {
#             "q": city,
#             "appid": self.api_key,
#             "units": "imperial"
#         }
        
#         try:
#             response = requests.get(base_url, params=params)
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching weather data: {e}")
#             return None

#     def save_to_s3(self, weather_data, city):
#         """Save weather data to S3 bucket"""
#         if not weather_data:
#             return False
            
#         timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
#         file_name = f"weather-data/{city}-{timestamp}.json"
        
#         try:
#             weather_data['timestamp'] = timestamp
#             self.s3_client.put_object(
#                 Bucket=self.bucket_name,
#                 Key=file_name,
#                 Body=json.dumps(weather_data),
#                 ContentType='application/json'
#             )
#             print(f"Successfully saved data for {city} to S3")
#             return True
#         except Exception as e:
#             print(f"Error saving to S3: {e}")
#             return False

# def main():
#     dashboard = WeatherDashboard()
    
#     # Create bucket if needed
#     dashboard.create_bucket_if_not_exists()
    
#     cities = ["Philadelphia", "Seattle", "New York", "Nigeria"]
    
#     for city in cities:
#         print(f"\nFetching weather for {city}...")
#         weather_data = dashboard.fetch_weather(city)
#         if weather_data:
#             temp = weather_data['main']['temp']
#             feels_like = weather_data['main']['feels_like']
#             humidity = weather_data['main']['humidity']
#             description = weather_data['weather'][0]['description']
            
#             print(f"Temperature: {temp}°F")
#             print(f"Feels like: {feels_like}°F")
#             print(f"Humidity: {humidity}%")
#             print(f"Conditions: {description}")
            
#             # Save to S3
#             success = dashboard.save_to_s3(weather_data, city)
#             if success:
#                 print(f"Weather data for {city} saved to S3!")
#         else:
#             print(f"Failed to fetch weather data for {city}")

# if __name__ == "__main__":
#     main()