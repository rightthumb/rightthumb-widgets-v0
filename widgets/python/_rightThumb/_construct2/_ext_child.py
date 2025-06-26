import _rightThumb._construct2 as __

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

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.registration = registration
		self.name = None
		self.size = 0
		self.status = True
		self.add( theID, registration )


	"""
	def add( self, theID, registration ):
		__.app.algorithmRegister( 'ext', 'add' )
		self.ids.append( theID )
		self.name = registration['name']
		self.focus = registration['focus']
		self.focusBase = None
		self.app = registration['app']
		self.parent = focus

		self.focus = self.imp.focus( parentApp=focus )
		self.base = registration['base']



		self.app = app
		self.parent = focus

		self.imp = importlib.import_module( self.app )
		self.size = _.get_size(self.imp)
		__.app.memory += self.size

		self.focus = self.imp.focus( parentApp=focus )
		self.focusPop = focus
		
		self.saveLogFile = True

		# load()
		self.imp.registerSwitches( argvProcessForce=False)

		# __.constructRegistration(appInfo[self.imp.focus(focus)]['file'],self.imp.focus(focus))

		__.appReg = self.focusPop



	"""

	def add( self, theID, registration ):
		__.app.algorithmRegister( 'ext', 'add' )
		self.ids.append( theID )
		self.name = registration['name']
		self.app = registration['app']
		self.parent = registration['focus']
		self.focusPop = registration['focus']
		# self.app = self.app+'.py'
		self.imp = None
		_.pr( self.app )
		try:
			self.imp = importlib.import_module( self.app )
		except Exception as e:
			_.pr( 'e:', e, self.app , 'ext 67')
			pass
		self.focus = self.imp.focus( parentApp=registration['focus'] )



		self.size = _.get_size(self.imp)
		__.app.memory += self.size

		
		self.saveLogFile = True

		# load()
		_.pr( '    made it here' )
		self.imp.registerSwitches()

		# __.constructRegistration(appInfo[self.imp.focus(focus)]['file'],self.imp.focus(focus))

		__.appReg = self.focusPop






	# def unregister( self ):

	#   for key in __.app.records['data'].keys():
	#       if self.name in __.app.records['data'][key].focus:
	#           __.app.records['data'][key].unregister()

	#   self.status = False
	#   self.imp = None
	#   __.app.memory -= self.size









 #    def provideImport( self ):
 #        return self.imp

 #    def listFunctions( self ):
 #        self.functions
 #        for func in self.functions:
 #            _.pr( func['name'], func['args'] )

 #    def pipe( self, data=[], focus=None ):
 #      # app.data('Pipe', focus=self.focusPop).set(None)
 #      app.data('Pipe', focus=self.focus).set(data)
 #      if focus is None:
 #          # focus = self.parent
 #          focus = self.focusPop
 #      __.app.transaction( 'ext', _from=self.focus, _to=focus, note='Pipe', data=data )

				
				



 #    def switch( self, names, value=None, appReg=False, delete=False,        d=False ):
 #        global appData
 #        global switches

 #        if type(appReg) == bool:
 #            appReg = self.focusPop

 #        for name in names.split(','):
 #            if not value is None:
 #                try:
 #                    appData[self.focus]['data']['field']['received']
 #                    profile = _profile.records.audit( name, value, appReg=[appReg,self.focus] )
 #                    appData[appReg]['data']['field']['sent'].append( profile )
 #                    appData[self.focus]['data']['field']['received'].append( profile )
 #                except Exception as e:
 #                    pass



 #            __.appReg = self.focus

 #            if delete or d:
 #                switches.fieldSet( name, 'active', False )

 #            else:

 #                switches.fieldSet( name, 'active', True )

 #                # if not type ( value ) == bool:
 #                if not value is None:
 #                    if type( value ) == list:
 #                        switches.fieldSet( name, 'values', value )
 #                        switches.fieldSet( name, 'value', ','.join(value) )
 #                    else:
 #                        switches.fieldSet( name, 'value', value )
 #                        switches.fieldSet( name, 'values', [value] )


 #        __.appReg = self.focusPop

 #    def deleteSwitch( self, name ):
 #        global switches
 #        __.appReg = self.focus

 #        switches.fieldSet( name, 'active', False )

 #        __.appReg = self.focusPop



	def schedule( self ):
		dataID = __.app.data( _.genGUID(), None, f='temp' ).single()
		__.app.async( 'action', self.scheduleRun, kwargs=[dataID], trigger=app.focus(appDBA).unregister )
		return dataID
		# return None



	def scheduleRun( self, dataID=None ):
		if not dataID is None:
			__.appReg = self.focus

		result = self.imp.action()
		__.app.id( dataID ).singleSet(result)


		if focusPop:
			__.appReg = self.focusPop

		return result
		return None


 #    def actionRun( self, focusPop=True ):
 #        __.appReg = self.focus

 #        result = self.imp.action()


 #        if focusPop:
 #            __.appReg = self.focusPop

 #        return result

 #    def action( self, focusPop=True ):
 #        __.appReg = self.focus

 #        result = self.imp.action()

 #        if focusPop:
 #            __.appReg = self.focusPop

 #        return result


 #    def do( self, func, arg=False, focusPop=True ):

 #        __.appReg = self.focus

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
 #            __.appReg = self.focusPop

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


