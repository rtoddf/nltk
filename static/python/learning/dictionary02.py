# data = {
# 	'key1': 'value1',
# 	'key2': 'value2',
# 	'key3': 'value3'
# }

# The methods dict.keys() and dict.values() return lists of the keys or values
# explicitly.

# for key, value in data.items():
# 	print key, value

# for key in data:
# 	print key

# Creates a new entry if the key is not already in dictionary.
# Overwrites the previous value if the key is already present.
# data = {'Name':'Zara','Age':7,'Class':'First'}

# data['age'] = 8						# update an existing entry
# data['school'] = 'DPS School'		# add a new entry

# delete a key/value
# The del operator does deletions.
data = {'a':1, 'b':2, 'c':3}
del data['b']

print data