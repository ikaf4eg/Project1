# Оператор in проверяет вхождение одного значение в другое.
# Можно проверять вхождение подстроки в строку:

# value = ['Мой', 'любимый', 'город']

# проверяем вхождение строки в список - результат False
# sub_value = 'ый гор'
# print(sub_value in value) # False

# строка 'Мой' присутствует в списке - результат True
# sub_value = 'Мой'
# print(sub_value in value) # True

# можно получить элемент списка и проверить входит ли он в список - результат всегда будет True
# sub_value = value[1]
# print(sub_value in value) # True

student = {'first_name': 'Иван', 'last_name': 'Иванов'}

# проверяем входит ли ключ 'first_name' в словарь - результат True
print('first_name' in student) # True

# оператор in проверяет именно ключ, а не значение, поэтому следующий код вернет False,
# не смотря на то, что в словаре есть значение 'Иван'
print('Иван' in student) # False

# Как мы уже знаем в Python важен регистр символов - маленькие 
# и большие буквы - это разные значения, 
# поэтому при проверке вхождения подстроки в строку 
# или при сравнении строк рекомендуется преобразовывать их в 
# нижний регистр, используя lower(), если конечно нам не важен регистр.

value = 'Мой любимый город'
sub_value = 'ГороД'
if sub_value.lower() in value.lower():
    print('Подстрока найдена')
else:
    print('Подстрока не найдена')