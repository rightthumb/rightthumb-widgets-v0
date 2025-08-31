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

}


def appSwitches():
	pass
	### EXAMPLE: START
	# app.load_switches = True
	# app.switch( 'Memory', '-m,-mem,-memory' )
	# app.switch( 'Memory', '-m,-mem,-memory', isRequired=True )
	# app.switch( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# app.switch( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', isRequired=True, description='Files' )
	### EXAMPLE: END

# _.autoBackupData = __.autoCreationConfiguration['backup']
# __.isRequired_Pipe = False
# __.isRequired_Pipe_or_File = False
focusID = None
def registration():
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
		app.switch( 'Ago' ).trigger( _.timeAgo )
		app.switch( 'Duration' ).trigger( _.timeFuture )
		app.defaultScriptTriggers()
	
	app.processSwitches()
	app.postLoad()

def end():
	app.async( 'action', action, trigger=app.focus(appDBA).unregister )

registration()

########################################################################################
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# date = _.friendlyDate( theDate )
# _.addComma()
# ####
# _async_child
# _audit_child
# _data_child
# _db_child
# _ext_child
# _focus_child
# _procedure_child
# _process_child
# _reg_child
# _switch_child
# _table_child
# _task_child
# p inFunc -f D:\tech\programs\python\src\windows\_rightThumb\_matrix\_switch_child.py
# ####
### EXAMPLE: END
########################################################################################
# START



def action():
	# should be   single task   OR   imply architecture and execute functions
	load()
	if not app.data('stdin').stdin() is None:
		for i,row in enumerate( app.data('stdin').get() ):
			pass
	

def load():
	app.data( 'AnyDesk.json' ).set( ___.table.get( 'AnyDesk.json' ) )


if __name__ == '__main__':
	end()






