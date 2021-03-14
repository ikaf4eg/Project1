# Сравнение с None
""" Вроде бы все правильно, но теперь мы не можем посчитать 
с помощью нашей функции количество элементов всего.
Задача: если параметр не передается, то должно выводиться общее 
количество элементов в списке.
Для решения этой задачи нам нужно сделать параметр is_fruit 
не обязательным, передав в него значение по умолчанию:"""

# def quantity(object_list, is_fruit=None):
# Тогда мы сможем вызвать функцию без указания этого параметра:
# print(f'Количество элементов всего = {quantity(item_list)}')
# Нам нужно сделать следующую проверку - если параметр is_fruit 
# заполнен И i['is_fruit'] == is_fruit тогда увеличивать счетчик элементов. 
# А ещё нам пригодится сравнение с None, а точнее is None

def quantity(object_list, is_fruit=None):
    result = 0
    for i in object_list:
        if is_fruit is None or i['is_fruit'] == is_fruit: # добавили в условие is_fruit and
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
print(f'Количество элементов всего = {quantity(item_list)}')