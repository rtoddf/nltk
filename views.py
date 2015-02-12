from flask import Flask
from flask import render_template

from app import app

# import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown
# from nltk.corpus import reuters
from nltk.corpus import inaugural

from helpers import get_lexical_diversity, get_fileids, get_categories, get_raw_text, get_text_count, get_uniqs_count, get_uniqs, get_word_count, get_total_word_count

# from random import choice
# import pprint
# import time

@app.route('/')
def home():
    inaugural_file_ids = get_fileids(inaugural)
    speech = inaugural_file_ids[-5]

    
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

@app.route('/words')
def words():
    alice = gutenberg.words('carroll-alice.txt')

    lexical_diversity_percentage = get_lexical_diversity(alice)
    word_count = get_word_count(alice)
    total_word_count = get_total_word_count(alice)

    macbeth_sents = gutenberg.sents('shakespeare-macbeth.txt')

    longest_len = max([len(s) for s in macbeth_sents])
    longest_sent = [s for s in macbeth_sents if len(s) == longest_len]

    return render_template('words.html',
        lexical_diversity_percentage=lexical_diversity_percentage,
        word_count=word_count,
        total_word_count=total_word_count,
        alice=alice,
        longest_sent=longest_sent)

@app.route('/fileids')
def fileids():
    fileids = gutenberg.fileids()

    # average characters in a word: raw/words
    # average word in a sentence: words/sents
    # lexical diversity - num_words/num_vocab

    for fileid in fileids:
      num_chars = len(gutenberg.raw(fileid))
      num_words = len(gutenberg.words(fileid))
      num_sents = len(gutenberg.sents(fileid))
      num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
      print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid



















