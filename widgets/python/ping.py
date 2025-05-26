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
import _rightThumb._matrix as _matrix
a, app, application = _matrix.theApp()
appDBA = _matrix.clearFocus( __name__, __file__ )
_matrix.appReg = appDBA
# _.pr( 'appDBA', appDBA )
app.focus( appDBA )
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = _matrix.appName( appDBA, parentApp, childApp )
	if reg:
		_matrix.appReg = f
	return f
_matrix.registeredApps.append( focus() )
import _rightThumb._base3 as _
import _rightThumb._base4 as ___
##################################################
program = {

	'file': 'ping.py',
	'liveAppName': _matrix.thisApp( __file__ ),
	'description': 'ping monitor',
	
	'categories': [
						'network',
						'tool',
						'ping',
						'test',
						'check',
						'status',
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
						'p ping -file file.txt',
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

}




def appSwitches():
	app.load_switches = True
	app.switch( 'Host', '-h,-host,-hosts,-server,-servers' )
	app.switch( 'SoundOnError', '-sound,-play,-error,-beep' )
	app.switch( 'Duration', '-time,-dur,-duration' )
	app.switch( 'Print', '-print' )
	_.isTime = True


# _.autoBackupData = __.autoCreationConfiguration['backup']
# __.isRequired_Pipe = False
# __.isRequired_Pipe_or_File = False
focusID = None
def registration():
	global appDBA
	global program
	global focusID
	focusID = app.focus( appDBA ).register( program )
	appSwitches()
	app.load()

	if app.load_switches:
		_.myFileLocation_Print = False
		app.switch( 'Files' ).trigger( _.myFileLocations )
		app.switch( 'Folder' ).trigger( _.myFolderLocations )
		app.switch( 'URL' ).trigger( _.urlTrigger )
		app.switch( 'Ago' ).trigger( _.timeAgo )
		app.switch( 'Duration' ).trigger( _.timeFuture )
		app.defaultScriptTriggers()
	
	app.processSwitches()
	app.postLoad()

registration()

########################################################################################
# START

import _rightThumb._beep as _beep
import platform
import subprocess
import socket

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
	s.connect((ip, int(port)))
	s.shutdown(2)
	return True
   except:
	return False


def formatData( result ):
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	return result

def check_ping(host):
	# https://stackoverflow.com/questions/26468640/python-function-to-test-ping/39563638
	if ':' in host:
		hp = host.split(':')
		h = hp[0]
		p = hp[1]
		response = isOpen(h,p)
	elif not ':' in host:
		if platform.system().lower() == "windows":
			# response = os.system("ping -n 1 -w 500 " + host + "")
			# response = os.system("dir")
			# response = os.system("ping -n 1 -w 500 " + host + " > nul")
			result = subprocess.run(['ping', '-n','1','-w','500',host], stdout=subprocess.PIPE)
			# _.pr(result)
		else:
			result = subprocess.run(['ping', '-c','1','-W','0.5',host], stdout=subprocess.PIPE)
			# response = os.system("ping -c 1 -W 0.5" + host + "> /dev/null")
		# _.pr(result.stdout)
	
		if 'reply' in str(result.stdout).lower():
			response = 1
		else:
			response = 0
		
		if app.switch('Print').isActive():
			if response:
				_.colorThis( host, 'green')
				_.colorThis( formatData(result.stdout), 'green')
			else:
				_.colorThis( host, 'red')
				_.colorThis( formatData(result.stdout), 'red')

	return response
	if response == 1:
		return "Network Active"
		return "alive"
	else:
		return "Network Error"
		return "not alive"
def action():
	hosts = ['google.com']
	if app.switch('Host').isActive():
		hosts = app.switch('Host').getValues()
	

	if not app.switch('Duration').isActive():
		for h in hosts:
			# _.pr( h, check_ping(h) )
			if check_ping(h):
				_.colorThis( h, 'green' )
			else:
				_.colorThis( h, 'red' )

	elif app.switch('Duration').isActive():
		bad = {}
		duration = app.switch('Duration').getValue()
		for h in hosts:
			bad[h] = 0
		while not time.time() > duration[0]:
			_.pr()
			_.pr()
			left = str( duration[0] - time.time() )
			_.colorThis( [ ' : ', left.split('.')[0], ' : ' ], 'yellow' )
			for h in hosts:
				# _.pr( h, check_ping(h) )
				if check_ping(h):
					bad[h] = 0
					if not app.switch('Print').isActive():
						_.colorThis( h, 'green' )
				else:
					bad[h] += 1
					if not app.switch('Print').isActive():
						_.colorThis( [ h, bad[h] ], 'red' )
					if app.switch('SoundOnError').isActive() and bad[h] > 1:
						_.color( [ '\t IS BEEPING!!', bad[h] ], c='red', b='on_white', attr='bold' )
						_beep.mission_impossible()
			time.sleep(2)


if __name__ == '__main__':
	app.asyn( 'action', action, trigger=app.focus(appDBA).unregister )





