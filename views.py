from flask import Flask
from flask import render_template

from app import app

# from random import choice
# import pprint
# import time

@app.route('/')
def home():
    return render_template('index.html')
