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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str

# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )
##################################################
import datetime
# import dateutil.relativedelta
##################################################

def appSwitches():
	_.switches.register('Flag', '-flag')
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	# activate trigger in registerSwitches 
	


_.appInfo[focus()] = {
	'file': '_rightThumb._backupLog',
	'description': 'Toolkit for manipulating the backup log',
	'categories': [
						'import',
						'log',
						'log manipulation',
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

_.appInfo[focus()]['examples'].append('')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = True

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
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

_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )
	# _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()


########################################################################################
# START

def action():
	pass
	# if _.switches.isActive('Input'):
	#     setPipeData( _.getText( _.switches.value('Input') ) )

	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#     pass



# def diffDic( x, y ):
#     if x > y:
#         a = x
#         b = y
#     else:
#         a = y
#         b = x
#     dt1 = datetime.datetime.fromtimestamp(b)
#     dt2 = datetime.datetime.fromtimestamp(a)
#     rd = dateutil.relativedelta.relativedelta (dt2, dt1)
#     return { 'y': rd.years, 'm': rd.months, 'd': rd.days, 'h': rd.hours, 'm': rd.minutes, 's': rd.seconds }

# def diffList( x, y ):
#     if x > y:
#         a = x
#         b = y
#     else:
#         a = y
#         b = x
#     dt1 = datetime.datetime.fromtimestamp(b)
#     dt2 = datetime.datetime.fromtimestamp(a)
#     rd = dateutil.relativedelta.relativedelta (dt2, dt1)
#     return [rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds]

# def diffPrint( x, y ):
#     if x > y:
#         a = x
#         b = y
#     else:
#         a = y
#         b = x
#     dt1 = datetime.datetime.fromtimestamp(b)
#     dt2 = datetime.datetime.fromtimestamp(a)
#     rd = dateutil.relativedelta.relativedelta (dt2, dt1)
#     return "%d years, %d months, %d days, %d hours, %d minutes and %d seconds" % (rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds)

def epochSec( x, y ):
	if x > y:
		a = x
		b = y
	else:
		a = y
		b = x
	return a - b

TheBackupFile = _v.table('fileBackup.json')

def setBackupFile(file=None):
	global TheBackupFile
	if not file is None:
		TheBackupFile = file
	return TheBackupFile
def loadBackupFile():
	global TheBackupFile
	global backupLog
	backupLog = _.getTable2(TheBackupFile)
	return backupLog
def addFlagIfHasBackup( backup ):
	global backupLog
	global TheBackupFile
	backupLog = loadBackupFile()

	for  i,log in enumerate(backupLog):
		backupLog[i]['file'] == __.path(backupLog[i]['file'])
		if log['backup'] == backup:
			flag = log['flag']
			# flag = _str.cleanBE( flag, ' ' )
			flag = flag.strip()
			flag = _str.cleanBE( flag, ',' )

			if len( str(flag) ) > 0:
				backupLog[i]['flag'] = flag + ',' + _.switches.value('Flag')
			else:
				backupLog[i]['flag'] = flag = _.switches.value('Flag')

			backupLog[i]['flag'] = backupLog[i]['flag'].strip()
			backupLog[i]['flag'] = _str.cleanBE( backupLog[i]['flag'], ',' )
			
	_.saveTable2( backupLog, TheBackupFile, printThis=False )


def autoFileVersion():
	global TheBackupFile
	if True:
		backupLog_epoch = os.path.getmtime( TheBackupFile )
		# _.pr( backupLog_epoch )
		if os.path.isfile( _v.table('fileBackup-versions-epoch.json') ):
			lastEpoch = _.getTable( 'fileBackup-versions-epoch.json' )['epoch']
			# _.pr(lastEpoch, backupLog_epoch-lastEpoch)
			if backupLog_epoch ==  lastEpoch:
				# _.cp( 'version calc skipped', 'green' )
				return None



	_.updateLine( ' Processing: backuplog version audit' )
	global ticket_transfer
	global backupLog
	global printLogName
	global autoVersionUpdate
	global deletedRecords

	ticket_transfer = _.getTable( 'ticket_transfer.index' )

	backupLog = _.tables.returnSorted( TheBackupFile, 'a.timestamp', loadBackupFile() )
	preClean = len(backupLog)
	newLog = []
	for i,d in enumerate(backupLog):
		if os.path.isfile(d['backup']):
			nr = cleanRecord( i, d )
			if not nr is None:
				newLog.append( nr )
	postClean = len(newLog)
	
	global fv
	_.saveTable( fv, 'fileBackup-versions.json', printThis=False )
	
	if type(deletedRecords) == list and len(deletedRecords):
		# _.cp( [ 'fileBackup cleaned', len(deletedRecords), ' records' ], 'green' )
		# _.pr( preClean, postClean )
		_.saveTable( deletedRecords, 'fileBackup-deleted.json', p=0 )


	for  i,record in enumerate(newLog):
		if record['timestamp'] in autoVersionUpdate:


			flag = record['flag']
			flag = _str.cleanBE( flag, ' ' )
			flag = _str.cleanBE( flag, ',' )
			flags = flag.lower().split(',')
			if not 'mv' in flags:
				newLog[i]['flag'] = str(flag) + ',MV'
			newLog[i]['flag'] = _str.cleanBE( newLog[i]['flag'], ' ' )
			newLog[i]['flag'] = _str.cleanBE( newLog[i]['flag'], ',' )
			newLog[i]['flag'] = newLog[i]['flag'].replace( ',,', ',' )
			newLog[i]['flag'] = newLog[i]['flag'].replace( ',,', ',' )


			# newLog[i]['v1'] += 1
			# newLog[i]['v2'] = 0
			# newLog[i]['version'] = str(newLog[i]['v']) + '.' + str(newLog[i]['v1']) + '.' + str(newLog[i]['v2']) + '.' + str(newLog[i]['v3'])
	backupLog = newLog
	autoBatchIdentify()
	_.saveTable2( backupLog, TheBackupFile, printThis=printLogName )
	# _.saveCSV(   backupLog, 'fileBackup.csv',  printThis=printLogName )
	backupLog_epoch = os.path.getmtime( TheBackupFile )
	_.saveTable( { 'epoch': backupLog_epoch }, 'fileBackup-versions-epoch.json', printThis=False )
	_.updateLine( '                                                   ' )
	_.pr()


def getFlags( data ):
	flag = data
	flag = _str.cleanBE( flag, ' ' )
	flag = _str.cleanBE( flag, ',' )
	flags = flag.lower().split(',')
	return flags

def cleanFlags( data ):
	flag = data
	flag = _str.cleanBE( flag, ' ' )
	flag = _str.cleanBE( flag, ',' )
	return flag

def removeFromFlags( data, remove ):
	if not remove in data:
		return data
	flag = data
	flag = _str.cleanBE( flag, ' ' )
	flag = _str.cleanBE( flag, ',' )
	flags = flag.split(',')

	newFlags = []
	for f in flags:
		if not remove in f:
			f = _str.cleanBE( f, ' ' )
			newFlags.append( f )
	newFlag = ','.join( newFlags )
	newFlag = _str.cleanBE( newFlag, ' ' )
	newFlag = _str.cleanBE( newFlag, ',' )
	return newFlag

if _.isWin:
	l = True
else:
	l = False

def subject( f ):
	global l
	if l:
		return f.lower()
	else:
		return f

lastVersion = {}

def cleanRecord( i, record ):
	global deletedRecords
	global spentBackupFile
	global backupLog
	global autoVersionUpdate
	global lastVersion
	global fv

	if deletedRecords is None:
		deletedRecords = _.getTable( 'fileBackup-deleted.json' )

	if record['backup'].lower() in spentBackupFile:
		deletedRecords.append(record)
		# _.pr( i )
		return None
	spentBackupFile[record['backup'].lower()] = 1

	record['file'] = record['file'][0].upper() + record['file'][1:]

	f = subject(record['file'])
	# flag = record['flag'].lower().split(',')
	try:
		flags = getFlags( record['flag'] )
	except Exception as e:
		flags = ''

	try:
		record['mime']
	except Exception as e:
		record['mime'] = 'text'

	try:
		record['status']
	except Exception as e:
		record['status'] = 1


	epoch = record['timestamp']
	newRecord = {}
	newRecord['id'] = record['id']
	newRecord['timestamp'] = record['timestamp']
	newRecord['file'] = record['file']
	newRecord['backup'] = record['backup']

	newRecord['mime'] = record['mime']
	newRecord['status'] = record['status']

	global ticket_transfer
	try:
		if 'session' in record:
			if record['session'] in ticket_transfer['old']:
				newRecord['session'] = ticket_transfer['old'][ record['session'] ]
			else:
				newRecord['session'] = record['session']
		else:
			newRecord['session'] = ''
	except Exception as e:
		newRecord['session'] = ''


	if not f in fv:
		fv[f] = {}
	if not 'v' in fv[f]:
		fv[f]['v'] = 0
	if not 'v1' in fv[f]:
		fv[f]['v1'] = 0
	if not 'v2' in fv[f]:
		fv[f]['v2'] = 0
	if not 'v3' in fv[f]:
		fv[f]['v3'] = 0
	if not 'epoch' in fv[f]:
		fv[f]['epoch'] = 0


	fv[f]['v3'] += 1
	if fv[f]['v3'] > 1:
		if 'v' in flags:
			fv[f]['v'] += 1
			fv[f]['v1'] = 0
			fv[f]['v2'] = 0
		elif epochSec( fv[f]['epoch'], epoch ) > 604800:
			# _.pr( getFlags( backupLog[fv[f]['i']]['flag'].lower() ) )
			# if 'flag' in record and len(record['flag']) and 'v' in getFlags( backupLog[fv[f]['i']]['flag'].lower() ):
			if 'flag' in record and len(record['flag']) and 'v' in getFlags( record['flag'].lower() ):
				fv[f]['v2'] += 1
			else:
				autoVersionUpdate.append( fv[f]['epoch'] )
				fv[f]['v1'] += 1
				fv[f]['v2'] = 1
		else:
			fv[f]['v2'] += 1

	fv[f]['epoch'] = epoch
	fv[f]['i'] = i

	if fv[f]['v3'] == 1:
		fv[f]['v2'] = 0
		fv[f]['v1'] = 0

	# fv[f]['epoch'] = epoch
	# try:
	# except Exception as e:

	#     if False:
	#         fv[f] = {
	#                     "epoch": epoch,
	#                     "v": 0,
	#                     "v1": 0,
	#                     "v2": 0,
	#                     "v3": 1
	#         }

	newRecord['version'] = str(fv[f]['v']) + '.' + str(fv[f]['v1']) + '.' + str(fv[f]['v2']) + '.' + str(fv[f]['v3'])
	if f in lastVersion:
		if lastVersion[f] == newRecord['version']:
			fv[f]['v3'] += 1
			newRecord['version'] = str(fv[f]['v']) + '.' + str(fv[f]['v1']) + '.' + str(fv[f]['v2']) + '.' + str(fv[f]['v3'])
	if '0.1.0.1' == newRecord['version']:
		newRecord['version'] = '0.0.0.1'
		fv[f]['v2'] = 0
		fv[f]['v1'] = 0
	lastVersion[f] = newRecord['version']
	newRecord['v'] = fv[f]['v']
	newRecord['v1'] = fv[f]['v1']
	newRecord['v2'] = fv[f]['v2']
	newRecord['v3'] = fv[f]['v3']
	# newRecord['file'] = newRecord['file'][0].upper() + newRecord['file'][1:]
	newRecord['backup'] = newRecord['backup'][0].upper() + newRecord['backup'][1:]
	

	if not 'name' in newRecord:
		parts = newRecord['file'].split(_v.slash)
		parts.reverse()
		newRecord['name'] = parts.pop(0)

	try:
		newRecord['flag'] = record['flag']
	except Exception as e:
		newRecord['flag'] = ''
		# _.pr( 'Error: field, flag' )
		# _.printVar( record )
		# sys.exit()
	return newRecord


# def updateAutoVersion( epoch ):
#     global backupLog

#     for  i,record in enumerate(backupLog):
#         if record['timestamp'] == epoch:
#             flag = record['flag']
#             flag = _str.cleanBE( flag, ' ' )
#             flag = _str.cleanBE( flag, ',' )
#             flags = flag.lower().split(',')
#             backupLog[i]['v1'] += 1
#             backupLog[i]['v2'] = 0
#             if not 'mv' in flags:
#                 backupLog[i]['flag'] = str(flag) + ',MV'
#             backupLog[i]['flag'] = _str.cleanBE( backupLog[i]['flag'], ' ' )
#             backupLog[i]['flag'] = _str.cleanBE( backupLog[i]['flag'], ',' )



def autoBatchIdentify():
	global backupLog
	global groupSeconds


	groupID = 0
	groupList = {}
	epochList = []

	last = time.time()
	lg = False
	for i,log in enumerate(backupLog):
		backupLog[i]['flag'] = removeFromFlags( log['flag'], '(G' )
		x = epochSec( last, log['timestamp'] )
		# y = diffPrint( last, log['timestamp'] )
		if x < groupSeconds:
			if not lg:
				pass
				# _.pr()
			lg = True

			if not last in epochList:
				epochList.append( last )
				groupList[ last ] = groupID

			if not log['timestamp'] in epochList:
				epochList.append( log['timestamp'] )
				groupList[ log['timestamp'] ] = groupID

			# _.pr( groupID, '\t', x, '\t', y, '\t', _.resolveEpochTest( log['timestamp'] ), log['flag'] )
		else:
			if lg == True:
				lg = False
				groupID += 1

		last = log['timestamp']

	for i,log in enumerate(backupLog):
		if log['timestamp'] in epochList:
			newFlag = str(log['flag']) + ',(G' + str( groupList[ log['timestamp'] ] ) + ')'
			backupLog[i]['flag'] = cleanFlags( newFlag )

def validateFlag( data ):
	data = _str.replaceDuplicate( data, ' ' )
	data = _str.cleanBE( data, ' ' )
	if data == 'v':
		data = 'V'
	return data

groupSeconds = 3
printLogName =False
fv = {}
backupLog = []
autoVersionUpdate = []
deletedRecords = None
spentBackupFile = {}


########################################################################################
if __name__ == '__main__':
	action()

# _bkLog.do( _bkLog.imp.autoFileVersion )







