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
import platform
# import shutil

import time
from datetime import datetime as dt, timedelta
import datetime

from shutil import copyfile

from pathlib import Path

import subprocess as sp
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
import _rightThumb._md5 as _md5




def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Short', '-short')
	_.switches.register('ShowLast', '-last','10')
	_.switches.register('CleanLog', '-clean')
	_.switches.register('JustFiles', '-files,-bk,-backups')
	_.switches.register('Audit', '-audit')
	_.switches.register('FindGroup', '-fg,-fgroup,-findgroup')
	_.switches.register('DontResolveIDs', '-nores')
	# _.switches.register('DontShowTickets', '-nt,-noTickets')
	_.switches.register('ShowTickets', '-tickets,-showTickets')
	# _.switches.register('BackupFiles', '-bk')
	



_.appInfo[focus()] = {
	'file': 'fileRecover.py',
	'description': 'Recover automatically backed up text files',
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

_.appInfo[focus()]['relatedapps'].append('p fileBackup')
_.appInfo[focus()]['relatedapps'].append('p fileBackupLogFix')


_.appInfo[focus()]['examples'].append('p fileRecover -i %tmpf0%')
_.appInfo[focus()]['examples'].append('p fileRecover -last 20')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p fileRecover -i base')
_.appInfo[focus()]['examples'].append('p fileRecover -i base -backups')
_.appInfo[focus()]['examples'].append('p fileRecover -i base -backups | p f + "class " - # -n')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p fileRecover -i base -audit')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('echo. | p fileRecover -last 20| p resolveIDs')

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

	_.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()



def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# __.pipeData = list(data)
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in sys.stdin.readlines():
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



_.appData[__.appReg]['pipe'] = ''
if not sys.stdin.isatty():
	_.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	pipeCleaner()



########################################################################################
# START

# import fileBackup2
# fileBackup2.focus(focus())
# fileBackup2.registerSwitches()
# _.switches.fieldSet('Result','active',True)
# _.switches.fieldSet('ForceBackup','active',True)
# focus()

# import fileBackup
# focus()


def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y_%m_%d-%H_%M_%S')
	theDate = str(theDate)
	return theDate


def getTime(time):

	day = time // (24 * 3600)
	time = time % (24 * 3600)
	hour = time // 3600
	time %= 3600
	minutes = time // 60
	time %= 60
	seconds = time
	result = "d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds)
	return result


def generateID(path):
	abPath = os.path.abspath(path)
	md5 = _md5.md5File(abPath)
	return _md5.md52GUID(md5,True)

def idExist(theID, data):
	found = False
	for d in data:
		if d['id'] == theID:
			found = True
	return found

def timeDelta(timestamp):
	t1 = datetime.datetime.fromtimestamp(timestamp)
	t2 = datetime.datetime.fromtimestamp(time.time())
	delta = t2 - t1
	sec = delta.total_seconds()
	return sec

def searchFileForString(filepath,seachFor):
	result = False
	seachFor = seachFor.lower()
	if not os.path.isfile(filepath):
		return result

	file = _.getText(filepath)
	for line in file:
		line = line.lower()
		if seachFor in line:
			result = True
			return result


def dataSearch(data, row, searchAll=True):
	global hasSearched
	global originalData
	hasSearched = True

	seachFor = input('Seach: ')

	file = data[int(row)]['file']
	if searchAll:
		data = originalData
	dataFound = []
	for d in data:
		if d['file'] == file:
			if searchFileForString(d['backup'],seachFor):
				dataFound.append(d)

	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	_.pr()
	_.tables.register('dataFound',dataFound)
	_.tables.fieldProfileSet('dataFound','timestamp','trigger',_.float2Date3)
	_.tables.fieldProfileSet('dataFound','row,flag','alignment','center')
	_.tables.print('dataFound','row,name,flag,timestamp,age,version')
	_.pr()
	# _.pr( 'HERE', 4 )
	ask(dataFound)



# backup
# file
# id
# timestamp

# hasSearched = False
# originalData = []

def cleanSelection(string):
	string = string.lower()
	string = string.replace(' ','')
	newSelection = ''
	for c in str(string):
		if c.isalnum() or c == ',':
			newSelection += c
	string = newSelection
	return string

def helpMenu():
	_.pr()
	_.pr('\tHelp:')
	_.pr()
	_.pr('\t\ts - (s24) - search for a file with the same src path that contains a specific string')
	_.pr('\t\tp - (p5)  - open and print full path of backup file')
	_.pr('\t\to - (o3)  - open and print full path of backup file')
	_.pr('\t\tf - (f1)  - change the flag of an item')
	_.pr('\t\tt - (t5275)  - print path to ticket')
	_.pr('\t\tr - Recover the original file then exit')
	_.pr('\t\tbk - List all paths to the backup files (len > 2 to not include dates)')
	_.pr('\t\tnumber - type a number from the above list to recover')
	_.pr('\t\tthis - (this5)  - list all backups for selected file')
	# _.pr('\t\tg')
	_.pr('\t\tx - exit')
	_.pr()


def ask(data, doneselection=False, backupfile='', originalfile=''):
	# print('ask'); sys.exit()
	global originalFile
	global hasSearched

	

	if type(doneselection) == bool:
		selection = input('Make Selection: ')
	else:
		selection = doneselection


	selection = cleanSelection(selection)



	selection = selection.lower()
	if 'bk' in selection:
		global records
		global thePath
		# _.pv(records)
		_.pr()
		_.pr(thePath,c='darkcyan')
		_.pr()
		for rec in records:
			if len(selection) > 2:
				_.pr(rec['backup'],c='cyan')
			else:
				_.pr(_.friendlyDate(_.md(rec['backup'])),rec['backup'],c='cyan')
		_.isExit(__file__)
		_.pr()
		_.pr()
		return None
	if 'this' in selection:
		selection = selection.replace( 'this', '' )
		fxx = data[int(selection)]['file']
		if os.path.isfile( fxx ):
			_.switches.fieldSet( 'ShowLast', 'active', False )
			_.switches.fieldSet( 'Input', 'active', True )
			_.switches.fieldSet( 'Input', 'value', fxx )
			action()


	if 't' in selection:
		# _.pr( selection )
		se = selection.replace( 't', '' ).replace( ' ', '' )

		try:
			if ',' in se:
				xse = se.split( ',' )[0]
			else:
				xse = se
			tmp = int(xse)
			good = True
		except Exception as e:
			good = False

		if good:
			_.pr()
			for xse in se.split( ',' ):
				_.pr( xse, _v.ticketPath( xse ) )
			sys.exit()

	if ',' in selection:

		try:
			if ',' in selection:
				xse = selection.split( ',' )[0]
			else:
				xse = selection
			tmp = int(xse)
			good = True
		except Exception as e:
			good = False

		if good:
			_.pr()
			for xse in selection.split( ',' ):
				tp = _v.ticketPath( xse )
				if type( tp ) == bool:
					good = False
				else:
					_.pr( xse, tp )
			if good:
				sys.exit()



	if selection == '':
		selection = '?'
	else:
		pass
		if len(selection) > 6:
			_.pr()
			_.pr('Make input less than 6')
			_.pr()
			ask(data)

	if selection == '':
		selection = '?'

	if selection == 'x':
		sys.exit()

	if len( selection ) == 4:
		try:
			tmp = int( selection )
			good = True
		except Exception as e:
			good = False


		if good:
			_.pr()
			_.pr( selection, _v.ticketPath( selection ) )
			sys.exit()



	if 'g' in selection:
		_.switches.fieldSet( 'Input', 'active', False )
		_.switches.fieldSet( 'ShowLast', 'active', False )
		_.switches.fieldSet( 'FindGroup', 'active', True )
		_.switches.fieldSet( 'FindGroup', 'value', selection )
		action()



	if selection == 'r':
		if len(backupfile) > 0 and len(originalfile) > 0:
			# copyfile(backupfile, originalfile)
			# _.decompress2(backupfile, originalfile)
			copyfile(_v.stmp+os.sep+'fileRecover.cache', originalfile)
			_.decrypt( originalfile)
			_.pr('Reverted to original, for real')
			_.pr()
			_.pr('Reverted to original')
			_.pr()
		sys.exit()

	if 'f' in selection or 'flag' in selection:
		selection = selection.replace(' ','')
		selection = selection.replace('flag','')
		selection = selection.replace('f','')
		_.pr()
		
		flag = input('Change flag to?: ')
		backupLogY = cleanLog( printThis=False )
		try:
			fileY = data[int(selection)]['file']
			idY = data[int(selection)]['id']
			found = False

			for blyi,bly in enumerate(backupLogY):
				if not found and backupLogY[blyi]['file'] == fileY and backupLogY[blyi]['id'] == idY:
					found = blyi
			if not type(found) == bool:
				backupLogY[found]['flag'] = flag
			_.saveTable( backupLogY, 'fileBackup.json', printThis=True )
			# _.pr( 'HERE', 0 )
		except Exception as e:
			_.pr('Error on flag change')
		backupLogY = []
		sys.exit()

	if 'p' in selection or 'o' in selection:
		selection = selection.replace(' ','')
		selection = selection.replace('p','')
		selection = selection.replace('o','')
		if len(selection) == 0:
			helpMenu()
			ask(data)
		try:
			_.pr()
			_.pr(data[int(selection)]['backup'])
			_.pr()
			# sp.Popen([_v.sublime, data[int(selection)]['backup']])
			_file_open.action(data[int(selection)]['backup'])

		except Exception as e:
			selection = '?'

	if 's' in selection:
		selection = selection.replace(' ','')
		selection = selection.replace('s','')
		if len(selection) == 0:
			helpMenu()
			ask(data)
		try:
			isNumber = True
			data[int(selection)]['backup']
		except Exception as e:
			isNumber = False
			_.pr()
			_.pr('Error')
			_.pr(selection)
		if isNumber:
			if not hasSearched:
				dataSearch(data,selection)
			else:
				_.pr()
				_.pr('\tSearch this list or all')
				_.pr('\t0 - search this list')
				_.pr('\t1 - search all')
				searchWhat = input('Choose: ')

				if len(searchWhat) == 1 and ('0' in searchWhat or '1' in searchWhat):
					if searchWhat == '1':
						dataSearch(data, selection, True)
					else:
						dataSearch(data, selection, False)
				else:
					_.pr('Error')
					sys.exit()



	try:
		isNumber = True
		data[int(selection)]['backup']
	except Exception as e:
		selection = '?'
	
	if selection == '?':
		helpMenu()
		ask(data)

	if isNumber:

		if not os.path.isfile(data[int(selection)]['backup']):
			_.pr('\tBackup file does not exist')
			_.pr()
			_.pr('\trun: p fileBackupLogFix')
			sys.exit()
		else:
			modifiedRaw = os.path.getmtime(data[int(selection)]['file'])
			modified = formatDate(modifiedRaw)
			newname = _v.myTXT + _v.slash + str(time.time()) + '-' + modified +  '-' + Path(data[int(selection)]['file']).name
			# _.pr(data[int(selection)]['file'])
			backupLogX = _.getTable('fileBackup.json')
			bkID = generateID(data[int(selection)]['file'])
			log = { 'id': bkID, 'timestamp': time.time(), 'file': os.path.abspath(data[int(selection)]['file']), 'backup': newname }
			backupLogX.append(log)
			

			# _.pr(os.path.isfile(data[int(selection)]['backup']),data[int(selection)]['backup'])
			# _.pr(os.path.isfile(data[int(selection)]['file']),data[int(selection)]['file'])
			# sys.exit()
			if not type(originalFile) == str:
				logCheck = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )
				if bkID == logCheck[0]['id']:
					# _.pr()
					# _.pr('First in log')
					originalFile = logCheck[0]['backup']

				else:
					_.saveTable(backupLogX,'fileBackup.json',printThis=True)
					# _.pr( 'HERE', 1 )
					# cpResult = copyfile(data[int(selection)]['file'],newname)
					cpResult = _.decompress2(data[int(selection)]['file'],newname)
					originalFile = newname
			if _.isWin:
				try:
					# sp.Popen([   _v.sublime.replace('"','')   ,   data[int(selection)]['file'].replace('"','')  ])
					_file_open.action(data[int(selection)]['file'].replace('"',''))
					_.waiting(3)
				except Exception as e:
					_.pr([   _v.sublime.replace('"','')   ,   data[int(selection)]['file'].replace('"','')  ])
					_.pr('unable to open')
			# cpResult = copyfile(data[int(selection)]['backup'], data[int(selection)]['file'])
			cpResult = _.decompress2(data[int(selection)]['backup'], data[int(selection)]['file'])
			# copyfile(_v.stmp+os.sep+'fileRecover.cache', data[int(selection)]['file'])
			_.pr()
			_.pr('\tRecovered')
			_.pr()
			_.pr(data[int(selection)]['file'])
			_.pr()
			if _.isWin:
				try:
					# sp.Popen([   _v.sublime.replace('"','')   ,   data[int(selection)]['file'].replace('"','')  ])
					_file_open.action(data[int(selection)]['file'].replace('"',''))
				except Exception as e:
					_.pr([   _v.sublime.replace('"','')   ,   data[int(selection)]['file'].replace('"','')  ])
					_.pr('unable to open')
				# _.pr(cpResult)
				# _.pr(newname)
				
			ask(data, backupfile=data[int(selection)]['backup'], originalfile=data[int(selection)]['file'])



def cleanLog(printThis=True):
	backupLog = _.tables.returnSorted( 'backupLog', 'a.timestamp', _.getTable('fileBackup.json') )
	newLog = []
	for i,row in enumerate(backupLog):
		data = {
					'id':            backupLog[i]['id'],
					'file':            backupLog[i]['file'],
					'flag':            backupLog[i]['flag'],
					'backup':        backupLog[i]['backup'],
					'timestamp':     backupLog[i]['timestamp'],
					"version":         backupLog[i]['version'],
					"v":             backupLog[i]['v'],
					"v1":             backupLog[i]['v1'],
					"v2":             backupLog[i]['v2'],
					"v3":             backupLog[i]['v3']
		}

		try:
			if not type(backupLog[i]['flag']) == str:
				data['flag'] = ''
			else:
				data['flag'] = backupLog[i]['flag']
		except Exception as e:
			data['flag'] = ''

		newLog.append( data )
	_.saveTable( newLog, 'fileBackup.json', printThis=True )
	# _.pr( 'HERE', 2 )
	return newLog

thePath = ''

def action():
	global thePath
	global records
	records = []
	load()
	if _.switches.isActive('CleanLog'):
		cleanLog()
		sys.exit()
		


	global originalFile
	global originalData


	hasSearched = False
	originalData = []
	originalFile = False
	

	now = time.time()
	if _.switches.isActive('Input') or _.switches.isActive('ShowLast'):
		pass
	else:
		_.switches.fieldSet('ShowLast','active',True)
		_.switches.fieldSet('ShowLast','value','40')
	if _.switches.isActive('Input'):
		global originalFileContents
		copyfile(_.switches.value('Input'), _v.stmp+os.sep+'fileRecover.cache')
		_.decrypt( _v.stmp+os.sep+'fileRecover.cache')
	if _.switches.isActive('Input') or _.switches.isActive('ShowLast'):
		path = _.switches.value('Input')
		thePath = path
		
		if os.path.isfile(path) or _.switches.isActive('ShowLast'):
			if not _.switches.isActive('ShowLast'):
				abPath = os.path.abspath(path)
				theID = generateID(path)
			# _.pr()
			data = []
			justFile = []
			# _.tables.register('backupLog',backupLog)
			if _.switches.isActive('Audit'):
				backupLog = _.tables.returnSorted( 'backupLog', 'a.timestamp', _.getTable('fileBackup.json') )
			else:
				backupLog = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )
			if _.switches.isActive('FindGroup'):
				findGroup = _.switches.value('FindGroup').lower()
				findGroup = findGroup.replace( ' ', '' ).replace( '(', '' ).replace( ')', '' ).replace( 'g', '' )

			i = 0
			for ii,logItem in enumerate(backupLog):
				if _.switches.isActive('FindGroup'):
					try:
						logItem['flag']
					except Exception as e:
						logItem['flag'] = ''
					if '(GID)'.replace( 'ID', findGroup ) in logItem['flag']:
						logItem['name'] = Path(logItem['file']).name
						logItem['row'] = i
						logItem['age'] = getTime(timeDelta(logItem['timestamp']))
						logItem['ticket_open_at_time'] = getTicket( logItem['timestamp'] )
						data.append(logItem)
						records.append(logItem)

						if len( justFile ) == 0:
							if _.switches.isActive('Audit'):
								original = logItem['file']
							else:
								justFile.append( logItem['file'] )

						justFile.append( logItem['backup'] )

						i += 1

				elif not _.switches.isActive('ShowLast') and logItem['file'] == abPath and not theID == logItem['id']:
					logItem['name'] = Path(logItem['file']).name
					logItem['row'] = i
					logItem['age'] = getTime(timeDelta(logItem['timestamp']))
					logItem['ticket_open_at_time'] = getTicket( logItem['timestamp'] )
					data.append(logItem)
					if len( justFile ) == 0:
						if _.switches.isActive('Audit'):
							original = logItem['file']
						else:
							justFile.append( logItem['file'] )

					justFile.append( logItem['backup'] )


					i += 1
				elif _.switches.isActive('ShowLast'):
					if ii < int(_.switches.value('ShowLast')) +1:
						logItem['name'] = Path(logItem['file']).name
						logItem['row'] = i
						logItem['age'] = getTime(timeDelta(logItem['timestamp']))
						logItem['ticket_open_at_time'] = getTicket( logItem['timestamp'] )
						data.append(logItem)
						justFile.append( logItem['backup'] )
						i += 1
			if not len(data) > 0:
				_.pr('No backup')
			else:
				if not _.switches.isActive('Short'):
					_.switches.fieldSet('Long','active',True)
				_.switches.fieldSet('Sort','value','age')
				
				
				if _.switches.isActive('JustFiles'):
					for bkf in justFile:
						_.pr(bkf)
					_.isExit(__file__)
				if _.switches.isActive('Audit'):
					justFile.append( original )
					# global appDBA
					# appDBA = __.appReg
					# sys.exit()
					inFunc = _.regImp( __.appReg, 'inFunc' )
					inFunc.switch( 'Log' )
					inFunc.deleteSwitch( 'Audit' )
					
					for bkf in justFile:
						# _.pr()
						_.pr( bkf )
						inFunc.switch( 'Input', bkf )
						inFunc.imp.data = []
						inFunc.imp.process = []
						inFunc.imp.log = []
						inFunc.imp.ignoreLines=[]
						functionLogPath = inFunc.do( 'action' )
					_.pr()
					_.pr( 'Log:', functionLogPath )


				else:

					for i,rec in enumerate(data):
						records.append(rec)
						# for k in rec:
						#     _.pr(k, rec[k])
						# sys.exit()
						try:
							data[i]['size'] = _dir.info( rec['backup'] )['size']
						except:
							data[i]['size'] = '0B'
						if rec['name'] == '__init__.py':
							data[i]['name'] = initName( rec )

					if platform.system() == 'Windows':
						os.system('cls')
					else:
						os.system('clear')
					
					_.pr()
					_.pr( 'log: fileBackup.json' )
					_.pr()

					_.tables.register('data',data)
					_.tables.fieldProfileSet('data','timestamp','trigger',_.float2Date3)
					if not _.switches.isActive('DontResolveIDs'):
						_.tables.fieldProfileSet('data','name','trigger',_.resolveIDs)
					_.tables.fieldProfileSet('data','row,flag','alignment','center')
					_.tables.sort( 'data', 'd.timestamp' )
					_.tables.print('data','row,name,flag,timestamp,age,version,ticket_open_at_time,session,size')
					_.pr()
					# _.pr( 'HERE', 3 )


					originalData = data

					# print(type(_.appData[__.appReg]['pipe']))
					# _.pr(type(_.appData[__.appReg]['pipe']))
					if type(_.appData[__.appReg]['pipe']) == str or type(_.appData[__.appReg]['pipe']) == bool:
						ask(data)
	# backup
# file
# id
# timestamp

def initName( record ):
	file = record['file']
	file = file.replace( _v.myAppsPy, '' )
	fileX = file.split( _v.slash )
	# _.pr( fileX )
	# sys.exit()
	# return '__init__: ' + fileX[1] + '.' + fileX[2] 
	return '__init__: '  + fileX[2][1:].replace( 'base3', 'base' ).upper()
	
ShowTickets = '-showTickets'
def getTicket( epoch ):
	global ShowTickets
	if not _.switches.isActive('ShowTickets'):
		note = ShowTickets
		ShowTickets = ''
		return note
	global epochTickets
	result = ''
	for ticket in epochTickets:
		# _.pr( epoch, ticket['start'], ticket['end'] )
		# sys.exit()
		try:
			if float(epoch) > float(ticket['start']) and float(epoch) < float(ticket['end']):
				result += ticket['id'] + ','
		except Exception as e:
			pass
	result = _str.cleanBE( result, ',' )
	return result

def load():
	global epochTickets
	_bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )
	# _bkLog.do(  )
	_bkLog.imp.autoFileVersion()

	ticketTimeline = _.regImp( __.appReg, 'ticketTimeline' )
	# ticketTimeline.do(  )
	ticketTimeline.imp.action()
	epochTickets = _.getTable( 'ticketTimeline.json' )


import _rightThumb._dir as _dir

hasSearched = False
originalData = []
originalFile = False


# sp.Popen
_file_open = _.regImp( __.appReg, 'file-open' )
_file_open.switch('App',_v.meta['code_editor'])
# _file_open.switch('Clean')
# _file_open.switch('Files',path)
# _file_open.action()
# _file_open.action(path)

########################################################################################
if __name__ == '__main__':
	action()







