import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

def get_current_weather(city="abuja"):
  

  weather_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv('WEATHER_APP_KEY')}&q={city}&units=metric"

  weather_data = requests.get(weather_url).json()

  return weather_data

if __name__ == "__main__":
  print("get current weather for you city...")

  city = input("Please enter your city name: \n")

  if not bool(city.strip()):
    city="abuja"

  weather_condition = get_current_weather(city)
  pprint(weather_condition)