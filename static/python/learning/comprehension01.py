# http://www.pythonforbeginners.com/lists/list-comprehensions-in-python/

# x = [i for i in range(10)]
# print x

# squares = [x**2 for x in range(10)]
# print squares

# list1 = [5, 6, 7]
# multiplied = [i*3 for i in list1]
# print multiplied

# list_of_words = ["this","is","a","list","of","words"]
# first_letters = [word[0] for word in list_of_words]
# print first_letters

def double(x):
    return x*2

def square(x):
    return x**2

doubles = [double(i) for i in range(10)]
print 'doubles: ', doubles

squares = [square(i) for i in range(10)]
print 'squares: ', squares

square2 = [square(i) for i in range(10) if i%2 == 0]
print 'square2: ', square2

square3 = [square(i) for i in range(20) if i%3 == 0]
print square3
