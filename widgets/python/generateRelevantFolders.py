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
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
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

##################################################


def appSwitches():
	pass
	_.switches.register('Print', '-print')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'generateRelevantFolders.py',
	'description': 'generate relevant folders for apps',
	'categories': [
						'app'
						'default'
						'tool'
						'setup'
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
						'p generateRelevantFolders',
						'',
						'p generaterelevantfolders -print +  py unity src  - pycache',
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
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
########################################################################################
# START

def searchFolder( folder ):
	global data
	global omit
	global cnt
	for o in omit.split(','):
		if o in folder:
			return False
	# _.pr('here',folder)
	if os.path.isdir( folder ):
		if not folder in data:
			# _.pr( folder )
			pp = os.path.abspath( folder )
			if _.switches.isActive('Print'):
				if _.showLine(pp):
					_.pr(pp)
					cnt+=1
			data.append( pp )
			for file in os.listdir(folder):
					try:
						searchFolder( folder + _v.slash + file )
					except Exception as e:
						pass


def action():
	global profile
	global folders
	global data
	global cnt

	if os.path.isfile(_v.relevant_folders):
		# _.pr( 'Deleted' )
		os.unlink(_v.relevant_folders)
	# _.pr( 'Scanning' )
	for part in profile.split(','):
		searchFolder( _v.userprofile + _v.slash + part )

	spent = []
	for folder in folders:
		if not folder in spent:
			spent.append(folder)
			searchFolder( folder )

	_.saveText( data, _v.relevant_folders )
	_.pr()
	_.colorThis( _v.relevant_folders, 'blue' )
	_.pr()
	_.colorThis( [ '', _.addComma(len(data)), 'folders'  ], 'green' )
	if _.switches.isActive('Print'):
		if not cnt == len(data):
			_.colorThis( [ '  ', cnt, 'found' ], 'yellow' )

	# _.pr( 'Done' )

omit = 'Lasalle,S_Archive,Projects,wp-content,wp-includes,FileZilla,httpdocs,images,ckeditor,HuMo-gen,cross-connect-master,iTunes,tech\\srv,pyFileFixity'
profile = 'Desktop,Documents,Downloads,Music,OneDrive,Pictures,SkyDrive,Videos'
folders = [
				_v.techFolder,
				'D:\\_Scott',
]
data = []
cnt=0


########################################################################################
if __name__ == '__main__':
	action()

# generateRelevantFolders





