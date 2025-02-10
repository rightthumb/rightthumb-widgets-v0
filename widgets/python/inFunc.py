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
import _rightThumb._md5 as _md5




def appSwitches():
	__.specifications['ext'] = '.py'
	_.switches.register( 'Files', '-f,-i,-file,-files','file.txt', isRequired=False, description='Files' )
	# _.switches.register( 'Files', '-f,-i,-file,-files','file.txt', isRequired=True, description='Files' )
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Test', '-test')
	_.switches.register('Log', '-log')
	_.switches.register('Audit', '-audit')
	_.switches.register('JustReturn', '-return')
	_.switches.register('NoResults', '-no')
	_.switches.register('Clean', '--c')
	_.switches.register('Top', '-t,-top')
	



_.appInfo[focus()] = {
	'file': 'inFunc.py',
	'description': 'List functions and classes',
	'categories': [
						'research',
						'function',
						'app',
						'report',
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


_.appInfo[focus()]['relatedapps'].append('p fileRecover -i blank22 -audit')

_.appInfo[focus()]['examples'].append('p inFunc -f base --c -no + "][\'pipe\']"  | p LinesToList')
_.appInfo[focus()]['examples'].append('p inFunc -f inFunc.py + for table --c -no | p LinesToList')
_.appInfo[focus()]['examples'].append('p inFunc -i base')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p infunc -i dir.py + print - # "()" "\n" "\t"')
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

	_.switches.trigger('Files',_.myFileLocations)
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



# os.path.isfile(files)
# os.system('cls')

# #######################################


########################################################################################
# START
def getLines( start, end ):
	global ignoreLines
	global file

	payload = ''
	active = False

	for i,line in enumerate(file):
		ii=i+1
		if start == ii:
			active = True
		if active and ii not in ignoreLines:
			# payload += str(ii) +' '+ line.replace( '\r','' ).replace( '\n','' ) + '\n'
			payload += line.replace( '\r','' ).replace( '\n','' ) + '\n'
		if end == ii:
			return payload

def classPathAdd( s, n ):
	p = s.split(',')
	p.append( n )
	s = ','.join( p )
	s = _str.cleanBE( s, ',' )
	return s

def classPathRemove( s ):
	p = s.split(',')
	p.pop( len(p)-1 )
	s = ','.join( p )
	s = _str.cleanBE( s, ',' )
	return s

def classPathRepo( s, n ):
	s = classPathRemove( s )
	s = classPathAdd( s, n )
	return s

def fixEnd( end ):
	global ignoreLines
	# _.pr()
	# _.pr(end)
	while end in ignoreLines:
		end -= 1
		# _.pr(end)
	# _.pr(end)
	# sys.exit()
	# _.pr()
	return end
def closeLog():
	global log
	global data
	global ignoreLines
	_.saveTable( ignoreLines, 'ignoreLines.json', printThis=True )

	return ''
	for d in data:
		_.pr( d )

#####################################################
def isChar(theChar):
	result = True
	if theChar == ' ':
		result = 1
	if theChar == '\t':
		result = 4

	return result

def getPreSpacing(line):
	result = ''
	spacing = 0
	for theChar in line:
		theChar = str(theChar)
		charData = isChar(theChar)
		if not type(charData) == bool:
			spacing += charData
			result += theChar
		else:
			break

			
	return {'cnt': spacing, 'txt': result}

def firstInfo(i,line):
	global ignoreLines

	result = False
	data = False
	try:
		preData = getPreSpacing(line)
		clean = line.replace(preData['txt'],'')
		firstWord = clean.split(' ')[0]

		if firstWord.startswith('#'):
			isComment = True
		else:
			isComment = False

		if firstWord.lower() == 'def':
			isFunction = True
		else:
			isFunction = False

		if firstWord.lower() == 'class':
			isClass = True
		else:
			isClass = False

		result = { 'cnt': int(preData['cnt']/4), 'first': firstWord.lower(), 'isFunction': isFunction, 'isClass': isClass, 'data': data, 'isSolo': False }
		if '#' in result['first'] or len(result['first']) == 0:
			ignoreLines.append( i+1 )
		if isFunction:
			result['name'] = clean.split(' ')[1].split('(')[0]
			result['arg'] = line.split('(')[1].split(')')[0]
			
		if isClass:
			result['name'] = clean.split(' ')[1].replace(':','')


		if not isFunction and not isClass:
			result = False
			if not isComment:
				test = clean.replace(' ','').replace('\t','')
				if len(test) > 1:
					result = { 'cnt': int(preData['cnt']/4), 'first': firstWord.lower(), 'isFunction': isFunction, 'isClass': isClass, 'data': data, 'isSolo': True }
					if '#' in result['first'] or len(result['first']) == 0:
						ignoreLines.append( i+1 )

	except Exception as e:
		pass


	return result

def attemptClose(info):
	global data
	global process

	result = False

	for i,p in enumerate(process):
		if p['status'] and data[p['location']]['cnt'] >= info['cnt']:
			# _.pr(data[p['location']]['cnt'],info['cnt'])
			data[p['location']]['end'] = info['line']
			data[p['location']]['size'] = info['line'] - data[p['location']]['start']
			process[i]['status'] = False

def addSpace(cnt):
	result = ''
	i = 0
	while i < cnt*4:
		result += ' '
		i += 1
	return result



def action():
	global data
	global process
	global log
	global ignoreLines
	global file
	md5Data=[]
	classDef = {}
	table = { 'parents': {}, 'lines': {}, 'lp': {}, 'dat': {} }
	if _.switches.isActive('Audit'):
		i = _.switches.values('Files')[0]
		fileRecover = _.regImp( __.appReg, 'fileRecover' )
		fileRecover.switch( 'Audit' )
		fileRecover.switch( 'Audit',  )
		fileRecover.switch( 'Input', i )
		fileRecover.do( 'action' )
		# _.switches.dumpSwitches()
		# focus()
		# _.pr( focus() )
		# _.pr( __.appReg )
		sys.exit()
	if _.switches.isActive('Files'):
		xXx = {
				'classes': 0,
				'functions': 0,
				'all': 0,

		}
		# _.pr( _.switches.value('Input') )
		# sys.exit()
		# _.pr(_.switches.values('Files'))
		if not os.path.isfile( _.switches.values('Files')[0] ):
			# _.printBold( 'Error: File Not Found', 'red' )
			_.printBold( 'File Not Found', 'red' )
			sys.exit()
		modifiedRaw = os.path.getmtime(_.switches.values('Files')[0])
		file = _.getText(_.switches.values('Files')[0])
		if _.switches.isActive('Plus') or _.switches.isActive('Minus'):
			doSearch = True
		else:
			doSearch = False
		found = []

		for i,line in enumerate(file):
			if _.switches.isActive('Top'):
				if line.startswith(' ') or line.startswith('\t'):
					continue
			line = _.listColor( line, _.switches.values('Plus'), 'green' )
			line = line.replace('\n','')
			if doSearch:
				if _.showLine(line):
					found.append(i)
			info = firstInfo(i,line)
			if not type(info) == bool:
				log.append( info )
				info['line'] = i
				if info['isSolo']:
					if len(process) > 0:
						attemptClose(info)

				else:
					attemptClose(info)
					info['start'] = i+1
					info['end'] = 0
					process.append({ 'status': True, 'location': len(data), 'cnt': info['cnt'] })
					data.append(info)
					# _.pr(line)
		try:
			data[len(data)-1]['end']
		except Exception as e:
			_.pr(' No Functions ')
			return False
		if data[len(data)-1]['end'] == 0:
			data[len(data)-1]['end'] = len(file)
			data[len(data)-1]['size'] = len(file) - data[len(data)-1]['start']

		if _.switches.isActive('Test'):
			closeLog()

		
		if doSearch and len(found) > 0:
			for dat in data:
				what=''
				# _.pr( dat )
				table['dat'][dat['start']] = dat
				lastPrint = ''
				for i,row in enumerate(found):
					maxSpace = 0

					classDef[i] = ''
					if dat['start'] <= row and dat['end'] >= row:
						if dat['isClass']:
							classDef[i] = 'class'
							s = str(addSpace(dat['cnt']))+'class'+str(dat['name'])
							if not lastPrint == s:
								if not _.switches.isActive('JustReturn'):
									# _.pr(addSpace(dat['cnt']), _.inlineBold('class','magenta') ,dat['name'])
									parent = { 'space': addSpace(dat['cnt']), 'type': 'class', 'label': dat['name'], 'line': row+1 }
									table['parents'][dat['start']] = parent
							lastPrint = s
						else:
							classDef[i] = 'def'
							s = str(addSpace(dat['cnt']))+'def'+str(dat['name'])
							if not lastPrint == s:
								if not _.switches.isActive('JustReturn'):
									# _.pr(addSpace(dat['cnt']),_.inlineBold('def','yellow'),dat['name'])
									parent = { 'space': addSpace(dat['cnt']), 'type': 'def', 'label': dat['name'], 'line': row+1 }
									table['parents'][dat['start']] = parent
							lastPrint = s
				for i,row in enumerate(found):
					what='parent'
					maxSpace = 0
					if not classDef[i] == 'class':
						if dat['start'] <= row and dat['end'] >= row:
							maxSpace += dat['cnt']
							line = file[row].replace('\t','')
							line = _str.replaceDuplicate(line,' ')
							line = _str.cleanBE(line,' ')
							spc = getPreSpacing(line)
							line = line.replace(  '\n', '' )
							printLine = line.replace(spc['txt'],'')
							for search in _.switches.values('Plus'):
								printLine = printLine.replace( search, _.inlineBold( search, 'green' ) )
								what='line'

							if not classDef == 'class':
								rowX = str(row)
# listColor( text, rows, color='green' )

								
								# _.pr( 'listColor:', rowX )
								# for x in _.switches.values('Plus'):
								#     _.pr( 'x:', x )
								#     rowX = rowX.replace( str(x), _.colorThis( str(x), 'green', p=0 ) )
								for search in _.switches.values('Plus'):
									printLine = printLine.replace( search, _.inlineBold( search, 'green' ) )
								if not _.switches.isActive('JustReturn'):
									# _.pr( addSpace(maxSpace+1), _.inlineBold( str(int(rowX)+1) ), printLine )
									table['lines'][int(rowX)+1] = { 'parent': dat, 'space': addSpace(maxSpace+1), 'line': int(rowX)+1, 'text': printLine, 'what': what }
							# _.pr()
		elif not doSearch:
			md5Data = []
			lastCount = 0
			p = ''
			for dat in data:
				# _.pr( dat )
				dat['end'] = fixEnd(dat['end'])
				dat['size'] = dat['end'] - dat['start']
				# _.pr( dat )
				# _.pr()
				# sys.exit()
				if dat['isClass']:
					if _.switches.isActive('Log'):
						pre = 'class '
						n = pre+dat['name']
						if dat['cnt'] == 0:
							p = ''
							p = classPathAdd( p, n )
						else:
							if dat['cnt'] == lastCount:
								p = classPathRepo( p, n )
							elif dat['cnt'] > lastCount:
								p = classPathAdd( p, n )
							elif dat['cnt'] < lastCount:
								p = classPathRemove( p )
						lastCount = dat['cnt']
						records = getLines( dat['start'],(dat['end']) )
						try:
							md5=_md5.md5(records)
						except Exception as e:
							md5='err'
						md5Data.append({ 'path': p, 'name': dat['name'], 'md5': md5, 'epoch': modifiedRaw, 'start': dat['start'], 'end': dat['end'], 'size': dat['size'] })
					else:
						if not _.switches.isActive('JustReturn'):
							xXx['classes'] += 1
							xXx['all'] += 1
							_.pr( addSpace(dat['cnt']),'class',dat['name'] )

				else:
					if _.switches.isActive('Log'):
						pre = 'def '
						n = pre+dat['name']
						if dat['cnt'] == 0:
							p = ''
							p = classPathAdd( p, n )
						else:
							if dat['cnt'] == lastCount:
								p = classPathRepo( p, n )
							elif dat['cnt'] > lastCount:
								p = classPathAdd( p, n )
							elif dat['cnt'] < lastCount:
								p = classPathRemove( p )
						lastCount = dat['cnt']
						try:
							md5=_md5.md5(records)
						except Exception as e:
							md5='err'
						records = getLines( dat['start'],(dat['end']) )
						md5Data.append({ 'path': p, 'name': dat['name'], 'md5': md5, 'epoch': modifiedRaw, 'start': dat['start'], 'end': dat['end'], 'size': dat['size'] })
					else:
						if not _.switches.isActive('JustReturn'):
							xXx['functions'] += 1
							xXx['all'] += 1
							_.pr( addSpace(dat['cnt']),'def',dat['name'] )

			pass

			# _.pr()
			# _.pr()
			# for m in md5Data:
			#     _.pr( m )
			# _.pr()
			# _.pr()
			if _.switches.isActive('Log'):
				return saveLog( md5Data )
		# _.printVarSimple( data )
		pass
		if len( table['lines'].keys() ):
			table['children'] = {}
			for ln in table['lines']:
				table['children'][ table['lines'][ln]['parent']['start'] ] = {}
			for ln in table['lines']:
				table['children'][ table['lines'][ln]['parent']['start'] ][ln] = {}
			# _.pr()
			# _.pr()
			for lnp in table['parents']:
				recP = table['parents'][lnp]
				if recP['type'] == 'class':
					_.pr(recP['space'], _.inlineBold(recP['type'],'magenta') ,recP['label'])
					xXx['classes'] += 1
					xXx['all'] += 1
				else:
					xXx['functions'] += 1
					xXx['all'] += 1
					if _.switches.isActive('NoResults') and _.switches.isActive('Clean'):
						if recP['type'] == 'def':
							# _.pr(recP['space']+recP['label'])
							_.pr(recP['label'])
					else:
						_.pr(recP['space'], _.inlineBold(recP['type'],'yellow') ,_.pr(recP['label'],c='cyan',p=0))
				if lnp in table['children']:
					ch = list(table['children'][lnp].keys())
					for lnc in ch:
						recC = table['lines'][lnc]
						# _.pr( addSpace(maxSpace+1), _.inlineBold( str(int(rowX)+1) ), printLine )

						PrintAudit = False

						if _.switches.isActive('NoResults'):
							if recC['what'] == 'parent':
								if not _.switches.isActive('Clean'):
									if PrintAudit: _.pr('3333')
									_.pr(recC['space'], _.inlineBold(recC['line']) ,recC['text'])
								else:
									if PrintAudit: _.pr('2222')
									_.pr(recC['name'])
						else:
							if PrintAudit: _.pr('1111')
							_.pr(recC['space'], _.inlineBold(recC['line']) ,recC['text'])

		if not _.switches.isActive('Clean'):
			_.pr()
			# _.pr(xXx)
			_.printDicFields(xXx)
			_.pr()
			_.cp( _.switches.values('Files')[0], 'cyan' )
		return data
	pass

def saveLog( md5Data ):
	logFile = _v.generateFunctionLogFilename( _.switches.values('Files')[0] )
	auditLog = []
	# auditLog = _.getTable( logFile )
	if len( auditLog ) == 0:
		# _.pr( 'First Audit' )
		auditLog = {}
		for md in md5Data:
			idx = md['path']
			auditLog[idx] = {}
			auditLog[idx]['first'] = md['epoch']
			auditLog[idx]['last'] = md['epoch']
			auditLog[idx]['edits'] = 1
			auditLog[idx]['lastMD5'] = md['md5']
			auditLog[idx]['line'] = md['start']
			auditLog[idx]['start'] = md['start']
			auditLog[idx]['end'] = md['end']
			auditLog[idx]['records'] = []
			auditLog[idx]['records'].append( md )
	else:
		for md in md5Data:
			idx = md['path']
			try:
				exists = True
				auditLog[idx]['lastMD5']
			except Exception as e:
				exists = False

			if not exists:
				auditLog[idx] = {}
				auditLog[idx]['first'] = md['epoch']
				auditLog[idx]['last'] = md['epoch']
				auditLog[idx]['edits'] = 1
				auditLog[idx]['lastMD5'] = md['md5']
				auditLog[idx]['line'] = md['start']
				auditLog[idx]['start'] = md['start']
				auditLog[idx]['end'] = md['end']
				auditLog[idx]['records'] = []
				auditLog[idx]['records'].append( md )
			else:
				if not auditLog[idx]['lastMD5'] == md['md5']:
					shouldAdd = True
					for rec in auditLog[idx]['records']:
						if rec['md5'] == md['md5']:
							shouldAdd = False
					if shouldAdd:
						auditLog[idx]['edits'] += 1
						auditLog[idx]['records'].append( md )

						if md['epoch'] > auditLog[idx]['last']:
							auditLog[idx]['lastMD5'] = md['md5']
							auditLog[idx]['last'] = md['epoch']
							auditLog[idx]['line'] = md['start']
							auditLog[idx]['start'] = md['start']
							auditLog[idx]['end'] = md['end']

						if md['epoch'] < auditLog[idx]['first']:
							auditLog[idx]['first'] = md['epoch']
	# _.pr('log2:',logFile)
	_.saveTable( auditLog, logFile, printThis=False )
	return auditLog



backupLog = []
data = []
process = []
log = []
ignoreLines=[]



# listFunc
########################################################################################
if __name__ == '__main__':
	action()







