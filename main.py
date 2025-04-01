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

@app.route('answer')
def answer():
    pass


@app.route('/astronaut_selection')
def selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                     <html lang="en">
                        <head>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                          <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                          <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                          <title>Отбор астронавтов</title>
                        </head>
                        <body>
                          <h1 align='center'>Анкета претендента</h1>
                          <h4 align='center'>на участие в миссии</h4>
                          <div>
                              <form class="login_form" method="post">
                                  <input type="text" class="form-control" id="surname" 
                                  placeholder="Введите фамилию" name="surname">
                                  <input type="text" class="form-control"
                                  id="name" placeholder="Введите имя" name="name">
                                  <input type="email" class="form-control" id="email"
                                  aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                  <div class="form-group">
                                    <label for="classSelect">Какое у вас образование?</label>
                                    <select class="form-control" id="classSelect" name="class">
                                      <option>Начальное</option>
                                      <option>Среднее</option>
                                      <option>Высшее</option>
                                      <option>Профессиональное</option>
                                    </select>
                                    </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="check1" name="check1">
                                    <label class="form-check-label" for="check1">Инженер-исследователь</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" class="form-check-input" id="check2" name="check2">
                                    <label class="form-check-label" for="check2">Инженер-строитель</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" class="form-check-input" id="check3" name="check3">
                                    <label class="form-check-label" for="check3">Пилот</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" class="form-check-input" id="check4" name="check4">
                                    <label class="form-check-label" for="check4">Метеоролог</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" class="form-check-input" id="check5" name="check5">
                                    <label class="form-check-label" for="check5">Инженер по жизнеобеспечению</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" class="form-check-input" id="check6" name="check6">
                                    <label class="form-check-label" for="check6">Инженер по радиационной защите</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" class="form-check-input" id="check7" name="check7">
                                    <label class="form-check-label" for="check7">Врач</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" class="form-check-input" id="check8" name="check8">
                                    <label class="form-check-label" for="check8">Экзобиолог</label>
                                    </div>
                                    <div class="form-group">
                                      <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex"
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                        <div class="form-group">
                                          <label for="about">Почему вы хотите принять участие в миссии?</label>
                                          <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                      </div>
                                      <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input"
                                             id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">
                                            Готовы остаться на марсе?
                                            </label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
