from flask import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<mod>')
def list_prof(mod):
    prof_list = ['Инженер-исследователь', 'пилот']
    return render_template('list.html', mod=mod, ls=prof_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
