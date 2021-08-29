#!/usr/bin/python3
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

_.appInfo[focus()] = {
	'file': '-paste.py',
	'liveAppName': __.thisApp( __file__ ),
 	'description': 'paste clipboard',
	'categories': [
						'clipboard',
						'paste',
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

def cleanString(data):
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	return data

def cleanStringA(data):
	data = _str.cleanBE(data,_v.default_powershell)
	data = _str.cleanBE(data,'\r')
	data = _str.cleanBE(data,'\n')
	data = _str.cleanBE(data,'\r')
	data = _str.cleanBE(data,'\t')
	data = _str.cleanBE(data,' ')
	return data

def formatData( result ):
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	return result



def clip_get():
	result = 'error'
	try:
		result = clip_get_2()
	except Exception as e:
		_.cp( '\tpython3 -m pip install pyperclip', 'yellow' )
		try:
			result = clip_get_1()
		except Exception as e:
			try:
				result = clip_get_3()
			except Exception as e:
				_.cp( 'Error: clipboard error', 'red' )
				_.cp( '\tpython3 -m pip install pyperclip', 'yellow' )

	if not result:
		_.cp( 'Error: clipboard error', 'red' )
		_.cp( '\tpython3 -m pip install pyperclip', 'yellow' )
		sys.exit()
	# print( result )
	# sys.exit()
	return result


def clip_get_1():
	from tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	return r.clipboard_get()


def clip_get_3():
	import subprocess
	# print('_.isWin:',_.isWin)
	if _.isWin:
		_.cp( 'Error: clipboard error', 'red' )
		return None

	tmpA = _v.stmp +_v.slash+ 'cryptString-A.txt'
	tmpB = _v.stmp +_v.slash+ 'cryptString-B.txt'
	if os.path.isfile(tmpA):
		os.unlink(tmpA)
	if os.path.isfile(tmpB):
		os.unlink(tmpB)
	if not _.which('xsel'):
		if not _.isWin:
			print( '\tsudo apt install xclip xsel' )
			return None

	cmd = ["xsel", "--clipboard", "--output", ">", tmpA ]
	# print( ' '.join(cmd) )
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	if os.path.isfile(tmpA):
		return _.getText( tmpA, raw=True, clean=2 )
	return None
	# return _.which('xsel')
	# return _.which('xclip')
	# return _.which('python3')

	# return 'test'

def clip_get_2():
	import pyperclip
	return cleanString( pyperclip.paste() )

	# global win32clipboard
	# if win32clipboard is None:
	# 	import win32clipboard
	# # get clipboard data
	# win32clipboard.OpenClipboard()
	# data = win32clipboard.GetClipboardData()
	# win32clipboard.CloseClipboard()
	# return data

win32clipboard = None

paste = clip_get

def action():


	print( clip_get() )



########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()




