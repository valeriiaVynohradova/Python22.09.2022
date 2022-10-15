#  завдання 1
#  урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в
# режимі реального часу)
import requests
#print('All these astronauts are in orbit right now: ')
#url = 'http://api.open-notify.org/astros.json'
#response = requests.get(url)
#response_json = response.json()
#in_orbit = response_json['people']
#for astronauts in in_orbit:
    #print(astronauts['name'])

# завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv, london)
# результатом буде приблизно такий результат
# {"coord":{"lon":30.7326,"lat":46.4775},"weather":[{"id":803,"main":"Clouds","description":"broken clouds",
# "icon":"04n"}],"base":"stations","main":{"temp":13.94,"feels_like":12.8,"temp_min":13.94,"temp_max":13.94,
# "pressure":1021,"humidity":54,"sea_level":1021,"grnd_level":1015},"visibility":10000,"wind":{"speed":4.58,"deg":314,
# "gust":8.16},"clouds":{"all":73},"dt":1664909335,"sys":{"country":"UA","sunrise":1664855942,"sunset":1664897549},
# "timezone":10800,"id":698740,"name":"Odesa","cod":200}
# погода змінюється, як і місто. яке ви введете
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране


#app_id = '47503e85fabbabc93cff28c52398ae97'
#url_weather = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={app_id}&units=metric'
#city_name = input('Please, enter the city: ')
#response = requests.get(url_weather)
#weather = response.json()
#if weather['cod'] == 200:
    #temperature = weather['main']['temp']

    #wind = weather['wind']['speed']

#print(f'{city_name}, {weather["main"]["temp"]}')

#url = 'https://api.openweathermap.org/data/2.5/weather?q=Ivano-Frankivsk&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
city_name = input('Enter the name of city:')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}' \
      f'&appid=47503e85fabbabc93cff28c52398ae97&units=metric'

response = requests.get(url)
response = response.json()

if response['cod'] == 200:
    temperature = response['main']['temp']

    wind = response['wind']['speed']

    print(f"The wind speed in {response['name']} is {wind} and temperature is {temperature}°C")

