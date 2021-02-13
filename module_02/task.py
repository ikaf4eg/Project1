print('Введите пароль:')
str1 = input()
str2 = 'Ваш пароль состоит только из цифр'

try:
    1/len(str1)
    int(str1)
except ZeroDivisionError:
    str2 = 'Вы ввели пустой пароль'
except ValueError:
    str2 = 'Требования к паролю соблюдены'
except:
    str2 = 'Видимо что-то случилось'

print(str2)