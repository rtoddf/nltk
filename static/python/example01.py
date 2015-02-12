import string
import json

# from collections import Counter
from bs4 import BeautifulSoup

orig = []

with open('text/text01.html') as infile:
	for line in infile:
		orig.append(line)

orig = ''.join(orig)
soup = BeautifulSoup(orig)
arr = soup.get_text().split()

# list comprehension
someLen = len(set([ word.lower() for word in arr if len(word) > 5 ]))
print someLen

# for word in arr:
# 	if len(word) > 5:
# 		print word

