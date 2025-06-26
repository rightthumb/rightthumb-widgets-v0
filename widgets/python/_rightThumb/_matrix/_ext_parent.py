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
def ext( name, app=None, trackingID=None ):
		appReg = _matrix.appReg
		focus = 'live'

		registration = None
		if not _matrix.app.label( name, focus ) in _matrix.app.records['data'].keys():
			registration = { 'name': name, 'app': app, 'focus': focus }
			
		if not app is None:
			registration = { 'name': name, 'app': app, 'focus': focus }
		# print( 'here', name, app, focus, registration )
		_matrix.app.sequences['all'] +=1
		try:
			_matrix.app.sequences['ext']['all'] +=1
		except Exception as e:
			_matrix.app.sequences['ext']['all'] = 1

		if registration is None:
			_matrix.app.additional_Not_Registration( 'ext', name, registration, focus )
			if _matrix.app.label( name, focus ) in _matrix.app.records[ 'ext' ].keys():
				return _matrix.app.records[ 'ext' ][ _matrix.app.label( name, focus )]
			if _matrix.app.label( 'Default', 'isDefault' ) in _matrix.app.records[ 'ext' ].keys():
				return _matrix.app.records[ 'ext' ][ _matrix.app.label( 'Default', 'isDefault' ) ]

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
			
			additional = _matrix.app.additional_Registration( 'ext', name, registration )
			if not additional is None:
				registration['additional'] == additional
			try:
				_ext_child
			except Exception as e:
				from _rightThumb._matrix import _ext_child
			_matrix.app.indexes['labels']['ext'].append( name )
			theID = _matrix.app.newMasterID()

			if not _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'ext' ].keys():
				_matrix.app.records[ 'ext' ][_matrix.app.label( name, focus, isBase=isBase )] = _ext_child.TheChild( theID=theID, registration=registration )
			elif _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'ext' ].keys():
				_matrix.app.records[ 'ext' ][_matrix.app.label( name, focus, isBase=isBase )].add( theID=theID, registration=registration )
			return _matrix.app.records[ 'ext' ][_matrix.app.label( name, focus, isBase=isBase )]
			# _matrix.app.records_ext[name] = _ext_child.TheChild( theID=theID, registration=registration )




