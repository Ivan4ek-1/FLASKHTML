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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
