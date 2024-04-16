import os
import sys
import time
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
import _rightThumb._vars as _v
import _rightThumb._string as _str
import glob

def appSwitches():
	_.switches.register('Recursive', '-r,-recursive')
	_.switches.register('JustName', '-jn,-justname')

_.appInfo[focus()] = {
	'file': 'hasAlias.py',
	'description': 'check if a folder has any bookmarks (bm)',
	'categories': [
						'research',
						'text manipulation',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [
						'p hasAlias',
	],
	'columns': [],
	}
_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

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
#n)--> start

def action():
	_.pr()
	bm = _bm.Bookmarks()
	bm.reverse()
	_.pr()
	_.pr()
	return False
	data = []
	find = _v.sanitizeFolder( os.getcwd() )
	dirList = os.listdir( _v.myBookmarks )
	for i,item in enumerate( dirList ):
		path = _v.myBookmarks + _v.slash + item
		if os.path.isfile( path ):
			if 'BM-' in item and '.txt' in item:
				alias = item.replace( 'BM-', '' ).replace( '.txt', '' )
				try:
					file0 = _.getText( path )
					file = file0[0]
					file = file.replace( '\n', '' )
					if _.switches.isActive( 'Recursive' ):
						if find + _v.slash == file or find == file or find + _v.slash in file:
							data.append({ 'alias': alias, 'folder': _v.resolveFolderIDs(file) })
					else:
						if find + _v.slash == file or find == file:
							_.pr( alias )
				except Exception as e:
					pass
	if _.switches.isActive( 'Recursive' ):
		if not _.switches.isActive( 'JustName' ):
			_.switches.fieldSet( 'Long', 'active', True )
			_.switches.fieldSet( 'GroupBy', 'active', True )
			_.switches.fieldSet( 'GroupBy', 'value', 'folder' )
			_.tables.register( 'data', data )
			_.tables.print( 'data', 'folder,alias' )
			_.pr()
			_.pr( len(data) )
		else:
			for x in data:
				_.pr( x['alias'] )

import _rightThumb._bookmarks as _bm

########################################################################################
if __name__ == '__main__':
	action()