import collections
import pandas

logs_data = pandas.read_excel('logs.xlsx', sheet_name='log1', engine='openpyxl')

logs_data_dict = logs_data.to_dict('records')

print(logs_data_dict[0])



