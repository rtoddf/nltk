from __future__ import division
import nltk
from nltk.book import *

# text1: Moby Dick by Herman Melville 1851
# text2: Sense and Sensibility by Jane Austen 1811
# text3: The Book of Genesis
# text4: Inaugural Address Corpus
# text5: Chat Corpus
# text6: Monty Python and the Holy Grail
# text7: Wall Street Journal
# text8: Personals Corpus
# text9: The Man Who Was Thursday by G . K . Chesterton 1908

def lexical_diversity(text):
	return len(text) / len(set(text))

def percentage(count, total):
	return 100 * count/total

print 'moby dick', lexical_diversity(text1)
print 'percentage', percentage(text1.count('monstrous'), len(text1))
print 'count for monstrous', text1.count('monstrous')
print 'moby dick count', len(text1)