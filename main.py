import requests
import re  # Импортируем модуль для работы с регулярными выражениями
import json


# Функция для проверки баланса
def check_balance(login, password):
    url = "https://my3.webcom.mobi/json/balance.php"
    headers = {"Content-type": "text/json; charset=utf-8"}

    data = {"login": login,
            "password": password}

    try:
        # Отправляем POST-запрос
        response = requests.post(url, data=json.dumps(data), headers=headers)

        # Проверяем успешность запроса и обрабатываем ответ
        if response.status_code == 200:
            response_data = response.json()
            return response_data['money']
        else:
            print(f"Произошла ошибка при выполнении запроса: {response.status_code}")
            return None
    except Exception as e:
        print(f"Произошла ошибка {e}")


# Функция для поверки правильности номера телефона
def validate_phone_number(phone_number):
    # Паттерн для проверки номера телефона (предполагаем, что номер состоит из 11 цифр)
    pattern = r'^79\d{9}$'  # Или r'^[79]\d{9}$'
    return bool(re.match(pattern, phone_number))  # Возвращает true или false


# Замените следующие значения на ваши данные
user = 'python24'
password = 'TCMS9L'
sender = 'python2024'
receiver = '79163439281'
text = 'Привет, Мир!'

# Проверяем баланс перед отправкой SMS
balance = check_balance(user, password)
if balance:
    print(f"Баланс: {balance} руб.")
    # Если баланс достаточен, отправляем SMS
    if float(balance) > 10:  # Предположим, что SMS стоит 10 рублей
        if not validate_phone_number(receiver):
            print("Ошибка, некорректный номер телефона")
        else:
            url = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
            try:
                response = requests.get(url)
                print(response)
                if response.status_code == 200:
                    print("Сообщение успешно отправлено")
                else:
                    print(f"Ошибка при отправке сообщения: {response.status_code}")
            except Exception as e:
                print(f"Произошла ошибка при отправке SMS: {e}")
    else:
        print("Недостаточно средств для отправки SMS")
else:
    print("Не удалось получить информацию о балансе")
