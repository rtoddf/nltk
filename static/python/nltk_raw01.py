import nltk
from urllib import urlopen

url = 'http://www.gutenberg.org/files/2554/2554.txt'
raw = urlopen(url).read()
# print type(raw)
# print len(raw)
# print raw[:175]

tokens = nltk.word_tokenize(raw)
# print type(tokens)
# print len(tokens)
# print tokens[:175]

text = nltk.Text(tokens)
# print type(text)
# print text[1020:1060]
print text.collocations()

# The find() and rfind() ("reverse find") methods help us get the right index values to use for slicing the string
print raw.find('PART I')
print raw.rfind('End of Project Gutenberg\'s Crime')
# We overwrite raw with this slice
raw = raw[5338:1157743]
print raw.find('PART I')