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

import time
def switch( name=None, switch=None, expected_input_example = None, isRequired=False, isPipe=False, description='', examples=None, required=None, related=None, isDefault=False, focus=None, trackingID=None,     f=None, printFocus=False ):
		appReg = _matrix.appReg
		if not f is None:
			focus = f

		if focus is None:
			stack = _matrix.app.c(c=1)
			try:
				focus = stack['programs'][0]
			except Exception as e:
				stack = _matrix.app.c(i=0,c=1)
				focus = stack['file']
			if focus == _matrix.app.theMatrix:
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


		if not _matrix.app.label( name, focus ) in _matrix.app.records[ 'async' ].keys() and _matrix.app.label( name, focus, isBase=True ) in _matrix.app.records[ 'async' ].keys():
			_matrix.app.records[ 'async' ][ _matrix.app.label( name, focus ) ] = _matrix.app.records[ 'async' ][ _matrix.app.label( name, focus, isBase=True ) ]
			return _matrix.app.records[ 'async' ][ _matrix.app.label( name, focus ) ]
		
		_matrix.app.sequences['all'] +=1
		try:
			_matrix.app.sequences['switch']['all'] +=1
		except Exception as e:
			_matrix.app.sequences['switch']['all'] = 1

		if registration is None:
			_matrix.app.additional_Not_Registration( 'switch', name, registration, focus )
			if _matrix.app.label( name, focus ) in _matrix.app.records[ 'switch' ].keys():
				return _matrix.app.records[ 'switch' ][ _matrix.app.label( name, focus )]
			if _matrix.app.label( 'Default', 'isDefault' ) in _matrix.app.records[ 'switch' ].keys():
				return _matrix.app.records[ 'switch' ][ _matrix.app.label( 'Default', 'isDefault' ) ]

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
			registration['hashID'] = _matrix.app.label( name, focus, isBase=isBase )
			
			additional = _matrix.app.additional_Registration( 'switch', name, registration )
			if not additional is None:
				registration['additional'] == additional
			try:
				_switch_child
			except Exception as e:
				from _rightThumb._matrix import _switch_child
			_matrix.app.indexes['labels']['switch'].append( name )
			theID = _matrix.app.newMasterID()

			if not _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'switch' ].keys():
				_matrix.app.records[ 'switch' ][_matrix.app.label( name, focus, isBase=isBase )] = _switch_child.TheChild( theID=theID, registration=registration )
			elif _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'switch' ].keys():
				_matrix.app.records[ 'switch' ][_matrix.app.label( name, focus, isBase=isBase )].add( theID=theID, registration=registration )
			return _matrix.app.records[ 'switch' ][_matrix.app.label( name, focus, isBase=isBase )]
			# _matrix.app.records_switch[name] = _switch_child.TheChild( theID=theID, registration=registration )




