from flask import *

app = Flask(__name__)

@app.route('/')
def first():
    return '<b>Миссия Колонизация Марса</b>'


@app.route('/index')
def index():
    return '<b>И на Марсе будут яблони цвести!</b>'


@app.route('/promotion')
def promotion():
    return '''
    <b>Человечество вырастает из детства.</b>
    </br><b>Человечеству мала одна планета.</b>
    </br><b>Мы сделаем обитаемыми безжизненные пока планеты.</b>
    </br><b>И начнем с Марса!</b>
    </br><b>Присоединяйся!</b>
    '''


@app.route('/image_mars')
def image_mars():
    return f'''
    <title>Привет, Марс!</title>
    <h1><b>Жди нас, Марс!</b></h1>
    <img src="{url_for('static', filename='images/MARS.png')}" alt='марс украли'>
    </br>Вот она какая, красная планета.
    '''

@app.route('/promotion_image')
def promotion_image():
    return f'''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
         rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
          crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <title>Колонизация</title>
      </head>
      <body>
        <h1><b>Жди нас, Марс!</b></h1>
        <img src="{url_for('static', filename='images/MARS.jpg')}" alt='марс украли'>
        <div class="alert alert-success" role="alert">
          </br><b>Человечество вырастает из детства.</b>
        </div>
        <div class="alert alert-primary" role="alert">
          </br><b>Человечеству мала одна планета.</b>
        </div>
        <div class="alert alert-danger" role="alert">
          </br><b>Мы сделаем обитаемыми безжизненные пока планеты.</b>
        </div>
        <div class="alert alert-warning" role="alert">
          </br><b>И начнем с Марса!</b>
        </div>
        <div class="alert alert-info" role="alert">
          </br><b>Присоединяйся!</b>
        </div>
      </body>
    </html>'''


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
                                      <option>Инженер-Исследователь</option>
                                      <option>Инженер-строитель</option>
                                      <option>Пилот</option>
                                      <option>Метеоролог</option>
                                      <option>Инженер по жизнеобеспечению</option>
                                      <option>Инженер по радиационной защите</option>
                                      <option>Врач</option>
                                      <option>Экзобиолог</option>
                                    </select>
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

@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
             rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
              crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Варианты выбора</title>
          </head>
          <body>
            <h1>Мое предложение: {planet_name}</h1>
            <h4>Эта планета близка к земле</h4>
            <div class="alert alert-success" role="alert">
              <b>На ней много необходимых ресурсов;</b>
            </div>
            <div class="alert alert-primary" role="alert">
              <b>На ней есть вода и атмосфера;</b>
            </div>
            <div class="alert alert-danger" role="alert">
              <b>На ней есть небольшое магнитное поле;</b>
            </div>
            <div class="alert alert-warning" role="alert">
              ><b>Наконец, она просто красива!</b>
            </div>
          </body>
        </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>'):
def results(nickname, level, rating):
    return f'''
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
                 rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
                  crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                <title>Результаты</title>
              </head>
              <body>
                <h1>Результаты отбора</h1>
                <h4>Претендента на участие в миссии {nickname}</h4>
                <div class="alert alert-success" role="alert">
                  <b>На ней много необходимых ресурсов;</b>
                </div>
                <div class="alert alert-primary" role="alert">
                  <b>На ней есть вода и атмосфера;</b>
                </div>
                <div class="alert alert-danger" role="alert">
                  <b>На ней есть небольшое магнитное поле;</b>
                </div>
                <div class="alert alert-warning" role="alert">
                  ><b>Наконец, она просто красива!</b>
                </div>
              </body>
            </html>'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
