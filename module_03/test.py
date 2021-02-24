def get_absolute_url(url,*args,**kwargs):
    for i in args:
        url+='/'+i
    url+='?'
    for k,v,in kwargs.items():
        url+=k+'='+v+'&'
    url = url[:len(url)-1]
    return url


print(get_absolute_url('www.yandex.ru', 'posts', 'news','122', id='24', author='admin', aaaa='bbb'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))