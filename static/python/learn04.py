import nltk
from nltk.corpus import brown

# print brown.words()

def search1(substring, words):
	result = []
	for word in words:
		if substring in word:
			result.append(word)
	return result

def search2(substring, words):
	for word in words:
		if substring in word:
			yield word

# print 'search1: '
# for item in search1('zz', brown.words()):
# 	print item

print 'search2: '
for item in search2('zz', brown.words()):
	print item