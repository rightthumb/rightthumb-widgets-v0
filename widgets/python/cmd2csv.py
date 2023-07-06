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



	# _.printVar( _dir.fileInfo( path ) )
##################################################

def appSwitches():
	pass
	_.switches.register( 'NoLabels', '-nl,-nolabel,-nolabels' )
	_.switches.register( 'Save', '-save', 'file.json' )
	_.switches.register( 'Print', '-print' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'cmd2table.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'CMD output to table',
	'categories': [
						'tool',
						'format',
						'data',
						'cmd',
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
						'netstat | p cmd2table',
						'',
						'p dirX -tp *;l --c -c s p -r -long | p cmd2table',
						'',
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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
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

table = {}
"""
def preProcess2( row ):
	global table
	for i,r in enumerate(row):
		if len(r):
			r = r.replace('\t',' ')
			if r == ' ':
				table[i] += 1
"""

def preProcess( row ):
	global data
	global table
	global fields
	global theIs
	global startOnLine
	fields = {}
	theIs = []
	# row = row.replace('\t',' ')
	

	for di,row in enumerate(data):
		original = row
		row = _str.cleanBE(row,' ')
		row = row.replace( '  ', '\t' )
		row = _str.replaceDuplicate(row,'\t')
		if '\t' in row:
			columns = row.split('\t')
			for i,column in enumerate(columns):
				column = _str.cleanBE(column,' ')
				columns[i] = column
			# _.pr(columns)
			for i,column in enumerate(columns):
				fields[i] = column.replace( ' ', '_' )
				table[ original.index(column) ] += 1
				x = original[ original.index(column) ]
				theIs.append( original.index(column) )
				# _.pr(x)
			# sys.exit()
			startOnLine = di
			break



def process():
	global table
	global data
	global delim
	global totalRows
	global threshold
	global fields
	global theIs
	global startOnLine

	# threshold = 50
	# threshold = 80
	# _.printVar( table )
	
	# _.pr()
	# _.pr(totalRows)
	# _.pr()
	# pause()

	records = []
	
	for di,row in enumerate(data):
		record = []
		build = ''
		pastClose = False
		lastBlank = False

		past = -1
		row2 = row.replace('\t',' ')
		row2 = _str.cleanBE(row2,' ')
		count = 0
		first = True
		theLast = None
		if len(row2):
			for i,r in enumerate(row):
				shouldRun = False


				if table[i]:
					if theLast is None and count > 0:
						shouldRun = True
					count+=1
					if first:
						first = False
					else:
						past+=1
						pastClose = True

				if lastBlank and not r == ' ':
					shouldRun = True

				if r == ' ':
					lastBlank = True



				if shouldRun:
					# _.pr( build  )
					if pastClose:
						if len( build ) > 1:

							if past > 0 and not len(record) == count-1:
							# if not len(record) == count-1:
								# past = count-1 - len(record)
								while not past == 0:
									past-=1
									record.append('')

							past = -1
							pastClose = False
							build = _str.replaceDuplicate(build,' ')
							build = _str.cleanBE(build,' ')
							record.append( build )
							build = ''

				build+=r
				if not r == ' ':
					lastBlank = False

			if len(build):
				build = _str.replaceDuplicate(build,' ')
				build = _str.cleanBE(build,' ')
				record.append( build )
			if len(record) < len(list(fields.keys())):
				past = len(list(fields.keys())) - len(record)
				while not past == 0:
					past-=1
					record.append('')
			if not record[0] == fields[0]:
				if di > startOnLine:
					records.append(record)
				# _.pr(record)
	pass
	lengths = {}
	for record in records:
		lengths[ len(record) ] = 0
	for record in records:
		lengths[ len(record) ] += 1
	maxTables = 0
	for key in lengths.keys():
		if lengths[key] > maxTables:
			maxTables = int(key)
		# p = _.pDiff( , len(records), 'l' )
	if  _.switches.isActive('NoLabels'):
		newRecords = records
	if not _.switches.isActive('NoLabels'):
		newRecords = []
		keys = {}
		first = True
		for record in records:
			if len(record) == len(list(fields.keys())):
				newRec = {}
				for i, column in enumerate(record):
					newRec[ fields[i] ] = column
				newRecords.append( newRec )
			else:
				_.pr( len(record),record )



	pass
	# if not _.switches.isActive('Save') or not len(_.switches.value('Save')):
	#     if not _.switches.isActive('Print'):
	#         for record in newRecords:
	#             _.pr( record )
	return newRecords
	# _.pr( len(records), len(newRecords) )



"""
def postProcess():
	global table
	global data
	global delim
	global threshold
	_.printVar( table )
	_.pr()
	_.pr(len(data))
	_.pr()
	
	records = []
	
	for row in data:
		record = []
		build = ''
		hadBreak = False
		pastClose = False
		for i,r in enumerate(row):
			if len(r):
				r = r.replace('\t',' ')
				if r == ' ':
					if len(build) and not hadBreak:
						p = _.pDiff( table[i]+1, len(data)+1, 'l' )
						if pastClose or p >= threshold:
							hadBreak = True
							pastClose = False
							record.append( build )
							build = ''

					
				else:
					build+=r
					hadBreak = False
					p = _.pDiff( table[i]+1, len(data)+1, 'l' )
					if p >= threshold:
						pastClose = True
		pass
		if len(build):
			record.append( build )
		records.append(record)
	pass
	lengths = {}
	for record in records:
		lengths[ len(record) ] = 0
	for record in records:
		lengths[ len(record) ] += 1
	maxTables = 0
	for key in lengths.keys():
		if lengths[key] > maxTables:
			maxTables = int(key)
		# p = _.pDiff( , len(records), 'l' )
	if not _.switches.isActive('Labels'):
		newRecords = records
	if _.switches.isActive('Labels'):
		newRecords = []
		keys = {}
		first = True
		for record in records:
			_.pr( len(record), maxTables )
			if first:
				if len(record) == maxTables:
					first = False
					for i, column in enumerate(record):
						keys[i] = column

			else:
				if len(record) == maxTables:
					newRec = {}
					for i, column in enumerate(record):
						newRec[ keys[i] ] = column
					newRecords.append( newRec )

	pass
	for record in newRecords:
		_.pr( record )
"""



def action():
	# _.pr( 'Change to, if last was space' )
	# sys.exit()
	global table
	global data
	global totalRows
	load()


	for row in data:
		row = row.replace('\t',' ')
		row = _str.cleanBE(row,' ')
		if len(row):
			totalRows += 1

	for row in data:
		for i,r in enumerate(row):
			table[i] = 0

	preProcess( row )
	records = process()

	if len(records):
		keys = list( records[0].keys() )

	_.pr( ','.join(keys) )
	for record in records:
		r = []
		for key in keys:
			r.append( record[key] )
		_.pr( ','.join(r) )

	# _.printVarSimple( records )    

	# if _.switches.isActive('Save') and len(_.switches.value('Save')):
	#     _.saveTable2( records, _.switches.values('Save')[0] )
	# elif _.switches.isActive('Print'):
	#     _.printVarSimple( records )


def load():
	global data
	data = None
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		data = _.appData[__.appReg]['pipe']


data = []
delim = ','
threshold = 80
totalRows = 0
########################################################################################
if __name__ == '__main__':
	action()







