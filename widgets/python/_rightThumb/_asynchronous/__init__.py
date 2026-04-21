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
# import platform

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
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': '_rightThumb._asynchronous',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'asynchronous',
	'categories': [
						'asynchronous',
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
						'p portscanner',
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
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
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
# for i,row in enumerate(_.isData(r=1)):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START




import threading
import ctypes
import time

from threading import Thread




class ThisAsyncThread(threading.Thread):
	
	
	def __init__( self, name, category, fn=None, a=None, t=None, k=None, p=0, timeout=120, start=True ):
		threading.Thread.__init__(self)
		global threadID
		self.tID = threadID
		threadID+=1
		self.name = name
		self.category = category
		self.fn = fn
		self.arg = a
		self.priority = p
		self.kwargs = k
		self.status = 0
		if not t is None:
			timeout = t

		self.killOn = timeout


		self.epoch = 0
		self.endTime = None
		self.duration = None

		self.wasKilled = False

		self.log = {}

		if start:
			self.status = 1
			self.start()



	def check( self ):
		if self.is_alive():
			self.status = 1
		return self.status

		

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
			self.status = 2
			if self.wasKilled:
				self.status = 3
				ended += ' killed '
			if error:
				self.status = 4
				ended += ' error '
			if completed:
				self.status = 2
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

















def handler( arg1='E1', arg2='E2' ):
	i=0
	# asdf
	while True:
		_.pr( i, arg1, arg2 )
		i+=1
		time.sleep(.5)










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



def action():

	# mgr = ThreadManager()
	# Thread(target=mgr.monitor).start()
	# # mgr.monitor

	# mgr.registeredThreads.append(
	#                 ThisThread(
	#                             name = 'Test 1',
	#                             fn = test,
	#                             # k = { 'arg1': 'a', 'arg2': 'b' },
	#                             timeout = None
	#                 )
	# )


	global registeredThreads

	registeredThreads.append(
					ThisThread(
								name = 'Test 1',
								fn = test,
								# k = { 'arg1': 'a', 'arg2': 'b' },
								timeout = None
					)
	)


	registeredThreads.append(
					ThisThread(
								name = 'Test 2',
								fn = test,
								timeout = None
					)
	)


	threadMonitor()    

	time.sleep(5)
	_.pr( 'killing' )
	# registeredThreads[0].kill()
	# registeredThreads[0].join()
	# _.pr( 'fin' )
	sys.exit()


# name, fn=None, a=None, t=None, k=None, timeout=120, start=True 









	# t1 = ThisThread('Test 1')
	# t1.function( handler, 99 )
	# t1.function( handler, k={ 'arg1': 'a', 'arg2': 'b' } )
	# t1.function( handler, k=( 'c', 'd' ) )
	# t1.start()
	# time.sleep(2)
	# t1.kill()
	# t1.join()

	# _.printVarSimple( log )




threadID = 0
log = {}
registeredThreads = []
threadMonitorFirstRun = True



class Asynchronous:
	
	def __init__( self ):
		self.started = time.time()
		self.THREADS = []
		self.timeout = 1
		self.tasks = []

		self.threadID = 0
		self.log = {}
		self.threadMonitorFirstRun = True

		self.queue = []
		self.queue_structure = {}

		self.categories = {}

		self.fully_loaded = False
		self.priority_max = 1
		self.max = 100
		self.last_activity = time.time()
		self.load = 1
		self.loaded = False
		self.monitor_running = False
		self.statuses = None
		self.print = False
		self.category_hash = {}

		self.completed_table = []

		self.recent_running = []
		self.recent = 10
		self.recentMin = 1

		self.pause = None
		self.pauseOn = None
		self.pauseFor = 5
		self.running_total = 0
		self.print = 0
		# self.pauseOn = 50
		# self.pauseFor = 10

	def web( self, m=20, safe=2, p=1, pf=None, po=None ):
		self.max = m

		self.print = p
		
		
		if safe:
			if safe >= 1:
				self.pause = .05
			if safe >= 2:
				self.pauseOn = 50
				self.pauseFor = 2

			if safe >= 3:
				self.pauseOn = 25
				self.pauseFor = 2

			if not pf is None:
				self.pauseFor = pf
				
			if not po is None:
				self.pauseOn = po


	def np( self , name, priority ):
		self.last_activity = time.time()
		self.categories[name] = priority

	def cp( self , category, priority ):
		self.last_activity = time.time()
		self.categories[category] = priority


	def category_hash_manager( self, name=None, category=None, e=None, t=None, add=None, reset=None, aa=None, ad=None ):
		if not reset is None:
			for category in self.category_hash:
				self.category_hash[category]['record']['active'] = 0
				self.category_hash[category]['record']['done'] = 0
				for name in self.category_hash[category]['children']:
					self.category_hash[category]['children'][name]['active'] = 0
					self.category_hash[category]['children'][name]['done'] = 0

		if not category in self.category_hash:
			self.category_hash[ category ] = { 'record': {}, 'children': {} }
			self.category_hash[ category ]['record'] = {
															'epoch': time.time(),
															'total': 0,
															'active': 0,
															'done': 0,
			}

		if not name in self.category_hash[ category ]['children']:
			self.category_hash[ category ]['children'][ name ] = {
															'epoch': time.time(),
															'total': 0,
															'active': 0,
															'done': 0,
			}


		if not e is None:
			self.category_hash[ category ]['record']['epoch'] = time.time()
			self.category_hash[ category ]['children'][ name ]['epoch'] = time.time()

		if not add is None:
			self.category_hash[ category ]['record']['total'] += 1
			self.category_hash[ category ]['children'][ name ]['total'] += 1

		if not aa is None:
			self.category_hash[ category ]['record']['active'] += 1
			self.category_hash[ category ]['children'][ name ]['active'] += 1

		if not ad is None:
			self.category_hash[ category ]['record']['done'] += 1
			self.category_hash[ category ]['children'][ name ]['done'] += 1



		self.completed_table = []
		
		try:
			for category in self.category_hash:
				if self.category_hash[category]['record']['done'] == self.category_hash[category]['record']['total']:
					self.completed_table.append({ 'category': category, 'name': None })
				for name in self.category_hash[category]['children']:
					if self.category_hash[category]['children'][name]['done'] == self.category_hash[category]['children'][name]['total']:
						self.completed_table.append({ 'category': category, 'name': name })
		except Exception as e:
			pass


	def register( self, name='default', category='default', fn=None, a=None, t=None, k=None, p=None, timeout=120, start=True ):

		self.category_hash_manager(  name, category, e=True, add=True  )


		self.last_activity = time.time()
		if not self.monitor_running:
			self.monitor_running = True
			Thread(target=self.monitor).start()
		if p is None:
			if name in self.categories:
				if type(self.categories[name]) == int:
					p = self.categories[name]
				elif type(self.categories[name]) == dict and 'priority' in self.categories[name]:
					p = self.categories[name]['priority']
				elif type(self.categories[name]) == dict and 'p' in self.categories[name]:
					p = self.categories[name]['p']
			elif category in self.categories:
				if type(self.categories[category]) == int:
					p = self.categories[category]
				elif type(self.categories[category]) == dict and 'priority' in self.categories[category]:
					p = self.categories[category]['priority']
				elif type(self.categories[category]) == dict and 'p' in self.categories[category]:
					p = self.categories[category]['p']
			else:
				p = 1
		
		if p > self.priority_max:
			self.priority_max
		self.queue.append({
								'status':     0,
								'record':     {
												'name':        name,
												'category':    category,
												'fn':         fn,
												'a':          a,
												't':          t,
												'k':          k,
												'p':          p,
												'timeout':     timeout,
												'start':    start
											},
		})

		if not category in self.queue_structure:
			self.queue_structure[ category ] = {}
		if not name in self.queue_structure[ category ]:
			self.queue_structure[ category ][ name ] = {  ''  }



	def activateThread( self, i ):
		self.last_activity = time.time()
		self.THREADS.append(
									ThisAsyncThread(
													name=         self.queue[i]['record']['name'],
													category=     self.queue[i]['record']['category'],
													fn=            self.queue[i]['record']['fn'],
													a=            self.queue[i]['record']['a'],
													t=            self.queue[i]['record']['t'],
													k=            self.queue[i]['record']['k'],
													p=            self.queue[i]['record']['p'],
													timeout=    self.queue[i]['record']['timeout'],
													start=        self.queue[i]['record']['start']
									)
		)

		self.queue[i]['status'] = 1

	def isComplete( self ):
		self.status_check()
		loaded = False


		t = time.time() - self.last_activity
		if  t >= self.load:
			loaded = True
		
		if self.loaded:
			loaded = True

		self.processExits()


		if not len( self.THREADS ) == self.statuses['done']:
			loaded = False
			# _.pr( 'nl:', 1, len( self.THREADS ), self.statuses['done'] )

		if not len(self.THREADS) == len(self.queue):
			loaded = False
			# _.pr( 'nl:', 2, len(self.THREADS), len(self.queue) )

		return loaded

		# and self.fully_loaded and
	def queue_manager( self ):
		self.status_check()
		index = {}
		if self.priority_max > 1:
			for x in range(1,self.priority_max):
				index[str(x)] = []
		if not '1' in index:
			index['1'] = []
		for x in self.categories:
			if not str(self.categories[x]) in index:
				index[ str(self.categories[x]) ] = []


		index = _.dic_key_sort2( index, n=True )

		# self.statuses
		for i, item in enumerate(self.queue):

			if item['status'] == 0:
				index[ str(item['record']['p']) ].append( i )

		cnt = 1
		if self.statuses['running'] + cnt > self.max:
			return None
		for p in index:
			for i in index[p]:
				if self.statuses['running'] + cnt > self.max:
					return None
				self.running_total += 1
				if not self.pauseOn is None:
					if self.running_total % self.pauseOn == 0:
						# _.updateLine( 'pause                                                                                        ' )
						# _.pr( 'pause' )
						time.sleep( self.pauseFor )
						# _.updateLine( 'resume                                                                                        ' )
						# _.pr( 'resume' )

				DONE = False
				while not DONE:
					try:
						self.activateThread( i )
						DONE = True
					except Exception as e:
						DONE = False
						time.sleep(.5)
				if not self.pause is None:
					time.sleep( self.pause )
				cnt += 1


	def status_check( self ):
		self.statuses = {
							'running': 0,
							'done': 0,
							
							'complete': 0,
							'queue': 0,
							'timeout': 0,
							'errors': 0,

							'total-queue': len(self.queue),
							'total-threads': len(self.THREADS),
							'not-scheduled': 0,
		}


		self.category_hash_manager( reset=True )

		for thread in self.THREADS:
			status = thread.check()

			if status > 1:
				self.category_hash_manager( thread.name, thread.category, ad=True )
				self.statuses['done'] += 1

			if status == 3:
				self.statuses['timeout'] += 1
			elif status == 4:
				self.statuses['errors'] += 1
			elif status == 2:
				self.statuses['complete'] += 1
			elif status == 1:
				self.statuses['running'] += 1
				self.category_hash_manager( thread.name, thread.category, aa=True )
			elif status == 0:
				self.statuses['not-scheduled'] += 1

		self.recent_running.append( int(self.statuses['running']) )


	def wait( self ):
		length = 0
		start = time.time()
		while not len(self.THREADS) and length < self.timeout:
			length = time.time() - start
		
		# if not len(self.THREADS):
		#     self.done = True


	def monitor( self ):
		global log
		self.done = False
		while not self.done:
			self.queue_manager()
			self.wait()

			if not self.done:
				# _.pr( 'monitor:', int( time.time() - self.started ) )
				# _.pr()
				# _.pr()
				for thread in self.THREADS:
					if not thread.killOn is None:
						if thread.duration is None:
							pass
							# _.pr()
							# _.pr()
							# _.pr( '        name:', thread.name )
							# _.pr( 'duration Var:', thread.duration )
							# _.pr( '    duration:', time.time() - thread.epoch )
							# _.pr( '      killOn:', thread.killOn )
						if thread.duration is None and (  time.time() - thread.epoch ) > thread.killOn:
							_.colorThis( 'TIMEOUT', 'red' )
							thread.kill()
							thread.join()

				# _.pr()
				# _.pr()

				# self.status_check()
				# _.printVarSimple( self.statuses )

				# len( self.THREADS ) == self.statuses['done'] and len(self.THREADS) == len(self.queue) and self.fully_loaded and   

				if self.isComplete():
					self.done = True
				
				if self.print:
					if self.print < 2:
						_.updateLine( '                                                                                        ' )
					status_update = ''
					# status_update += 'Thread Manager: '
					status_update += 'Running: '
					# status_update += str(self.statuses['running'])
					# status_update += _.cp(str(self.statuses['running']),'yellow',p=0)
					status_update += _.cp( self.recently() ,'yellow',p=0)
					status_update += ' \t Done: '
					status_update += _.cp(str(_.percentageDiffIntAuto( self.statuses['done'], self.statuses['total-queue']  ))+'%  ','yellow',p=0)
					# status_update += str(self.statuses['done'])
					status_update += _.cp(_.addComma(self.statuses['done']),'green',p=0)
					# status_update += '\t'
					status_update += ' of '
					# status_update += str(self.statuses['total-queue'])
					status_update += _.cp(_.addComma(self.statuses['total-queue']),'cyan',p=0)
					if self.statuses['timeout']:
						status_update += '\t'
						status_update += 'Timeout: '
						status_update += _.cp(_.addComma(self.statuses['timeout']),'red',p=0)
					if self.statuses['errors']:
						status_update += '\t'
						status_update += 'Errors: '
						status_update += _.cp(_.addComma(self.statuses['errors']),'red',p=0)
					status_update += '                                       '

					# _.pr( status_update )
					if self.print > 1:
						_.pr( status_update )
					else:
						_.pr( status_update, end='\r' )

					# _.cp( status_update, 'cyan' )

				time.sleep(.2)

		pass
		# _.printVarSimple( log )
		if self.print == 1:
			_.updateLine( '                                                                                           ' )
		self.isExit()


	def recently( self ):
		recent = []
		recentTMP = []
		recent_running = self.recent_running.copy()
		recent_running.reverse()
		for i,x in enumerate(recent_running):
			if len(recent) <= self.recent:
				recentTMP.append( x )
				if x > self.recentMin:
					recent.append( x )

		recent.sort()
		recentTMP.sort()
		if not len(recent) and not len(recentTMP):
			return '0'
		if not len(recent):
			return str( recentTMP[ len(recentTMP)-1 ] )

		else:
			l = recent[0]
			m = recent[ len(recent)-1 ]
			if l == m:
				return str(m)
			else:
				return str(l)+'-'+str(m)


		


	def processExits( self ):
		if not len(self.completed_table):
			return None

		for i,task in enumerate(self.tasks):
			pass
			status = 0
			shouldRun = False


			for ct in self.completed_table:
				if task['name'] is None and ct['name'] is None and ct['category'] == task['category']:
					shouldRun = True
				elif task['category'] is None and ct['category'] is None and ct['name'] == task['name']:
					shouldRun = True
				elif task['category'] is None and ct['category'] is None and ct['name'] is None and task['name'] is None:
					pass
				elif task['category'] == ct['category'] and ct['name'] == task['name']:
					shouldRun = True





			if shouldRun:
				if not task['status'] == 0:
					shouldRun = False
				
			if shouldRun:
				try:
					if not task['arg'] is None:
						task['script'](task['arg'])
					else:
						if task['kwargs'] is None:
							task['script']()
						elif type(task['kwargs']) == dict:
							task['script'](**task['kwargs'])
						elif type(task['kwargs']) == list or type(task['kwargs']) == tuple:
							task['script'](*task['kwargs'])
						elif type(task['kwargs']) == str:
							task['script'](task['kwargs'])
					status = 1
				except Exception as e:
					status = 2

			pass
			self.tasks[i]['status'] = status
	

	def atExit( self, name=None, category=None, fn=None, a=None, k=None ):
		self.tasks.append({ 'name': name, 'category': category, 'script': fn, 'arg': a, 'kwargs': k, 'status': 0 })

	def isExit( self ):
		for i,task in enumerate(self.tasks):
			pass
			status = 0
			shouldRun = False

			if self.tasks[i]['status'] == 0:
				shouldRun = True

				
			if shouldRun:
				time.sleep(1.5)
				status = 3
				try:
					if not task['arg'] is None:
						task['script'](task['arg'])
					else:
						if task['kwargs'] is None:
							task['script']()
						elif type(task['kwargs']) == dict:
							task['script'](**task['kwargs'])
						elif type(task['kwargs']) == list or type(task['kwargs']) == tuple:
							task['script'](*task['kwargs'])
						elif type(task['kwargs']) == str:
							task['script'](task['kwargs'])
					status = 1
				except Exception as e:
					status = 2

			
				self.tasks[i]['status'] = status


			# elif  is None:

		# self.tasks.append({ 'script': script, 'args': args })




__.asyn = Asynchronous()
asynchronous = __.asyn
_async = __.asyn
manage = __.asyn

# import _rightThumb._asynchronous as _async


# _async = _.regImp( __.appReg, '_rightThumb._asynchronous' )
# _async.imp.manage.register( fn=test )








