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
__.registeredApps.append( focus() )


import _rightThumb._base3 as _
_.load()

##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str



##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','one.txt:1-18 two.txt:1-18; one.txt LAST-BACKUP ', isRequired=True, description='Files' )
	_.switches.register( 'NoBreak', '-nb,-nobreak' )


	"""
	_.switches.documentation( 'Test', { 
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	"""


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'compareFiles.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Compare as many files as you want ',
	'categories': [
						'compare',
						'file',
						'xref',
						'tool',
						'research',
						'troubleshoot',
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
						'p compareFiles -f one.js one.js + items',
						'',
						'p compareFiles -f one.js:1-18 two.js:1-18 + date:',
						'',
						'p compareFiles -f one.js two.js LAST-BACKUP',
						'p compareFiles -f one.js LAST-BACKUP two.js LAST-BACKUP',
						'',
						'LAST-BACKUP gets the backup of the file before it ONLY',
						'',
						'',
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
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
	
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


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
########################################################################################
# START

def action():
	global data
	global backupFiles
	load()

	for i,record in enumerate(data):
		_.pr()
		_.pr()
		_.pr()
		
		if 'LAST-BACKUP'.lower() in record['file'].lower():
			delim = ' - '
			last_backup = _.caseUnspecific( data=record['file'], subject='LAST-BACKUP' )[0]
			last_backup_color = _.colorThis( [ 'LAST-BACKUP' ], 'red', p=0 )
			delim_color = _.colorThis( [ delim ], 'green', p=0 )
			newPrint = record['file']
			# _.pr()
			# _.pr()
			# _.pr()
			# _.pr(last_backup)
			# _.pr()
			# _.pr()
			# _.pr(  newPrint.split( last_backup+delim )  )
			theRest = _.colorThis( [ newPrint.split( last_backup+delim )[1] ], 'yellow', p=0 )

			newPrint = last_backup_color+delim_color+theRest
			_.pr(newPrint)
		else:
			_.colorThis( [ record['file'] ], 'yellow' )
		report = {}
		for ii,test in enumerate(data):
			if not i == ii:
				report[  test['file']  ] = []
		for ii,test in enumerate(data):
			first = False
			lastID = 0
			if not i == ii:
				for ir,row in enumerate(record['data']):
					if not row in test['data']:
						if not first:
							first = True
							_.pr()
							# _.pr()
							# _.pr()
							_.colorThis(  [ '\t', test['file'] ] , 'cyan' )
						if not lastID == ir-1:
							_.pr()
							_.pr()
						lastID = ir
						if not _.switches.isActive('NoBreak'):
							pre = '                     '
							iTxt = len(str(ir+1))
							prei = 0
							while not prei == iTxt:
								prei+=1
								pre += ' '
							non_break = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
							maxWidth = 200
							rowi = 0
							cntBase = len(pre)
							cnt = cntBase
							last_nb = None
							newText = []
							# newText.append('test   ')

							done = False
							while not done:

								try:
									row[rowi]
								except Exception as e:
									done = True

								if not done:
									newText.append(  row[rowi]  )
									if not row[rowi] in non_break:
										last_nb = rowi
									cnt+=1
									if cnt >= maxWidth:
										cnt=cntBase
										if last_nb is None or last_nb == rowi:
											newText.append('\n'+pre)
										else:
											newText.reverse()
											while not rowi == last_nb:
												rowi-=1
												newText.pop(0)
											newText.reverse()
											newText.append('\n'+pre)



								rowi+=1
							pass
							row = ''.join( newText )
						# _.pr( 'estimate:', estimate )
						p = _.colorThis( [ '\t\t', ir+1  ], 'purple', p=0 )+'\t'+_.plusColor( row )
						# _.colorThis( [ row ], 'bold', p=0 )
						_.pr(p)


	spent_sp = []
	if len( backupFiles ):
		_.pr()
		_.pr()
		_.colorThis( [ 'backup files:' ], 'green' )
		for record in backupFiles:
			_.pr()
			if not data[ record['i'] ]['start'] is None:
				spent_sp.append( record['i'] )
				scan_profile = scan_audit( record['i'] )
				sp = scan_profile
				part_profile = {
									'match': str(sp['match'])+'%',
									'start': sp['start'],
									'end': sp['end'],
									'lines': sp['lines'],
									'parent_lines': sp['pLines'],
				}
				_.colorThis( [ '\t', _.simpleDic(part_profile)  ], 'yellow' )
				_.colorThis( [ '\t', record['file'] ], 'cyan' )
			else:
				_.colorThis( [ '\t', record['file'] ], 'cyan' )
			_.pr()
	pass
	hasScans = False
	for i,record in enumerate(data):
		if record['scan'] and not i in spent_sp:
			hasScans = True
	if hasScans:
		_.pr()
		_.pr()
		_.colorThis( [ 'audit auto line matching:' ], 'green' )
	for i,record in enumerate(data):
		if record['scan'] and not i in spent_sp:
			_.pr()
			scan_profile = scan_audit( record['i'] )
			sp = scan_profile
			part_profile = {
								'match': str(sp['match'])+'%',
								'start': sp['start'],
								'end': sp['end'],
								'lines': sp['lines'],
								'parent_lines': sp['pLines'],
			}
			_.colorThis( [ '\t', _.simpleDic(part_profile)  ], 'yellow' )
			_.colorThis( [ '\t', record['file'] ], 'cyan' )
			_.pr()



def scan_audit( i ):
	global data
	start_p = data[ i-1 ]['start']
	end_p = data[ i-1 ]['end']

	start = data[ i ]['start']
	end = data[ i ]['end']



	xFirst = end_p-start_p
	xScan = end-start
	pFirst = _.percentageDiffIntAuto( xFirst, xScan )
	xDiff = 0
	if xFirst > xScan:
		xDiff = xFirst - xScan
	elif xFirst < xScan:
		xDiff = xScan - xFirst
	scan_profile = {

						'pStart': start_p,
						'pEnd': start_p,
						'pLines': xFirst,

						'start': start,
						'end': end,
						'lines': xScan,

						'diff': xDiff,
						'match': pFirst,
	}

	return scan_profile

	if False and pFirst < 90:
		_.pr()
		_.pr()
		_.pr( 'Scan Audit, Differences:' )
		_.pr( '\tfirst:', xFirst )
		_.pr( '\tscan:', xScan )
		_.pr()
		_.pr( '\tdiff:', xDiff )
		_.pr()
		_.pr( '\tper:', pFirst )
		_.pr()
		_.pr()


def load():
	global data
	global backupFiles
	for ifn,filename in enumerate(_.switches.values('Files')):
		start = None
		end = None
		ids = []
		test = []
		partial = False
		scan = False
		filelabel = filename.split(':')[0]
		isBackup = False
		start_p = None
		end_p = None
		shouldRun = False
		is_scan = False



		_.pr()
		if ':' in filename:
			shouldRun = True
		if filename.count(':') == 1 and filename[1] == ':':
			shouldRun = False
			filelabel = filename


		# _.pr('shouldRun',shouldRun)
		if shouldRun:


			if filename.count(':') == 2 and filename[1] == ':':
				part = []
				filelabelX = filename.split(':')
				filelabelX.reverse()
				xx = filelabelX[0]
				filelabelX.pop(0)
				filelabelX.reverse()
				filelabel = ':'.join(filelabelX)
				part.append( filelabel )
				part.append( xx )
				# _.pr( part )
			else:
				part = filename.split(':')
			partial = True
			filename = part[0]
			if 'scan' in part[1]:
				scan = True

		if 'LAST-BACKUP'.lower() in filename.lower():
			filelabel = 'LAST-BACKUP'
			backup = 0
			if '+' in filename:
				try:
					backup = int( filename.split('+')[1] )                
				except Exception as e:
					backup = '?'
			isBackup = True
			filename = _.lastBackup( _.switches.values('Files')[ifn-1].split(':')[0] , backup )
			backupFiles.append({ 'file': filename, 'i': ifn })
			if filename is None:
				_.pr( 'No Backup Found' )
				sys.exit()
			filelabel = filelabel + ' - ' + data[ifn-1]['file']
			if not data[ifn-1]['start'] is None:
				scan = True
		fileData = _.getText( filename )
		# _.pr( '\n\ngetText:', filename, type(fileData), '\n\n' )
		original = fileData


		# if filename.lower().endswith( ':scan' ):
		#     scan = True
		#     is_scan = True
			
		#     filelabelX = filename.split(':')
		#     filelabelX.reverse()
		#     filelabelX.pop(0)
		#     filelabelX.reverse()
		#     filelabel = ':'.join(filelabelX)
		#     filename = ':'.join(filelabelX)


		if scan:
			is_scan = True
			partial = True
			found = False
			# _.pr( '\n\n', data[ifn-1]['start'], '\n\n' )
			startScanA = data[ifn-1]['original'][  data[ifn-1]['start']-1  ]
			startScanB = data[ifn-1]['data'][  data[ifn-1]['start']-1  ]

			endScanA = data[ifn-1]['original'][  data[ifn-1]['end']-1  ]
			endScanB = data[ifn-1]['data'][  data[ifn-1]['end']-1  ]
			start_p = data[ifn-1]['start']
			end_p = data[ifn-1]['end']
			start = None
			end = None
			iSalt = 1
			for i,row in enumerate(fileData):
				isave = i + iSalt
				if start is None:
					if row == startScanA:
						start = isave
				elif end is None:
					if row == endScanA:
						end = isave
			if start is None:

				for i,row in enumerate(fileData):
					isave = i + iSalt
					if start is None:
						if row == startScanB:
							start = isave
					elif end is None:
						if row == endScanA:
							end = isave
				
				if start is None:

					for i,row in enumerate(fileData):
						isave = i + iSalt
						if start is None:
							if _.textClean(row) == startScanB:
								start = isave
						elif end is None:
							if _.textClean(row) == endScanB:
								end = isave

					if start is None:
						_.colorThis( ['startScanA', startScanA], 'cyan' )
						if not startScanB == startScanA:
							_.colorThis( ['startScanB', startScanB], 'cyan' )
						_.colorThis( [ '\tthe second document has been scanned and the above is missing ' ], 'yellow' )
						_.colorThis( 'auto line number search FAIL: 0', 'red' )
						sys.exit()
				elif end is None:
					start = None
					for i,row in enumerate(fileData):
						isave = i + iSalt
						if start is None:
							if row == startScanB:
								start = isave
						elif end is None:
							if row == endScanB:
								end = isave
			if not end_p is None and end_p == len(data[ifn-1]['data']):
				end = len(fileData)-1
			# if not end_p is None:
			#     _.pr( end_p, len(data[ifn-1]['data']) )
			if start is None or end is None:
				_.colorThis( ['endScanA', endScanA], 'cyan' )
				if not endScanA == endScanB:
					_.colorThis( ['endScanB', endScanB], 'cyan' )
				_.colorThis( [ '\tthe second document has been scanned and the above is missing ' ], 'yellow' )
				_.colorThis( 'auto line number search FAIL: 1', 'red' )
				sys.exit()
			if False and isBackup:
				_.pr()
				_.pr('start',start)
				_.pr('end',end)
				_.pr()
				_.pr( 'p diff', end_p-start_p )
				_.pr( 'diff', end-start )
				_.pr()
				_.pr(fileData[start-1])
				_.pr(fileData[end-1])
				_.pr()
				# sys.exit()

		if partial and not scan:
			# _.colorThis( '                                       HERE' )
			start = int(part[1].split('-')[0])
			if '-' in part[1]:
				end = int(part[1].split('-')[1])
			else:
				end = len(fileData)-1

		active = True
		first = False
		killOn = 5
		ikill = 0
		for i,row in enumerate(fileData):

			if partial:
				if i+1 < start:
					active = False
				elif i+1 > end:
					active = False
				else:
					active = True

			if active:
				if False and isBackup:
					_.pr( i, 'start', start, fileData[i] )
					ikill+=1
					if ikill == killOn:
						sys.exit()
				fileData[i] = _.textClean( row )
			else:
				fileData[i] = ''
				original[i] = ''

		pass
		if True and is_scan:
			xFirst = end_p-start_p
			xScan = end-start
			pFirst = _.percentageDiffIntAuto( xFirst, xScan )
			xDiff = 0
			if xFirst > xScan:
				xDiff = xFirst - xScan
			elif xFirst < xScan:
				xDiff = xScan - xFirst
			if pFirst < 90:
				_.pr()
				_.pr()
				_.pr( 'Scan Audit, Differences:' )
				_.pr( '\tfirst:', xFirst )
				_.pr( '\tscan:', xScan )
				_.pr()
				_.pr( '\tdiff:', xDiff )
				_.pr()
				_.pr( '\tper:', pFirst )
				_.pr()
				_.pr()
				pause = input( ' pause: ' )

		data.append({  'file': filelabel, 'data': fileData, 'partial': partial, 'start': start, 'end': end, 'original': original, 'scan': is_scan, 'i': ifn  })
		# for deli,record in enumerate(data):
		#     if deli <= ifn-2:
		#         del data[i]['original']
	pass
	for i,record in enumerate(data):
		del data[i]['original']


data = []
backupFiles = []
########################################################################################
if __name__ == '__main__':
	action()