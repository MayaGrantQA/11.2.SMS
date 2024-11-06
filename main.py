import requests
import re  # Импортируем модуль для работы с регулярными выражениями
import json
from tkinter import *
from tkinter import messagebox as mb


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
            mb.showerror("Ошибка!", f"Произошла ошибка проверки баланса: {response.status_code}")
            return None
    except Exception as e:
        mb.showerror("Ошибка!", f"Произошла ошибка при проверке баланса: {e}")


# Функция для поверки правильности номера телефона
def validate_phone_number(phone_number):
    # Паттерн для проверки номера телефона (предполагаем, что номер состоит из 11 цифр)
    pattern = r'^79\d{9}$'  # Или r'^[79]\d{9}$'
    return bool(re.match(pattern, phone_number))  # Возвращает true или false


def send_sms():
    # Замените следующие значения на ваши данные
    user = 'python24'
    password = 'TCMS9L'
    sender = 'python2024'
    receiver = receiver_entry.get()
    text = text_entry.get()

    # Проверяем баланс перед отправкой SMS
    balance = check_balance(user, password)
    if balance:
        if float(balance) > 10:  # Предположим, что SMS стоит 10 рублей
            if not validate_phone_number(receiver):
                mb.showerror("Ошибка!", "Некорректный номер телефона.")
            else:
                url = (f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}"
                       f"&dadr={receiver}&text={text}")
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        mb.showinfo("Ура!", "Сообщение успешно отправлено!")
                    else:
                        mb.showerror("Ошибка", f"Ошибка при отправке сообщения: {response.status_code}")
                except Exception as e:
                    mb.showerror("Ошибка", f"Произошла ошибка при отправке SMS: {e}")
        else:
            mb.showerror("Ошибка", "Недостаточно средств для отправки SMS")
    else:
        mb.showerror("Ошибка", "Не удалось получить информацию о балансе")


# Создаем окно tkinter
window = Tk()
window.title("Отправка SMS")
window.geometry("250x110")

# Создаем и размещаем виджеты
Label(text="Номер получателя: ").pack()
receiver_entry = Entry()
receiver_entry.pack()

Label(text="Введите текст SMS: ").pack()
text_entry = Entry()
text_entry.pack()

send_button = Button(text="Отправить SMS", command=send_sms)
send_button.pack()

window.mainloop()
