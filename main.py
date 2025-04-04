from flask import *

from data import db_session
from forms.loginform import LoginForm
from data.users import User
from data.jobs import Jobs

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
    db_session.global_init("db/blogs.db")
    #app.run(host='127.0.0.1', port=8000)
    # captain = User()
    # captain.surname = "Scott"
    # captain.name = "Ridley"
    # captain.age = 21
    # captain.position = 'captain'
    # captain.speciality = 'research engineer'
    # captain.address = 'module_1'
    # captain.email = "scott_chief@mars.org"
    #
    # chef = User()
    # chef.surname = "Scott"
    # chef.name = "Jeff"
    # chef.age = 23
    # chef.position = 'chef'
    # chef.speciality = 'chef'
    # chef.address = 'module_1'
    # chef.email = "cookchief@mars.org"
    #
    # navigator = User()
    # navigator.surname = "Black"
    # navigator.name = "Vova"
    # navigator.age = 47
    # navigator.position = 'navigator'
    # navigator.speciality = 'navigator'
    # navigator.address = 'module_2'
    # navigator.email = "black@mars.org"
    #
    # fool = User()
    # fool.surname = "Carrey"
    # fool.name = "Jim"
    # fool.age = 18
    # fool.position = 'fool'
    # fool.speciality = 'standup'
    # fool.address = 'module_3'
    # fool.email = "clown@mars.org"

    firstjob = Jobs()
    firstjob.team_leader = 1
    firstjob.job = 'deployment of residential modules 1 and 2'
    firstjob.work_size = 15
    firstjob.collaborators = 2, 3
    firstjob.start_date = 'now'
    firstjob.is_finished = False

    db_sess = db_session.create_session()
    # db_sess.add(captain)
    # db_sess.add(chef)
    # db_sess.add(navigator)
    # db_sess.add(fool)
    db_sess.add(firstjob)
    db_sess.commit()