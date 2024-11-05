import requests

# Замените следующие значения на ваши данные
user = 'python24'
password = 'TCMS9L'
sender = 'python2024'
receiver = '79163439281'
text = 'Привет, Мир!'

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
