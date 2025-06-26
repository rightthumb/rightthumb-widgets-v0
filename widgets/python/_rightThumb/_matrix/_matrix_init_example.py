import os

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import sys
import time
##################################################
import _rightThumb._construct as __
import _rightThumb._matrix as _matrix
a, app, application = _matrix.theApp()
appDBA = _matrix.clearFocus( __name__, __file__ )
_matrix.appReg = appDBA
# _.pr( 'appDBA', appDBA )
app.focus( appDBA )
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = _matrix.appName( appDBA, parentApp, childApp )
	if reg:
		_matrix.appReg = f
	return f
_matrix.registeredApps.append( focus() )
import _rightThumb._base3 as _
import _rightThumb._base4 as ___
##################################################

program = {
	'file': 'thisApp.py',
	'liveAppName': _matrix.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
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
						'p thisApp -file file.txt',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}




def appSwitches():
	pass
	# app.load_switches = True
# _.autoBackupData = __.autoCreationConfiguration['backup']
# __.isRequired_Pipe = False
# __.isRequired_Pipe_or_File = False
focusID = None
def registration():
	# _.pr( 'matrix2 registration()' )
	global appDBA
	global program
	global focusID
	focusID = app.focus( appDBA ).register( program )
	appSwitches()
	app.load()
	if app.load_switches:
		_.myFileLocation_Print = False
		app.switch( 'Files' ).trigger( _.myFileLocations )
		app.switch( 'Folder' ).trigger( _.myFolderLocations )
		app.switch( 'URL' ).trigger( _.urlTrigger )
		
		app.defaultScriptTriggers()
	app.processSwitches()
	app.postLoad()

registration()


########################################################################################
# START

def action():
	load()
	if not app.data('stdin').stdin() is None:
		for i,row in enumerate( app.data('stdin').get() ):
			_.pr( row )

	data = app.ext( 'test', 'matrix2' ).action(unload=True,schedule=False,timeout=120)

def load():
	app.data( 'AnyDesk.json' ).set( ___.table.get( 'AnyDesk.json' ) )


if __name__ == '__main__':
	app.async( 'action', action, trigger=app.focus(appDBA).unregister )




