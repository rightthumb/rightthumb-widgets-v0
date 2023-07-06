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
	# _blowfish.genPassword()
	# _blowfish.genPassword('string')
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
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
	

_.autoBackupData = True


_.appInfo[focus()] = {
	'file': 'dnd_CSS_Profile.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Find patterns in ',
	'categories': [
						'dnd',
						'd&d',
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
						'b dnd',
						'p dnd_CSS_Profile -f p1dkrl57o41hii1lot19p5sn9pte4-html.html',
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
########################################################################################
# START

def cleanText( row ):
	row = row.replace( '\t', '' )
	row = _str.replaceDuplicate( row, ' ' )
	row = _str.cleanBE( row, ' ' )
	return row

def profileCSS( row ):
	global data
	css = []
	one = row.split( '{' )
	name = one[0]
	cssItem = one[1].split( '}' )[0]
	cssX = cssItem.split( ';' )

	for x in cssX:
		if len( x ):
			css.append( x+';' )
	return { 'name': name, 'css': css, 'flat': ''.join( css ) }



def action():
	global data
	load()

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner()
		# _.printVar(_.appData)
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			if row.startswith( '.' ) and '{' in row:
				record = profileCSS( row )
				data.append( record )
				# _.pr( record )

		records = []
		for i,record in enumerate(data):
			if data[i]['flat'] in records:
				data[i]['group'] = records.index( data[i]['flat'] )
			else:
				data[i]['group'] = len( records )
				records.append( data[i]['flat'] )

		pass
		count = {}
		printed = {}
		for i,record in enumerate(data):
			try:
				count[record['group']] += 1
			except Exception as e:
				count[record['group']] = 1
				printed[record['group']] = False


			
		report = []
		iX = 1
		for i,record in enumerate(data):
			if count[record['group']] > 0:
				report.append( record )

				if not printed[record['group']]:
					printed[record['group']] = True
					_.pr( iX, record['group'],'\t', count[record['group']],'\t', record['css'][0] )
					iX += 1

		_.pr( 'Data Len:', len( data ) )
		# _.saveTable( data, 'dnd_CSS_Profile.json' )
		# _.switches.fieldSet( 'Long', 'active', True )
		# _.switches.fieldSet( 'GroupBy', 'active', True )
		# _.switches.fieldSet( 'GroupBy', 'active', 'group' )
		# logCheck = _.tables.returnSorted( 'data', 'a.group', report )
		# _.tables.print( 'data', 'group,name,flat' )




def load():
	# global data
	# data = _.getTable( 'table.json' )

	# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[focus()]['liveAppName'], 'project': 'app_instance' }

	if _.switches.isActive('Files'):
		tmpFiles = []
		hasFiles = False
		for file in _.switches.values('Files'):
			if os.path.isfile( file ):
				hasFiles = True
				for row in _.getText( file, raw=True, clean=2 ).split('\n'):
					tmpFiles.append( row )
		if hasFiles:
			_.setPipeData( tmpFiles, focus() )
		if not hasFiles:
			if type( _.appData[__.appReg]['pipe'] ) == bool:
				_.appData[__.appReg]['pipe'] = []
				for row in _.switches.value('Files').split( ',' ):
					_.appData[__.appReg]['pipe'].append( row )

data = []
groupID = 0
########################################################################################
if __name__ == '__main__':
	action()




# div#page23-div
#     p.ft245    font-size:28px;    Class Features
#         p.ft244    font-size:16px;    Hit Points
#             p.ft246    font-size:11px;    <b>Hit Dice:</b> 1d8 per cleric level
#                 p.ft243    font-size:11px;    Constitution modifier per cleric level after 1st
#     p.ft248    font-size:16px;    Creating a Cleric ( Underlined )
#     p.ft231    font-size:13px;    Chapter 3: Classes ( bottom of page )
	





# hackData = []
# $('.p li').each(function(){
#     hackData.push( $(this).text() );
# });
# copy( hackData )









