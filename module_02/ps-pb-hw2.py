import time
import os

os.system('cls') # Очищаем консоль

i = 0 # переменная для цикла

# Создаём словари с паролями для юзеров
account1 = {'login': 'ivan','password':'q1'}
account2 = {'login': 'petr','password':'q2'}
account3 = {'login': 'olga','password':'q3'}
account4 = {'login': 'anna','password':'q4'}

acc_list = [account1,account2,account3,account4 # Список всех аккаунтов
]
# Создаём бд с данными юзеров
user1 = {'name':'Иван','age':'20','account':'account1'}
user2 = {'name':'Пётр','age':'25','account':'account2'}
user3 = {'name':'Ольга','age':'18','account':'account3'}
user4 = {'name':'Анна','age':'27','account':'account4'}

user_list = [user1,user2,user3,user4] # Список всех юзеров

key = input('Введите ключ (name или account): ') # Запрашиваем ключ
key = key.lower() # Переводим ключ в нижний регистр

# Проверка на существование ключа и вывод информации по ключу
# обо всех пользователях
try:
    while i < 4:
        key_print = user_list[i].get(f'{key}')
        print (f'значение ключа {key} для юзера {i+1} = ' + key_print)
        i = i + 1
# В случае ошибки выход из программы
except:
    print("Введенный ключ не найден")
    exit()

# Запрашиваем порядковый номер юзера
listnumb = input('Введите порядковый номер: ') 
user_listx = user_list[int(listnumb) - 1]
acc_listx = acc_list[int(listnumb) - 1]

print('Данные по юзеру №' + listnumb + ':')
print('имя: ' + user_listx['name'])
print('возраст: ' + user_listx['age'])
print('логин: ' + acc_listx['login'])
print('пароль: ' + acc_listx['password'])
