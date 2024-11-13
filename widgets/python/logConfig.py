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
# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
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

##################################################

# from lxml import html
# import requests
# import cssselect
import webbrowser

##################################################


def appSwitches():
	pass
	_.switches.register('Input', '-i,-f,-file','file.json')
	_.switches.register('Label', '-l,-label')

	



_.appInfo[focus()] = {
	'file': 'logConfig.py',
	'description': 'Preps log for config app',
	'categories': [
						'management',
						'maintanance',
						'log',
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

_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['examples'].append('p logConfig -i indexTable_drives-{B1669E09-DB5B-E77C-7B53-65EE04FBF88E}.json -l drive log')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})





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
	# _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



########################################################################

# def processFolder(folder, qID):
# __.queueLastActivity = time.time()
# __.projectData[focus()][__.pdID[focus()]].append( obj )
# _.threads.add( 'test', testFunction, [{'two':item}], kwargs=True )
# _.threads.add( 'process_folder', processFolder, [ path ] )
# _.threads.spent( qID, sys.getsizeof( 'obj') )
					################
# _.threads.add( 'test', trigger=complete, triggerArg={'hello','test'}, loaded=False )
# _.threads.add( 'test', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
# _.threads.maxThreadsSafe = 250
# _.threads.report = True
# _.threads.projectDataFileSQL = db
# _.threads.auditPrint = False

##################

# _.appData[focus()]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
# _.appInfo[focus()]['instance'] = _.genUUID()
# # _.appData[focus()]['audit'].append( { 'start': True, 'note': '', 'entire': True, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );

# _dir.sqlCreateTable( db, deleteDBFirst=True, close=True )
# obj = _dir.fileInfo( path, sql=True )
# _.pr(   _dir.fileInfo( _.switches.value('Input') )['size']   )

# _.saveLog('queue')
# _.saveLog('audit')

########################################################################

# os.path.isfile(files)
# os.system('cls')

# _.switches.isActive('_File_')
# global

# _.appInfo[focus()]['categories']

# #######################################
# uuidProject = { 'input': _.switches.value('Input'), 'note': 'sample' }
# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[__.appReg]['file'], 'project': uuidProject }
# _.genUUID(project='')
# _.genUUID('temp file')
# _.genUUID({'file':'app.py'})
# #######################################
# import blank
# blank.focus(focus())
# blank.registerSwitches()
# _.switches.fieldSet('Input','active','one')
# _.switches.fieldSet('Input','value','one')
# focus()
# #######################################

# _.switches.fieldSet('_File_','active',True)

# _.switches.dumpSwitches(includeBlank=False)

# _.tables.register('childClassItems',childItems)
# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
# _.tables.print('childClassItems','name')

# backupLog = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )

# _mime.isText(file)
# _mime.isBinary(file)

# books = _.getText(_v.myTables + _v.slash+'bible_books.csv')
# _.saveText(convertedFile,'file.txt')

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')
# _.saveTable( jsonFile, 'file.json', printThis=True )

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START

def action():
	logConfigFile_tmp = 'logConfig.json'
	runOld = False

	if not runOld:
		# _.pr( 0 )
		if _.switches.isActive('Input'):
			if _.switches.isActive('Label'):
				label = _.switches.value('Label').replace( ',', ' ' )
			else:
				label = _.switches.value('Input').replace( '.json', '' ).replace( '_', ' ' )

			log = _.getTable( _.switches.value('Input') )

			if len(log) == 0:
				log = _.getTable2( _.switches.value('Input') )

			newLog = []
			if type( log ) == dict:
				newLog.append( log )
			else:
				newLog = [log[len(log)-1]]
				# for l in log:
				#     newLog.append( log )

			# _.pr( 1 )
			info = {
						'file': _.switches.value('Input'),
						'path': os.path.abspath( _.switches.value('Input') ),
						'label': label,
						'log': newLog
			}
			# _.pr( 2 )
			# _.pr( 'logConfigFile_tmp:',logConfigFile_tmp )
			# _.pr( type(info) )
			# _.pr( sys.getsizeof(info) )
			# _.pr( (info) )
			# _.printVar( info )
			_.saveTable( info, logConfigFile_tmp, tableTemp=True, printThis=False )
			
			infoTextRows = _.getText( _v.stmp + _v.slash + logConfigFile_tmp )

			infoTextBuild = 'configGen.data = '

			for line in infoTextRows:
				infoTextBuild += line

			infoTextBuild += ';'
			_.saveText( infoTextBuild, _v.log_config )
			# _.pr( 3 )
			_browser.imp.project.open( _v.log_config_html )
			# _browser.imp.project.inject( infoTextBuild )

			test = False
			_.pr( test )
			while not test:
				time.sleep( 1 )
				try:
					test = _browser.imp.project.injectReturn( 'configGen.talk.done' )
					how = 0
				except Exception as e:
					test = False
					how = 1
				_.pr( test, how )

			if test:
				configurationFile = _browser.imp.project.injectReturn( 'configGen.talk.saveData()' )
				_browser.imp.project.close()
				# generatedLogFile = _v.stmp + _v.slash+'generatedLogFile_' + _.genUUID() + '.json'
				_.printVar( configurationFile )
				# _.saveText( configurationFile, generatedLogFile )

				theLog = _.getTable('logConfig.json')
				found = False
				for i,record in enumerate(theLog):
					if record['file'] == configurationFile['file']:
						theLog[i] = configurationFile
						found = True
						_.pr( 'Record Updated' )
						break

				if not found:
					_.pr( 'Record Added' )
					theLog.append( configurationFile )
				_.saveTable( theLog, 'logConfig.json', printThis=True )
			
				# try:
				#     generatedLog = _.getTable2(generatedLogFile)
				#     os.remove(generatedLogFile)
				#     if len( generatedLog ) > 0:
				#         theLog = _.getTable('logConfig.json')
				#         theLog.append( generatedLog )
				#         _.saveTable( theLog, 'logConfig.json', printThis=True )
				# except Exception as e:
				#     _.pr( 'Error: unable to update log' )

	if runOld:
		if _.switches.isActive('Input'):
			if _.switches.isActive('Label'):
				label = _.switches.value('Label').replace( ',', ' ' )
			else:
				label = _.switches.value('Input').replace( '.json', '' ).replace( '_', ' ' )

			log = _.getTable( _.switches.value('Input') )
			if len(log) == 0:
				log = _.getTable2( _.switches.value('Input') )

			newLog = []
			if type( log ) == dict:
				newLog.append( log )
			else:
				for l in log:
					newLog.append( log )


			info = {
						'file': _.switches.value('Input'),
						'path': os.path.abspath( _.switches.value('Input') ),
						'label': label,
						'log': newLog
			}
			_.saveTable( info, logConfigFile_tmp, tableTemp=True, printThis=False )
			
			infoTextRows = _.getText( _v.stmp + _v.slash + logConfigFile_tmp )

			infoTextBuild = 'configGen.data = '

			for line in infoTextRows:
				infoTextBuild += line

			infoTextBuild += ';'

			_.saveText( infoTextBuild, _v.log_config )

			webbrowser.open( _v.log_config_html, new=2 )

			generatedLogFile = _v.stmp + _v.slash+'generatedLogFile_' + _.genUUID() + '.json'
			_.saveText( 'copy(configGen.talk.saveData())', generatedLogFile )
			do = 'start "EDIT" %n% ' + generatedLogFile
			os.system('"' + do + '"')
			pause = input('pause')
		
			try:
				generatedLog = _.getTable2(generatedLogFile)
				os.remove(generatedLogFile)
				if len( generatedLog ) > 0:
					theLog = _.getTable('logConfig.json')
					theLog.append( generatedLog )
					_.saveTable( theLog, 'logConfig.json', printThis=True )
			except Exception as e:
				pass




########################################################################################
if __name__ == '__main__':
	action()






