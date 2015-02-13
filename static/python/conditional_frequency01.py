import nltk
from nltk.corpus import webtext
from nltk.corpus import nps_chat
from nltk.corpus import brown

determiners = ['who', 'which', 'when', 'what', 'where', 'how']
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']

# now let's do all the genres
# We'll use NLTK's support for conditional frequency distributions
cfd = nltk.ConditionalFreqDist(
	(genre, word)
	for genre in brown.categories()
	for word in brown.words(categories=genre))

print cfd.tabulate(conditions=genres, samples=determiners)



# http://stackoverflow.com/questions/15145172/nltk-conditionalfreqdist-to-pandas-dataframe

# read up on ConditionalFreqDist at:
# http://nltk.readthedocs.org/en/latest/api/nltk.html
# there may be built in ways to return the data to chart










