cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')

if city.lower() == str.lower(tourists[0]['city']): # Проверка города туриста 1
    idx = 0 # указание на индекс туриста 1
elif city.lower() == str.lower(tourists[1]['city']): # Проверка города туриста 2
    idx = 1 # указание на индекс туриста 2
elif city.lower() == str.lower(tourists[2]['city']): # Проверка города туриста 3
    idx = 2 # указание на индекс туриста 3
else: # Если введён город не из списка посещённых городов. Выход из программы.
    print(f"Никто из туристов в городе {city} не был.")
    exit()
# Вывод текста с информацией о туристе на экран
print(f"Турист {tourists[idx]['user']['name']} - возраст {tourists[idx]['user']['age']}. Посетил город {tourists[idx]['city']}.")