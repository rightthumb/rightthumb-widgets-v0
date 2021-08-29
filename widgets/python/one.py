#!/usr/bin/python3
# import sys
# print(__name__)
# print(type(__name__))
# sys.exit()

test = 'one '
test2 = test.join('two')
test3 = ''.join('two')
test = 'one'
test4 = ' '.join([test,'two'])
print(test)
print(test2)
print(test3)
print(test4)


test =  {'2', '1', '3'}
s = ', '
print(s.join(test))

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))