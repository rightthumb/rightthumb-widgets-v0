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
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._encryptString as _blowfish
##################################################

def appSwitches():
	pass
	_.switches.register( 'Encrypt', '-en,-encrypt' )
	_.switches.register( 'Decrypt', '-de,-decrypt' )
	_.switches.register( 'Password', '-password,-p', 'only -p if password is MACHINE' )
	_.switches.register( 'Vault', '-v,-vault' )
	_.switches.register( 'Clipboard', '-clip,-copy,-copied,-clipboard' )
	_.switches.register( 'JustReturn', '-jr' )
	_.switches.register( 'Temp', '-temp' )
	
	


__.releaseAcquiredData = False
_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'cryptString.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'encrypt or decrypt string',
	'categories': [
						'encrypt',
						'decrypt',
						'crypt',
						'string',
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
						'p cryptString -vault -en "1password!"',
						'',
						'p cryptString -vault -de Gb6xPipPDZQq3mLCubP1Ow==',
						'',
						'p fileTail -f %scrap% | p cryptString -vault',
						'',
						'p fileTail -f %scrap%  -lines 50| p cryptString -password 123 456 789',
						'',
	],
	'columns': [
					   # { 'name': 'name', 'abbreviation': 'n' },
	],
	'aliases': [
					   # 'this',
					   # 'app',
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



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

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )

_.postLoad( __file__ )


########################################################################################
# START

def formatData( result ):
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	return result

def clip_set_0(data):
	global win32clipboard
	if win32clipboard is None:
		import win32clipboard
	# set clipboard data
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	try:
		win32clipboard.SetClipboardText( data )
	except Exception as e:
		win32clipboard.EmptyClipboard()
		_.colorThis(  [ 'Unable to set clipboard data' ], 'red'  )
	win32clipboard.CloseClipboard()


def clip_set_2(data):
	import pyperclip
	pyperclip.copy( cleanString(data) )

def clip_set_3(data):
	import subprocess
	if _.isWin:
		_.cp( 'Error: clipboard error', 'red' )
		return None

	tmpA = _v.stmp +_v.slash+ 'cryptString-A.txt'
	tmpB = _v.stmp +_v.slash+ 'cryptString-B.txt'
	if os.path.isfile(tmpA):
		os.unlink(tmpA)
	if os.path.isfile(tmpB):
		os.unlink(tmpB)
	
	_.saveText( data, tmpA )
	time.sleep(.2)
	if not os.path.isfile(tmpA):
		print( 'no file' )
		return None

	# cmd = ["cat", tmpA, "|",  "xsel", "--clipboard", "--input"  ]
	# mycmd=subprocess.getoutput( ' '.join(cmd) )
	from subprocess import Popen, PIPE
	p = Popen(['xsel','-pi'], stdin=PIPE)
	p.communicate(input= formatData(data) )

	p = Popen(['xsel', '-bi'], stdin=PIPE)
	p.communicate(input= formatData(data) )
	# p.communicate(input=data)


	result = None
	try:
		result = clip_get_3()
	except Exception as e:
		result = None

	if not result:
		# print( ' '.join(cmd) )
		_.cp( 'Error: unable to copy', 'red' )
		print(data)

	# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

	# p1 = subprocess.Popen(["cat", tmpA], stdout=subprocess.PIPE)
	# p2 = subprocess.Popen(["xsel", "--clipboard", "--input"], stdin=p1.stdout, stdout=subprocess.PIPE)
	# p2.communicate()


	time.sleep(.2)
	if os.path.isfile(tmpA):
		return _.getText( tmpA, raw=True, clean=2 )
	return None


def clip_set_1(data):
	from tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append( cleanString(data) )
	# r.destroy()

def clip_set(data):
	# clip_set_3(data)
	try:
		clip_set_2(data)
	except Exception as e:
		try:
			clip_set_1(data)
		except Exception as e:
			try:
				clip_set_3(data)
			except Exception as e:
				_.cp( 'Error: clipboard error', 'red' )
				sys.exit()



# def clip_set_tmp(data):
	# clip_set_2(data)
	# return None
	# try:
	# 	clip_set_1(data)
	# except expression as identifier:
	# 	try:
	# 		clip_set_2(data)
	# 	except expression as identifier:
	# 		try:
	# 			clip_set_3(data)
	# 		except expression as identifier:
	# 			try:
	# 				clip_set_4(data)
	# 			except expression as identifier:
	# 				print( 'python3 -m pip install pyperclip' )
	# 				print( 'pip3 install pyperclip' )
	# 				print()
	# 				print( 'sudo apt install xclip xsel' )
	# 				print( 'sudo pacman xclip xsel' )
	# 				print( 'sudo dnf xclip xsel' )
	# 				print( '' )


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

def action():


	# print(1010,_.switches.isActive('Encrypt'))
	password = None
	if  _.switches.isActive('Password'):
		if len(  _.switches.value('Password')  ):
			password = _.switches.values('Password')[0]
		else:
			password = None
	else:
		password = None

		if  _.switches.isActive('Vault'):
			password = _vault.key()

		if password is None:
			password = _vault.key()


	if  _.switches.isActive('Clipboard'):
		
		data = clip_get()

		data = cleanString( data )
		if _.switches.value('Clipboard').lower().startswith('p'):
			print( '|'+data+'|' )



		if data.endswith('=') or data.endswith('/U') or _.switches.isActive('Decrypt'):
			clip = _blowfish.decrypt( data, _vault.key() )
		else:
			clip = _blowfish.encrypt( data, _vault.key() )

		clip = cleanString( clip )
		if _.switches.value('Clipboard').lower().startswith('p'):
			print( clip )

		clip_set(  clip  )

		if  _.switches.isActive('Temp'):
			
			loops = 5

			if len( _.switches.value('Temp') ):
				loops = int( _.switches.value('Temp') )

			while loops:
				_.updateLine( 'waiting: '+str(loops) )
				loops -= 1
				if not loops:
					_.updateLine( '                  ' )
					_.updateLine( '\r' )
					break
				time.sleep(1)
				_.updateLine( '                  ' )

			# print()
			clip_set( '' )
			_.updateLine( '                                    ' )
			_.updateLine( 'clipboard cleared' )
			time.sleep(1)
			_.updateLine( '                                    ' )


		sys.exit()





	if _.switches.isActive('Encrypt'):
		# print(1030,_.switches.isActive('Encrypt'))
		if not _.switches.isActive('JustReturn'):
			_.colorThis( _blowfish.encrypt( ' '.join( _.switches.values('Encrypt') ), password ), 'green' )
		elif _.switches.isActive('JustReturn'):
			return _blowfish.encrypt( ' '.join( _.switches.values('Encrypt') ), password )

	elif _.switches.isActive('Decrypt'):
		# print(1040)
		if not _.switches.isActive('JustReturn'):
			_.colorThis( _blowfish.decrypt( _.switches.values('Decrypt')[0], password ), 'green' )
		elif _.switches.isActive('JustReturn'):
			return _blowfish.decrypt( _.switches.values('Decrypt')[0], password )
	else:
		# print(1050)
		for i,row in enumerate(_.isData(c=False,focus=focus())):
			row = row.replace( '\n', '' )
			if row.endswith('='):
				try:
					de_row = _blowfish.decrypt( row, password )
				except Exception as e:
					pass
				if  not _.switches.isActive('Password'):
					row = de_row
				elif  _.switches.isActive('Password'):

					if len( _.switches.values('Password') ) > 1:

						for i,pw in enumerate( _.switches.values('Password') ):
							if i:
								good=True
								for x in de_row:
									if not x in _str.printable:
										good = False
								# print('good:',good,x)
								if not good:
									try:
										de_row = _blowfish.decrypt( row, pw )
									except Exception as e:
										pass
								else:
									row = de_row





					good=True
					for x in de_row:
						if not x in _str.printable:
							good = False
					# print('good:',good,x)
					if not good:
						row = _blowfish.decrypt( row, _vault.key() )
					else:
						row = de_row

			print( row )
		# print( password )

				

# _vault = _.regImp( __.appReg, '_rightThumb._vault' )
import _rightThumb._vault as _vault



########################################################################################
if __name__ == '__main__':
	action()






