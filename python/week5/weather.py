import requests

# get user's location by asking them
city= input("Where are you located? (e.g. Halifax)\n")

# API for the weather: open-weather: https://openweathermap.org/current
# However, here I am using Geocoding API from above to get weather by city
# Geocoding API: https://openweathermap.org/api/geocoding-api
# for key you'll have to sign up
API_KEY = "67da29cb91129f1a68c1c06c1be92daa"
URI = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
response = requests.get(URI)

# convert this response to proper JSON format using online formatter to have an idea
# online tool: https://codebeautify.org/jsviewer
# this tool gave me prettier JSON, I will take - lat, long - from that to query the weather
latitude, longitude = response.json()[0].get("lat"), response.json()[0].get("lon")
# get response from weather app now
URI = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
response = requests.get(URI)

print(f"Thank you. Weather in {city}:")
print(f'{response.json().get("weather")[0].get("description")}')

# convert the temperature from metric system (Kelvin) to celcius
min = response.json().get("main").get("temp_min") - 273.15
max = response.json().get("main").get("temp_max") - 273.15
print(f"Min temp: {min:.2f} *c\nMax temp: {max:.2f} *c")
