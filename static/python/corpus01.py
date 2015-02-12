import os
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer

## create the corpus of 1965 songs from html files
corpusdir = '../../data/billboard_data/1960/billboard_1965/'
bb_1965 = PlaintextCorpusReader(corpusdir, '.*')

## get the raw text from specific songs/files
help = bb_1965.raw('help.html')
desolation_row = bb_1965.raw('desolation_row.html')

## clean the raw text to remove the p tags
clean_help = nltk.clean_html(help)
clean_desolation = nltk.clean_html(desolation_row)

# word tokenize
tokens_help = nltk.word_tokenize(clean_help)
tokens_desolation = nltk.word_tokenize(clean_desolation)

# point of speech tagging
tags_help = nltk.pos_tag(tokens_help)
tags_desolation = nltk.pos_tag(tokens_desolation)

tokenizer = RegexpTokenizer(r'\w+')

## print the unique, sorted pos tags
for item in sorted(set(tags_help)):
	print 'help tags: ', item

for item in sorted(set(tags_desolation)):
	print 'desolation row tags: ', item

# nltk.pos_tag(tokens)

# for line in clean:
# 	print line

# print clean
# print help_words

# for fileid in bb_1965.fileids():
# 	print 'fileid: ', fileid

# print bb_1965.fileids()
# print 'help: ', help