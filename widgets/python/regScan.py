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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str

##################################################

##################################################


def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','Logfile.CSV', description='Files' )
	_.switches.register( 'Key', '-key' )
	_.switches.register( 'No', '-no', 'file OR reg    OR    f OR r' )

	_.switches.register( 'Binary', '-bin,-binary' )
	_.switches.register( 'Text', '-txt,-text' )


_.autoBackupData = False
# _.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'regScan.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Scan registry',
	'categories': [
						'scan',
						'reg',
						'registry',
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
						'p regScan -f Logfile.CSV ',
						''
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )

########################################################################################
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# _.setPipeData( os.listdir(os.getcwd()), focus() )
# _.showLine(item)
#     if os.path.isdir(row):
#     if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START

def processReg( path, vLx=None ):
	global data
	
	if 'r' in _.switches.value('No'):
		return None

	if path.lower().startswith('computer\\'):
		path = path[9:]
	if path.upper().startswith('HKEY_LOCAL_MACHINE\\'):
		path = 'HKLM\\' + path[19:]
	elif path.upper().startswith('HKEY_CURRENT_USER\\'):
		path = 'HKCU\\' + path[18:]

	run = True
	if run and path.lower() in data:
		run = False
	if run and path.startswith('\\REGISTRY'):
		run = False

	if run:
		if path.startswith('HKLM\\') or path.startswith('HKCU\\'):
			run = True
		else:
			run = False


	if run:
		# _.pr( path )
		# _.pr(  )
		# _.printVarSimple( record )
		# _.pr( record.keys() )
		
		data.append( path.lower() )
		lm_cu = ''
		if path.startswith('HKLM\\'):
			lm_cu = 'HKLM'
		elif path.startswith('HKCU\\'):
			lm_cu = 'HKCU'

		else:
			return None

		path = path[5:]
		# _.pr(path)
		# _.pr('|'+path+'|')

		# _.pr()
		# _.pr(path)
		# _.pr()

		try:
			if lm_cu == 'HKLM':
				# key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, key )
				key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE , path )
				# key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE , 'SOFTWARE\\Microsoft\\Windows' )
				# key = winreg.OpenKey( lm , key )
			elif lm_cu == 'HKCU':
				key = winreg.OpenKey( winreg.HKEY_CURRENT_USER , path )
			
			# _.colorThis( path, 'green' )

			table = []
			try:
				i = 0
				while 1:
					name, value, vtype = winreg.EnumValue(key, i)
					if not type(value) == bytes:
						v = value
					else:
						v = 'bytes'
					vLxS = ''
					if not vLx is None and vLx == name:
						vLxS = 'xXx'

					r = { 's': vLxS, 'name': name, 'type': type(value), 't': vtype, 'value': v }
					if _.showLine( str(r) ):
						table.append(r)
					# _.pr(name, vtype, type(value))
					# print (repr(name))
					i += 1
			except WindowsError:
				pass

			if len(table):
				_.colorThis( lm_cu+'\\'+path, 'green' )
				_.tables.register( 'data', table )
				_.tables.print( 'data', 's,name,type,t,value' )

				# print ("Bot donf")

			winreg.CloseKey(key)
			# sys.exit()
		except Exception as e:
			if vLx == None:
				parts = path.split( '\\' )
				parts.reverse()
				vLx = parts.pop(0)
				parts.reverse()
				processReg( '\\'.join(parts) , vLx=vLx )



def processFile( path ):
	global dataF

	if not os.path.isfile(path):
		return None

	if 'f' in _.switches.value('No'):
		return None

	if path.lower() in dataF:
		return None
	
	dataF.append( path.lower() )


	if _.showLine(path):
		if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
			_.pr( path )
		else:

			info = _dir.info( path, mime=True )
			if type(info) == bool:
				return None

			if info['name'] == 'desktop.ini':
				return None
			if info['mime'] == 'Binary' and _.switches.isActive('Binary'):
				_.pr( path )
			elif info['mime'] == 'Text' and _.switches.isActive('Text'):
				_.pr( path )



def action():
	global data
	global dataF
	# load()

	data.append( 'path' )
	data.append( 'hklm' )
	data.append( 'hkcu' )
	data.append( 'hkcu\\software' )

	if _.switches.isActive('Key'):
		keys = _.switches.values('Key')
		if not len(keys) and not type( _.appData[__.appReg]['pipe'] ) == bool:
			keys = _.appData[__.appReg]['pipe']
		for k in keys:
			processReg(k)

	if _.switches.isActive('Files'):
		
		# computer_name = os.getenv('COMPUTERNAME')


		# lm = winreg.ConnectRegistry( computer_name, winreg.HKEY_LOCAL_MACHINE )
		# cu = winreg.ConnectRegistry( computer_name, winreg.HKEY_CURRENT_USER )
		# _.pr( 'here' )

		theLogFiles = _.switches.values('Files')
		if not len(theLogFiles) and not type( _.appData[__.appReg]['pipe'] ) == bool:
			theLogFiles = _.appData[__.appReg]['pipe']

		for theLogFile in theLogFiles:
			# _.pr( 'Log:', theLogFile )
			# records = _.getCSV( theLogFile )
			records = _.csv( theLogFile )
			for record in records:
				run = True

				if 'NOT FOUND'     in record['Result']:
					run = False
				if 'ACCESS DENIED' in record['Result']:
					run = False

				if run:
					if 'Reg' in record['Operation']:
						processReg( record['Path'] )
			
					if 'File' in record['Operation']:
						processFile( record['Path'] )


					



	if not _.switches.isActive('Files'):
		if not type( _.appData[__.appReg]['pipe'] ) == bool:
			_.pipeCleaner()
			# _.printVar(_.appData)
			for i,row in enumerate(_.appData[__.appReg]['pipe']):
				loRow = row.lower()
				shouldRun = False
				if loRow.startswith( 'hklm'+_v.slash ):
					shouldRun = True
				if loRow.startswith( 'hkcu'+_v.slash ):
					shouldRun = True
				if shouldRun:
					if not loRow in data:
						data.append( row.lower() )
						do = 'call q "' + row + '">'+_v.txt_temp
						_.pr( row )
						os.system('"' + do + '"')
						result = _.getText( _v.txt_temp, raw=True, clean=2 )
						for line in result.split('\n'):
							if _.showLine( line ):
								_.pr( line )



# https://docs.python.org/3.6/library/winreg.html
# https://mail.python.org/pipermail/python-list/2009-August/548680.html
# https://stackoverflow.com/questions/30932831/winreg-openkey-throws-filenotfound-error-for-existing-registry-keys

# def load():
#     global data
#     data = _.getData( 'table' )


import _rightThumb._dir as _dir
import winreg
data = []
dataF = []



########################################################################################
if __name__ == '__main__':
	action()







