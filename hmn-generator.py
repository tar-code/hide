import requests

url = 'https://hdmn.cloud/ru/demo/'

# Попытка получить страницу и проверить статус ответа
try:
    response = requests.get(url)
    
    # Проверка на успешный ответ от сервера
    if response.status_code == 200:
        # Если текст на странице содержит "Ваша электронная почта", продолжаем
        if 'Ваша электронная почта' in response.text:
            email = input('Введите электронную почту для получения тестового периода: ')

            response = requests.post('https://hdmn.cloud/ru/demo/success/', data={
                "demo_mail": f"{email}"
            })

            if 'Ваш код выслан на почту' in response.text:
                print('print("\033[32mВаш код уже в пути!\033[0m") Проверьте свой почтовый ящик.')
            else:
                print('Указанная почта не подходит для получения тестового периода.')
        else:
            print('На странице не найдено нужного текста. Проверьте доступность страницы.')
    else:
        print(f"Ошибка при запросе к странице. Код ответа: {response.status_code}")
        
except requests.RequestException as e:
    print(f"Ошибка при запросе к сайту: {e}")
