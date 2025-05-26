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

# _.pr('*** it loaded ***')
import os
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





focusID = app.focus( appDBA ).register({
									'file': 'struct2_test4.py',
									'liveAppName': _matrix.thisApp( __file__ ),
									'description': 'Test app for import',
									'categories': [
														'test',
														'import',
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
														'pp struct2_test4 -file file.txt',
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

	})


def appSwitches():
	pass

	app.switch( 'Input', '-i' )
	# app.switch( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	





def registerSwitches():
	app.data( 'Pipe', focus='live' ).pipe()
	# app.data( 'Pipe', focus=appDBA ).pipe()
	_matrix.load()

	appSwitches()

	_.myFileLocation_Print = False
	app.switch( 'Files' ).trigger( _.myFileLocations )
	app.switch( 'Folder' ).trigger( _.myFolderLocations )
	app.switch( 'URL' ).trigger( _.urlTrigger )
	

	
	app.defaultScriptTriggers()
	app.processSwitches()



registerSwitches()



def action():
	app.data( 'data in struct2_test5' ).set( ___.table.get( 'AnyDesk.json' ) )
	_.colorThis( '\n\n\n\n                                                                        success' )
	_.colorThis( ' This thing Works ', 'green' )
	_.colorThis( ' This thing Works ', 'red' )
	_.colorThis( ' This thing Works ', 'yellow' )
	_.colorThis( '                                                                        success\n\n\n\n' )
	return 12345012345012345012345012345012345012345012345012345012345012345012345012345012345012345012345012345



if __name__ == '__main__':
	app.asyn( 'action', action, trigger=app.focus(appDBA).unregister )




