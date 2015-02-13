from flask import Flask
from flask import render_template

from app import app

import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown
# from nltk.corpus import reuters
# from nltk.corpus import inaugural
from nltk.corpus import webtext as webtext

# import nltk.book as book

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

@app.route('/macbeth')
def words():
    macbeth_sents = gutenberg.sents('shakespeare-macbeth.txt')

    print macbeth_sents

    longest_len = max([len(s) for s in macbeth_sents])
    longest_sent = [s for s in macbeth_sents if len(s) == longest_len]

    return render_template('macbeth.html',
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

    # print 'percentage', percentage(text1.count('monstrous'), len(text1))

@app.route('/alice')
def alice():
    alice = gutenberg.words('carroll-alice.txt')

    alice_words = nltk.Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))

    text1 = book.text1

    lexical_diversity_percentage = get_lexical_diversity(alice)
    word_count = get_word_count(alice)
    total_word_count = get_total_word_count(alice)

    concordance_alice = text1.concordance("monstrous")

    return render_template('alice.html',
        lexical_diversity_percentage=lexical_diversity_percentage,
        word_count=word_count,
        total_word_count=total_word_count,
        concordance_alice=concordance_alice,
        alice=alice,
        text1=text1)

def lexical_div(un, total):
    return total/un

@app.route('/webtext')
def webtext():
    # print webtext.fileids()

    # print nltk.corpus.gutenberg.fileids()
    # print nltk.corpus.webtext.fileids()

    webtext = nltk.corpus.webtext
    nps_chat = nltk.corpus.nps_chat

    webtext_ids = [fileid for fileid in webtext.fileids()]
    nps_chat_ids = [fileid for fileid in nps_chat.fileids()]


    pirates = webtext.raw('pirates.txt')
    pirates_words = len(webtext.words('pirates.txt'))
    pirates_sents = len(webtext.sents('pirates.txt'))
    uniqs = len(set([w.lower() for w in webtext.words('pirates.txt')]))

    lexical_diversity = lexical_div(uniqs, pirates_words)

    # text1 = book.text1
    # pirates = webtext.raw('pirates.txt')

    return render_template('webtext.html',
        webtext_ids=webtext_ids,
        nps_chat=nps_chat_ids,
        pirates=pirates)

@app.route('/brown')
def brown():
    brown = nltk.corpus.brown

    categories = [category for category in brown.categories()]

    news_text = brown.words(categories='news')
    # frequent distribution
    fdist = nltk.FreqDist([w.lower() for w in news_text])

    most_common = fdist.most_common(50)

    # modal verbs
    modals_verbs = ['can', 'could', 'may', 'might', 'must', 'will']
    determiners = ['who', 'which', 'when', 'what', 'where', 'how']
    modal_verbs = [(modal, fdist[modal]) for modal in modals_verbs]
    determiners_pos = [(d, fdist[d]) for d in determiners]

    return render_template('brown.html',
        categories=categories,
        news_text=news_text,
        fdist=fdist,
        most_common=most_common,
        modal_verbs=modal_verbs,
        determiners_pos=determiners_pos)














