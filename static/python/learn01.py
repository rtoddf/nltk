import nltk

s = ['tom', 'bob', 'chris', 'mary', 'bob', 'mary']
t = ['tom', 'mary', 'carrie', 'sam']

# # iterate over the items of s
# for item in s:
# 	print 'item: ', item

# # iterate over the items of s in order
# for item in sorted(s):
# 	print 'sorted: ', item

# # unique
# for item in set(s):
# 	print 'unique: ', item

# for item in reversed(s):
# 	print 'rev: ', item

# for item in set(s).difference(t):
# 	print 'diff: ', item

raw = 'Red lorry, yellow lorry, red lorry, yellow lorry.'
print 'raw: ', raw

text = nltk.word_tokenize(raw)
print 'text: ', text

fdist = nltk.FreqDist(text)
print 'fdist: ', list(fdist)