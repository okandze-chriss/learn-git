from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1> Hello World </h1>"

