import os, sys, time

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


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
### EXAMPLE: START
# import simplejson as json
# from threading import Timer
# from lxml import html
# import requests
# import cssselect
# import sqlite3
### EXAMPLE: END
##################################################


def appSwitches():
	pass
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )
	### EXAMPLE: END


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
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
						'p thisApp -file file.txt',
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# date = _.friendlyDate( theDate )
# _.addComma()
### EXAMPLE: END
########################################################################################
# START



try:
	import pyodbc
except Exception as e:
	pass
	
try:
	import ctypes
except Exception as e:
	pass


import threading

from threading import Thread




class ThisThread(threading.Thread):
	
	
	def __init__( self, name, fn=None, a=None, t=None, k=None, timeout=120, start=True ):
		threading.Thread.__init__(self)
		global threadID
		self.tID = threadID
		threadID+=1
		self.name = name
		self.fn = fn
		self.arg = a
		self.kwargs = k

		if not t is None:
			timeout = t

		self.killOn = timeout


		self.epoch = 0
		self.endTime = None
		self.duration = None

		self.wasKilled = False

		self.log = {}

		if start:
			self.start()



		

	def run( self ):
		self.epoch = time.time()
		completed = False
		error = False
		try:
			if not self.arg is None:
				self.fn(self.arg)
			else:
				if self.kwargs is None:
					self.fn()
				elif type(self.kwargs) == dict:
					self.fn(**self.kwargs)
				elif type(self.kwargs) == list or type(self.kwargs) == tuple:
					self.fn(*self.kwargs)
				elif type(self.kwargs) == str:
					self.fn(self.kwargs)
			completed = True
		except Exception as e:
			error = True
		finally:
			self.endTime = time.time()
			self.duration = self.endTime - self.epoch
			# _.pr()
			# _.colorThis(  [ self.tID, 'ended' ], 'red'  )
			ended = ''
			if self.wasKilled:
				ended += ' killed '
			if error:
				ended += ' error '
			if completed:
				ended += ' completed '

			self.log = {
								'id': self.getID(),
								'tID': self.tID,
								'name': self.name,
								'start': self.epoch,
								'end': self.endTime,
								'duration': self.duration,
								'ended': ended,
			}

	def getID( self ):

		for id, thread in threading._active.items():
			if thread is self:
				return id
 
	def kill( self ):
		self.wasKilled = True
		thread_id = self.getID()
		res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
			ctypes.py_object(SystemExit))
		if res > 1:
			ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)









# class ThreadManager:
	
#     def __init__( self ):
#         self.registeredThreads = []
#         self.timeout = 1
#         self.tasks = []
		
#     def wait( self ):
#         length = 0
#         start = time.time()
#         while not len(self.registeredThreads) and length < self.timeout:
#             length = time.time() - start
		
#         if not len(self.registeredThreads):
#             self.done = True

#     def monitor( self ):
#         global log
#         self.done = False
#         while not self.done:
			
#             self.wait()

#             if not self.done:
#                 # _.pr()
#                 # _.pr()
#                 for thisThread in self.registeredThreads:
#                     if not thisThread.killOn is None:
#                         if thisThread.duration is None:

#                             _.pr()
#                             _.pr()
#                             _.pr( '        name:', thisThread.name )
#                             _.pr( 'duration Var:', thisThread.duration )
#                             _.pr( '    duration:', time.time() - thisThread.epoch )
#                             _.pr( '      killOn:', thisThread.killOn )
#                         if thisThread.duration is None and (  time.time() - thisThread.epoch ) > thisThread.killOn:
#                             _.colorThis( 'TIMEOUT', 'red' )
#                             thisThread.kill()
#                             thisThread.join()

#                 # _.pr()
#                 # _.pr()


#                 complete = 0
#                 for thisThread in self.registeredThreads:
#                     if not thisThread.duration is None:
#                         complete += 1

#                 if len( self.registeredThreads ) == complete:
#                     self.done = True

#                 time.sleep(.2)

#         pass
#         # _.printVar( log )
#         self.isExit()


#     def atExit( self, script, args=None, kwargs=False ):
#         self.tasks.append({ 'script': script, 'args': args })

#     def isExit( self ):
#         for task in self.tasks:
#             if task['args'] is None:
#                 task['script']()
#             # elif task is None:
#             #     pass

#         self.tasks.append({ 'script': script, 'args': args })










def handler( arg1='E1', arg2='E2' ):
	i=0
	# asdf
	while True:
		_.pr( i, arg1, arg2 )
		i+=1
		time.sleep(.5)



	# _.printVar( log )





def test():

	threadID = registerThread()

	cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};User=root;Password=;Database=theworld;Server=127.0.0.1;Port=3306;String Types=Unicode')
	# cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};User ID=myuserid;Password=pwdpwd;Server=127.0.0.1;Database=sys;Port=3306;String Types=Unicode')
	cursor = cnxn.cursor()

	# cursor.execute("""
	#                         CREATE TABLE Persons (
	#                             PersonID int,
	#                             LastName varchar(255),
	#                             FirstName varchar(255),
	#                             Address varchar(255),
	#                             City varchar(255)
	#                         );
	# """)
	# cursor.execute("SHOW TABLES")
	# rows = cursor.fetchall()
	# # _.pr( rows[1] )
	# for row in rows:
	#     _.pr(row)





	# cursor.execute("""
	#                     INSERT INTO Persons (PersonID, LastName, FirstName, Address, City )
	#                     VALUES ( 1, 'Reph', 'Scott', '4477 Amberly Oaks Court', 'Tampa' );
	# """)
	# cnxn.commit()
	# _.pr( 'Added' )

	start = time.time()
	loops = 20

	i=0
	while i < loops:
		i+=1

		while requestAccess( 'database', threadID ): pass

		cursor.execute("SELECT LastName, FirstName FROM Persons ")
		rows = cursor.fetchall()
	end = time.time()
	total = end - start
	average = total / loops
	_.pr(  )
	_.pr( 'Loops:', loops )
	_.pr( 'Total milliseconds:', total )
	_.pr( 'Average:', average )



	# _.pr( rows[1] )
	# for row in rows:
	#     _.pr(row)

class Asset_Manager:

	def __init__( self ):

		self.asset_rest = {}

		self.indexes = {}
		self.assets = {}
		self.threads = []
		self.transactions = []

		self.tables = [
							'assets',
							'data_table_1000_2000',
							'data_table_2000_3000',
							'data_table_3000_4000',
							'data_table_4000_5000',
							'data_table_500_1000',
							'data_table_manager',
							'request',
							'terminals'
		]

		self.sql_factors = [
								{ 'command': 'select', 'scan': 'join id uuid terminal like % = < > del and where -( ( sum( concat( month( between * , \' " group-by order-by or completed expired -0- -1- isloaded' },
								{ 'command': 'insert', 'scan': ', \' "' },
								{ 'command': 'update', 'scan': ', \' " % = < > and or -0- -1- between like active_on del isloaded' },
								{ 'command': 'create', 'scan': ', \' "' },
		]




		


		# status:
		#         0 free
		#         1 in use
		#         2 in waiting

		self.sql_statistics_factored = {}


	def wait( self, timer='full' ):

		pass

	def registerThread( self ):

		thisID = _.genUUID()
		self.threads.append( thisID )
		for i,x in self.threads:
			if x == thisID:
				self.indexes[thisID] = i
		for key in self.assets.keys():
			self.assets[key]['threads'][thisID] = 0

	def registerAsset( self, asset, rest=0.001 ):
		



		self.assets[asset] = { 'status': 0, 'epoch': 0, 'rest': rest, 'threads': {} }
		for thread in self.threads:
			self.assets[key]['threads'][thread] = 0

	def restA( self ):
		# time.sleep(0.001)
		i=0
		while i<2000:
			i+=1
			pass

	def requestAccess( self, asset, threadID ):
		self.assets[asset]['threads'][threadID] = time.time()
		rest = self.assets[asset]['rest']
		epoch = self.assets[asset]['epoch']

		while self.assets[asset]['status']:
			self.restA()


		while (  time.time() - epoch  ) > rest:
			pass

		while self.checkQueue( self, asset, threadID ):
			self.restA()
		self.assets[label]['status'] = 1
		self.last_start[asset] = time.time()
		return True


	def checkQueue( self, asset, threadID ):
		queue = []
		for thread in self.assets[asset]['threads'].keys():
			if self.assets[asset]['threads'][thread] > 0:
				queue.append( self.assets[asset]['threads'][thread] )
		queue.sort()
		queue.reverse()
		if self.assets[asset]['threads'][threadID] == queue[0]:
			return True
		else:
			return False

	# def accessStart( self, asset, threadID ):
	#     self.assets[asset]['epoch'] = time.time()
	#     self.last_start = time.time()
	def omitIt( self ):
		omitIs = ['and', 'or'," ' ", ' " ', ' % ', '0', '1', 'select', ' = ', ' < ', ' > ', ' , ' ]
		for x in self.sql_factors:
			for o in x['scan'].split(' '):
				good = True
				for oo in o:
					if not oo in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_':
						good = False


				if good:
					if not o in omitIs:
						omitIs.append(o)
				else:
					if not ' '+o+' ' in omitIs:
						omitIs.append(' '+o+' ')
		return omitIs

	def accessEnd( self, asset, threadID, sql=None ):

		if sql is None:
			self.transactions.append({
										'start': self.last_start[asset],
										'end': end,
										'duration': end - self.last_start[asset],
										'asset': factors,
										'thread': threadID,
				})

		if not sql is None:

			omitIs = self.omitIt()
			omitHas = ['  ']



			sql = ' '+sql+' '
			sql = sql.lower()
			sql = sql.replace( '\n', ' \n ' )
			sql = sql.replace( '\t', ' ' )
			sql = sql.replace( '=', ' = ' )
			tables = []
			factors = {}
			end = time.time()
			for table in self.tables:
				if table in sql:
					tables.append(table)
			for factor in self.sql_factors:
				if factor['command'] in sql:
					factors[factor['command']] = {}
					for scan in factor['scan'].split(' '):
						if len(scan):
							# omitIs omitHas
							if not scan.replace( '-', ' ' ) in omitIs and scan.replace( '-', ' ' ) in sql:
								good = True
								for oHas in omitHas:
									if oHas in scan.replace( '-', ' ' ):
										good = False
								if good:
									try:
										factors[factor['command']][scan.replace( '-', ' ' )] += 1
									except Exception as e:
										factors[factor['command']][scan.replace( '-', ' ' )] = 1
							elif not ' '+scan+' ' in omitIs and ' '+scan+' ' in sql:
								good = True
								for oHas in omitHas:
									if oHas in ' '+scan+' ':
										good = False
								if good:
									try:
										factors[factor['command']][scan] += 1
									except Exception as e:
										factors[factor['command']][scan] = 1
							elif not scan in omitIs and scan in sql:
								good = True
								for oHas in omitHas:
									if oHas in scan:
										good = False
								if good:
									try:
										factors[factor['command']][scan] += 1
									except Exception as e:
										factors[factor['command']][scan] = 1



			pass
			self.transactions.append({
										'start': self.last_start[asset],
										'end': end,
										'duration': end - self.last_start[asset],
										'asset': factors,
										'thread': threadID,
										'tables': tables,
										'factor': factors,
				})
		self.assets[key]['threads'][threadID] = 0
		self.assets[label]['epoch'] = time.time()
		self.assets[label]['status'] = 0






"""
##############################
next steps

	uuid label in thread
		

		while requestAccess( 'database', threadID ): time.sleep(0.001)


	releaseAsset( 'database', threadID )    
	managed_asset_queue
		register assets
			type label

		register threads 
			each thread per asset OR add on FIRST request of access



	START THREAD PER EACH ASSET

	thread registration of label 


##############################
"""

class Manage:
	def __init__( self ):
		self.threadMonitorFirstRun = True
		self.threads = []
		self.log = []

	def threadMonitor( self ):
		
		if self.threadMonitorFirstRun:
			self.threadMonitorFirstRun = False
			Thread(target=self.threadMonitor).start()
			return None
		
		
		done = False
		while not done:
			# _.pr()
			# _.pr()
			for thisThread in self.threads:
				if not thisThread.killOn is None:
					if thisThread.duration is None:

						_.pr()
						_.pr()
						_.pr( '        name:', thisThread.name )
						_.pr( 'duration Var:', thisThread.duration )
						_.pr( '    duration:', time.time() - thisThread.epoch )
						_.pr( '      killOn:', thisThread.killOn )
					if thisThread.duration is None and (  time.time() - thisThread.epoch ) > thisThread.killOn:
						_.colorThis( 'TIMEOUT', 'red' )
						thisThread.kill()
						thisThread.join()

			# _.pr()
			# _.pr()


			complete = 0
			for thisThread in self.threads:
				if not thisThread.duration is None:
					complete += 1

			if len( self.threads ) == complete:
				done = True

			time.sleep(.2)

	def register( self, name=None, fn=None, a=None, t=None, k=None, timeout=120, start=True ):
		if name is None:
			name = _.genUUID()
		
		self.threads.append(
			ThisThread(
						name = name,
						fn = fn,
						a = a,
						t = t,
						k = k,
						timeout = timeout,
						start = start,
			)
		)
		if self.threadMonitorFirstRun:
			self.threadMonitor()



threadID = 0
log = {}
manager = Manage()



def action():
	pass
	"""
	import _rightThumb._simpleThreads as _threads

	
	_threads.manager.register(
		name = 'Test 2',
		fn = self.terminal,
		timeout = None
	)


	
	"""


########################################################################################
if __name__ == '__main__':
	action()






