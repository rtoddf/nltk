import string
import json
from collections import Counter
from bs4 import BeautifulSoup

orig = []
translation = []
exclude = ['i', 'me', 'my', 'myself', 'we', 'us', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'whose', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'will', 'would', 'should', 'can', 'could', 'ought', 'i\'m', 'you\'re', 'he\'s', 'she\'s', 'it\'s', 'we\'re', 'they\'re', 'i\'ve', 'you\'ve', 'we\'ve', 'they\'ve', 'i\'d', 'you\'d', 'he\'d', 'she\'d', 'we\'d', 'they\'d', 'i\'ll', 'you\'ll', 'he\'ll', 'she\'ll', 'we\'ll', 'they\'ll', 'isn\'t', 'aren\'t', 'wasn\'t', 'weren\'t', 'hasn\'t', 'haven\'t', 'hadn\'t', 'doesn\'t', 'don\'t', 'didn\'t', 'won\'t', 'wouldn\'t', 'shan\'t', 'shouldn\'t', 'can\'t', 'cannot', 'couldn\'t', 'mustn\'t', 'let\'s', 'that\'s', 'who\'s', 'what\'s', 'here\'s', 'there\'s', 'when\'s', 'where\'s', 'why\'s', 'how\'s', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'upon', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'say', 'says', 'said', 'shall']

addresses = [
	'1789_washington',
	'1793_washington',
	'1953_eisenhower',
	'1957_eisenhower',
	'1961_kennedy',
	'1965_johnson',
	'1969_nixon',
	'1973_nixon',
	'1977_carter',
	'1981_reagan',
	'1985_reagan',
	'1989_bush',
	'1993_clinton',
	'1997_clinton',
	'2001_bush',
	'2005_bush',
	'2009_obama'
]

address = addresses[1]

with open('../../data/addresses/' + address + '.html') as infile:
	for line in infile:
		orig.append(line)

print 'orig', orig

orig = ''.join(orig)
soup = BeautifulSoup(orig)

arr = soup.get_text().split()

for word in arr:
	word = word.strip(string.punctuation).lower()
	if word not in exclude:
		translation.append(word)

worddict = Counter(translation).most_common(10)
wordjson = json.dumps(worddict, separators=(',', ':'), sort_keys=True, indent=4)

with open('../../data/addresses_data/' + address + '.json', 'w') as outfile:
	json.dump(worddict, outfile)