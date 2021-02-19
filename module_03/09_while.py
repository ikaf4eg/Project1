# Цикл while означает - до тех пор пока выражение expression будет 
# возвращать True, нужно выполнить код цикла.

student1 = {'name': 'Иван', 'cities': ['Москва', 'Лондон']}
student2 = {'name': 'Мария', 'cities': ['Париж', 'Нью Йорк']}
student3 = {'name': 'Петр', 'cities': ['Пекин', 'Токио']}

students = [student1, student2, student3]

city = 'Париж'

name = ''
iterations = 0
while not name and iterations < len(students): # пока выполняется это условие - заходим в цикл
    if city in students[iterations]['cities']:
        name = students[iterations]['name']
    iterations += 1

if name:
    print(f'Город {city} посещал студент с именем {name}')
else:
    print(f'Город {city} никто не посещал')

print(f'Количество итераций: {iterations}')

# Конструкцией not name мы проверяем - пустая строка name или нет т.е. 
# пока "не name"или можно перевести как “Выполнять цикл до тех пор 
# пока name ничего не содержит”. Как только name будет что то содержать, 
# то условие not name уже не выполнится.

# Так пишут профессионалы: 
# while not name and iterations < len(students):
#    if city in students[iterations]['cities']:
#        name = students[iterations]['name']
#    iterations += 1

# Если забыть добавить увеличение переменной-счётчика в цикле while 
# или забыть прописать условие на ограничение количества итераций, 
# то можно ненамеренно уйти в бесконечный цикл. 
# Если вдруг это случилось, нажмите CTRL+C для остановки исполнения программы.