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
	_.switches.register('unformatSize', '-usize')
	_.switches.register('Bits2Bytes', '-bbsize')
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
def get_drive_info(drive_letter):
	import win32com.client
	drive_letter = drive_letter.rstrip("\\")  # Remove trailing backslash if present
	wmi = win32com.client.GetObject("winmgmts:")
	
	# Iterate over logical disks to find the matching drive letter
	for logical_disk in wmi.InstancesOf("Win32_LogicalDisk"):
		if logical_disk.DeviceID == drive_letter:
			# Find the associated partition
			for partition in logical_disk.Associators_("Win32_LogicalDiskToPartition"):
				# Find the physical disk associated with the partition
				for disk in partition.Associators_("Win32_DiskDriveToDiskPartition"):
					serial = disk.SerialNumber
					while serial.startswith('0') or serial.startswith('_'):
						serial = serial[1:]
					if serial.endswith('.'):
						serial = serial[:-1]
					return {
						"drive": drive_letter.strip(),
						"model": disk.Model.strip(),
						"serial": serial.strip()
					}
	return {
				"drive": '?',
				"model": '?',
				"serial": '?'
			}
def ask( letter, instance, driveID=False ):
	ms = get_drive_info(letter)
	if not driveID:
		driveID = genGUID()
	global drive_database
	global drive_records
	global machineID
	space = get_drive_space(letter)
	global recover
	rec = {}
	if recover and driveID and driveID in recover:
		rec['name'] = recover[driveID]['name']
		rec['description'] = recover[driveID]['description']
		rec['owner'] = recover[driveID]['owner']
		rec['priority'] = recover[driveID]['priority']
		rec['type'] = recover[driveID]['type']
		rec['sizeF'] = recover[driveID]['sizeF']
	else:
		rec['name'] = ''
		rec['description'] = ''
		rec['owner'] = 'Scott'
		rec['priority'] = '4'
		rec['type'] = 'thumb'
		rec['sizeF'] = _.formatSizeUp(space['total'])
	form = {
		'Config': {
			# 'html': True,
			# 'terminal': True,
			# 'post': 'https://cli.sds.sh/forms/',
			# 'table': 'Code_Snippet_Documentation',
			# 'save': 'forms-test.json',
			"field": {"width": 45}
		},
		'Code Snippet Documentation': [
			{'label': 'id', 'disabled': True, 'type': 'text', 'value': driveID},
			{'label': 'drive', 'type': 'text', 'value': letter},
			{'label': 'model', 'disabled': True, 'type': 'text', 'value': ms['model']},
			{'label': 'serial', 'disabled': True, 'type': 'text', 'value': ms['serial']},
			{'label': 'machineID', 'disabled': True, 'type': 'text', 'value': machineID},
			{'label': 'name', 'type': 'text', 'value': rec['name']},
			{'label': 'description', 'type': 'text', 'value': rec['description']},
			{'label': 'owner', 'type': 'text', 'value': rec['owner']},
			{'label': 'pc', 'type': 'text', 'value': socket.gethostname()},
			{'label': 'priority', 'type': 'text', 'value': rec['priority']},
			{'label': 'date', 'disabled': True, 'type': 'text', 'value': _.friendlyDate(instance['timestamp']).split(' ')[0]},
			{'label': 'epoch', 'disabled': True, 'type': 'text', 'value': str(instance['timestamp'])},
			
			{'label': 'sizeF', 'type': 'text', 'value': rec['sizeF'] },
			{'label': 'usedF', 'disabled': True, 'type': 'text', 'value': _.formatSize(space['used'])},
			{'label': 'freeF', 'disabled': True, 'type': 'text', 'value': _.formatSize(space['free'])},
			
			{'label': 'sizeB', 'disabled': True, 'type': 'text', 'value': str(space['total'])},
			{'label': 'usedB', 'disabled': True, 'type': 'text', 'value': str(space['used'])},
			{'label': 'freeB', 'disabled': True, 'type': 'text', 'value': str(space['free'])},

			{'label': 'type', 'type': 'radio', 'options': ['internal', 'external', 'button', 'thumb'], 'value': rec['type']},
		],
	}
	record = _.Form(form)
	_.pr(line=1,c='green')
	_.pv(record)
	_.pr(line=1,c='green')
	global drive_database
	global file_drives
	drive_database[record['id']] = record
	_.saveTable(drive_database, file_drives)
	return record
def scanDrives():
	# print(genGUID())
	global drive_database
	global machineID
	driveID = False
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
					printDrives()
					record = ask( letter, instance, driveID )
					drive_database[driveID] = record
				else:
					record = drive_database[driveID]
					drive_database[driveID] = record
			else:
				printDrives()
				record = ask( letter, instance )
				drive_database[driveID] = record
				file = open(idFile,'w') 
				file.write(driveID)
				file.close()
		global ActiveDrives
		ActiveDrives.append(driveID)
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
printDrives_printed = False
def printDrives():
	global drive_database
	global printDrives_printed
	if not printDrives_printed:
		printDrives_printed = True
		drive_records = []
		for id in drive_database:
			rec = drive_database[id]
			drive_records.append(rec)
		_.pt(drive_records, 'drive,name,pc,priority,type,id',long=1)
def action():
	global ActiveDrives
	global printDrives_printed
	ActiveDrives = []
	if _.switches.isActive('Bits2Bytes'):
		original = ' '.join(_.switches.values('Bits2Bytes')).upper()
		fixed = original.strip('ps')
		fixed = original.strip('s')
		if original.lower().endswith('ps'):
			end = 'ps'
		elif original.lower().endswith('s'):
			end = 's'
		else:
			end = ''
		_.pr(  _.formatSize(int(_.unFormatSize(fixed))/8)+end )
		return False
	if _.switches.isActive('unformatSize'):
		_.pr(_.unFormatSize(  ' '.join(_.switches.values('unformatSize'))  ))
		return False
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
	global file_drives
	global recover

	# Initialize variables
	drive_database = {}  # Initialize as empty dictionary
	machineID = _v.getMachineID()
	fdr = '_indexTable_drives-1.3-' + machineID + '.index'
	file_drives = 'indexTable_drives-1.3-' + machineID + '.index'
	file_driveLog = 'indexTable_logs-1.3-' + machineID + '.json'
	drive_database = _.getTable(file_drives) or {}
	recover = _.getTable(fdr) or {}
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
	
	# _.switches.fieldSet('Long','active',True)
	length = len(drive_database)

	
	instance = scanDrives()
	logSave(instance, file_driveLog)
	if not length == len(drive_database) or printDrives_printed == False:
		# _.pr()
		# _.saveTable(drive_database, file_drives)
		_.pr()

		drive_records = []
		for id in drive_database:
			rec = drive_database[id]
			if id in ActiveDrives:
				rec['attached'] = 'Yes'
			else:
				rec['attached'] = ''
			drive_records.append(rec)

		def fp(): _.tables.fieldProfileSet('default','attached','alignment','right')
		_.pt(drive_records, 'attached,drive,name,pc,priority,type,id',fn=fp,long=1)



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
