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


from _rightThumb._base3 import _0_10_36_238 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','Procmon_log_.CSV', isRequired=True, description='Files' )
	_.switches.register( 'Key', '-key', 'HKLM,HKCU' )
	_.switches.register( 'Table', '-table' )


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'regScanMon.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Load Procmon csv log. Look up in registry and scan for something specific',
	'categories': [
						'registry',
						'Procmon',
						'search',
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
						'p regScanMon -file Procmon_log_.CSV',
						'p regScanMon -file outlook_reg_sample.CSV + .pst',
						'p regScanMon -key hkcu -table -file outlook_reg_sample.CSV + .pst ',
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
# START

# REG_EXPAND_SZ
# REG_MULTI_SZ
# REG_DWORD
def extract( data ):
	records = []
	for row in data.split('\n'):
		if 'REG_EXPAND_SZ' in row or 'REG_SZ' in row or 'REG_DWORD' in row:
			if 'REG_MULTI_SZ' in row:
				data = row.split( 'REG_MULTI_SZ' )    
			if 'REG_EXPAND_SZ' in row:
				data = row.split( 'REG_EXPAND_SZ' )
			if 'REG_SZ' in row:
				data = row.split( 'REG_SZ' )
			if 'REG_DWORD' in row:
				data = row.split( 'REG_DWORD' )
			if len( data ) > 1:
				for i,d in enumerate( data ):
					data[i] = _str.replaceDuplicate (data[i], ' ' )
					data[i] = data[i].replace( '\t', '' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
					data[i] = _str.cleanBE( data[i], ' ' )
				records.append({ 'field': data[0], 'value': data[1]  })
	return records
				
				


def action():
	_.pr( 'use: regScan' )
	sys.exit()
	global data
	load()

	spent = []
	_.pr()
	_.pr()
	for i,record in enumerate(data):
		if _.switches.isActive('Plus'):
			_.loadingAnimation('Searching')
		if record['Operation'].startswith('Reg'):
			shouldRun = True
			if record['Path'].count( _v.slash ) < 4:
				shouldRun = False
			if record['Result'] == 'NAME NOT FOUND':
				shouldRun = False
			if record['Result'] == 'ACCESS DENIED':
				shouldRun = False
			if _.switches.isActive('Key'):
				if 'cu' in _.switches.value('Key').lower():
					if not record['Path'].lower().startswith('hkcu'):
						shouldRun = False
				else:
					if not record['Path'].lower().startswith('hklm'):
						shouldRun = False

			if shouldRun:
				if not record['Path'].lower() in spent:
					spent.append( record['Path'].lower() )
					shouldRun = True

					# _.printTest( record, x=0 )
					do = 'call q "' + record['Path'] + '">'+_v.txt_temp
					os.system('"' + do + '"')
					result = _.getText( _v.txt_temp, raw=True, clean=2 )
					if _.showLine( result ):

						# _.pr( '--------------------' )
						# _.pr( _v.txt_temp )
						# # _.pr( result )
						# _.pr( '--------------------' )
						# _.pr()
						# _.LoadingDone('Test Exit')
						# sys.exit()
						# pause=input('pause: ')
						if _.switches.isActive('Plus'):
							_.LoadingDone('Found')
						_.colorThis( record['Path'], 'green' )
						fields = extract( result )
						if not len( fields ):
							_.colorThis( result, 'white' )
						else:
							if _.switches.isActive('Table'):
								_.switches.fieldSet( 'Long', 'active', True )
								theLabel = _.genUUID()
								_.tables.register( theLabel, fields )
								_.tables.fieldProfileSet(theLabel,'field,value','alignment','left')
								_.tables.print( theLabel, 'field,value' )
							else:
								for field in fields:
									_.pr()
									_.colorThis( field['field'], 'Color.darkcyan' )
									_.colorThis( '\t'+field['value'], 'Color.cyan' )
						_.pr()
						_.pr()

	if _.switches.isActive('Plus'):
		_.LoadingDone('Search Complete')



def load():
	global data
	data = _.csv( _.switches.values('Files')[0] )


data = []
########################################################################################
if __name__ == '__main__':
	action()







