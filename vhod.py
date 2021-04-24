from flask import Flask
from flask import request, url_for
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from data.users import User
from data import db_session
import db
from data import users
from formavoprosa import bootstrap
app = Flask(__name__)
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='venv/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="log" placeholder="Введите логин" name="log">
                                    <input type="password" class="form-control" id="pas" placeholder="Введите пароль" name="pas">
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':

        user = User()
        user.login = request.form['log']
        user.password = request.form['pas']
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        exists = db.session.query(User.id).filter_by(name=f'user.login').scalar() is not None

        def check_in():
            Session = sessionmaker(bind=sqlalchemy.engine)
            query = db_sess.query(users).filter(users.login.in_([user.login]), users.password.in_([user.password]))
            result = query.first()
            if result:
                return True
            else:
                return False
        if exists:
            if check_in():
                @app.route('/aa', methods=['POST', 'GET'])
                def aa():
                    return bootstrap("ww")

        if not exists:
            db_sess.add(user)
            db_sess.commit()

            @app.route('/bb', methods=['POST', 'GET'])
            def bb():
                return bootstrap("asddas")
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')