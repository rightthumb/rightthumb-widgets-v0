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
def async( name, script=None, kwargs=None, timeout=None, trigger=None, tkwargs=None, ttimeout=None, focus=None, trackingID=None,    k=None, t=None, tk=None, tt=None, ttime=None, f=None ):
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

		_matrix.app.sequences['all'] +=1
		try:
			_matrix.app.sequences['async']['all'] +=1
		except Exception as e:
			_matrix.app.sequences['async']['all'] = 1

		if registration is None:
			_matrix.app.additional_Not_Registration( 'async', name, registration, focus )
			if _matrix.app.label( name, focus ) in _matrix.app.records[ 'async' ].keys():
				return _matrix.app.records[ 'async' ][ _matrix.app.label( name, focus )]
			if _matrix.app.label( 'Default', 'isDefault' ) in _matrix.app.records[ 'async' ].keys():
				return _matrix.app.records[ 'async' ][ _matrix.app.label( 'Default', 'isDefault' ) ]

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
			
			additional = _matrix.app.additional_Registration( 'async', name, registration )
			if not additional is None:
				registration['additional'] == additional
			try:
				_async_child
			except Exception as e:
				from _rightThumb._matrix import _async_child
			_matrix.app.indexes['labels']['async'].append( name )
			theID = _matrix.app.newMasterID()

			if not _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'async' ].keys():
				_matrix.app.records[ 'async' ][_matrix.app.label( name, focus, isBase=isBase )] = _async_child.TheChild( theID=theID, registration=registration )
			elif _matrix.app.label( name, focus, isBase=isBase ) in _matrix.app.records[ 'async' ].keys():
				_matrix.app.records[ 'async' ][_matrix.app.label( name, focus, isBase=isBase )].add( theID=theID, registration=registration )
			return _matrix.app.records[ 'async' ][_matrix.app.label( name, focus, isBase=isBase )]
			# _matrix.app.records_async[name] = _async_child.TheChild( theID=theID, registration=registration )




