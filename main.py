from flask import Flask
from vhod import form_sample
app = Flask(__name__)
from data import db_session
from formavoprosa import bootstrap
db_session.global_init("db/users.db")

@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
@app.route('/vhh', methods=['POST', 'GET'])
def vhh():
    return form_sample()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')