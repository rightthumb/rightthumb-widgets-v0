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
_.switches.register('File', '-f,-file','file.json')
_.switches.register('Password', '-password')
_.switches.register('Save', '-save','file.json')
_.switches.register('DecryptionTable', '-decryptiontable','DecryptionTable_._000000.json')
_.switches.register('Scramble', '-scramble')

_.appInfo=    {
	'file': 'unhackable.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p unhackable -build')
_.appInfo['examples'].append('p unhackable -build bible')
_.appInfo['examples'].append('p unhackable -build %tmpf4%')
_.appInfo['examples'].append('p unhackable -scramble')
_.appInfo['examples'].append('p unhackable -message "test message" -save file.json -password thePassword')
_.appInfo['examples'].append('p unhackable -file file.json -password thePassword')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p unhackable3 -message "Merry Christmas" -save secret_message.json -password JESUS -decryptiontable DecryptionTable_._000000.json')
_.appInfo['examples'].append('p unhackable3 -file secret_message.json -password JESUS')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})

if __name__ == '__main__':
	_.switches.process()

	baseKey = '{6D20F981-9E43-94B4-9483-223F7080E5FE}'
	if _.switches.isActive('Password'):
		baseKey = _.switches.value('Password')


	if not os.path.isfile(_v.myTables + _v.slash+'DecryptionTable0.json'):
		print('Missing: ' + _v.myTables + _v.slash+'DecryptionTable0.json') #
		sys.exit()



########################################################################################
if _.switches.isActive('Range'):
	theRange = int(_.switches.value('Range'))
else:
	# theRange = 100
	# theRange = 1000
	theRange = 5
	# theRange = 50
	# theRange = 50
	# theRange = 10000
def genGUID():
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	result = str(string).upper()
	result = '{' + result + '}'
	return result

def build():
	if _.switches.value('Build') == 'bible':
		bible()
		sys.exit()
	if os.path.isfile(_.switches.value('Build')):
		buildFile()
		sys.exit()
	global theRange
	data = _.getTable('DecryptionTable0.json')
	theRange = len(data[0]['char'])
	i = 0
	for d in data:
		for x in range(0,theRange):
			data[i]['ids'].append(genGUID())
		# print(data[i]['char'])
		i += 1
	_.saveTableSplitNew(data,'DecryptionTable')
########################################################################################





def newID(char):
	global data
	# global theRange
	# theRange = len(data[0]['ids']) - 1
	# print(char)
	result = ''
	i = 0
	for d in data:
		if char == data[i]['char']:
			try:
				result = data[i]['ids'][random.randint(0,len(data[i]['ids']) - 1)]
			except Exception as e:
				result = data[i]['ids'][random.randint(0,len(data[i]['ids']) - 1)]
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
	if len(ids) == 38 and ids[0] == '{' and ids[-1] == '}' and len(ids.split('-')) == 5:
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
	else:
		result = ids

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
	print(char,item) #
	print(getChar(item)) #

def percentage(percent, whole): ##############################################
	p = (percent / whole) * 100.0
	x = str(p)
	y = x.split('.')[0]    
	z = float(y)
	# print(x,y,z,p)
	# a = round(float(z),2) 
	# print(type(p),type(a))
	return p

def pData(inData,pDaTest=False):
	# print(inData)
	def genPhoKey(string):
		x = scrampleIDs(genFileID(string))
		l = x.split('-')
		m = l[len(l)-1]
		n = m.replace('}','')
		n = n.replace('A','0A')
		n = n.replace('B','B1')
		
		return n

	def syncDigits(inNu,pho):
		# print(inNu,pho)

		if genPhoKey(str(inNu)) == pho:
			result = inNu
			found = True
		else:
			found = False

		if not found:
			for x in range(1,100):
				test = inNu + x
				if genPhoKey(str(test)) == pho:
					found = True
					result = test
					break

		if not found:
			for x in range(1,100):
				test = inNu - x
				if genPhoKey(str(test)) == pho:
					found = True
					result = test
					break


		if not found:
			for x in range(99,1000):
				test = inNu + x
				if genPhoKey(str(test)) == pho:
					found = True
					result = test
					break

		if not found:
			for x in range(99,1000):
				test = inNu - x
				if genPhoKey(str(test)) == pho:
					found = True
					result = test
					break

		if not found:
			for x in range(999,10000):
				test = inNu + x
				if genPhoKey(str(test)) == pho:
					found = True
					result = test
					break

		if not found:
			for x in range(999,10000):
				test = inNu - x
				if genPhoKey(str(test)) == pho:
					found = True
					result = test
					break

		return result





	d = _.switches.value('Password')
	data = d.split(';')[0]
	t = len(data.replace('-',''))
	aData = data.split('-')

	result = []
	resultX = []
	resultY = []
	for aD in aData:
		p = percentage(len(aD),t)
		x = str(p)
		y = x.split('.')[0]    
		z = float(y)
		resultX.append(p)

	l = 0
	for rX in resultX:
		l += rX
		resultY.append(l)

	resultY[len(resultY)-1] = 100
	group = 0
	for x in range(0,inData):
		p = percentage(x,inData)
		if p >= resultY[group]:
			result.append(x)
			group += 1


	if d == data:
		spin = []
		for r in result:
			spin.append(genPhoKey(str(r)))
		tmp0 = spin[0]
		tmp1 = spin[len(spin)-1]
		spin[0] = tmp1
		spin[len(spin)-1] = tmp0
		rx = ''
		for r in spin:
			rx += r
			rx += '-'
		rx = _str.cleanLast(rx,'-')


		_.switches.fieldSet('Password','value',data + ';' + rx)
		# print('Password:',len(data + ';' + rx))
	else:
		if not pDaTest:
			_.switches.fieldSet('Password','value',data)
		we = str(d.split(';')[1])
		doKey = we.split('-')
		tmp0 = doKey[0]
		tmp1 = doKey[len(doKey)-1]
		doKey[0] = tmp1
		doKey[len(doKey)-1] = tmp0
		# print(result)
		for i,fx in enumerate(result):
			result[i] = syncDigits(fx,doKey[i])
			# print(result[i])

			
	print('Encryption databases:',len(result))


	return result
pu_File = ''
def message():
	global data
	global imported
	global baseKey
	global pu_File
	if len(_.switches.value('Save')) > 0:
		pu_File = _.switches.value('Save')
	elif len(pu_File) > 0:
		_.switches.fieldSet('Save','value',pu_File)
	p = _.switches.value('Password')
	baseKey = p.split(';')[0]
	chosenFile = chooseFile()
	# print(chosenFile)
	# print(chosenFile)
	# print(_.switches.value('Password'))
	# data = _.getLastTableSplit('DecryptionTable')
	note = _.switches.value('Message')
	# print(imported)
	if not imported:
		print(note)
	noteb = bytes(note, 'utf-8')
	encoded = base64.b64encode(noteb)
	if not imported:
		print(encoded.decode('utf-8'))
	encrypted = []
	en = encoded.decode('utf-8')
	check = genFileID(en)
	try:
		d = pData(len(en))
		cant = False
	except Exception as e:
		cant = True


	if cant:
		print('Error: pData')
		return False
	else:
	
		_last = -1
		for i,pD in enumerate(d):
			chosenFileID = genFileID(chosenFile[i])
			encrypted.append(scrampleIDs(chosenFileID))

		group = 0
		end = len(d) - 1
		data = _.getTable(chosenFile[0],'split')
		# print('data',len(data))
		# print(d)
		# sys.exit()

		for i,dat in enumerate(en):
			if not group == end:
				if not i < d[group]:
					group += 1
					data = []
					data = _.getTable(chosenFile[group],'split')
			g = newID(dat)
			if not imported:
				print(dat,g)
			encrypted.append(scrampleIDs(g))
		filex = ''
		for d in encrypted:
			# print(d)
			filex += d + '\n'
		filex = _str.cleanLast(filex,'\n')
		if _.switches.isActive('Save'):
			if len(_.switches.value('Save')) > 0:
				pu_File = _.switches.value('Save')
			elif len(pu_File) > 0:
				_.switches.fieldSet('Save','value',pu_File)
			# print(len(encrypted),_.switches.value('Save'))
			_.saveTable2(encrypted,_.switches.value('Save'))
		status = True
		if file(encrypted,check):
			status = True
		else:
			status = False
		return status
def file(confirm=[],check=''):
	global data
	global imported
	global baseKey
	if len(confirm) == 0:
		fileX = _.getTable2(_.switches.value('File'))
	else:
		fileX = confirm
	p = _.switches.value('Password')
	baseKey = p.split(';')[0]


	try:
		if len(confirm) == 0:
			d = pData(len(fileX) - len(baseKey.split('-')))
		else:
			d = pData(len(fileX) - len(baseKey.split('-')),True)
		cant = False
	except Exception as e:
		cant = True


	if cant:
		print('Error: pData')
		return False
	else:
		# print(_.switches.value('Password'))
		chosenFile = []
		for i,pD in enumerate(d):
			chosenFile.append(getFileFromID(scrampleIDs(fileX[i])))
		for pD in d:
			fileX.pop(0)
		decrypted = ''


		end = len(d) - 1
		group = 0
		data = _.getTable(chosenFile[0],'split')
		for i,dat in enumerate(fileX):
			if not group == end:
				if not i < d[group]:
					group += 1
					data = []
					data = _.getTable(chosenFile[group],'split')

			decrypted += getChar(scrampleIDs(dat))

		decryptedb = bytes(decrypted, 'utf-8')
		decoded = base64.b64decode(decryptedb)
		if len(confirm) > 0:

			# testCheck = check
			testCheck = genFileID(decrypted)

			if testCheck == check:
				status = True
			else:
				status = False

		else:
			try:
				if imported:
					text = str(decoded.decode('utf-8'))
					text = text.replace('[(n)]','\n')
					_.saveText(text,'_chat_in')

				else:
					print(decoded.decode('utf-8'))
				status = True
			except Exception as e:
				status = False
	return status


########################################################################################


def genFileID(chosenFile):
	global baseKey
	# print(baseKey)
	# print('baseKey',baseKey)
	# print(chosenFile)
	# sys.exit()
	md5 = _md5.md5(chosenFile + baseKey)
	# md5 = _md5.md5(chosenFile)
	return _md5.md52GUID(md5,True)

def chooseFile():
	# print(_v.myTables + _v.slash+'tablesets')
	dirList = os.listdir(_v.myTables + _v.slash+'tablesets')
	fileList = []
	for d in dirList:
		if d.startswith('DecryptionTable_._'):
			fileList.append({'file': d, 'sort_field': genGUID()})
	# print(fileList)
	newFileList = _.sort(fileList,'sort_field')
	result = []
	for fl in newFileList:
		result.append(fl['file'])
	return result

def getFileFromID(fileID):
	global baseKey
	# print(_v.myTables)
	# print('theID:',fileID)
	# print(_v.myTables + _v.slash+'tablesets')
	dirList = os.listdir(_v.myTables + _v.slash+'tablesets')
	fileList = []
	result = ''
	for d in dirList:
		# print(d)
		if d.startswith('DecryptionTable_._'):
			# print('_______________________________________________________ found')
			# print(genFileID(d))
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
	# print(data)
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


def bible():
	global data
	global theRange
	data = _.getText(_v.myTables + _v.slash + 'bibleRef_int.txt')
	theRange = 472
	blank = _.getTable('DecryptionTable0.json')
	bank = []
	include = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=*'
	for ids in data:
		ids = ids.replace('\n','')
		ids = ids.replace('\t','x')
		# print(ids)
		bank.append({'id': ids, 'sort_field': genGUID()})
	# sys.exit()
	# print(len(bank))
	# for d in bank:
	#     print(d)
	newBank = _.sort(bank,'sort_field')
	del bank
	del data
	data = []

	# i = 0
	# for d in blank:
	#     if blank[i]['char'] == '=':
	#         blank[i]['ids'] = eq
	#     if blank[i]['char'] == '[RETURN]':
	#         blank[i]['ids'] = rtn
	#     i += 1
	# del eq
	# del rtn
	# print(newBank)
	# print(len(newBank))

	i = 0
	for dd in blank:
		for x in range(0,theRange):
			blank[i]['ids'].append(newBank[0]['id'])
			newBank.pop(0)

		i += 1


	# print(theRange)
	# print(blank)
	_.saveTableSplitNew(blank,'DecryptionTable')


def buildFile():
	global data
	global theRange
	data = _.getText(_.switches.value('Build'))
	r = int(round(float(len(data)/66),0))
	x = r * 66
	if x > r:
		theRange = r - 1
	else:
		theRange = r
	# print(len(data))
	# print(theRange)
	blank = _.getTable('DecryptionTable0.json')
	bank = []
	include = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=*'
	for ids in set(data):
		ids = ids.replace('\n','')
		ids = ids.replace('\t','x')
		# print(ids)
		if len(ids) > 0:
			bank.append({'id': ids, 'sort_field': genGUID()})
	# sys.exit()
	# print(len(bank))
	# for d in bank:
	#     print(d)
	newBank = _.sort(bank,'sort_field')
	del bank
	del data
	data = []

	# i = 0
	# for d in blank:
	#     if blank[i]['char'] == '=':
	#         blank[i]['ids'] = eq
	#     if blank[i]['char'] == '[RETURN]':
	#         blank[i]['ids'] = rtn
	#     i += 1
	# del eq
	# del rtn
	# print(newBank)
	# print(len(newBank))

	i = 0
	for dd in blank:
		for x in range(0,theRange):
			blank[i]['ids'].append(newBank[0]['id'])
			newBank.pop(0)

		i += 1


	# print(theRange)
	# print(blank)
	_.saveTableSplitNew(blank,'DecryptionTable')


########################################################################################
imported = False
if __name__ == '__main__':
	if _.switches.isActive('Build'):
		build()
	if _.switches.isActive('Test'):
		# test()
		pData(2000)
	if _.switches.isActive('Message'):
		message()
	if _.switches.isActive('File'):
		file()
	if _.switches.isActive('Scramble'):
		scramble()


########################################################################################
# def importedAction(filename,password):

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




