"""В Python существует понятие чистых и грязных функций.
Чистая функция - функция, которая не изменяет передаваемые параметры.
Грязные функции - функция, которая изменяет передаваемые параметры.
Например, функция для вычисления длины списка len() является чистой
А наша функция (написаная ранее) sort_list() является грязной, потому что 
она меняет параметр списка, который мы ей передаем
"""
def sort_list(my_list, direction=None):
    """Сортировка списка my_list методом пузырька.
    :param my_list: список значений
    :param direction: (опциональный) направление сортировки. Возможные значения: 1, -1
    """
    # создаем новую переменную new_list в функции - она доступна только в этой функции
    # и не доступна в теле основной программы
    new_list = []
    for element in my_list:
        new_list.append(element)

    if direction:
        # Сортируем список только если передан параметр direction
        for i in range(len(new_list)):
            for j in range(i, len(new_list)):
                if (direction == -1 and new_list[i] > new_list[j]) or (direction == 1 and new_list[i] < new_list[j]):
                    # Если direction == -1 и текущий элемент больше следующего
                    # или direction == 1 и текущий элемент меньше следующего,
                    # то меняем местами элементы.
                    temp = new_list[i]
                    new_list[i] = new_list[j]
                    new_list[j] = temp

    return new_list


list1 = [1, 9, 0]
print(f'{list1} - значение list1 до вызова функции')

sorted_list = sort_list(list1, -1) # результат функции sort_list() передаем в новую переменную sorted_list

print(f'{list1} - значение list1 после вызова функции')
print(f'{sorted_list} - значение переменной sorted_list')