http://www.pythonforbeginners.com/dictionary/
http://www.crummy.com/software/BeautifulSoup/bs4/doc/
http://stackoverflow.com/questions/328059/create-a-list-that-contain-each-line-of-a-file
http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
http://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python
http://www.tutorialspoint.com/python/python_files_io.htm
http://effbot.org/zone/python-list.htm
https://devcenter.heroku.com/articles/getting-started-with-python
http://www.kgryte.com/blog/explorations-in-data/
http://phantomjs.org/quick-start.html
http://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States
http://avalon.law.yale.edu/subject_menus/inaug.asp
http://avalon.law.yale.edu/20th_century/eisen1.asp


convert an int to a string str(6)
%d and %f
'%.3f' %z (rounds to 3 decimal points)
'\n' - new line
'\t' - tab

z = 6
y = 'something %d' %z

d - integers
f - floats

# lists
x = []
x.append('something')
x.insert(1, 'else')
x.pop('something')
len('words')		# 5
len(list)			# returns the number of items in the list

list('ham')			# returns ['h', 'a', 'm']

# tuples - no return policy (enumerated)
x = ('ham', 4, 5)
# no remove, add, insert, etc

# dicitonaries
del sam['health']


if():
	...
elif():
	...
else:
	...

if (7) and (6):
if not (0):
# 0 is always false


x = 0
while (x < 10):
	x += 1

x, y = 0, 0
while (True):
	x += 1
	y += 2
	if(x + y > 10):
		break

# range(30) up to, but not including the number
for i in range(30):
	print i

for i in range(10, 30, 2):
	print i

# continue
for i in range(30):
	if not(i % 3):
		print i

# exception handling
# try and catch
try:
	x = 5 + 'ham'
except:
	print 'darn it'		#or pass

raise TypeError('hahahahahah')
# there are other types of errors

# finally
try:
	x = 5 + 'ham'
except ZeroDivisionError:		#specific errors you're looking for
	print 'will not print'
finally:
	print 'this'

# functions
def doesNothing():
	print 'something'

dir() lists all functions and vars, etc
local vs global vars


documenting is triple quotes
"""
some stuff
"""

print myFunc.__doc__		#let's you see documenting
















