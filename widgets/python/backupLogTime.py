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
	# _blowfish.genPassword('string')
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5


	# _filePathPatterns.switch( 'Files', _.switches.value('Files') )
##################################################

def appSwitches():
	pass
	_.switches.register( 'Ago', '-ago', isRequired=True, description='How long ago' )
	_.switches.register('NoCount', '--c,--count')
	_.switches.register('Fields', '-field,-fields')
	_.switches.register('All', '-all')

	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='' )


	_.switches.documentation( 'Ago', { 
										'examples': [
														'p backupLogTime -ago 2m',
														'p backupLogTime -ago 2d',
														'p backupLogTime -ago 2w',
														'p backupLogTime -ago 2y',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )


_.autoBackupData = True


_.appInfo[focus()] = {
	'file': 'backupLogTime.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Lookup items in backup log by time',
	'categories': [
						'audit',
						'tool',
						'backuplog',
						'backup log',
						'time',
						'history',
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
						'p backupLogTime -ago 1m',
						'p backupLogTime -ago 2w -fields file',
						'',
						'p backupLogTime -ago 1y -fields timestamp -all | p resolveIDs | sort',
						'',
						'p backupLogTime -ago 2d -fields timestamp version file0',
						'p backupLogTime -ago 2d -fields timestamp version file1',
						'p backupLogTime -ago 2d -fields timestamp version file2',
						'',
						'p backupLogTime -ago 2w -fields timestamp version file0 + *.php certificate',
						'p backupLogTime -ago 2w -fields timestamp version file0 backup + *.php certificate -long',
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

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )

########################################################################################
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# _.setPipeData( os.listdir(os.getcwd()), focus() )
# _.showLine(item)
#     if os.path.isdir(row):
#     if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START

def buildFields( record ):
	global records
	# base = "record['THIS']"
	result = []
	thisRecord = {}
	sss = 0
	for field in _.switches.values( 'Fields' ):
		
		if 'file' in field:
			f = field.replace( 'file', '' )
			field = 'file'
			if len(f):
				sss = 1
				s = int( f )
		# result.append( base.replace( 'THIS', field ) )
		if field == 'timestamp':
			result.append( '\t'+_.resolveEpochTest(record[field]) )
			thisRecord[field] = _.resolveEpochTest(record[field])

		elif sss:
			x = record[field].split(_v.slash)
			y = []
			x.reverse()
			ss = s
			while not ss == -1:
				try:
					y.append( x[ss] )
				except Exception as e:
					pass
				ss -=1
			

			z = _v.slash.join( y )
			result.append( '\t'+z )
			thisRecord[field] = z

			

		else:
			try:
				result.append( '\t'+str(record[field]) )
				thisRecord[field] = str(record[field])
			except Exception as e:
				result.append( '\t'+str('') )
				thisRecord[field] = ''
				pass
	pass
	# _.pr( '\t'.join( result ) )
	records.append( thisRecord )
	pass
	# if len( result ) == 6:
	#     _.pr( result[0], result[1], result[2], result[3], result[4], result[5] )
	# if len( result ) == 5:
	#     _.pr( result[0], result[1], result[2], result[3], result[4] )
	# if len( result ) == 4:
	#     _.pr( result[0], result[1], result[2], result[3] )
	# if len( result ) == 3:
	#     _.pr( result[0], result[1], result[2] )
	# if len( result ) == 2:
	#     _.pr( result[0], result[1] )
	# if len( result ) == 1:
	#     _.pr( result[0] )


def action():
	global data
	global records
	load()

	ago = _.timeAgo()

	# _.printTest( ago )
	# _.pr( ago )
	# sys.exit()
	spent = []
	files = 0
	edits = 0

	# statusValues = {}
	for record in data:

		# try:
		#     statusValues[record['status']]+=1
		# except Exception as e:
		#     statusValues[record['status']]=1
			
		if (record['timestamp']) > (ago):
			
			if record['status'] == 1 and _.showLine( record['file'] ):
				if _.switches.isActive( 'All' ) and _.switches.isActive( 'Fields' ):
					buildFields( record )
				edits+=1
				if not record['file'] in spent:
					if not _.switches.isActive( 'All' ) and _.switches.isActive( 'Fields' ):
						buildFields( record )
					spent.append( record['file'] )
					files+=1
	
	# _.printVar(statusValues)
	if len( records ):
		_.tables.register( 'data', records )
		_.tables.print( 'data', ','.join(records[0].keys()) )
	if not _.switches.isActive( 'NoCount' ):
		_.pr()
		_.pr( 'files:', _.addComma(files) )
		_.pr( 'edits:', _.addComma(edits) )
		_.pr()
		_.pr( 'fileBackup.json' )



def load():
	global data
	data = _.tables.returnSorted( 'data', 'd.timestamp', _.getTable('fileBackup.json') )
	_bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )
	_bkLog.do( _bkLog.imp.autoFileVersion )

records = []
data = []
########################################################################################
if __name__ == '__main__':
	action()







