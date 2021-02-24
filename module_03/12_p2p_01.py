# Функция получения ссылки с учетом переданных в неё
# позиций и ключей для навигации
def get_absolute_url(url, *args, **kwargs):
    url = url # пепеменная для печати функции
    for i in args:
        url = url + f'/{i}' # цикл для пепедачи в переменную позиций
    j = len(kwargs)
    url = url + '?'
    for k, v in kwargs.items(): # цикл для передачи в переменную ключей
        if j > 0 and j < len(kwargs):
            url = url + '&'
        url = f'{url}{k}={v}'
        j-=1
    return url


print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))