import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

def get_current_weather():
  print("get current weather for you city...")

  city = input("Please enter your city name: \n")

  weather_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv('WEATHER_APP_KEY')}&q={city}&units=metric"

  weather_data = requests.get(weather_url).json()

  pprint(weather_data)

if __name__ == "__main__":
  get_current_weather()
