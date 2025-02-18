import requests

url = 'https://hdmn.cloud/ru/demo/'

try:
    response = requests.get(url)
    response.encoding = 'utf-8'  # Установка кодировки для корректного чтения текста

    if response.status_code == 200:
        if 'Ваша электронная почта' in response.text:
            email = input('Введите электронную почту для получения тестового периода: ')
            
            try:
                response = requests.post('https://hdmn.cloud/ru/demo/success/', data={"demo_mail": email})
                response.encoding = 'utf-8'

                if response.status_code == 200 and 'Ваш код выслан на почту' in response.text:
                    print('✅ \033[1;32mВаш код уже в пути!\033[0m Проверьте свой почтовый ящик.')
                else:
                    print('⚠️ \033[1;31mУказанная почта не подходит для получения тестового периода.\033[0m')

            except requests.RequestException as e:
                print(f"❌ \033[1;31mОшибка при отправке почты:\033[0m {e}")
        else:
            print('⚠️ \033[1;31mНа странице не найдено нужного текста.\033[0m Проверьте доступность страницы.')
    else:
        print(f"❌ \033[1;31mОшибка при запросе к странице.\033[0m Код ответа: {response.status_code}")

except requests.RequestException as e:
    print(f"❌ \033[1;31mОшибка при запросе к сайту:\033[0m {e}")
