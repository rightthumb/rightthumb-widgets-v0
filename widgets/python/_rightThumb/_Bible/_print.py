import _rightThumb._construct as __
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
				# print( bk, lastBook )
				if not bk == lastBook:
					result.append(  bk  )
				lastBook = bk
			else:
				result.append(x)
	_.colorThis( [ ' '.join( result ) ], 'green' )

	
