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

import re
import sys


def build():
	
	

	if _.switches.isActive('Verses'):
		base = ' '.join( _.switches.values('Verses') )
		if _.switches.isActive('Minus'):
			minus = ' '.join( _.switches.values('Minus') )
			base+='-'+minus
		base = _str.replaceDuplicate(base,' ')
		base = _str.cleanBE(base,' ')
		base = base.replace( ' :', ':' )
		base = base.replace( ': ', ':' )
		base = base.replace( '- ', '-' )
		base = base.replace( ' -', '-' )
		if not ':' in base:
			base+=':0'
			# _.pr( base )
			# sys.exit()

		q = {
				'book': None,
				'chapter': None,
				'verse': None,
		}
		# _.pr( ':', base.count(':') )
		# _.pr( '-', base.count('-') )
		if base.count(':') > 1:
			matches = re.finditer(   ':'   , base)
			dex = [match.start() for match in matches]
			# _.pr( 'dex', dex )
		# _.pr()
		# _.pr( base )
		# _.pr()
		# separate multi book and verse
		#    p Bible -vs jn 1:1-2-2:4-6
		clean=False
		i=0
		while not clean and i<50:
			i+=1
			# _.pr('itter')
			clean = True
			n = []
			for y in base.split(' '):
				hasDash=False
				dashFixed=False
				b = ''
				for x in y:
					if x == '-':
						if hasDash and not dashFixed:
							dashFixed = True
							b+=' - '
						else:
							b+='-'
							hasDash = True

					else:
						b+=x
				n.append(b)
			base = ' '.join(n)
			base = _str.replaceDuplicate(base,' ')
			base = _str.cleanBE(base,' ')
			n = []
			for y in base.split(' '):
				if y.count(':') > 1 and y.count('-') == 1:
					n.append( y.split('-')[0] )
					n.append( '-' )
					n.append( y.split('-')[1] )
				else:
					n.append(y)
			base = ' '.join(n)
			base = _str.replaceDuplicate(base,' ')
			base = _str.cleanBE(base,' ')    

			for y in base.split(' '):
				if y.count('-') > 1:
					clean = False
				if y.count(':') > 1:
					clean = False
		if i>45:
			_.colorThis( ' You entered that wrong, try again ', 'red' )
		
		# book number test
		base = _str.replaceDuplicate(base,' ')
		base = base.replace( '--','-' )
		base = base.replace( '- -','-' )
		base = _str.cleanBE(base,' ')
		base = _str.cleanBE(base,'--')
		base = _str.cleanBE(base,'-')
		base = _str.cleanBE(base,' ')
		xp = base.split(' ')
		mx = len(xp)-1
		n = []
		addNext = True
		for i,x in enumerate(xp):
			shouldAdd=True
			hasAfter=True;
			if i==mx:
				hasAfter=False
			if x=='1' or x=='2' or x=='3' and hasAfter:
				if x+xp[i+1] in _B.Books:
					shouldAdd=False
					n.append(x+xp[i+1])
					addNext=False
			if shouldAdd:
				if addNext:
					n.append(x)
				addNext=True

		base = ' '.join(n)


		# add book to segments
		xp = base.split(' ')
		mx = len(xp)-1
		n = []
		addNext = True
		lastBook='Error'
		for i,x in enumerate(xp):
			if hasAlpha(x):
				lastBook = x
			else:
				if ':' in x:
					n.append(lastBook+' '+x)
				else:
					n.append(x)
		# base = ' '.join(n)

		done=False
		while not done:
			done=True
			ni = []
			for i,x in enumerate(n):
				if x == '-':
					ni.append(i)
					done=False
			if not done:
				nn = []
				nm = []
				for i,x in enumerate(n):
					if not i in ni and not i-1 in ni and not i+1 in ni:
						nn.append(x)
					else:
						nm.append( x )
						if len(nm) == 3:
							nn.append(nm)
							nm = []
				n = nn



		_B.query = n


def hasAlpha( check ):
	for x in check:
		if x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
			return True
	return False







