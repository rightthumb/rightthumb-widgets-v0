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
# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword('string')
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
#     _blowfish.encrypt( infilepath, outfilepath, key )
#     _blowfish.decrypt( infilepath, outfilepath, key )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browserX = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

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
# _file_folder = _.regImp( __.appReg, 'file_folder' )
#     _file_folder.switch( 'Save,Clean' )
#     _file_folder.switch( 'Compair,Clean' )
#     _file_folder.switch( 'Folder', '' )
# _fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
#     _fileNameDate.imp.newName( filename )
#     _fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )
# _filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	# _filePathPatterns.switch( 'NoPrint' )
	# _filePathPatterns.switch( 'Files', _.switches.value('Files') )
	# folderReport = _filePathPatterns.action()
# txtBackup = _.regImp( __.appReg, 'txtBackup' )
#     txtBackup.switch( 'Input', filename )
#     txtBackup.switch( 'Flag', 'pre replaceText' )
#     recoveryFile = txtBackup.do( 'action' )
# _folderContent = _.regImp( __.appReg, 'file' )
#     _folderContent.switch( 'Silent' )
#     _folderContent.switch( 'Folder', _v.myAppsBatch )
#     _folderContent.switch( 'NoExtension' )

#     _folderContent.switch( 'Recursive' )

#     _folderContent.switch( 'Text' )
#     _folderContent.switch( 'Binary' )
#     _folderContent.switch( 'Label', 'App: ' )
#     _folderContent.switch( 'Prefix', ';t' )
#     files = _folderContent.do( 'action' )['files']
#     folders = _folderContent.do( 'action' )['folders']
# _tickets = _.regImp( __.appReg, 'ticketTimeline' )
#     _tickets.switch( 'ReturnFiles' )
#     records = _tickets.do( 'records' )
##################################################

##################################################


def appSwitches():
	pass
	_.switches.register( 'Good', '-good','good.CSV', isRequired=True, description='Files' )
	_.switches.register( 'Bad', '-bad','bad.CSV', isRequired=True, description='Files' )


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'processMonitor_xRef.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Cross ref',
	'categories': [
						'tool',
						'Procmon',
						'Process monitor',
						'Process',
						'monitor',
						'cross reference',
						'cross',
						'reference',
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
						'p regScanMon -file Procmon_log_.CSV',
						'p regScanMon -file outlook_reg_sample.CSV + .pst',
						'p regScanMon -file outlook_reg_sample.CSV + .pst -key hkcu -table',
						''
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

def extract( data ):
	records = []
	for row in data.split('\n'):
		if 'REG_EXPAND_SZ' in row or 'REG_SZ' in row or 'REG_DWORD' in row:
			if 'REG_EXPAND_SZ' in row:
				data = row.split( 'REG_EXPAND_SZ' )
			if 'REG_SZ' in row:
				data = row.split( 'REG_SZ' )
			if 'REG_DWORD' in row:
				data = row.split( 'REG_DWORD' )
			if len( data ) > 1:
				for i,d in enumerate( data ):
					data[i] = _str.replaceDuplicate (data[i], ' ' )
					data[i] = data[i].replace( '\t', '' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
				records.append({ 'field': data[0], 'value': data[1]  })
	return records
				



def action():
	global data
	global spent
	global log

	load()

	omit = {
				'RegQueryKey': [ 'BUFFER TOO SMALL' ],
				'CreateFile': [ 'CreateFile' ],
	}

	# tempSpent = []
	# for i,record in enumerate(data['bad']):
	#     item = record['Operation'] +', '+ record['Result']
	#     if not item in tempSpent:
	#         _.pr( item )
	#         tempSpent.append( item )

	# for i,record in enumerate(data['good']):
	#     item = record['Operation'] +', '+ record['Result']
	#     if not item in tempSpent:
	#         _.pr( item )
	#         tempSpent.append( item )


	# sys.exit()

	_.pr()
	_.pr()

	errorsSpent = []
	for i,record in enumerate(data['good']):
		if record['Result'] == 'SUCCESS':

			if '.pst' in record['Path'].lower() and 'grow' in record['Path'].lower():
				# _.pr()
				# _.pr()
				# _.pr()
				# _.pr()
				# _.printTest( record, x=0 )
				# _.pr()
				# _.pr()
				# _.printTest( data['index'][ record['Path'].lower() ], x=0 )
			# if i:
				try:


					for test in data['index'][ record['Path'].lower() ]:

						# if not test['Operation'] == record['Operation']:
						#     _.pr( test['Path'], record['Operation'], test['Operation'] )
						if test['Operation'] == record['Operation']:

							# spent['good'] = test['Sort']
							# data['map'].append([ record, test ])

							if not test['Result'] == record['Result']:
								if test['Result'] in omit.keys() and test['Result'] in omit[record['Result']]:
									pass
								else:
									thisError = test['Operation']+','+test['Result']+','+test['Path'].lower()
									if not thisError in errorsSpent:
										errorsSpent.append( thisError )
										_.pr( record['Operation'],  test['Result'], test['Path'] )


				except Exception as e:
					pass

		# if i:
		#     _.pr( record.keys() )
		#     _.printTest( record )


"""
	{
		"Sequence": "n/a"
		"Time of Day": "8:55:31.9494627 PM",
		"Process Name": "OUTLOOK.EXE",
		"PID": "8212",
		"Operation": "Thread Create",
		"Path": "",
		"Result": "SUCCESS",
		"Detail": "Thread ID: 13940",
	}
"""


def load():
	global data

	data['good'] = _.csv( _.switches.values('Good')[0] )
	for i,record in enumerate(data['good']):
		data['good'][i]['Sort'] = i

		if record['Path'].endswith(_v.slash):
			record['Path'] = record['Path'][:-1]
			data['good'][i]['Path'] = record['Path']



	data['bad'] = _.csv( _.switches.values('Bad')[0] )
	for i,record in enumerate(data['bad']):
		data['bad'][i]['Sort'] = i

		if record['Path'].endswith(_v.slash):
			record['Path'] = record['Path'][:-1]
			data['bad'][i]['Path'] = record['Path']

		label = record['Path'].lower()
		
		try:
			data['index'][label].append(record)
		except Exception as e:
			data['index'][label] = []
			data['index'][label].append(record)


	# data['index']


data = { 'good': [], 'bad': [], 'index': {}, 'map': [] }
spent = { 'good': -1, 'bad': -1 }
log = []
########################################################################################
if __name__ == '__main__':
	action()