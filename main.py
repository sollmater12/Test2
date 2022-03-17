import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def check():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <link rel="icon" href="static/img/favicon.ico" type="image/x-icon">
                    <link rel="shortcut icon" href="static/img/favicon.ico" type="image/x-icon">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def two_params(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <link rel="icon" href="static/img/favicon.ico" type="image/x-icon">
                    <link rel="shortcut icon" href="static/img/favicon.ico" type="image/x-icon">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}</h2>
                    <div class="alert alert-success" role="alert">
                          Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-light" role="alert">
                          составляет {rating}
                    </div>
                    <div class="alert alert-warning" role="alert">
                          Желаем удачи!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    port = int(os.environ.get("POST", 5000))
    app.run(host="0.0.0.0", port=port)
