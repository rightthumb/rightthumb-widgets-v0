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
import _rightThumb._construct2 as __
a, app, application = __.theApp()
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
# _.pr( 'appDBA', appDBA )
app.focus( appDBA )
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
import _rightThumb._base4 as ___

##################################################


# _.pr( focus( parentApp='parent' ) )
# _.pr( app.base(   focus( parentApp='parent' )   ) )
# sys.exit()



focusID = app.focus( appDBA ).register({
									'file': 'thisApp.py',
									'liveAppName': __.thisApp( __file__ ),
									'description': 'Changes the world',
									'categories': [
														'DEFAULT',
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

	})


def appSwitches():
	pass

	# app.switch( 'Input', '-i' )
	app.switch( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	

	
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )






def registerSwitches():
	global appDBA
	app.data( 'Pipe', focus='live' ).pipe()
	# app.data( 'Pipe', focus=appDBA ).pipe()
	__.load()

	appSwitches()

	_.myFileLocation_Print = False
	app.switch( 'Files' ).trigger( _.myFileLocations )
	app.switch( 'Folder' ).trigger( _.myFolderLocations )
	app.switch( 'URL' ).trigger( _.urlTrigger )
	

	
	app.defaultScriptTriggers()
	app.processSwitches()



registerSwitches()

# app.switches().dump()
# sys.exit()

def test():
	i=0
	while i < 100:
		pass 
	_.pr( 'ran' )

def handler( arg1='E1', arg2='E2' ):
	i=0
	# asdf
	while True:
		_.pr( i, arg1, arg2 )
		i+=1
		time.sleep(.5)


# app.async( 'test', {'script': handler, 'name': 'a', 'timeout': 1, 'kwargs': { 'arg1': 'a', 'arg2': 'b',  } } )
# app.async( 'test', {'script': handler, 'name': 'b', 'timeout': 1, 'kwargs': ['1'] } )
# app.async( 'test', {'script': handler, 'name': 'c', 'timeout': 1, 'kwargs': ('2') } )

def change(data):
	return '|'+str(data)+'|'

def callersname( i=0 ):
	callers = []
	i=0
	error=False
	while not error:
		try:
			callers.append(sys._getframe(i).f_code.co_name)
		except Exception as e:
			error=True
		i+=1

	return callers

def one(i):
	return callersname( i )
def two(i):
	return one( i )
def three(i):
	return two( i )
def four(i):
	return three( i )
def five(i):
	return four( i )

def fn(i):
	fn.f += i
	return fn.f

# sys.getfilesystemencoding()

def action():
	# _.pr( sys._getframe().f_code.co_name, dir(sys._getframe()) )
	
	# _.pr( five(0) )
	# sys._getframe(  ).f_code.co_filename

	# fn.f = 1
	# _.pr( fn.f )
	# _.pr( fn.f )

	# sys.exit()
	global appDBA
	
	# sys._getframe().f_code.co_name

	app.data( 'AnyDesk.json' ).set( ___.table.get( 'AnyDesk.json' ) )
	# _.pr( app.data( 'AnyDesk.json' ).get() )
	_.printVarSimple( app.data( 'AnyDesk.json' ).get() )


	# app.switch( 'Files', { 'name': 'Files', 'switches': '-f,-files', 'focus': __.appReg } )


	x = app.switch( 'Files' ).about()
	_.printVarSimple( x )

	# _.pr( "a.ir()", a.ir() )
	# _.pr( 'Files', a.s('Files').a() )

	if a.ir() and a.s('Files').a() and a.s('Files').l() and not app.switch('Files').inVal('one') and a.ps('thisProcess', 'Files and One', i=1 ):
		_.pr( 'Missing one' )
	if a.ir() and a.s('Files').a() and a.s('Files').l() and app.switch('Files').inVal('one') and a.ps('thisProcess', 'Files and One', i=1 ):
		_.pr( 'Works' )

	if a.ir() and a.s('Files').a() and not a.s('Files').l() and a.ps('thisProcess', 'Files and One', i=1 ):
		_.pr( 'No Switch Values' )
	if a.ir() and not a.s('Files').a() and a.ps('thisProcess', 'Files and One', i=1 ):
		_.pr( 'Missing Files Switch' )

	testVar = {}

	if a.ir() and a.s('Files').a() and a.docIF( 'test' in testVar.keys(), 'hasKey', 'test in testVar' ):
		a.ps('Files and test', 'docIF test', i=1 )
		_.pr( 'docIF True' )
	else:
		a.ps('Files and test', 'docIF test', i=1 )
		_.pr( 'docIF False' )
	
	pass
	# temp = app.ext( 'test', 'struct2_test5' )
	# app.ext( 'test' ).imp.action()
	# temp = app.ext( 'test', 'struct2_test5' ).schedule()
	# _.pr('NEW HERE',__.genUUID())
	# _.pr('HERE')
	# app.viewLog()
	
	# data = app.id( temp ).singleGetWait()
	# _.pr( '**********', data )

	app.switch('Files').call()


	_.colorThis( ['                                                    ******************  THIS APP IS DONE  ****************** '] )
	


# epyi construct2 -file _switch_child
# epyi construct2 -file _async_child
# epyi construct2 -file _process_child
# epyi construct2 -file _focus_child
# epyi construct2 -file _data_child
# epyi construct2 -file _ext_child
# epy genBase4Sections


	# test()

	# test = ___.table.get( 'appRegistration.json' )


if __name__ == '__main__':
	app.async( 'action', action, trigger=app.focus(appDBA).unregister )



# sys._getframe().f_code.co_name



