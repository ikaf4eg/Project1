from app import app
from flask import render_template


@app.route('/')
def index():

    # Выполняем расчеты на сервере
    result1 = 10 + 25
    result2 = 200 - 300

    # Создаем словарь, в который помещаем результаты расчетов
    # Этот словарь будет являться контекстом - его передадим в функцию render_template
    context = {
        'result1': result1,
        'result2': result2,
    }

    return render_template('index.html', **context)