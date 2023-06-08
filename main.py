from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Hello, world'


@app.route('/profile/<string:name>')
def get_my_name(name):
    return f'My name is {name}'








# app.run()
