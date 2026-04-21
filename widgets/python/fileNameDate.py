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
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
##################################################

def appSwitches():
	pass
	_.switches.register('Input', '-i,-f,-file','file.txt *** NOT FILE TO RENAME ')
	_.switches.register('KeepSequence', '-n,-keepnumber')
	_.switches.register('Undo', '-undo','last')
	_.switches.register('Test', '-test','both')
	_.switches.register('Folder', '-folder')
	_.switches.register('Recursive', '-r,-recursive')
	_.switches.register('LogReport', '-log','sample')
	_.switches.register('Epoch', '-epoch', '1566853484.2928526')

	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'fileNameDate.py',
	'description': 'Rename files to include the modified date',
	'categories': [
						'DEFAULT'
				],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'dir /b *signaturemassageandfacialspa*.sql | p fileNameDate',
						'p fileNameDate + signaturemassageandfacialspa',
						'',
						'p fileNameDate + signaturemassageandfacialspa -test',
						'',
						'p fileNameDate -undo -folder -recursive ',
						'p fileNameDate -undo -folder -r ',
						'',
						''
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],

	}

_.appData[focus()] = {
	'start': __.startTime,
	'uuid': '',
	'audit': [],
	'pipe': False,
	'data': {
				'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
				'table': {'sent': [], 'received': [] }, 
	},
	}

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	
	_.defaultScriptTriggers()
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
########################################################################################
# START

def hasDate( data ):
	x = data.split( '_' )[0]
	l = len(x)
	c = x.count( '-', 0, len(x) )
	# _.pr(l, c)
	if l == 10 and c == 2 and data.startswith(x):
		return True
	else:
		return False


def addSuffix( baseName, suffix ):
	if type(suffix) == bool:
		return baseName
	oldBaseName = baseName
	dotSplit = baseName.split( '.' )
	dotSplit.reverse()
	noExt = baseName[:-(len(dotSplit[0])+1)]
	ext = dotSplit[0]
	baseName = noExt + suffix + '.' + ext
	return baseName

def new_name( data, info=False, theTime=False, skipSequence=False, addSequence=False, suffix=False ):
	global spent
	if type(info) == bool:
		info = _dir.fileInfo( data )
	if not theTime:
		d = info['date_modified'].split(' ')[0] + '_'
	else:
		d = info['date_modified'].replace( ' ', '_' ).replace( ':', '-' ) 
		if not addSequence:
			d += '-0'
	
	dataX = addSuffix( data, suffix )
	if not hasDate( data ):
		n = d + '_' + dataX
	else: 
		if '__' in data:
			pre = len( data.split('__')[0] ) + 2
		else:
			pre = len( data.split('_')[0] ) + 1
		x = data[pre:]
		data = x
		dataX = addSuffix( data, suffix )
		n = d + '_' + dataX
		
	if addSequence:
		for x in range(1,100000000):
			nw = d + '-' + str(x) + '_' + dataX
			if not os.path.isfile(nw):
				n = nw
				break
	if not _.switches.isActive( 'KeepSequence' ):
		if not skipSequence:
			if ').' in n:
				for x in range(0,1001):
					w = '(' + str(x) + ')'
					n = n.replace( ' '+w, '' )
					n = n.replace( w, '' )
	n = removeEndSpace( n, info )
	n = n.replace( ' ', '_' )
	data = dataX
	if os.path.isfile(n) or n in spent:
		if not theTime:
			n = new_name( data, info, theTime=True )
		elif not skipSequence:
			n = new_name( data, info, theTime=True, skipSequence=True )
		elif not addSequence:
			n = new_name( data, info, theTime=True, addSequence=True )
		else:
			n = data

	spent.append(n)
	return n

def findRecord_path_ID( path ):
	global data

	for i,record in enumerate(data):
		if path in record['path']:
			return i
	return False

def findRecord_name_ID( name ):
	global data

	for i,record in enumerate(data):
		if name in record['new']:
			return i
	return False
# signaturemassageandfacialspa.sql
def removeEndSpace( name, info ):
	eX = ( len(info['ext'])+1 )
	end = name[( ( eX+1 ) * -1):]
	endX = name[( ( eX ) * -1):]

	while end[0] == ' ':
		bX = len(name) - ( eX+1 )
		beginning = name[:(bX)]
		name = beginning + endX

		eX = ( len(info['ext'])+1 )
		end = name[( ( eX+1 ) * -1):]
		endX = name[( ( eX ) * -1):]

	while '  ' in name:
		name = name.replace( '  ', ' ' )

	return name
def testSequence( folder, name, ext, seq ):
	eX = ( len(ext)+1 )
	bX = len(name) - eX
	end = name[(eX * -1):]
	beginning = name[:(bX)]
	w = ' (' + str(seq) + ')'
	test = beginning + w + end
	if os.path.isfile( folder + _v.slash + test ):
		return False
	else:
		return test



def osSequence( path, name='signaturemassageandfacialspa.sql' ):
	info = _dir.fileInfo( path )
	# _.printVar( info )
	last = False
	success = False
	for x in range(1,1001):
		test = testSequence( info['folder'], name, info['ext'], x )
		if type( test ) == bool:
			current = True
		else:
			current = False
		if last and not current:
			success = test

		last = current

	if type( success ) == bool:
		return False
	else:
		return info['folder'] + _v.slash + success
	
def searchFolder( folder ):
	global theFiles
	# _.pr('here',folder)
	for file in os.listdir(folder):
		if _.showLine( file ):
			if os.path.isfile( file ):
				theFiles.append( __.path( folder + _v.slash + file ) )
		if _.switches.isActive( 'Recursive' ):
			if os.path.isdir( file ):
				# searchFolder( folder + _v.slash + file )
				try:
					searchFolder( folder + _v.slash + file )
					# _.pr( '   OK:', folder + _v.slash + file )
				except Exception as e:
					# _.pr( 'ERROR:', folder + _v.slash + file )
					pass

def action():
	global data
	global theFiles
	global epoch
	load()
	if _.switches.isActive( 'Undo' ) and _.switches.isActive( 'Epoch' ):
		if not len( _.switches.value( 'Epoch' ) ):
			_.pr( 'Error: Missing epoch' )
			sys.exit()

		epoch = float( _.switches.value( 'Epoch' ) )
		for i,record in enumerate(data):
			if epoch == record['epoch']:
				theFiles.append( record['path'][1] )


	elif _.switches.isActive( 'LogReport' ):

		sampleSize = 3

		records = {}
		epochs = []
		profiles = []
		for i,record in enumerate(data):
			if not record['epoch'] in epochs:
				epochs.append(record['epoch'])

		for epoch in epochs:
			records[epoch] = []

		for i,record in enumerate(data):
			records[record['epoch']].append( record )

		# _.printVar( records )

		for epoch in epochs:
			least = 99999
			base = ''
			for row in records[epoch]:
				c = row['folder'].count( _v.slash, 0, len(row['folder']) )
				if c < least:
					least = c
					base = row['folder']
					# _.pr( base )
			inAll = True
			isAll = True
			# _.pr( 'base:', base, least, c )
			for row in records[epoch]:
				if not base == row['folder']:
					isAll = False
				if not base in row['folder']:
					inAll = False
			if len(records[epoch]) == 1:
				profiles.append({ 'id': epoch, 'type': 'a file', 'description': str(len(records[epoch]))+'\tFile:\t'+records[record['epoch']][0]['new']  })
			elif not inAll and not isAll:
				profiles.append({ 'id': epoch, 'type': 'obscure', 'description': str(len(records[epoch]))+'\tMisc locations' })
			elif not isAll:
				profiles.append({ 'id': epoch, 'type': 'recursive', 'description': str(len(records[epoch]))+'\tFolders:\t'+base +' -recursive' })
			else:
				profiles.append({ 'id': epoch, 'type': 'folder', 'description': str(len(records[epoch]))+'\tFolder:\t'+base })

		logReport = _.switches.value( 'LogReport' )

		if 'sample' in logReport:
			for i,epoch in enumerate(epochs):
				sample = 0
				_.pr()
				_.pr()
				_.pr( epoch, profiles[i]['description'] )
				_.pr()
				for row in records[epoch]:
					if sample <= sampleSize:
						sample+=1
						_.pr( '\t', row['path'][0] )
			sys.exit()
		else:
		
			_.pr()
			_.pr( 'Rename Log:' )
			_.pr()
			for row in profiles:
				_.pr( '\t', row['id'], '\t', row['description'] )
			_.pr()



		# _.pr( epochs )


		sys.exit()
	elif _.switches.isActive( 'Undo' ) and 'l' in _.switches.value( 'Undo' ).lower():
		if not len(data):
			_.pr( 'No records' )
			sys.exit()
		
		theFiles = []
		epoch = data[len(data)-1]['epoch']
		for i,record in enumerate(data):
			if epoch == record['epoch']:
				theFiles.append( record['path'][1] )
		
	elif _.switches.isActive( 'Undo' ) and _.switches.isActive( 'Folder' ):
		# _.pr( 'HERE' )
		# sys.exit()
		theFiles = []
		folder = os.getcwd()
		
		for i,record in enumerate(data):
			if _.switches.isActive( 'Recursive' ):
				if folder in record['folder']:
					theFiles.append( record['path'][1] )
			else:
				if record['folder'] == folder:
					theFiles.append( record['path'][1] )
	else:
		if _.switches.isActive('Input'):
			path = _.switches.values('Input')[0]
			if os.path.isfile(path):
				_.setPipeData( _.getText( _.switches.value('Input') ), focus() )
			else:
				if type( _.appData[__.appReg]['pipe'] ) == bool:
					_.appData[__.appReg]['pipe'] = []
					for row in _.switches.value('Input').split( ',' ):
						_.appData[__.appReg]['pipe'].append( row )
		if not type( _.appData[__.appReg]['pipe'] ) == bool:
			_.pipeCleaner()
			theFiles = _.appData[__.appReg]['pipe']
		else:
			theFiles = []
			searchFolder( os.getcwd() )


	if len(theFiles):
		# _.pr( _.printVar(theFiles) )
		records = []


		# _.pr()
		# for i,row in enumerate( theFiles ):
		#     _.pr(row)
		# sys.exit()

		thisFolder = os.getcwd()
		thisFolder += _v.slash
		# _.pr(thisFolder)
		# sys.exit()
		for i,row in enumerate( theFiles ):
			# osSequence( row )
			if _.switches.isActive('Undo'):
				if os.path.isfile( row ):
					info = _dir.fileInfo( row )
					n = findRecord_name_ID( info['name'] )
					if not type(n) == bool:
						info['original'] = data[n]['original']
					else:
						info['original'] = ''


					theID = findRecord_path_ID( __.path( row ) )
					if type( theID ) == bool:
						pass
						# _.pr( 'Error:', row )
					
					else:
						if os.path.isfile( data[theID]['path'][0] ):
							oldSequence = osSequence( data[theID]['path'][0], data[theID]['original'] )
							if type( oldSequence ) == bool:
								pass
								# _.pr( 'Error:', row )
							else:
								try:
									os.rename( data[theID]['path'][1], oldSequence )
									status = True
								except Exception as e:
									status = False
								# _.pr( data[theID]['original'] )
								data.pop( theID )
								info['original'] = '('+ info['original'] +') '+ oldSequence
								if status:
									_.saveTable( data, 'fileNameDate_log.json', printThis=False )

						else:
							try:
								os.rename( data[theID]['path'][1], data[theID]['path'][0] )
								status = True
							except Exception as e:
								status = False
							# _.pr( data[theID]['original'] )
							data.pop( theID )
							if status:
								_.saveTable( data, 'fileNameDate_log.json', printThis=False )

					preX = ''
					preY = ''
					if not thisFolder == info['folder']+_v.slash and thisFolder in info['folder']:
						pre = info['folder'].replace( thisFolder, '' )
						preX = pre + _v.slash
					info['new_name'] = preY + preX + info['original']
					info['old_name'] = preY + preX + info['name']
					info['row'] = row
					records.append( info )
			else:
				if os.path.isfile( row ):
					info = _dir.fileInfo( row )
					n = findRecord_name_ID( info['name'] )
					if not type(n) == bool:
						info['original'] = data[n]['original']
					else:
						info['original'] = ''

					info['row'] = row
					records.append( info )

		records = _.tables.returnSorted( 'data', 'a.date_created_raw', records )
		if not _.switches.isActive('Undo'):
			for i,record in enumerate(records):
				records[i]['new_name'] = new_name( record['name'], record )
				record['new_name'] = records[i]['new_name']
				# _.pr( record['date_modified'] )

				if not _.switches.isActive( 'Test' ):
					log = { 'original': record['name'], 'new': record['new_name'] , 'folder': record['folder'] , 'path': [], 'epoch': epoch}
					log['path'].append( record['path'] )
					records[i]['new_name'] += log['new']

					preX = ''
					preY = ''
					if not thisFolder == record['folder']+_v.slash and thisFolder in record['folder']:
						pre = record['folder'].replace( thisFolder, '' )
						preX = pre + _v.slash
					records[i]['new_name'] = preY + preX + log['new']
					records[i]['old_name'] = preY + preX + log['original']
					
					try:
						os.rename( log['path'][0], record['folder'] +_v.slash+ log['new'] )
						status = True
					except Exception as e:
						status = False
					log['path'].append( __.path( record['folder'] +_v.slash+ log['new'] ) )
					# _.pr( log['original'] )
					if len( log['path']) == 2 and not log['path'][0] == log['path'][1]:
						data.append( log )
					if status:
						_.saveTable( data, 'fileNameDate_log.json', printThis=False )

		_.switches.fieldSet( 'Long', 'active', True )
		_.tables.register( 'data', records )
		if not _.switches.isActive( 'Test' ):
			_.tables.print( 'data', 'old_name,new_name' )
			_.pr()
			_.saveTable( data, 'fileNameDate_log.json' )
		else:
			_.tables.print( 'data', 'old_name,new_name,original' )



def load():
	global data
	data = _.getTable( 'fileNameDate_log.json' )
data = []
spent = []
theFiles = []
epoch = time.time()
########################################################################################
if __name__ == '__main__':
	action()