#!/usr/bin/python3
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


