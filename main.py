from flask import Flask

app = Flask(__name__)


@app.route('/')
def name():
    return "Миссия Колонизация Марса"


@app.route("/index")
def motto():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return "Человечество вырастает из детства.</br>Человечеству мала одна планета.</br>Мы сделаем обитаемыми безжизненные пока планеты.</br>И начнем с Марса!</br>Присоединяйся!"


@app.route("/image_mars")
def image_mars():
    return """<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/img/mars.jpg">
                        </br>Вот она какая, красная планета.
                    </body>
                </html>"""


@app.route("/promotion_image")
def promotion_image():
    return """<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                         crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
                        <title>Колонизация</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/img/mars.jpg">
                        <div class="alert alert-dark" role="alert">
                         <h4>Человечество вырастает из детства.</h4>
                        </div>
                        <div class="alert alert-success" role="alert">
                         <h4>Человечеству мала одна планета.</h4>
                        </div>
                        <div class="alert alert-dark" role="alert">
                         <h4>Мы сделаем обитаемыми безжизненные пока планеты.</h4>
                        </div>
                        <div class="alert alert-warning" role="alert">
                         <h4>И начнём с Марса!</h4>
                        </div>
                        <div class="alert alert-danger" role="alert">
                         <h4>Присоединяйся!</h4>
                        </div>
                    </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
