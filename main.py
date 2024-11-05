import requests
import re  # Импортируем модуль для работы с регулярными выражениями

# Функция для проверки правильности номера телефона
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

if not validate_phone_number(receiver):
    print("Ошибка, некорректный номер телефона")
else:
    # Формируем URL для отправки SMS
    url = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
    print(url)
    # Отправляем запрос
    try:
        response = requests.get(url)
        print(response.status_code)
        # Выводим результат
        if response.status_code == 200:
            print("Сообщение успешно отправлено")
        else:
            print("Ошибка при отправке сообщения", response.status_code)
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
