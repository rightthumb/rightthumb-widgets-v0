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
### EXAMPLE: START
# import simplejson as json
# from threading import Timer
# from lxml import html
# import requests
# import cssselect
# import sqlite3
### EXAMPLE: END
##################################################


def appSwitches():
	pass
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )
	### EXAMPLE: END


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
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
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	### EXAMPLE: START
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
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
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
			'/usr/bin/bluefish',
			'/usr/bin/brackets ',
			'/usr/bin/lighttable',
			'/usr/bin/gedit',
			'/usr/bin/kakoune',
			'/usr/bin/vscode',
			
			'/usr/bin/notepad++',
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
			'/usr/bin/vi',
			'',
	]

	theLIST = [
			"sublime_text",
			"code-oss",
			"brackets",
			"notepad++",
			"bluefish",

			"acme",
			"akelpad",
			"alphatk",
			"arachnophilia",
			"atom",
			"bbedit",
			"bbedit",
			"brackets",
			"codewright",
			"crimson",
			"cudatext",
			"cygnused",
			"eddie",
			"emeditor",
			"epsilon",
			"featherpad",
			"geany",
			"gedit",
			"golded",
			"html_kit",
			"hxd",
			"jedit",
			"jove",
			"juffed",
			"kate",
			"kedit",
			"kile",
			"komodo",
			"kwrite",
			"lapis",
			"leafpad",
			"leo",
			"lighttable",
			"mcedit",
			"metapad",
			"microemacs",
			"mousepad",
			"multi-edit",
			"nedit",
			"notepad",
			"notepad2",
			
			"notetab",
			"pe",
			"pluma",
			"polyedit",
			"pfe",
			"pspad",
			"q10",
			"rj",
			"sam",
			"scite",
			"simpletext",
			"slickedit",
			"smultron",
			"subethaedit",
			"hydra",
			
			"teachtext",
			"ted",
			"tex-edit",
			"textpad",
			"wildedit",
			"texniccenter",
			"texshop",
			"textedit",
			"textmate",
			"textwrangler",
			"topstyle",
			"ultraedit",
			"ulysses",
			"vedit",
			"winedt",
			"x11",
			"xedit",
			"yudit"
	]

	na = []
	for x in find_unix_editor:
		parts = x.split('/')
		parts.reverse()
		na.append( parts.pop(0) )
	saveList = []
	allList = []
	for x in theLIST:
		allList.append( '/usr/bin/'+x )
		if not x in na:
			saveList.append( '/usr/bin/'+x )

	_.printVarSimple(allList)




########################################################################################
if __name__ == '__main__':
	action()