import time
import requests
from IPython.display import display, HTML
import ipywidgets as widgets

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
                    # Отображение ссылки для повторного запроса
                    display_retry_link()
                else:
                    print('Указанная почта не подходит для получения тестового периода.')
            else:
                print('На странице не найдено нужного текста. Проверьте доступность страницы.')
        else:
            print(f"Ошибка при запросе к странице. Код ответа: {response.status_code}")

    except requests.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")

def display_retry_link():
    # Функция для отображения ссылки для повторного запроса
    html = """
    <a href="javascript:void(0)" onclick="window.location.reload();">Повторить запрос</a>
    <p>При нажатии на ссылку страница будет обновлена, и можно будет ввести новый email.</p>
    """
    display(HTML(html))

def main():
    send_email()

if __name__ == "__main__":
    main()
