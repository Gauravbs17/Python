import json
with open('weather_json.json')as f:
    data=json.load(f)
#Extract file required weather data
current_temp=data['main']['temp']
humidity=data['main']['humidity']
weather_desc=data['weather'][0]['description']
#display the weather data
print(f"Current temperature:{current_temp}°C")
print(f"Humidity:{humidity}%")
print(f"Weather description:{weather_desc}")
