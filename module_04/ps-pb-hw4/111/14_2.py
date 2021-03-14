# Поиск в списке словарей
""" Нам нужно посчитать количество фруктов в списке. 
Для этого потребуется добавить к каждому элементу признак - это 
фрукт или не фрукт. Таким образом каждый элемент списка будет 
не просто строка, а словарь, который содержит название и признак 
фрукт/не фрукт:"""

item_list = [{'title': 'Яблоко', 'is_fruit': True},
             {'title': 'Апельсин', 'is_fruit': True},
             {'title': 'Банан', 'is_fruit': True},
             {'title': 'Автомобиль', 'is_fruit': False},
             {'title': 'Телефон', 'is_fruit': False},
             {'title': 'Груша', 'is_fruit': False}, ]

""" Чтобы посчитать количество фруктов - добавим в функцию параметр 
типа bool, в который будем передавать что именно считать - фрукты 
или не фрукты и при вызове функции будем передавать True или False:"""

def quantity(object_list, is_fruit):
    result = 0
    for i in object_list:
        if i['is_fruit'] == is_fruit:
            result += 1
    return result


item_list = [{'title': 'Яблоко', 'is_fruit': True},
             {'title': 'Апельсин', 'is_fruit': True},
             {'title': 'Банан', 'is_fruit': True},
             {'title': 'Автомобиль', 'is_fruit': False},
             {'title': 'Телефон', 'is_fruit': False},
             {'title': 'Груша', 'is_fruit': True}, ]

print(f'Количество фруктов = {quantity(item_list, is_fruit=True)}')
print(f'Количество не фруктов = {quantity(item_list, is_fruit=False)}')