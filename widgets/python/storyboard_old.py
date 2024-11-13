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
# import simplejson as json
# from threading import Timer


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
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )

##################################################

from operator import itemgetter
# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Report', '-r,-report')
	_.switches.register('Child', '-child')
	_.switches.register('All', '-all')
	_.switches.register('Fields', '-fields')
	_.switches.register('Ask', '-ask')
	



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

_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p storyboard ')
_.appInfo[focus()]['examples'].append('p storyboard -r characters')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('previously blank22 ')

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
	# _.pr( records )
	paths = []
	cntK = {}
	
	configurations = []
	for rec in records:
		# cntK[str(rec)] = 0
		try:
			type( cntK[str(rec)] )
			cntK[str(rec)] += 1
			# _.pr( 'here', cntK[str(rec)] )
			# _.pr( str(rec) )
		except Exception as e:
			# _.pr( type( cntK[str(rec)] ) )
			cntK[str(rec)] = 1
			paths.append({ 'cnt': 0, 'config': configID, 'rec': rec })
			n = {}
			n['cnt'] = 0
			n['config'] = configID
			for k in rec.keys():
				n[k] = rec[k]
			configurations.append( n )
			configID+=1
			# paths.append([0,rec])
		
	
	# paths = sorted(paths, key=itemgetter('cnt'))
	# paths = sorted(paths, key=itemgetter(0) )
	print_records = []
	custom_sort = []
	for i,rec in enumerate(paths):
		paths[i]['cnt'] = cntK[str(paths[i]['rec'])]
		print_records.append({ 'cnt': paths[i]['cnt'], 'rec': str(paths[i]['rec']) })
		for ii,conf in enumerate(configurations):
			if conf['config'] == rec['config']:
				configurations[ii]['cnt'] = paths[i]['cnt']

		# paths[i][0] = cntK[str(paths[i][1])]
		# _.pr( paths[i] )
		# _.pr( paths[i]['cnt'],'\t', paths[i]['rec'] )

	_.switches.fieldSet( 'Long', 'active', True )
	# # _.switches.fieldSet( 'Input', 'value', 'one' )
	# _.pr()
	# test = _.tables.returnSorted( 'test', 'd.cnt', print_records )
	# _.tables.print('test','cnt,rec')
	# _.pr()
	# _.pr()
	# test2 = _.tables.returnSorted( 'test2', 'd.rec', print_records )
	# _.tables.print('test2','cnt,rec')
	# _.pr()
	_.pr()

	if len( configurations ) > 0:
		_.tables.register('data',configurations)
		_.tables.print('data', ','.join( configurations[0].keys() ) )
		# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
	else:
		_.pr( 'Error: configurations == 0' )
		_.pr( paths )
	return configurations

def reportChild( parentIn='', childIn='', fieldsIn='' ):
	global configFile
	_.pr()
	_.pr( 'Report:', parentIn )
	_.pr()
	keyList = {}
	cKeyList = {}
	records = []
	fieldsSpecified = False
	if not fieldsIn == '':
		fieldsSpecified = True
		fieldsIn = fieldsIn.lower()
		fieldList = fieldsIn.split(',')
	# _.pr( 'fieldsSpecified:', fieldsSpecified )
	for config in configFile[ str(parentIn) ]:
		# _.pr( config )
		for label in config.keys():
			keyList[label] = auditType( config[label] )
		# _.pr( label, keyList[label] )
		if keyList[label] == 'child':
			# _.pr( 'fieldsSpecified', fieldsSpecified )
			if not len( cKeyList.keys() ):
				for cLabel in config[label][0].keys():
					if fieldsSpecified:
						shouldProcess = False
						if cLabel.lower() in fieldList:
							shouldProcess = True
					else:
						# _.pr( '0 HERE' )
						if cLabel == 'id':
							shouldProcess = False
						else:
							shouldProcess = True


					if shouldProcess:
						# _.pr( '* HERE' )
						cKeyList[cLabel] = cleanTypeString( config[label][0][cLabel] )
						# _.pr( 'HERE', cLabel, cKeyList[cLabel] )

			for child in config[label]:
				for cLabel in cKeyList.keys():

					try:
						dt = cleanTypeString( child[cLabel] )
					except Exception as e:
						_.pr( 'Error: key', cLabel )
						_.pr( child )


					# _.pr( cLabel, dt )
					try:
						if type( cKeyList[cLabel] ) == str or type( cKeyList[cLabel] ) == list:
							error = False
						else:
							error = True
					except Exception as e:
						error = True
					
					if error:
						_.pr('Error: field')
						sys.exit()


					# _.pr( cLabel, cKeyList[cLabel] )


					if type( cKeyList[cLabel] ) == list and not dt in cKeyList[cLabel]:
						cKeyList[cLabel].append( dt )
					if type( cKeyList[cLabel] ) == str and not dt == cKeyList[cLabel]:
						# _.pr( 'HERE' )
						tmp = cKeyList[cLabel]
						cKeyList[cLabel] = []
						cKeyList[cLabel].append( tmp )
						cKeyList[cLabel].append( dt )
	# _.pr( cKeyList )
	keyList = {}

	for config in configFile[ str(parentIn) ]:
		for label in config.keys():
			keyList[label] = auditType( config[label] )
		# _.pr( keyList[label] )
		if keyList[label] == 'child':
			for child in config[label]:
				rec = {}
				for cLabel in cKeyList.keys():
					if type(cKeyList[cLabel]) == list:
						rec[cLabel] = cleanTypeString( child[cLabel] )
					elif cKeyList[cLabel] == 'list':
						if len(child[cLabel]) == 0:
							rec[cLabel] = '0'
						else:
							rec[cLabel] = '1+'
					elif cKeyList[cLabel] == 'int':
						rec[cLabel] = cKeyList[cLabel]
					else:
						rec[cLabel] = str(cKeyList[cLabel])+'*'

				records.append( rec )
	# _.pr( records )
	findGroups( records )




def reportParent( parentIn='', fieldsIn='' ):
	global configFile
	_.pr()
	_.pr( 'Report:', parentIn )
	_.pr()
	keyList = {}
	cKeyList = {}
	records = []
	fieldsSpecified = False
	if not fieldsIn == '':
		fieldsSpecified = True
		fieldsIn = fieldsIn.lower()
		fieldList = fieldsIn.split(',')
	for label in configFile[ str(parentIn) ][0].keys():
		keyList[label] = auditType( configFile[ str(parentIn) ][0][label] )
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
				cKeyList[label] = cleanTypeString( configFile[ str(parentIn) ][0][label] )
				# _.pr( 'HERE', label, cKeyList[label] )



	for config in configFile[ str(parentIn) ]:

		for label in cKeyList.keys():

			try:
				dt = cleanTypeString( config[label] )
			except Exception as e:
				_.pr( 'Error: key', label )
				_.pr( config )


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

	for config in configFile[ str(parentIn) ]:
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
	return findGroups( records )
	# sys.exit()



def action():
	global configFile

	if not _.switches.isActive('Report'):
		if not _.switches.isActive('All'):
			for config in configFile.keys():
				_.pr( config )
		else:
			if not _.switches.isActive('All'):
				for config in configFile.keys():
					_.pr( '______________________________________________________________________________________________________________________________________________' )
					reportParent( parentIn=config )
					reportChild( parentIn=config )
					_.pr( '______________________________________________________________________________________________________________________________________________' )
			else:
				for config in configFile.keys():
					_.pr( '______________________________________________________________________________________________________________________________________________' )
					reportParent( parentIn=config )
					fields = ''
					while not fields == 'x':
						_.pr( '____________________________________' )
						fields = input( ' What fields? ' )
						if not fields == 'x' and not fields == 'b':
							groups = reportParent( parentIn=config, fieldsIn=fields )
							_.pr(  )
							_.pr( groups )
							_.pr(  )
							failtype = input( ' Fail type (h,s,field)? ' )
							if 'f' == failtype:
								failField = input( ' Field? ' )


					_.pr( '_______________________________________________________________________' )
					reportChild( parentIn=config )
					_.pr( '____________________________________' )
					fields = ''
					while not fields == 'x':
						_.pr( '____________________________________' )
						fields = input( ' What fields? ' )
						if not fields == 'x' and not fields == 'b':
							groups = reportChild( parentIn=config, fieldsIn=fields )
							_.pr(  )
							_.pr( groups )
							_.pr(  )
							failtype = input( ' Fail type (h,s,field)? ' )
							if 'f' == failtype:
								failField = input( ' Field? ' )
					_.pr( '______________________________________________________________________________________________________________________________________________' )


	else:
		if _.switches.isActive('Fields'):
			reportChild( _.switches.value('Report'), fieldsIn=_.switches.value('Fields') )
		else:
			reportChild( _.switches.value('Report') )


configID = 0
configFile = _.getTable('auditCodeBase.json')
########################################################################################
if __name__ == '__main__':
	action()


# storyboard

# findGroups




