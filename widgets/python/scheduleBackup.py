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
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Clean', '-c,-count,--c')

	_.switches.register('Folder', '-f,-folder')

	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Binary', '-bin')

	_.switches.register('Recursive', '-r,-recursive')
	_.switches.register('Confirm', '-confirm')
	_.switches.register('BackupOnce', '-once')

	_.switches.register('FullPath', '-path')
	



_.appInfo[focus()] = {
	'file': 'scheduleBackup.py',
	'description': 'Schedule files to backup once or as regular',
	'copy': 'files',
	'categories': [
						'schedule Backup',
						'scheduleBackup',
						'schedule',
						'scheduler',
						'backup',
						'recursive',
						'files',
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
						'p scheduleBackup -r + index ',
						'p scheduleBackup -bin ',
						'p scheduleBackup -bin -confirm',
						'',
						'p scheduleBackup -once -confirm',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
	],
	'aliases': [
					# 'this',
					# 'app',
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

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
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
########################################################################################
# START



def isText(file):
	return _mime.isText(file)

def whatIsIt(file):
	if isText(file):
		result = 'Text'
	else:
		result = 'Binary'
	return result

def getFolder(folder):
	global i
	global scheduler
	global scheduleStatus
	global epoch

	try:
		dirList = os.listdir(folder)
		takeAction = True
	except Exception as e:
		takeAction = False
	if takeAction:
		if os.path.isdir(folder):
			dirList = os.listdir(folder)
		for item in dirList:
			path = folder + _v.slash + item
			path = path.replace(_v.slash+_v.slash,_v.slash)
			if os.path.isfile(path):

				if _.showLine(path):

					shouldInclude = False
					if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
						i = i + 1
						# _.pr(0,whatIsIt(path),path)
						# _.pr(path)
						shouldInclude = True

					else:
						if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
							i = i + 1
							# _.pr(1,whatIsIt(path),path)
							# _.pr(path)
							shouldInclude = True

						if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
							i = i + 1
							# _.pr(2,whatIsIt(path),path)
							# _.pr(path)
							shouldInclude = True

						if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
							i = i + 1
							# _.pr(3,whatIsIt(path),path)
							# _.pr(path)
							shouldInclude = True

						if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
							i = i + 1
							# _.pr(4,whatIsIt(path),path)
							# _.pr(path)
							shouldInclude = True

					if shouldInclude:

						if _.switches.isActive('FullPath'):

							if not _.switches.isActive('Confirm') and _.switches.isActive('Clean'):
								_.colorThis( [  path  ], 'purple' )
							else:
								_.colorThis( [  path  ], 'cyan' )

						else:
							_.colorThis( [  '\t', path.replace( os.getcwd()+_v.slash, '' )  ], 'cyan' )

						# _.pr( path )
						if _.switches.isActive('Confirm'):
							if _.switches.isActive('BackupOnce'):
								status = scheduleStatus['onceActive']
							else:
								status = scheduleStatus['default']

							scheduler.append( { 'timestamp': time.time(), 'file': path, 'status': status, 'app': 'scheduleBackup', 'group': epoch } )

						


	

 


			elif os.path.isdir(path) and _.switches.isActive('Recursive'):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):
					try:
						getFolder(newFolder)
					except Exception as e:
						pass
				else:
					_.pr('error')






def action():
	global i
	global scheduler
	load()

	if not _.switches.isActive('Clean'):
		_.pr()
		_.colorThis( [  'Files:'  ], 'yellow' )
		_.pr()

	if _.switches.isActive('Folder') == False:
		folder = os.getcwd()
	else:
		folder = _.switches.value('Folder')
	
	getFolder(folder)

	if not _.switches.isActive('Clean'):
		_.pr()
		if i:
			if not _.switches.isActive('Confirm'):
				msg = _.colorThis( [  '', i, ''  ], 'yellow', p=0 )
				msg += _.colorThis( [  'files would have been scheduled to backup'  ], 'green', p=0 )
				_.pr( msg )
				
				_.colorThis( 'Preview: nothing scheduled to backup', 'red' )
			else:
				msg = _.colorThis( [  '', i, ''  ], 'yellow', p=0 )
				msg += _.colorThis( [  'files scheduled to backup'  ], 'green', p=0 )
				_.pr( msg )


	
	if _.switches.isActive('Confirm'):
		_.saveTable( scheduler, 'fileBackupSchedule.json', p=0 )

i = 0

def load():
	global scheduler
	scheduler = _.getTable('fileBackupSchedule.json')


scheduleStatus = {
					'default': 0,
					'defaultSpent': 1,
					'defaultSpentAltID': 2,
					'defaultDeactivated': 33,

					'onceActive': 50,
					'onceSpent': 100,

					'onceDeactivated': 333,
}
epoch = time.time()
scheduler = []
########################################################################################
if __name__ == '__main__':
	action()






