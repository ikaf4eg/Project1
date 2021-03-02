book_list = [{'title': 'Война и мир', 'author': 'Толстой Л.Н.'},
             {'title': 'Идиот', 'author': 'Достоевский Ф.М.'},
             {'title': 'Капитанская дочка', 'author': 'Пушкин А.С.'}]

len_max = 0

for book in book_list:
    title = book['title']
    if len(title) > len_max:
        len_max = len(title)


print(f'Самое длинное название книги содержит {len_max} символов')