from __future__ import division
import nltk
from nltk.book import *

def lexical_diversity(text):
    return len(text) / len(set(text))

def percentage(count, total):
    return 100 * count/total

def get_lexical_diversity(self):
    return lexical_diversity(text1)
