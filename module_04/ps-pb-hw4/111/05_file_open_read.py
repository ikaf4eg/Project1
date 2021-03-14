file_object = open('c:/Users/ikaf/Desktop/MyProjects/Project1/module_04/input.txt', encoding='utf-8')

# Метод read() возвращает строку. 
# Но иногда полезно прочитать файл построчно. 
# Для этого используется метод readlines() - он возвращает список строк
# file_content = file_object.readlines()
# Результат - список строк. В конце каждой строки кроме последней стоит символ переноса:
# ['Я к вам пишу — чего же боле?\n', 'Что я могу ещё сказать?\n', 'Теперь, я знаю, в вашей воле\n', 'Меня презреньем наказать.']

# Можно не пользоваться методом readlines(), а просто обойти file_object циклом for:
# for line in file_object:
#    print(line)

# Отметим еще раз, что методы read() и readlines() возвращают строки. 
# Если в файле будут числовые значения, то нам нужно будет 
# воспользоваться методами int() или float() чтобы преобразовать 
# строковые данные в числа.

summ = 0
for line in file_object:
    number = float(line)
    summ += number

print(summ)