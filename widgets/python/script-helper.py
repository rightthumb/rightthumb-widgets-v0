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
	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	### EXAMPLE: END

### EXAMPLE: START
# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
# 	finds the file in probable locations
# 	and 
# 		if  _.autoBackupData = True
# 		and __.releaseAcquiredData = True
# 			GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
# 		you can run apps on usb at a clients office
# 			when you get home run: p app -loadepoch epoch 
# 				backed up
# 					pipe
# 					files
# 					tables
### EXAMPLE: END
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	### EXAMPLE: START
	# _.default_switch_trigger('Plus', trigger_plus)
	# _.switches.trigger( 'Files',_.inRelevantFolder )	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
# 	if os.path.isdir( row ):
# 	if os.path.isfile( row ):
#	os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
# 													if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START



def action():

	# indexes
	# relevant_OC
	# inIndex
	#--> replace string fix {:replace:}
	if _.switches.isActive('Replace'):
		dump =' '.join(_.switches.values('Replace'))
		# print(dump)
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
			# print(i,text)
		pass
		a=Q[0]
		b=Q[1]
		c=Q[2]
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
			print(a)
		return a
	_.e('use a switch\n p script-heplper ?? c')




########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





