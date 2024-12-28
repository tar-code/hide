import requests
from bs4 import BeautifulSoup

url = 'https://hdmn.cloud/ru/demo/'

# Попытка получить страницу и проверить статус ответа
try:
    response = requests.get(url)
    
    # Проверка на успешный ответ от сервера
    if response.status_code == 200:
        # Использование BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Проверка наличия текста "Ваша электронная почта" на странице
        if 'Ваша электронная почта' in soup.get_text():
            email = input('Введите электронную почту для получения тестового периода: ')

            # Отправка данных на сервер
            response = requests.post('https://hdmn.cloud/ru/demo/success/', data={"demo_mail": email})

            if response.status_code == 200 and 'Ваш код выслан на почту' in response.text:
                print('Подтвердите e-mail. Проверьте свой почтовый ящик.')
            else:
                print('Указанная почта не подходит для получения тестового периода или ошибка на сервере.')
        else:
            print('На странице не найдено нужного текста. Проверьте доступность страницы.')
    else:
        print(f"Ошибка при запросе к странице. Код ответа: {response.status_code}")
        
except requests.RequestException as e:
    print(f"Ошибка при запросе к сайту: {e}")
