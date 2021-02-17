age_min = 18

viewer = {'name': 'Иван', 'age': 10, 'ticket': False, 'promo': True}

if viewer['age'] >= age_min and (viewer['ticket'] or viewer['promo']):
    print(f"Зритель {viewer['name']} может смотреть фильм")
else:
    print(f"Зритель {viewer['name']} не может смотреть фильм")

# Оператор and проверяет, что все условия равны True. 
# Если хотя бы одно из условий, объединенных оператором and равно False, 
# то в результате получается False.

# Для сравнения со значение True или False не обязательно 
# писать == True или == False - это можно опускать и сокращать запись:
# a = True
# if a:
#     print('Условие выполнено')
# else:
#     print('Условие не выполнено')

#Оператор or - это логическое ИЛИ. 
# Он проверяет что хотябы 1 условие выполняется:

# False and True вернет False;
# False or True вернет True.