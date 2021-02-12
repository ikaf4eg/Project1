password = input("Введите пароль: ")
# Обрабатываются два условия   
try:
    password[0]
    int(password)/0
# У пустой строки нет индекса вызывается ошибка IndexError
except IndexError:
    print("Вы ввели пустой пароль")
# Изменяется тип переменной со строки на числовой и деление на ноль вызывает  ZeroDivisionError
except ZeroDivisionError:
    print("Ваш пароль состоит только из цифр")
# Тип переменной верный числовой, но значение (содержит буквы) не корректно вызывается ValueError
except ValueError:
    print("Требования к паролю соблюдены")