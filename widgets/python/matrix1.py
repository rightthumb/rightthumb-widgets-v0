#!/usr/bin/python3
import os
import sys
import time
##################################################
import _rightThumb._construct as __
import _rightThumb._matrix as _matrix
a, app, application = _matrix.theApp()
appDBA = _matrix.clearFocus( __name__, __file__ )
_matrix.appReg = appDBA
# print( 'appDBA', appDBA )
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

	'file': 'matrix1.py',
	'liveAppName': _matrix.thisApp( __file__ ),
 	'description': 'matrix test 1',
	
	'categories': [
						'matrix',
						'test',
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
						'p matrix1',
						'p matrix1 -file',
						'p matrix1 -file two',
						'',
						['p matrix1 -file one two', 'red'],
						'',
	],
	'columns': [
					   { 'name': 'name', 'abbreviation': 'n' },
					   # { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					   # 'this',
					   # 'app',
	],

}



def appSwitches():
	pass
	# print('appSwitches')
	app.switch( 'Memory', '-m,-mem,-memory' )
	app.switch( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	

	

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
		app.defaultScriptTriggers()
	
	app.processSwitches()
	app.postLoad()

registration()

# app.switches().dump()
# sys.exit()

def test():
	i=0
	while i < 100:
		pass 
	print( 'ran' )

def handler( arg1='E1', arg2='E2' ):
	i=0
	# asdf
	while True:
		print( i, arg1, arg2 )
		i+=1
		time.sleep(.5)


# app.asyn( 'test', {'script': handler, 'name': 'a', 'timeout': 1, 'kwargs': { 'arg1': 'a', 'arg2': 'b',  } } )
# app.asyn( 'test', {'script': handler, 'name': 'b', 'timeout': 1, 'kwargs': ['1'] } )
# app.asyn( 'test', {'script': handler, 'name': 'c', 'timeout': 1, 'kwargs': ('2') } )

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
# print( 'mem', app.switch('Memory').isActive() )
if app.switch('Memory').isActive():
	_matrix.memoryPrint = True
	print( '_matrix.memoryPrint = True' )
# def x():
# x()
def action():

	# print( a.c(r=1) )
	# print( a.c(isChild=True) )
	# sys.exit()
	# print( sys._getframe().f_code.co_name, dir(sys._getframe()) )
	
	# print( five(0) )
	# sys._getframe(  ).f_code.co_filename

	# fn.f = 1
	# print( fn.f )
	# print( fn.f )

	# sys.exit()
	global appDBA
	
	# sys._getframe().f_code.co_name

	app.data( 'AnyDesk.json' ).set( ___.table.get( 'AnyDesk.json' ) )
	# print( app.data( 'AnyDesk.json' ).get() )
	# _.printVarSimple( app.data( 'AnyDesk.json' ).get() )


	# app.switch( 'Files', { 'name': 'Files', 'switches': '-f,-files', 'focus': _matrix.appReg } )


	x = app.switch( 'Files' ).about()
	# _.printVarSimple( x )

	# print( "a.ir()", a.ir() )
	# print( 'Files', a.s('Files').a() )

	if a.ir() and a.s('Files').a() and a.s('Files').l() and not app.switch('Files').inVal('one') and a.ps('thisProcess', 'Files and One', i=1 ):
		print( 'Missing one' )
	if a.ir() and a.s('Files').a() and a.s('Files').l() and app.switch('Files').inVal('one') and a.ps('thisProcess', 'Files and One', i=1 ):
		print( 'Works' )

	if a.ir() and a.s('Files').a() and not a.s('Files').l() and a.ps('thisProcess', 'Files and One', i=1 ):
		print( 'No Switch Values' )
	if a.ir() and not a.s('Files').a() and a.ps('thisProcess', 'Files and One', i=1 ):
		print( 'Missing Files Switch' )

	testVar = {}
	if a.ir() and a.s('Files').a() and a.docIF( 'test' in testVar.keys(), 'hasKey', 'test in testVar' ):
		a.ps('Files and test', 'docIF test', i=1 )
		print( 'docIF True' )
	else:
		a.ps('Files and test', 'docIF test', i=1 )
		print( 'docIF False' )
	
	pass
	# print( ' i am here ' )
	# temp = app.ext( 'test', 'struct2_test5' , trackingID=123 )
	# temp = app.ext( 'test', 'struct2_test5' ).imp.action()
	# app.ext( 'test' ).imp.action()
	# temp = app.ext( 'test', 'struct2_test5' ).schedule(unload=True)
	# data = app.id( temp ).singleGetWait()
	# temp = app.ext( 'test', 'struct2_test5' ).schedule()
	# print('NEW HERE',_matrix.genUUID())
	# print('HERE')
	# app.viewLog()
	# data = app.ext( 'test', 'struct2_test5' ).action()
	data = app.ext( 'test', 'matrix2' ).action(unload=True,schedule=False,timeout=120)
	print( '**********', data )
	# print( '**********', data )
	# app.switch('Files').callers()

	# print( a.c(isChild=True) )

	_.colorThis( ['                                                    ******************  THIS APP IS DONE  ****************** '] )
	_.colorThis( [ appDBA, '_matrix.app.memory_max', _.formatSize(_matrix.app.memory_max) ], 'yellow' )
	# app.totalMemory()
	# print(list( app.records['switch'].keys() ))
	# _.printVarSimple( list( app.records['switch'].keys() ) )



# epyi matrix -file _async_child
# epyi matrix -file _audit_child
# epyi matrix -file _data_child
# epyi matrix -file _db_child
# epyi matrix -file _ext_child
# epyi matrix -file _focus_child
# epyi matrix -file _procedure_child
# epyi matrix -file _process_child
# epyi matrix -file _reg_child
# epyi matrix -file _switch_child
# epyi matrix -file _table_child
# epyi matrix -file _task_child


# epy genBase4Sections

# p file + _child --c | p line --c -make " n {} "

	# test()

	# test = ___.table.get( 'appRegistration.json' )


if __name__ == '__main__':
	app.asyn( 'action', action, trigger=app.focus(appDBA).unregister )



# sys._getframe().f_code.co_name

