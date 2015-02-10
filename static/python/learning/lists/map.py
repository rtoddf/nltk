# use lambda if its readable and one liner - must return a value

items = [1, 2, 3, 4, 5]
words = [' apple', 'banana  ', 'pineapple    ', '  carrot  ']

def square(x): return x**2

def strip(w): return w.strip()

# squared = [square(x) for x in items]

# for x in items:
#     squared.append(x ** 2)

squared = list(map(square, items))
cubed = list(map((lambda x: x**3), items))

print 'squared: ', squared
print 'cubed: ', cubed

stripped = [word.strip() for word in words]
stripper = list(map(strip, words))

print 'words: ', words
print 'stripped: ', stripped
print 'stripper: ', stripper
