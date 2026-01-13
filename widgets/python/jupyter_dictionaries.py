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

# 835B0032-Legacy
data = {"name": "John Smith", "hometown": {"name": "New York", "id": 123},"test":'this'}

print(data.keys())
print(data['hometown'].keys())

print(data.values())
# print(data.index('name'))
# print('\t' + data.iterkeys().next()) # works with ver2
test_var = data.keys()

##############################################################
dictionary_test = {}
dictionary_test[0] = 55555555555555555555
# print(count(dictionary_test))
# dictionary_test[] = 'test'
print(dictionary_test)


##############################################################
def keyList(dictionary):
	# print dictionary.keys()
	thisKeyset = dictionary.keys()
	# result = thisKeyset[2]
	result = {}
	# result.push(123)
	i=0
	for keyItem in thisKeyset:

		print(keyItem)
	#     result.append(keyItem)
		try:
			subItem = keyList(dictionary[keyItem])
			result[i] = {'label':keyItem,'data':subItem}
			# result.append(dictionary[keyItem].keys())
		except Exception as e:
			result[i] = {'label':keyItem,'data':'null'}
			# print('test')
		i+=1
	return result

def keyList2(dictionary):
	# print dictionary.keys()
	thisKeyset = dictionary.keys()
	# result = thisKeyset[2]
	result = '{'
	# result.push(123)
	i=0
	for keyItem in thisKeyset:

		print(keyItem)
	#     result.append(keyItem)
		try:
			subItem = keyList2(dictionary[keyItem])
			result[i] = ',' + keyItem + ':' + subItem
			# result.append(dictionary[keyItem].keys())
		except Exception as e:
			result[i] = {'label':keyItem,'data':'null'}
			# print('test')
		i+=1
	return result


new_list = keyList(data)
print('')
print(new_list)
print('---------------------- END')
# print(extractLabels(new_list))
print('')

##############################################################


print(test_var)

dataTuple = ("name", "John Smith", "hometown", 123)

print(dataTuple)

print(dataTuple.index(123))

print('---------------------- END')
print('---------------------- END')
print('---------------------- END')

d = {'simple_key':'hello'}
# Grab 'hello'
print(d.index('hello'))