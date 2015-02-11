from flask import Flask
from flask import render_template

from app import app

# import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown
# from nltk.corpus import reuters
from nltk.corpus import inaugural

from helpers import get_fileids, get_categories, get_raw_text, get_text_count, get_uniqs_count, get_uniqs

# from random import choice
# import pprint
# import time

@app.route('/')
def home():
    inaugural_file_ids = get_fileids(inaugural)
    speech = inaugural_file_ids[-5]

    # helper_text = get_lexical_diversity('bob')
    gutenberg_file_ids = get_fileids(gutenberg)
    brown_file_ids = get_fileids(brown)
    brown_categories = get_categories(brown)
    # reuters_categories = get_categories(reuters)
    
    raw_text = get_raw_text(inaugural, speech)
    text_count = get_text_count(inaugural, speech)
    uniqs_count = get_uniqs_count(inaugural, speech)
    uniqs = get_uniqs(inaugural, speech)

    print inaugural_file_ids[-1]

    return render_template('index.html',
    gutenberg_file_ids=gutenberg_file_ids,
    brown_file_ids=brown_file_ids,
    brown_categories=brown_categories,
    # reuters_categories=reuters_categories,
    inaugural_file_ids=inaugural_file_ids,
    raw_text=raw_text,
    text_count=text_count,
    uniqs_count=uniqs_count,
    uniqs=uniqs)
