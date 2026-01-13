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
	_.switches.register( 'todo', '-todo' )
	_.switches.register( 'Clip', '-clip' )
	_.switches.register( 'Add-todo', '-a,-add' )
	_.switches.register( 'Remove-todo', '-r,-rm' )
	pass 

_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs'] 
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'todo.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'todo lists from scrap',
	'categories': [
						'scrap',
						'todo',
						'list',
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



def action():

	if _.switches.isActive('Clip'):
		_paste = _.regImp( __.appReg, '-paste' )
		_copy = _.regImp( __.appReg, '-copy' )
		data = _paste.imp.paste()
		data = data.replace( 'ToDo', 'todo' )
		data = data.replace( 'TODO', 'todo' )
		new=[]
		do=''
		if _.switches.isActive('Add-todo'):
			do='add'
		if _.switches.isActive('Remove-todo'):
			do='remove'

		if not do:
			if 'todo:' in data:
				do='remove'
			else:
				do='add'

		if do == 'add':
			for line in data.split('\n'):
				test = _str.cleanBE(line,'\t')
				test = _str.cleanBE(line,' ')
				test = _str.replaceDuplicate(test,' ')
				test = test.replace('\r','')
				if test:
					if not line.startswith('todo:'):
						line = 'todo: '+line
				new.append(line)
		if do == 'remove':
			for line in data.split('\n'):
				if line.startswith('todo: '):
					line = line.split('todo: ')[1]
				if line.startswith('todo:x '):
					line = line.split('todo:')[1]
				if line.startswith('todo:'):
					line = line.split('todo:')[1]
				new.append(line)
		data='\n'.join(new)
		data=data.replace('todo: x ', 'todo:x ')
		_copy.imp.copy( data )
		return None
	pass
	if _.switches.isActive('todo'):
		path=_v.myHome  +os.sep+  'projects'  +os.sep+  'project-log.txt'
		last=-1
		for i,line in enumerate(_.getText(path,raw=True).split('\n')):
			if line.lower().startswith('todo:'):
				# _.pr(i,i-last)
				# _.pr(last-i)
				if i-last > 10:
					_.pr()
					_.cp( _.linePrint(txt='_',p=0), 'yellow' )
					_.pr(i+1)
					_.pr()
				else:
					ix=1
					while not ix==i-last:
						_.pr()
						ix+=1
				_.pr(line)
				last=i


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()