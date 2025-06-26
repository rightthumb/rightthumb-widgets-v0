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
def process( name, description=None, isIF=None, focus=None, trackingID=None,    d=None, i=None, f=None ):
		appReg = _matrix.appReg
		if not f is None:
			focus = f

		if focus is None:
			stack = _matrix.app.c(c=1)
			try:
				focus = stack['file']
			except Exception as e:
				stack = _matrix.app.c(i=0,c=1)
				focus = stack['file']
			if focus == _matrix.app.theMatrix:
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
	
		_matrix.app.sequences['all'] +=1
		try:
			_matrix.app.sequences['process']['all'] +=1
		except Exception as e:
			_matrix.app.sequences['process']['all'] = 1

		if registration is None:
			_matrix.app.additional_Not_Registration( 'process', name, registration, focus )
			if _matrix.app.label( name, focus ) in _matrix.app.records[ 'process' ].keys():
				return _matrix.app.records[ 'process' ][ _matrix.app.label( name, focus )]
			if _matrix.app.label( 'Default', 'isDefault' ) in _matrix.app.records[ 'process' ].keys():
				return _matrix.app.records[ 'process' ][ _matrix.app.label( 'Default', 'isDefault' ) ]

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
			
			additional = _matrix.app.additional_Registration( 'process', name, registration )
			if not additional is None:
				registration['additional'] == additional
			try:
				_process_child
			except Exception as e:
				from _rightThumb._matrix import _process_child
			_matrix.app.indexes['labels']['process'].append( name )
			theID = _matrix.app.newMasterID()

			if not _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'process' ].keys():
				_matrix.app.records[ 'process' ][_matrix.app.label( name, focus, isBase=isBase )] = _process_child.TheChild( theID=theID, registration=registration )
			elif _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'process' ].keys():
				_matrix.app.records[ 'process' ][_matrix.app.label( name, focus, isBase=isBase )].add( theID=theID, registration=registration )
			return _matrix.app.records[ 'process' ][_matrix.app.label( name, focus, isBase=isBase )]
			# _matrix.app.records_process[name] = _process_child.TheChild( theID=theID, registration=registration )




