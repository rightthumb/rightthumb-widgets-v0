
import importlib
class regImp:

	def __init__( self, focus=None, app=None, argvProcessForce=False, dirty=False, a=None, i=None ):
		if focus == 0: focus = None
		# if app == 'file-open': self.switch('Clean')
		DEFAULTS = {
						'file-open': {'Clean': 1},
		}


		if (not '__' and '.' in focus) or app is None:
			# pr('_.imp should be __.imp, auto corrected', focus, c='r')
			return __.imp(focus)

		if not a is None: app=a
		if not i is None: app=i
		global regImps
		global appInfo
		if app is None:
			err( 'class regImp', 'expected: _.regImp(__.appReg,app)  or _.regImp(focus(),app)' )

		if focus is None: focus = __.appReg

		regImps[focus] = {}

		# self.functions = autoKwargsGetArgsFromApp(app)

		self.app = app
		self.parent = focus
		# print_( 'self.imp = importlib.import_module', app )
		self.imp = importlib.import_module(app)
		# self.imp = importlib.util.spec_from_file_location( app, _v.py + _v.slash + app + '.py' )
		# print(app)
		# print(app)
		# print(app)
		# for x in dir(self.imp):
		#   print(x)
		# sys.exit()
		# print_( os.path.isfile( _v.py + _v.slash + app + '.py' ) )
		# print_( self.imp )
		# print_( self.imp.test )
		# sys.exit()
		# print_(self.imp.focus())

		self.focus = self.imp.focus( parentApp=focus )
		# print('self.focus:',self.focus)
		self.focusPop = focus

		self.saveLog = True

		try:
			self.imp.registerSwitches( argvProcessForce=False)
		except Exception as e:
			self.imp.sw()

		appInfo[self.imp.focus(focus)] = appInfo[self.imp.focus()]
		appData[self.imp.focus(focus)] = appData[self.imp.focus()]
		__.constructRegistration(appInfo[self.imp.focus(focus)]['file'],self.imp.focus(focus))

		regImps[focus] = {}
		regImps[focus][app] = self.imp

		__.appReg = self.focusPop

		if dirty   and   not self.focus == '__init___-___init__':
			self.imp.appDBA = self.focus


		# self.provideImport()

		if app in DEFAULTS:
			for sw in DEFAULTS[app]:
				if type(DEFAULTS[app][sw]) == str:
					self.switch(sw,DEFAULTS[app][sw])
				elif DEFAULTS[app][sw]:
					self.switch(sw)
				else:
					self.switch(sw,delete=True)
		# if app == 'file-open': self.switch('Clean')


	def provideImport( self ):
		return self.imp

	def listFunctions( self ):
		self.functions
		for func in self.functions:
			print_( func['name'], func['args'] )

	def pipe( self, data=[], xfer=False, clear=True, appReg=False ):
		global appData
		if type(data) == bool:
			return appData[self.focus]['pipe']

		if type(appReg) == bool:
			appReg = self.focusPop

		if not len( data ):
			if xfer:
				data = appData[appReg]['pipe']
				if clear:
					appData[appReg]['pipe'] = []

		appData[self.focus]['pipe'] = data

		try:
			appData[self.focus]['data']['table']['received']

			profile = _profile.records.audit( 'pipe', data, appReg=[appReg,self.focus] )
			appData[appReg]['data']['table']['sent'].append( profile )
			appData[self.focus]['data']['table']['received'].append( profile )
		except Exception as e:
			pass

	def switch( self, names=[], value=None, appReg=False, dump=False, delete=False,        d=False ):
		global appData
		global switches

		if type(appReg) == bool:
			appReg = self.focusPop

		if dump:
			switches.dumpSwitches()
		else:
			for name in names.split(','):
				vl = value
				if name == 'Password' or name == 'Key':
					vl = '*******'
				if not value is None:
					try:
						appData[self.focus]['data']['field']['received']
						profile = _profile.records.audit( name, vl, appReg=[appReg,self.focus] )
						appData[appReg]['data']['field']['sent'].append( profile )
						appData[self.focus]['data']['field']['received'].append( profile )
					except Exception as e:
						pass


				# print_(self.focus)
				__.appReg = self.focus

				if delete or d:
					switches.fieldSet( name, 'active', False )

				else:

					switches.fieldSet( name, 'active', True )

					# if not type ( value ) == bool:
					if not value is None:
						if type( value ) == list:
							switches.fieldSet( name, 'values', value )
							switches.fieldSet( name, 'value', ','.join(value) )
						else:
							switches.fieldSet( name, 'value', value )
							switches.fieldSet( name, 'values', [value] )


			pass
		__.appReg = self.focusPop

	def deleteSwitch( self, name ):
		global switches
		__.appReg = self.focus

		switches.fieldSet( name, 'active', False )

		__.appReg = self.focusPop


	def kwargs( self, *args, **kwargs ):
		focusPop=True
		if 'focusPop' in kwargs:
			focusPop=kwargs['focusPop']
			del kwargs['focusPop']

		__.appReg = self.focus

		self.imp.appDBA = self.focus
		if args and kwargs:
			result = self.imp.action(*args, **kwargs)
		elif args:
			result = self.imp.action(*args)
		elif kwargs:
			result = self.imp.action(**kwargs)
		else:
			result = self.imp.action()

		if focusPop:
			__.appReg = self.focusPop

		return result
	def action( self, arg='c766f06b', focusPop=True ):
		# focusBK = __.appReg
		__.appReg = self.focus

		self.imp.appDBA = self.focus
		if not arg == 'c766f06b':
			result = self.imp.action(arg)
		else:
			result = self.imp.action()

		if focusPop:
			__.appReg = self.focusPop

		return result


	# def do( self, func, arg=False, focusPop=True ):
	def do(self, *args, **kwargs):
		# focusBK = __.appReg
		focusPop=True

		args=list(args)
		if len(args) == 1 and args[0] == 'action': return self.action()
		func=args.pop(0)
		_kwargs={}
		for k in kwargs:
			if k == 'focusPop': focusPop=kwargs[k]
			else: _kwargs[k]=kwargs[k]

		__.appReg = self.focus

		if 'function' in str(type( func )):
			return func()
		elif type( func ) == str:
			theFunction = eval( 'self.imp.' + func )
		else:
			theFunction = func

		result = 'theFunction'+fak(args,kwargs)


		# if type( arg ) == bool:
		#   result = theFunction()
		# elif type( arg ) == dict:
		#   result = theFunction(**arg)
		# elif type( arg ) == list:
		#   result = theFunction(*arg)
		# else:
		#   result = theFunction(arg)



		if focusPop:
			__.appReg = self.focusPop

		return result

	def execute( self, func, arg=False, nofocus=False ):
		global threads
		theFunc = eval('self.imp.'+func)

		shouldRun = True
		if not nofocus and  type(arg) == bool:
			args = [ self.focus ]
		elif not nofocus and  not type(arg) == bool:
			args = [ arg, self.focus ]

		if nofocus and  type(arg) == bool:
			shouldRun = False
			theID = threads.add( 'execute', theFunc, loaded=True )
		elif nofocus and  not type(arg) == bool:
			args = [ arg ]


		if shouldRun:

			theID = threads.add( 'execute', theFunc, args, loaded=True )

		# if self.saveLog:
		# else:
		#   theID = threads.add( 'execute', theFunc, [ arg, self.focus ], trigger=saveThreadsLog, loaded=True )

		return theID