import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("weather_api")

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code != 200:
    print("Error:", data.get("message"))


# print(json.dumps(data, indent=4))

print(f"Todays weather of {city}:")
print(f"Weather: {data['weather'][0]['main']} ({data['weather'][0]['description']})")
print(f"Temperature: {data["main"]["temp"]}")