

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
import _rightThumb._vars as _v
import _rightThumb._encryptString as _blowfish
import _rightThumb._md5 as _md5

def getText( theFile, raw=False, clean=False,  e=0 ):
	lines = None
	if os.path.isfile(theFile):
		try:
			f = open(theFile, 'r', encoding='utf-8')
			lines = f.readlines()
			f.close()
		except Exception as e:
			try:
				f = open(theFile, 'r', encoding='latin-1')
				lines = f.readlines()
				f.close()
			except Exception as e:
				f = open(theFile, 'r')
				lines = f.readlines()
				f.close()
	else:
		if not e:
			return None
		print('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( '\\n', '\n' )

		if clean:
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		return txt
	elif clean:
		# lines = _str.replaceDuplicate( lines, '\n' )
		# lines = _str.cleanBE( lines, '\n' )
		for i,row in enumerate(lines):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			if type(clean) == int:
				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )
			if clean == 3:
				row = ' ' + row + ' '

			# print( row )
			lines[i] = row
		return lines
	else:
		return lines

def saveText( rows, theFile, errors=True ):
	# print(type(rows))
	try:
		if type(rows) == bytes:
			rows = str(rows,'utf-8')
		f = open(theFile,'w', encoding='utf-8')
		# if type(rows) == str:

		# print(type(rows))
		# f.write(str(rows))
		# rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
		# f.write(rows)
		# f.write(rows.encode("iso-8859-1", "replace"))

		# print(type(rows))
		if type(rows) == str:
			# print(rows)
			f.write(rows)
		else:
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						f.write(str(row) + '\n')
				else:
					f.write(str(row) + '\n')
		f.close()
	except Exception as e:
		if type(rows) == list:
			result = ''
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						result += str(row) + '\n'
				else:
					result += str(row) + '\n'

			rows = result
		open(theFile, 'wb').write(rows)
		if errors:
			print( 'Auto correction when saving text' )
def default():
	from _rightThumb._vault import vault_helper
	extract = vault_helper.action()

	fld = str(_v.python['src']['windows']+_v.slash+'_rightThumb'+_v.slash+'_vault'+_v.slash+'helper.py').split(str(_v.slash))
	fld.reverse()
	fld[0] = 'helper.py'
	fld.reverse()
	f = _v.slash.join( fld )

	file = getText( f, raw=True )
	if 'platform' in file:
		foundPlat = True
	else:
		foundPlat = False
		print(_md5.md5(str(extract)))
		print(_md5.md5(str(extract)))
		saveText( _blowfish.decrypt( file, _md5.md5(str(extract)) ), f )
	from _rightThumb._vault import helper
	if foundPlat:
		helperEn()
	else:
		saveText(file,f)
	return helper.passcret()

def helperEn():
	from _rightThumb._vault import vault_helper
	extract = vault_helper.action()
	fld = str(_v.python['src']['windows']+_v.slash+'_rightThumb'+_v.slash+'_vault'+_v.slash+'helper.py').split(str(_v.slash))
	fld.reverse()
	fld[0] = 'helper.py'
	fld.reverse()
	f = _v.slash.join( fld )
	file = getText( f, raw=True )
	saveText( _blowfish.encrypt( file, _md5.md5(str(extract)) ), f )

