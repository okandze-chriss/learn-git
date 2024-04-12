from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1> Welcome to my flask app !</h1>"


@app.route('/hello')
def hello_world():
    return "<h1> Hello World !!!</h1>"