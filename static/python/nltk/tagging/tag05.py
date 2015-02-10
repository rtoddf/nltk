pos = {}
pos['colorless'] = 'ADJ'
pos['ideas'] = 'N'
pos['sleep'] = 'V'
pos['furiously'] = 'ADV'

# print pos['ideas']

## to just find the keys, we can convert the dictionary to a list
## or use the dictionary in a context where a list is expected, as the parameter of sorted(), or in a for loop

print list(pos)
print sorted(pos)
print [w for w in pos if w.endswith('s')]

## As well as iterating over all keys in the dictionary with a for loop, we can use the for loop as we did for printing lists

for word in sorted(pos):
	print word + ':', pos[word]

print pos.keys()
print pos.values()
print pos.items()

for key, val in sorted(pos.items()):
	print key + ':', val