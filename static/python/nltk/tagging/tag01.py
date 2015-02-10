import nltk
from nltk.corpus import brown

text = 'And now for something completely different'

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

# print 'tags: ', tags

text2 = 'They refuse to permit us to obtain the refuse permit'
tokens2 = nltk.word_tokenize(text2)
tags2 = nltk.pos_tag(tokens2)

# print 'tags2: ', tags2

text3 = nltk.Text(word.lower() for word in brown.words())
print text3.similar('woman')

# print 'text3: ', text3