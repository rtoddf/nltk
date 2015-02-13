import string
import json
from collections import Counter
from bs4 import BeautifulSoup

orig = []
translation = []
exclude = ['i', 'me', 'my', 'myself', 'we', 'us', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'whose', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'will', 'would', 'should', 'can', 'could', 'ought', 'i\'m', 'you\'re', 'he\'s', 'she\'s', 'it\'s', 'we\'re', 'they\'re', 'i\'ve', 'you\'ve', 'we\'ve', 'they\'ve', 'i\'d', 'you\'d', 'he\'d', 'she\'d', 'we\'d', 'they\'d', 'i\'ll', 'you\'ll', 'he\'ll', 'she\'ll', 'we\'ll', 'they\'ll', 'isn\'t', 'aren\'t', 'wasn\'t', 'weren\'t', 'hasn\'t', 'haven\'t', 'hadn\'t', 'doesn\'t', 'don\'t', 'didn\'t', 'won\'t', 'wouldn\'t', 'shan\'t', 'shouldn\'t', 'can\'t', 'cannot', 'couldn\'t', 'mustn\'t', 'let\'s', 'that\'s', 'who\'s', 'what\'s', 'here\'s', 'there\'s', 'when\'s', 'where\'s', 'why\'s', 'how\'s', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'upon', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'say', 'says', 'said', 'shall']

books = [
	'john_3',
	'a_wrinkle_in_time',
	'alice_in_wonderland',
	'green_eggs_and_ham',
	'peter_pan',
	'the_gettysburg_address',
	'the_great_gatsby',
	'the_legend_of_sleepy_hollow',
	'the_time_machine',
	'the_velveteen_rabbit',
	'to_kill_a_mockingbird',
	'where_the_wild_things_are',
	'whitefang'
]

which_book = books[0]

# open url instead

with open('../../data/books/' + which_book + '.html') as infile:
    for line in infile:
        orig.append(line)

orig = ''.join(orig)
soup = BeautifulSoup(orig)

arr = soup.get_text().split()

for word in arr:
    word = word.strip(string.punctuation).lower()
    if word not in exclude:
        translation.append(word)

worddict = Counter(translation).most_common(10)
wordjson = json.dumps(worddict, separators=(',', ':'), sort_keys=True)

with open('../../data/books_data/' + which_book + '.json', 'w') as outfile:
  json.dump(worddict, outfile)

page = open('../../data/books/' + which_book + '.html')
souper = BeautifulSoup(page)
tags = souper.findAll('img')

for img in souper('img'):
    souper.img.extract()

# for br in souper('br'):
#     souper.br.extract()

with open('../../data/books/' + which_book + '.html', 'w') as myFile:
	souper = str(souper)
	myFile.write(souper)