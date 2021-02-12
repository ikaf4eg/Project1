a = input('Введите значение переменной "a": ')
b = input('Введите значение переменной "b": ')

summ = int(a) + float(b)
dif = int(a) - int(b)

print('сумма a и b = ' + str(summ))
print('разность a и b = ' + str(dif))
print('b в квадрате = ' + str(int(b)**2))
print('если b разделить на цело на 2, то получится: ' + str(int(b)//2))
print('остаток от деления b на 2 = : ' + str(int(b)%2))