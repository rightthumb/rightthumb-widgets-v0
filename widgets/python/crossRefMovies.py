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

import os
import sys
import time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append(focus())
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register('Input', '-i,-f,-file','one.csv two.csv')
	_.switches.register('FileOne', '-1,-one','%tmpf1%')
	_.switches.register('FileTwo', '-2,-two','%tmpf2%')
	_.switches.register('NoCount', '-nocount')
	_.switches.register('Report', '-report','1')
	_.switches.register('NoCount', '--c')

	_.switches.register('Exif', '-exif','new,files')
	_.switches.register('CSV', '-csv')

	_.switches.register('Single', '-single')

	_.switches.register('Test', '-test')


_.appInfo[focus()] = {
	'file': 'crossRefMovies.py',
	'description': 'Cross reference 2 lists',
	'categories': [
						'lists',
						'data',
						'research',
						'xref',
						'cross reference',
						'entertainment',
						'ent',
						'movies',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

_.appInfo[focus()]['relatedapps'].append('p dir ? Generates Files for this app')
_.appInfo[focus()]['relatedapps'].append('p jsonFieldsInFolder ? ')
_.appInfo[focus()]['relatedapps'].append('p exifCompare ? ')


_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2%')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -nocount')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -nocount -report 1')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -report 2')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -report')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -nocount --c')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -nocount --c -report 1')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -csv')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -exif')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -exif n')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -exif new')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -exif file')
_.appInfo[focus()]['examples'].append('p crossRefMovies -1 %tmpf1% -2 %tmpf2% -exif f n')
_.appInfo[focus()]['examples'].append('')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		_.argvProcess = True
		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()



def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )

def setPipeData(data):
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in data:
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')



focus()
_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )



########################################################################################
# START

import exifCompare as _exif
focus()

def relevantFolders():
	global fDataOne
	global fDataTwo
	global fDataOneTotal
	global fDataTwoTotal
	global relevantFoldersOne
	global relevantFoldersTwo

	# _.pr( fDataOne )
	toDrillDown = []
	_.pr()
	for k in fDataOne.keys():
		s = fDataOne[k]
		p = _.percentageDiffIntAuto( fDataOne[k], fDataOneTotal )
		if p > 5:
			toDrillDown.append( k )
			_.pr( p, k, fDataOne[k], fDataOneTotal )
	cMax = 0
	for k in toDrillDown:
		s = fDataOne[k]
		p = _.percentageDiffIntAuto( fDataOne[k], fDataOneTotal )
		if p == 100:
			if k.count( _v.slash ) > cMax:
				cMax = k.count( _v.slash )

	for k in toDrillDown:
		s = fDataOne[k]
		p = _.percentageDiffIntAuto( fDataOne[k], fDataOneTotal )
		if p == 100:
			if k.count( _v.slash ) == cMax:
				relevantFoldersOne.append( k )
		else:
			relevantFoldersOne.append( k )
	_.pr()
	for rf in relevantFoldersOne:
		_.pr( rf )
	_.pr()
	_.pr()
	if not _.switches.isActive('Single'):
		toDrillDown = []
		for k in fDataTwo.keys():
			s = fDataTwo[k]
			p = _.percentageDiffIntAuto( fDataTwo[k], fDataTwoTotal )
			if p > 5:
				toDrillDown.append( k )
				_.pr( p, k, fDataTwo[k], fDataTwoTotal )
		cMax = 0
		for k in toDrillDown:
			s = fDataTwo[k]
			p = _.percentageDiffIntAuto( fDataTwo[k], fDataTwoTotal )
			if p == 100:
				if k.count( _v.slash ) > cMax:
					cMax = k.count( _v.slash )

		for k in toDrillDown:
			s = fDataTwo[k]
			p = _.percentageDiffIntAuto( fDataTwo[k], fDataTwoTotal )
			if p == 100:
				if k.count( _v.slash ) == cMax:
					relevantFoldersTwo.append( k )
			else:
				relevantFoldersTwo.append( k )
		_.pr()
		for rf in relevantFoldersTwo:
			_.pr( rf )

def documentFolders( folder, tL=1 ):
	global fDataOne
	global fDataTwo
	global fDataOneTotal
	global fDataTwoTotal
	if tL == 1:
		fDataOneTotal += 1
	if tL == 2:
		fDataTwoTotal += 1

	folder = str(folder).lower()
	
	if _v.slash in folder:
		f = folder.split(_v.slash)
		fx = ''
		for fRow in f:
			fx += fRow + _v.slash
			fy = _str.cleanBE( fx , _v.slash )
			if tL == 1:
				try:
					fDataOne[fy] += 1
				except Exception as e:
					fDataOne[fy] = 1

			if tL == 2:
				try:
					fDataTwo[fy] += 1
				except Exception as e:
					fDataTwo[fy] = 1
def documentExt( file ):
	global ext
	file = str(file).lower()
	if '.' in file:
		e = file.split( '.' )
		ex = e[ len(e)-1 ]
		if not ex in ext:
			ext.append( ex )

def xRefTrue( data ):
	global dOne
	global dTwo
	global behavior
	if len( dOne[data] ) == 1 and len( dTwo[data] ) == 1:
		_.pr()
		_.pr( dOne[data] )
		_.pr( dTwo[data] )

def noFranchise():
	global dOne
	global dTwo
	missingFranchise = []
	_.pr()
	_.pr()
	_.pr()
	for k in dOne.keys():
		found = False
		for record in dOne[k]:
			if not len(record['franchise']):
				found = True
		if found:
			missingFranchise.append( k )
			_.pr( k )
	if not _.switches.isActive('Single'):
		for k in dTwo.keys():
			found = False
			for record in dTwo[k]:
				if not len(record['franchise']):
					found = True
			if found:
				missingFranchise.append( k )
				_.pr( k )

def words():
	global dOne
	global dTwo

	for k in dOne.keys():
		k = _str.removeNonAlpha2( k )
		k = _str.replaceDuplicate( k,' ' )
		k = _str.cleanBE( k,' ' )
		for s in k.split(' '):
			_.pr( s.lower() )

	for k in dTwo.keys():
		k = _str.removeNonAlpha2( k )
		k = _str.replaceDuplicate( k,' ' )
		k = _str.cleanBE( k,' ' )
		for s in k.split(' '):
			_.pr( s.lower() )
def exif():
	global dOne
	global dTwo

	c = 'exiftool "THEFILE" -json > C:\\exif\\MOD_BYTES.json'
	e = 'C:\\exif\\MOD_BYTES.json'

	# _.pr(dOne)

	exifFiles = []
	for k in dOne.keys():
		for row in dOne[k]:
			f = str(row['folder']) + _v.slash + str(row['file'])
			x = c.replace( 'MOD', str(row['mod']) ).replace( 'BYTES', str(row['bytes']) ).replace( 'THEFILE', f )
			te = e.replace( 'MOD', str(row['mod']) ).replace( 'BYTES', str(row['bytes']) )
			if not te in exifFiles:
				exifFiles.append( te )
				if not 'f' in _.switches.value('Exif').lower():
					if 'n' in _.switches.value('Exif').lower():
						if not os.path.isfile( te ):
							_.pr( x )
						else:
							size = os.stat( te ).st_size
							if not size:
								_.pr( x )
					else:
						_.pr( x )
				else:
					if 'n' in _.switches.value('Exif').lower():
						if not os.path.isfile( te ):
							_.pr( te )
					else:
						_.pr( te )

	if not _.switches.isActive('Single'):
		exifFiles.append( 'C:\\exif\\1516473860.0_1499553772.json' )
		for k in dTwo.keys():
			for row in dTwo[k]:
				f = str(row['folder']) + _v.slash + str(row['file'])
				x = c.replace( 'MOD', str(row['mod']) ).replace( 'BYTES', str(row['bytes']) ).replace( 'THEFILE', f )
				te = e.replace( 'MOD', str(row['mod']) ).replace( 'BYTES', str(row['bytes']) )
				if not te in exifFiles:
					exifFiles.append( te )
					if not 'f' in _.switches.value('Exif').lower():
						if 'n' in _.switches.value('Exif').lower():
							if not os.path.isfile( te ):
								_.pr( x )
							else:
								size = os.stat( te ).st_size
								if not size:
									_.pr( x )
						else:
							_.pr( x )
					else:
						if 'n' in _.switches.value('Exif').lower():
							if not os.path.isfile( te ):
								_.pr( te )
						else:
							_.pr( te )

def csvExport():
	global dOne
	global dTwo

	c = '"FIELD",'
	e = '"FIELD"'

	for k in dOne.keys():
		for row in dOne[k]:
			r = ''
			r += c.replace( 'FIELD', row['size'] )
			r += c.replace( 'FIELD', row['title'] )
			r += c.replace( 'FIELD', row['file'] )
			r += c.replace( 'FIELD', row['franchise'] )
			r += c.replace( 'FIELD', row['folder'] )
			r += c.replace( 'FIELD', row['bytes'] )
			r += c.replace( 'FIELD', row['mod'] )
			r += e.replace( 'FIELD', row['imdbID'] )
			_.pr( r )

	# if not _.switches.isActive('Single'):

def action():
	global dOne
	global dTwo
	global ext

	fileTwo = []
	# _.pr( _.appData )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		fileOne = _.appData[__.appReg]['pipe']
		fieldSet( 'Single', 'active', True )
	else:
		if _.switches.isActive('Input'):
			one = _.switches.value('Input').split(',')[0]
			two = _.switches.value('Input').split(',')[1]
		elif _.switches.isActive('FileOne') and _.switches.isActive('FileTwo'):
			one = _.switches.value('FileOne')
			two = _.switches.value('FileTwo')
		else:
			_.pr('Error 0')
			sys.exit()
		try:
			fileOne = _.getText( one )
			fileTwo = _.getText( two )
		except Exception as e:
			_.pr('Error 1')
			sys.exit()

	listOne = []
	listTwo = []
	rawOne = []
	rawTwo = []
	dOne = {}
	dTwo = {}
	d = "{ 'franchise': r[0], 'title': r[1], 'folder': r[2], 'file': r[3], 'mod': r[4], 'bytes': r[5], 'size': r[6], 'imdbID': r[7], 'id': str(r[4])+'_'+str(r[5]) }"
	for row in fileOne:
		row = row.replace( '\n', '' )
		if __.theDelim in row:
			r = row.split( __.theDelim )
			if not r[1] in rawOne:
				listOne.append( { 'row': r[1], 'found': False } )
				rawOne.append( r[1] )
			documentFolders( r[2], 1 )
			documentExt( r[3] )
			data = eval( d )
			try:
				dOne[r[1]].append( data )
			except Exception as e:
				dOne[r[1]] = []
				dOne[r[1]].append( data )

	if not _.switches.isActive('Single'):
		for row in fileTwo:
			row = row.replace( '\n', '' )
			if __.theDelim in row:
				r = row.split( __.theDelim )
				if not r[1] in rawTwo:
					listTwo.append( { 'row': r[1], 'found': False } )
					rawTwo.append( r[1] )
				documentFolders( r[2], 2 )
				documentExt( r[3] )
				data = eval( d )
				try:
					dTwo[r[1]].append( data )
				except Exception as e:
					dTwo[r[1]] = []
					dTwo[r[1]].append( data )

		_.saveText( ext, _v.myTables + _v.slash+'movieExt.txt' )
		for r1i, row1 in enumerate(listOne):
			found = False
			for r2i, row2 in enumerate(listTwo):
				if row1['row'] == row2['row']:
					found = True
					listTwo[r2i]['found'] = True
			listOne[r1i]['found'] = found

		fileOneFalseCount = 0
		fileOneTrueCount = 0
		fileOneFalseList = []
		fileOneTrueList = []
		for i, row in enumerate(listOne):
			if not row['found']:
				fileOneFalseCount += 1
				fileOneFalseList.append( row['row'] )
			else:
				fileOneTrueList.append( row['row'] )
				fileOneTrueCount += 1
		fileTwoFalseCount = 0
		fileTwoTrueCount = 0
		fileTwoFalseList = []
		fileTwoTrueList = []
		for i, row in enumerate(listTwo):
			if not row['found']:
				fileTwoFalseCount += 1
				fileTwoFalseList.append( row['row'] )
			else:
				fileTwoTrueList.append( row['row'] )
				fileTwoTrueCount += 1


	if not _.switches.isActive('Single') and not _.switches.isActive('Exif') and not _.switches.isActive('CSV') and not _.switches.isActive('Test'):
		if not fileOneFalseCount and not fileTwoFalseCount:
			_.pr( 'Lists are a match' )
		else:
			if not fileOneFalseCount:
				_.pr( 'All items in one are in two' )
			else:
				if not _.switches.isActive('Report') or '1' in _.switches.value('Report') or 'one' in _.switches.value('Report').lower():
					if not _.switches.isActive('Report'):
						_.pr( 'Items in list 1 that are missing in list 2:' )
						_.pr()
					for i, row in enumerate(fileOneFalseList):
						if _.switches.isActive('NoCount'):
							_.pr( row )
						else:
							_.pr( i+1, row )
					if not _.switches.isActive('Report'):
						_.pr()
						_.pr()
						_.pr()
			if not fileTwoFalseCount:
				_.pr( 'All items in two are in one' )
			else:
				if not _.switches.isActive('Report') or '2' in _.switches.value('Report') or 'two' in _.switches.value('Report').lower():
					if not _.switches.isActive('Report'):
						_.pr( 'Items in list 2 that are missing in list 1:' )
						_.pr()
					for i, row in enumerate(fileTwoFalseList):
						if _.switches.isActive('NoCount'):
							_.pr( row )
						else:
							_.pr( i+1, row )
			if not _.switches.isActive('NoCount'):
				_.pr()
				_.pr( 'One:' )
				_.pr( '\tTotal:\t', fileOneTrueCount+fileOneFalseCount )
				# _.pr( '\tTrue:\t', fileOneTrueCount )
				_.pr( '\tFalse:\t', fileOneFalseCount )
				_.pr( '\t% T:\t', str(_.percentageDiffIntAuto( fileOneTrueCount+fileOneFalseCount, fileOneTrueCount))+'%' )
				_.pr( '\t% F:\t', str(_.percentageDiffIntAuto( fileOneTrueCount+fileOneFalseCount, fileOneFalseCount))+'%' )
				_.pr()
				_.pr( 'Two:' )
				_.pr( '\tTotal:\t', fileTwoTrueCount+fileTwoFalseCount )
				# _.pr( '\tTrue:\t', fileTwoTrueCount )
				_.pr( '\tFalse:\t', fileTwoFalseCount )
				_.pr( '\t% T:\t', str(_.percentageDiffIntAuto( fileTwoTrueCount+fileTwoFalseCount, fileTwoTrueCount))+'%' )
				_.pr( '\t% F:\t', str(_.percentageDiffIntAuto( fileTwoTrueCount+fileTwoFalseCount, fileTwoFalseCount))+'%' )

				_.pr()
				_.pr( 'Totals:' )
				_.pr( '\tRows:\t', fileTwoTrueCount+fileTwoFalseCount+fileOneTrueCount+fileOneFalseCount )
				_.pr()
				_.pr( '\tUnique:\t', fileTwoTrueCount+fileTwoFalseCount+fileOneFalseCount )
				_.pr( '\tTrue:\t', fileOneTrueCount )
				_.pr( '\tFalse:\t', fileTwoFalseCount+fileOneFalseCount )
				_.pr( '\t% T:\t', str(_.percentageDiffIntAuto( fileTwoTrueCount+fileTwoFalseCount+fileOneFalseCount, fileTwoTrueCount))+'%' )
				_.pr( '\t% F:\t', str(_.percentageDiffIntAuto( fileTwoTrueCount+fileTwoFalseCount+fileOneFalseCount, fileTwoFalseCount+fileOneFalseCount))+'%' )
		_.pr()
		_.pr()
		relevantFolders()
		# noFranchise()
		# words()
		# for data in fileOneTrueList:
		#     xRefTrue( data )
	if _.switches.isActive('Exif'):
		exif()
	if _.switches.isActive('CSV'):
		csvExport()
	if _.switches.isActive('Test'):
		test()
	
# { 'franchise': r[0], 'title': r[1], 'folder': r[2], 'file': r[3], 'mod': r[4], 'bytes': r[5], 'size': r[6], 'imdbID': r[7], 'id': str(r[4])+'_'+str(r[5]) }

def test():
	global dOne
	# t = '2005 Pride & Prejudice'
	# t = '2007-2010 Cranford'
	# t = '2007 Persuasion'
	# t = '2014 The Hundred-Foot Journey'
	# t = '2011 From Prada to Nada'
	# t = '2014 Love by the Book'
	# t = '2017 Logan'
	# t = '2010 Letters to Juliet'
	t = '2003 The Lord of the Rings: The Return of the King'
		# fix this type %tmpf1% | p line + 623492938

	data = []
	for record in dOne[ t ]:
		data.append( record['id'] )
		# _.pr( record['id']+'.json' )

	# sys.exit()
	_exif.setPipeData( data )
	records = _exif.identify()
	_.pr()
	i = 0
	for record in records:
		i += 1
		_.pr( record['keep'], record['id'],  )
	_.pr(i)



behavior = []
dOne = {}
dTwo = {}
fDataOne = {}
fDataTwo = {}
fDataOneTotal = 0
fDataTwoTotal = 0
relevantFoldersOne = []
relevantFoldersTwo = []
ext = []

exifJSON = {}

# crossRefMovies
########################################################################################
if __name__ == '__main__':
	action()