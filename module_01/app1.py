import time
import os

slide1 = '(^_^)'
slide2 = '(^_~)'
slide3 = '(^_^)'
slide4 = '(о_О)'
slide5 = '(O_O)'
slide6 = 'Hello, World!'

str1 = """
******Заметки лесника******

Погода была пасмурной.
...
...
"""

str2 = """
******Заметки лесника******

Погода была пасмурной.
Шел дождь.
...
"""

str3 = """
******Заметки лесника******

Погода была пасмурной.
Шел дождь.
Но настроение все равно хорошее!
"""

str4 = """
******Заметки лесника******

         КОНЕЦ

****************************
"""

time.sleep(1)
print(slide1, end='\r')
time.sleep(1)
print(slide2, end='\r')
time.sleep(1)
print(slide3, end='\r')
time.sleep(1)
print(slide4, end='\r')
time.sleep(1)
print(slide5, end='\r')
time.sleep(1)
print(slide6, end='\r')
time.sleep(1)

# очищаем окно терминала
os.system('cls')
# выводим сообщение
print(str1, end='\r')
# засыпаем на 1 секунду
time.sleep(1)

# повторяем операцию для остальных строк
os.system('cls')
print(str2, end='\r')
time.sleep(1)

os.system('cls')
print(str3, end='\r')
time.sleep(1)

os.system('cls')
print(str4, end='\r')
time.sleep(1)