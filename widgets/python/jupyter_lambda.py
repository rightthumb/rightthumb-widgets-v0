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

def square(num): return num**2
print(square(2))


rev = lambda s: s[::-1]
print(rev('hello'))


adder = lambda x,y : x+y
print(adder(2,3))


print('-----------------------------')
# **Use for, split(), and if to create a Statement that will print out words that start with 's':**
anotherTest = lambda st: [print(x) for x in st.split(' ') if x[0] == 's' and len(x) > 1]
anotherTest('Print only the words that start with s in this sentence')