import requests
import unittest
import pytest

with open("api_key.txt", "r") as file:
    key = file.read()

def get_data(city):
    data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}{key}")
    d = eval(data.text)
    return d

def get_temp(data: dict): # getTemp
  temp = round(float(data.get('main')['temp']) - 273.15, 1)
  return temp

def get_weather(data: dict):
  weather = data.get('weather')[0]['main']
  answer = f"{data.get('name').title()} {weather}"
  return weather

def set_weather_info(city):
        try:
            data = get_data(city)
            print(f"Today's weather in {data['name']} is {get_weather(data)}. The temperature is {get_temp(data)} °C")
        except KeyError as e:
            raise KeyError("Location not found")

def test_weather_wrong_location():
    with pytest.raises(KeyError):
        assert set_weather_info("Egegeg23")
