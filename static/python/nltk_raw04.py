import os

directory = os.listdir('.')
print directory

url = '../../data/topsongs/help.html'
f = open(url)
raw = f.read()

print raw

# for line in raw:
# 	print line