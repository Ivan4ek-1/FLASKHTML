from flask import *

from forms.loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
