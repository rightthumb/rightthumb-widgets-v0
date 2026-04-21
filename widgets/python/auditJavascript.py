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

# import os
import sys
# import simplejson as json
# from threading import Timer

import datetime
from datetime import datetime as dt, timedelta
import time

##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.json')
	



_.appInfo[focus()] = {
	'file': 'auditJavascript.py',
	'description': 'Process audit log of web dev project',
	'categories': [
						'audit',
						'javascript',
						'tool',
						'dev',
						'development',
				],
	'relatedapps': [
						'p jsAuditLog'
	],
	'prerequisite': [],
	'examples': [
						'p auditJavascript -f textOverflow_audit_log.json',
						'p auditJavascript -i textOverflow_audit_log.json  -g f'
	],
	'columns': [
					{ 'name': 'function', 'abbreviation': 'f' },
					{ 'name': 'action', 'abbreviation': 'a' },
					{ 'name': 'milliseconds', 'abbreviation': 'm' },
					{ 'name': 'seconds', 'abbreviation': 's' }
	]
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

# _.appInfo[focus()]['relatedapps'].append('p jsAuditLog')
# _.appInfo[focus()]['examples'].append('p auditJavascript -f textOverflow_audit_log.json')
# _.appInfo[focus()]['examples'].append('p auditJavascript -i textOverflow_audit_log.json  -g f')

# _.appInfo[focus()]['columns'].append({'name': 'function', 'abbreviation': 'f'})
# _.appInfo[focus()]['columns'].append({'name': 'action', 'abbreviation': 'a'})
# _.appInfo[focus()]['columns'].append({'name': 'milliseconds', 'abbreviation': 'm'})
# _.appInfo[focus()]['columns'].append({'name': 'seconds', 'abbreviation': 's'})



# _.printVar( _.appInfo[focus()] )
# sys.exit()




def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		_.argvProcess = True
		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()





def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in sys.stdin.readlines():
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')




_.appData[__.appReg]['pipe'] = ''
if not sys.stdin.isatty():
	_.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	pipeCleaner()



# os.path.isfile(files)
# os.system('cls')

# _.switches.isActive('_File_')
# global

# _.appInfo[focus()]['categories']

# #######################################
# uuidProject = { 'input': _.switches.value('Input'), 'note': 'sample' }
# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[__.appReg]['file'], 'project': uuidProject }
# _.genUUID(project='')
# _.genUUID('temp file')
# _.genUUID({'file':'app.py'})
# #######################################
# import blank
# blank.focus(focus())
# blank.registerSwitches()
# _.switches.fieldSet('Input','active','one')
# _.switches.fieldSet('Input','value','one')
# focus()
# #######################################

# _.switches.fieldSet('_File_','active',True)

# _.switches.dumpSwitches(includeBlank=False)

# _.tables.register('childClassItems',childItems)
# _.tables.print('childClassItems','name')
# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)

# backupLog = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )

# _mime.isText(file)
# _mime.isBinary(file)

# books = _.getText(_v.myTables + '\\bible_books.csv')
# _.saveText(convertedFile,'file.txt')

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START
# epoch = str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S'))
# epoch = str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(float(word)/1000.)    )  )

# datetime.datetime.fromtimestamp(float(word))
# time.gmtime(float(word)/1000.)

# seconds=(rcccc/1000)%60
# sec = int(seconds)


def action(data=False):
	if _.switches.isActive('Input') or not type(data) == bool:
		if not type(data) == bool:
			log = _.tables.returnSorted( 'auditJavascript', 'a.timestamp', data )
		else:
			log = _.tables.returnSorted( 'auditJavascript', 'a.timestamp', _.getTable2(_.switches.value('Input')) )

		data = {}
		if not len( log ):
			_.pr( 'No Data' )
			sys.exit()
		total = log[len(log)-1]['timestamp'] - log[0]['timestamp']
		theTotal = 'seconds: ' + str((total/1000)%60)
		# pause  = input('pause')

		for row in log:
			# _.pr(row.keys())
			# _.pr(  row['function'], row['action'] )
			try:
				data[row['uuid']].append(row)
			except Exception as e:
				data[row['uuid']] = []
				data[row['uuid']].append(row)

		report = {}

		last = 0
		for key in data.keys():
			# _.pr(key)
			last = 0
			for row in _.tables.returnSorted( 'auditJavascript', 'a.timestamp', data[key] ):
				if not last == 0:
					diff = row['timestamp'] - last
				else:
					diff = 0
				last = row['timestamp']
				if not 'start' in row['action']:
					# _.pr( row['timestamp'], '\t', diff, '\t',row['function'], '\t', row['action'].replace('end ','').replace('end','') )
					nm = row['function'] + '__' + row['action'].replace('end ','').replace('end','').replace('  ',' ').replace(' ','_')
					try:
						report[nm].append(diff)
					except Exception as e:
						report[nm] = []
						report[nm].append(diff)

		logReport = []
		for key in report.keys():
			logReport.append( {'function': key.split('__')[0], 'action': key.split('__')[1].replace('_',' '), 'milliseconds': sum(report[key]), 'seconds': (sum(report[key])/1000)%60} )

			# _.pr(key,'\tmilliseconds:',sum(report[key]),'\tseconds:',)

		_.pr()
		_.tables.register('auditJavascriptReport',logReport)
		_.tables.print('auditJavascriptReport','function,action,milliseconds,seconds')

		_.pr()
		_.pr()

		
		_.pr('algorithm total:')
		_.pr('\t\t',theTotal)
		_.pr()
		_.pr()
		


##############################################

#             put this in javascript

# family.v.auditOverflow.push( { 'action': 'start', 'function': 'textOverflowStart', 'timestamp': (new Date).getTime(), 'uuid': '' } );

##############################################


# auditJavascript
########################################################################################
if __name__ == '__main__':
	action()