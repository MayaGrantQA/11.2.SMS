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
            mb.showinfo("Баланс", f'Баланс счёта {response_data['money']} руб.')
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
    text = text_entry.get(1.0, END)

    if len(text) > 160:
        mb.showerror("Ошибка", "Текст SMS не может превышать 160 символов")
        return

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

# Функция для обновления метки с количеством символов
def update_character_count(event):
    text = text_entry.get(1.0, END)
    character_count_label.config(text=f"Количество символов: {len(text)}/160")


# Создаем окно tkinter
window = Tk()
window.title("Отправка SMS")
window.geometry("400x200")

# Создаем и размещаем виджеты
Label(text="Номер получателя в формате 79*********: ").pack()
receiver_entry = Entry()
receiver_entry.pack()

Label(text="Текст SMS (макс. 160 символов):").pack()
text_entry = Text(height=6, width=30)
text_entry.pack()
text_entry.bind("<KeyRelease>", update_character_count)  # Обновляем счетчик при вводе

character_count_label = Label(text="Количество символов: 0/160")
character_count_label.pack()

send_button = Button(text="Отправить SMS", command=send_sms)
send_button.pack()

window.mainloop()
