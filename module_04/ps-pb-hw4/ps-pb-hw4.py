from collections import defaultdict, Counter
import pandas

# def 

logs_data = pandas.read_excel('logs.xlsx', sheet_name='log1', engine='openpyxl')

logs_data_dict = logs_data.to_dict('records')

sales_dict = defaultdict(int) # Создаем словарь с заранее заданным типом значений

for element in logs_data_dict:
    # Добавляем элемент в словарь sales_dict
    # element['item'] - название товара
    # Если ключа с таким названием в sales_dict нет, то будет значение 0,
    # таким образом мы просто увеличим его на 1  
    sales_dict[element['Браузер']] += 1
    sales_dict[element['Дата посещения'].month] += 1

sales_counter = Counter(sales_dict) # Создаем объект Counter из полученного словаря и используем метод most_common
print(f'Самый популярный товар: {sales_counter.most_common(7)[0][0]}. Количество продаж: {sales_counter.most_common(7)[0][1]}')
# print(f'Самый популярный товар: {sales_counter.most_common(7)[0][0]}. Количество продаж: {sales_counter.most_common(7)[0][1]} В месяце {sales_counter.most_common(7)[0][2]} количество продаж: {sales_counter.most_common(7)[0][3]}')
print(sales_dict)

# print(logs_data_dict)



