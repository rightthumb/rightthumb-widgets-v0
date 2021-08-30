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
def db( name, registration=None, focus=None, trackingID=None ):
		appReg = _matrix.appReg
		_matrix.app.sequences['all'] +=1
		try:
			_matrix.app.sequences['db']['all'] +=1
		except Exception as e:
			_matrix.app.sequences['db']['all'] = 1

		if registration is None:
			_matrix.app.additional_Not_Registration( 'db', name, registration, focus )
			if _matrix.app.label( name, focus ) in _matrix.app.records[ 'db' ].keys():
				return _matrix.app.records[ 'db' ][ _matrix.app.label( name, focus )]
			if _matrix.app.label( 'Default', 'isDefault' ) in _matrix.app.records[ 'db' ].keys():
				return _matrix.app.records[ 'db' ][ _matrix.app.label( 'Default', 'isDefault' ) ]

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
			
			additional = _matrix.app.additional_Registration( 'db', name, registration )
			if not additional is None:
				registration['additional'] == additional
			try:
				_db_child
			except Exception as e:
				from _rightThumb._matrix import _db_child
			_matrix.app.indexes['labels']['db'].append( name )
			theID = _matrix.app.newMasterID()

			if not _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'db' ].keys():
				_matrix.app.records[ 'db' ][_matrix.app.label( name, focus, isBase=isBase )] = _db_child.TheChild( theID=theID, registration=registration )
			elif _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'db' ].keys():
				_matrix.app.records[ 'db' ][_matrix.app.label( name, focus, isBase=isBase )].add( theID=theID, registration=registration )
			return _matrix.app.records[ 'db' ][_matrix.app.label( name, focus, isBase=isBase )]
			# _matrix.app.records_db[name] = _db_child.TheChild( theID=theID, registration=registration )



