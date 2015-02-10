import nltk
from nltk.corpus import reuters
from nltk.corpus import inaugural

# print reuters.fileids()
# print reuters.categories()

# print inaugural.fileids()
# years = [fileid[:4] for fileid in inaugural.fileids()]
# print years

# cfd = nltk.ConditionalFreqDist(
# 	(target, fileid[:4])
# 	for fileid in inaugural.fileids()
# 	for w in inaugural.words(fileid)
# 	for target in ['america', 'citizen']
# 	if w.lower().startswith(target))

# cfd.plot()

help(nltk.corpus.reader)