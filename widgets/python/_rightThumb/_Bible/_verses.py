import _rightThumb._construct as __
import _rightThumb._base3 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._Bible as _B


def build(q):
	table = []
	if type(q) == str:
		if ':0' in q:
			# print( 'asdf', q )
			q = q.split(':0')[0]
			xp = q.split(' ')
			# print(xp[0])
			# print(_B.Books)
			bk = str(_B.Books[xp[0]])
			ch = str(xp[1])
			vs = 1
			done=False
			
			while not done:
				if not str(vs) in _B.Bible[bk][ch]:
					done=True
				else:
					table.append({ 'vs': str(vs), 'word': _B.Bible[bk][ch][str(vs)] })
				vs+=1

			return table



	if type(q) == str:
		xp = q.split(' ')
		bk = str(_B.Books[xp[0]])
		ch = xp[1].split(':')[0]
		vs = xp[1].split(':')[1]
		if not '-' in vs:
			return [{ 'vs': str(vs), 'word': _B.Bible[bk][ch][vs] }]
		vsS = int(vs.split('-')[0])
		vsE = int(vs.split('-')[1])
		ii=vsS
		i=0
		while ii < vsE+1 and i < 1000:
			i+=1
			# print(ii)
			try:
				table.append({ 'vs': str(ii), 'word': _B.Bible[bk][ch][str(ii)] })
			except Exception as e:
				pass
			ii+=1
		

		return table
	elif type(q) == list:
		start = q[0]
		end = q[2]
		bk = str(_B.Books[start.split(' ')[0]])
		aCH = int(start.split(' ')[1].split(':')[0])
		aVS = int(start.split(' ')[1].split(':')[1])

		bCH = int(end.split(' ')[1].split(':')[0])
		bVS = int(end.split(' ')[1].split(':')[1])

		# print( bk )
		# print( aCH, aVS )
		# print( bCH, bVS )

		ch = aCH
		vs = aVS
		done=False
		while not done:
			if not str(vs) in _B.Bible[bk][str(ch)]:
				vs = 1
				ch+=1
				if not str(ch) in _B.Bible[bk]:
					done = True
				if not done:
					table.append({ 'ch': ch })
			if not done:
				table.append({ 'vs': vs, 'word': _B.Bible[bk][str(ch)][str(vs)] })
			# print( bk, ch, vs )
			if ch == bCH and vs == bVS:
				done=True
			vs+=1
		# print( vs ,bVS )
		return table



