# Оптимизация кода с помощью collections

# Задача: дан журнал продаж в виде списка словарей.
# Требуется найти самый продаваемый товар.

""" 
sales_log = [{'user': 'Маша', 'item': 'Телескоп'},
       {'user': 'Юля', 'item': 'Айфон'}, 
       {'user': 'Иван', 'item': 'Ноутбук'},
       {'user': 'Сергей', 'item': 'Браслет'},
       {'user': 'Инна', 'item': 'Айфон'},
       {'user': 'Ольга', 'item': 'Айфон'},
       {'user': 'Дмитрий', 'item': 'Браслет'}, ]

sales_dict = {} # Создаем пустой словарь

for element in sales_log:
    item_title = element['item'] # Получаем название товара по ключу item
    if item_title in sales_dict.keys(): # Проверяем - присутствует ли такое название в списке ключей в словаре sales_dict
        sales_dict[item_title] += 1 # Если присутствует, то увеличиваем значение на 1
    else:
        sales_dict[item_title] = 1 # Если такого ключа нет в словаре sales_dict, то создаем его и присваиваем значение 1

# Ищем максимальное значение
maximum = 0
item_title = ''

# Пробегаемся по всем элементам из словаря sales_dict
for k, v in sales_dict.items():
    if v > maximum:
        maximum = v
        item_title = k
print(f'Самый популярный товар: {item_title}. Количество продаж: {maximum}')
"""

# Продвинутый метод: используем модуль collection:
from collections import defaultdict, Counter


sales_log = [{'user': 'Маша', 'item': 'Телескоп'},
       {'user': 'Юля', 'item': 'Айфон'}, 
       {'user': 'Иван', 'item': 'Ноутбук'},
       {'user': 'Сергей', 'item': 'Браслет'},
       {'user': 'Инна', 'item': 'Айфон'},
       {'user': 'Ольга', 'item': 'Айфон'},
       {'user': 'Дмитрий', 'item': 'Браслет'}, ]

sales_dict = defaultdict(int) # Создаем словарь с заранее заданным типом значений

for element in sales_log:
    # Добавляем элемент в словарь sales_dict
    # element['item'] - название товара
    # Если ключа с таким названием в sales_dict нет, то будет значение 0,
    # таким образом мы просто увеличим его на 1  
    sales_dict[element['item']] += 1

sales_counter = Counter(sales_dict) # Создаем объект Counter из полученного словаря и используем метод most_common
print(f'Самый популярный товар: {sales_counter.most_common(1)[0][0]}. Количество продаж: {sales_counter.most_common(1)[0][1]}')

# Код программы сильно сократился!!!

