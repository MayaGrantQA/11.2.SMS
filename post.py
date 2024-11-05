# Делаем проект по просмотру баланса.

import requests
import json

# Задаем параметры запроса
url = "https://my3.webcom.mobi/json/balance.php"
headers = {"Content-type": "text/json; charset=utf-8"}

data = {"login": "python24",
        "password": "TCMS9L"}
try:
    # Отправляем POST-запрос
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Проверяем успешность запроса и обрабатываем ответ
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        print(f"Баланс: {response_data['money']} руб.")
    else:
        print(f"Произошла ошибка при выполнении запроса: {response.status_code}")
except Exception as e:
    print(f"Произошла ошибка {e}")
