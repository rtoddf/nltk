from urllib import urlopen

url = "http://www.rtodd.net/index.html"
html = urlopen(url).read()

print html[:60]

with open('files/index.html', 'w') as text_file:
    text_file.write(html)
