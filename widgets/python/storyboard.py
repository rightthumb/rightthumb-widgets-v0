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
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )
##################################################
from operator import itemgetter
##################################################


def appSwitches():
	_.switches.register('Project', '-p,-project')
	_.switches.register('Report', '-r,-report')
	_.switches.register('Child', '-child')
	_.switches.register('All', '-all')
	_.switches.register('Fields', '-fields')
	_.switches.register('Ask', '-ask')
	_.switches.register('AnswerFile', '-answerfile')
	_.switches.register('If', '-if')
	



_.appInfo[focus()] = {
	'file': 'storyboard.py',
	'description': 'Storyboards paths from config files',
	'categories': [
						'app',
						'programming',
						'tool',
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

_.appInfo[focus()]['relatedapps'].append('p storyboard_old ?')

_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p storyboard ')
_.appInfo[focus()]['examples'].append('p storyboard -r characters')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p storyboard -r characters -answerfile %myTables%\\storyboard_answerFile.txt')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p storyboard -r characters -project validator -answerfile %myTables%\\storyboard_answerFile_auto.txt ')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p storyboard -r characters -project validator -answerfile %myTables%\\storyboard_answerFile_auto_all.txt ')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('previously blank22 ')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p storyboard -r characters -project validator -if')
_.appInfo[focus()]['examples'].append('')

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
	_.defaultScriptTriggers()

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = True

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
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
if not sys.stdin.isatty():
	_.setPipeData( sys.stdin.readlines() )
	# _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



########################################################################################
# START

def cleanTypeString( data ):
	dt = type( data )
	ds = str( dt )
	ds = ds.replace( "<class '", '' ).replace( "'>", '' ).replace( ' ','' )
	return ds

def auditType( data ):
	result = cleanTypeString( data )
	if type( data ) == list and len( data ) :
		if type( data[0] ) == dict:
			result = 'child'
	return result

def findGroups( records ):
	global configID
	paths = []
	cntK = {}
	
	configurations = []
	for rec in records:
		try:
			type( cntK[str(rec)] )
			cntK[str(rec)] += 1
		except Exception as e:
			cntK[str(rec)] = 1
			pid = newID()
			paths.append({ 'cnt': 0, 'pid': pid, 'rec': rec })
			n = {}
			n['pid'] = pid
			n['gid'] = configID
			n['cnt'] = 0
			for k in rec.keys():
				n[k] = rec[k]
			configurations.append( n )
			

	print_records = []
	custom_sort = []
	for i,rec in enumerate(paths):
		paths[i]['cnt'] = cntK[str(paths[i]['rec'])]
		print_records.append({ 'cnt': paths[i]['cnt'], 'rec': str(paths[i]['rec']) })
		for ii,conf in enumerate(configurations):
			if conf['pid'] == rec['pid']:
				configurations[ii]['cnt'] = paths[i]['cnt']

	_.switches.fieldSet( 'Long', 'active', True )
	_.pr()

	if len( configurations ) > 0:
		_.tables.register('data',configurations)
		_.tables.print('data', ','.join( configurations[0].keys() ) )
		# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
	else:
		_.pr( 'Error: configurations == 0' )
		_.pr( paths )
	configID+=1
	return configurations



def report( configFile, parentIn='', fieldsIn='', allFields=False ):
	if _.switches.isActive('All'):
		allFields = True
	_.pr()
	_.pr( 'Report:', parentIn )
	_.pr()
	keyList = {}
	cKeyList = {}
	records = []
	children = []
	parentFields = []
	childrenFields = []
	fieldsSpecified = False
	if not fieldsIn == '':
		fieldsSpecified = True
		fieldsIn = fieldsIn.lower()
		fieldList = fieldsIn.split(',')


	# find children
	for config in configFile:
		for label in config.keys():
			# _.pr( label )
			keyList[label] = auditType( configFile[0][label] )
			if keyList[label] == 'child':
				if not label in children:
					children.append( label )
						
			elif not label == 'id' and not label in parentFields:
				parentFields.append( label )

	# find fields
	for label in configFile[0].keys():
		keyList[label] = auditType( configFile[0][label] )
		if not keyList[label] == 'child':
			if fieldsSpecified:
				shouldProcess = False
				if label.lower() in fieldList:
					shouldProcess = True
			else:
				if label == 'id':
					shouldProcess = False
				else:
					shouldProcess = True
			if shouldProcess:
				cKeyList[label] = cleanTypeString( configFile[0][label] )
				# _.pr( fieldsSpecified, label, cKeyList[label] )

	# check for changes 
	for config in configFile:

		for label in cKeyList.keys():

			try:
				dt = cleanTypeString( config[label] )
			except Exception as e:
				_.pr( 'Error: key', label )
				# _.pr( config )


			# _.pr( label, dt )
			try:
				if type( cKeyList[label] ) == str or type( cKeyList[label] ) == list:
					error = False
				else:
					error = True
			except Exception as e:
				error = True
			
			if error:
				_.pr('Error: field')
				sys.exit()


			# _.pr( label, cKeyList[label] )


			if type( cKeyList[label] ) == list and not dt in cKeyList[label]:
				cKeyList[label].append( dt )
			if type( cKeyList[label] ) == str and not dt == cKeyList[label]:
				# _.pr( 'HERE' )
				tmp = cKeyList[label]
				cKeyList[label] = []
				cKeyList[label].append( tmp )
				cKeyList[label].append( dt )


	# _.pr( cKeyList )
	keyList = {}

	for config in configFile:
		rec = {}
		for label in cKeyList.keys():
			# _.pr( label )
			if type(cKeyList[label]) == list:
				rec[label] = cleanTypeString( config[label] )
			elif cKeyList[label] == 'list':
				if len(config[label]) == 0:
					rec[label] = '0'
				else:
					rec[label] = '1+'
			elif cKeyList[label] == 'int':
				rec[label] = cKeyList[label]
			else:
				rec[label] = str(cKeyList[label])+'*'

		records.append( rec )
	# _.pr( records )
	
	# global settings
	settings = findGroups( records )
	if not fieldsIn == '':
		for b in settings:
			_.pr( b )
	# if fieldsIn == '':
	storyboard = {}

	if not fieldsIn == '':
		if len( storyboard.keys() ) == 0:
			storyboard = { 'pid': newID(), 'name': parentIn }
		if not fieldsIn == '':
			storyboard['settings'] = settings


	# global fields
	fields = ''
	# while not 'endall' in fields:
	#     if not 'endall' in fields:
	while not fields == 'x' and not 'endall' in fields:
		_.pr(  )
		_.pr(  )


		if  allFields:
			_.pr( ','.join( parentFields ) )
		# else:
		fields = answer( ' What fields? ' )
		if not fields == 'x' and not fields == 'b' and not 'endall' in fields:
			_.pr( 'fields:', fields )
			if fieldsIn == '':
				storyboard = {}
			if len( storyboard.keys() ) == 0:
				storyboard = { 'pid': newID(), 'name': parentIn }
			if not fieldsIn == '':
				storyboard['settings'] = settings
			failtype = answer( ' Fail type (h,s,field)? ' )
			storyboard['fail'] = failtype
			failField = ''
			if 'f' == failtype:
				failField = answer( ' Field? ' )
				storyboard['fail_field'] = failField.lower()
			reportData = report( configFile, parentIn, fields )
			_.pr( 'reportData:', sys.getsizeof( str(reportData) ), len( reportData.keys() ) )
			# sys.exit()
			# if sys.getsizeof( str(reportData) ) > 5:
			if len( reportData.keys() ) > 0:
				try:
					storyboard['groups'].append( reportData )
				except Exception as e:
					storyboard['groups'] = []
					storyboard['groups'].append( reportData )
		if 'endall' in fields:
			return storyboard
		else:
			childrenRecords = {}
			if not len( children ) > 0:
				return storyboard
			else:
				
				for child in children:
					childrenRecords[child] = []

					for config in configFile:
						for ch in config[child]:
							childrenRecords[child].append( ch )

					# if  allFields:
					#     for label in childrenRecords[child][0].keys():
					#         if not label == 'id' and not label in childrenFields:
					#             childrenFields.append( label )
					#     childfields = ','.join( childrenFields )
					#     reportData = report( childrenRecords[child], child, fieldsIn=childfields )
					# else:
					reportData = report( childrenRecords[child], child )
					# if sys.getsizeof( str(reportData) ) > 5:
					if len( reportData.keys() ) > 0:
						try:
							storyboard['children'].append( reportData )
						except Exception as e:
							storyboard['children'] = []
							storyboard['children'].append( reportData )

				return storyboard

def answer( text ):
	global answerID
	global answerFile
	global fields

	if _.switches.isActive('AnswerFile'):
		_.pr( answerID )
		try:
			theAnswer = answerFile[answerID].replace( '\n', '' )
			answerID += 1
			_.pr(  )
			_.pr( 'text:', text, 'answer:', theAnswer )
		except Exception as e:
			_.pr( 'Error: answerFile' )
			_.pr( answerID )
			_.pr( 'text:', text )
			sys.exit()
	else:
		theAnswer = input( text )
		answerFile.append( theAnswer )
		
	return theAnswer



def action():
	if _.switches.isActive('If'):
		if not _.switches.isActive('Project'):
			_.pr( 'Error: please specify a project' )
			sys.exit()
		project = _.switches.value('Project')
		config = _.getTable( 'storyboard_' + project + '.json' )

		for key in config[project].keys():
			processKeyIf( config[project][key], key )

		sys.exit()

	global configFile
	global answerFile
	global results
	global attributesTable

	project = _.switches.value('Project')
	results = {}
	results[ project ] = {}


	for config in configFile.keys():
		if not config == 'type':
			reportData = report( configFile[config], parentIn=config, fieldsIn='' )
			# results.append( reportData )
			results[ project ][config] = reportData

	_.pr()
	_.pr()
	_.pr()
	_.pr( _.d2json(results) )
	# _.copyDicAsJSON( results, openUML=True )
	_.setUmlData( results )

	if not _.switches.isActive('AnswerFile'):
		if _.switches.isActive('All'):
			answerBackup = _v.myTables + _v.slash+'storyboard_answerFile_auto_all.txt'
		else:
			answerBackup = _v.myTables + _v.slash+'storyboard_answerFile_auto.txt'

		_.saveText( answerFile, answerBackup )
		_.pr()
		_.pr( answerBackup )
	_.saveTable( results, 'storyboard_' + project + '.json', printThis=True )
	_.pr()
	_.pr()
	_.pr()

	surfData( results[ project ], [], parent=True )
	_.pr()
	_.pr()
	_.pr()

	# _.pr( 'attributesTable:', len(attributesTable), ','.join( attributesTable[0].keys() ) )
	
	_.pr()
	_.pr()
	# for a in attributesTable:
	#     _.pr( a )
	for key in attributesTable.keys():
		# _.pr( key )
		_.pr()
		_.pr()
		_.pr( '_____________________________________XX_____________________________________' )
		_.pr()
		_.pr()
		_.tables.register( 'data', attributesTable[ key ] )
		_.tables.print('data', ','.join( attributesTable[ key ][0].keys() ) )
		



def surfData( data, path, parent=False ):
	# _.pr()
	if parent:
		path=[]

	if type( data ) == dict:
		hasName = False
		hasGroups = False
		hasSettings = False
		hasChildren = False
		for key in data.keys():
			if parent:
				path=[]
			# _.pr( 'key:', key )
			if key == 'children':
				hasChildren = True
			if key == 'settings':
				hasSettings = True
			if key == 'groups':
				hasGroups = True
			if key == 'name':
				hasName=True
				path2 = papp( path, data[ key ] )


		for key in implode( data, parent ).split(','):
			if parent:
				path=[]
			if not hasName:
				path2 = path
			pass
			# _.pr( type(path), path, path2 )
			# _.pr( 'hasPID:', path2, hasPID( data[ key ] ) )
			# _.pr( 'auditType:', auditType( data[ key ] ) )

			# if hasPID( data[ key ] ):
			#     addAttributes( data[ key ], path2 )


		if hasGroups:
			pass
			# _.pr( 'hasGroups:', hasGroups)
			# path3 = papp( path2, 'groups')
			path3 = path2
			# addAttributes( data[ 'groups' ], path3 )
			surfData( data[ 'groups' ], path3 )

		if hasSettings:
			# _.pr( 'hasSettings:', hasSettings)
			# path3 = papp( path2, 'settings')
			path3 = path2
			addAttributes( data[ 'settings' ], path3 )
			# surfData( data[ 'settings' ], path3 )

		if hasChildren:
			# _.pr( 'hasChildren:', hasChildren)
			# path3 = papp( path2, 'children')
			path3 = path2
			# addAttributes( data[ 'children' ], path3 )
			# addAttributes( data[ 'children' ], path3 )
			surfData( data[ 'children' ], path3 )


		# if hasPID( data):
		#     addAttributes( data, path2 )
		# _.pr( 'implode:', implode( data ).split(',') )
		for key in implode( data ).split(','):
			if parent:
				path=[]
			surfData( data[ key ], path )

	if type( data ) == list:
		for d in data:
			surfData( d, path )

def papp( data, addText, parent=False ):
	global omitParent
	shouldRun = True

	if addText in data:
		shouldRun = False
	
	if addText in omitParent:
		if addText in data:
			shouldRun = False

	if shouldRun:
		if not type( addText ) == str:
			_.pr( 'papp:', addText )
		if not len( data ):
			data.append( addText )
		else:    
			if not data[ len(data)-1 ] == addText and not data[ len(data)-2 ] == addText:
				data.append( addText )


	return data


def implode( data, parent=False ):
	global omitParent
	omit = ['groups','settings','children']
	n = []
	try:
		for d in data.keys():
			if not d in omit :
				n.append( d )
	except Exception as e:
		try:
			for d in data[0].keys():
				if not d in omit:
					n.append( d )
		except Exception as e:
			_.pr( 'Error: implode' )
			_.pr( data )
			sys.exit()
	if parent:
		omitParent = n
	return ','.join( n )


def implode2( data, parent=False ):
	global omitParent
	omit = ['groups','settings','children']
	n = []
	try:
		for d in data.keys():
			if not d in omit :
				if not type(data[d]) == list and not type(data[d]) == dict:
					n.append( d )
	except Exception as e:
		try:
			for d in data[0].keys():
				if not d in omit:
					if not type(data[d]) == list and not type(data[d]) == dict:
						n.append( d )
		except Exception as e:
			_.pr( 'Error: implode' )
			_.pr( data )
			sys.exit()
	if parent:
		omitParent = n
	return ','.join( n )


def addAttributes( data, path ):
	global attributesTable



	_.pr()
	_.pr( '____________________________________________________________________________' )
	try:
		_.pr( 'Path:', ','.join( path ) )
	except Exception as e:
		_.pr( 'Path:', path )


	# _.pr( ','.join( path ) )
	if len( data ) > 0:
		_.pr()
		_.pr()
		try:


			if type(data) == list:
				# _.pr( 'implode:', implode2( data[0] ) )
				_.tables.register( 'data', data )
				_.tables.print('data', implode( data[0] ) )

			if type(data) == dict:
				# _.pr( 'implode:', implode2( data ) )
				_.tables.register( 'data', [data] )
				_.tables.print('data', implode2( data ) )


		except Exception as e:
			_.pr( 'Error: attributes' )
			_.pr( type(data) )
			_.pr( implode2( data ) )
			_.pr( data )
			sys.exit()
	n = '-'.join( data[0].keys() ) + '_' +  '-'.join( path )
	attributesTable[ n ] = []
	for d in data:
		x = d
		x['xpath'] = '-'.join( path )
		attributesTable[ n ].append( x )

def hasPID( row ):
	try:
		if type( row['pid'] ) == int:
			return True
		else:
			return False
	except Exception as e:
		return False

def theTree( data ):
	auditType


def newID():
	global recordID
	recordID += 1
	return recordID


def processKeyIf( data, label ):
	_.pr( '#########################################' )
	_.pr()
	_.pr( '# ' + data['name'] )
	_.pr()
	_.pr( 'for row in config[\'' + label + '\']:' )
	if data['fail'] == 'f':
		data['fail'] = data['fail_field']
	processGroupIf( data['groups'], data['fail'], 'row', 1 )
	


def processGroupIf( data, fail, label, tabs ):
	for i,row in enumerate(data):
		keys = []

		for key in row.keys():
			keys.append( key )

		if 'fail' in keys:
			if data[i]['fail'] == 'f':
				fail = data[i]['fail_field']
			else:
				fail = data[i]['fail']

		if 'settings' in keys:
			processSettingsIf( data[i]['settings'], fail, label, tabs )
		
		if 'groups' in keys:
			processGroupIf( data[i]['groups'], fail, label, tabs )

		if 'children' in keys:
			processChildrenIf( data[i]['children'], fail, label, tabs )


def processSettingsIf( data, fail, label, tabs ):
	def f( fld ):
		return label+'[\'' + fld + '\']'
	# return ''
	omit = ['pid','gid','cnt']
	# _.pr()
	# _.pr( addTabs( tabs ) + '# Settings:' )
	for row in data:
		statement = []
		for key in row.keys():
			if not key in omit:
				if row[key] == 'str*':
					task =  f(key) + ' == test' 
				elif row[key] == 'bool*':
					task = f(key)
				elif row[key] == '0' or row[key] == '1+':
					task = 'len(' + f(key) + ')'
				elif not '*' in row[key]:
					task = 'not type(' + f(key) + ') == bool'
				else:
					task = 'Error: ' + key + ' ' + row[key]
				statement.append( task )
				_.pr( addTabs( tabs ) + 'if ' + ' and '.join( statement ) + ':')
				# _.pr( addTabs( tabs ) + task )
				# _.pr( addTabs( tabs ) + key, row[key], type(row[key]) )


def processChildrenIf( data, fail, label, tabs ):
	# return ''
	_.pr()
	_.pr( addTabs( tabs ) + '# Children:' )
	for i,row in enumerate(data):
		keys = []

		for key in row.keys():
			keys.append( key )

		nLabel = label+'_c'
		_.pr( addTabs( tabs ) + 'for '+nLabel+' in '+label+'[\'' + data[i]['name'] + '\']:' )


		label = nLabel
		tabs += 1
		if 'fail' in keys:
			if data[i]['fail'] == 'f':
				fail = data[i]['fail_field']
			else:
				fail = data[i]['fail']

		if 'settings' in keys:
			processSettingsIf( data[i]['settings'], fail, label, tabs )
		
		if 'groups' in keys:
			processGroupIf( data[i]['groups'], fail, label, tabs )

		if 'children' in keys:
			processChildrenIf( data[i]['children'], fail, label, tabs )


def addTabs( tabs ):
	result = ''
	i = 0
	while not i == tabs:
		result += '    '
		i+=1
	return result

attributesTable = {}

recordID = 0
configID = 0
configFile = _.getTable('auditCodeBase.json')

omitParent = []
answerFile = []
if _.switches.isActive('AnswerFile'):
	answerFile = _.getText( _.switches.value('AnswerFile') )
answerID = 0
########################################################################################
if __name__ == '__main__':
	action()


# storyboard

# findGroups


# p storyboard -r characters
# CHAR
# h
# x
# GROUPID,IS
# h
# x
# x







