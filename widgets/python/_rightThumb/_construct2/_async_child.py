import threading

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import ctypes
import time
from threading import Thread
import _rightThumb._construct2 as __
import _rightThumb._base3 as _


isTest = 3
isTest = 2
isTest = 0
threadID = 0
records = {}

log = []


class TheChild:
	def __init__( self, theID, registration ):
		__.app.sequences['async']['algorithm'] = {}
		global records
		self.id = theID
		self.ids = []
		self.registration = registration
		records[self.id] = []
		self.add( theID, registration )



	def add( self, theID, registration ):
		__.app.algorithmRegister( 'async', 'add' )
		self.ids.append( theID )
		global records
		kwargs = None
		timeout = None
		name = ''
		trigger = None
		trigger_kwargs = None
		trigger_timeout = None
		self.focus = registration['focus']
		if 'name' in registration.keys():
			name = registration['name']

		if 'timeout' in registration.keys():
			timeout = registration['timeout']
		if 'k' in registration.keys():
			kwargs = registration['k']
		if 'kwargs' in registration.keys():
			kwargs = registration['kwargs']

		if 'trigger' in registration.keys():
			trigger = registration['trigger']

		if 'tkwargs' in registration.keys():
			trigger_kwargs = registration['tkwargs']
		
		if 'ttimeout' in registration.keys():
			trigger_timeout = registration['ttimeout']


		
		if kwargs is None:
			records[self.id].append(
							ThisThread(
										theID = theID,
										name = name,
										fn = registration['script'],
										# k = { 'arg1': 'a', 'arg2': 'b' },
										timeout = timeout,
										trigger = trigger,
										trigger_kwargs = trigger_kwargs,
										trigger_timeout = trigger_timeout,
							)
			)
		elif not kwargs is None:
			records[self.id].append(
							ThisThread(
										theID = theID,
										name = name,
										fn = registration['script'],
										k = kwargs,
										timeout = timeout,
										trigger = trigger,
										trigger_kwargs = trigger_kwargs,
										trigger_timeout = trigger_timeout,
							)
			)

		global threadMonitorActive
		if not threadMonitorActive:
			threadMonitor()


class ThisThread(threading.Thread):
	
	
	def __init__( self, theID, name, fn=None, a=None, t=None, k=None, timeout=120, start=True, trigger=None, trigger_kwargs=None, trigger_timeout=None  ):
		threading.Thread.__init__(self)
		global threadID
		self.tID = threadID
		threadID+=1
		self.name = name
		self.fn = fn
		self.arg = a
		self.kwargs = k
		self.trigger = trigger
		self.trigger_kwargs = trigger_kwargs
		self.trigger_timeout = trigger_timeout

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
			ended = ''
			if self.wasKilled:
				ended += ' killed '
			if error:
				ended += ' error '
			if completed:
				ended += ' completed '
			global isTest
			if isTest:
				_.colorThis(  [ self.tID, self.name, ended ], 'red'  )

			self.log = {
								'id': self.getID(),
								'tID': self.tID,
								'name': self.name,
								'start': self.epoch,
								'end': self.endTime,
								'duration': self.duration,
								'ended': ended,
			}
			global log
			log.append( self.log )
			# _.pr( 'THE END' )
			if not self.trigger is None:
				# _.pr( '\n\n\tTHE END trigger' )
				# _.colorThis( 'if not self.trigger is None:' )
				__.app.async( self.name + ' Trigger', self.trigger, kwargs=self.trigger_kwargs, timeout=self.trigger_timeout )

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


threadMonitorFirstRun = True

threadMonitorActive = False
def threadMonitor():
	global isTest
	global threadMonitorActive
	global threadMonitorFirstRun

	if threadMonitorFirstRun:
		threadMonitorFirstRun = False
		Thread(target=threadMonitor).start()
		return None
	threadMonitorActive = True
	global records
	global log
	done = False
	while not done:
		if isTest >= 3:
			_.pr()
			_.pr()
		for key in records.keys():
			for thisThread in records[key]:
				if not thisThread.killOn is None:
					if thisThread.duration is None:
						if isTest >= 3:
							_.pr()
							_.pr()
							_.pr( '        name:', thisThread.name )
							_.pr( 'duration Var:', thisThread.duration )
							_.pr( '    duration:', time.time() - thisThread.epoch )
							_.pr( '      killOn:', thisThread.killOn )
					if thisThread.duration is None and (  time.time() - thisThread.epoch ) > thisThread.killOn:
						_.colorThis( [  'TIMEOUT', thisThread.tID, thisThread.name  ] , 'red' )
						thisThread.kill()
						thisThread.join()

		if isTest >= 3:
			_.pr()
			_.pr()


		complete = 0
		total = 0
		for key in records.keys():
			for thisThread in records[key]:
				total+=1
				if not thisThread.duration is None:
					complete += 1


		if total == complete:
			done = True
			threadMonitorActive = False

		time.sleep(.2)
	if isTest >= 2:
		_.printVar( log )







