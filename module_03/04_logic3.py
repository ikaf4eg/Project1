# Оператор not - это логическое НЕ. Например, можно проверить - если 
# элемент еще не входит в список, то добавить его туда. 
# Выполни следующий код:

# создаем список городов
cities = ['Москва', 'Париж', 'Лондон']

# определяем новый город
new_city = 'Нью Йорк'

# проверяем: если нового города нет в списке, то добавляем его
# иначе выводим сообщение, что город не добавлен.
# в данном случае город добавиться в список
if new_city not in cities:
    cities.append(new_city)
    print('Город добавлен в список')
else:
    print('Город не добавлен в список')

# повторный вызов этого же когда не добавит город в список, потому что он там уже есть
# условие "new_city not in cities" будет равно False
if new_city not in cities:
    cities.append(new_city)
    print('Город добавлен в список')
else:
    print('Город не добавлен в список')