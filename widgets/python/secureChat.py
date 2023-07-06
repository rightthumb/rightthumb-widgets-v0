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

import os
# import sys
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import uuid
import random

# _.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.switches.register('IP', '-ip','192.168.1.10')
_.switches.register('Port', '-port','10000')
_.switches.register('Message', '-message','this is a test message')
_.switches.register('Table', '-table','tableName.json')
_.switches.register('File', '-f,-file','file.zip')
_.switches.register('Encrypt', '-encrypt')
_.switches.register('Auto', '-auto')
_.switches.register('Secure', '-secure,-unhackable','password')

_.switches.register('Chat', '-chat','_chat_out')
_.switches.register('DBMax', '-dbmax','200')

# chatFile = '_chat_out'


_.appInfo=    {
	'file': 'secureChat.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}


_.appInfo['examples'].append('')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p secureChat -ip 192.168.1.10 -port 10000 -auto -encrypt -file file.json -chat _chat_out -secure 777')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p secureChat -ip 192.168.1.10 -port 10000 -auto -encrypt -file file.json -chat _chat_out -secure 8E74877F-F62C-8CF6-07E4-9F54B3831007')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p secureChat -ip 192.168.1.10 -port 10000 -auto -encrypt -file file.json -chat _chat_out -secure auto -dbmax 100')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p secureChat -ip 192.168.1.10 -port 10000 -auto -encrypt -file file.json -chat _chat_out -secure auto')
# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


_.switches.process()




def genUUID():
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	return string
def genPassword():
	global autoPass
	global chatCnt

	def genKey(lo):
		key = genUUID()
		iw = 0
		lo = lo + 15
		while iw < lo:
			iw += 1
			key += genUUID()

		key = key.replace('{','')
		key = key.replace('}','')
		key = key.replace('-','')
		return key
	def genLo():
		dirList = os.listdir(_v.myTables + _v.slash+'tablesets')
		fileList = []
		for d in dirList:
			if d.startswith('DecryptionTable_._'):
				fileList.append(d)
		
		mi = 4
		ma = len(fileList)
		if ma == 3:
			mi = 3
		elif ma == 2:
			mi = 2


		# print('chatCnt',chatCnt)
		if chatCnt > 1000 and ma > 6:
			mi = 6

		
		if chatCnt > 10000:
			mix = float(ma / 2)
			mi = int(str(mix).split('.')[0])
			# print('mi:',mi)

		if ma <= 5:
			lo = ma
		else:
			if _.switches.isActive('DBMax'):
				ma = int(_.switches.value('DBMax'))
				if mi > ma:
					mi = int(ma/2)
				
				# print(ma)
				# sys.exit()
			# print(mi,ma)
			lo = random.randint(mi,ma)
			# print(lo)
		if chatCnt < 30:
			lo = 2
		elif chatCnt < 50:
			lo = 3
		elif chatCnt < 100:
			lo = 4
		if lo > ma:
			lo = ma
		return [lo,mi,ma]
	def btN(one,two):
		if one == two:
			btResult = 0
		elif one > two:
			btResult = one - two
		else:
			btResult = two - one
		return btResult

	def ranHelper(lR,gRan,tA=3):
		test = True
		for r in lR:
			if btN(r,gRan) < tA:
				test = False
		return test



	def gen(loX):
		global times
		global key
		lo = loX[0]
		try:
			times
		except Exception as e:
			times = 0
		by = 5
		key = genKey(lo)
		if times % by == 0:
			tms = times / by
			loT = lo - tms
			if loT > loX[1]:
				lo = loT
			# else:
			#     lo = loT
		times += 1
		# lo = 2
		r = []
		iw = 0
		while iw < lo:
			
			
			genX  = random.randint(3,len(key)-3)
			if ranHelper(r,genX):
				r.append(genX)
				iw += 1

		return r
	test = False

	lo = genLo()
	while not test:
		r = gen(lo)
		r.sort()
		t = 0
		test = True
		for x in r:
			z = x - t
			t = x
			if z < 3:
				test = False

	g = 0
	result = ''
	for i,k in enumerate(key):
		if i in r:
			result += '-'
		result += k
	result = result.replace('--','-')
	autoPass = result
	return result


########################################################################################

def action():
	global autoPass
	fileDate = ''
	chatFile = _.switches.value('Chat')

	# print(autoPass)
	while True:
		try:
			newDate = os.path.getmtime(chatFile)
			if not newDate == fileDate:
				fileDate = newDate
				_.switches.process()
				loop()
				print('File Sent')
		except Exception as e:
			raise e
def loop():
	global autoPass
	global chatCnt
	# _.switches.process()
	chatData0 = _.getText(_.switches.value('Chat'))
	chatCnt = 0
	for cc in chatData0:
		chatCnt += len(cc)
	# print('chatCnt',chatCnt)
	genPassword()

	_.switches.fieldSet('Secure','value',autoPass)
	chatData = ''
	for cd in chatData0:
		chatData += cd
	# print(len(chatData))
	# print(chatData)
	chatData = chatData.replace('\n','[(n)]')
	pu_File = _.switches.value('File')
	pu_Secure = str(_.switches.value('Secure'))
	# print(autoPass)
	_.switches.fieldSet('Secure','value',autoPass)
	autoPass = autoPass.split(';')[0]
	import unhackable
	# print('pre:',,_.switches.value('Secure'))
	# p unhackable -message "test message" -save file.json -password 777
	_.switches.fieldSet('Message','active',True)
	_.switches.fieldSet('Message','value',chatData)

	_.switches.fieldSet('Save','active',True)
	_.switches.fieldSet('Save','value',pu_File)

	_.switches.fieldSet('Password','active',True)
	_.switches.fieldSet('Password','value',autoPass)
	unhackable.baseKey = autoPass
	unhackable.imported = True

	if unhackable.message():
		autoPass = _.switches.value('Password')
		# print(autoPass)
		import server
		_.switches.process()
		_.switches.fieldSet('Secure','value',autoPass)
		# print(autoPass)
		# print()
		server.passGet = autoPass
		server.action()
		# print(_.switches.value('Secure'))
		# server.action()
	else:
		loop()

########################################################################################
if __name__ == '__main__':
	action()






