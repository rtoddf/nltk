import nltk
from nltk.corpus import brown

alice = nltk.Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))

print 'alice: ', alice.concordance('alice')
print len(alice)

print brown.categories()
print brown.words(categories='government')
