'''
When there are a lot of parameters it is easy to get confused
about the correct order. Instead we can refer to parameters by name,
and even assign them a default value just in case one was not provided
by the calling program. Now the parameters can be specified in any order,
and can be omitted.
'''

def repeat(msg='<empty>', num=1):
	return msg * num

# print repeat(num=3)
# print repeat(msg='Alice')
# print repeat(num=5, msg='Alice')

# args are unnamed arguments, and must come first
# kwargs are named arguments and come second
def generic(*args, **kwargs):
	print 'args: ', args
	print 'kwargs: ', kwargs

print generic(1, 'African swallow', monty='python')

song = [['four', 'calling', 'birds'],
		['three', 'French', 'hens'],
		['two', 'turtle', 'doves']]

zip1 = zip(song[0], song[1], song[2])
zip2 = zip(*song)

print zip1
print zip2
