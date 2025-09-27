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


my_file = open('test.txt')
print my_file.read()
my_file.seek(0)
print my_file.read()

print '----------'

my_file2 = open('test2.txt','w+')
my_file2.write('This is a new line')

my_file2 = open('test2.txt')
print my_file2.read()

print '--------------------------------'

for line in open('test.txt'):
	print line

print '----------'

i=0
for one_liner in open('test.txt'):
	print 'Line: {} = {}'.format(i,one_liner)
	i+=1