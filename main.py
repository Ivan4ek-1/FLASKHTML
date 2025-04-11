from flask import *

from data import db_session
from forms.addjob import JobsForm
from forms.loginform import LoginForm
from forms.registerform import RegisterForm
from data.users import User
from data.jobs import Jobs
from data.db_session import global_init
from flask_login import current_user, LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


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


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add_job',  methods=['GET', 'POST'])
def add_job():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.team_leader = form.team_leader.data
        jobs.job = form.job.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.start_date = form.start_date.data
        jobs.end_date = form.end_date.data
        jobs.is_finished = form.is_finished.data
        current_user.jobs.append(jobs)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('job.html', title='Добавление работы', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.hashed_password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.login == form.login.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            login=form.login.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.hashed_password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(host='127.0.0.1', port=8000)
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

    # firstjob = Jobs()
    # firstjob.team_leader = 1
    # firstjob.job = 'deployment of residential modules 1 and 2'
    # firstjob.work_size = 15
    # firstjob.collaborators = 2, 3
    # firstjob.start_date = 'now'
    # firstjob.is_finished = False
    #
    # db_sess = db_session.create_session()
    # db_sess.add(captain)
    # db_sess.add(chef)
    # db_sess.add(navigator)
    # db_sess.add(fool)
    # db_sess.add(firstjob)
    # db_sess.commit()