a = 15
b = 0
try:
    result = a/b
except:
    print('Нельзя делить на 0')
    result = 0

print('результат деления = ' + str(result))