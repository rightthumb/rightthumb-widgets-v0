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
	'file': 'bm-dirty.py',
	'liveAppName': __.thisApp( __file__ ),
 	'description': 'auto add bookmarks',
	'categories': [
						'bookmarks',
						'default',
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


data="""ii|/mnt/d/tech/hosts/VULCAN/indexes
vi|/mnt/d/tech/hosts/VULCAN/indexes
iv|/mnt/d/tech/hosts/VULCAN/indexes
hh|/mnt/d/tech/hosts
mi|/mnt/d/tech/hosts/MSI/indexes
im|/mnt/d/tech/hosts/MSI/indexes
pp|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs
p|{6FAB5628-94A1-410A-82D1-1D42A2A11750}
ppp|/mnt/d/tech/programs
git|/mnt/d/tech/programs/git
b|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/bash
bash|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/bash
livepp|/mnt/d/tech/programs
l.pp|/mnt/d/tech/programs
l.b|/mnt/d/tech/programs/bash
l.bash|/mnt/d/tech/programs/bash
l.py|/mnt/d/tech/programs/python/src/unity
dl|/mnt/c/Users/Scott/Downloads
l.ttt|/mnt/d/tech/programs/databank/tables
l.db|/mnt/d/tech/programs/databank/tables
live.pp|/mnt/d/tech/programs
pp.live|/mnt/d/tech/programs
live.py|/mnt/d/tech/programs/python/src/unity
py.live|/mnt/d/tech/programs/python/src/unity
live.i|/mnt/d/tech/hosts/VULCAN/indexes
i.live|/mnt/d/tech/hosts/VULCAN/indexes
h|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}
i|{A8693D4B-8A80-898F-83F0-E806D2F36800}/hosts/VULCAN/indexes
tt|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/tables
ttt|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/databank/tables
py|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/python/src/unity
ent|/mnt/d/entertainment/movies
pr|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects
doc|/mnt/c/Users/Scott/Documents
docs|/mnt/c/Users/Scott/Documents
d|/mnt/c/Users/Scott/Desktop
ps|/mnt/c/Users/Scott/Documents/WindowsPowerShell
ps1|/mnt/c/Users/Scott/Documents/WindowsPowerShell
doc.ps|/mnt/c/Users/Scott/Documents/WindowsPowerShell
doc.ps1|/mnt/c/Users/Scott/Documents/WindowsPowerShell
key|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/keys
keys|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/keys
key.p|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/keys/p
k.p|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/keys/p
kp|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/keys/p
k|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/keys
config|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/config
ta|/mnt/d/techApps
sh.stuff|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/sh-stuff
stuff.sh|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/sh-stuff
sh|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/sh-stuff
sshfs|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/sshfs_test
b.live|/mnt/d/tech/programs/bash
bash.live|/mnt/d/tech/programs/bash
.rt|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt
pr.live|/mnt/d/tech/hosts/VULCAN/projects
h.live|/mnt/d/tech/hosts/VULCAN
ovpn|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/ovpn
ovpn.live|/mnt/d/tech/hosts/VULCAN/projects/ovpn
bash.test|/mnt/d/tech/hosts/VULCAN/projects/bash
pp.l|/mnt/d/tech/programs
py.l|/mnt/d/tech/programs/python/src/unity
i.l|/mnt/d/tech/hosts/VULCAN/indexes
b.l|/mnt/d/tech/programs/bash
bash.l|/mnt/d/tech/programs/bash
pr.l|/mnt/d/tech/hosts/VULCAN/projects
h.l|/mnt/d/tech/hosts/VULCAN
ovpn.l|/mnt/d/tech/hosts/VULCAN/projects/ovpn
bm|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs/python/src/unity/_rightThumb/_bookmarks
tool.live|/mnt/d/tech/programs/bash/install/py
tool|/mnt/d/tech/programs/bash/install/py
tt-|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt/profile/tables
p-|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt/profile
rt-|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt
pr-|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt/profile/projects"""



def action():
	global data
	file = ''
	for line in data.split('\n'):
		line = line.replace( chr(27), '' )
		line = line.replace( chr(10), '\n' )
		a = line.split('|')[0]
		bm = _v.resolveFolderIDs(line.split('|')[1])
		if os.path.isdir(bm):
			text=''
			if not _.isWin:
				text += 'source $HOME/.bashrc'
			text += '\n'
			if _.isWin:
				text += bm[0]+':'
				text += '\n'

			text += 'cd '
			text += bm
			text += '\n'

			text += 'm '
			text += a
			text += '\n'
			text += '\n'
			file += text
			print(text)
	_copy.imp.copy( file )

_copy = _.regImp( __.appReg, '-copy' )


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






