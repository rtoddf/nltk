import nltk
from nltk.corpus import gutenberg

fileids = gutenberg.fileids()
# print 'fileids: ', fileids

emma = gutenberg.words('austen-emma.txt')

# average characters in a word: raw/words
# average word in a sentence: words/sents
# lexical diversity - num_words/num_vocab

# for fileid in fileids:
# 	num_chars = len(gutenberg.raw(fileid))
# 	num_words = len(gutenberg.words(fileid))
# 	num_sents = len(gutenberg.sents(fileid))
# 	num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
# 	print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

macbeth_sents = gutenberg.sents('shakespeare-macbeth.txt')

longest_len = max([len(s) for s in macbeth_sents])
longest_sent = [s for s in macbeth_sents if len(s) == longest_len]

print 'longest_sent: ', longest_sent