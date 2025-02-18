import requests
import re
import time
import os
from IPython.display import display, Javascript

def restart_colab():
    """Функция для автоматической перезагрузки среды Google Colab"""
    display(Javascript("location.reload()"))
    time.sleep(2)  # Небольшая задержка перед завершением
    exit()

url = 'https://hdmn.cloud/ru/demo/'

try:
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        if 'Ваша электронная почта' in response.text:
            email = input('Введите электронную почту для получения тестового периода: ')

            if not isinstance(email, str) or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("❌ Некорректный e-mail. Введите правильный адрес.")
                exit()

            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.post('https://hdmn.cloud/ru/demo/success/', data={"demo_mail": email}, headers=headers)

            if response.status_code == 200 and 'Ваш код выслан на почту' in response.text:
                print('✅ Ваш код уже в пути! Проверьте свой почтовый ящик.')

                # Автоматическая перезагрузка Colab
                restart_colab()

            else:
                print('⚠️ Указанная почта не подходит для получения тестового периода.')
        else:
            print('⚠️ На странице не найден нужный текст. Проверьте доступность сайта.')
    else:
        print(f"❌ Ошибка при запросе к странице. Код ответа: {response.status_code}")

except requests.ConnectionError:
    print("❌ Ошибка соединения. Проверьте интернет или сайт недоступен.")
except requests.RequestException as e:
    print(f"❌ Ошибка при запросе к сайту: {e}")
