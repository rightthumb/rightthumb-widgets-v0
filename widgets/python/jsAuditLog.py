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
# import _rightThumb._encryptString as _blowfish
_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog


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
	_.switches.register('File', '-i,-f,-file','file.txt')
	_.switches.register('Cache', '-cache', 'jsAuditLog.cache' )
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'jsAuditLog.py',
	'description': 'Aquire and process audit log of web dev project',
	'categories': [
						'audit',
						'javascript',
						'tool',
						'dev',
						'development',
				],
	'relatedapps': [],
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
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('type %tmpf0% | p changeTextEnd + ;. "function(" -text  ";n;t;tfamily.v.tracker.push({\'action\';.\'change\',\'function\';.\'*_*\',\'timestamp\';.(new Date).getTime(),\'id\';.family.talk.thisTable});" -payload ;. 0 nsif -add ')
_.appInfo[focus()]['examples'].append('echo shared.js | p changeTextEnd + ;. "function(" -text  ";n;t;tfamily.v.tracker.push({\'action\';.\'change\',\'function\';.\'*_*\',\'timestamp\';.(new Date).getTime()});" -payload ;. 0 nsif -add')
_.appInfo[focus()]['examples'].append('')

_.appInfo[focus()]['relatedapps'].append('p changeTextEnd (see comment at bottom of this app) ')
_.appInfo[focus()]['relatedapps'].append('p auditJavascript')
_.appInfo[focus()]['examples'].append('p jsAuditLog')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p jsAuditLog -f index.htm')
_.appInfo[focus()]['examples'].append('p jsAuditLog -cache')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('type %tmpf0% | p line -p [ 0 | p countEach')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p jsAuditLog -cache | + generateCode.js   |   p line -p [ 0 | p countEach')
_.appInfo[focus()]['examples'].append('')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})


# _.printVar( _.appInfo[focus()] )
# sys.exit()


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

def quickTrigger( data ):
	global name_resolution

	for row in name_resolution:
		if row['registration'] == data:
			return row['description']
	return data

def quickTriggerMem( data ):
	result = '0'
	try:
		result = str(sys.getsizeof( str(data) ))
	except Exception as e:
		result = '0'
	result = result.replace( ' ', '' )
	result = result.replace( '\t', '' )
	return result


def printTable():
	global data
	nData = []
	for x in data:
		if _.showLine(str(x)):
			nData.append(x)
	data = nData

	_.tables.register( 'data', data )
	# try:
		
	# except Exception as e:
	#     pass
	_.tables.fieldProfileSet( 'data', 'id', 'trigger', quickTrigger )
	_.tables.fieldProfileSet( 'data', 'm', 'trigger', quickTriggerMem )
	fields = []
	for x in 'function,id,d,m,a,h,action'.split(','):
		if x in list(data[0].keys()):
			fields.append(x)
	_.tables.print( 'data', ','.join(fields) )

	_.pr()
	_.pr( len(data) )
	_.pr()



# family.v.tracker.push({'action':'change','function':'isProject[shared.js ](519)','timestamp':(new Date).getTime()});

def action():
	global data
	_.switches.fieldSet( 'Long', 'active', True )


	if _.switches.isActive('Cache'):
		if not len(_.switches.value('Cache')):
			cache = 'jsAuditLog.cache'
		else:
			cache = _.switches.values('Cache')[0]
		data = _.getTable2(cache)
		printTable()
		sys.exit()

	# f = _.switches.values('File')[0]
	# p = os.path.abspath(f)
	# # x = os.path.normpath( p )
	# x = path2url( p )
	# _.pr( x )

	# sys.exit()

	global name_resolution
	if _.switches.isActive('File'):
		_.setClip( """family.v.tracker.push({'action':'**********','function':'NOTE_HERE','timestamp':(new Date).getTime()});""" )
		_browser.imp.project.open( _.path2url(_.switches.values('File')[0]) )
	else:
		_browser.imp.project.open( 'file:///D:/_Scott/S_Documents/Sites/RightThumb/projects/john/index.htm' )
	# _browser.imp.project.open( 'https://tpn.rephrecruiting.com/' )
	# _browser.imp.project.open( 'http://rightthumb.com/projects/john/' )
	pause = input( 'pause' )
	# data =_browser.imp.project.injectReturn( 'family.v.auditOverflow' )
	data =_browser.imp.project.injectReturn( 'family.v.tracker' )
	_.saveTable2( data, 'jsAuditLog.cache' )
	_.colorPrint(  [ '', 'cache: jsAuditLog.cache' ]  , 'yellow' )
	name_resolution =_browser.imp.project.injectReturn( 'family.talk.adherence.r_ids()' )
	printTable()

	# data =_browser.imp.project.injectReturn( 'JSON.parse( JSON.stringify( window ) )' )
	# _.pr()
	try:
		_.printVar( name_resolution )
	except Exception as e:
		pass
	# _auditJS.imp.action( data )
	_.colorPrint(  [ '', 'cache: jsAuditLog.cache' ]  , 'yellow' )
	_browser.imp.project.close()
	
name_resolution = []

_auditJS = _.regImp( __.appReg, 'auditJavascript' )
# jsAuditLog

# p f -in *.js + ;. "function(" -jn | p line --c - jquery > %tmpf0%
# type %tmpf0% | p changeTextEnd + ;. "function(" -text  ";n;t;tfamily.v.tracker.push({'action';.'change','function';.'*_*','timestamp';.(new Date).getTime(),'id';.family.talk.thisTable,'d';.family.talk.adherence.r_d(),'a';.family.talk.adherence.r_a(),'m';.family.talk.adherence.r_m()});" -payload ;. 0 nsif -add - setTimeout

# adherence.r_a()});
# adherence.r_a(),'m':family.talk.adherence.r_m()});

########################################################################################
if __name__ == '__main__':
	action()







