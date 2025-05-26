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
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
##################################################
import glob
import shutil
# from lxml import html
# import requests
# import cssselect
# import sqlite3
##################################################


def appSwitches():
	_.switches.register('Recursive', '-r,-recursive')
	_.switches.register('JustName', '-jn,-justname')
	



_.appInfo[focus()] = {
	'file': 'cleanBookmarks.py',
	'description': 'clean bookmarks',
	'categories': [
						'research',
						'text manipulation',
				],
	'relatedapps': [
						'create bookmark to current folder',
						'    p m -a test',
						'list all bookmarks',
						'    p bookmarks',
						'quick generate bookmarks if blank',
						'   p bm-dirty | bash',
						'remove all bookmarks that no longer exist',
						'    p clean-bm -good -save',
						'bookmark location',
						'    p b -a ww',
						# '',
						# 'old not sure what it does',
						# '    p cleanBookmarks -?',
						# '',
	],
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

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

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

def action():
	data = []
	find = _v.sanitizeFolder( os.getcwd() )
	dirList = os.listdir( _v.myBookmarks )
	for i,item in enumerate( dirList ):
		path = _v.myBookmarks + _v.slash + item
		bad = _v.myBookmarks + _v.slash+'bad'+_v.slash + item
		if os.path.isfile( path ):
			if 'BM-' in item and '.txt' in item:
				alias = item.replace( 'BM-', '' ).replace( '.txt', '' )
				try:
					file0 = _.getText( path )
					file = file0[0]
					file = file.replace( '\n', '' )
					# _.pr( file )
					location = _v.resolveFolderIDs(file)


					if not os.path.isdir( location ):
						_.pr( 'BAD:\t', location )
						shutil.move( path, bad )
						# if _.switches.isActive( 'Delete' ):
							# os.remove( path )
					# else:
					#     p = _v.sanitizeFolder( location )

					#     if not file == p:
					#         _.saveText( p, b )

				except Exception as e:
					pass
					# shutil.move( path, bad )



########################################################################################
if __name__ == '__main__':
	action()





