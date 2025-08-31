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
import _rightThumb._encryptString as _blowfish
# import _rightThumb._md5 as _md5
##################################################

def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Last', '-last','200')
	_.switches.register('JSON', '-json')
	# _.switches.register('JSON', '-json')
	_.switches.register('Int', '-int', 'Mem_Usage')


__.setting('receipt-log',True)
__.setting('receipt-file',True)
__.setting('require-pipe||file',True)
# __.setting('require-pipe',True)
# __.setting('pre-error',False)
# __.setting('myFileLocations-skip-validation',False)
# __.setting('switch-raw',[])



_.appInfo[focus()] = {
	'file': 'printTable.py',
	'description': 'Print any table',
	'categories': [
						'tool',
						'research',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [
					'p printTable -i siteData_answerFile_auto_labels.json -long',
					'',
					'',
					'p printTable -long -i fileBackup.json -last 50 -c timestamp file backup + netblock_owner.json',
					'',
					'p printTable -long -i netblock_owner.json -c org ip -g org',
					'p printTable -long -i netblock_owner.json -c timezone org -g timezone',
					'p printTable -long -i netblock_owner.json -c timezone org ip -g timezone org',
					'',
					'',
					'netstat -n | - 127.0.0.1 | p cmd2table -print | p printTable -g State -c State Foreign_Address -long',
					'',
					'',
					'tasklist | p cmd2table -print | p printTable -s PID + .exe',
					'tasklist | p cmd2table -print -int Mem_Usage | p printTable -s Mem_Usage + .exe',
					'tasklist | p cmd2table -print | p printTable -s Mem_Usage + .exe -int Mem_Usage ',
					'tasklist | p cmd2table -print -int Mem_Usage | p printTable -g image_name -s image_name d.mem_usage -int mem_usage',
					'',
					'',
					'task -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb);"',
					'task -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb); mem=int(MEM_USAGE)" -s mem',
					'',
					''
	],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}
data=[]


if not sys.stdin.isatty():
	import simplejson
	pipe = sys.stdin.read()
	skipLoad = True
	data = simplejson.loads(pipe)
	_.switches.fieldSet( 'Input', 'active', True )

if _.switches.isActive('Input'):
	if not skipLoad:
		data = _.getTable2( _.switches.value('Input') )
if data:
	_.columnAbbreviations(data)

# _.pv(_.appInfo[focus()]['columns']); sys.exit();

# def int_trigger(data):
#   data = data.replace(' ', '_')
#   # data = data.replace('_', ' ')
#   return data

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
	_.defaultScriptTriggers()

	_.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Int',int_trigger)
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

_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
# START

def cleanData( data ):
	fields = []
	newFields = []
	for record in data:
		for key in record.keys():
			if not key in fields:
				fields.append( key )
	for i,record in enumerate(data):
		for key in fields:
			if not key in record.keys():
				record[key] = ''

		for key in record.keys():
			if ' ' in key:
				data[i][ key.replace( ' ', '_' ) ] = record[key]
				del data[i][key]

		

		for key in record.keys():
			if not key in newFields:
				newFields.append( key )
			# data[i][key] = str(record[key])
			# _.pr( key, record[key] )
			# _.pr( type( record[key] ), key )
	return data

def action():
	The_Totals = {}
	skipLoad = False
	global data

	if data:
		for i,record in enumerate(data):
			for key in record.keys():
				try:
					if not len(record[key]):
						data[i][key] = ''
				except Exception as e:
					pass


		if _.switches.isActive('JSON'):
			_.printVar1( data )
			sys.exit()


		keys = []
		if type( data ) == dict:
			data = [data]

		if not type( data ) == list:
			_.pr( 'Error: bad file' )
			sys.exit()
		else:
			try:
				for k in data[0].keys():
					keys.append( k )
			except Exception as e:
				_.pr( 'Error: bad file' )
				sys.exit()

		# here

		if not len( data ):
			_.pr( 'No data' )
			return False

		pass
		for i,rec in enumerate(data):
			for k in rec.keys():
				try:
					data[i][k] = int( data[i][k] )
				except Exception as e:
					pass



		# if _.switches.isActive('Int'):
		#   # _.pr( 'here' )
		#   d = []
		#   for i,rec in enumerate(data):
		#       for k in rec.keys():
		#           for y in _.switches.values('Int'):
		#               if k.lower() == y.lower():
		#                   try:
		#                       data[i][k] = int( data[i][k] )
		#                   except Exception as e:
		#                       d.append(i)

		#   if len(d):
		#       d.reverse()
		#       newData = []
		#       for i,r in enumerate(data):
		#           if not i in d:
		#               newData.append(r)
		#       data = newData

		if _.switches.isActive('Plus') or _.switches.isActive('Minus'):
			newData = []
			for i,r in enumerate(data):
				if _.showLine( str(r) ):
					newData.append(r)
			data = newData



		if _.switches.isActive('Int'):

			for i,rec in enumerate(data):
				for k in rec.keys():
					for num in _.switches.values('Int'):
						if num.lower().replace(' ','_') == k.lower().replace(' ','_'):
							cleaned = ''
							temp = str( data[i][k] )
							for xy in temp:
								if xy in '0123456789':
									cleaned+=xy
							if not len(cleaned):
								cleaned = '0'
							try:
								cleaned_int = int( cleaned )
								if not k in The_Totals:
									The_Totals[k] = 0
								The_Totals[k] += cleaned_int
								data[i][k] = cleaned_int
							except Exception as e:
								pass


		if _.switches.isActive('Last'):
			if 'timestamp' in data[0].keys():
				data = _.tables.returnSorted( 'data', 'd.timestamp', data )
				_.tables.fieldProfileSet( 'data', 'timestamp', 'trigger', _.resolveEpochTest )
			else:
				data.reverse()
			newData = []
			threshold = int( _.switches.value('Last') )
			for i,record in enumerate(data):
				if i <= threshold:
					if _.showLine( str(record) ):
						newData.append( record )
			pass

			_.pr()
			newData = cleanData( newData )

			_.tables.register('data',newData )
			_.tables.fieldProfileSet('data','field','alignment','right')
			# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
			if _.switches.isActive('Column'):
				_.tables.print( 'data', _.switches.value('Column') )
			else:
				_.tables.print( 'data', ','.join(keys) )

		else:

			_.pr()
			data = cleanData( data )
			_.tables.register('data',data )
			_.tables.fieldProfileSet('data','field','alignment','right')
			# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
			if _.switches.isActive('Column'):
				_.tables.print( 'data', _.switches.value('Column') )
			else:
				_.tables.print( 'data', ','.join(keys) )

	pass
	if len( The_Totals.keys() ):
		for k in The_Totals:
			txt = _.colorThis( k+':', 'green', p=0 )
			txt += '\t'
			txt += _.colorThis( _.addComma( The_Totals[k] ) , 'yellow', p=0 )
			_.pr( txt )

		# _.printVarSimple( data[0] )
########################################################################################
if __name__ == '__main__':
	action()







