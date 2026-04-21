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
##################################################

def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Search', '-search' )
	_.switches.register( 'Fields', '-field,-fields' )
	_.switches.register( 'One', '-one' )
	_.switches.register( 'Spaces', '-space,-spaces,-spaceing,-spacing', '0 fields' )
	_.switches.register( 'Lines', '-lines' )
	_.switches.register( 'Required', '-r,-required' )
	_.switches.register( 'Validate', '-validate' )
	_.switches.register( 'Index', '-index', 'type' )
	_.switches.register( 'Table', '-table' )


__.fieldSettings = {  'primary': None, 'secondary': None, 'omit': []  }
_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

def field_trigger(data):
	if '[' in data:
		data = data.replace( '[', '' )
		data = data.replace( ']', '' )
		__.fieldSettings['primary'] = data
	if '(' in data:
		data = data.replace( '(', '' )
		data = data.replace( ')', '' )
		__.fieldSettings['secondary'] = data
	return data



_.appInfo[focus()] = {
	'file': 'traverse.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Traverse a JSON file',
	'categories': [
						'traverse',
						'JSON',
						'tool',
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
						'p traverse -files 5e-SRD-Spells.json + cleric -one',
						'p traverse -files 5e-SRD-Spells.json + cleric -search range~90 -fields name level school.name',
						'p traverse -files 5e-SRD-Spells.json + cleric -fields name level school.name -search level=0',
						'p traverse -files 5e-SRD-Spells.json + cleric -fields name level school.name range -search range-~feet',
						'p traverse -files 5e-SRD-Spells.json + cleric -fields name level school.name range -search range~feet',
						'p traverse -files 5e-SRD-Spells.json + cleric -fields name level school.name range -search range~mile',
						'',
						'p traverse -files 5e-SRD-Spells.json -search level=0 -fields name level',
						'',
						'p traverse -f 5e-SRD-Spells.json -fields school.name | p counteach',
						'',
						'p traverse -f 5e-SRD-Spells.json -search classes.i.name=cleric name~spiritual',
						'',
						'p traverse -f 5e-SRD-Spells.json -search classes.i.name=cleric school.name=Illusion',
						'',
						['SET SUBJECT=cleric &  p file --c + 5e | p traverse + %SUBJECT% -fields name class.name -space 0 f', 'purple'],
						'',
						'p traverse -f 5e-SRD-Features.json -fields choice.from.i.name -search class.name=sorcerer | p simpleList  -split choice.from.i.name: 1 | p simpleList -split ","',
						'',
						'n D:\\_Scott\\S_Documents\\Projects\\DND\\Research\\cmd.txt',
						'',
						'',
						'',
						'p traverse -f Spells.json -fields school.name | p simpleList -split : 1 | p simpleList | p counteach',
						'p traverse -f Spells.json -fields name | p simpleList -split : 1 | p simpleList | sort',
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
	'notes': [
					# {},
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
	__.myFileLocations_SKIP_VALIDATION = False
	# _.switches.trigger( 'Search', search_trigger )
	_.switches.trigger( 'Fields', field_trigger )
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START



def start(thisFILE):
	if _.switches.isActive('Fields'):
		if len( _.switches.values('Fields') ) == 1:
			_.switches.fieldSet( 'Spaces', 'active', True )
			_.switches.fieldSet( 'Spaces', 'values', ['0'] )

	__.fieldSettings['omit'] = []
	global data

	if _.switches.isActive('Plus'):
		IDs = []
		for x in _.traverse( data, config={'inDicI':_.switches.value('Plus').replace(',',' ').lower()})['inDicI']:
			IDs.append(int(x[0]))
		# _.pr( thisFILE, IDs )
	for i,record in enumerate(data):
		thisRecordIsGood = False
		

		thisRecord = {}
		if _.switches.isActive('Fields'):
			for fr in _.switches.values('Fields'):
				thisRecord[fr] = ''
		good = True
		if _.switches.isActive('Plus'):
			if not i in IDs:
				good = False
		if good:
			if _.switches.isActive('Search'):
				for x in _.switches.values('Search'):
					x = x.lower()
					isOmit=None

					if '>' in x or '<' in x:
						# _.pr('BBB')
						if '>=' in x:
							y=x.split('>=')
						elif '<=' in x:
							y=x.split('<=')
						elif '>' in x:
							y=x.split('>')
						elif '<' in x:
							y=x.split('<')

						# _.pr( y )
					elif '-~' in x:
						isOmit = True
						y=x.split('-~')
					elif '-=' in x:
						isOmit = True
						y=x.split('-=')
					elif '=' in x:
						isOmit = False
						y=x.split('=')
					elif '~' in x:
						isOmit = False
						y=x.split('~')

					found_table = _.traverse( record, config={'find_path':y[0]})
					if 'find_path' in found_table:
						found_table = found_table['find_path']
					else:
						found_table = []
						good = False
					wasFound = False
					for found in found_table:
						xIS = None
						xIN = None
						if '>' in x or '<' in x:
							# _.pr( 'AAA' )
							try:
								if '>=' in x:
									if not int(found) >= int(y[1]):
										good=False
								elif '<=' in x:
									if not int(found) <= int(y[1]):
										good=False
								elif '>' in x:
									if not int(found) > int(y[1]):
										good=False
								elif '<' in x:
									# _.pr('HERE')
									if not int(found) < int(y[1]):
										good=False

							except Exception as e:
								# _.pr( 'ERROR' )
								good=False

						else:
							if '~' in x:
								if _.showLine( str(found), y[1] ):
									xIN = True
								else:
									xIN = False
							elif '=' in x:
								if y[1].lower() == str(found).lower():
									xIS = True
								else:
									xIS = False

							if '~' in x:
								if xIN or xIS:
									wasFound = True
							if '=' in x:
								if xIN or xIS:
									wasFound = True
					if '>' in x or '<' in x:
						pass
					else:
						if isOmit and wasFound:
							good = False
						elif not isOmit and not wasFound:
							good = False


					

			if good:
				shouldShow = False
				fieldCount = 0
				global fileFirst
				if thisFILE in fileFirst:
					if not fileFirst[ thisFILE ]:
						fileFirst[ thisFILE ] = True
						_.colorThis( [ '\n', thisFILE ], 'purple' )
				
				if _.switches.isActive('Lines'):
					_.colorThis( '__________________________________________________________________________________', 'yellow' )



				if not _.switches.isActive('Fields'):
					if _.switches.isActive('Validate'):
						_.printVar(record)
					else:
						_.printVarSimple(record)
					
				else:
					display = []
					for x in _.switches.values('Fields'):
						if not '.' in x:
							try:
								display.append({ 'field': x, 'value': str(record[x]) })
							except Exception as e:
								pass
							# _.pr( _.colorThis( x+':', 'yellow', p=0 ), _.colorThis( record[x], 'green', p=0 ) )
						else:
							found_table_i = _.traverse( record, config={'find_path':x})
							if 'find_path' in found_table_i:
								found_table_i = found_table_i['find_path']
								try:
									display.append({ 'field': x, 'value': ', '.join( found_table_i ) })
								except Exception as e:
									pass

								# _.pr()
								# _.pr()
								# _.pr( found_table_i )
								# _.pr()
								# _.pr()

							# bld = 'record'
							# for st in x.split('.'):
							#     bld+='["'+st+'"]'
							# _.pr( bld )
							# # _.pr( _.colorThis( x+':', 'yellow', p=0 ), _.colorThis( eval(bld), 'green', p=0 ) )
							# try:
							#     display.append({ 'field': x, 'value': str(eval(bld)) })
							# except Exception as e:
							#     pass
					pass
					_.fields.asset( 'project',  display )
					if not __.fieldSettings['primary'] is None and  len(display) > 1:
						# _.pr( len(display),'display',display )
						pri = 0
						sec = 0
						for dx in display:
								if dx['field'] == __.fieldSettings['primary']:
									pri+=1
								if dx['field'] == __.fieldSettings['secondary']:
									sec+=1

						if pri:
							for dx in display:
								if not dx['field'] == __.fieldSettings['primary']:
									__.fieldSettings['omit'].append( dx['field'] )
						elif sec:
							for dx in display:
								if not dx['field'] == __.fieldSettings['secondary']:
									__.fieldSettings['omit'].append( dx['field'] )

					newDisplay = []
					for dx in display:
						if not dx['field'] in __.fieldSettings['omit']:
							newDisplay.append( dx )
					_.fields.asset( 'project',  newDisplay )
					
					shouldShow = True
					if _.switches.isActive('Required'):
						if not len(newDisplay) == len(_.switches.values('Fields')):
							shouldShow = False

					if shouldShow:
						for dx in newDisplay:
							fieldCount+=1
							thisRecordIsGood = True

							thisRecord[ dx['field'] ] = dx['value']
							if not _.switches.isActive('Table'):
								_.pr( _.colorThis( 
									_.fields.value( 'project', 'field', dx['field'], r=1 )
									+':', 'yellow', p=0 ), _.colorThis( 
									_.fields.value( 'project', 'value', dx['value'] )
									, 'green', p=0 ) )
					
				if not _.switches.isActive('Table'):
					if shouldShow:
						if not _.switches.isActive('Spaces'):
							_.pr()
							_.pr()
						elif  _.switches.isActive('Spaces'):
							spaces = 0
							mx = int( _.switches.values('Spaces')[0] )
							while not spaces == mx:
								spaces+=1
								_.pr()
					# _.pr('fieldCount',fieldCount, _.switches.isActive('Spaces'), _.switches.values('Spaces')[0], )
					if _.switches.isActive('Spaces') and _.switches.values('Spaces')[0] == '0' and len( _.switches.values('Spaces') ) > 1 and 'f' in _.switches.values('Spaces')[1] and fieldCount > 1:
						_.pr()
					if _.switches.isActive('One'):
						sys.exit()
		
		if thisRecordIsGood:
			__.traverse_table.append( thisRecord )
	if _.switches.isActive('Table') and len(__.traverse_table):
		_.tables.register( 'data', __.traverse_table )
		_.tables.print( 'data', ','.join(_.switches.values('Fields')) )

fileFirst = {}

def action():

	if _.switches.isActive('Index'):

		for row in _.isData(r=1):
			_.pr()
			_.pr()
			_.colorThis( row, 'yellow' )
			_.traverse( _.getTable( row ) )
			# _.printVarSimple( _.traverse_dic_research )
			x = []
			for t in _.traverse_dic_research['type']:
				if _.switches.value('Index') == 'type':
					_.colorThis( ['\t',t], 'white' )
				for f in _.traverse_dic_research['type'][t]:
					ff = f
					# ff = f.replace( '-i-', 'i' )
					delim = '-i-'
					if ff.startswith(delim):
						ff = ff[ len(delim+'.'): ]
					if _.switches.value('Index') == 'type':
						_.colorThis( ['\t\t',ff], 'cyan' )
					x.append( ff )
			x.sort()
			if not _.switches.value('Index') == 'type':
				_.pr(  )
				for y in x:
					_.colorThis( ['\t',y], 'cyan' )
		sys.exit()
	# if _.switches.isActive('Search'):
	#     _.pr( 'search active' )
	#     _.pr( _.switches.value('Search') )
	#     _.pr( _.switches.values('Search') )

	global data
	global fileFirst
	for i,row in enumerate(_.isData(r=1)):

		if len(_.isData()) > 1:
			fileFirst[ row ] = False

		try:
			data = _.getTable( row )
			start(thisFILE=row)
		except Exception as e:
			_.colorThis( [ 'Error: FILE' ], 'red' )
			
__.traverse_table = []


########################################################################################
if __name__ == '__main__':
	action()







