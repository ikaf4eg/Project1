# Большие данные и журналы регистрации

# Константы
GENDER_MALE = 'm'
GENDER_FEMALE = 'f'


# Список пользователей
user_list = [{'name': 'Иван', 'gender': GENDER_MALE},
             {'name': 'Петр', 'gender': GENDER_MALE},
             {'name': 'Марья', 'gender': GENDER_FEMALE},
             {'name': 'Дарья', 'gender': GENDER_FEMALE},
             {'name': 'Юлия', 'gender': GENDER_FEMALE}, ]

# Список товаров
item_list = [{'title': 'Часы', 'cost': 9800},
             {'title': 'Кофемашина', 'cost': 23500},
             {'title': 'Фитнес-браслет', 'cost': 13200},
             {'title': 'Айфон', 'cost': 73900},
             {'title': 'Чехол для телефона', 'cost': 250}, ]

# Журнал регистрации - каждая запись в журнале содержит сведения о покупке
log = [{'user': user_list[0], 'purchases': [item_list[0], item_list[1], item_list[2]]},
       {'user': user_list[1], 'purchases': [item_list[0], item_list[2]]},
       {'user': user_list[2], 'purchases': [item_list[2], item_list[3]]},
       {'user': user_list[3], 'purchases': [item_list[2], item_list[3]]},
       {'user': user_list[4], 'purchases': [item_list[4], item_list[2]]}, ]

# Создадим список для хранения популярных товар: popular_items.
# Этот список будет состоять из словарей следующей структуры:
# {
#     'title':    наименование товара
#     'quantity': количество проданных товаров
# }
popular_items = []

# Обходим все записи из списка log
for record in log:
    
    # Для каждой записи из списка 'log' в цикле обходим все записи из списка 'purchases'
    for item in record['purchases']:
        
        # Получаем название купленного товара
        purchase_title = item['title']

        # Ищем купленный товар в списке popular_items по ключу 'title'
        found = False
        for popular_item in popular_items:
            # Если нашли товар, то увеличиваем значение ключа 'quantity' на 1
            # и выходим из цикла, используя оператор break
            if popular_item['title'] == purchase_title:
                popular_item['quantity'] += 1
                found = True
                break
        
        # Если купленный товар не найден в списке popular_items,
        # то добавляем его и ставим количество (quantity) = 1
        if not found:
            popular_items.append({'title': purchase_title, 'quantity': 1})
            
# Выводим продажи по каждому товару
for popular_item in popular_items:
    print(f"Количество продаж товара {popular_item['title']} = {popular_item['quantity']}")

    # Создадим переменную, в которой будем хранить максимальное значение
# Изначально значение будет равно 0
max_count = 0

# Создадим переменную для хранения названия самого популярного товара
popular_item_title = ''

for popular_item in popular_items:
    # Обходим все элементы в списке popular_items
    if popular_item['quantity'] > max_count:
        # Для каждого элемента выполняем сравнение: если значение ключа 'quantity' > max_count,
        # то записываем в max_count значение ключа 'quantity' и запоминаем название товара
        max_count = popular_item['quantity']
        popular_item_title = popular_item['title']

print('------')
print(f"Самый популярный товар: {popular_item_title}")