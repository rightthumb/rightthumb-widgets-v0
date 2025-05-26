import _rightThumb._construct as __

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
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._Bible as _B


def label(q):

	if type(q) == str:
		if ':0' in q:
			q = q.split(':0')[0]
		q = [q]

	result = []

	lastBook=''
	for rec in q:
		for x in rec.split(' '):
			if x in _B.Books:
				bk = _B.labels[ str(_B.Books[x]) ]
				# _.pr( bk, lastBook )
				if not bk == lastBook:
					result.append(  bk  )
				lastBook = bk
			else:
				result.append(x)
	_.colorThis( [ ' '.join( result ) ], 'green' )

	



