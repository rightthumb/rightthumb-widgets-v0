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
	# _.switches.register( 'Files', '-f,-file,-files','file.txt',  isRequired=True, description='Files' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', description='Files' )
	_.switches.register( 'Parents', '-p,-parent,-parents' )
	_.switches.register( 'Fields', '-field,-fields' )
	_.switches.register( 'Lookup', '-lookup' )
	_.switches.register( 'IncludeLists', '-lists' )
	_.switches.register( 'IncludeDics', '-dics' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'traverseDic.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Traverse dictionary file',
	'categories': [
						'traverse',
						'profile',
						'variable',
						'programming',
						'research',
						'tool',
						'har',
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
						"""p traverseDic -f www.rightthumb.com.har -parent "['log', 'entries', '-i-', 'request']" content - text -lookup""",
						'',
						"""p traverseDic -f www.rightthumb.com.har -parent "['log', 'entries', '-i-', 'request']" -lookup""",
						'',
						'p traverseDic -f www.rightthumb.com.har -field url -lookup',
						'',
						'p traverseDic -f www.rightthumb.com.har -p content - text -lookup',
						'',
						'p traverseDic -f www.rightthumb.com.har -parent log;entries;-i-  -lookup',
						'',
						'p traverseDic -f www.rightthumb.com.har -parent log;entries;-i-  content  -lookup - text',
						'',
						'p traverseDic -f littlealchemy.com.har -parents log;entries;-i-;response;cookies  -lookup',
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
	# _.switches.trigger( 'Files', _.myFileLocations )
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



def action():
	global delim
	global theI
	global payload
	# traverse_dic traverse_dic_research

	if not _.switches.isActive('Files'):
		_.colorThis( [ 'File is isRequired' ], 'red' )
		sys.exit()
	
	for file in _.switches.values('Files'):
		records = {}
		_.traverse_dic_research['theFields'] = []
		theDic = _.getTable2(file)
		_.traverse_dic( theDic )
		for record in _.traverse_dic_research['theFields']:
			shouldInclude = True
			if record['type'] == 'list' and not _.switches.isActive('IncludeLists'):
				shouldInclude = False
			if record['type'] == 'dict' and not _.switches.isActive('IncludeDics'):
				shouldInclude = False
			# if True:
			if shouldInclude:
				
				# _.pr( record )
				if _.switches.isActive('Parents'):
					found = False
					for pp in _.switches.values('Parents'):
						pp = _str.cleanBE(pp,' ')
						# _.pr( '|'+pp+'|' )
						# found = False
						if len(pp):
							if '[' in pp:
								ppx = eval(pp)
								if ppx == record['parents']:
									found = True
									# _.pr('A')

							elif not ';' in pp:
								if pp.lower() == record['parents'][ len(record['parents'])-1 ].lower():
									found = True
									# _.pr('B', pp)
							elif ';' in pp:
								# _.pr( pp )
								found = False
								mpx = len(record['parents'])-1
								ipi = 0
								pps = pp.split(';')
								if mpx and mpx+1 >= len(pps):
									# good = True
									# testing = { 'a': [], 'b': [] }
									testing = []
									for ip, px in enumerate(pps):
										ipi+=1
										# _.pr( mpx, mpx-ip )
										# temp.append([ px, record['parents'][ ip ] ])
										# _.pr(px, record['parents'][ ip ] )
										# testing['a'].append( px.lower() )
										# testing['b'].append( record['parents'][ ip ].lower() )
										if px.lower() == record['parents'][ ip ].lower():
											# testing.append([  px.lower(), record['parents'][ ip ].lower()  ])
											testing.append(record['parents'][ ip ])
											# good = False
									if len(testing) == len(pps) and (len(record['parents']) == ipi or len(record['parents']) == ipi+1):
										# _.pr( 'xx', len(testing) , len(pps) )
										# _.pr()
										# _.pr()
										# _.pr()
										# for x in temp:
										#     _.pr(x)
										# _.pr(  )
										found = True
										# _.pr('C', record['parents'], pp, len(pp),'\t',testing)


					pass
					if not found:
						shouldInclude = False

				if shouldInclude:
					if _.switches.isActive('Fields'):
						found = False
						for pp in _.switches.values('Fields'):
							if pp.lower() == record['field'].lower():
								found = True
						if not found:
							shouldInclude = False

					# shouldInclude = True


					if shouldInclude and _.showLine( record['field'] ):
						if _.switches.isActive('Lookup'):
							try:
								records[ delim.join(record['parents']) ].append( record )
							except Exception as e:
								records[ delim.join(record['parents']) ] = []
								records[ delim.join(record['parents']) ].append( record )
							"""
							try:
								records[ str(record['parents']) ].append( record )
							except Exception as e:
								records[ str(record['parents']) ] = []
								records[ str(record['parents']) ].append( record )
							"""
						else:
							pass
							_.pr( record )
		if _.switches.isActive('Lookup'):


			theSearch = {}
			for key in records.keys():
				# _.pr()
				fields = []
				for ri, record in enumerate(records[key]):
					fields.append(record['field'])
				for ri, record in enumerate(records[key]):
					field = record['parents'] + [ record['field'] ]

					try:
						theSearch[ record['field'] ].append( field )
					except Exception as e:
						theSearch[ record['field'] ] = []
						theSearch[ record['field'] ].append( field )
			# _.printVarSimple( theSearch )
			researchType = 'single'
			keys = list( records.keys() )
			config = { 'common': [], 'i': 0 }
			# if len(keys) > 1:
				# researchType = 'multi_individual'
			keysX = []
			m = 999999
			for key in records.keys():
				kk = key.split(delim)
				if m > len(kk)-1:
					m = len(kk)-1
				keysX.append( kk )

			my=0
			while not my == m:
				test = None
				good = True
				ix = len(keysX)-1
				iy=0
				while not ix == iy:
					if not test is None and keysX[iy][my] == test:
						good = True
					elif not test is None and not keysX[iy][my] == test:
						good = False
					if not good:
						break
					test = keysX[iy][my]
					iy+=1
				if good:
					researchType = 'multi_pattern'
					if test == theI:
						config['i']+=1
					config['common'].append( test )
				if not good:
					break
				my+=1

				pass


			pass
			# researchType single multi_individual multi_pattern
			# _.pr( 'records', records )
			# _.pr( 'researchType', researchType )
			pass
			if False and researchType == 'single' or researchType == 'multi_individual':

				payload = {}
				for key in records.keys():
					# _.pr()
					fields = []
					for ri, record in enumerate(records[key]):
						fields.append(record['field'])
					for ri, record in enumerate(records[key]):
						field = record['parents'] + [ record['field'] ]
						_.traverse_dic_research['returnField'] = []
						# _.pr( field )
						_.traverse_dic( theDic, config={ 'returnField': field } )
						for tdri, pay in enumerate(_.traverse_dic_research['returnField']):
							pay['parents'].pop()
							try:
								payload[ key ][ delim.join(pay['parents']) ][ record['field'] ] = pay['data']
							except Exception as e:
								try:
									payload[ key ][ delim.join(pay['parents']) ]={}
									for fieldX in fields:
										payload[ key ][ delim.join(pay['parents']) ][fieldX]=None
								except Exception as e:
									payload[ key ] = {}
									payload[ key ][ delim.join(pay['parents']) ] = {}
									for fieldX in fields:
										payload[ key ][ delim.join(pay['parents']) ][fieldX]=None

								payload[ key ][ delim.join(pay['parents']) ][ record['field'] ] = pay['data']
			if True:
				# _.pr( 'test' )
			# elif False and researchType == 'multi_pattern':
				# _.pr( 'here' )
				# _.printVarSimple( theSearch )
				# _.printVarSimple( config )
				# sys.exit()
				config['default'] = {}
				payload = {}
				for key in records.keys():
					fields = []
					for ri, record in enumerate(records[key]):
						fields.append(record['field'])
					config['default'][key] = fields

				_.traverse_dic_research['returnFields'] = []
				_.traverse_dic( theDic, config={ 'returnFields': theSearch } )


				for tdri, pay in enumerate(_.traverse_dic_research['returnFields']):
					# _.pr()
					# _.pr( pay['parents'] )
					# _.pr( pay['parentsI'] )
					# pay['parents'].pop()
					var = buildVariable({
											'pay': pay,
											'settings': config,
					})
					d = pay['data']
					do = var + ' = d'
					exec( do )
					# _.pr( do, d )
					# _.pr( payload )
					# _.pr( do )


				_.printVarSimple( payload )
				pass
			pass
			# _.printVarSimple( config )
			# _.printVarSimple( payload )



def buildVariable( config ):
	global payload
	global delim
	global theI



	# _.pr( config )
	r = 'xXx'
	blank = '[\''+r+'\']'
	build = []
	build2 = []
	build.append( 'payload' )
	build2.append( 'payload' )
	# _.pr()
	# _.pr(config['pay']['parents'])
	# _.pr(config['pay']['parentsI'])
	# _.printVarSimple( config['settings'] )
	# sys.exit()
	for i,item in enumerate(config['pay']['parents']):
		# _.pr( config['pay']['parents'][i] )
		# _.pr( item )
		# field2 = 
		build2.append( str(item) )

		field = None
		if item == theI:
			# _.pr( 'here' )
			# sys.exit()
			field = str(config['pay']['parentsI'][i])
		elif i > len(config['settings']['common'])-1 :
			field = str(config['pay']['parentsI'][i])
			field2 = str(config['pay']['parents'][i])

		if not field is None:
			do = ''.join( build )
			# _.pr( 'do', do )
			test = eval( do )
			build.append( blank.replace( r, field ) )
			
			do = ''.join( build )
			# _.pr( 'do', do )
			if not field in test:
				exec( ''.join( build ) + '={ }' )

			px = delim.join(build2)
			if px in config['settings'].keys():
				# _.pr( 'here' )
				# sys.exit()
				for x in config['settings'][px]:
					y = ''.join( build+[ blank.replace( r, x ) ] )
					exec( y + '=None' )
			# if 

	return ''.join( build + [blank.replace( r, config['pay']['parentsI'].pop() )] )



	
	"""
	record = {'type': 'int', 'field': 'size', 'parents': ['log', 'entries', '-i-', 'response', 'content']}
	pay = { 'parents': [], 'data': '' }
	config = { 'common': [], 'i': 0, 'default': {} }
	{
		'key': key,
		'pay': pay,
		'record': record,
		'settings': config,
		'payload': payload,
		'var': 'payload',
	}
	"""



payload = {}
delim = '____'
delim = '_'
theI = '-i-'

########################################################################################
if __name__ == '__main__':
	action()







