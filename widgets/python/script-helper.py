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
	_.switches.register( 'Replace', '-replace', '"\'haystack\' \'needle\' \'new\'"' )
	_.switches.register( 'NoPrint', '--c' )
	_.switches.register( 'isFile', '-fi' )
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
	# 'app': '7facG-jo0Cxk',
	'file': 'script-heplper.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'usage in .bat .sh etc',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'programming',
						'script',
						'code',
						'',
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
						_.hp('p script-helper -replace "\'C:\\\\Users\\\\Scott\\\\OneDrive\\\\Pictures\\\\terminal-wallpaper\\\\\' \'\\\\\\\\\' \'\\\\\'"'),
						_.hp(''),
						_.hp('.bat'),
						_.hp('	call p script-helper -replace "\'%b%\' \'/\' \'\\\\\'" > %tmpf%'),
						_.hp('	SET /p b=<%tmpf%'),
						_.hp(''),
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



def action():

	# indexes
	# relevant_OC
	# inIndex
	#--> replace string fix {:replace:}
	if _.switches.isActive('Replace'):
		dump =' '.join(_.switches.values('Replace'))
		# _.pr(dump)
		_code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
		_code.imp.validator.register( dump, 'javascript' )
		status = _code.imp.validator.createIndex( dump, 'javascript', skipLoad=True, simple=False, B=True )

		Q = []
		i=-1
		for ii,x in enumerate(_code.imp.validator.identity['identity']):
			i+=1
			o = x
			c = _code.imp.validator.identity['location']['open'][o]
			l = _code.imp.validator.getLabel( o, string=True )
			text=_code.imp.validator.assetSnipet( o, c )
			text=text[1:]
			text=text[:-1]
			Q.append(text)
			# _.pr(i,text)
		pass
		a=Q[0]
		b=Q[1]
		c=Q[2]
		if _.switches.isActive('isFile'):
			path=a
			a=_.getText(a,raw=True)
		if b=='\\\\':
			b='\\'
		if c=='\\\\':
			c='\\'
		if b=='\\\\\\\\':
			b='\\\\'
		if c=='\\\\\\\\':
			c='\\\\'



		i=0
		while b in a:
			i+=1; a=a.replace(b,c);
			if i>1000: break;
		if not _.switches.isActive('NoPrint'):
			_.pr(a)
		if _.switches.isActive('isFile'):
			_.saveText( a, path )
		return a
	_.e('use a switch\n p script-heplper ?? c')



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





