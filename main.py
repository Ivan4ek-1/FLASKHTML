from flask import *

app = Flask(__name__)

@app.route('/')
def first():
    return '<b>Миссия Колонизация Марса</b>'


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<mod>')
def list_prof(mod):
    lst = ['инженер-исследователь', 'пилот', 'профессиональный комик']
    return render_template('list.html', mod=mod, lst=lst)

@app.route('/auto_answer')
@app.route('/answer')
def answer():
    dt = {'title': 'Анкета', 'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
          'profession': 'штурман марсохода', 'sex': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!',
          'ready': True}
    return render_template('auto_answer.html', dt=dt)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
