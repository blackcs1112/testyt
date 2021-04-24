from flask import Flask, request

app = Flask(__name__)



@app.route('/results', methods=['POST', 'GET'])
def bootstrap(word):
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
                        <title>Вопрос</title>
                      </head>
                      <body>
                        <h6>вопрос</h6>
                        <h8>{word}</h8>
                        <div class="form-group">
                            <div class="form-group">
                                <label for="about">Ваш ответ</label>
                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                            </div>
                        </div>
                      </body>
                    </html>'''
    elif request.method == 'POST':
        print(request.form['about'])
        return "принято"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')