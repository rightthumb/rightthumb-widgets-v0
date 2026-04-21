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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._encryptString as _blowfish
# import _rightThumb._date as _date
import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
##################################################

def appSwitches():
	pass
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'updateQuickIndex.py',
	'description': 'Updates index of frequently used files',
	'categories': [
						'research',
						'index',
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

_.appInfo[focus()]['examples'].append('p updateQuickIndex')

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

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	
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

_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
# START
def isInternal( item ):
	global drive_records
	# item = item[1:-1]
	if not '{' in item:
		item = ''
	else:
		item = '{' + item.split( '{' )[1]

	for i,row in enumerate(drive_records):
		if item == drive_records[i]['id'] and drive_records[i]['type'].lower() == 'internal':
			return True
	return False

def action():
	global results
	today = _.resolveEpochTest( time.time() ).split( ' ' )[0]
	dirList = os.listdir(_v.myIndexes)
	for i,item in enumerate(dirList):
		path = _v.myIndexes + _v.slash + item
		if os.path.isfile( path ):
			# if _dir.fileInfo( path )['date_created'].split( ' ' )[0] == today:
			# _.pr( item )
			if isInternal( item ):
				processFile( path )
	_.saveText( results, _v.quickIndex )
	_.pr( 'Quick index updated' )
	_.pr( _v.quickIndex )

def processFile( path ):
	global results
	
	file = _.getText( path )
	for row in file:
		row = row.replace( '\n', '' )
		if testPath( row ):
			results.append( row )
	return results

def testPath( path ):
	global folderList

	for test in folderList:
		if test in path:
			return True
	
	return False



results = []
profile = 'Desktop,Documents,Downloads,Music,OneDrive,Pictures,SendTo,SkyDrive,Start Menu,Videos'
folders = 'D:\\_Scott,D:\\tech,D:\\Files,D:\\Chat,C:\\tech'
folderList = folders.split( ',' )
p = _v.getUserProfile()
for f in profile.split( ',' ):
	folderList.append( p + _v.slash + f )
file_drives = 'indexTable_drives-' + _v.getMachineID() + '.json'
drive_records = _.getTable( file_drives )
# _v.quickIndex
########################################################################################
if __name__ == '__main__':
	action()







