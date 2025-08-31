

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

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
				print( 'focus', focus )

		if name is None:
			name = 'Default'
			focus = 'isDefault'
		if switch is None:
			registration = None
		else:
			registration = { 'name': name, 'switches': switch, 'expected_input_example': expected_input_example, 'isRequired': isRequired, 'isPipe': isPipe, 'description': description, 'examples': examples, 'required': required, 'related': related, 'isDefault': isDefault }


		if not self.label( name, focus ) in self.records[ 'async' ].keys() and self.label( name, focus, isBase=True ) in self.records[ 'async' ].keys():
			self.records[ 'async' ][  self.label( name, focus )  ] = self.records[ 'async' ][  self.label( name, focus, isBase=True )  ]
			return self.records[ 'async' ][  self.label( name, focus )  ]
		


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
		# print( 'here', name, app, focus, registration )


