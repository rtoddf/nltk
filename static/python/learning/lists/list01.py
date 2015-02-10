# http://www.tutorialspoint.com/python/python_lists.htm

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

# list values can be accessed by their indices

print 'the list values can be accessed with indices: ', list1[1]
print 'from list 2: ', list2[4]

year_list = [2000, 2002, 2003, 2004, 2005]
print 'year list: ', year_list

# you can update the list by calling the index and the new value
year_list[1] = 2001
print 'year list after: ', year_list

# use del list[i] to deleted an item
del year_list[0]
print 'after delete: ', year_list

'''
Basic operations
Lists respond to the + and * operators much like strings;
they mean concatenation and repetition here too,
except that the result is a new list, not a string.
'''

list_nums1 = [1, 2, 12, 24, 98, 102]
list_nums2 = [15, 24, 76, 98, 1002]

# length
print 'length: ', len(list_nums1)

# concatenation
list_add = list_nums1 + list_nums2
print 'list_add: ', list_add

# repetition
list_mult = ['help']
print list_mult*4

# membership
print 24 in list_nums1

bobs = ['Bobby', 'Bob', 'Robert', 'Bobbie', 'Bobberino']
print 'whole list: ', bobs
print 'from the last: ', bobs[-1]
print 'starting with: ', bobs[1:]
print 'range, up to but not including: ', bobs[1:3]
