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

import uuid
import simplejson as json
import random

import os
import sys

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import _rightThumb._md5 as _md5

import base64

_.switches.register('Build', '-build')
_.switches.register('Test', '-test')
_.switches.register('Range', '-range')
_.switches.register('Message', '-message')
_.switches.register('Save', '-save','file.json')
_.switches.register('File', '-file','file.json')
_.switches.register('DecryptionTable', '-decryptiontable','DecryptionTable_._000000.json')
_.switches.register('Scramble', '-scramble')
_.switches.register('Password', '-password')

_.appInfo=    {
	'file': 'unhackable.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p unhackable -build')
_.appInfo['examples'].append('p unhackable -scramble')
_.appInfo['examples'].append('p unhackable -message "test message" -save file.json -password thePassword')
_.appInfo['examples'].append('p unhackable -file file.json -password thePassword')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


_.switches.process()

baseKey = '{6D20F981-9E43-94B4-9483-223F7080E5FE}'
if _.switches.isActive('Password'):
	baseKey = _.switches.value('Password')

# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass


########################################################################################
if _.switches.isActive('Range'):
	theRange = int(_.switches.value('Range'))
else:
	# theRange = 100
	# theRange = 5
	# theRange = 50
	theRange = 10000
def genGUID():
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	result = str(string).upper()
	result = '{' + result + '}'
	return result

def build():
	global theRange
	data = _.getTable('DecryptionTable0.json')
	i = 0
	for d in data:
		for x in range(0,theRange):
			data[i]['ids'].append(genGUID())
		print(data[i]['char'])
		i += 1
	_.saveTableSplitNew(data,'DecryptionTable')
########################################################################################
def newID(char):
	global data
	# print(char)
	result = ''
	i = 0
	for d in data:
		if char == data[i]['char']:
			try:
				result = data[i]['ids'][random.randint(0,theRange - 1)]
			except Exception as e:
				result = data[i]['ids'][random.randint(0,theRange - 1)]
			break
		i += 1
	return result
def getChar(ids):
	global data
	char = '*nope'
	i = 0
	for d in data:
		if ids in data[i]['ids']:
			char = data[i]['char']
		i += 1
	return char



def scrampleIDs(ids):
	result = ''
	
	i=0
	for char in ids:
		if i == 1:
			result += ids[36]
		elif i == 2:
			result += ids[35]
		elif i == 8:
			result += ids[20]
		elif i == 36:
			result += ids[1]
		elif i == 35:
			result += ids[2]
		elif i == 20:
			result += ids[8]
		elif i == 10:
			result += ids[15]
		elif i == 11:
			result += ids[16]
		elif i == 12:
			result += ids[17]
		elif i == 13:
			result += ids[18]
		elif i == 15:
			result += ids[10]
		elif i == 16:
			result += ids[11]
		elif i == 17:
			result += ids[12]
		elif i == 18:
			result += ids[13]
		else:
			result += char
		i+=1

	return result





def test():
	global theRange
	global data
	data = _.getLastTableSplit('DecryptionTable')

	if len(_.switches.value('Test')) > 0:
		char = _.switches.value('Test')
	else:
		char = 'A'

	item = newID(char)
	print(char,item)
	print(getChar(item))

def message():
	global data
	chosenFile = chooseFile()
	# print(chosenFile)
	chosenFileID = genFileID(chosenFile)
	data = _.getTable(chosenFile)
	# data = _.getLastTableSplit('DecryptionTable')
	note = _.switches.value('Message')
	print(note)
	noteb = bytes(note, 'utf-8')
	encoded = base64.b64encode(noteb)
	print(encoded.decode('utf-8'))
	encrypted = []
	# print(chosenFileID,'test')
	encrypted.append(scrampleIDs(chosenFileID))
	for d in encoded.decode('utf-8'):
		g = newID(d)
		print(d,g)
		encrypted.append(scrampleIDs(g))
	file = ''
	for d in encrypted:
		# print(d)
		file += d + '\n'
	file = _str.cleanLast(file,'\n')
	if _.switches.isActive('Save'):
		# _.saveText(file,_.switches.value('Save'))
		_.saveTable2(encrypted,_.switches.value('Save'))
	decrypted = ''
	encrypted.pop(0)
	print()
	# print(encrypted)
	for d in encrypted:
		g = getChar(scrampleIDs(d))
		# print(g)
		decrypted += g
	print(decrypted)
	decryptedb = bytes(decrypted, 'utf-8')
	decoded = base64.b64decode(decryptedb)
	print(decoded.decode('utf-8'))
	# print(decoded)

def file():
	global data
	file = _.getTable2(_.switches.value('File'))
	data = _.getTable(getFileFromID(scrampleIDs(file[0])))
	# print(getFileFromID(file[0]))
	file.pop(0)
	# print(file)
	decrypted = ''
	for d in file:
		decrypted += getChar(scrampleIDs(d))
	# print(decrypted)
	decryptedb = bytes(decrypted, 'utf-8')
	decoded = base64.b64decode(decryptedb)
	print(decoded.decode('utf-8'))

########################################################################################


def genFileID(chosenFile):
	global baseKey
	md5 = _md5.md5(chosenFile + baseKey)
	return _md5.md52GUID(md5,True)

def chooseFile():
	dirList = os.listdir(_v.myTables)
	fileList = []
	for d in dirList:
		if d.startswith('DecryptionTable_._'):
			fileList.append({'file': d, 'sort_field': genGUID()})
	# print(fileList)
	newFileList = _.sort(fileList,'sort_field')
	return newFileList[0]['file']

def getFileFromID(fileID):
	dirList = os.listdir(_v.myTables)
	fileList = []
	result = ''
	for d in dirList:
		if d.startswith('DecryptionTable_._'):
			if genFileID(d) == fileID:
				result = d
	if result == '':
		print('Bad Password')
		sys.exit()
	return result

########################################################################################
############################################## might need to go up a digit in range
def scramble():
	global data
	global theRange
	data = _.getLastTableSplit('DecryptionTable')
	theRange = len(data[0]['ids'])
	blank = _.getTable('DecryptionTable0.json')
	bank = []
	include = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
	i = 0
	for d in data:
		if data[i]['char'] == '=':
			eq = data[i]['ids']
		if data[i]['char'] == '[RETURN]':
			rtn = data[i]['ids']
		if data[i]['char'] in include:
			# print(data[i]['char'])
			for ids in data[i]['ids']:
				# print(ids)
				bank.append({'id': ids, 'sort_field': genGUID()})
		i += 1
	# print(len(bank))
	# for d in bank:
	#     print(d)
	newBank = _.sort(bank,'sort_field')
	del bank
	del data
	data = []

	i = 0
	for d in blank:
		if blank[i]['char'] == '=':
			blank[i]['ids'] = eq 
		if blank[i]['char'] == '[RETURN]':
			blank[i]['ids'] = rtn
		i += 1
	del eq
	del rtn
	# print(newBank)
	# print(len(newBank))

	i = 0
	for dd in blank:
		if blank[i]['char'] in include:
			# print(nb['id'])
			for x in range(0,theRange):
				blank[i]['ids'].append(newBank[0]['id'])
				newBank.pop(0)
			# if not len(blank[i]['ids']) == theRange:

		i += 1


	# print(theRange)
	# print(blank)
	_.saveTableSplitNew(blank,'DecryptionTable')
########################################################################################
if __name__ == '__main__':
	if _.switches.isActive('Build'):
		build()
	if _.switches.isActive('Test'):
		test()
	if _.switches.isActive('Message'):
		message()
	if _.switches.isActive('File'):
		file()
	if _.switches.isActive('Scramble'):
		scramble()


########################################################################################

# b table
# del DecryptionTable_._000*

# p unhackable -build
# p unhackable -scramble

# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble



# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble
# p unhackable -scramble


# b mdt
# p unhackable -message "test message" -save file.json

# done




