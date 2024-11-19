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
import shutil
import uuid
import simplejson as json
import time
import datetime
import sys
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('Scan', '-scan')
_.switches.register('Index', '-i,-index','usb, C:\\ D:'+_v.slash)
_.switches.register('History', '-h,-history')
_.switches.register('Path', '-p,-path')

_.appInfo=    {
	'file': 'drive.py',
	'description': 'Manages drives and indexes',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p drive -scan')
_.appInfo['examples'].append('p drive -index usb')
_.appInfo['examples'].append('p drive -index usb internal')
_.appInfo['examples'].append('p drive -index C:\\Users\\Scott\\Desktop Desktop')
_.appInfo['examples'].append('p drive -index C:\\ D:'+_v.slash)
_.appInfo['examples'].append('p drive -index cloud')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('found an id, here is how to research it...')
_.appInfo['examples'].append('\tp dirDB + indexTable_drives - backup --c | p f3 + CDE18F2D7BEF -jn')
_.appInfo['examples'].append('')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})
_.appInfo['columns'].append({'name': 'initiated', 'abbreviation': 'i'})
_.appInfo['columns'].append({'name': 'type', 'abbreviation': 't'})
_.appInfo['columns'].append({'name': 'priority', 'abbreviation': 'p'})
_.appInfo['columns'].append({'name': 'drive', 'abbreviation': 'd,l,dr'})
_.appInfo['columns'].append({'name': 'machineID', 'abbreviation': 'm'})
_.appInfo['columns'].append({'name': 'timestamp', 'abbreviation': 'ts,time,date'})

def formatColumns(columns):
	result = ''
	for c in columns.split(','):
		for col in _.appInfo['columns']:
			for a in col['abbreviation'].split(','):
				if a == c:
					c = col['name']
		result += c + ','
	result = result[:-1]
	return result

_.switches.trigger('Column',formatColumns)
_.switches.process()
_.maxNameLength = 40
# _.columnTab = '\t'

_.tables.register('Auto')
# _.tables.trigger('Auto','timestamp',_.float2Date)
_.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)

# if _.switches.isActive('Path') == False:
#     Folder = _.switches.value('Path')








# if _.switches.isActive('Path') == False:
#     folder = _.switches.value('Path')

# if _.switches.isActive('Help') == True:
#     print('Drive Log\n')
#     print('Example:')
#     print('\tp drive -s')
#     print('\tp drive -h {F8E01519-3977-04B8-3416-1F0048BD97C3} | p line -p " " 0 -u')
#     print()
#     print('Columns:')
#     print('\tdrive name id type priority machineID pc timestamp\n')
#     _.tables.register('Auto',_.switch)
#     _.tables.print('Auto','name,switch,expected_input_example')
#     sys.exit()

def getID(drive):
	# print(drive)
	driveID = ''
	if os.path.isdir(drive) == True:
		idFile = drive + 'drive.id.sys'
		if os.path.isfile(idFile) == True:
			# os._exit(0)
			initiated = os.path.getctime(idFile)
			driveID = open( idFile, 'r' ).read()
			driveID = driveID.replace(' ','')
			driveID = driveID.replace('\n','')
			driveID = driveID.replace('\r','')
		# else:
			# print('Error')
			# os._exit(0)
	return driveID

def genGUID():
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	result = str(string).upper()
	result = '{' + result + '}'
	return result

def stamp2Date(ts):
	return datetime.datetime.fromtimestamp(int(ts) / 1e3)

def recordCheck(theID,letter):
	global records_drives
	result = False
	try:
		i = 0
		for r in records_drives:
			if records_drives[i]['type'] == 'button':
				records_drives[i]['type'] = 'button(usb)'
			if records_drives[i]['type'] == 'thumb':
				records_drives[i]['type'] = 'thumb(usb)'

			if records_drives[i]['id'] == theID:
				records_drives[i]['drive'] = letter
				result = True
			i += 1
	except Exception as e:
		pass
	return result

def recordLabel(theID,letter):
	global records_drives
	result = ''
	try:
		i = 0
		for r in records_drives:
			if records_drives[i]['id'] == theID:
				result = records_drives[i]['name']
			i += 1
	except Exception as e:
		pass
	return result

def getRecord(theID):
	global records_drives
	result = False
	try:
		i = 0
		for r in records_drives:
			if records_drives[i]['id'] == theID:
				result = records_drives[i]
			i += 1
	except Exception as e:
		pass
	return result

def appendRecord(driveID,letter,initiated):
	global machineID
	showInfo = True
	if letter == 'C:'+_v.slash:
		result = {'name': 'C_Drive', 'type': 'internal', 'priority': 1, 'drive': letter, 'id': driveID, 'machineID': machineID, 'pc': os.getenv('COMPUTERNAME'), 'timestamp': int(round(time.time() * 1000))}
	else:
		if showInfo:
			print('TYPE:\t','internal','external','thumb','button','cloud\n')
			showInfo = False
		print(letter)
		name = input('\t    name: ')
		theType = input('\t    type: ')
		ipriority = input('\tpriority:  ')
		result = {'name': name, 'type': theType, 'priority': int(ipriority), 'drive': letter, 'id': driveID, 'machineID': machineID, 'pc': os.getenv('COMPUTERNAME'), 'initiated': initiated, 'timestamp': int(round(time.time() * 1000))}
	return result

def scanDrives():
	global records_drives
	global machineID
	instance = {'instance': genGUID(), 'timestamp': int(round(time.time() * 1000)),'machineID': machineID, 'drives': []}
	
	for l in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(','):
		letter = l + ':'+_v.slash
		idFile = letter + 'drive.id.sys'
		if os.path.isdir(letter) == True:
			if os.path.isfile(idFile) == True:
				driveID = getID(letter)
				# print(driveID)
				if recordCheck(driveID,letter) == False:
					records_drives.append(appendRecord(driveID,letter,os.path.getctime(idFile)))

				instance['drives'].append({'name': recordLabel(driveID,letter), 'drive': letter, 'id': driveID, 'pc': os.getenv('COMPUTERNAME')})
				# print(letter,driveID)
			else:
				driveID = genGUID()
				records_drives.append(appendRecord(driveID,letter,int(round(time.time() * 1000))))
				file = open(idFile,'w') 
				file.write(driveID)                 
				file.close()
				os.system('attrib +h ' + idFile)
				# print(letter,driveID)
				# print(letter,'New Drive ID:',driveID)
	return instance


def logSave(rows,theFile):
	if os.path.isfile(theFile) == True:
		theJSON = _.getTable(theFile)
	else:
		theJSON = []
	theJSON.append(rows)
	_.saveTable(theJSON,theFile,True,False)


def printDriveRows(what):
	global records_drives
	global driveTotal
	rows = []
	for r in records_drives:
		if what == 'all':
			driveTotal +=1
			rows.append(r)
			# print(r['drive'],r['name'],'\t',r['id'])
		else:
			if os.path.isdir(r['drive']) == True:
				if recordCheck(getID(r['drive'])):
					driveTotal +=1
					rows.append(r)
				# print(r['drive'],r['name'],'\t',r['id'])
	if _.switches.isActive('Column'):
		_.tables.register('Auto',rows)
		_.tables.print('Auto','Column')
	else:
		_.tables.register('Auto',rows)
		_.tables.print('Auto','drive,name,id,priority')
	print('\nTotal:',driveTotal)

def initiateScan():
	global file_drives
	global records_drives

	if os.path.isfile(_v.myTables + _v.slash + file_drives) == True:
		records_drives = _.getTable(file_drives)
	else:
		records_drives = []

	# print(records_drives)
	# sys.exit()

	result = scanDrives()
	# print(result)
	# sys.exit()
	
	logSave(result,file_driveLog)
	_.saveTable(records_drives,file_drives,True,False)
	printActive()

def historyLog():
	global file_driveLog
	records = _.getTable(file_driveLog)
	for record in records:
		for r in record['drives']:
			if _.switches.value('History') == r['id']:
				# print(record['instance'],str(record['timestamp']),stamp2Date(record['timestamp']))
				print(stamp2Date(record['timestamp']))


def printActive():
	global records_drives
	global machineID
	rows = []
	i = 0
	for l in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(','):
		letter = l + ':'+_v.slash
		if os.path.isdir(letter) == True:
			try:
				record = getRecord(getID(letter))
				# print(letter,type(record))
				if type(record) == dict:
					rows.append(record)
				i += 1
			except Exception as e:
				pass
	os.system('cls')
	os.system('echo.')
	if _.switches.isActive('Column'):
		_.tables.register('Auto',rows)
		_.tables.print('Auto','Column')
	else:
		_.tables.register('Auto',rows)
		_.tables.print('Auto','drive,name,id,priority')
	print('\nTotal:',i)

def getFolder(folder,file):
	global i
	try:
		dirList = os.listdir(folder)
		action = True
	except Exception as e:
		action = False
	if action == True:
		if os.path.isdir(folder) == True:
			dirList = os.listdir(folder)
		for item in dirList:
			path = folder + _v.slash + item
			path = path.replace(_v.slash+_v.slash,_v.slash)
			if os.path.isfile(path) == True:
				pass
				result = str(path) + '\n'
				open(file,"a+b").write(result.encode())
						
			if os.path.isdir(path) == True:
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder) == True:
					try:
						getFolder(newFolder,file)
					except Exception as e:
						pass
				else:
					print('error')

def index():
	initiateScan()
	print('')
	print('Indexing...')
	print('')
	indexTemp = '00{3C2D3003A97C}'
	success = False
	global records_drives
	indexWhat = _.switches.value('Index')
	if ',' in indexWhat:    
		indexWhat = indexWhat.split(',')
		indexWhat[0] = _.ci(indexWhat[0])
		indexWhat[1] = _.ci(indexWhat[1])
	if not indexWhat:
		do = 'index_internal'
	elif type(indexWhat) == list:
		result = True
		newList = []
		for iW in indexWhat:
			i = 0
			for record in records_drives:
				if record['id'] == getID(record['drive']) and (iW in record['drive'] or iW in record['name'] or iW in record['type'] or iW == record['id']):
					# print(record['drive'])
					newList.append(record['drive'])
				i += 1
			# print(len(newList), len(indexWhat))
			if len(newList) == len(indexWhat) or len(newList) > len(indexWhat):
				pass
			else:
				result = False
		if result:
			do = 'index_listed'
		else:
			do = 'index_special'
	elif type(indexWhat) == str:
		do = 'index_specified_drive'
	# print(do)
	# print(type(indexWhat))

	# os._exit(0)

	def indexDrive(i):
		if os.path.isdir(records_drives[i]['drive']):
			print('\tIndexing drive: ',records_drives[i]['drive'])
			if records_drives[i]['priority'] < 10:
				priority = '0' + str(records_drives[i]['priority'])
			else:
				priority = '' + str(records_drives[i]['priority'])
			path = _v.myIndexes
			file = priority + records_drives[i]['id']
			fullpath = path + _v.slash + file
			fullpathTMP = path + _v.slash + indexTemp

			open(fullpathTMP,'wb').write(b'')
			getFolder(records_drives[i]['drive'],fullpathTMP)
			if os.path.isfile(fullpath):
				modDate = os.path.getmtime(fullpath)
				shutil.move(fullpath, path + _v.slash + 'archive'+_v.slash + formatDate(modDate) + '__' + file)
			shutil.move(fullpathTMP, fullpath)
			print('\t\t',fullpath)

	if do == 'index_listed':
		newListPrint = ''
		for n in newList:
			newListPrint += n + ', '
		newListPrint = _str.cleanLast(newListPrint,', ')
		print('\nIndexing', newListPrint,'\n')
		# print('Indexing', newList,'\n')
		# os._exit(0)
		for iW in newList:
			i = 0
			for record in records_drives:
				if iW == record['drive'] and record['id'] == getID(record['drive']):
					indexDrive(i)
				i += 1
	if do == 'index_special':
		if not os.path.isdir(indexWhat[0]):
			print('Error: Not a drive')
		else:
			print('Indexing: ' + indexWhat[0])
			path = _v.myIndexes
			file = indexWhat[1]
			fullpath = path + _v.slash + file
			try:
				if os.path.isfile(fullpath):
					modDate = os.path.getmtime(fullpath)
					shutil.move(fullpath, path + _v.slash + 'archive'+_v.slash + formatDate(modDate) + '__' + file)
				open(file,'wb').write(b'')
				getFolder(indexWhat[0],fullpath)
				print('\t\t',fullpath)
				success = True
			except Exception as e:
				print('Error Indexing: ' + indexWhat[0])
				success = False

	if do == 'index_specified_drive':
		result = True
		newList = []
		i = 0
		for record in records_drives:
			if record['id'] == getID(record['drive']) and (indexWhat in record['drive'] or indexWhat in record['name'] or indexWhat in record['type'] or indexWhat == record['id']):
				newList.append(record['drive'])
				# indexDrive(i)
			i += 1
		newListPrint = ''
		for n in newList:
			newListPrint += n + ', '
		newListPrint = _str.cleanLast(newListPrint,', ')
		print('\nIndexing', newListPrint,'\n')
		for iW in newList:
			i = 0
			for record in records_drives:
				if iW == record['drive'] and record['id'] == getID(record['drive']):
					try:
						indexDrive(i)
						success = True
					except Exception as e:
						success = False
						print('Error Indexing: ' + record['drive'])
				i += 1

	if do == 'index_internal':
		i = 0
		for record in records_drives:
			if record['type'] == 'internal':
				try:
					indexDrive(i)
					success = True
				except Exception as e:
					success = False
					print('Error Indexing: ' + record['drive'])
			i += 1
	print('')
	if success:
		print('Indexing Complete')
	else:
		print('Failure')

def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y.%m.%d-%H.%M-%S')
	# theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y-%m-%d %H:%M:%S')
	theDate = str(theDate)
	return theDate


machineID = _v.getMachineID()
file_drives = 'indexTable_drives-' + machineID + '.json'
file_driveLog = 'indexTable_logs-' + machineID + '.json'
driveTotal = 0
# print(file_drives)
if __name__ == '__main__':
	_.switches.fieldSet('Long','active',True)
	if _.switches.isActive('Path'):
		print('machineID:',machineID)
		print(file_drives)
		print(file_driveLog)

	if _.switches.isActive('Scan'):
		initiateScan()

	if _.switches.isActive('History'):
		historyLog()

	if _.switches.isActive('Index'):
		index()




# found an id, here is how to research it...
	# p dirdb + indexTable_drives - backup --c | p f3 + CDE18F2D7BEF -jn



# print(genGUID())


