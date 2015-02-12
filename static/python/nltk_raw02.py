import nltk
from urllib import urlopen

url = 'http://news.bbc.co.uk/2/hi/health/2284783.stm'
raw = urlopen(url).read()
clean = nltk.clean_html(raw)

html_file = open('scrape.html', 'w')
html_file.write(clean.encode('utf-8'))
html_file.close()

# A token is the technical name for a sequence of
# characters

tokens = nltk.word_tokenize(clean)
print tokens