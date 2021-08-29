import _rightThumb._matrix as _matrix
import time
def nuc( name, registration=None, focus=None, trackingID=None ):
		appReg = _matrix.appReg
		_matrix.app.sequences['all'] +=1
		try:
			_matrix.app.sequences['nuc']['all'] +=1
		except Exception as e:
			_matrix.app.sequences['nuc']['all'] = 1

		if registration is None:
			_matrix.app.additional_Not_Registration( 'nuc', name, registration, focus )
			if _matrix.app.label( name, focus ) in _matrix.app.records[ 'nuc' ].keys():
				return _matrix.app.records[ 'nuc' ][ _matrix.app.label( name, focus )]
			if _matrix.app.label( 'Default', 'isDefault' ) in _matrix.app.records[ 'nuc' ].keys():
				return _matrix.app.records[ 'nuc' ][ _matrix.app.label( 'Default', 'isDefault' ) ]

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
			
			additional = _matrix.app.additional_Registration( 'nuc', name, registration )
			if not additional is None:
				registration['additional'] == additional
			try:
				_nuc_child
			except Exception as e:
				from _rightThumb._matrix import _nuc_child
			_matrix.app.indexes['labels']['nuc'].append( name )
			theID = _matrix.app.newMasterID()

			if not _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'nuc' ].keys():
				_matrix.app.records[ 'nuc' ][_matrix.app.label( name, focus, isBase=isBase )] = _nuc_child.TheChild( theID=theID, registration=registration )
			elif _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'nuc' ].keys():
				_matrix.app.records[ 'nuc' ][_matrix.app.label( name, focus, isBase=isBase )].add( theID=theID, registration=registration )
			return _matrix.app.records[ 'nuc' ][_matrix.app.label( name, focus, isBase=isBase )]
			# _matrix.app.records_nuc[name] = _nuc_child.TheChild( theID=theID, registration=registration )

