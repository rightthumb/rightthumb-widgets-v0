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
##################################################
import os, sys, time
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
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Type', '-t,-type' )
	_.switches.register( 'Name', '-name' )
	
	_.switches.register( 'Hr', '-hr' )
	_.switches.register( 'Random', '-r,-random' )


	pass

_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'greeting.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'greeting used in vps-hoth-7i0ZA-7GT90c-bot-chat',
	'categories': [
						'bot',
						'greeting',
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
						_.hp('p thisApp -file file.txt'),
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
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
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


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START

import random



def timeGreeting():

	if _.switches.isActive('Hr'):
		tb = _.timeblock(hr=_.switches.value('Hr'))
	else:
		tb = _.timeblock(epoch=time.time())

	

	return tb

name=None

def action(t=None):
	global name
	greetings = _.getTableDB('time-greeting.hash')

	if _.switches.value('Type')=='random':
		_.switches.fieldSet( 'Random', 'active', True )

	ti = timeGreeting()
	ty = _.rli(  'endearing name mean sexy mf none'.split(' ')  )
	
	if _.switches.isActive('Random'):
		if 'time' in _.switches.value('Random').lower():
			ti = _.rli(  'wee early morning afternoon evening late'.split(' ')  )
		
		# if 'type' in _.switches.value('Random').lower():
	# else:
	if _.switches.isActive('Type'):
		ty = _.switches.value('Type')
	if not t is None:
		ty = t

	ty=ty.lower()
	TG = greetings[ ti ]
	greeting = _.rli(TG)

	if ty == 'none':
		_.pr( greeting )
		return ''
	
	
	# endearing, name, mean, sexy, mf, none
	if ty == 'none':
		_.pr( greeting )
		return ''
	if ty == 'mf':
		end = _.getText(_v.ttt+os.sep+'greeting-mf.txt',raw=True,clean=2).split('\n')
	if ty == 'name':
		if _.switches.isActive('Name'):
			end = _.switches.values('Name')
		else:
			try:
				end = [_.switches.values('Type')[1]]
			except Exception as e:
				if not name is None:
					end=[name]
				else:
					end = 'Scott'.split(' ')

	if ty == 'sexy':
		end = ['sexy']
	if ty == 'mean':
		end = _.getText(_v.ttt+os.sep+'greeting-mean.txt',raw=True,clean=2).split('\n')
	if ty == 'endearing':
		end = _.getText(_v.ttt+os.sep+'greeting-endearing.txt',raw=True,clean=2).split('\n')

	END = _.rli(end).title()
	result = greeting+', '+END
	_.pr( result )
	return result


	# data = _.getText(_v.ttt+os.sep+'endearing.txt',raw=True,clean=2).split('\n')
	# d = random.randint(0,len(data)-1)

	# _.pr(data[d])



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





