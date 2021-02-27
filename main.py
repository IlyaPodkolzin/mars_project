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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
