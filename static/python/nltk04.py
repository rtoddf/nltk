import nltk
from nltk.corpus import webtext
from nltk.corpus import nps_chat
from nltk.corpus import brown 

# for fileid in webtext.fileids():
# 	print fileid, webtext.raw(fileid)[:65]

# for fileId in nps_chat.fileids():
# 	print fileId

pirates = webtext.raw('pirates.txt')
pirates_char = len(webtext.raw('pirates.txt'))
pirates_words = len(webtext.words('pirates.txt'))
pirates_sents = len(webtext.sents('pirates.txt'))
print 'pirates_char: ', pirates_char, 'pirates_words: ', pirates_words, 'pirates_sents: ', pirates_sents, 'avg char per word: ', int(pirates_char/pirates_words), 'avg words per sentence: ', int(pirates_words/pirates_sents)

uniqs = len(set([w.lower() for w in webtext.words('pirates.txt')]))

def lexical_div(un, total):
	return total/un

print 'lexical diversity: ', lexical_div(uniqs, pirates_words)

# brown_categories = brown.categories()
# for genre in brown_categories:
# 	print genre

news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
# modal verbs
modals = ['can', 'could', 'may', 'might', 'must', 'will']
determiners = ['who', 'which', 'when', 'what', 'where', 'how']
for m in modals:
	print m + ':', fdist[m]

for d in determiners:
	print d + ':', fdist[d]

# now let's do all the genres
# We'll use NLTK's support for conditional frequency distributions
cfd = nltk.ConditionalFreqDist(
	(genre, word)
	for genre in brown.categories()
	for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
cfd.tabulate(conditions=genres, samples=determiners)














