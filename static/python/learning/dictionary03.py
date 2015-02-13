## Can build up a dict by starting with the the empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value-for-that-key

data = {}
data['a'] = 'alpha'
data['b'] = 'beta'
data['o'] = 'omega'

print data			## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
# print data['a']		## Simple lookup, returns 'alpha'
# data['a'] = 6		## Put new key/value into dict

# print 'a' in data

# for key in data:
# 	print key

## Get the .keys() and .values() list:
print data.keys()
print data.values()

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(data.keys()):
	print key, data[key]

## .items() is the dict expressed as (key, value) tuples
print 'something', data.items()

# the % operator works conveniently to substitute values from a dict into a string by name
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
string = 'i want %(count)d copies of %(word)s' % hash

print 'string', string