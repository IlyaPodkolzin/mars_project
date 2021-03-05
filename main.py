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


@app.route("/astronaut_selection")
def astronaut_selection():
    return """<!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" 
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                             crossorigin="anonymous">
                            <title>Отбор астронавтов</title>
                        </head>
                        <body>
                            <center><h1>Анкета претендента</h1>
                            <h3>на участие в миссии</h3></center>
                            <form>
                                <div class="mx-auto p-2 bg-warning text-dark border border-2 col-sm-5">
                                    <div class="col-auto y-0">
                                        <input type="text" class="form-control" placeholder="Введите фамилию">
                                        <input type="text" class="form-control" placeholder="Введите имя">
                                    </div>
                                    
                                    <div class="col-auto mt-4">
                                        <input type="text" class="form-control" id="inlineFormInputGroup" placeholder="Введите адрес почты">
                                    </div>
                                    
                                    <label class="mb-1 sr-only" for="inlineFormInput">Какое у вас образование?</label>
                                    
                                    <div class="dropdown open">
                                        <button class="btn btn-light btn-sm dropdown-toggle col-sm-12 " type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                            Начальное
                                        </button>
                                    </div>
                                    
                                    <label class="mt-3 mb-2 sr-only" for="inlineFormInput">Какие у вас есть профессии?</label>
                                    
                                    <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="check1">
                                        <label class="form-check-label" for="check1">Инженер-исследователь</label>
                                    </div>
                                    
                                    <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="check1">
                                        <label class="form-check-label" for="check1">Инженер-строитель</label>
                                    </div>
                                    
                                    <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="check1">
                                        <label class="form-check-label" for="check1">Пилот</label>
                                    </div>
                                    
                                    <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="check1">
                                        <label class="form-check-label" for="check1">Метеоролог</label>
                                    </div>
                                    
                                    <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="check1">
                                        <label class="form-check-label" for="check1">Инженер по жизнеобеспечению</label>
                                    </div>
                                    
                                    <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="check1">
                                        <label class="form-check-label" for="check1">Инженер по радиационной защите</label>
                                    </div>
                                    
                                    <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="check1">
                                        <label class="form-check-label" for="check1">Врач</label>
                                    </div>
                                    
                                    <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="check1">
                                        <label class="form-check-label" for="check1">Экзобиолог</label>
                                    </div>
                                    
                                    <label class="mt-3 sr-only" for="inlineFormInput">Укажите пол</label>
                                    
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                      <label class="form-check-label" for="flexRadioDefault1">Мужской</label>
                                    </div>
                                    
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2">
                                      <label class="form-check-label" for="flexRadioDefault2">Женский</label>
                                    </div>
                                    
                                    <div class="mt-3">
                                      <label for="exampleFormControlTextarea1" class="form-label">Почему Вы хотите принять участие в миссии?</label>
                                      <textarea class="form-control" rows="3"></textarea>
                                    </div>
                                    
                                    <div class="mt-3">
                                      <label for="formFile" class="form-label">Приложите фотографию</label>
                                      <input class="form-control-sm" type="file">
                                    </div>
                                    
                                    <div class="form-check mt-3">
                                        <input type="checkbox" class="form-check-input" id="check1">
                                        <label class="form-check-label" for="check1">Готовы остаться на Марсе?</label>
                                    </div>
                                    
                                    <div class="col-12 mt-3">
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </div>
                                </div>
                            </form>
                        </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
