str1 = "начало_"
str2 = "конец"
sum = str1 + str2*3 #переменная str2 умножена на 3, в выводе будет 3 переменных подрят

print(sum)
print(str(len(sum))) #len - длина строки

sentence = "Первое Второе И Салат"

print(sentence.upper()) # ПЕРВОЕ ВТОРОЕ И САЛАТ
print(sentence.lower()) # первое второе и салат

# capitalize: делает первый символ заглавным, остальные маленькими
# count: считает количество символов в строке (Int)
# isnumeric: проверить, что строка содержит только цифры (True|False)
# isalpha: проверить, что строка содержит только буквы (алфавитные символы) (True|False)
# lstrip, rstrip, strip: удалить пробелы слева, справа, с обоих сторон
# find: найти подстроку в строке
    # Метод find возвращает индекс первого вхождения искомого текста в строке. Нумерация начинается с нуля т.е. индекс первого символа в строке = 0, а не 1.
    # Метод find просматривает строку слева направо и возвращает индекс первого вхождения.
    # rfind: найти подстроку в строке - просмотр справа налево
    # Если искомый текст не найден, то оба метода возвращают -1. При поиске учитывается регистр!!!


# Передача переменных в строки!!
last_name = "Иванов"
first_name = "Иван"
age = 38

print("Клиенту с фамилией {} и именем {} {} лет".format(last_name, first_name, age))
# Клиенту с фамилией Иванов и именем Иван 38 лет

# f-строки!!!

last_name = "Иванов"
first_name = "Иван"
age = 38

result = f'Клиенту с фамилией {last_name} и именем {first_name} {age} лет'

print(result)
# Клиенту с фамилией Иванов и именем Иван 38 лет