import json
import requests
import nltk

from urllib import urlopen
from pprint import pprint

from flask import Flask
from flask import render_template

from app import app
from helpers import get_lexical_diversity, get_fileids, get_categories, get_raw_text, get_text_count, get_uniqs_count, get_uniqs, get_word_count, get_total_word_count

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scraper')
def scraper():
    from bs4 import BeautifulSoup

    r = requests.get('https://www.cia.gov/library/publications/the-world-factbook/geos/countrytemplate_us.html')
    soup = BeautifulSoup(r.content)

    wrappers = soup.find_all('div', class_='CollapsiblePanel')
    
    questions = []
    all_categories = []
    all_answers = []

    for wrapper in wrappers:
        questions.append(wrapper.find_all('h2', class_='question')[0].text)
        qs = wrapper.find_all('h2', class_='question')

    for box in soup.find_all('div', class_='box'):
        categories = []
        for category in box.find_all('tr', class_='noa_light'):
            categories.append(category.find_all('a')[0].text.replace(':', ''))

            category_answers = []
            for answer in category.find_next_siblings('tr'):
                if answer.find_all('div', class_='category_data') != []:
                    the_answer = answer.find_all('div', class_='category_data')[0].text
                    category_answers.append(the_answer)

            print category.find_all('a')[0].text.replace(':', '')
            print category_answers
            print '******'

        all_categories.append(categories)

    return render_template('scraper.html',
        questions=questions,
        all_categories=all_categories)

@app.route('/gutenberg')
def gutenberg():
    from nltk.corpus import gutenberg
    file_ids = get_fileids(gutenberg)

    # average characters in a word: raw/words
    # average word in a sentence: words/sents
    # lexical diversity - num_words/num_vocab

    for fileid in file_ids:
        num_chars = len(gutenberg.raw(fileid))
        num_words = len(gutenberg.words(fileid))
        num_sents = len(gutenberg.sents(fileid))
        num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
        print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

    emma = gutenberg.words('austen-emma.txt')
    emma_len = len(emma)
    # print 'percentage', percentage(text1.count('monstrous'), len(text1))

    macbeth_sents = gutenberg.sents('shakespeare-macbeth.txt')
    macbeth_longest_len = max([len(s) for s in macbeth_sents])
    macbeth_longest_sent = [s for s in macbeth_sents if len(s) == macbeth_longest_len]

    return render_template('gutenberg.html',
        file_ids=file_ids,
        emma=emma,
        emma_len=emma_len,
        macbeth_longest_sent=macbeth_longest_sent)


@app.route('/webtext')
def webtext():
    from nltk.corpus import webtext as webtext
    from nltk.corpus import nps_chat

    # list comprehension version
    file_ids = [fileid for fileid in webtext.fileids()]
    chat_file_ids = [fileid for fileid in nps_chat.fileids()]

    pirates = webtext.raw('pirates.txt')
    pirates_words = len(webtext.words('pirates.txt'))
    pirates_sents = len(webtext.sents('pirates.txt'))
    uniqs = len(set([w.lower() for w in webtext.words('pirates.txt')]))

    lexical_diversity = lexical_div(uniqs, pirates_words)

    # import nltk.book as book
    # text1 = book.text1
    # pirates = webtext.raw('pirates.txt')

    return render_template('webtext.html',
        file_ids=file_ids,
        chat_file_ids=chat_file_ids,
        pirates=pirates)


@app.route('/brown')
def brown():
    from nltk.corpus import brown
    file_ids = get_fileids(brown)

    categories = [category for category in brown.categories()]

    news_text = brown.words(categories='news')
    # frequent distribution
    fdist = nltk.FreqDist([w.lower() for w in news_text])

    most_common = fdist.most_common(50)

    # modal verbs
    modal_verbs = ['can', 'could', 'may', 'might', 'must', 'will', 'shall', 'should', 'would']
    determiners = ['who', 'which', 'when', 'what', 'where', 'how']
    modal_verbs_frequency = [(modal, fdist[modal]) for modal in modal_verbs]
    determiners_pos = [(d, fdist[d]) for d in determiners]

    return render_template('brown.html',
        file_ids=file_ids,
        categories=categories,
        news_text=news_text,
        fdist=fdist,
        most_common=most_common,
        modal_verbs=modal_verbs,
        modal_verbs_frequency=modal_verbs_frequency,
        determiners_pos=determiners_pos) 



@app.route('/inaugural')
def inaugural():
    from nltk.corpus import inaugural
    file_ids = get_fileids(inaugural)
    speech = file_ids[-1]
    
    raw_text = get_raw_text(inaugural, speech)
    text_count = get_text_count(inaugural, speech)
    uniqs_count = get_uniqs_count(inaugural, speech)
    uniqs = get_uniqs(inaugural, speech)

    return render_template('inaugural.html',
        file_ids=file_ids,
        raw_text=raw_text,
        text_count=text_count,
        uniqs_count=uniqs_count,
        uniqs=uniqs)
    # reuters_categories = get_categories(reuters)
    # reuters_categories=reuters_categories

@app.route('/reuters')
def reuters():
    from nltk.corpus import reuters
    categories = [category for category in reuters.categories()]

    return render_template('reuters.html',
        categories=categories)

# movie this to gutenberg
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
