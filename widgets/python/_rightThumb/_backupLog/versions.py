# from _rightThumb._backupLog import versions as versions

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


import os
import time

import _rightThumb._construct as __
import _rightThumb._base3 as _
import _rightThumb._dir as _dir


def subject( item ):
	if _.isWin:
		return item.lower()
	else:
		return item

def flag( item, search='v' ):

	if item not None and type(item) == dict and 'flag' in item:
		if search in item['flag'].lower().split(','):
			return True
	return False
s = subject

class Versions:
	def __init__( self ):
		self.vs = _.getTable( 'fileBackup-versions.index' )
		self.levelOn = 604800



	def save( self ):
		_.saveTable( self.vs, 'fileBackup-versions.index' )

	def file( self, path=None, record=None ):
		if not os.path.isfile(path):
			return None
		if record is None:
			info = _dir.info(path)
			e = info['me']
		else:
			e = record['timestamp']
		if not s(path) in self.vs:
			self.vs[s(path)] = {
									'v0': 0,
									'v1': 0,
									'v2': 0,
									'v3': 0,
									'e': 0,
									'v': '0.0.0.0',
								}

		self.vs[s(path)]['v3'] += 1
		v = self.vs[s(path)]
		
		if record is None:
			if info['me'] < v['e']:
				return None
		else:
			if record['timestamp'] < v['e']:
				return None

		if flag( record, 'v' ):
			self.vs[s(path)]['v0'] += 1
			self.vs[s(path)]['v1'] = 0
			self.vs[s(path)]['v2'] = 0

		if e >= self.levelOn:
			self.vs[s(path)]['v1'] += 1
			self.vs[s(path)]['v2'] = 0
		else:
			self.vs[s(path)]['v2'] += 1

		version = self.vs[s(path)]['v0'] +'.'+ self.vs[s(path)]['v1'] +'.'+ self.vs[s(path)]['v2'] +'.'+ self.vs[s(path)]['v3']
		self.vs[s(path)]['v'] = version
		if record is None:
			self.vs[s(path)]['e'] = info['me']
		else:
			self.vs[s(path)]['e'] = record['timestamp']

		if record is None:
			self.save()
		return version

v = Versions()

