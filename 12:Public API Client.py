# The Challenge: Use a free public API (like the OpenWeatherMap API or The Movie Database API) 
# to fetch data. For example, ask the user for a city and display the current weather.

# Step 0: The "Developer" Setup - Getting Your API Key

# Step 1: Making Your First API Call

"""
import requests

api_key = '77ff3b34261236b28febbc581d937b5a'
url = 'https://api.openweathermap.org/data/2.5/weather?'
params = {
  'lat': 44.34,
  'lon': 10.99,
  'appid':api_key
}
response = requests.get(url, params=params)
# print(response.text)

x = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=77ff3b34261236b28febbc581d937b5a')
# print(x.status_code)
"""

# Step 2: Parsing the JSON and Extracting Data
"""
import requests

api_key = '77ff3b34261236b28febbc581d937b5a'
units = 'metric'
url = 'https://api.openweathermap.org/data/2.5/weather?'
params = {
  'lat': 44.34,
  'lon': 10.99,
  'appid':api_key,
  'units':units
}
response = requests.get(url, params=params)
# print(response.text)
# x = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=77ff3b34261236b28febbc581d937b5a')
x = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=77ff3b34261236b28febbc581d937b5a&units=metric')
# print(x.status_code)

# print(response.json())
API_Data = response.json()
#for key in API_Data:{
#    print(key,":", API_Data[key])
#}

weather = API_Data["weather"]
# print(weather)

temp = API_Data["main"]["temp"]
# print(temp)
"""

# Step 3: Building the Interactive Application

import requests

api_key = '77ff3b34261236b28febbc581d937b5a'
# city_name = 'London'
units = 'metric'
url = 'https://api.openweathermap.org/data/2.5/weather?'
params = {
  'lat': 44.34,
  'lon': 10.99,
  'appid':api_key,
  'units':units,
#  'q':city_name
}
response = requests.get(url, params=params)
# print(response.text)
# x = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=77ff3b34261236b28febbc581d937b5a')
x = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=77ff3b34261236b28febbc581d937b5a&units=metric')
# print(x.status_code)

# print(response.json())
API_Data = response.json()
#for key in API_Data:{
#    print(key,":", API_Data[key])
#}

# weather = API_Data["weather"]
# print(weather)

# temp = API_Data["main"]["temp"]
# print(temp)

while True:
    city_name = input("Which city do you want the data for (Or to exit type 'q')? ")
    if city_name.lower() == 'q':
        break
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={units}')
    # print(response.json())
    if response.status_code != 200:
        print(f"Error: Could not recieve data for {city_name}, Try Again!")
        continue
    try:
        API_Data = response.json()
        description = API_Data['weather'][0]['description']
        temp = API_Data['main']['temp']
        feels_like = API_Data['main']['feels_like']

        print(f"--- Weather in {city_name} ---")
        print(f"Description: {API_Data["weather"][0]["description"]}")
        print(f"Current Temperature: {API_Data["main"]["temp"]}")
        print(f"Feels Like: {API_Data["main"]["feels_like"]}")

    except KeyError:
        print(f"Error: Cannot locate the weather for {city_name}")
