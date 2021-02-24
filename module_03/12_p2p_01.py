# Функция получения ссылки с учетом переданных в неё
# позиций и ключей для навигации
def get_absolute_url(url, *args, **kwargs):
    print_url = url # пепеменная для печати функции
    for i in args:
        print_url = print_url + f'/{i}' # цикл для пепедачи в переменную позиций
    j = len(kwargs)
    for k, v in kwargs.items(): # цикл для передачи в переменную ключей
        if j == len(kwargs):
            print_url = print_url + '?'
        elif j > 0:
            print_url = print_url + '&'
        print_url = f'{print_url}{k}={v}'
        j-=1
    return print_url


print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))