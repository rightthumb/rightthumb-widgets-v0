#!/usr/bin/python3
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