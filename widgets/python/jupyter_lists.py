#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

#835B0032-Legacy

my_list0 = [1,2,3,4,5,6]
my_list1 = ['A string',23,100.232,'o']

print len(my_list1)
print my_list1

my_list1.append(my_list0)

print len(my_list1)
print my_list1

print my_list1[1:]
print my_list1[:2]
print my_list1[0]
print my_list1[4]
print my_list1[4][1:]
print my_list1[4][1:3]


poped = my_list1.pop()
print len(my_list1)
print my_list1
print 'Popped {}'.format(poped)

poped = my_list1.pop()
print len(my_list1)
print my_list1
print 'Popped {}'.format(poped)

poped = my_list1.pop()
print len(my_list1)
print my_list1
print 'Popped {}'.format(poped)


name = {}

name['first'] = 'Scott'
name['last'] = 'Reph'

print name

print 'My name is {} {}'.format(name['first'],name['last'])

name['middle'] = 'T'

print name

print 'My name is {} {} {}'.format(name['first'],name['middle'],name['last'])

print '-----------------------------------'

new_list = ['a','e','x','b','c']

print new_list
new_list.reverse()
print new_list
new_list.sort()
print new_list
new_list.reverse()
print new_list
new_list.sort()
print new_list

print '-----------------------------------'

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

print matrix

first_col = [row[0] for row in matrix]

print first_col

cell_example = matrix[2][1]

print cell_example

print '-----------------------------------'

print new_list
print new_list.count('a')
print len(new_list)