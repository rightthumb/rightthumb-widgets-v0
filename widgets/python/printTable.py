#!/usr/bin/python3
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

	


_.appInfo[focus()] = {
	'file': 'printTable.py',
	'description': 'Print any table',
	'categories': [
						'tool',
						'research',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

_.appInfo[focus()]['examples'].append('p printTable -i siteData_answerFile_auto_labels.json  -long')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p printTable -long -i fileBackup.json -last 50 -c timestamp file backup + netblock_owner.json')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p printTable -long -i D:\\tech\\hosts\\MSI\\txt\\	1571025031.332114-2019_10_13-23_50_31-netblock_owner.json -c org ip -g org')
_.appInfo[focus()]['examples'].append('p printTable -long -i D:\\tech\\hosts\\MSI\\txt\\	1571025031.332114-2019_10_13-23_50_31-netblock_owner.json -c timezone org -g timezone')
_.appInfo[focus()]['examples'].append('p printTable -long -i D:\\tech\\hosts\\MSI\\txt\\	1571025031.332114-2019_10_13-23_50_31-netblock_owner.json -c timezone org ip -g timezone org')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('netstat -n | - 127.0.0.1  | p cmd2table -print | p printTable -g State -c State Foreign_Address -long')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('tasklist | p cmd2table -print | p printTable -s PID + .exe')
_.appInfo[focus()]['examples'].append('tasklist | p cmd2table -print -int Mem_Usage | p printTable -s Mem_Usage + .exe')
_.appInfo[focus()]['examples'].append('tasklist | p cmd2table -print | p printTable -s Mem_Usage + .exe -int Mem_Usage ')
_.appInfo[focus()]['examples'].append('tasklist | p cmd2table -print -int Mem_Usage | p printTable -g image_name -s image_name d.mem_usage -int mem_usage')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('tasklist | p cmd2table -print | p printTable -sort image_name - svchost -s image_name + .exe %*  ')
_.appInfo[focus()]['examples'].append('task -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb);"')
_.appInfo[focus()]['examples'].append('task -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb); mem=int(MEM_USAGE)" -s mem')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})

# def int_trigger(data):
# 	data = data.replace(' ', '_')
# 	# data = data.replace('_', ' ')
# 	return data

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
			# print( key, record[key] )
			# print( type( record[key] ), key )
	return data

def action():
	The_Totals = {}
	skipLoad = False
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		skipLoad = True
		# print( _.appData[__.appReg]['pipe'] )
		_.saveText( _.appData[__.appReg]['pipe'], _v.myTemp + _v.slash+'_printTable_temp.json' )
		data = _.getTable2( _v.myTemp + _v.slash+'_printTable_temp.json' )
		_.switches.fieldSet( 'Input', 'active', True )

	if _.switches.isActive('Input'):
		if not skipLoad:
			data = _.getTable2( _.switches.value('Input') )

		for i,record in enumerate(data):
			for key in record.keys():
				try:
					if not len(record[key]):
						data[i][key] = '-'
				except Exception as e:
					pass


		if _.switches.isActive('JSON'):
			_.printVar1( data )
			sys.exit()


		keys = []
		if type( data ) == dict:
			data = [data]

		if not type( data ) == list:
			print( 'Error: bad file' )
			sys.exit()
		else:
			try:
				for k in data[0].keys():
					keys.append( k )
			except Exception as e:
				print( 'Error: bad file' )
				sys.exit()

		# here

		if not len( data ):
			print( 'No data' )
			return False

		pass
		for i,rec in enumerate(data):
			for k in rec.keys():
				try:
					data[i][k] = int( data[i][k] )
				except Exception as e:
					pass



		# if _.switches.isActive('Int'):
		# 	# print( 'here' )
		# 	d = []
		# 	for i,rec in enumerate(data):
		# 		for k in rec.keys():
		# 			for y in _.switches.values('Int'):
		# 				if k.lower() == y.lower():
		# 					try:
		# 						data[i][k] = int( data[i][k] )
		# 					except Exception as e:
		# 						d.append(i)

		# 	if len(d):
		# 		d.reverse()
		# 		newData = []
		# 		for i,r in enumerate(data):
		# 			if not i in d:
		# 				newData.append(r)
		# 		data = newData

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

			print()
			newData = cleanData( newData )

			_.tables.register('data',newData )
			_.tables.fieldProfileSet('data','field','alignment','right')
			# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
			if _.switches.isActive('Column'):
				_.tables.print( 'data', _.switches.value('Column') )
			else:
				_.tables.print( 'data', ','.join(keys) )

		else:

			print()
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
			print( txt )

		# _.printVarSimple( data[0] )
########################################################################################
if __name__ == '__main__':
	action()




