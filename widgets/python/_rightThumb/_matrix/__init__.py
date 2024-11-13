import os

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import sys
import signal

#                                       #
import _rightThumb._construct as __
__.autoCreationConfiguration
#                                       #
import _rightThumb._base3 as _


# import os

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

import time

import _rightThumb._vars as _v

# import uuid
# from threading import Timer

start = time.time()





def genUUID():
	import uuid
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	return string


appReg = ''

class Appp:
	global indexes
	global masterID
	global masterSequence


	def __init__( self ):
		do = 'cls'
		# os.system( '"' + do + '"' )
		# _.pr()
		# _.pr( genUUID() )
		# _.colorThis( [ ' ****************************************** this thing just started ******************************************' ], 'green' )
		self.theMatrix = '_rightThumb._matrix'
		self.childFiles = [
								"_async_child",
								"_audit_child",
								"_data_child",
								"_db_child",
								"_ext_child",
								"_focus_child",
								"_procedure_child",
								"_process_child",
								"_reg_child",
								"_switch_child",
								"_table_child",
								"_task_child"
							]
		self.dafault = None
		self.memory = 0
		self.memory_max = 0


		self.temp = 99
		self.algorithmLog = {}
		# self.records_{} = {}


		self.lastSwitch = ''

		self.monitor_records = {}
		self.spentIDs = []
		self.masterID = 0

		self.algorithmID = 0

		self.help_switches = '?,/?,-?,/h,/help,-help,--help'
		self.load_switches = False

		self.indexes = {
							'ids': {},
							'labels': {},
							# '{}': { 'names': [] }
		}


		self.indexes['labels']['free']     = []
		self.indexes['labels']['nuc']     = []
		self.indexes['labels']['asyn']     = []
		self.indexes['labels']['data']      = []
		self.indexes['labels']['audit']     = []
		self.indexes['labels']['switch']    = []
		self.indexes['labels']['table']     = []
		self.indexes['labels']['db']        = []
		self.indexes['labels']['focus']        = []
		self.indexes['labels']['ext']       = []
		self.indexes['labels']['reg']       = []
		self.indexes['labels']['process']   = []
		self.indexes['labels']['procedure'] = []
		self.indexes['labels']['task']      = []


		self.records = {}


		self.records['nuc']       = {}
		self.records['asyn']     = {}
		self.records['data']      = {}
		self.records['audit']     = {}
		self.records['switch']    = {}
		self.records['table']     = {}
		self.records['db']        = {}
		self.records['focus']     = {}
		self.records['ext']       = {}
		self.records['reg']       = {}
		self.records['process']   = {}
		self.records['procedure'] = {}
		self.records['task']      = {}


		self.sequences = {}
		self.sequences['all']       = 0
		self.sequences['free']      = {}
		self.sequences['nuc']       = {}
		self.sequences['asyn']     = {}
		self.sequences['data']      = {}
		self.sequences['audit']     = {}
		self.sequences['switch']    = {}
		self.sequences['table']     = {}
		self.sequences['db']        = {}
		self.sequences['focus']     = {}
		self.sequences['ext']       = {}
		self.sequences['reg']       = {}
		self.sequences['process']   = {}
		self.sequences['procedure'] = {}
		self.sequences['task']      = {}

		self.ifSet = []
		self.ifSetAction = {}
		self.transactionLog = []


	def transaction( self, label, _from, _to, note=None, data=None ):
		if not data is None:
			import _rightThumb._profileVariables as _profile
			profile = _profile.records.audit( 'xfer', data )
		else:
			profile = None
		self.transactionLog.append({ 'epoch': time.time(), 'type': label, 'from': _from, 'to': _to, 'profile': profile, 'note': note })

	def base( self, focus ):
		global delimReg
		return focus.split(delimReg)[0]

	def label( self, name, focus, isBase=False ):
		name = str(name)
		focus = str(focus)
		if focus is None:
			global appReg
			focus = appReg

		if focus == 'isDefault':
			return name + ' | ' + focus

		if isBase:
			return name + ' | ' + self.base(focus)
		else:
			return name + ' | ' + focus

	def help( self ):
		global mainApp
		record = self.focus(mainApp).record
		__.columnAbbreviations = 1

		try:
			if type( record['description'] ) == list:
				_.pr( _.inlineBold('Description:   '))
				for x in record['description']:
					_.pr( '                 - ', x )
				_.pr()
			else:
				_.pr( _.inlineBold('Description:   '), record['description'] + '\n')
			configured = True
		except Exception as e:
			configured = False
		try:
			if len(record['prerequisite']) > 0:
				_.printBold('Prerequisite:')
				for docItem in record['prerequisite']:
					if type(docItem) == list:
						_.colorThis( '\t\t'+docItem[0], docItem[1]  )
					else:
						_.colorizeRow( '\t\t'+ docItem , 2)
					# _.colorizeRow('\t' + prereq,2)
				_.pr('\n')
		except Exception as e:
			pass
		try:
			if len(record['relatedapps']) > 0:
				_.printBold('Related Apps:')
				for docItem in record['relatedapps']:
					if type(docItem) == list:
						_.colorThis( '\t\t'+docItem[0], docItem[1]  )
					else:
						_.colorizeRow( '\t\t'+ docItem , 2)
				_.pr('\n')
		except Exception as e:
			pass

		if configured:
			if len(record['examples']) > 0:
				_.printBold('Examples:')
				for docItem in record['examples']:

					if type(docItem) == list:
						_.colorThis( '\t\t'+docItem[0], docItem[1]  )
					else:
						_.colorizeRow( '\t\t'+ docItem , 2)

					# _.colorizeRow('\t' + ex,2)
				_.pr('\n')
			if len(record['columns']) > 0:
				_.printBold('Columns and abbreviations:')
				result = ''
				if len( record['columns'] ):
					# fields.register( 'columns', 'name,abbreviation', script=__.triggerTest )
					_.fields.asset( 'columns', record['columns'] )
					_.pr()

				if __.columnAbbreviations == 0:
					for col in record['columns']:
						result += col['name'] + '(' + col['abbreviation'] + '), '
					result = result[:-2]
					_.colorizeRow('\t' + result + '\n',2)

				if __.columnAbbreviations == 1:
					for col in record['columns']:
						abbreviation =  _.fields.value( 'columns', 'abbreviation', col['abbreviation'] )
						name =          _.fields.value( 'columns', 'name', col['name'] )
						_.colorizeRow( '\t' + abbreviation + '\t' + name )
						# _.pr( '\t', col['abbreviation'], '\t', col['name']  )

				if len( record['columns'] ):
					_.pr()
					_.pr()
				# _.pr('\n')
		# self.print()


		# _.printVar( record )
		if self.load_switches:
			theSwitches = []
			for i,key in enumerate(self.records['switch'].keys()):
				if key.endswith(mainApp):
					name = self.records['switch'][key].name
					switches = self.records['switch'][key].switches
					example = self.records['switch'][key].expected_input_example
					if example is None:
						example = ''
					theSwitches.append({ 'name': name, 'switches': switches, 'example': example  })
					# if name == 'Files':
					#     _.pr(dir(self.records['switch'][key]))

					# _.pr( name, switches, example )
			_.fields.asset( 'switches', theSwitches )
			for switch in theSwitches:
				if switch['name'] == 'Help':
					_.pr()
				line = ''
				line += _.fields.value( 'switches', 'name', switch['name'] )
				line += '\t'
				line += _.fields.value( 'switches', 'switches', switch['switches'] )
				line += '\t'
				line += _.fields.value( 'switches', 'example', switch['example'] )
				_.colorizeRow( line )

				# _.pr( key )
		sys.exit()

	def newMasterID( self ):
		self.masterID+=1
		newID = self.masterID

		if not self.spentIDs.count(newID):
			self.spentIDs.append(newID)
			if self.spentIDs.count(newID) > 1:
				return self.newMasterID()
			return newID
		else:
			return self.newMasterID()
			

	def ir( self, activity=None ):
		self.ifSet = []
		if not activity is None:
			self.ifSetAction[activity] = []
		
		return True


	def postLoad( self ):
		pass



	def id( self, theID ):
		for t in self.records.keys():
			for k in self.records[t]:
				try:
					if self.records[t][k].id == theID:
						return self.records[t][k]
				except Exception as e:
					pass
				
		return None


	def defaultScriptTriggers( self ):
		self.switch( 'Column' ).triggerColumns()
		self.switch( 'Sort' ).triggerColumnsSort()
		self.switch( 'GroupBy' ).triggerColumns()
		self.switch( 'Ago' ).triggerAgo()
		# self.switch( 'PlusClose' ).trigger( PlusClose )


	def additional_Not_Registration( self, segment, name, registration, focus=None ):
		return None

	def additional_Registration( self, segment, name, registration, focus=None ):
		return None
		if segment == 'data' and not registration is None and name == 'Pipe' and 'pipe' in  list(registration.keys()) :
			pass


	def REPLACE_THIS_2( self, name, registration=None, focus=None, trackingID=None ):
		global appReg
		global appReg
		global appReg
		global appReg
		self.sequences['all'] +=1
		try:
			self.sequences['REPLACE_THIS_1']['all'] +=1
		except Exception as e:
			self.sequences['REPLACE_THIS_1']['all'] = 1

		if registration is None:
			self.additional_Not_Registration( 'REPLACE_THIS_1', name, registration, focus )
			if self.label( name, focus ) in self.records[ 'REPLACE_THIS_0' ].keys():
				return self.records[ 'REPLACE_THIS_0' ][ self.label( name, focus )]
			if self.label( 'Default', 'isDefault' ) in self.records[ 'REPLACE_THIS_0' ].keys():
				return self.records[ 'REPLACE_THIS_0' ][ self.label( 'Default', 'isDefault' ) ]

			else:
				return None
		else:
			registration['trackingID'] = trackingID
			registration['epoch'] = time.time()
			if focus is None:
				focus = appReg
			
			if 'isBase' in registration.keys():
				isBase = True
			else:
				isBase = False

			registration['focus'] = focus
			registration['name'] = name
			registration['hashID'] = self.label( name, focus, isBase=isBase )
			
			additional = self.additional_Registration( 'REPLACE_THIS_1', name, registration )
			if not additional is None:
				registration['additional'] == additional
			try:
				_REPLACE_THIS_0_child
			except Exception as e:
				from _rightThumb._matrix import _REPLACE_THIS_0_child
			self.indexes['labels']['REPLACE_THIS_1'].append( name )
			theID = self.newMasterID()

			if not self.label( name, focus, isBase=isBase ) in self.records[ 'REPLACE_THIS_0' ].keys():
				self.records[ 'REPLACE_THIS_0' ][self.label( name, focus, isBase=isBase )] = _REPLACE_THIS_0_child.TheChild( theID=theID, registration=registration )
			elif self.label( name, focus, isBase=isBase ) in self.records[ 'REPLACE_THIS_0' ].keys():
				self.records[ 'REPLACE_THIS_0' ][self.label( name, focus, isBase=isBase )].add( theID=theID, registration=registration )
			return self.records[ 'REPLACE_THIS_0' ][self.label( name, focus, isBase=isBase )]
			# self.records_REPLACE_THIS_1[name] = _REPLACE_THIS_2_child.TheChild( theID=theID, registration=registration )


	def __switch__( self, name=None, switch=None, expected_input_example = None, isRequired=False, isPipe=False, description='', examples=None, required=None, related=None, isDefault=False, focus=None, trackingID=None,         f=None, printFocus=False ):
		global appReg
		if not f is None:
			focus = f

		if focus is None:
			stack = self.c(c=1)
			try:
				focus = stack['programs'][0]
			except Exception as e:
				stack = self.c(i=0,c=1)
				focus = stack['file']
			if focus == self.theMatrix:
				global mainApp
				focus = mainApp
				
			if _matrix.printSwitcheFocus or printFocus:
				_.pr( 'focus', focus )

		if name is None:
			name = 'Default'
			focus = 'isDefault'
		if switch is None:
			registration = None
		else:
			registration = { 'name': name, 'switches': switch, 'expected_input_example': expected_input_example, 'isRequired': isRequired, 'isPipe': isPipe, 'description': description, 'examples': examples, 'required': required, 'related': related, 'isDefault': isDefault }


		if not self.label( name, focus ) in self.records[ 'asyn' ].keys() and self.label( name, focus, isBase=True ) in self.records[ 'asyn' ].keys():
			self.records[ 'asyn' ][  self.label( name, focus )  ] = self.records[ 'asyn' ][  self.label( name, focus, isBase=True )  ]
			return self.records[ 'asyn' ][  self.label( name, focus )  ]
		


	def __async__( self, name, script=None, kwargs=None, timeout=None, trigger=None, tkwargs=None, ttimeout=None, focus=None, trackingID=None,        k=None, t=None, tk=None, tt=None, ttime=None, f=None ):
		global appReg
		if not f is None:
			focus = f

		if focus is None:
			stack = self.c(c=1)
			try:
				focus = stack['file']
			except Exception as e:
				stack = self.c(i=0,c=1)
				focus = stack['file']
			if focus == self.theMatrix:
				global mainApp
				focus = mainApp

		if not tt is None:
			timeout = tt
		if not ttime is None:
			timeout = ttime
		if not tk is None:
			tkwargs = tk

		if not k is None:
			kwargs = k
		if not t is None:
			timeout = t
		if script is None:
			registration = None
		else:
			registration = { 'script': script, 'kwargs': kwargs, 'timeout': timeout, 'trigger': trigger, 'tkwargs': tkwargs, 'ttimeout': ttimeout }



	def __process__( self, name, description=None, isIF=None, focus=None, trackingID=None,        d=None, i=None, f=None ):
		global appReg
		if not f is None:
			focus = f

		if focus is None:
			stack = self.c(c=1)
			try:
				focus = stack['file']
			except Exception as e:
				stack = self.c(i=0,c=1)
				focus = stack['file']
			if focus == self.theMatrix:
				global mainApp
				focus = mainApp

		if not d is None:
			description = d
		if not i is None:
			isIF = i
		if description is None:
			registration = None
		else:
			registration = { 'name': name, 'description': description, 'isIF': isIF }
	

	def __focus__( self, name, registration=None, focus='live', trackingID=None ):
		global appReg
		if self.dafault is None:
			self.dafault = self.label( name, focus )
		if not self.label( name, focus ) in self.records['focus'].keys():
			registration = { 'name': name }

		if not registration is None:
			registration = { 'name': name }

	def __data__( self, name, value=None, focus=None, trackingID=None,         f=None ):
		global appReg
		if not f is None:
			focus = f

		if focus is None:
			stack = self.c(c=1)
			try:
				focus = stack['file']
			except Exception as e:
				stack = self.c(i=0,c=1)
				focus = stack['file']
			if focus == self.theMatrix:
				global mainApp
				focus = mainApp
				
		# if focus is None and name == 'Pipe':
		if name == 'Pipe' or name == 'stdin':
			focus = 'live'


		registration = None
		if not self.label( name, focus ) in self.records['data'].keys():
			registration = { 'name': name, 'value': value }
			
		if not value is None:
			registration = { 'name': name, 'value': value }
			

	def __ext__( self, name, app=None, trackingID=None ):
		global appReg
		focus = 'live'

		registration = None
		if not self.label( name, focus ) in self.records['data'].keys():
			registration = { 'name': name, 'app': app, 'focus': focus }
			
		if not app is None:
			registration = { 'name': name, 'app': app, 'focus': focus }
		# _.pr( 'here', name, app, focus, registration )




#7F21BD8F

# ############################# ############################# 

	def ext( self, name, app=None, trackingID=None ):
		try:
			_ext_parent
		except Exception as e:
			from _rightThumb._matrix import _ext_parent
		return _ext_parent.ext( name, app, trackingID )
# ############################# ############################# 

	def nuc( self, name, registration=None, focus=None, trackingID=None ):
		try:
			_nuc_parent
		except Exception as e:
			from _rightThumb._matrix import _nuc_parent
		return _nuc_parent.nuc( name, registration, focus, trackingID )
	# ############################# 

	def nucleation( self, name, registration=None, focus=None, trackingID=None ):   
		return self.nuc( name, registration, focus, trackingID )
# ############################# ############################# 
	def asyn( self, name, script=None, kwargs=None, timeout=None, trigger=None, tkwargs=None, ttimeout=None, focus=None, trackingID=None,        k=None, t=None, tk=None, tt=None, ttime=None, f=None ):
		try:
			_async_parent
		except Exception as e:
			from _rightThumb._matrix import _async_parent
		return _async_parent.asyn( name, script, kwargs, timeout, trigger, tkwargs, ttimeout, focus, trackingID,        k, t, tk, tt, ttime, f )
# ############################# ############################# 
	def data( self, name, value=None, focus=None, trackingID=None,         f=None ):
		try:
			_data_parent
		except Exception as e:
			from _rightThumb._matrix import _data_parent
		return _data_parent.data( name, value, focus, trackingID,         f )
# ############################# ############################# 

	def audit( self, name, registration=None, focus=None, trackingID=None ):
		try:
			_audit_parent
		except Exception as e:
			from _rightThumb._matrix import _audit_parent
		return _audit_parent.audit( name, registration, focus, trackingID )
# ############################# ############################# 
	def switch( self, name=None, switch=None, expected_input_example = None, isRequired=False, isPipe=False, description='', examples=None, required=None, related=None, isDefault=False, focus=None, trackingID=None,         f=None, printFocus=False ):
		self.load_switches = True
		try:
			_switch_parent
		except Exception as e:
			from _rightThumb._matrix import _switch_parent
		return _switch_parent.switch( name, switch, expected_input_example, isRequired, isPipe, description, examples, required, related, isDefault, focus, trackingID,         f, printFocus )
# ############################# ############################# 
	def table( self, name, registration=None, focus=None, trackingID=None ):
		try:
			_table_parent
		except Exception as e:
			from _rightThumb._matrix import _table_parent
		return _table_parent.table( name, registration, focus, trackingID )
# ############################# ############################# 
	def db( self, name, registration=None, focus=None, trackingID=None ):
		try:
			_db_parent
		except Exception as e:
			from _rightThumb._matrix import _db_parent
		return _db_parent.db( name, registration, focus, trackingID )
# ############################# ############################# 
	def focus( self, name, registration=None, focus='live', trackingID=None ):
		try:
			_focus_parent
		except Exception as e:
			from _rightThumb._matrix import _focus_parent
		return _focus_parent.focus( name, registration, focus, trackingID )
	# ############################# 
	def reg( self, name, registration=None, focus=None, trackingID=None ):
		try:
			_reg_parent
		except Exception as e:
			from _rightThumb._matrix import _reg_parent
		return _reg_parent.reg( name, registration, focus, trackingID )
# ############################# ############################# 
	def process( self, name, description=None, isIF=None, focus=None, trackingID=None,        d=None, i=None, f=None ):
		try:
			_process_parent
		except Exception as e:
			from _rightThumb._matrix import _process_parent
		return _process_parent.process( name, description, isIF, focus, trackingID,        d, i, f )
# ############################# ############################# 
	def procedure( self, name, registration=None, focus=None, trackingID=None ):
		try:
			_procedure_parent
		except Exception as e:
			from _rightThumb._matrix import _procedure_parent
		return _procedure_parent.procedure( name, registration, focus, trackingID )
# ############################# ############################# 
	def task( self, name, registration=None, focus=None, trackingID=None ):
		try:
			_task_parent
		except Exception as e:
			from _rightThumb._matrix import _task_parent
		return _task_parent.task( name, registration, focus, trackingID )
# ############################# ############################# 
	e = ext
	external = ext

	n = nuc

	s = switch
	switches = switch

	adt = audit

	d = data

	a = asyn
	asynchronous = asyn

	t = table
	tables = table

	database = db
	databases = db

	f = focus

	r = reg
	registration = reg

	ps = process
	processes = process

	pr = procedure
	procedures = procedure



	tk =  task
	tasks =  task

#       self.records['']          = {}
#       self.records['ext']       = {}
#       self.records['nuc']       = {}
#       self.records['asyn']     = {}
#       self.records['data']      = {}
#       self.records['audit']     = {}
#       self.records['switch']    = {}
#       self.records['table']     = {}
#       self.records['db']        = {}
#       self.records['focus']     = {}
#       self.records['reg']       = {}
#       self.records['process']   = {}
#       self.records['procedure'] = {}
#       self.records['task']      = {}
#       self.records['']          = {}


# __child
# _ext_child
# _nuc_child
# _async_child
# _data_child
# _audit_child
# _switch_child
# _table_child
# _db_child
# _focus_child
# _reg_child
# _process_child
# _procedure_child
# _task_child
# __child


#       self.indexes['labels']['']          = []
#       self.indexes['labels']['ext']       = []
#       self.indexes['labels']['nuc']       = []
#       self.indexes['labels']['async']     = []
#       self.indexes['labels']['data']      = []
#       self.indexes['labels']['audit']     = []
#       self.indexes['labels']['switch']    = []
#       self.indexes['labels']['table']     = []
#       self.indexes['labels']['db']        = []
#       self.indexes['labels']['focus']     = []
#       self.indexes['labels']['reg']       = []
#       self.indexes['labels']['process']   = []
#       self.indexes['labels']['procedure'] = []
#       self.indexes['labels']['task']      = []
#       self.indexes['labels']['']          = []


#E61F59D5






	def processSwitches( self ):
		appDBA = self.c(c=1)['file']
		# global appReg
		global mainApp
		if not appDBA == mainApp:
			return None

		global switchDelim
		global switchDelimReplace
		appReg = mainApp
		# if appDBA == mainApp:
		if True:
			active = {}
			lastActive = None
			arg = list(sys.argv)
			for i,a in enumerate(arg):
				if a in self.help_switches.split(','):
					self.help()
			for i,a in enumerate(arg):
				found = False
				for ii,key in enumerate(self.records['switch'].keys()):
					# _.pr(mainApp,appDBA,'\t',self.label( key, appDBA ))
					if not self.records['switch'][key].isDefault:
						for s in self.records['switch'][key].switches.split(','):

							if s.lower() == a.lower():
								if self.records['switch'][key].appReg == appReg:
									found = True
									active[ self.records['switch'][key].name ] = []
									lastActive = self.records['switch'][key].name
									active[ lastActive ].append( i )

				if not found and not lastActive is None:
					active[ lastActive ].append( i )

		for key in active.keys():
			for i, x in enumerate(active[key]):
				if not i:
					self.records['switch'][self.label( key, appDBA )].pos = i
					self.records['switch'][self.label( key, appDBA )].setActive()
					# self.records['switch'][key].pos = i
					# self.records['switch'][key].setActive()
				else:
					
					self.records['switch'][self.label( key, appDBA )].values.append( self.records['switch'][self.label( key, appDBA )].format( arg[x] ) )

			tmp = self.records['switch'][self.label( key, appDBA )].values
			for i,x in enumerate(tmp):
				try:
					tmp[i] = tmp[i].replace( switchDelim, switchDelimReplace )
				except Exception as e:
					pass

			try:
				self.records['switch'][self.label( key, appDBA )].value = switchDelim.join( tmp )
			except Exception as e:
				self.records['switch'][self.label( key, appDBA )].value = tmp

	def viewLog( self ):
		_.colorThis( 'HERE', 'green' )
		for i,record in enumerate(self.algorithmLog):
			_.pr( record )
		_.colorThis( [ '', i, ], 'yellow' )


	def callLocation( self, data, name=None ):
		file = None
		line = None
		function = None
		data = str(data)
		path = data.split('"')[1]
		p = path.split(_v.slash)
		file = p.pop().replace('.py','')
		if file == '__init__':
			one = p.pop()
			two = p.pop()
			file = two+'.'+one

		left = data.split('"')[2].split(' ')
		line = left[len(left)-1].replace( '>', '' )
		function = data.split(' ')[2]
		if function == '<module>':
			return None
		if '_bootstrap' in function:
			return None

		if function == '__init__':
			function = 'CLASS'

		return {
					'name': name,
					'file': file,
					'line': line,
					'function': function,
		}

	def c( self, i=1, depth=0, record=False, isChild=None, callers=False, notChild=None,     r=None, c=None, d=None, nc=None ):
		if not nc is None:
			notChild = nc
		if not d is None:
			depth = d
		if not c is None:
			isChild = c
		if not r is None:
			record = r
		if not isChild is None:
			record=True

		notMatrix = True
		if not notChild is None:
			notMatrix = True
		if not isChild is None:
			notMatrix = True

		callersData = self.callers( i )
		programs = []
		for cd in callersData:
			if cd['file'] in program_registration_list:
				programs.append(cd['file'])

		result = callersData
		if True and record:
			result = {
						'file': callersData[depth]['file'],
						'function': callersData[depth]['function'],
						'line': callersData[depth]['line'],
						'programs': programs,
						'name': callersData[depth]['name'],
			}
			if notMatrix and result['file'] == self.theMatrix:
				depth+=1
				if len(callersData)-1 >= depth:
					result = {
								'file': callersData[depth]['file'],
								'function': callersData[depth]['function'],
								'line': callersData[depth]['line'],
								'programs': programs,
								'name': callersData[depth]['name'],
					}
			if not notChild is None and notChild:
				error = False
				while result['file'] in self.childFiles and not error:
					depth+=1
					try:
						result = {
									'file': callersData[depth]['file'],
									'function': callersData[depth]['function'],
									'line': callersData[depth]['line'],
									'programs': programs,
									'name': callersData[depth]['name'],
						}
					except Exception as e:
						error = True
				if error:
					result['error'] = 'notChild excede i'


		if callers and type(result) == dict:
			return { 'caller': result, 'stack': callersData }
		return result

	def callers( self, i=1 ):
		callers = []
		error=False
		while not error:

			try:
				try:
					try:
						n = ''+sys._getframe(i).f_back.f_locals['registration']['name']+''
					except Exception as e:
						n = ''
					if n == '':
						try:
							n = ''+sys._getframe(i).f_back.f_locals['name']+''
						except Exception as e:
							n = ''
					if n == '':
						try:
							n = ''+sys._getframe(i).f_back.f_locals['self'].name+''
						except Exception as e:
							n = ''

					x = self.callLocation(  sys._getframe(i).f_back.f_code, n  )



				except Exception as e:
					x = None
					# x = dir(sys._getframe(i))
				xxx = sys._getframe(i).f_code.co_name

				if '_bootstrap' in xxx:
					error=True
				else:
					if not x is None:
						callers.append(x)

			except Exception as e:
				error=True
			i+=1
		return callers

	def algorithmIncrement( self, record, config=None ):
		add = {
					'epoch': time.time(),
					'config': config
		}
		self.algorithmLog[ record['id'] ]['increment'].append( add )
		
	def algorithmResult( self, record, result=None ):
		# return result
		self.algorithmLog[ record['id'] ]['end'] = time.time()
		self.algorithmLog[ record['id'] ]['mem'] = _.get_size(result)
		return result

	def algorithmRegister( self, trackingID=None, result=None, note=None, documentation={} ):
		self.algorithmID+=1
		stack = self.c(c=1,callers=True)

		record = { 'id': self.algorithmID, 'start': time.time(), 'end': None, 'mem': None, 'caller': stack['caller'], 'stack': stack['stack'], 'increment': [] }
		for key in documentation.keys():
			record[key] = documentation[key]

		if not trackingID is None:
			record['trackingID'] = trackingID
		if not result is None:
			record['result'] = result
		if not note is None:
			record['note'] = note
		if not trackingID is None:
			_.colorThis( '_______________________________________', 'yellow' )
			_.printVar(record)
			_.colorThis( '_______________________________________', 'yellow' )
		self.algorithmLog[ self.algorithmID ] = record
		
		self.ifSet.append(record)

		# if not trackingID is None:
		#   self.ifSetAction[trackingID].append( record )

		self.counter( 'algorithm', stack['caller']['file'], stack['caller']['function'] )
		return record

	pass

	def counter( self, label, child, algorithm ):
		return None
		if child in self.sequences.keys():
			# _.pr( '\t\t ***************** \t\t', child, algorithm, self.sequences )
			if not label in self.sequences[child].keys():
				# _.pr('reset A')
				self.sequences[child][label] = {}

			if not algorithm in self.sequences[child][label].keys():

				self.sequences[child][label][algorithm] = 0

			self.sequences[child][label][algorithm] += 1
			# _.pr( '\t\t ***************** \t\t', child, label, algorithm, self.sequences[child][label][algorithm] )

	def docIF( self, do, runEval=False, trackingID=None, note=None, documentation={} ):
		documentation['eval'] = runEval
		algorithm = self.algorithmRegister( trackingID=trackingID, note=note, documentation=documentation )
		if runEval:
			return self.algorithmResult( algorithm, result=do )
		else:
			return self.algorithmResult( algorithm, result=eval(do) )

	def totalMemory( self ):
		# return None
		global memoryPrint
		total = 0
		for key in self.records['data'].keys():
			total += _.get_size( self.records['data'][key].value )
			
		for key in self.records['ext'].keys():
			total += _.get_size( self.records['ext'][key].imp )
		callers = self.callers()
		# _.pr( 'memoryPrint:', memoryPrint )
		if memoryPrint:
			_.colorThis({
					'file': callers[0]['file'],
					'fn': callers[0]['function'],
					'before': self.memory,
					'after': total,
					'name': callers[0]['name'],
				},'green')
		
		self.memory = total
		if total > self.memory_max:
			self.memory_max = total
		return total

	def load( self ):
		if self.load_switches:
			self.switch('Default', 'default', isDefault=True, focus='isDefault' )
			# sys.exit()
			self.switch('Help', '?,/?,-?,/h,/help,-help,--help')
			self.switch('Column', '-c,-column', 'size, name')
			self.switch('Sort','-s,-sort', 'Asc:type, Desc:ext')
			self.switch('Debug', '-d,-debug')
			self.switch('Errors', '-e,-Error,-Errors', '8,11 OR hide:8,11')
			self.switch('Timeout', '-t,-Timeout')
			self.switch('GroupBy', '-g,-group,-groupby', 'ext, month')
			self.switch('GroupSpaces', '-gs,-space,-groupspaces')
			self.switch('TableProfile', '-tp,-table',' *;c *;l  h;l header;left  size;l,gs')
			# self.switch('ShortenColumn', '-sc,-shortencolumn')
			self.switch('Long', '-l,-long')
			self.switch('Short', '-sc,-short')
			self.switch('Length', '-length','x3')
			self.switch('Report', '-report')
			self.switch('Plus', '+')
			self.switch('Minus', '-')
			self.switch('PlusOr', '-or')
			self.switch('PlusClose', '+close', '90%')
			self.switch('PrintAutoAbbreviations', ',-printa,-aprint')
			self.switch('LoadEpoch', '-loadepoch')
			self.switch('NoColor', '-nocolor')
			self.lastSwitch = 'NoColor'


def theApp():
	return app,app,app



class AppIntermediate:
	def __init__( self ):
		self.log = []


def sw():
	global switchDelim
	return switchDelim

# app.records['switch'][key].required


def clearFocus( name, file ):
	global mainApp
	global program_registration_list
	f = file.split(_v.slash)
	if name == '__main__':
		# x = '__' + f[len(f)-1].replace('.py','') + '__'
		x = f[len(f)-1].replace('.py','') 
	else:
		x = f[len(f)-1].replace('.py','')
	if mainApp is None:
		mainApp = x
	program_registration_list.append(x)
	return x


def appName( appReg, parentApp='', childApp='' ):
	global delimReg
	if not parentApp == '':
		appReg = appReg + delimReg + parentApp
	if not childApp == '':
		appReg = parentApp + delimReg + appReg
	return appReg

def constructRegistration( file, dba ):
	global registeredAppsAll
	shouldAdd = True
	for ra in registeredAppsAll:
		if ra['dba'] == dba:
			shouldAdd = False
	if shouldAdd:
		registeredAppsAll.append({ 'file': file, 'dba': dba })

def thisApp( file ):
	f = file.split(_v.slash)
	x = f[len(f)-1].replace('.py','')
	return x




def appName( appReg, parentApp='', childApp='' ):
	global delimReg
	if not parentApp == '':
		appReg = appReg + delimReg + parentApp
	if not childApp == '':
		appReg = parentApp + delimReg + appReg
	return appReg


class GenChildLabel:
	def gen( file ):
		parts = file.split(_v.slash)
		result = parts.pop().replace( '.py', '' )
		result = result.split('_')[1]
		return result

delimReg = '|'
program_registration_list = []
registeredAppsAll = []
registeredApps = []
switchDelim = '{E46-F6-A39}'
switchDelimReplace = '{E46F6A39-F3B0-491D-8F87-33354BD4FBAA}'
memoryPrint = False

app = Appp()


end = time.time()



"""
asyn      a    asynchronous
data       d    data
audit      adt  audit
switch     s    switches
table      t    tables
db         db   database
ext        e    external
reg        r    registration
process    ps   processes
procedure  pr   procedures
task       tk   tasks
"""
# type %tmpf0% | p line --c -make "epyi matrix -child {}_child"
# type %tmpf0% | p line --c -make "self.records_{} = { }"
# type %tmpf0% | p line --c -make "'{}': { 'all': 0, 'algorithm': { } }"
# type %tmpf0% | p line --c -make "'{}': { 'names': [] }"
# type %tmpf0% | p line --c -make ""


"""
aRec = __.app.algorithmRegister( 'data', 'add' )
__.app.algorithmIncrement( aRec, {
									'task': None
	} )
algorithmResult( self, aRec, result=None )
"""
# epyi matrix -file _async_child
# epyi matrix -file _audit_child
# epyi matrix -file _data_child
# epyi matrix -file _db_child
# epyi matrix -file _ext_child
# epyi matrix -file _focus_child
# epyi matrix -file _procedure_child
# epyi matrix -file _process_child
# epyi matrix -file _reg_child
# epyi matrix -file _switch_child
# epyi matrix -file _table_child
# epyi matrix -file _task_child

# epyi matrix -file _async_parent
# epyi matrix -file _audit_parent
# epyi matrix -file _data_parent
# epyi matrix -file _db_parent
# epyi matrix -file _ext_parent
# epyi matrix -file _focus_parent
# epyi matrix -file _procedure_parent
# epyi matrix -file _process_parent
# epyi matrix -file _reg_parent
# epyi matrix -file _switch_parent
# epyi matrix -file _table_parent
# epyi matrix -file _task_parent

# epyi matrix -file _async_child

# p genBase4Sections -save

# algorithmRegister

# b matrix
# p file --c | p pipeList -remove .py - __init__

# switch__(
# switch(
# process(
# def totalMemory
# processSwitches(

# ** Make triggers possibly a list of fn or dics
# add script triggers to everything
#   ex data - matrix2 test3 

# def postLoad(
# def c(

# 2385 
# 2437 3239
# 1250 3239

# 21BD8F
# 1F59D5
#########################
# _.pr( end-start )
#########################
memoryPrint = False
mainApp = None
printSwitcheFocus = False



