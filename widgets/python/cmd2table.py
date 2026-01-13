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
	_.switches.register( 'FixCol', '-fc,-fix,-fixcol,-col' )
	_.switches.register( 'Int', '-int', 'Mem_Usage' )
	_.switches.register( 'Make', '-make', "rename '{name}' '{file}'" )
	_.switches.register( 'Settings', '-settings', "{'quote':1}" )
	_.switches.register( 'App', '-app', "df" )
	_.switches.register( 'Netstat', '-n,-p,-ports,-netstat' )


	_.switches.register( 'Underline', '-u,-under,-underline', '=' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False



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
						'netstat -n | - 127.0.0.1  | p cmd2table -print | p printTable -g State -c State Foreign_Address -long',
						'',
						'tasklist | p cmd2table -print | p printTable -s PID + .exe',
						'tasklist | p cmd2table -print -int Mem_Usage | p printTable -s Mem_Usage + .exe',
						'tasklist | p cmd2table -print | p printTable -s Mem_Usage + .exe -int Mem_Usage ',
						'tasklist | p cmd2table -print -int Mem_Usage | p printTable -g image_name -s image_name d.mem_usage -int mem_usage',
						'',
						'',
						'p ls -movietitle -c n tf -table header;left --c | p cmd2table -make rename \'{name}\' \'{file}\' -settings quote',
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

def int_trigger(data):
	data = data.replace(' ', '_')
	return data

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
	_.switches.trigger( 'Int', int_trigger )
	
	
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

def colSearch( row ):
	global uData
	if not _.switches.isActive('Underline'):
		return preProcess( row )



	global data
	global table
	global fields
	global theIs
	global startOnLine
	fields = {}
	theIs = []

	spacing = None
	for i,r in enumerate(data):
		if _.switches.value('Underline')+_.switches.value('Underline')+_.switches.value('Underline') in r:
			spacing = i
	if spacing is None and len(data):
		preProcess( row )
	elif not len( data ):
		_.colorThis( 'No Data', 'red' )
	else:
		indexA =  []
		indexB =  []
		indexBreaks =  []

		for i,x in enumerate(data[spacing]):
			if not x == ' ':
				indexB.append( i )
			else:
				indexBreaks.append(i)
				indexA.append( indexB )
				indexB = []
		if len(indexB):
			indexA.append( indexB )

		started = False
		preFields =  []
		indexB =  []

		for i,x in enumerate(data[spacing-1]):
			# _.pr(x)
			if not x == ' ' or started:
				started = True
				indexB.append( x )
				# _.pr( indexB )
			if i in indexBreaks:
				started = False
				cleaned = _str.cleanBE(''.join(indexB),' ')
				preFields.append( cleaned )
				indexB = []

		if len(indexB):
			cleaned = _str.cleanBE(''.join(indexB),' ')
			preFields.append( cleaned )
		
		for i,pf in enumerate(preFields):
			for x in indexA[i]:
				fields[x] = pf.replace( ' ', '_' )

		for row in data:
			for i,y in enumerate(row):
				if not i in fields:
					fields[i] = preFields[ len(preFields)-1 ]
		

		# _.printTest( fields )
		startOnLine = spacing+1


		uData = []
		for iD,row in enumerate(data):
			started = False
			record = {}
			indexB = []
			if iD >= startOnLine:
				for i,x in enumerate( row ):
					# _.pr(x)
					if not x == ' ' or started:
						started = True
						indexB.append( x )
						# _.pr( indexB )
					if i in indexBreaks:
						started = False
						cleaned = _str.cleanBE(''.join(indexB),' ')
						record[fields[i-1]] = cleaned
						indexB = []
				if len(indexB):
					cleaned = _str.cleanBE(''.join(indexB),' ')
					record[fields[i-1]] = cleaned
				uData.append( record )
				# _.printTest( record )



		# _.pr(preFields)
		# sys.exit()


		# _.pr( 'found column spacing' )
		# sys.exit()



def preProcess( row ):
	_.switches.fieldSet( 'Underline', 'active', False )
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
		for x in _.switches.values('FixCol'):
			for y in _.caseUnspecific( row, x ):
				row = row.replace( y+' ', y+'\t' )

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
	global uData
	if _.switches.isActive('Underline'):
		return uData
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
	if not _.switches.isActive('Save') or not len(_.switches.value('Save')):
		if not _.switches.isActive('Print') and not _.switches.isActive('Make'):
			for record in newRecords:
				_.pr( record )
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

	if _.switches.isActive('Netstat'):
		records = parse_netstat_output(data)
		recs=[]
		for rec in records:
			if _.showLine(str(rec)):
				recs.append(rec)
		_.pt(recs)
		return records

	else:
		for row in data:
			row = row.replace('\t',' ')
			row = _str.cleanBE(row,' ')
			if len(row):
				totalRows += 1

		for row in data:
			for i,r in enumerate(row):
				table[i] = 0

		colSearch( row )
		# preProcess( row )

		records = process()

	for i,rec in enumerate(records):
		for k in rec.keys():
			try:
				records[i][k] = int( records[i][k] )
			except Exception as e:
				pass
	if _.switches.isActive('Int'):

		for i,rec in enumerate(records):
			for k in rec.keys():
				for num in _.switches.values('Int'):
					if num.lower() == k.lower():
						# _.pr(k)
						cleaned = ''
						temp = str( records[i][k] )
						for xy in temp:
							if xy in '0123456789':
								cleaned+=xy

						if not len(cleaned):
							cleaned='0'
						try:
							records[i][k] = int( cleaned )
						except Exception as e:
							pass
						records[i][k]=int(cleaned)
						# _.pr(cleaned)
						# sys.exit()



	if _.switches.isActive('Save') and len(_.switches.value('Save')):
		_.saveTable2( records, _.switches.values('Save')[0] )
	elif _.switches.isActive('Print'):
		_.printVarSimple( records )
	
	settings = {}
	if _.switches.isActive('Settings'):
		x = ' '.join(  _.switches.values('Settings')  )
		dic = None
		key = None
		try:
			dic = eval(x)
		except Exception as e:
			key = x
		if not dic is None:
			for k in dic:
				settings[k.lower()] = dic[k]
		
		if not key is None:
			settings[key.lower()] = None


	if _.switches.isActive('Make'):
		m = ' '.join(  _.switches.values('Make')  )
		result = []
		if len( records ):
			for record in records:
				mm = m
				isValid = True
				for key in record:
					for string in _.caseUnspecific( m, '{'+key+'}' ):
						ran = True
						if not len(record[key]):
							isValid = False
						mm = mm.replace( string, record[key] )
				if isValid and ran:
					result.append(mm)
		for rec in result:
			if 'quote' in settings:
				rec = rec.replace( "'", '"' )
			_.pr( rec )


def get_command_output(cmd):
	import subprocess
	process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, _ = process.communicate()
	return output.decode()

def parse_netstat_output(output):
	import re
	lines = output.split("\n")
	keys = ["Proto", "Local", "Foreign", "State", "PID/Program name"]
	data = []

	for line in lines[2:]:
		line = line.strip()
		if line:
			# Replace multiple spaces with a single space
			line = re.sub(r'\s+', ' ', line)
			values = line.split(" ")
			entry = {keys[i]: values[i] if i < len(values) else '' for i in range(len(keys))}
			data.append(entry)

	for rec in data:
		p=rec['State']
		while '::' in p: p=p.replace('::',':')
		if ':' in p:
			pp=p.split(':')
			if len(pp) > 1:
				rec['Port']=int(pp[-1])
		if not 'Port' in rec: rec['Port']=''

	return data

def load():
	global data
	data = None

	if _.switches.isActive('Netstat'):
		_.pr('netstat -tulanp',c='green')
		data = get_command_output('netstat -tulanp')
		return data

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		data = _.appData[__.appReg]['pipe']


	not_alphanumeric = []
	for row in data:
		for char in row:
			if not char in _str.alphanumeric:
				if not char in not_alphanumeric:
					not_alphanumeric.append(char)

	for row in data:
		for x in not_alphanumeric:
			if x+x+x in row:
				_.switches.fieldSet( 'Underline', 'active', True )
				_.switches.fieldSet( 'Underline', 'value', x )
				_.switches.fieldSet( 'Underline', 'values', [x] )





data = []
delim = ','
threshold = 80
totalRows = 0
uData = []
########################################################################################
if __name__ == '__main__':
	action()