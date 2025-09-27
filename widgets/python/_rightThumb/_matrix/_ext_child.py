import _rightThumb._matrix as _matrix

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import _rightThumb._base3 as _
import importlib

thisChildApp = _matrix.GenChildLabel.gen( __file__ )

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.registration = registration
		self.name = None
		self.size = 0
		self.status = True
		self.add( theID, registration )

	def callers( self, trackingID=None ):_.printVar( _matrix.app.algorithmRegister(trackingID=trackingID) );


	def add( self, theID, registration ):
		# _.pr( '  *** ext here A ***' )
		algorithm = _matrix.app.algorithmRegister(trackingID=registration['trackingID'])
		self.ids.append( theID )
		self.focus = registration['focus']
		self.name = registration['name']
		self.hashID = registration['hashID']

		self.app = registration['app']
		self.parent = registration['focus']
		self.focusPop = registration['focus']
		# self.app = self.app+'.py'
		self.imp = None
		# _.pr( self.app )
		try:
			self.imp = importlib.import_module( self.app )
		except Exception as e:
			# _.pr( 'e:', e, self.app , 'ext 67')
			pass
		# _.pr( '  *** ext here X ***' )
		# self.focus = self.imp.focus( parentApp=registration['focus'] )


		self.size = _.get_size(self.imp)
		# try:
		# except Exception as e:
		#     pass

		
		self.saveLogFile = True

		# load()
		# _.pr( '    made it here' )
		self.imp.registration()

		# _matrix.constructRegistration(appInfo[self.imp.focus(focus)]['file'],self.imp.focus(focus))

		_matrix.appReg = self.focusPop

		_matrix.app.totalMemory()
		_matrix.app.algorithmResult( algorithm, result=None )
		# _.pr( '  *** ext here B ***' )



	def unregister( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		# _.pr( 'unregistered' )
	# for key in _matrix.app.records['data'].keys():
	#     if self.name in _matrix.app.records['data'][key].focus:
	#         _matrix.app.records['data'][key].unregister()
		appDBA = self.imp.appDBA
		self.status = False
		self.imp = None
		self.size = _.get_size(self.imp)
		_matrix.app.totalMemory()
		_matrix.app.focus(appDBA).unregister()
		# _.pr( 'unregistered complete' )
		# _.colorThis( [ self.name, '_matrix.app.memory_max', _.formatSize(_matrix.app.memory_max) ], 'yellow' )
		_matrix.app.algorithmResult( algorithm, result=None )



	def action2( self, unload=False, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		# _matrix.appReg = self.focus

		result = self.imp.action()


		# if focusPop:
		#     _matrix.appReg = self.focusPop

		if unload:
			self.unregister()
		
		return _matrix.app.algorithmResult( algorithm, result=result )
	

	def action( self, unload=False, schedule=False, timeout=None, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		if schedule:
			algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
			temp = self.schedule( unload=unload, timeout=timeout )
			result = _matrix.app.id( temp ).singleGetWait()
		elif not schedule:
			result = self.imp.action()
			# _.pr( result )

		return _matrix.app.algorithmResult( algorithm, result=result )


	def scheduleAction( self, unload=False, timeout=None, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)

		dataID = _matrix.app.data( _matrix.genUUID() ).single()

		if unload:
			_matrix.app.async( _matrix.genUUID(), self.scheduleRunAction, kwargs=[dataID], trigger=self.unregister, timeout=timeout )
		else:
			_matrix.app.async( _matrix.genUUID(), self.scheduleRunAction, kwargs=[dataID], timeout=timeout )
		
		return _matrix.app.algorithmResult( algorithm, result=dataID )

	def schedule( self, unload=False, timeout=None, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)

		dataID = _matrix.app.data( _matrix.genUUID() ).single()

		if unload:
			_matrix.app.async( _matrix.genUUID(), self.scheduleRunAction, kwargs=[dataID], trigger=self.unregister, timeout=timeout )
		else:
			_matrix.app.async( _matrix.genUUID(), self.scheduleRunAction, kwargs=[dataID], timeout=timeout )
		
		return _matrix.app.algorithmResult( algorithm, result=dataID )


	def scheduleRunAction( self, dataID=None, unload=False, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		# if not dataID is None:
		#     _matrix.appReg = self.focus

		result = self.imp.action()
		_matrix.app.id( dataID ).singleSet(result)


		# if focusPop:
		#     _matrix.appReg = self.focusPop

		if unload:
			self.unregister()
		
		return _matrix.app.algorithmResult( algorithm, result=result )



 #    def actionRun( self, focusPop=True ):
 #        _matrix.appReg = self.focus

 #        result = self.imp.action()


 #        if focusPop:
 #            _matrix.appReg = self.focusPop

 #        return result

 #    def action( self, focusPop=True ):
 #        _matrix.appReg = self.focus

 #        result = self.imp.action()

 #        if focusPop:
 #            _matrix.appReg = self.focusPop

 #        return result


 #    def do( self, func, arg=False, focusPop=True ):

 #        _matrix.appReg = self.focus

 #        if type( func ) == str:
 #            theFunction = eval( 'self.imp.' + func )
 #        else:
 #            theFunction = func

 #        if type( arg ) == bool:
 #            result = theFunction()
 #        elif type( arg ) == dict:
 #            result = theFunction(**arg)
 #        elif type( arg ) == list:
 #            result = theFunction(*arg)

		

 #        if focusPop:
 #            _matrix.appReg = self.focusPop

 #        return result

 #    def execute( self, func, arg=False, nofocus=False ):
 #        global threads
 #        theFunc = eval('self.imp.'+func)

 #        shouldRun = True
 #        if not nofocus and  type(arg) == bool:
 #            args = [ self.focus ]
 #        elif not nofocus and  not type(arg) == bool:
 #            args = [ arg, self.focus ]

 #        if nofocus and  type(arg) == bool:
 #            shouldRun = False
 #            theID = threads.add( 'execute', theFunc, loaded=True )
 #        elif nofocus and  not type(arg) == bool:
 #            args = [ arg ]


 #        if shouldRun:

 #            theID = threads.add( 'execute', theFunc, args, loaded=True )

 #        # if self.saveLogFile:
 #        # else:
 #        #   theID = threads.add( 'execute', theFunc, [ arg, self.focus ], trigger=saveThreadsLog, loaded=True )

 #        return theID



