import requests
import re
import time
import os
from IPython.display import display, Javascript

def restart_colab():
    """Автоматическая перезагрузка среды Google Colab"""
    display(Javascript("location.reload()"))
    time.sleep(2)
    exit()

url = 'https://hdmn.cloud/ru/demo/'
max_retries = 5  # Количество попыток переподключения
retry_delay = 10  # Задержка между попытками (в секундах)

def get_valid_page():
    """Функция для повторного подключения к сайту, если текст не найден"""
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.encoding = 'utf-8'

            if response.status_code == 200:
                if 'Ваша электронная почта' in response.text:
                    return response  # Если нужный текст найден, возвращаем ответ
                else:
                    print(f"⚠️ Попытка {attempt+1}: На странице нет нужного текста. Пробую снова...")
            else:
                print(f"❌ Ошибка {response.status_code}. Пробую снова...")

        except requests.RequestException as e:
            print(f"❌ Ошибка соединения: {e}. Пробую снова...")

        attempt += 1
        time.sleep(retry_delay)  # Задержка перед повторной попыткой

    print("❌ Не удалось получить нужный текст после нескольких попыток. Завершаю выполнение.")
    exit()

# Запрашиваем страницу с проверкой
response = get_valid_page()

email = input('Введите электронную почту для получения тестового периода: ')

if not isinstance(email, str) or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("❌ Некорректный e-mail. Введите правильный адрес.")
    exit()

# Отправляем POST-запрос
post_url = 'https://hdmn.cloud/ru/demo/success/'
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.post(post_url, data={"demo_mail": email}, headers=headers)

if response.status_code == 200 and 'Ваш код выслан на почту' in response.text:
    print('✅ Ваш код уже в пути! Проверьте свой почтовый ящик.')

    # Автоматическая перезагрузка Colab
    restart_colab()
else:
    print('⚠️ Указанная почта не подходит для получения тестового периода.')
