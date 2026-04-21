#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import sys
import _rightThumb._construct as __
import _rightThumb._vars as _v
os=__.os
h  = _v.config_hash['wprofile']
index=__.getTable(_v.table('bookmarks.index'))['labels']
bm=sys.argv[len(sys.argv)-1]
if bm in index:
	print(_v.resolveFolderIDs(index[bm]))