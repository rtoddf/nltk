list1 = [1, 2, 12, 24, 98, 102]
list2 = [15, 24, 76, 98, 1002]

'cmp compares elements of both lists'

print cmp(list1, list2)

'''
FUNCTIONS - len, max, min
'''

print 'max value: ', max(list1)
print 'min value: ', min(list1)


'''
METHODS - append, extend, count, index, insert, remove, sort, reverse
remove only removes the first instance of the obj



pop, removes and returns the last item in the list
'''

list2.append(98)
print 'append: ', list2
print 'count: ', list2.count(98)

list2.extend([45, 45])
print 'extend list2: ', list2

print 'index: ', list2.index(76)
# print 'index: ', list2.index(103)

list2.insert(2, 49)
print 'insert list2: ', list2

# print 'pop: ', list2.pop()
# print list2

list2.remove(45)
print 'remove: ', list2

list5 = ['bob', 'cat', 'dog', 'apple']
print list5

list5.reverse()
print 'reverse list5: ', list5
list5.sort()
print 'reverse list5: ', list5

a = [66.25, 333, 333, 1, 1234.5]
a.reverse()
print a

