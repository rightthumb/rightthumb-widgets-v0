import os

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import colorama
colorama.init()


class ColorMin:
	bold = '\033[1m'
	cyan = '\033[96m'
	green = '\033[1;32;40m'
	yellow = '\033[93m'
	blue = '\033[1;34;40m'
	red = '\033[91m'
	purple = '\033[95m'
	end = '\033[0m'

def colorThis( txt, color, p=1 ):
	if color == '':
		result = txt
	else:
		c = eval( 'ColorMin.' + color )
		result = c + txt + ColorMin.end
	if p:
		_.pr( result )
	return result

def colorList( txt, theList ):
	result = ''
	for color in theList:
		result += colorThis( txt, color, p=0 )
	return result

def colorList2( theList ):
	result = ''
	for i,record in enumerate(theList):
		result += colorThis( record[0], record[1], p=0 )
		
	return result
# bold cyan green yellow blue red purple
def printMessage():

	msg2 = colorList2( [
							[ 'L', 'yellow' ],
							[ 'o', 'purple' ],
							[ 'a', 'bold' ],
							[ 'd', 'green' ],
							[ 'i', 'purple' ],
							[ 'n', 'cyan' ],
							[ 'g', '' ],
							[ '.', 'bold' ],
							[ '.', 'purple' ],
							[ '.', 'yellow' ],
							[ '.', 'red' ],
							[ '.', 'blue' ],
		] )

	dots = colorList( '.', [
							'yellow',
							'purple',
							'bold',
							'red',
							'blue',
		] )

	msg = colorThis( '                                          Loading', 'green', p=0 ) + dots

	os.system('cls')
	_.pr()
	_.pr()
	_.pr()
	_.pr()
	colorThis( '                                          Loading...', 'green' )
	# colorThis( '                                          Loading...', 'yellow' )
	# _.pr( msg )
	# pause=input('')
# printMessage()
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append(focus())
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
_qi = _.regImp( __.appReg, 'updateQuickIndex' )
##################################################
# import os
import sys
import time
import simplejson as json

import shutil
import uuid
import time
import datetime

from tkinter import *
from tkinter.ttk import *
import shutil
if _.isWin:
	import wmi
##################################################

def appSwitches():
	_.switches.register('Scan', '-scan')
	_.switches.register('Index', '-i,-index','usb, C:\\ D:'+_v.slash)
	_.switches.register('History', '-h,-history')
	_.switches.register('Path', '-p,-path')
	
	_.switches.register('ChainOfCustody', '-custody')
	_.switches.register('CustodyChain', '-chain')
	



_.appInfo[focus()] = {
	'file': 'drive.py',
	'description': 'Manages drives and indexes',
	'categories': [
						'index',
						'drive',
						'admin',
						'manage',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}


_.appInfo[focus()]['examples'].append('p drive -scan')
_.appInfo[focus()]['examples'].append('p drive -index usb')
_.appInfo[focus()]['examples'].append('p drive -index usb internal')
_.appInfo[focus()]['examples'].append('p drive -index C;.\\Users\\Scott\\Desktop Desktop')
_.appInfo[focus()]['examples'].append('p drive -index C;.\\ D;.'+_v.slash)
_.appInfo[focus()]['examples'].append('p drive -index cloud')

_.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})
_.appInfo[focus()]['columns'].append({'name': 'initiated', 'abbreviation': 'i'})
_.appInfo[focus()]['columns'].append({'name': 'type', 'abbreviation': 't'})
_.appInfo[focus()]['columns'].append({'name': 'priority', 'abbreviation': 'p'})
_.appInfo[focus()]['columns'].append({'name': 'drive', 'abbreviation': 'd,l,dr'})
_.appInfo[focus()]['columns'].append({'name': 'machineID', 'abbreviation': 'm'})
_.appInfo[focus()]['columns'].append({'name': 'timestamp', 'abbreviation': 'ts,time,date'})


_.maxNameLength = 40



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		_.argvProcess = True
		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	_.switches.trigger('Input',_.formatColumns)
	__.cls_process_switches_help = True
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()



def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )

def setPipeData(data):
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in data:
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')



_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )



########################################################################################
def getID(drive):
	# _.pr(drive)
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
			# _.pr('Error')
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
	global drive_records
	result = False
	try:
		i = 0
		for r in drive_records:
			if drive_records[i]['type'] == 'button':
				drive_records[i]['type'] = 'button(usb)'
			if drive_records[i]['type'] == 'thumb':
				drive_records[i]['type'] = 'thumb(usb)'

			if drive_records[i]['id'] == theID:
				drive_records[i]['drive'] = letter
				result = True
			i += 1
	except Exception as e:
		pass
	return result

def recordLabel(theID,letter):
	global drive_records
	result = ''
	try:
		i = 0
		for r in drive_records:
			if drive_records[i]['id'] == theID:
				result = drive_records[i]['name']
			i += 1
	except Exception as e:
		pass
	return result

def getRecord(theID):
	global drive_records
	result = False
	try:
		i = 0
		for r in drive_records:
			if drive_records[i]['id'] == theID:
				result = drive_records[i]
			i += 1
	except Exception as e:
		pass
	return result

def appendRecord(driveID,letter,initiated):
	global machineID
	showInfo = True
	if False and letter == 'C:'+_v.slash:
		result = {'name': 'C_Drive', 'type': 'internal', 'priority': 1, 'drive': letter, 'id': driveID, 'machineID': machineID, 'pc': os.getenv('COMPUTERNAME'), 'timestamp': int(round(time.time() * 1000))}
	else:
		if showInfo:
			# _.pr('TYPE:\t','internal','external','thumb','button','cloud\n')
			showInfo = False
		_.pr(letter)
		# name = input('\t    name: ')
		# theType = input('\t    type: ')
		# ipriority = input('\tpriority:  ')
		info = Documentation_Initial(letter)


		name = info.label
		theType = info.type
		ipriority = info.priority


		descriptors = info.descriptors
		owner = info.owner
		drivesize = info.driveSize
		volumesize = info.volumeSizeTotal
		volumesizefree = info.volumeSizeFree
		
		volumesizeused = info.volumeSizeUsed
		serial = info.serial

		if not info.save:
			sys.exit()
		result = {'serial': serial, 'name': name, 'type': theType, 'priority': int(ipriority), 'drive': letter, 'id': driveID, 'machineID': machineID, 'pc': os.getenv('COMPUTERNAME'), 'initiated': initiated, 'timestamp': time.time(), 'volumesizeused': volumesizeused, 'volumesizefree': volumesizefree, 'volumesize': volumesize, 'drivesize': drivesize, 'descriptors': descriptors, 'owner': owner }
	return result

def scanDrives():
	global drive_records
	global machineID
	instance = {'instance': genGUID(), 'timestamp': int(round(time.time() * 1000)),'machineID': machineID, 'drives': []}
	
	for l in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(','):
		letter = l + ':'+_v.slash
		idFile = letter + 'drive.id.sys'
		if os.path.isdir(letter):
			if os.path.isfile(idFile) == True:
				driveID = getID(letter)
				# _.pr(driveID)
				if recordCheck(driveID,letter) == False:
					drive_records.append(appendRecord(driveID,letter,os.path.getctime(idFile)))

				instance['drives'].append({'name': recordLabel(driveID,letter), 'drive': letter, 'id': driveID, 'pc': os.getenv('COMPUTERNAME')})
				# _.pr(letter,driveID)
			else:

				if hasPermission( l ):
					driveID = genGUID()
					drive_records.append(appendRecord(driveID,letter,time.time()))
					file = open(idFile,'w') 
					file.write(driveID)                 
					file.close()
					os.system('attrib +h ' + idFile)
					# _.pr(letter,driveID)
					# _.pr(letter,'New Drive ID:',driveID)

		_.saveTable( drive_records, file_drives, p=0 )
	return instance


def logSave(rows,theFile):
	if os.path.isfile(theFile) == True:
		theJSON = _.getTable(theFile)
	else:
		theJSON = []
	theJSON.append(rows)
	_.saveTable(theJSON,theFile, p=0 )


def printDriveRows(what):
	global drive_records
	global driveTotal
	rows = []
	for r in drive_records:
		if what == 'all':
			driveTotal +=1
			rows.append(r)
			# _.pr(r['drive'],r['name'],'\t',r['id'])
		else:
			if os.path.isdir(r['drive']) == True:
				if recordCheck(getID(r['drive'])):
					driveTotal +=1
					rows.append(r)
				# _.pr(r['drive'],r['name'],'\t',r['id'])
	if _.switches.isActive('Column'):
		_.tables.register('Auto',rows)
		_.tables.print('Auto','Column')
	else:
		_.tables.register('Auto',rows)
		_.tables.print('Auto','drive,name,id,priority')
	_.pr('\nTotal:',driveTotal)

def initiateScan():

	global file_drives
	global drive_records

	if os.path.isfile(_v.myTables + _v.slash + file_drives) == True:
		drive_records = _.getTable(file_drives)
	else:
		drive_records = []

	# _.pr(drive_records)
	# sys.exit()

	result = scanDrives()
	# _.pr(result)
	# sys.exit()
	
	logSave(result,file_driveLog)
	_.saveTable( drive_records, file_drives, p=0 )
	printActive()

def historyLog():
	global file_driveLog
	records = _.getTable(file_driveLog)
	for record in records:
		for r in record['drives']:
			if _.switches.value('History') == r['id']:
				# _.pr(record['instance'],str(record['timestamp']),stamp2Date(record['timestamp']))
				_.pr(stamp2Date(record['timestamp']))


def printActive():
	global drive_records
	global machineID
	rows = []
	i = 0
	for l in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(','):
		letter = l + ':'+_v.slash
		if os.path.isdir(letter) == True:
			try:
				record = getRecord(getID(letter))
				# _.pr(letter,type(record))
				if type(record) == dict:
					rows.append(record)
				i += 1
			except Exception as e:
				pass
	os.system('cls')
	_.pr()
	if _.switches.isActive('Column'):
		_.tables.register('Auto',rows)
		_.tables.print('Auto','Column')
	else:
		_.tables.register('Auto',rows)
		_.tables.print('Auto','drive,name,id,priority')
	# _.pr('\nTotal:',i)
	_.colorThis(  [ '\nTotal:',i ], 'yellow'  )

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
					_.pr('error')

def index():
	global indexTemp
	initiateScan()
	_.pr('')
	_.pr('Indexing...')
	_.pr('')
	
	allDrives = False
	global drive_records
	# indexWhat = _.switches.value('Index').split(',')
	indexWhat = _.switches.values('Index')
	# _.pr( 'indexWhat', indexWhat )
	# sys.exit()


	isInternal = False
	for i,x in enumerate(indexWhat):
		indexWhat[i] = _.ci(indexWhat[i])
		if i == 0:
			if not len(indexWhat[i]):
				isInternal = True
	if isInternal:
		indexWhat = []
		for record in drive_records:
			if record['id'] == getID( record['drive'] ) and record['type'].lower() == 'internal':
				indexWhat.append( record['drive'] )
	elif type(indexWhat) == list:
		result = True
		newList = []
		for i,iW in enumerate(indexWhat):
			if ':' in iW:
				iW = iW.split( ':' )[0]
			# _.pr(  )
			# _.pr( iW )
			# _.pr(  )
			found = False
			for ii,record in enumerate(drive_records):
				# _.printVar( record )
				if not found:
					shouldIndex = False
					if record['id'] == getID( record['drive'] ):
						if len(iW) > 1:
							if iW.lower() == record['name'].lower() or iW.lower() == record['id'].lower() or iW.lower() == record['type'].lower():
								shouldIndex = True
							else:
								for d in record['descriptors'].lower():
									if d == iW.lower():
										shouldIndex = True

						else:
							if iW.lower()+':'+_v.slash in record['drive'].lower() or iW.lower() == str( record['priority'] ):
								shouldIndex = True
					if shouldIndex:
						found = True
						indexWhat[i] = ii

	# _.pr(do)
	# _.pr(type(indexWhat))

	# os._exit(0)
	# sys.exit()
	def indexDrive( i ):
		global indexIDs

		if os.path.isdir(drive_records[i]['drive']):
			indexIDs.newID(  drive_records[i]['drive'][0]  )
			_.pr('\tIndexing drive: ',drive_records[i]['drive'])
			if drive_records[i]['priority'] < 10:
				priority = '0' + str(drive_records[i]['priority'])
			else:
				priority = '' + str(drive_records[i]['priority'])
			path = _v.myIndexes
			file = priority + drive_records[i]['id']
			fullpath = path + _v.slash + file
			fullpathTMP = indexIDs.value(  drive_records[i]['drive'][0]  )

			open(fullpathTMP,'wb').write(b'')
			getFolder(drive_records[i]['drive'],fullpathTMP)
			if os.path.isfile(fullpath):
				modDate = os.path.getmtime(fullpath)
				shutil.move(fullpath, path + _v.slash + 'archive'+_v.slash + formatDate(modDate) + '__' + file)
			shutil.move(fullpathTMP, fullpath)
			_.pr('\t\t',fullpath)

	def indexFolder( iW, f ):
		if os.path.isdir( f ):
			indexIDs.newID(iW)
			_.pr('\tIndexing drive: ', iW )
			path = _v.myIndexes
			file = iW + '.txt'
			fullpath = path + _v.slash + file
			fullpathTMP = indexIDs.value(iW)

			open(fullpathTMP,'wb').write(b'')
			getFolder( f, fullpathTMP )
			if os.path.isfile(fullpath):
				modDate = os.path.getmtime(fullpath)
				shutil.move(fullpath, path + _v.slash + 'archive'+_v.slash + formatDate(modDate) + '__' + file)
			shutil.move(fullpathTMP, fullpath)
			_.pr('\t\t',fullpath)
	anyFail = False
	for i,iW in enumerate(indexWhat):
		if type( iW ) == int:
			try:
				indexDrive( iW )
				success = True
			except Exception as e:
				success = False
				anyFail = True
				_.pr( 'Error Indexing: ' + record['drive'] )
			
		else:
			f = resolveAlias( iW )
			_.pr( f )
			if not os.path.isdir( f ):
				_.pr('Error: Not an alias')
			else:
				try:
					indexFolder( iW, f )
					success = True
				except Exception as e:
					success = False
					anyFail = True
					_.pr( 'Error Indexing: ' + iW )

				

	if not anyFail:
		_.pr('Indexing Complete')
	else:
		_.pr('Failure')

def resolveAlias( alias ):

	file = _v.bookmarkFormat.replace( 'ALIASHERE', alias )
	if os.path.isfile( file ):
		f = _.getText( file )
		f = f[0].replace( '\n', '' )
		f = _v.resolveFolderIDs( f )
	else:
		f = alias
	return f



def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y.%m.%d-%H.%M-%S')
	# theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y-%m-%d %H:%M:%S')
	theDate = str(theDate)
	return theDate

##########################################################################################################################
class Documentation_Initial:

	def __init__( self, letter=None ):
		if _.isWin:
			letter = _str.removeNonAlpha( letter )
		# _.pr(letter)
		# _.pr(letter[0])
		if _.isWin:
			self.letter = letter[0]
		else:
			self.letter = letter
		self.owner = ''
		self.serial = ''
		self.type = ''
		self.label = ''
		self.descriptors = ''
		self.priority = 4

		self.descriptorID = -1
		self.descriptorLoop = -1

		self.volumeSizeTotalInt = 0
		self.volumeSizeTotal = 0
		self.volumeSizeUsed = 0
		self.volumeSizeFree = 0
		self.driveSize = 0
		self.driveSizeLabel = 0

		self.save = False

		delim = '_'
		space = '-'

		if not letter is None:

			window = Tk()
			window.title('Drive documentation')



			raw_label = StringVar()
			raw_type = StringVar()
			raw_priority = StringVar()
			raw_textarea = StringVar()
			raw_owner = StringVar()

			raw_owner.set( 'RightThumb' )
			raw_label.set( self.letter.upper() + space + 'Drive' )

			space0 = Label(window, text='   ')
			ownerLabel = Label(window, text='owner')
			owner = Entry(window, textvariable=raw_owner, justify=LEFT, width=40)

			nameLabel = Label(window, text='drive label')
			name = Entry(window, textvariable=raw_label, justify=LEFT, width=40)

			space1 = Label(window, text='   ')

			rad1 = Radiobutton(window,text='internal', value='internal', variable=raw_type)
			rad2 = Radiobutton(window,text='external', value='external', variable=raw_type)
			rad3 = Radiobutton(window,text='thumb', value='thumb', variable=raw_type)
			rad4 = Radiobutton(window,text='button', value='button', variable=raw_type)
			rad5 = Radiobutton(window,text='cloud', value='cloud', variable=raw_type)
			rad6 = Radiobutton(window,text='card', value='card', variable=raw_type)
			rad7 = Radiobutton(window,text='archive', value='archive', variable=raw_type)

			space2 = Label(window, text='   ')

			priorityLabel = Label(window, text='priority')
			priority = Entry(window, textvariable=raw_priority, justify=LEFT, width=10)

			space3 = Label(window, text='   ')
			space4 = Label(window, text='   ')

			pad_x = 5
			pad_y = 5

			textareaLabel = Label(window, text='descriptors list')
			scrollbar1 = Scrollbar(window)
			# textarea1 = Text(window, variable=raw_textarea, width=20, height=10)
			textarea1 = Text(window, width=20, height=10)

			textarea1.config(yscrollcommand=scrollbar1.set)
			scrollbar1.config(command=textarea1.yview)



		def textarea_bind_ENTER(p1):
			# _.pr( 'Got: ', textarea1.get("1.0",END) )
			self.descriptorID = -1

		def validate():
			self.owner = raw_owner.get()
			self.type = raw_type.get()
			self.label = raw_label.get()
			self.priority = raw_priority.get()
			self.descriptors = textarea1.get("1.0",END)
			self.descriptors = _str.replaceDuplicate(self.descriptors,' ')
			self.descriptors = _str.cleanBE(self.descriptors,' ')
			self.descriptors = _str.replaceDuplicate(self.descriptors,'\n')
			self.descriptors = _str.cleanBE(self.descriptors,'\n')

			if not self.type == '' and not self.label == '' and not self.priority == '' and isInt( self.priority ):
				self.descriptors = self.descriptors.replace( '\n', ',' )
				self.priority = int( self.priority )
				self.volumeSizeInfo()
				if not self.type == 'cloud':
					self.findSerial()

				# for x in dir(window):
				#     x = str(x)
				#     if not x.startswith('_'):
				#         _.pr(x)
				self.save = True
				window.destroy()
				window.quit()

			else:
				_.pr('Please complete form')
		def loopDescriptorTest(i):
			try:
				if len(self.descriptors.split('\n')[i]) == 0:
					test = False
				test = True
			except Exception as e:
				test = False
			return test

		def loopDescriptorAdd(i):
			return delim + self.descriptors.split('\n')[i]

		def loopDescriptor():
			result = ''
			shouldReset = False
			done = False
			maxDescriptors = len( self.descriptors.split('\n') )

			if maxDescriptors == 1:
				if self.descriptorID == -1:
					self.descriptorID += 1
					if loopDescriptorTest(self.descriptorID+1):
						result = loopDescriptorAdd(self.descriptorID)
					else:
						shouldReset = True
					done = True
				else:
					shouldReset = True
					done = True

			if not done:
				# _.pr('loopDescriptorTest:',loopDescriptorTest(self.descriptorID+1))
				if loopDescriptorTest(self.descriptorID+1):
					self.descriptorID += 1
				else:
					if loopDescriptorTest(self.descriptorLoop+2):
						self.descriptorLoop += 1
						self.descriptorID = self.descriptorLoop + 1
					else:
						done = True
						shouldReset = True
						
			if not done:
				
				if self.descriptorLoop == -1:
					result = loopDescriptorAdd(self.descriptorID)
				else:
					i = -1
					while i <= self.descriptorLoop-1:
						i += 1
						# _.pr(self.descriptorID,self.descriptorLoop,i)
						result += loopDescriptorAdd(i)
					result += loopDescriptorAdd(self.descriptorID)



			if shouldReset:
				# _.pr('shouldReset:',shouldReset)
				self.descriptorID = -1
				self.descriptorLoop = -1

			return result

		def suggestName():
			shouldReset = False

			textarea = textarea1.get("1.0",END)
			textarea = _str.replaceDuplicate(textarea,' ')
			textarea = _str.cleanBE(textarea,' ')
			textarea = _str.replaceDuplicate(textarea,'\n')
			textarea = _str.cleanBE(textarea,'\n')

			if not self.owner == raw_owner.get():
				shouldReset = True
			if not self.type == raw_type.get():
				shouldReset = True
			if not self.descriptors == textarea:
				shouldReset = True
			if shouldReset:
				self.descriptorID = -1
				self.descriptorLoop = -1
				# _.pr('reset')
			self.owner = raw_owner.get()
			self.type = raw_type.get()
			self.label = raw_label.get()
			self.priority = raw_priority.get()
			self.descriptors = textarea

			

		
			self.volumeSizeInfo()
			midLabel = ''
			if self.type == 'button':
				midLabel = 'btn'
			if self.type == 'thumb':
				midLabel = 'usb'
			if self.type == 'external':
				midLabel = 'Drive'
			if self.type == 'archive':
				midLabel = 'archive'


			theDriveSize = self.volumeSizeTotalInt


			if self.type == 'archive':

				if not self.owner == 'RightThumb':
					suggestion = self.owner + '\'s' + delim + theDriveSize + delim + midLabel + loopDescriptor()
				else:
					suggestion = 'my' + delim + theDriveSize + delim + midLabel + loopDescriptor()



			elif not self.owner == 'RightThumb':
				suggestion = self.owner + '\'s' + delim + theDriveSize + delim + midLabel + loopDescriptor()
			else:
				suggestion = 'my' + delim + theDriveSize + delim + midLabel + loopDescriptor()

			if self.type == 'cloud':
				suggestion = self.descriptors.split('\n')[self.descriptorID] + space + 'Cloud'
			if self.type == 'internal':
				if not _.isWin:
					# _.pr( '|', self.letter, '|')
					if self.letter == '/':
						suggestion = 'ROOT Drive'
					else:
						suggestion = self.letter + space + 'Drive'
				else:
					suggestion = self.letter.upper() + space + 'Drive'

			suggestion = suggestion.replace( ' ', space )
			raw_label.set(suggestion)

		# textarea1.bind('<Return>', textarea_bind_ENTER)

		btn = Button(window, text='Done', command=validate)
		btn_suggest = Button(window, text='suggest label', command=suggestName)
		theRow = 0
		space0.grid(column=0, row=theRow)

		theRow +=1
		ownerLabel.grid(column=1, row=theRow)
		owner.grid(column=2, row=theRow, columnspan=4 )

		theRow +=1
		nameLabel.grid(column=1, row=theRow)
		name.grid(column=2, row=theRow, columnspan=4 )

		theRow +=1
		space1.grid(column=0, row=theRow)

		theRow +=1;theColumn = 1
		theColumn+=1;rad1.grid(column=theColumn, row=theRow)
		theColumn+=1;rad2.grid(column=theColumn, row=theRow)
		theColumn+=1;rad3.grid(column=theColumn, row=theRow)
		theColumn+=1;rad4.grid(column=theColumn, row=theRow)
		theRow +=1;theColumn = 2
		theColumn+=1;rad5.grid(column=theColumn, row=theRow)
		theColumn+=1;rad6.grid(column=theColumn, row=theRow)
		theColumn+=1;rad7.grid(column=theColumn, row=theRow)

		theRow +=1
		space2.grid(column=7, row=theRow)

		theRow +=1
		priorityLabel.grid(column=1, row=theRow)
		priority.grid(column=2, row=theRow )

		theRow +=1
		theRow +=1
		space3.grid( column=6, row=theRow, rowspan=2 )

		theRow +=1
		theRow +=1
		textareaLabel.grid( column=1, row=theRow )
		theRow +=1
		textarea1.grid(row=theRow, column=1, padx=pad_x, pady=pad_y, sticky=W)
		scrollbar1.grid(row=theRow, column=2, padx=pad_x, pady=pad_y, sticky=W)
		
		theRow +=1
		space4.grid( column=1, row=theRow )


		theRow +=1
		btn_suggest.grid(column=1, row=theRow )
		btn.grid(column=5, row=theRow )
		theRow +=1
		space4.grid( column=1, row=theRow )

		window.mainloop()

	def extractSerials( self, data ):
		try:
			data = str( data )
			drive = False
			serial = False
			c = 'PHYSICALDRIVE0"'
			d = 'PHYSICALDRIVE1"'
			if 'Tag' in data:
				if c in data:
					drive = 'c'
				if d in data:
					drive = 'd'
				sData = data.split('\n')
				for i,x in enumerate(sData):
					if 'Serial'.lower() in x.lower():
						y = x.split('"')[1].replace( ' ', '' )
						serial = y
			return [drive,serial]
		except Exception as e:
			return None
	
	def getSerials( self ):
		result = []
		if _.isWin:
			c = wmi.WMI()
			for i,x in enumerate(c.Win32_PhysicalMedia()):
				result.append( self.extractSerials( x ) )
		else:
			result = '0'
		return result
	def crossRefSerials( self, serialNumbers ):
		if False:
			global drive_records
			
			for sn in serialNumbers:
				found = False
				for record in drive_records:
					if sn[1] == record['serial']:
						found = True
				if not found:
					return sn[1]



	def findSerial( self ):
		serialNumbers = self.getSerials()
		if self.letter.upper() == 'C':
			for sn in serialNumbers:
				if not type(sn[0]) == bool:
					if sn[0].upper() == 'C':
						self.serial = sn[1]
						break
		elif self.letter.upper() == 'D':
			for sn in serialNumbers:
				if not type(sn[0]) == bool:
					if sn[0].upper() == 'D':
						self.serial = sn[1]
						break
		else:
			self.serial = self.crossRefSerials( serialNumbers )


	def volumeSizeInfo( self ):
		_.pr( self.letter )
		_.pr( self.letter )
		if _.isWin:
			total, used, free = shutil.disk_usage( self.letter + ':'+_v.slash )
		else:
			total, used, free = shutil.disk_usage( self.letter )
		self.volumeSizeTotalInt = formatSizeInt(total)
		self.volumeSizeTotal = formatSize(total)
		self.volumeSizeUsed = formatSize(used)
		self.volumeSizeFree = formatSize(free)
		self.driveSize = estimateDriveSize(total)

		if not 'g' in self.volumeSizeTotal.lower():
			self.driveSizeLabel = formatSize(self.driveSize)
		else:
			self.driveSizeLabel = self.driveSize

def hasPermission(drive):
	file = drive + ':'+_v.slash + _.genUUID()
	try:
		_.saveTable2( { 'data': file }, file )
	except Exception as e:
		pass
	if os.path.isfile(file):
		os.remove( file )
		return True
	else:
		return False







##########################################################################################################################

def isFloat( data ):
	data = str( data )
	result = True
	if isInt( data ):
		result = False
	else:
		try:
			float( data )
		except Exception as e:
			result = False

	return result
def isInt( data ):
	data = str( data )
	d = '0123456789'
	result = True
	for c in data:
		if not c in d:
			result = False
	return result


def removeNumbers( n ):
	result = ''
	n = '0123456789.'
	for ch in n:
		if not ch in n:
			result += ch
	return result

def estimateDriveSize( size ):
	_.pr( 'size:', size )
	_.pr( 'gigSize:', gigSize( size ) )
	_.pr( 'formatSizeB:', formatSizeB( size ) )
	raw = formatSizeB(size)
	done = False
	i = 0
	_.pr( 'pre:', raw)
	while not done:
		i += 1
		estimate = i * 64
		if estimate > raw:
			done = True
	_.pr( 'post:', estimate)
	if 'TB' in formatSize( estimate ):
		estimate = estimate * 1073741824
		_.pr('TB')
	else:
		_.pr( removeNumbers(size) )
		estimate = unFormatSize( str(estimate) + removeNumbers(size) )


	_.pr( 'formated:', formatSize( estimate ) )
	return estimate

def formatSizeB( size ):
	try:
		size = int(size)
	except Exception as e:
		size = float(size)
	result = ''
	if size == None:
		result = ''
	elif size < 1024:
		result = str(size) + ''
	elif size > 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str(num) + ''
	elif size > 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str(num) + ''
	elif size > 1073741824 and size < 1099511627776 :
		num = round(size / 1073741824, 2)
		result = str(num) + ''
	else:
		num = round(size / 1073741824, 2)
		result = str(num) + ''
	if isInt(result):
		result = int(result)
	elif isFloat(result):
		result = float(result)
	else:
		result = 0
	return result

def formatSizeInt( size ):
	# size = int(size)
	try:
		size = int(size)
	except Exception as e:
		size = float(size)
	result = ''
	if size == None:
		result = ''
	elif size < 1024:
		result = str(int(size)) + 'B'
	elif size > 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str(int(num)) + 'KB'
	elif size > 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str(int(num)) + 'MB'
	elif size > 1073741824 and size < 1099511627776 :
		num = round(size / 1073741824, 2)
		result = str(int(num)) + 'GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(int(num)) + 'TB'
	return result

def formatSize( size ):
	# size = int(size)
	try:
		size = int(size)
	except Exception as e:
		size = float(size)
	result = ''
	if size == None:
		result = ''
	elif size < 1024:
		result = str((size)) + 'B'
	elif size > 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str((num)) + 'KB'
	elif size > 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str((num)) + 'MB'
	elif size > 1073741824 and size < 1099511627776 :
		num = round(size / 1073741824, 2)
		result = str((num)) + 'GB'
	else:
		num = round(size / 1099511627776, 2)

		result = str((num)) + 'TB'
	return result

def unFormatSize( size ):
	size = str(size)
	size = size.upper()
	factor = ''

	if 'TB' in size:
		factor = 1099511627776    
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024
	else:
		factor = 1
	size = size.replace('T','')
	size = size.replace('B','')
	size = size.replace('M','')
	size = size.replace('K','')
	size = size.replace('G','')
	size = float(size)
	result = round(size * factor,0)
	return result

def gigSize( size ):
	size = int( size )
	return size / 1073741824


##########################################################################################################################




def volumeSizeInfo( letter ):
	# classy

	if _.isWin:
		total, used, free = shutil.disk_usage( letter + ':'+_v.slash )
	else:
		total, used, free = shutil.disk_usage( letter )

	volumeInfo = {
				'volumeSizeTotalInt': formatSizeInt(total),
				'volumeSizeTotal': formatSize(total),
				'volumeSizeUsed': formatSize(used),
				'volumeSizeFree': formatSize(free),
				'driveSize': estimateDriveSize(total),
	}

	return volumeInfo

##########################################################################################################################
def action():
	
	check = _.switches.all()
	if not check:
		os.system('cls')
		_.colorThis( [  '\n', 'Error:'  ], 'red' )
		_.colorThis( [  '\n', '\tA switch is required.\n'  ], 'yellow' )
		_.pr( _.colorThis( '\t\t Try:', 'yellow', p=0 ) , _.colorThis( 'p drive --help', 'green', p=0 ) )

	# sys.exit()

	if _.switches.isActive('Path'):
		_.pr('machineID:',machineID)
		_.pr(file_drives)
		_.pr(file_driveLog)

	if _.switches.isActive('Scan'):
		initiateScan()

	if _.switches.isActive('History'):
		historyLog()

	if _.switches.isActive('Index'):
		index()
		_qi.imp.action()

class Index_IDs:
	def __init__( self ):
		self.IDs = {}
	def newID( self, subject ):
		tID = _.miniUUID()
		if _.isWin:
			path = _v.cmdGetVar('userprofile') + _v.slash + '00' + tID
		else:
			path = _v.cmdGetVar('HOME') + _v.slash + '00' + tID
		self.IDs[subject] = { 'subject': subject, 'path': path, 'id': tID }
		return path
	def value( self, subject ):
		return self.IDs[subject]

class Indexing_DB:
	def __init__( self, subject ):
		self.subject
	def insert( self, data ):
		# dont forget to have *extension* as its own field,  possibly *dir* bk updated version is faster
		pass
	def complete( self ):
		pass

indexIDs = Index_IDs()

if _.isWin:
	indexTemp = _v.cmdGetVar('userprofile') + _v.slash + '00' + _.miniUUID()
else:
	indexTemp = _v.cmdGetVar('HOME') + _v.slash + '00' + _.miniUUID()
# indexTemp = _v.cmdGetVar('userprofile') + _v.slash + '00{3C2D3003A97C}'
machineID = _v.getMachineID()
file_drives = 'indexTable_drives-' + machineID + '.json'
file_driveLog = 'indexTable_logs-' + machineID + '.json'
driveTotal = 0
# _.pr(file_drives)
_.switches.fieldSet('Long','active',True)
########################################################################################
if __name__ == '__main__':
	action()


"""
linux
	next step?
		fcntl
			https://stackoverflow.com/questions/4193514/how-to-get-hard-disk-serial-number-using-python

	insert into?
		crossRefSerials


"""




