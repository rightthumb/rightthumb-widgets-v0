
class Threads:
	# Threads.openCnt
	# Threads.closedCnt
	openCnt = 0
	closedCnt = 0
	def __init__( self, name=None, func=None, arg=None, kwargs=None, focus=None, qID=None, addID=None, pID=None, timeout=None ):
		global appInfo
		if name is None:
			name = __.uuid()
		# Threads.openCnt += 1
		self.active = False

		self.created = time.time()
		if focus is None:
			focus = __.appReg
		self.app = appInfo[focus]['file']
		self.name = name
		self.func = func
		self.focus = focus
		self.arg = arg
		self.kwargs = kwargs
		self.qID = qID
		self.addID = addID
		self.created = time.time()
		self.status = True
		self.instance = ''
		self.bottom = False
		self.timeout = timeout
		self.hasTimedOut = 0
		self.pID = pID
		self.sstatus = 2



		self.data = False
		# self.trigger = False
		# self.triggerArg = False
		self.executed = False
		self.triggerError = False

		self.thisThread = None

		__.threadActivity[self.qID] = {}
		__.threadActivity[self.qID]['error'] = False
		__.threadActivity[self.qID]['activity'] = time.time()
		__.threadActivity[self.qID]['log'] = False

		# try:
		#   self.instance = appInfo[focus]['instance']
		# except Exception as e:



		self.log = {
						'id':       self.qID,
						'parent':   self.pID,
						'app':      self.app,
						'func':     'unknown',
						'arg':      'unknown',
						'instance': self.instance,
						'focus':    self.focus,
						'start':    0,
						'end':      0,
						'runtime':  0,
						'mem':      0,
						'lines':      0,
						'wait':     0,
						'qcount':   0
		}
		try:
			self.log['func'] = self.func.__name__
		except Exception as e:
			pass

		self.log['arg'] = _profile.records.audit(  self.name+' - '+str(self.qID)  , self.arg )
		# if not type(self.arg) == str and not type(self.arg) == list and not type(self.arg) == dict and not type(self.arg) == int and not type(self.arg) == float and not type(self.arg) == tuple:
		#     try:
		#         self.log['arg'] = str(self.arg)
		#     except Exception as e:
		#         pass
		# else:



		try:
			self.argID = self.arg
			self.argID.append( self.qID )
		except Exception as e:
			self.argID = False
		self.open()
	def getLog( self ):
		self.log['error'] = __.threadActivity[self.qID]['error']
		self.log['activity'] = __.threadActivity[self.qID]['activity']
		self.log['errorlog'] = __.threadActivity[self.qID]['log']
		if self.thisThread is None:
			self.log['thisThread'] = None
		else:
			self.log['thisThread'] = self.thisThread.log
		# try:
		# except Exception as e:
		#     pass
		return self.log



	def open( self ):
		# print_('open 0')
		self.sstatus = 1
		__.queueLastActivity = time.time()
		self.active = True
		self.log['start'] = time.time()
		self.log['qcount'] = __.queueCount

		if self.kwargs:
			if self.addID:
				data = [{ 'func': self.func, 'args': self.arg[:-1] }]
				data[0]['args'][0]['qID']=self.qID
				self.thisThread = ThisThread(
												qID = self.qID,
												name = self.name+' - '+str(self.qID),
												fn = self.func,
												k = data[0]['args'][0],
												t = self.timeout,
												start = True,
				)
				# threadTimer( .0001, threadKwargs, data, qID=self.qID )
			else:
				data = [[{ 'func': self.func, 'args': self.arg }]]
				self.thisThread = ThisThread(
												qID = self.qID,
												name = self.name+' - '+str(self.qID),
												fn = self.func,
												k = self.arg,
												t = self.timeout,
												start = True,
				)
				# threadTimer( .0001, threadKwargs, data, qID=self.qID )
		else:
			if self.addID:
				self.thisThread = ThisThread(
												qID = self.qID,
												name = self.name+' - '+str(self.qID),
												fn = self.func,
												a = self.qID,
												t = self.timeout,
												start = True,
				)
				# threadTimer( .0001, self.func, self.argID, qID=self.qID )
			else:
				self.thisThread = ThisThread(
												qID = self.qID,
												name = self.name+' - '+str(self.qID),
												fn = self.func,
												a = self.arg,
												t = self.timeout,
												start = True,
				)
				# threadTimer( .0001, self.func, self.arg, qID=self.qID )
		# print_('open 1')

	def close( self, mem=0, data=False, trigger=False, triggerArg=False, kwargs=False, lines=0 ):
		self.sstatus = 0
		__.queueLastActivity = time.time()
		if not type(trigger) == bool:
			try:
				triggerName = trigger.__name__
			except Exception as e:
				triggerName = ''

			try:



				if type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger )
				elif not type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger, data )
				elif type(data) == bool and not type(triggerArg) == bool:
					threadTimer( .0001, trigger, triggerArg )
				elif not type(data) == bool and not type(triggerArg) == bool and kwargs:
					args = [{ 'func': trigger, 'args': triggerArg }]
					args[0]['args'][0]['data'] = data
					threadTimer( .0001, threadKwargs, args )
				elif not type(data) == bool and not type(triggerArg) == bool and not kwargs:
					try:
						triggerArg.append(data)
						threadTimer( .0001, threadKwargs, triggerArg )
					except Exception as e:
						try:
							triggerArg[0].append(data)
							threadTimer( .0001, threadKwargs, triggerArg )
						except Exception as e:
							printBold('close trigger error '+str(self.focus)+' '+ str(self.name) +' '+ str(self.func)+' '+ str(triggerName), 'red' )
							self.triggerError = True


				self.executed = True
				if self.triggerError:
					self.executed = False
			except Exception as e:
				printBold('close trigger error '+str(self.focus)+' '+ str(self.name) +' '+ str(self.func)+' '+ str(triggerName), 'red')
				self.triggerError = True



		# Threads.closedCnt += 1
		# print_('Closed:',self.qID,'\tTotal Closed:',Threads.newCounter,'\tScheduler:',__.queueCountScheduleAudit,__.queueCountSchedule,'\tTimers:',__.queueCountTimer)
		self.status = False
		self.log['end'] = time.time()
		self.log['runtime'] = self.log['end'] - self.log['start']
		self.log['mem'] = mem
		self.log['lines'] = lines
		if not type(data) == bool:
			self.data = data
		return self.qID

	def openCnt( self ):
		return Threads.openCnt

	def closedCnt( self ):
		return Threads.closedCnt