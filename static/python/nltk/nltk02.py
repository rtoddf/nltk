import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.corpus import nps_chat

# print gutenberg.fileids()
# print brown.fileids()
# print webtext.fileids()
# print nps_chat.fileids()

# alice = nltk.Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))

# alice = nltk.Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))

alice = gutenberg.words('carroll-alice.txt')

print alice

# print 'alice: ', alice.concordance('alice')
# print len(alice)

# print brown.categories()
# print brown.words(categories='government')
