from curses import termattrs
import requests

API_KEY = "c0a1b1f57b5b9b585b0f91867cb9961a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# get user city
city = input("Enter a city: ") 
# request url and check response
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

# check satus of repond
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"], 2)

    # convert kelvin to fahrenheight
    temperature_fahrenheight = round((temperature - 273.15) * (9/5) + 32, 2)

    # weather output
    print("Weather: ", weather)
    print("Temperature: ", temperature_fahrenheight, "Fahrenheight")
else:
    print("An error occurred. ")