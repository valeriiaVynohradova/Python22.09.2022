# Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ), отримайте курс валют і запишіть
# його в текстовий файл такому форматі (список):
# "[дата створення запиту]"
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
# P.S.не забувайте про DRY, KISS, SRP та перевірки

import requests
import datetime

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
date = datetime.date.today()

try:
    result = requests.request('GET', url)
except Exception as error:
    print(error)
else:
    if 300 > result.status_code >= 200:
        if content_type := result.headers.get('Content-Type'):
            if content_type == 'application/json; charset=utf-8':
                response_json = result.json()
                response = [str(date)]
                for i, value in enumerate(response_json, 1):
                    currency = str(i) + ". " + value['txt'] + " to UAH: " + str(value['rate'])
                    response.append(currency)
                with open('exchange_rate.txt', 'w', encoding='utf-8') as file:
                    file.write('\n'.join(response))
