#!/usr/bin/python3
#835B0032-Legacy


# %s = str()
# %r = repr()

stri = 'tHiS eXaMpLe'
print 'Place another string with a mod and s: %s' %(stri)
stri2 = 'test2'
print 'Place another string with a mod and s: %s and %s' %(stri,stri2)

print 'Place another string with a mod and s: {} this {}'.format('test1','test2')

print 'Place another string with a mod and s: {} this {}'.format('test1','test2')

print 'Place another string with a mod and s: {x} this {x}'.format(x='inserted')

print 'Floating point numbers: %10.2f' %(13.144)

print 'Floating point numbers: %1.2f' %(13.144)

print 'Here is a number: %r. Here is a string: %r' %(123.1,'hi')


print 'Object 1: {a}, Object 2: {b}, Object 3: {c}, Object 4: {d}'.format(a=1,b='two',c=12.3,d=stri)

print 'Object 1: {a}, Object 2: {b}, Object 3: {c}, Object 4: {d}, '.format(a=1,b='two',c=12.3,d=stri) + stri2




