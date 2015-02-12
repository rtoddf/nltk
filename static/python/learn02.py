import nltk

# words = 'I turned off the spectroroute'.split()
# wordlens = [(len(word), word) for word in words]
# print 'wordlens before: ', wordlens

# wordlens.sort()
# print 'wordlens after: ', wordlens

# # The underscore is just a regular Python variable, but we can use underscore by convention to indicate that we will not use its value.
# joined = ' '.join(w for (_, w) in wordlens)
# print 'joined: ', joined

# lexicon = [
# 	('the', 'det', ['Di:', 'D@']),
# 	('off', 'prep', ['Qf', 'O:f'])
# 	]
# print lexicon

# tuplized = tuple(lexicon)
# print tuplized

text = '''"When I use a word," Humpty Dumpty said in rather a scornful tone, "it means just what I choose it to mean - neither more nor less."'''

tokenize = [w.lower() for w in nltk.word_tokenize(text)]

maxie = max([w.lower() for w in nltk.word_tokenize(text)])

# The second line uses a generator expression
# faster if there is a great deal of text
maxe = max(w.lower() for w in nltk.word_tokenize(text))

print 'text: ', text
print 'tokenize: ', tokenize
print 'maxie: ', maxie
print 'maxe: ', maxe