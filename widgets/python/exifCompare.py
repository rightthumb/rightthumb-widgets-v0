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
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

##################################################

# from lxml import html
# import requests
# import cssselect

##################################################


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Folder', '-folder')
	



_.appInfo[focus()] = {
	'file': 'exifCompare.py',
	'description': 'Changes the world',
	'categories': [
						'research',
						'text manipulation',
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

_.appInfo[focus()]['relatedapps'].append('p jsonFieldsInFolder ?')
_.appInfo[focus()]['relatedapps'].append('p crossRefMovies ?')

_.appInfo[focus()]['examples'].append('p exifCompare -i C:\\exif\\1515521970.777321_3992730304.json C:\\exif\\1515523707.3214042_548566997.json')

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
	# _.appData[__.appReg]['pipe'] = list(data)
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




_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )
	# _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



########################################################################################

########################################################################################
# START

def f( field ):
	global cData
	try:
		result = cData[field]
	except Exception as e:
		result = 0
	return result

def vote( data ):
	global cData

	h = 0
	w = 0
	m = 0
	a = 0


	for exif in data:
		cData = exif['exif'][0]
		ih = f('ImageHeight')
		iw = f('ImageWidth')
		im = f('Megapixels')
		ia = f('AudioChannels')

		if ih > h:
			h = ih
		if iw > w:
			w = iw
		if im > m:
			m = im
		if ia > a:
			a = ia
	maxVote = 0
	for i,exif in enumerate(data):
		cData = exif['exif'][0]
		ih = f('ImageHeight')
		iw = f('ImageWidth')
		im = f('Megapixels')
		ia = f('AudioChannels')

		vote = 0

		if ih == h:
			vote += 1
		if iw == w:
			vote += 1
		if im == m:
			vote += 1
		if ia == a:
			vote += 1
		if vote > maxVote:
			maxVote = vote
		data[i]['vote'] = vote
		
	for i,exif in enumerate(data):
		if data[i]['vote'] == maxVote:
			return data[i]

def t2d( data ):
	if str(data) == '0':
		result = 0
	else:
		result = str(data)
		result = result.replace( '.', ':' )
		result = result + ':0'
	# _.pr( result )
	return result

def durationNumber( data ):
	if str(data) == '0':
		return 0
	
	dTime = data.split(':')

	h = ( dTime[0] )
	m = ( dTime[1] )
	s = ( dTime[2] )
	data = float( h + '.' + m )
	return data

def movieDuration( data ):
	if str(data) == '0':
		return 'Error'
	
	dTime = data.split(':')

	h = ( dTime[0] )
	m = ( dTime[1] )
	s = ( dTime[2] )
	data = float( h + '.' + m )

	if data <= 0.05 and data >= 0.001:
		result = 'Micro'
	elif data <= 0.17 and data >= 0.05:
		result = 'Clip'
	elif data <= 0.30 and data >= 0.17:
		result = '30ish'
	elif data <= 1.17 and data >= .30:
		result = '1HRish'
	elif data <= 1.45 and data >= 1.17:
		result = '1.5HRish'
	elif data <= 2.17 and data >= 1.45:
		result = '2HRish'
	elif data <= 2.45 and data >= 2.17:
		result = '2.5HRish'
	elif data <= 3.17 and data >= 2.45:
		result = '3HRish'
	elif data <= 3.45 and data >= 3.17:
		result = '3.5HRish'
	elif data <= 4.45 and data >= 3.45:
		result = 'LONG'
	elif data >= 4.45:
		result = 'TOO_LONG'
	return result

def movieQuality( data ):
	result = 'Error'
	if data <= 0.09 and data >= 0.001:
		result = 'Pitiful'
	elif data <= 0.225 and data >= 0.09:
		result = 'Low'
	elif data <= 1 and data >= 0.225:
		result = 'Medium'
	elif data <= 1.9 and data >= 1:
		result = 'High'
	elif data <= 3 and data >= 2:
		result = 'Amazing'
	elif data >= 3:
		result = 'Epic'
	return result

def movieType( data ):
	result = 'Error'
	if data <= 300 and data >= 1:
		result = 'Phone'
	elif data <= 800 and data >= 300:
		result = 'Mobile'
	elif data > 720:
		result = 'Standard'
	return result

def setIndicatorTest( file ):
	s = _str.stripNonAlphaNumaric( file )
	s = ' ' + s + ' '
	result = False
	for i,x in enumerate(__.setIndicators):
		for xx in (x):
			if xx in s.lower():
				# _.pr(xx)
				result = i
	return result

def typeScore( data ):
	if data == 'Phone':
		result = 1
	elif data == 'Mobile':
		result = 2
	elif data == 'Standard':
		result = 3
	return result

def qualityScore( data ):
	if data == 'Pitiful':
		result = 1
	elif data == 'Low':
		result = 2
	elif data == 'Medium':
		result = 3
	elif data == 'High':
		result = 4
	elif data == 'Amazing':
		result = 5
	elif data == 'Epic':
		result = 6
	return result

def durationScore( data ):
	if data == 'Micro':
		result = 1
	elif data == 'Clip':
		result = 2
	elif data == '30ish':
		result = 3
	elif data == '1HRish':
		result = 4
	elif data == '1.5HRish':
		result = 5
	elif data == '2HRish':
		result = 6
	elif data == '2.5HRish':
		result = 7
	elif data == '3HRish':
		result = 8
	elif data == '3.5HRish':
		result = 9
	elif data == 'LONG':
		result = 10
	elif data == 'TOO_LONG':
		result = 11
	return result

def action():
	global cData


	shouldRun = False
	if _.switches.isActive('Folder'):
		shouldRun = True
		folder = os.getcwd()
		files = os.listdir(folder)
		
	if _.switches.isActive('Input'):
		shouldRun = True
		files = _.switches.value('Input').split(',')

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		shouldRun = True
		files = _.appData[__.appReg]['pipe']
	if shouldRun:
		data = []
		for i,file in enumerate(files):
			if file.endswith('.json'):
				size = os.stat( file ).st_size
				if size:
					file = file.lower()
					c = file.replace( __.exif_Folder, '' ).replace( '.json', '' )
					s = c.split('_')
					info = {
								'mod': float(s[0]),
								'bytes': int(s[1]),
					}
					data.append( { 'vote': 0, 'exif': _.getTable2( file ), 'info': info } )

		for exif in data:
			cData = exif['exif'][0]
			# _.pr( f('ImageHeight'), f('ImageWidth') , f('Megapixels'), f('AudioChannels') )
			_.pr( f('ImageHeight') )

		bestVideo = vote( data )
		cData = bestVideo['exif'][0]
		# _.pr( 'Best:', bestVideo['info'], f('ImageHeight'), f('ImageWidth') , f('Megapixels'), f('AudioChannels') )

def identify():
	global cData
	data = []
	groups = {}
	hasGroup = 0
	for i,mID in enumerate(_.appData[__.appReg]['pipe']):
		file = __.exif_Folder + mID + '.json'
		size = os.stat( file ).st_size
		error = False
		if not size:
			error = True
		record = { 
					'id': mID,
					'vote': 0,
					'exif': False,
					'isfile': os.path.isfile( file ),
					'file': file,
					'groupid': False,
					'time': 0,
					'grouptime': 0,
					'groupcnt': 0,
					'keep': False,
					'error': error,
		}
		if not record['isfile']:
			record['error'] = True
		if not record['isfile'] or record['error']:
			_.pr( 'Error:', file )
		if record['isfile'] and not record['error']:
			record['exif'] = _.getTable2( file )
			cData = record['exif'][0]
			
			record['set'] = setIndicatorTest( f('FileName') )
			record['type'] = movieType( f('ImageHeight') )
			record['quality'] = movieQuality( f('Megapixels') )
			record['duration'] = movieDuration( f('Duration') )
			record['time'] = durationNumber( f('Duration') )

			if not type( record['set'] ) == bool:
				hasGroup += 1
				record['groupid'] = str(record['set']) +'_'+ str(record['type']) +'_'+ str(record['quality']) +'_'+ f('FileTypeExtension') #+'_'+ record['duration']
				try:
					groups[ record['groupid'] ] += 1
				except Exception as e:
					groups[ record['groupid'] ] = 1
		# _.pr( record['groupid'], record['type'], f('ImageHeight'), record['duration'] )
		data.append( record )
		# _.pr( f('FileName') )

	if hasGroup > 1:
		g = 0
		theGroups = {}
		theGroupVote = {}
		for gp in groups.keys():
			single = False
			if groups[gp] == 1:
				single = True
			else:
				g += 1
			cnt = 0
			groupTime = 0
			for i,record in enumerate(data):
				if record['groupid'] == gp:
					cData = record['exif'][0]
					if single:
						data[i]['groupid'] = False
						data[i]['set'] = False
					else:
						groupTime += record['time']
						cnt += 1
			for i,record in enumerate(data):
				if record['groupid'] == gp:
					if not single:
						data[i]['grouptime'] = groupTime
						data[i]['groupcnt'] = cnt
			ran = False
			for i,record in enumerate(data):
				if record['groupid'] == gp:
					try:
						theGroups[record['groupcnt']].append( record )
					except Exception as e:
						theGroups[record['groupcnt']] = []
						theGroups[record['groupcnt']].append( record )

		for record in data:
			cData = record['exif'][0]
			_.pr( record['groupid'], record['type'], f('ImageHeight'), record['duration'], record['grouptime'], movieDuration( t2d( record['grouptime'] ) ), record['time'] )

		_.pr()
		_.pr( 'Group Winners:' )
		keepGID = []
		keepID = []
		for gp in theGroups.keys():
			theGroupVote[record['groupcnt']] = vote(theGroups[gp])
			keepGID.append( theGroupVote[record['groupcnt']]['groupid'] )
			_.pr( theGroupVote[record['groupcnt']]['groupid'] )

		_.pr()
		_.pr( 'Non-Group Winner:' )
		cnt = 0
		noGroup = {}
		noGroupVote = {}
		for record in data:
			if type( record['groupid'] ) == bool:
				cnt += 1
				t = record['type']
				if t == 'Phone':
					t = 'Mobile'
				try:
					noGroup[t].append( record )
				except Exception as e:
					noGroup[t] = []
					noGroup[t].append( record )
				
		if cnt:
			for gp in noGroup.keys():
				noGroupVote[gp] = vote(noGroup[gp])
				cData = noGroupVote[gp]['exif'][0]
				_.pr( gp )
				_.pr( noGroupVote[gp]['type'], f('ImageHeight'), noGroupVote[gp]['duration'] )
				keepID.append( noGroupVote[gp]['id'] )
			
		for i,record in enumerate(data):
			data[i]['exif'] = False
			if record['id'] in keepID:
				data[i]['keep'] = True
			if record['groupid'] in keepGID:
				data[i]['keep'] = True
		return data

	else:
		keepID = []
		cnt = 0
		noGroup = {}
		noGroupVote = {}
		for record in data:
			if type( record['groupid'] ) == bool:
				cnt += 1
				t = record['type']
				# if t == 'Phone':
				#     t = 'Mobile'
				try:
					noGroup[t].append( record )
				except Exception as e:
					noGroup[t] = []
					noGroup[t].append( record )
				
		if cnt:
			for gp in noGroup.keys():
				noGroupVote[gp] = vote(noGroup[gp])
				cData = noGroupVote[gp]['exif'][0]
				_.pr( gp )
				_.pr( noGroupVote[gp]['type'], f('ImageHeight'), noGroupVote[gp]['duration'] )
				keepID.append( noGroupVote[gp]['id'] )
			
		for i,record in enumerate(data):
			data[i]['exif'] = False
			if record['id'] in keepID:
				data[i]['keep'] = True
		return data




# durationScore( data )
# qualityScore( data )
# typeScore( data )



# FileType
# VideoFrameRate

# ImageWidth
# ImageHeight

# DisplayWidth
# DisplayHeight

# AudioCodecID
# AudioSampleRate
# AudioChannels
# TrackType
# Megapixels

# Duration

__.setIndicators = [
[" i ", " ii ", " iii ", " iv ", " v ", " vi ", " vii ", " viii ", " ix ", " x ", " xi ", " xii " ],
[" e1 ", " e2 ", " e3 ", " e4 ", " e5 ", " e6 ", " e7 ", " e8 ", " e9 ", " e01 ", " e02 ", " e03 ", " e04 ", " e05 ", " e06 ", " e07 ", " e08 ", " e09 ", " e10 ", " e11 ", " e12 ", " e13 ", " e14 ", " e15 ", " e16 ", " e17 ", " e18 ", " e19 ", " e20 ", " e21 ", " e22 ", " e23 ", " e24 ", " e25 ", " e26 ", " e27 ", " e28 ", " e29 ", " e30 "],
[" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 01 ", " 02 ", " 03 ", " 04 ", " 05 ", " 06 ", " 07 ", " 08 ", " 09 ", " 10 ", " 11 ", " 12 ", " 13 ", " 14 ", " 15 ", " 16 ", " 17 ", " 18 ", " 19 ", " 20 ", " 21 ", " 22 ", " 23 ", " 24 ", " 25 ", " 26 ", " 27 ", " 28 ", " 29 ", " 30 "],
[" cd1 ", " cd2 ", " cd3 ", " cd4 ", " cd5 ", " cd6 ", " cd7 ", " cd8 ", " cd9 ", " cd01 ", " cd02 ", " cd03 ", " cd04 ", " cd05 ", " cd06 ", " cd07 ", " cd08 ", " cd09 ", " cd10 ", " cd11 ", " cd12 ", " cd13 ", " cd14 ", " cd15 ", " cd16 ", " cd17 ", " cd18 ", " cd19 ", " cd20 ", " cd21 ", " cd22 ", " cd23 ", " cd24 ", " cd25 ", " cd26 ", " cd27 ", " cd28 ", " cd29 ", " cd30 "],
[" chapter "],
[" part "],
[" pt1 ", " pt2 ", " pt3 ", " pt4 ", " pt5 ", " pt6 ", " pt7 ", " pt8 ", " pt9 ", " pt01 ", " pt02 ", " pt03 ", " pt04 ", " pt05 ", " pt06 ", " pt07 ", " pt08 ", " pt09 ", " pt10 ", " pt11 ", " pt12 ", " pt13 ", " pt14 ", " pt15 ", " pt16 ", " pt17 ", " pt18 ", " pt19 ", " pt20 ", " pt21 ", " pt22 ", " pt23 ", " pt24 ", " pt25 ", " pt26 ", " pt27 ", " pt28 ", " pt29 ", " pt30 "],
]
cData = {}
__.exif_Folder = 'c:\\exif'+_v.slash
# errorLog = _.getTable('Exif_Errors.json')


# exifCompare
########################################################################################
if __name__ == '__main__':
	action()