# this is a list
myList = ['first', 'second', 'third']

# this is a dictionary
myDict = {0: 'first', 1: 'second', 2: 'third'}

# empty declaration plus assignment of key-value pair
emptyDict = {}
emptyDict['key4'] = 'value4'

# accessing/getting values
data = {'name': 'zara', 'age': 7, 'class': 'first'}

# get all keys
print data.keys()

# get all values
print data.values()

# prints name and age
print 'name: ', data['name']
print 'age: ', data['age']

# od = collections.OrderedDict(sorted(new_dict.items()))
# print od