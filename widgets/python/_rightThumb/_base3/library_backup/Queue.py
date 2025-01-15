
class Queue:

	def __init__( self ):

		self.created = time.time()
		self.loadedBy = 0
		self.loadTime = 0
		self.completionTime = 0
		self.lastActivity = 0
		self.lastActivityEach = {}

		# self.qID_index = {}

		self.records = {}
		self.nextID = 0
		self.opened = 0
		self.closed = 0
		self.notstarted = 0
		self.maxInQueue = 0
		self.maxThreads = 100
		self.maxThreadsSafe = 100
		self.minThreads = 50
		self.table = {'focus': [], 'name': []}
		self.schedulerInitialized = False


		self.auditPrint = True
		self.maxThreadsAuto = True
		self.auditInitialized = False
		self.auditPercentChangeMax = 30
		self.auditPercentChangeMin = 10
		self.auditPercentReduceBy = 5
		self.auditPercentReduceByDrastic = 15
		self.auditPercentDrasticThreshold = 3
		self.auditWatchMax = 5
		self.auditPercentSample = 10
		self.auditMaxFailuresBeforeAction = 3
		self.auditLogInternal = []
		self.auditLogExternal = []
		self.auditAutoAdjust = False


		##
		self.scheduleLoop = .01
		self.auditLoop = .1
		self.autoLoadedAfter = 5
		self.statusTotal = 0
		self.prefix = False
		##


		self.autoLoaded = True

		self.report = False
		self.reportPrinted = False


		self.timeout = False
		self.timeoutAsk = False


		self.saveLog = True
		self.isLoaded = False

		self.appStructure = __.structure()

		__.totalTask = 0
		__.queueCount = 0
		__.queueCountSchedule = 0
		__.queueCountAudit = 0
		__.queueCountScheduleAudit = 0
		__.queueCountAuditAudit = 0
		__.queueLastActivity = time.time()
		__.queueCountTimer = 0

		__.threadActivity = {}

		self.projectDataMaxLen = 2000
		self.projectDataDetected = False
		__.datadumps = 0
		__.projectData = {}
		__.pdID = {}
		__.saveInitiated = False

		self.listeningFor = False



	def killAll( self ):



		for focus in self.records.keys():
			for i, threads in enumerate( self.records[focus]['threads'] ):
				if not threads.thisThread is None and threads.sstatus == 1:

					name = self.records[focus]['threads'][i].name
					qID = self.records[focus]['threads'][i].qID

					self.records[focus]['threads'][i].hasTimedOut = 1
					self.records[focus]['threads'][i].thisThread.kill()
					self.spent( qID, 0 )

		self.isLoaded = True
		for focus in self.records.keys():
			for name in self.records[focus]['names'].keys():
				self.records[focus]['names'][name]['loaded'] = True
				self.spendFocus( name, focus, 99 )



# func=False, arg=False, kwargs=False, focus=False , addID=True ,
# loaded=False,
# , pID=False



	def register( self, name, trigger=None, triggerArg=False, triggerKwargs=False,  timeout=False, database=False, focus=None,      completed=None, onComplete=None,      oc=None, c=None, a=None, k=None, t=None, d=None  ):
		if not completed is None:
			trigger = completed
		if not onComplete is None:
			trigger = onComplete
		if not oc is None:
			trigger = oc
		if not c is None:
			trigger = c

		if not a is None:
			triggerArg = a
		if not k is None:
			triggerKwargs = k
		if not t is None:
			timeout = t
		if not d is None:
			database = d



		loaded = False



		# print_('arg:',arg)
		# print_( name, type( trigger ) )
		# sys.exit()
		nextID = False
		global appInfo
		self.lastActivity = time.time()

		if focus is None:
			focus = __.appReg
		pass

		try:
			self.lastActivityEach[focus][name] = time.time()
		except Exception as e:
			self.lastActivityEach[focus] = {}
			self.lastActivityEach[focus][name] = time.time()



		try:
			__.projectData[focus]
		except Exception as e:
			__.projectData[focus] = {}

		__.projectData[focus][name] = {}
		# if not 'folder' in name:
		#   print_( 'zero' )
		#   sys.exit()

		__.projectData[focus][name][0] = {}
		__.projectData[focus][name][0]['saveInitiated'] = False
		# print_( 'check3:', focus, name, 0 )
		__.projectData[focus][name][0]['data'] = []

		__.projectData[focus][name][1] = {}
		__.projectData[focus][name][1]['saveInitiated'] = False
		# print_( 'check4:', focus, name, 1 )
		__.projectData[focus][name][1]['data'] = []

		try:
			__.pdID[focus]
		except Exception as e:
			__.pdID = {}
			__.pdID[focus] = {}


		__.pdID[focus][name] = 0

		if self.maxThreadsAuto:
			maxThreads = self.maxThreadsSafe
		else:
			maxThreads = self.maxThreads
		if trigger is None:
			trigger = False

		try:
			self.records[focus]['names'][name] = {
													'timeout': timeout,
													'loaded': loaded,
													'trigger': trigger,
													'maxThreads': maxThreads,
													'failure': 0,
													'changes': 0,
													'watch': 0,
													'closed': 0,
													'database': database,
													'executed': False,
													'projectSaveInitiated': False,
												}
		except Exception as e:
			self.records[focus] = {
										'threads': [],
										'open': 0,
										'app': appInfo[focus]['file'],
										'names': {
												name: {
													'timeout': timeout,
													'loaded': loaded,
													'trigger': trigger,
													'maxThreads': maxThreads,
													'failure': 0,
													'changes': 0,
													'watch': 0,
													'closed': 0,
													'database': database,
													'executed': False,
													'projectSaveInitiated': False,
												}
										}
			}



		pass
		self.isLoaded = False
		self.records[focus]['names'][name]['loaded'] = loaded
		if not self.auditAutoAdjust:
			# print_(focus,name)
			if self.maxThreadsAuto:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreadsSafe
			else:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreads


		if not loaded:
			self.records[focus]['names'][name]['loaded'] = False

		if not trigger is None:
			self.records[focus]['names'][name]['trigger'] = trigger
			if not triggerArg is None:
				self.records[focus]['names'][name]['triggerArg'] = triggerArg
			else:
				self.records[focus]['names'][name]['triggerArg'] = False



		if not self.auditInitialized and self.maxThreadsAuto:
			self.auditInitialized = True
			threadTimer( self.auditLoop, threadAudit )
			# Timer( .3, threadAudit ).start()

		return nextID



	def add( self, name, func=False, arg=False, kwargs=False, focus=False , addID=True , trigger=False, triggerArg=False, triggerKwargs=False, loaded=False, timeout=False, database=False, pID=False ):
		# print_('arg:',arg)
		# print_( name, type( trigger ) )
		# sys.exit()
		nextID = False
		global appInfo
		self.lastActivity = time.time()

		if type(focus) == bool:
			focus = __.appReg

		try:
			self.lastActivityEach[focus][name] = time.time()
		except Exception as e:
			self.lastActivityEach[focus] = {}
			self.lastActivityEach[focus][name] = time.time()

		try:
			self.records[focus]['threads']
			self.records[focus]['names'][name]['loaded'] = loaded
		except Exception as e:

			try:
				__.projectData[focus]
			except Exception as e:
				__.projectData[focus] = {}

			__.projectData[focus][name] = {}
			# if not 'folder' in name:
			#   print_( 'zero' )
			#   sys.exit()

			__.projectData[focus][name][0] = {}
			__.projectData[focus][name][0]['saveInitiated'] = False
			# print_( 'check3:', focus, name, 0 )
			__.projectData[focus][name][0]['data'] = []

			__.projectData[focus][name][1] = {}
			__.projectData[focus][name][1]['saveInitiated'] = False
			# print_( 'check4:', focus, name, 1 )
			__.projectData[focus][name][1]['data'] = []

			try:
				__.pdID[focus]
			except Exception as e:
				__.pdID = {}
				__.pdID[focus] = {}


			__.pdID[focus][name] = 0

			if self.maxThreadsAuto:
				maxThreads = self.maxThreadsSafe
			else:
				maxThreads = self.maxThreads
			try:
				self.records[focus]['names'][name] = {
														'timeout': timeout,
														'loaded': loaded,
														'trigger': trigger,
														'maxThreads': maxThreads,
														'failure': 0,
														'changes': 0,
														'watch': 0,
														'closed': 0,
														'database': database,
														'executed': False,
														'projectSaveInitiated': False,
													}
			except Exception as e:
				self.records[focus] = {
											'threads': [],
											'open': 0,
											'app': appInfo[focus]['file'],
											'names': {
													name: {
														'timeout': timeout,
														'loaded': loaded,
														'trigger': trigger,
														'maxThreads': maxThreads,
														'failure': 0,
														'changes': 0,
														'watch': 0,
														'closed': 0,
														'database': database,
														'executed': False,
														'projectSaveInitiated': False,
													}
											}
				}


		if type(timeout) == bool:
			timeout = self.records[focus]['names'][name]['timeout']


		self.isLoaded = False
		self.records[focus]['names'][name]['loaded'] = loaded
		if not self.auditAutoAdjust:
			# print_(focus,name)
			if self.maxThreadsAuto:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreadsSafe
			else:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreads


		if not loaded:
			self.records[focus]['names'][name]['loaded'] = False

		if not type(trigger) == bool:
			self.records[focus]['names'][name]['trigger'] = trigger
			if not type(triggerArg) == bool:
				self.records[focus]['names'][name]['triggerArg'] = triggerArg
			else:
				self.records[focus]['names'][name]['triggerArg'] = False

		if not type(func) == bool:
			self.table['focus'].append(focus)
			# self.table['name'].append(name)
			nextID = self.nextID
			# self.qID_index[ (qID) ] = { 'focus': focus, 'name': name }
			self.records[focus]['threads'].append( Threads( name, func, arg, kwargs, focus, nextID, addID, pID=pID, timeout=timeout ) )

			shouldOpen = False
			if not self.records[focus]['names'][name]['maxThreads']:
				shouldOpen = True
			elif self.opened > self.records[focus]['names'][name]['maxThreads']:
				shouldOpen = True
			if not shouldOpen:
				self.notstarted += 1
			else:
				pass
				# self.records[focus]['threads'][nextID].open()
				# self.cnt( focus, True )
			self.nextID += 1
			if not self.schedulerInitialized and True:
				self.schedulerInitialized = True
				threadTimer( self.scheduleLoop, threadSchedule )
				# Timer( self.scheduleLoop, threadSchedule ).start()

		if not self.auditInitialized and self.maxThreadsAuto:
			self.auditInitialized = True
			threadTimer( self.auditLoop, threadAudit )
			# Timer( .3, threadAudit ).start()

		return nextID

	def loadedGroup( self, name=False , focus=False ):

		if self.autoLoaded:

			if type(focus) == bool:
				focus = __.appReg


			hasChildren = False
			for rec in self.records[focus]['threads']:
				if rec.focus == focus and rec.name == name:
					# if name == 'processMovies':
					#     colorThis( [ 'processMovies' ], 'red' )
					hasChildren = True


			if hasChildren:
				self.records[focus]['names'][name]['loaded'] = True



	def loaded( self, name=False , focus=False ):


		if self.autoLoaded:

			if type(focus) == bool:
				focus = __.appReg


			hasChildren = False
			for rec in self.records[focus]['threads']:
				if rec.focus == focus and rec.name == name:
					# if name == 'processMovies':
					#     colorThis( [ 'processMovies' ], 'red' )
					hasChildren = True


			if hasChildren:
				# self.isLoaded = True
				if not type(name) == bool:
					self.records[focus]['names'][name]['loaded'] = True
					# name = str(list(self.records[focus]['names'].keys())[0])
				else:
					for f in self.records.keys():
						for n in self.records[f]['names'].keys():
							if not self.records[f]['names'][n]['loaded']:
								self.records[f]['names'][n]['loaded'] = True


		pass
		allComplete = True
		for f in self.records.keys():
			for n in self.records[f]['names'].keys():
				if not self.records[f]['names'][n]['loaded']:
					allComplete = False
		if allComplete:
			self.isLoaded = True


	def spent( self, qID, mem=0, data=False, trigger=False, triggerArg=False, kwargs=False, lines=0 ):
		qID = int(qID)
		focus = False
		result = False
		for i,t in enumerate(self.records[self.table['focus'][qID]]['threads']):
			if self.records[ self.table['focus'][qID] ]['threads'][i].qID == qID:
				result = self.records[self.table['focus'][qID]]['threads'][i].close( mem, data, trigger, triggerArg, kwargs, lines )
				focus = self.table['focus'][qID]
				name = self.records[self.table['focus'][qID]]['threads'][i].name
		if not type(focus) == bool:
			self.cnt( focus, False )

			# if self.isEverythingLoadedEach(  focus,  name  ) and self.notstarted == 0:
			if self.isEverythingLoadedEach(  focus,  name  ) and self.isEverythingClosedEach( focus, name ):
				self.spendFocus( name, focus, 1 )
				self.printReport()
		return result



	def printReport( self ):
		if not self.reportPrinted:
			self.completionTime = time.time() - self.created
			if self.report:
				self.reportPrinted = True
				print_('__________________________________________')
				print_()
				print_('opened:',self.opened)
				# print_('records open:',self.records[focus]['open'])
				print_('isEverythingLoaded:',time.time()-self.loadedBy,time.time()-self.lastActivity)
				print_('spendFocus')
				print_('queueCountSchedule:',__.queueCountSchedule)
				print_('queueCountAudit:',__.queueCountAudit)
				print_('audit:',__.queueCountAudit)
				print_()
				print_('load time:\t', int(self.loadTime))
				print_('time after load:\t', int(time.time()-self.loadedBy))
				print_()
				print_('app time:\t', int(self.completionTime))
				print_()
				print_('maxInQueue:',self.maxInQueue)
				# str((self.completionTime/1000)%60)
				print_()
				print_('timeouts:',self.timeoutCount())
				# print_("Average of the list =", round(average, 2))
				print_()
				print_('__________________________________________')
			elif self.statusTotal > 0:
				cTime = round(self.completionTime,2)
				if cTime > 60:
					ncTime = str(round((self.completionTime/60),2)) + ' min'
				else:
					ncTime = str(round(self.completionTime,2)) + ' sec'
				print_('App time: ' + str(ncTime), end='\r', flush=True)
				# sys.stdout.flush()

	def spendFocus( self, name, focus, which ):


		# print_( 'spendFocus which:', which )

		# print_( 'HERE: 0' )
		self.saveData()
		# print_( 'HERE: 1' )

		if not self.records[focus]['names'][name]['executed']:
			if not type( self.records[focus]['names'][name]['trigger'] ) == bool:
				if not type( self.records[focus]['names'][name]['triggerArg'] ) == bool:
					# Timer(.0001, self.records[focus]['names'][name]['trigger'], self.records[focus]['names'][name]['triggerArg']).start()
					# print_( '\trunning 0' )
					self.records[focus]['names'][name]['trigger'](**self.records[focus]['names'][name]['triggerArg'])

				else:
					# print_( '\trunning 1' )
					self.records[focus]['names'][name]['trigger']()
			self.records[focus]['names'][name]['executed'] = True
		# print_( 'HERE: 2' )


	def log( self, name=False, focus=False ):
		if type(focus) == bool:
			focus = __.appReg
		log = []
		if not type(name) == bool:
			for i,t in enumerate(self.records[focus]['threads']):
				if self.records[focus]['threads'][i].name == name:
					log.append(self.records[focus]['threads'][i].getLog())
		else:
			for i,t in enumerate(self.records[focus]['threads']):
				for n in self.records[focus]['names']:
					if self.records[focus]['threads'][i].name == n:
						log.append(self.records[focus]['threads'][i].getLog())

		for f in self.records:
			self.records[f]['threads'] = False
			for n in self.records[f]['names']:
				if not type(self.records[f]['names'][n]['trigger']) == bool:
					self.records[f]['names'][n]['trigger'] = True



		return {
					'session': _v.session(),
					'created': self.created,
					'loadedby': self.loadedBy,
					'loadtime': self.loadTime,
					'lastactivity': self.lastActivity,
					'completiontime': self.completionTime,
					'nextid': self.nextID,
					'maxinqueue': self.maxInQueue,
					'totaltask': __.totalTask,
					'records': self.records,
					'maxthreadssafe': self.maxThreadsSafe,
					'projectdatamaxlen': self.projectDataMaxLen,
					'datadumps': __.datadumps,
					'appstructure': __.structure(),
					'threadlog': log
		}

	def cnt( self, focus, up ):
		# self.maxThreadsSafe
		# self.maxThreads
		if up:
			if self.opened > self.maxInQueue:
				self.maxInQueue = self.opened
			self.lastActivity = time.time()
			self.records[focus]['open'] += 1
			self.opened += 1
			__.queueCount += 1
		else:
			self.closed += 1
			self.records[focus]['open'] -= 1
			self.opened -= 1
			__.queueCount -= 1

	def schedule( self ):
		Timer = __.imp('threading.Timer')
		__.queueCountSchedule += 1
		__.queueCountScheduleAudit -= 1



		if self.opened > self.maxThreads and self.notstarted > 0:
			pass
			time.sleep(.02)
			# Timer( self.scheduleLoop, threadSchedule ).start()
		else:

			i = 0
			while self.opened < self.maxThreads-10 and i < self.notstarted:
				# time.sleep(.02)
				# print_( 'open:', self.opened, 'max:', self.maxThreads )
				# if self.opened < self.maxThreads-10 and i < self.notstarted:
				chosen = self.nextInQueue()
				if type(chosen) == bool:
						return False
				else:
					try:
						self.records[chosen['focus']]['threads'][chosen['qID']].open()
						self.notstarted -= 1
						self.cnt( chosen['focus'], True )
						i += 1
					except Exception as e:
						time.sleep(.2)
						try:
							self.records[chosen['focus']]['threads'][chosen['qID']].open()
							self.notstarted -= 1
							self.cnt( chosen['focus'], True )
							i += 1
						except Exception as e:
							time.sleep(.2)
							try:
								self.records[chosen['focus']]['threads'][chosen['qID']].open()
								self.notstarted -= 1
								self.cnt( chosen['focus'], True )
								i += 1
							except Exception as e:
								pass


		if self.notstarted > 0:
			try:
				Timer( self.scheduleLoop, threadSchedule ).start()
			except Exception as e:
				time.sleep(.2)
				try:
					Timer( self.scheduleLoop, threadSchedule ).start()
				except Exception as e:
					time.sleep(.2)
					try:
						Timer( self.scheduleLoop, threadSchedule ).start()
					except Exception as e:
						time.sleep(.2)
						try:
							Timer( self.scheduleLoop, threadSchedule ).start()
						except Exception as e:
							pass




	def nextInQueue( self ):
		chosen = False
		try:
			for key in self.records.keys():
				for i,q in enumerate(self.records[key]['threads']):
					if not self.records[key]['threads'][i].active:
						chosen = { 'focus': key, 'qID': self.records[key]['threads'][i].qID }
			if type(chosen) == bool:
				# print_('active:',self.checkActive())
				return False
		except Exception as e:
			chosen = False
		return chosen

	def checkActive( self ):
		active = 0
		for key in self.records.keys():
			for i,q in enumerate(self.records[key]['threads']):
				if not self.records[key]['threads'][i].active:
					active += 1
		return active

	def isEverythingLoaded( self ):
		loaded = True
		shouldRun = True
		if self.loadedBy > 0:
			if self.loadedBy > self.lastActivity:
				shouldRun = False

		if shouldRun:
			for f in self.records.keys():
				for n in self.records[f]['names'].keys():
					if not self.records[f]['names'][n]['loaded']:
						loaded = False
			if loaded:
				self.loadedBy = time.time()
				self.loadTime = self.loadedBy - self.created
				# self.isLoaded = True
		return loaded

	def isEverythingClosedEach( self, focus, name ):

		closed = 0
		total = 0
		for key in self.records.keys():
			for i,q in enumerate(self.records[key]['threads']):
				if self.records[key]['threads'][i].name == name and self.records[key]['threads'][i].focus == focus:
					total += 1
					if self.records[key]['threads'][i].sstatus == 0:
						closed += 1
		if total and closed and total == closed:
			return True
		return False

	def isEverythingLoadedEach( self, focus, name ):
		f = focus
		n = name



		hasChildren = False
		for rec in self.records[focus]['threads']:
			if rec.focus == focus and rec.name == name:
				# if name == 'processMovies':
				#     colorThis( [ 'processMovies' ], 'red' )
				hasChildren = True


		if not hasChildren:
			loaded = False
		if hasChildren:



			diff = int(time.time() - self.lastActivityEach[focus][name])
			if diff > self.autoLoadedAfter:
				self.loadedGroup( name=name , focus=focus )


			loaded = True
			shouldRun = True
			# if self.loadedBy > 0:
			#     if self.loadedBy > self.lastActivityEach[focus][name]:
			#         shouldRun = False

			if shouldRun:

				if not self.records[f]['names'][n]['loaded']:
					loaded = False

				if loaded:
					self.loadedBy = time.time()
					self.loadTime = self.loadedBy - self.created
					# self.isLoaded = True



			allComplete = True
			for f in self.records.keys():
				for n in self.records[f]['names'].keys():
					if not self.records[f]['names'][n]['loaded']:
						allComplete = False
			if allComplete:
				self.isLoaded = True


		return loaded



	def getRuntimeMemoryFocus( self, focus ):
		runtime = []
		memory = []
		runtimeMemory = []
		for i,q in enumerate(self.records[focus]['threads']):
			if not self.records[key]['threads'][i].status:
				run = self.records[focus]['threads'][i].log['runtime']
				mem = self.records[focus]['threads'][i].log['mem']
				runtime.append( run )
				memory.append( mem )
				runtimeMemory.append({ 'runtime': run, 'mem': mem })

		return { 'runtime': runtime, 'mem': memory, 'runmem': runtimeMemory, 'averagemem': self.calcAverage(memory), 'averageruntime': self.calcAverage(runtime)  }

	def getRuntimeMemoryNameFocus( self, name, focus ):
		runtime = []
		runtimebottom = []
		memory = []
		runtimeMemory = []
		self.numberClosed()
		if self.records[focus]['names'][name]['closed'] < 5:
			return False

		for i,q in enumerate(self.records[focus]['threads']):
			if not self.records[focus]['threads'][i].status and self.records[focus]['threads'][i].name == name:
				run = self.records[focus]['threads'][i].log['runtime']
				mem = self.records[focus]['threads'][i].log['mem']
				runtime.append( run )
				memory.append( mem )
				runtimeMemory.append({ 'runtime': run, 'mem': mem })
			if not self.records[focus]['threads'][i].status and self.records[focus]['threads'][i].name == name and not self.records[focus]['threads'][i].bottom:
				self.records[focus]['threads'][i].bottom = True
				runtimebottom.append( run )

			if len(runtime) == 0 or len(memory) == 0 or len(runtimebottom) == 0 :
				return False

		try:

			data = {
					'runtime': runtime,
					'runtimebottom': runtimebottom,
					'mem': memory,
					'runmem': runtimeMemory,
					'averagemem': self.calcAverage(memory),
					'averageruntime': self.calcAverage(runtime)
		}

		except Exception as e:
			data = False
			# print_(memory)

		return data

	def getRuntimeMemoryReport( self ):
		self.runtime = []
		self.mem = []
		self.runtimeMemory = []
		self.averagemem = 0
		self.averageruntime = 0
		for key in self.records.keys():
			for i,q in enumerate(self.records[key]['threads']):
				if not self.records[key]['threads'][i].status:
					run = self.records[key]['threads'][i].log['runtime']
					mem = self.records[key]['threads'][i].log['mem']

					self.runtime.append( run )
					self.mem.append( mem )
					self.runtimeMemory.append({ 'runtime': runtime, 'mem': mem })

		self.averagemem = self.calcAverage(mem)
		self.averageruntime = self.calcAverage(runtime)
		return { 'runtime': runtime, 'mem': mem, 'runmem': self.runtimeMemory, 'averagemem': self.averagemem, 'averageruntime': self.averageruntime }


	def calcAverage( data ):
		return round(data, 2)

	def saveData( self ):

		import sqlite3
		for focus in __.projectData:
			try:
				del __.projectData[focus][0]
			except Exception as e:
				pass
			for name in __.projectData[focus].keys():
				logName = 'auto_' + self.records[focus]['app'] + '_' + name + '_' + str(self.created)
				for pdID in __.projectData[focus][name].keys():
					if len(__.projectData[focus][name][pdID]['data']):
						__.datadumps += 1
						if type(self.records[focus]['names'][name]['database']) == bool or self.records[focus]['names'][name]['database'] is None:
							if len(__.projectData[focus][name][pdID]['data']) > 0:

								saveTableSplitNew( __.projectData[focus][name][pdID]['data'], logName, project=True )
								print_( 'check0:', focus, name, pdID )
								if not 'folder' in name:
									print_( 'zero' )
									sys.exit()
								__.projectData[focus][name][pdID]['data'] = []
						else:
							print_()
							print_('Data saved to:',self.records[focus]['names'][name]['database'])
							print_()


							if len(__.projectData[focus][name][pdID]['data']) > 0:
								try:
									conn = sqlite3.connect(self.records[focus]['names'][name]['database'])
									cursor = conn.cursor()
									errors = []
									for sql in __.projectData[focus][name][pdID]['data']:
										try:
											cursor.execute( sql )
										except Exception as e:
											errors.append( sql )
									conn.commit()
									conn.close()
									if len(errors) > 0:
										saveTableSplitNew( errors, logName+'__ERRORS__', project=True )
								except Exception as e:
									saveTableSplitNew( __.projectData[focus][name][pdID]['data'], logName, project=True )
									print_( 'check1:', focus, name, pdID )
								if not 'folder' in name:
									print_( 'zero' )
									sys.exit()
								__.projectData[focus][name][pdID]['data'] = []



	def manageData( self ):
		import sqlite3
		self.data = {}
		self.data[0] = 0
		self.data[1] = 0
		for focus in __.projectData:
			# print_( 'focus:', focus )
			try:
				del __.projectData[focus][0]
			except Exception as e:
				pass
			for name in __.projectData[focus].keys():
				logName = 'auto_' + self.records[focus]['app'] + '_' + name + '_' + str(self.created)
				for pdID in __.projectData[focus][name].keys():
					if not type(__.projectData[focus][name][pdID]['saveInitiated']) == bool:
						# print_('saveInitiated:',__.projectData[focus][name][pdID]['saveInitiated'])
						# print_()
						# print_(len( __.projectData[focus][name][ __.projectData[focus][name][pdID]['saveInitiated']['pdID'] ]['data'] ), __.projectData[focus][name][pdID]['saveInitiated']['size'] )
						# print_()
						if len( __.projectData[focus][name][ __.projectData[focus][name][pdID]['saveInitiated']['pdID'] ]['data'] ) > __.projectData[focus][name][pdID]['saveInitiated']['size']:
							__.projectData[focus][name][pdID]['saveInitiated']['timeSizeChange'] = time.time()
						else:
							# print_()
							# print_('got here')
							# print_()

							diff = time.time() - __.projectData[focus][name][pdID]['saveInitiated']['timestamp']
							print_()
							# print_()
							# print_('diff:',diff)
							# print_()
							print_( 'diff:', diff )
							print_( __.projectData[focus][name][pdID]['saveInitiated']['size'], len(__.projectData[focus][name][  __.projectData[focus][name][pdID]['saveInitiated']['pdID']  ]['data']))
							if diff > __.projectData[focus][name][pdID]['saveInitiated']['startAfterNoChangeFor']:
								__.datadumps += 1
								if type(self.records[focus]['names'][name]['database']) == bool or self.records[focus]['names'][name]['database'] is None:
									tmpData = __.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data']
									print_( 'save started' )
									saveTableSplitNew( tmpData, __.projectData[focus][name][pdID]['saveInitiated']['logname'], project=True )
									tmpData = []
									print_( 'post split save:', len(__.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data']) )
									__.projectData[__.projectData[focus][name][pdID]['saveInitiated']['focus']][__.projectData[focus][name][pdID]['saveInitiated']['pdID']] = []
									if not 'folder' in name:
										print_( 'zero' )
										sys.exit()
									__.projectData[focus][name][pdID]['saveInitiated'] = False
									threadTimer( .5, enableThreadDataSwap )

								else:
									print_()
									print_('Data saved to:',self.records[focus]['names'][name]['database'])
									print_()
									# try:
									conn = sqlite3.connect(self.records[focus]['names'][name]['database'])
									cursor = conn.cursor()
									errors = []
									for sql in __.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data']:
										try:
											cursor.execute( sql )
										except Exception as e:
											errors.append( sql )
									conn.commit()
									conn.close()
									if len(errors) > 0:
										saveTableSplitNew( errors, logName+'__ERRORS__', project=True )
									# except Exception as e:
									#   saveTableSplitNew( __.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data'], __.projectData[focus][name][pdID]['saveInitiated']['logname'], project=True )



									# __.projectData[focus][name][  __.projectData[focus][name][pdID]['saveInitiated']['pdID']  ]['data'] = []
									if not 'folder' in name:
										print_( 'zero' )
										sys.exit()
									__.projectData[focus][name][pdID]['saveInitiated'] = False
									threadTimer( .5, enableThreadDataSwap )



		tmpData = []

		if not __.saveInitiated:
			for focus in __.projectData:
				try:
					del __.projectData[focus][0]
				except Exception as e:
					pass
				for name in __.projectData[focus].keys():
					for pdID in __.projectData[focus][name].keys():
						# print_('data len:',len(__.projectData[focus][name][pdID]['data']))
						# print_('projectDataMaxLen:',self.projectDataMaxLen)
						if len(__.projectData[focus][name][pdID]['data']):
							self.projectDataDetected = True

							# print_()
							# print_( len(__.projectData[focus][name][pdID]['data']), self.projectDataMaxLen )
							# print_()

							if len(__.projectData[focus][name][pdID]['data']) >= self.projectDataMaxLen:

								if __.pdID[focus][name] == 0:
									__.pdID[focus][name] = 1
									print_( 'NOW: 1' )
								else:
									__.pdID[focus][name] = 0
									print_( 'NOW: 0' )

								logname = 'auto_' + self.records[focus]['app'] + '_' + str(self.created)
								__.saveInitiated = True

								__.processing = [ focus, name, pdID ]

								__.projectData[focus][name][pdID]['saveInitiated'] = {
															'logname': logname,
															'pdID': pdID,
															'focus': focus,
															'timestamp': time.time(),
															'size': len(__.projectData[focus][name][pdID]['data']),
															'startAfterNoChangeFor': 3,
															'timeSizeChange': 0,

								}


			# self.timeout = False
			# self.timeoutAsk = False



	def listen( self, qID, trigger=False, triggerArg=False, kwargs=False, data=False  ):
		try:
			self.listeningFor['active']
		except Exception as e:
			self.listeningFor = []
		self.listeningFor.append( { 'active': True, 'qID': qID, 'trigger': trigger, 'triggerArg': triggerArg, 'kwargs': kwargs, 'data': data } )

	def listener( self ):
		for li,listen in enumerate(self.listeningFor):
			if self.listeningFor[li]['active']:
				for focus in self.records.keys():
					for i,q in enumerate(self.records[focus]['threads']):
						if self.records[focus]['threads'][i].qID == listen['qID'] and not self.records[focus]['threads'][i].status:
							thisData0 = self.records[focus]['threads'][i].data
							thisData1 = self.listeningFor[li]['data']
							thisData = False
							if sys.getsizeof(thisData0) > sys.getsizeof(thisData1):
								thisData = thisData0
							elif sys.getsizeof(thisData0) < sys.getsizeof(thisData1):
								thisData = thisData1
							self.listeningFor[li]['data'] = False
							self.listeningFor[li]['active'] = False
							self.records[focus]['threads'][i].data = False
							self.listenActivated( self.listeningFor[li]['trigger'], self.listeningFor[li]['triggerArg'], self.listeningFor[li]['kwargs'], thisData )


	def listenActivated( self, trigger=False, triggerArg=False, kwargs=False, data=False  ):

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
					threadTimer( .0001, trigger, [data] )
				elif type(data) == bool and not type(triggerArg) == bool:
					threadTimer( .0001, trigger, triggerArg )
				elif not type(data) == bool and not type(triggerArg) == bool and kwargs:
					args = [{ 'func': trigger, 'args': triggerArg }]
					try:
						args[0]['args'][0]['data'] = data
					except Exception as e:
						args[0]['args']['data'] = data


					# print_(args)
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
							print_('listener trigger error')


			except Exception as e:
				print_('listener trigger error')


	def printStatus( self ):
		pDone = str(int(percentageDiffInt(self.closed, self.statusTotal)))
		if not type( self.prefix ) == bool:
			print_(' ' + self.prefix + ':', pDone + '%' , end='\r')
		else:
			print_(' ' + pDone + '%' , end='\r')
		sys.stdout.flush()

	def timeoutCount( self ):
		cnt = 0
		for focus in self.records.keys():
			for i,q in enumerate(self.records[focus]['threads']):

				if self.records[focus]['threads'][i].hasTimedOut:
					cnt += 1
		return cnt



	def kill( self, qID ):

		qID = int(qID)
		focus = None
		rID = None
		for i,t in enumerate(self.records[self.table['focus'][qID]]['threads']):
			if self.records[ self.table['focus'][qID] ]['threads'][i].qID == qID:
				focus = self.table['focus'][qID]
				name = self.records[self.table['focus'][qID]]['threads'][i].name

				self.spent( qID, 0 )
				self.records[focus]['threads'][i].hasTimedOut = 1
				self.records[focus]['threads'][i].thisThread.kill()



	def checkTimeout( self ):

		for focus in self.records.keys():
			for i, threads in enumerate( self.records[focus]['threads'] ):
				if not threads.thisThread is None:
					if threads.status and threads.timeout:
						dur = time.time() - threads.log['start']
						if dur > threads.timeout:
							# print_( 'time ran out',threads.qID )
							# print_( 'time ran out',threads.qID )
							# print_( 'time ran out',threads.qID )


							# for x in dir(threads.thisThread):
							#     print_(x)

							# sys.exit()


							self.spent( threads.qID, 0 )
							self.records[focus]['threads'][i].hasTimedOut = 1
							self.records[focus]['threads'][i].thisThread.kill()
							# print_( 'stopped' )



		# return None
		# if self.opened:
		#     for focus in self.records.keys():
		#         for i, threads in enumerate( self.records[focus]['threads'] ):
		#             if not threads.thisThread is None:
		#                 if threads.status and threads.timeout:
		#                     print_( 'Has timeout' )
		#                     dur = time.time() - threads.log['start']
		#                     if dur > threads.timeout:
		#                         print_( 'time ran out' )
		#                         self.spent( threads.qID, 0 )
		#                         self.records[focus]['threads'][i].hasTimedOut = 1
		#                         self.records[focus]['threads'][i].thisThread.kill()
		#                         self.records[focus]['threads'][i].thisThread.join()
		#                         print_( 'stopped' )



		# if not type( self.timeout ) == bool:
		#     for focus in self.records.keys():
		#         for i,q in enumerate(self.records[focus]['threads']):
		#             if self.records[focus]['threads'][i].status:
		#                 diff = time.time() - self.records[focus]['threads'][i].created
		#                 if diff > self.timeout:
		#                     self.records[focus]['threads'][i].timeout = True
		#                     __.threadQueue[  self.records[focus]['threads'][i].qID  ]._stop()

		# for focus in self.records.keys():
		#     for name in self.records[focus]['names'].keys():
		#         if not type( self.records[focus]['names'][name]['timeout'] ) == bool:
		#             for i,q in enumerate(self.records[focus]['threads']):
		#                 if name == self.records[focus]['threads'][i].name:
		#                     if self.records[focus]['threads'][i].status:
		#                         diff = time.time() - self.records[focus]['threads'][i].created
		#                         if diff > self.records[focus]['names'][name]['timeout']:
		#                             self.records[focus]['threads'][i].timeout = True
		#                             __.threadQueue[  self.records[focus]['threads'][i].qID  ]._stop()



	def audit( self ):
		if not type(self.listeningFor) == bool:
			self.listener()
		self.schedule()
		self.checkTimeout()
		self.isEverythingLoaded()
		__.queueCountAudit += 1
		__.queueCountAuditAudit -= 1
		self.numberClosed()
		if not self.isLoaded:
			if self.autoLoaded:

				diff2 = int(time.time() - __.queueLastActivity)
				diff = int(time.time() - self.lastActivity)
				if diff > self.autoLoadedAfter:
					if diff2 > self.autoLoadedAfter:
						if self.auditPrint:
							print_('Auto Loaded:', diff)

						for focus in self.records.keys():
							for name in self.records[focus]['names'].keys():
								self.loaded( name=name, focus=focus )

						self.numberClosed()


		self.manageData()



		if self.auditPrint:
			if self.projectDataDetected:

				if False:
					print_()
					print_()
					print_('Opened:',self.opened,'\tClosed:',self.totalClosed,'\tClosed:',self.closed,'\tTotal:',self.nextID,'\tMax in queue:',self.maxInQueue,'\tTotal Task:',__.totalTask,'\tTotal Audit:',__.queueCountScheduleAudit+__.queueCountSchedule )
					print_()
				for focus in __.projectData:
					try:
						del __.projectData[focus][0]
					except Exception as e:
						pass
					for name in __.projectData[focus].keys():
						print_( 'pre:', focus, name, __.projectData[focus].keys() )
						print_( '0:', len(__.projectData[focus][name][0]['data']), focus, name )
						print_( '1:', len(__.projectData[focus][name][1]['data']), focus, name )
						if len(__.projectData[focus][name][0]['data']) or len(__.projectData[focus][name][1]['data']):
							if False:
								print_('Name:',name, '\tProject 0 Length:', len(__.projectData[focus][name][0]['data']), '\tProject 1 Length:', len(__.projectData[focus][name][1]['data']),'\tdb:',self.records[focus]['names'][name]['database'] )
							if True:
								print_('Name:',name, '\tOpened:',self.opened,'\tClosed:',self.closed,'\tTotal:',self.nextID,'\tMax in queue:',self.maxInQueue,'\tTotal Task:',__.totalTask, '\tProject 0 Length:', len(__.projectData[focus][name][0]['data']), '\tProject 1 Length:', len(__.projectData[focus][name][1]['data']),'\tdb:',self.records[focus]['names'][name]['database'] )
			else:
				print_('Opened:',self.opened,'\tClosed:',self.closed,'\tTotal:',self.nextID,'\tMax in queue:',self.maxInQueue,'\tTotal Task:',__.totalTask,'\tTotal Audit:',__.queueCountScheduleAudit+__.queueCountSchedule )
			# print_( self.opened, self.isLoaded, self.notstarted )
			if False:
				print_()
				print_( self.opened, self.isLoaded, self.notstarted )
				print_()

		elif self.statusTotal > 0:
			self.printStatus()

		pass
		# if self.opened == 0:
		for f in self.records.keys():
			for n in self.records[f]['names'].keys():
				if self.isEverythingLoadedEach( name=n, focus=f ) and self.isEverythingClosedEach( name=n, focus=f ):
					self.spendFocus( n, f, 2 )


		if self.opened == 0 and self.isLoaded and self.notstarted <= 0:
			if self.auditPrint:
				print_('audit:',__.queueCountAudit)
			self.printReport()
			self.saveData()
			if self.saveLog:
				threadTimer( 1, saveThreadsLog )

			for f in self.records.keys():
				for n in self.records[f]['names'].keys():
					self.spendFocus( n, f, 2 )


		else:
			diff = self.nextID - self.opened

			if diff < 5:
				threadTimer( self.auditLoop, threadAudit )
				# Timer( .5, threadAudit ).start()
			else:
				for f in self.records.keys():
					for n in self.records[f]['names'].keys():

						data = self.getRuntimeMemoryNameFocusTopBottom( n, f )
						if type(data) == bool:
							threadTimer( self.auditLoop, threadAudit )
							# Timer( .5, threadAudit ).start()
							return False
						else:
							diff = percentageDiffInt(data['top'], data['bottom'])
							diff2 = percentageDiffInt(data['top'], data['freshbottom'])

							if diff < self.auditPercentChangeMax or diff2 < self.auditPercentChangeMax:
								self.records[f]['names'][n]['failure'] = 0
								self.records[f]['names'][n]['changes'] = 0
								self.records[f]['names'][n]['watch'] = 0
								shouldAct = False
							else:
								if not self.records[f]['names'][n]['watch'] >= self.auditWatchMax:
									self.records[f]['names'][n]['watch'] += 1
								else:
									self.records[f]['names'][n]['failure'] += 1
									self.records[f]['names'][n]['changes'] += 1
								shouldAct = True

							if shouldAct:

								if self.records[f]['names'][n]['failure'] >= self.auditMaxFailuresBeforeAction:
									lastMax = self.records[f]['names'][n]['maxThreads']
									if self.records[f]['names'][n]['changes'] >= self.auditPercentDrasticThreshold:
										changeBy = self.auditPercentReduceByDrastic
									else:
										changeBy = self.auditPercentReduceBy

									newMax = percentageInt(self.opened, changeBy)

									if newMax < self.minThreads:
										newMax = self.minThreads
									if newMax > self.maxThreadsSafe:
										newMax = self.maxThreadsSafe
									self.auditAutoAdjust = True
									self.records[f]['names'][n]['maxThreads'] = newMax
									print_('_________________________________________')
									print_()
									print_('Changed max threads from:', lastMax,'to:',newMax)

				threadTimer( self.auditLoop, threadAudit )
				# Timer( .5, threadAudit ).start()
	# self.auditWatchMax

# watch

#                           if self.records[f]['names'][n]['maxThreads'] == 0:
#                               newMax = self.opened
#                       percentageInt(percent, whole)
#                       if not self.records[f]['names'][n]['loaded']:
#                           self.records[f]['names'][n]['maxThreads'] = True

#                           self.records[f]['names'][n]['maxThreads'] =


#       self.auditPercentReduceByOverMax = 15       self.maxThreads = 1000
#       self.auditPercentReduceByOverMaxBy = 30


# self.auditPercentReduceByDrastic
#       self.auditPercentChangeMin = 10
#       self. = 5

#       self.auditPercentChangeMin = 10
#       self.auditPercentReduceBy = 5

# self.records[focus]['names'][name]['maxThreads']
# self.auditPercentChangeMax
#           __.queueCountAudit += 1
#           Timer( .5, threadSchedule ).start()

# threadTimer
# thread = Timer( .0001, threadKwargs, data ).start()
# thread = Timer( .0001, threadKwargs, data ).start()
# thread = Timer( .0001, self.func, self.argID ).start()
# thread = Timer( .0001, self.func, self.arg ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( .3, threadAudit ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( .5, threadAudit ).start()
# Timer( .5, threadAudit ).start()
# Timer( .5, threadAudit ).start()


# __.queueCountScheduleAudit = 0
# __.queueCountAuditAudit = 0


	def numberClosed( self ):
		self.isEverythingLoaded()
		totalClosed = 0
		for f in self.records.keys():
			for i,t in enumerate(self.records[f]['threads']):
				for n in self.records[f]['names'].keys():
					if not self.records[f]['threads'][i].name == n:
						self.records[f]['names'][n]['closed'] = 0


		info = {}
		for f in self.records.keys():
			for i,t in enumerate(self.records[f]['threads']):
				if not self.records[f]['threads'][i].status:
					for n in self.records[f]['names'].keys():
						if self.records[f]['threads'][i].name == n:
							try:
								info[n]['total'] += 1
								info[n]['closed'] += 1
							except Exception as e:
								info[n] = {}
								info[n]['total'] = 0
								info[n]['closed'] = 0
								info[n]['total'] += 1
								info[n]['closed'] += 1
							if not self.records[f]['threads'][i].status:
								self.records[f]['names'][n]['closed'] += 1
								totalClosed += 1
						# if info[n]['total'] == info[n]['closed'] and info[n]['total'] > 0 and self.opened == 0 and self.isEverythingLoaded() and self.notstarted == 0:
							if self.isEverythingLoadedEach( name=n, focus=f ) and self.isEverythingClosedEach( name=n, focus=f ):
								self.spendFocus( n, f, 3 )
								# if not type( self.records[f]['names'][n]['trigger'] ) == bool:


		self.totalClosed = totalClosed



	def getRuntimeMemoryNameFocusTopBottom( self, name, focus ):
		topruntime = []
		bottomruntime = []
		bottomruntimeFresh = []

		length = len(self.records[focus]['threads'])
		sampleSize = percentageInt( self.auditPercentSample, length )
		bottom = length - sampleSize
		data = self.getRuntimeMemoryNameFocus( name, focus )
		if type(data) == bool:
			return False
		if len(data['runtimebottom']) < 5:
			return False
		else:

			for i,row in enumerate(data['runtime']):
				if i <= sampleSize:
					topruntime.append(row)
				if i >= bottom:
					bottomruntime.append(row)
			for i,row in enumerate(data['runtimebottom']):
					bottomruntimeFresh.append(row)

			topaverageruntime = self.calcAverage(topruntime)
			bottomaverageruntime = self.calcAverage(bottomruntime)
			freshbottomaverageruntime = self.calcAverage(bottomruntimeFresh)

			return { 'top': topaverageruntime, 'bottom': bottomaverageruntime, 'freshbottom': freshbottomaverageruntime }


	def getRuntimeMemoryFocusTopBottom( self, focus ):
		topruntime = []
		bottomruntime = []

		length = len(self.records[focus]['threads'])
		sampleSize = percentageInt( self.auditPercentSample, length )
		bottom = length - sampleSize
		data = self.getRuntimeMemoryFocus( focus )

		for i,row in enumerate(data['runtime']):
			if i <= sampleSize:
				topruntime.append(row)
			if i >= bottom:
				bottomruntime.append(row)

		topaverageruntime = self.calcAverage(topruntime)
		bottomaverageruntime = self.calcAverage(bottomruntime)

		return { 'top': topaverageruntime, 'bottom': bottomaverageruntime }



def enableThreadDataSwap():
	print_( 'key test00:', __.projectData[ __.processing[0] ].keys() )
	print_( 'enableThreadDataSwap: initiated' )
	# print_( __.processing )
	print_( 'post process size:', len(__.projectData[ __.processing[0] ][ __.processing[1] ][   __.processing[2]   ]['data']) )
	__.saveInitiated = False

	# __.projectData[focus][name][0]['data'] = []
	print_( 'key test0:', __.projectData[ __.processing[0] ].keys() )
	# __.projectData[ __.processing[0] ][ __.processing[1] ][   __.processing[2]   ]['data'] = []
	# __.projectData[ '__main__' ][ 'folder' ][   __.processing[2]   ]['data'] = []
	print_( 'key test1:', __.projectData[ __.processing[0] ].keys() )

# def hasTimedOut():
#   print_( 'hasTimedOut' )

# @timeout( 10, hasTimedOut() )
def threadTimer( tim, func, args=False, qID=False ):
	Timer = __.imp('threading.Timer')
	__.totalTask += 1
	# print_(func.__name__)
	shouldRun = True
	if func.__name__ == 'threadSchedule':
		if __.queueCountScheduleAudit > 4:
			shouldRun = False
		else:
			__.queueCountScheduleAudit += 1

	if func.__name__ == 'threadAudit':
		if __.queueCountAuditAudit > 4:
			shouldRun = False
		else:
			__.queueCountAuditAudit += 1

	if shouldRun:
		if tim < .01:
			tim = .01

		try:
			if type(args) == bool:
				if not type(qID) == bool:
					__.threadQueue[qID] = Timer( tim, func )
					__.threadQueue[qID].start()
				else:
					Timer( tim, func ).start()
			else:
				if not type(qID) == bool:
					__.threadQueue[qID] = Timer( tim, func, args )
					__.threadQueue[qID].start()
				else:
					Timer( tim, func, args ).start()
			__.queueCountTimer += 1
			# https://stackoverflow.com/questions/34562473/most-pythonic-way-to-kill-a-thread-after-some-period-of-time
			# __.threadQueue[qID].join(30)
			# if __.threadQueue[qID].is_alive():
			#   print_( 'Has Timed Out' )
			#   e.set()
			# else:
			#   pass
		except Exception as e:
			print_('Thread Error:',__.queueCountTimer)


def threadAudit():
	global threads
	threads.audit()

def threadSchedule():
	global threads
	threads.schedule()

def threadKwargs( data=False ):
	# print_(data)
	try:
		data['func'](**data['args'][0])
	except Exception as e:
		try:
			data[0]['func'](**data['args'][0])
		except Exception as e:
			print_('Error: kwargs')



def percentageInt( percent, whole, isFloat=False ):
	# return int((percent * whole) / 100.0)
	if not isFloat:
		return int(round( (percent * whole) / 100.0 , 0))
	else:
		return round( (percent * whole) / 100.0 , 1)

def percentageDiffInt( smaller, bigger, isFloat=False, rnd=1 ):
	# fr = force rounding
	# return int((smaller/bigger)*100)
	try:

		if not isFloat:
			return int(round( abs(smaller/bigger)*100, 0))
		else:
			r = round( abs(smaller/bigger)*100, rnd)
			if str(r) == '0.0':
				return 0
			# if str(r).endswtih('.0'):
			#     return int(r)

			return r

	except Exception as e:
		return 0
		smaller+=1
		bigger+=1
		if not isFloat:
			return int(round( abs(smaller/bigger)*100, 0))
		else:
			r = round( abs(smaller/bigger)*100, rnd)
			if str(r) == '0.0':
				return 0
			return r

def percentageDiff( smaller, bigger, isFloat=False ):
	# fr = force rounding
	# return int((smaller/bigger)*100)
	try:

		if not isFloat:
			return abs(smaller/bigger)*100
		else:
			r = abs(smaller/bigger)*100
			if str(r) == '0.0':
				return 0
			# if str(r).endswtih('.0'):
			#     return int(r)

			return r

	except Exception as e:
		return 0
		smaller+=1
		bigger+=1
		if not isFloat:
			return abs(smaller/bigger)*100
		else:
			r = abs(smaller/bigger)*100
			if str(r) == '0.0':
				return 0
			return r


def percentageDiffIntAuto( smaller, bigger, isFloat=False ):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	if not isFloat:
		return percentageDiffInt(s, b)
	else:
		result = round(float((s/b)*100), 1)
		r = str(result)
		if '.0' in r:
			result = int(result)
		return result

def percentageDiffAuto( smaller, bigger, isFloat=False, rnd=1 ):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	return percentageDiffCalc(s, b, isFloat, rnd)

def percentageDiffSmaller( smaller, bigger, isFloat=False, rnd=1 ):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	a = percentageDiffCalc(s, b, isFloat, rnd)
	b = percentageDiffCalc(b, s, isFloat, rnd)
	if a<b:
		return a
	else:
		return b



def percentageDiffCalc( smaller, bigger, isFloat=False, rnd=1 ):
	# x=abs(abs(smaller - bigger)/smaller)*100
	try:

		if not isFloat:
			return int(round( abs(abs(smaller - bigger)/smaller)*100, 0))
		else:
			r = round( abs(abs(smaller - bigger)/smaller)*100, rnd)
			if str(r) == '0.0':
				return 0
			# if str(r).endswtih('.0'):
			#     return int(r)

			return r

	except Exception as e:
		return 0
		smaller+=1
		bigger+=1
		if not isFloat:
			return int(round( abs(abs(smaller - bigger)/smaller)*100, 0))
		else:
			r = round( abs(abs(smaller - bigger)/smaller)*100, rnd)
			if str(r) == '0.0':
				return 0
			return r


	# = 0.2 = 20%
 # |5 - 6|/5 = 1/5 = 0.2 = 20%


	# return percentageDiffInt(s, b, isFloat, rnd)


def LoadingDone(done=None):
	if not done is None:
		__.loadingVar['done'] = done
	__.loadingVar['hasLoaded'] = True

	global threads
	while not __.loadingVar['hasCleared']:
		time.sleep( .2 )
	time.sleep( .7 )
	print_( '                                                        ', end='\r' )
	time.sleep( 2 )
	__.loadingVar['hasCleared'] = False
	__.loadingVar['hasLoaded'] = False
	__.loadingVar['isRunning'] = False
	del threads
	threads = Queue()