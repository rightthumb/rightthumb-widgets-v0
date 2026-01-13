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

#A1695618-Converted

# https://www.youtube.com/watch?v=2LOHY-HsYHc
print("------------")
print(3 + 12)
print(42 - 21)
print(3 * 5)
print(9 + 12 - 8 + 72)
print(2 * 9 / 3)
print(2 * ((9/3)+2))
print(2 * (9/3)+2)
print(2 * 9/3+2)

print("------------")
print(2 < 3)
print("----")

testVar = "this"

if testVar == "this":
	print("true")
else:
	print("false")
	
	
	
	
	print("THIS IS A TAB TEST (4 space)")
	
	
print("------------")
str (2)
testVar = "from var"
print("this " + str (2) + " more text " + testVar)

test = "this " + str (2) + " more text " + testVar

print(test)


print("------------")
print('Hello\u0020World !') # unicode

print("")
print("")

print("------------") #array
print("array") 
print("")
vec = [137.5,9,13]
print(vec)
print(vec[0])

print("----") ###########

i = 0
for item in vec:
	print("array item " + str(i) + ": " + str(item))
	i += 1

print("----") ###########
# https://snakify.org/lessons/two_dimensional_lists_arrays/
print("multidimensional array (two)")
print("")
name = "generic string example"
vec = [["my string" ,1, 9, 3],[3,7,"sample",5], [2, name, 4, 5, 6]]
print(vec[0][0])
print(vec[0][2])
print("----")
i = 0
ii = 0

for item in vec:
	print("" + str(i))
	for subItem in item:
		print("array item [" + str(i) + "][" + str(ii) + "]: " + str(subItem))
		ii += 1
	i += 1
	ii = 0


print("------------")

testVar = "Dumbledore"
print(testVar)
print(testVar[0])
print(testVar[0:3])
print(testVar[6:10])


print("------------") #for

for i in range(4):
	print(i)
print("----")
for i in range(3,8):
	print(i)
print("----")

for i in range(1, 102, 20):
	print(i)


print("------------") #loops
# https://www.tutorialspoint.com/python/python_loops.htm
print("Loops")
print("")
i = 0
while (i < 3):
   print('Loop: ', i)
   i = i + 1

print("--") #loops #for
fruits = ['banana', 'apple',  'mango']
print(str(    len(fruits)    ) + " items")
for index in range(len(fruits)):
   print('Fruit:', fruits[index])

print("--")

for item in fruits:
	print(item)
print("----") #loops #break
for letter in 'Python':     # First Example
   if letter == 'h':
	break
   print('Letter :', letter)
print("--")
var = 10                    # Second Example
while var > 0:              
   print('Value :', var)
   var = var -1
   if var == 5:
	break
print("----") #loops #continue ( skips )
for letter in 'Python':     # First Example
   if letter == 'h':
	continue
   print('Letter :', letter)
print("--")
var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var >= 3 and var < 7:
		print("-")
		continue

   print('Value :', var)
print("----") #loops #pass ( function placeholder without skip )
for letter in 'Python': 
   if letter == 'h':
	pass
	print('This is pass block')
   print('Current Letter :', letter)




print("------------") #function

def function_name( str ):
   print(str)
   return

function_name("Function Success")

print("----")
def doMe(str):
	return str

doMe("Return instead of print") #no_print
print(doMe("Return instead of print"))


print("----") #function #type

def beverage(drink):
	if type(drink) == type(""):
		print("Have you had a cup of " + drink + " today??")
	else:
		print("Please input string")
	return drink

print(beverage(1))
print("-")
print(beverage("coffee"))


print("------------") #