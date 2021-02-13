# создаем 3 словаря для хранения данных о 3х студентах
student1 = {'first_name': 'Иван', 'age': 32, 'cities': ['Москва', 'Лондон']}
student2 = {'first_name': 'Петр', 'age': 21, 'cities': ['Москва']}
student3 = {'first_name': 'Дарья', 'age': 18, 'cities': ['Париж']}

# создаем список словарей из студентов
students = [student1, student2, student3]

# выводим все элементы из списка студентов
# каждый выводимый элемент - словарь
print(students[0]) # {'first_name': 'Иван', 'age': 32, 'cities': ['Москва', 'Лондон']}
print(students[1]) # {'first_name': 'Петр', 'age': 21, 'cities': ['Москва']}
print(students[2]) # {'first_name': 'Дарья', 'age': 18, 'cities': ['Париж']}

# создаем переменную для хранения нулевого студента - элемент из списка студентов с индексом 0
student0 = students[0]

# выводим по ключам значения нулевого студента - обращаемся к ключам через квадратные скобки
print(student0['first_name']) # Иван
print(student0['age'])    # 32
print(student0['cities'])   # ['Москва', 'Лондон']
print(student0['cities'][0]) # Москва

# Метод get() принимает 2 аргумента:
# 1 - ключ
# 2 - значение по умолчанию: подставляется, 
# если искомый ключ в словаре не найден

student = {'first_name': 'Иван', 'age': 32}
birthday = student.get('birthday', 'дата рождения не указана')
print(birthday) # дата рождения не указана