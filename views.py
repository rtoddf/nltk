from flask import Flask
from flask import render_template

from app import app

from helpers import get_lexical_diversity

# from random import choice
# import pprint
# import time

@app.route('/')
def home():
    helper_text = get_lexical_diversity('bob')

    return render_template('index.html',
    helper_text=helper_text)
