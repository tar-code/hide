import time
import requests
from IPython.display import display, HTML
import ipywidgets as widgets
import os
import sys

url = 'https://hdmn.cloud/ru/demo/'

def send_email():
    try:
        response = requests.get(url)

        # Проверка на успешный ответ от сервера
        if response.status_code == 200:
            # Если текст на странице содержит "Ваша электронная почта", продолжаем
            if 'Ваша электронная почта' in response.text:
                email = input('Введите электронную почту для получения тестового периода: ')

                response = requests.post('https://hdmn.cloud/ru/demo/success/', data={
                    "demo_mail": email
                })

                if 'Ваш код выслан на почту' in response.text:
                    print('Подтвердите e-mail. Проверьте свой почтовый ящик.')
                    # Отображение кнопки для повторного запроса
                    display_retry_button()
                else:
                    print('Указанная почта не подходит для получения тестового периода.')
            else:
                print('На странице не найдено нужного текста. Проверьте доступность страницы.')
        else:
            print(f"Ошибка при запросе к странице. Код ответа: {response.status_code}")

    except requests.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")

def display_retry_button():
    # Функция для отображения кнопки для повторного выполнения
    button = widgets.Button(description="Повторить запрос")
    button.on_click(on_retry_button_click)
    display(button)

def on_retry_button_click(b):
    print("Процесс завершен. Ожидаем повторный запуск...")
    # Ожидаем 5 секунд и затем перезапускаем выполнение
    time.sleep(5)
    # Очищаем среду выполнения
    os.kill(os.getpid(), 9)  # Этот вызов завершит процесс Python и перезапустит среду Colab.

def main():
    send_email()

if __name__ == "__main__":
    main()
