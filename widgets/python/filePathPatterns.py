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
##################################################
# from lxml import html
# import requests
# import cssselect
# import sqlite3
##################################################

def appSwitches():
	pass
	# _.switches.register('Input', '-i,-input','file.txt')
	_.switches.register('Files', '-f,-file,-files','file.txt')
	_.switches.register('NotSorted', '-notsorted')
	_.switches.register('Unique', '-u,-unique',' use this switch ')
	_.switches.register('LastFolder', '-last,-lastfolder')
	_.switches.register('Validate', '-v,-validate')
	_.switches.register('Report', '-r,-report')
	_.switches.register('NoPrint', '-noprint')
	_.switches.register('JustReturn', '-justreturn')
_.autoBackupData = True

_.appInfo[focus()] = {
	'file': 'filePathPatterns.py',
	'appLive': __.thisApp( __file__ ),
	'description': 'Identifies patterns in file paths',
	'categories': [
						'tool',
						'file',
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
						'p files --c | p filePathPatterns -u',
						'p files --c | p filePathPatterns -last',
						'p filePathPatterns -f %tmpf0% -r 0',
						'p filePathPatterns -f %tmpf0% -r 35',
						'',
						'',
						'p dirDB + netflix --c | p filePathPatterns -r',
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
# _.appInfo[focus()]['examples'].append('p filePathPatterns -file file.txt')
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
_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )
_.postLoad( __file__ )

########################################################################################
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# if os.path.isfile(item):

########################################################################################
# START

def collectFolders( data ):
	global allFolders
	for folder in data:
		if not folder in allFolders:
			allFolders.append( folder )

def fileInfo( path ):
	folderList = []
	parts = path.split( _v.slash )
	file = parts.pop()
	folder = _v.slash.join( parts )
	folderList.append( folder )
	pTemp = parts
	last = ''
	for i,x in enumerate(parts):
		if len( pTemp ):
			pFolder = pTemp.pop()
			folderList.append( _v.slash.join( pTemp ) )
			if i == 0:
				last = pFolder
	# last = parts[len(parts)-1]
	collectFolders( folderList )
	info = {
				'path' : path,
				'isfile' : os.path.isfile(path),
				'file' : file,
				'folder' : folder,
				'parts' : parts,
				'last' : last,
				'folderList' : folderList,
	}
	return info

def folderInfo( folder ):
	folderList = []
	parts = folder.split( _v.slash )
	folderList.append( folder )
	pTemp = parts
	last = ''
	for i in range(0,len(parts)):
		if len( pTemp ) > 1:
			pFolder = pTemp.pop()
			folderList.append( _v.slash.join( pTemp ) )
			if i == 0:
				last = pFolder
	# last = parts[len(parts)-1]
	collectFolders( folderList )
	info = {
				'folder' : folder,
				'parts' : folder.split( _v.slash ),
				'last' : last,
				'folderList' : folderList,
	}
	return info

def theFolder( path ):
	folderParts = path.split( _v.slash )
	file = folderParts.pop()
	folder = _v.slash.join( folderParts )
	return folder

def lastFolderOne( path ):
	folderPath = theFolder( path )
	folderParts = folderPath.split( _v.slash )
	folderParts.reverse()
	return folderParts[0]

def uniqueData(setPipe=True):
	data = []
	for path in _.appData[__.appReg]['pipe']:
		folder = theFolder( path )
		if not folder in data:
			data.append( folder )
	if setPipe:
		_.appData[__.appReg]['pipe'] = data
	else:
		return data

def lastFolderAll():
	data = []
	for path in _.appData[__.appReg]['pipe']:
		folder = lastFolderOne( path )
		if not folder in data:
			data.append( folder )
	_.appData[__.appReg]['pipe'] = data

def folderReport():
	global allFolders
	global totalThreshold
	folderData = []
	for i,folder in enumerate(uniqueData( False )):
		if i == 0 and False:
			if _.switches.isActive('JustReturn'):
				return folderInfo(folder)
			_.pr( _.switches.isActive('JustReturn') )
			_.printVar( folderInfo(folder) )
			sys.exit()
		folderData.append( folderInfo(folder) )
	allFoldersData = {}
	for folder in allFolders:
		allFoldersData[folder] = { 'omit': False, 'percent': 0, 'total': 0, 'isCount': 0, 'hasCount': 0, 'level': folder.count(_v.slash), 'folder': folder, 'info': folderInfo(folder) }
	for path in _.appData[__.appReg]['pipe']:
		folder = theFolder( path )
		longest = 0
		for aFolder in allFolders:
			if aFolder.lower() == folder.lower():
				allFoldersData[aFolder]['isCount']+=1
			elif aFolder in folder:
				allFoldersData[aFolder]['hasCount']+=1
	total = len(_.appData[__.appReg]['pipe'])
	patternX = {}
	for folder in allFoldersData.keys():
		allFoldersData[folder]['count'] = allFoldersData[folder]['hasCount'] + allFoldersData[folder]['isCount']
		allFoldersData[folder]['percent'] = _.percentageDiffInt( allFoldersData[folder]['hasCount'], total )
		allFoldersData[folder]['total'] = _.percentageDiffInt( allFoldersData[folder]['count'], total )
		patternX[allFoldersData[folder]['total']] = []
	for folder in allFoldersData.keys():
		patternX[allFoldersData[folder]['total']].append( allFoldersData[folder] )
	for folder in allFoldersData.keys():
		omit = []
		for record in patternX[ allFoldersData[folder]['total'] ]:
			for i,fld in enumerate( record['info']['folderList'] ):
				if not i == 0:
					omit.append( fld )
		for record in patternX[ allFoldersData[folder]['total'] ]:
			if record['folder'] in omit:
				allFoldersData[ record['folder'] ]['omit'] = True
	report = []
	if len( _.switches.value( 'Report' ) ):
		try:
			totalThreshold = int( _.switches.value( 'Report' ) )
		except Exception as e:
			pass
	for folder in allFoldersData.keys():
		if not allFoldersData[folder]['omit'] and allFoldersData[folder]['total'] > totalThreshold:
			report.append( allFoldersData[folder] )
	if not _.switches.isActive( 'NoPrint' ):
		_.switches.fieldSet( 'Long', 'active', True )
		_.tables.register( 'data', report )
		_.tables.print( 'data', 'total,percent,count,isCount,hasCount,level,folder' )
		_.pr()
		_.pr( 'total:', _.addComma(total) )
	return report

def folderReportNew():
	global allFolders
	allFolders = []
	isCount = []
	hasCount = []
	for path in _.appData[__.appReg]['pipe']:
		folder = theFolder( path )
		if not folder in allFolders:
			isCount.append( 1 )
			allFolders.append( folder )
		else:
			isCount[ allFolders.index( folder ) ] += 1

def action():
	load()
	_v.slash
	data = '\n'.join( _.appData[__.appReg]['pipe'] )
	f = data.count('\\')
	b = data.count('/')
	if f > b:
		_v.slash = '\\'
	else:
		_v.slash = '/'

	# _.pr( _v.slash ); _.isExit(__file__)
	# _.pr( _.appData[__.appReg]['pipe'] )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		if not _.setPipeDataRan:
			_.pipeCleaner(1)
		# _.printVar(_.appData)
		# _.switches.dumpSwitches(includeBlank=False)
		if _.switches.isActive( 'JustReturn' ):
			_.switches.fieldSet( 'NoPrint', 'active', True )
			_.appData[__.appReg]['pipe'] = sorted(_.appData[__.appReg]['pipe'], key=lambda v: (v.upper(), v[0].islower()))
			return folderReport()
		if _.switches.isActive( 'NotSorted' ):
			_.appData[__.appReg]['pipe'] = sorted(_.appData[__.appReg]['pipe'], key=lambda v: (v.upper(), v[0].islower()))
		# _.pr( 'HERE' )
		if _.switches.isActive( 'Report' ):
			_.pr( 'X HERE X' )
			return folderReport()
		if _.switches.isActive( 'Unique' ):
			uniqueData()
		if _.switches.isActive( 'LastFolder' ):
			lastFolderAll()
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			# sys.exit()
			shouldPrint = True
			if _.switches.isActive( 'Validate' ):
				if not os.path.isdir(row):
					shouldPrint = False
			if shouldPrint:
				_.pr( row )

def load():
	if _.switches.isActive('Files'):
		tmpFiles = []
		hasFiles = False
		for file in _.switches.values('Files'):
			if os.path.isfile( file ):
				hasFiles = True
				for row in _.getText( file, raw=True, clean=2 ).split('\n'):
					tmpFiles.append( row )
		if hasFiles:
			_.setPipeData( tmpFiles, __.appReg )
		if not hasFiles:
			if type( _.appData[__.appReg]['pipe'] ) == bool:
				_.appData[__.appReg]['pipe'] = []
				for row in _.switches.value('Files').split( ',' ):
					_.appData[__.appReg]['pipe'].append( row )
allFolders = []
totalThreshold = 50

########################################################################################
if __name__ == '__main__':
	action()