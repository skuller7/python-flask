from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    print('Received a request on /hello')
    return 'Hello, World!'

@app.route('/goodbye')
def goodbye():
    print('Received a request on /goodbye')
    return 'Goodbye!'

@app.route('/new-route')
def nNew():
    return 'Test new route'