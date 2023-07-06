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
# import platform
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
	_.switches.register( 'Count', '-count' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'find_text_editors.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'find text editors',
	'categories': [
						'tool',
						'app finder',
						'finder',
						'code editor',
						'text editor',
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
						'p find_text_editors',
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
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations )
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

	find_unix_editor = [
			'/snap/bin/subl',
			'/usr/bin/sublime_text',
			'/usr/bin/subl',
			'/opt/sublime/subl',
			'/opt/sublime/sublime_text',

			'/snap/bin/code',
			'/usr/bin/code-oss',
			"/usr/bin/brackets",
			'/usr/bin/bluefish',
			'/usr/bin/notepad++',



			"/usr/bin/acme",
			"/usr/bin/akelpad",
			"/usr/bin/alphatk",
			"/usr/bin/arachnophilia",
			"/usr/bin/bbedit",
			"/usr/bin/bbedit",
			"/usr/bin/codewright",
			"/usr/bin/crimson",
			"/usr/bin/cudatext",
			"/usr/bin/cygnused",
			"/usr/bin/eddie",
			"/usr/bin/emeditor",
			"/usr/bin/epsilon",
			"/usr/bin/featherpad",
			"/usr/bin/golded",
			"/usr/bin/html_kit",
			"/usr/bin/hxd",
			"/usr/bin/jedit",
			"/usr/bin/jove",
			"/usr/bin/juffed",
			"/usr/bin/kedit",
			"/usr/bin/kile",
			"/usr/bin/komodo",
			"/usr/bin/lapis",
			"/usr/bin/leafpad",
			"/usr/bin/leo",
			"/usr/bin/mcedit",
			"/usr/bin/metapad",
			"/usr/bin/microemacs",
			"/usr/bin/mousepad",
			"/usr/bin/multi-edit",
			"/usr/bin/nedit",
			"/usr/bin/notepad",
			"/usr/bin/notepad2",
			"/usr/bin/notetab",
			"/usr/bin/pe",
			"/usr/bin/pluma",
			"/usr/bin/polyedit",
			"/usr/bin/pfe",
			"/usr/bin/pspad",
			"/usr/bin/q10",
			"/usr/bin/rj",
			"/usr/bin/sam",
			"/usr/bin/scite",
			"/usr/bin/simpletext",
			"/usr/bin/slickedit",
			"/usr/bin/smultron",
			"/usr/bin/subethaedit",
			"/usr/bin/hydra",
			"/usr/bin/teachtext",
			"/usr/bin/ted",
			"/usr/bin/tex-edit",
			"/usr/bin/textpad",
			"/usr/bin/wildedit",
			"/usr/bin/texniccenter",
			"/usr/bin/texshop",
			"/usr/bin/textedit",
			"/usr/bin/textmate",
			"/usr/bin/textwrangler",
			"/usr/bin/topstyle",
			"/usr/bin/ultraedit",
			"/usr/bin/ulysses",
			"/usr/bin/vedit",
			"/usr/bin/winedt",
			"/usr/bin/x11",
			"/usr/bin/xedit",
			"/usr/bin/yudit",


			'/usr/bin/vscode',
			'/usr/bin/lighttable',
			'/usr/bin/gedit',
			'/usr/bin/kakoune',
			'/usr/bin/brackets ',
			
			'/usr/bin/limetext ',
			'/usr/bin/leafpad ',
			
			'/usr/bin/atom',
			'/usr/bin/pico',
			'/usr/bin/nano',
			'/usr/bin/kwrite',
			'/usr/bin/kate',
			'/usr/bin/geany',

			'/usr/bin/medit',
			'/usr/bin/neovim',
			'/usr/bin/jed',
			'/usr/bin/micro',
			'/usr/bin/gvim',
			'/usr/bin/vim',
			'/usr/bin/vi'
	]



	if _.switches.isActive('Count'):
		_.pr( len(find_unix_editor) )
	else:
		if _.isWin:

			_.pr( 'not currently windows compatable' )
		else:
			for editor in find_unix_editor:
				parts = editor.split('/')
				parts.reverse()
				app = parts.pop(0)
				del parts
				if os.path.isfile(editor):
					_.pr( app )

########################################################################################
if __name__ == '__main__':
	action()







