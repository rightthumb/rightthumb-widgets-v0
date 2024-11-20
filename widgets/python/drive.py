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
import sys
import time

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
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()

##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str

##################################################

def appSwitches():
	_.switches.register('Scan', '-scan')
	_.switches.register('Index', '-i,-index','usb, C:\\ D:'+_v.slash)
	_.switches.register('History', '-h,-history')
	_.switches.register('Path', '-p,-path')
	_.switches.register('RegisterIDs', '-ids,-id', 'optional file name here', isData='name', description='Register IDs')
	_.switches.register('JustID', '-justID')
	_.switches.register('formatSizeUp', '-sizeUp')
	_.switches.register('formatSize', '-size')
_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'drive.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Manages drives and indexes',
	'categories': [
						'index',
						'drive',
						'admin',
						'manage',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p drive -scan',
						'p drive -index usb',
						'p drive -index usb internal',
						'p drive -index C:\\Users\\Scott\\Desktop Desktop',
						'p drive -index C:\\ D:'+_v.slash,
						'p drive -index cloud',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
						{ 'name': 'name', 'abbreviation': 'n' },
						{ 'name': 'initiated', 'abbreviation': 'i' },
						{ 'name': 'type', 'abbreviation': 't' },
						{ 'name': 'priority', 'abbreviation': 'p' },
						{ 'name': 'drive', 'abbreviation': 'dldr' },
						{ 'name': 'machineID', 'abbreviation': 'm' },
						{ 'name': 'timestamp', 'abbreviation': 'tstimedate' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}
_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] }, 
		},
	}

def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True
		_.load()

		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()
	_.myFileLocation_Print = False
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.defaultScriptTriggers()
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
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )
_.postLoad( __file__ )

########################################################################################
# START


def genGUID():
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	result = str(string).upper()
	result = '{' + result + '}'
	return result

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

def get_drive_space(path):
	total, used, free = shutil.disk_usage(path)
	return {
		"total": total,
		"used": used,
		"free": free
	}

def ask( letter, instance, driveID=False ):
	if not driveID:
		driveID = genGUID()
	global drive_database
	global drive_records
	global machineID
	space = get_drive_space(letter)
	form = {
		'Config': {
			# 'html': True,
			# 'terminal': True,
			# 'post': 'https://cli.sds.sh/forms/',
			# 'table': 'Code_Snippet_Documentation',
			# 'save': 'forms-test.json',
			"field": {"width": 40}
		},
		'Code Snippet Documentation': [
			{'label': 'id', 'disabled': True, 'type': 'text', 'value': driveID},
			{'label': 'drive', 'type': 'text', 'value': letter},
			{'label': 'machineID', 'disabled': True, 'type': 'text', 'value': machineID},
			{'label': 'name', 'type': 'text', 'value': ''},
			{'label': 'description', 'type': 'text', 'value': ''},
			{'label': 'owner', 'type': 'text', 'value': ''},
			{'label': 'pc', 'type': 'text', 'value': socket.gethostname()},
			{'label': 'priority', 'type': 'text', 'value': '4'},
			{'label': 'date', 'disabled': True, 'type': 'text', 'value': _.friendlyDate(instance['timestamp']).split(' ')[0]},
			{'label': 'epoch', 'disabled': True, 'type': 'text', 'value': str(instance['timestamp'])},
			
			{'label': 'sizeF', 'type': 'text', 'value': _.formatSizeUp(space['total'])},
			{'label': 'usedF', 'disabled': True, 'type': 'text', 'value': _.formatSize(space['used'])},
			{'label': 'freeF', 'disabled': True, 'type': 'text', 'value': _.formatSize(space['free'])},
			
			{'label': 'sizeB', 'disabled': True, 'type': 'text', 'value': str(space['total'])},
			{'label': 'usedB', 'disabled': True, 'type': 'text', 'value': str(space['used'])},
			{'label': 'freeB', 'disabled': True, 'type': 'text', 'value': str(space['free'])},

			{'label': 'type', 'type': 'radio', 'options': ['internal', 'external', 'button', 'thumb'], 'value': 'thumb'},
		],
	}
	return _.Form(form)
def scanDrives():
	# print(genGUID())
	global drive_database
	global machineID
	instance = {'instance': genGUID(), 'timestamp': int(time.time()),'machineID': machineID, 'drives': []}
	record = False
	for l in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(','):
		letter = l + ':\\'
		idFile = letter + 'drive.id.sys'
		if os.path.isdir(letter):
			# _.pr(letter,c='green')
			if os.path.isfile(idFile):
				driveID = getID(letter)
				# print(drive_database,driveID)
				if not driveID in drive_database:
					record = ask( letter, instance, driveID )
					drive_database[driveID] = record
				else:
					record = drive_database[driveID]
					drive_database[driveID] = record
			else:
				record = ask( letter, instance )
				drive_database[driveID] = record
				file = open(idFile,'w') 
				file.write(driveID)
				file.close()
				
		if record:
			instance['drives'].append(record)

	return instance

def logSave(rows,theFile):
	if os.path.isfile(theFile) == True:
		theJSON = _.getTable(theFile)
	else:
		theJSON = []
	theJSON.append(rows)
	_.pr()
	_.saveTable(theJSON,theFile,True,False)



def round_up_to_nearest(size_in_bytes):
	import math
	# Define thresholds for GB and TB
	GB = 10**9
	TB = 10**12

	if size_in_bytes >= TB:
		# Convert to TB, round up to the nearest whole TB
		size_in_tb = math.ceil(size_in_bytes / TB)
		return f"{size_in_tb} TB"
	elif size_in_bytes >= GB:
		# Convert to GB, round up to the nearest whole GB
		size_in_gb = math.ceil(size_in_bytes / GB)
		return f"{size_in_gb} GB"
	else:
		# Smaller than 1 GB; return as bytes
		return f"{size_in_bytes} bytes"

import socket
import uuid
import time
import shutil

def action():
	if _.switches.isActive('formatSizeUp'):
		_.pr(_.formatSizeUp(int(_.switches.value('formatSizeUp'))))
		return False
	if _.switches.isActive('formatSize'):
		_.pr(_.formatSize(int(_.switches.value('formatSize'))))
		return False
	if _.switches.isActive('JustID'):
		_.pr(genGUID())
		return False
	global drive_database
	global machineID

	# Initialize variables
	drive_database = {}  # Initialize as empty dictionary
	machineID = _v.getMachineID()
	file_drives = 'indexTable_drives-1.3-' + machineID + '.index'
	file_driveLog = 'indexTable_logs-1.3-' + machineID + '.json'
	drive_database = _.getTable(file_drives) or {}
	
	if _.switches.isActive('RegisterIDs'):
		def isDict(idIndex,data):
			for idr in data:
				if not idr in idIndex:
					idIndex[idr] = data[idr]['name']
			return idIndex
		def isList(idIndex,data):
			for idr in data:
				if not idr['id'] in idIndex:
					idIndex[idr['id']] = idr['name']

			return idIndex
		idResolution = _.getTable('idResolution.json')
		idIndex = {}
		for idr in idResolution: idIndex[idr['id']] = idr['name']

		if not _.isData():
			idIndex = isList(idIndex,_.getTable('indexTable_drives-' + machineID + '.json'))
			idIndex = isDict(idIndex,drive_database)
		else:
			for path in _.isData():
				data = _.getTable2(path)
				if type(data) == list:
					idIndex = isList(idIndex,data)
				else:
					idIndex = isDict(idIndex,data)


		idResolution = []
		for idr in idIndex:
			idResolution.append({'id':idr,'name':idIndex[idr]})
		_.saveTable(idResolution,'idResolution.json')
		_.isExit(__file__)







	# Get drive records or initialize as empty list
	
	length = len(drive_database)
	drive_records = []
	for id in drive_database:
		drive_records.append(drive_database[id])
	_.switches.fieldSet('Long','active',True)
	_.pt(drive_records, 'drive,name,pc,priority,type,id')
	
	instance = scanDrives()
	logSave(instance, file_driveLog)
	if not length == len(drive_database):
		_.pr()
		_.saveTable(drive_database, file_drives)
		_.pr()

		drive_records = []
		for id in drive_database:
			drive_records.append(drive_database[id])
		_.switches.fieldSet('Long','active',True)
		_.pt(drive_records, 'drive,name,pc,priority,type,id')



	# _.pr( _drive.Scan().file_drives )
# 	i=0
# 	while i < 100:
# 		i+=1
# 		_.pr( 'Uncle Scotty, I just love being with you.',c='random' )
# 	_.e('drive is deprecated','and is now drive1')
# import _rightThumb._drive as _drive
# from _rightThumb._date import _date
# import _rightThumb._date as _date


# found an id, here is how to research it...
	# p dirDB + indexTable_drives - backup --c | p f3 + CDE18F2D7BEF -jn



########################################################################################
if __name__ == '__main__':
	action()
