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
import simplejson as json
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

import re
# from lxml import html
# import requests
# import cssselect

##################################################


def appSwitches():
	_.switches.register('Count', '-c,-count')
	_.switches.register('NoCount', '--c,--count')
	_.switches.register('JustCount', '-jc,++c,++count')
	_.switches.register('Parse', '-p,-parse')
	_.switches.register('Parse2', '-p2')
	_.switches.register('ParseClean', '-pc')
	_.switches.register('Alpha', '-a,-alpha')
	_.switches.register('Word', '-w,-word')
	_.switches.register('Progress', '-progress')
	_.switches.register('Make', '-m,-make')
	_.switches.register('Substitute', '-sub,-substitute')
	_.switches.register('Unique', '-u,-unique')
	_.switches.register('Character', '-char,-Character')
	_.switches.register('LineNumber', '-ln,-line,-linenumber')
	_.switches.register('CrossReference', '-x,-cross','file.txt \\ 3, (0-4)')
	_.switches.register('CrossReferenceReverse', '-xr','')
	_.switches.register('CrossReferenceUltimate', '-xu,-xl','file.txt \\ 3, (0-4)')
	_.switches.register('CrossReferenceIntelligent', '-xi','build')
	_.switches.register('CrossReferenceSaveTables', '-xs','')
	_.switches.register('Clean', '-clean','')
	_.switches.register('Quote', '-q,-quote','')
	_.switches.register('NoClean', '-noclean','')
	_.switches.register('NoSpaceClean', '-nospaceclean','')
	_.switches.register('xReplace', '-xreplace','')
	_.switches.register('FixChar', '-fixchar','')
	_.switches.register('Precsv2json', '-precsv2json','')
	_.switches.register('Postcsv2json', '-postcsv2json','')
	_.switches.register('Test', '-test','')
	_.switches.register('x92', '-x92','')
	_.switches.register('Strict', '-strict','')
	_.switches.register('FixCSV', '-fixcsv','')
	_.switches.register('Upper', '-upper','')
	_.switches.register('Lower', '-lower','')
	_.switches.register('EndsWith', '-ew','')
	_.switches.register('CountDiv', '-div','')
	_.switches.register('Original', '-original','')
	_.switches.register('Blanks', '-blanks','')
	



_.appInfo[focus()] = {
	'file': 'line3.py',
	'description': 'Manipulate data',
	'categories': [
						'research',
						'text manipulation',
						'manipulate',
						'manipulation',
						'pipe',
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


_.appInfo[focus()]['examples'].append('dd | p line -p \\ 1')
_.appInfo[focus()]['examples'].append('dd | p line -p \\ e 2')
_.appInfo[focus()]['examples'].append('dd | p line -p \\ "1;2;3"')
_.appInfo[focus()]['examples'].append('p f -papa + \\GLENNALLEN\\ \\AppData\\ - \\Local\\ . | p line --c -p \\ 5 > ~dup.txt')
_.appInfo[focus()]['examples'].append('p f -dad + papa .jpg - 983db650f7f | p line --c -p \\ ee > "~dup.txt"')
_.appInfo[focus()]['examples'].append('p f -pub + papa .jpg - 983db650f7f79bc8 | p line --c -p \\ ee > "~dup.txt"')
_.appInfo[focus()]['examples'].append('type %f1% | p line -x %f2% \\ 3')
_.appInfo[focus()]['examples'].append('type %f1% | p line -x %f2% \\ 3 -xr')
_.appInfo[focus()]['examples'].append('type %f1% | p line -xu %f2% \\ 5 - joomla')
_.appInfo[focus()]['examples'].append('p file + test --c | p line -make "move {}  C:\\tech\\hosts\\MSI\\programs\\python\\" | p execute')
_.appInfo[focus()]['examples'].append('p file + transaction  --c | p line --c -make "move {}  C:\\tech\\hosts\\MSI\\programs\\python\\" | p execute')
_.appInfo[focus()]['examples'].append('p file + bm- | p f + { -jn | p line --c -make "xcopy /d/y {} Default(bookmarks)\\" | p execute')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('type techfolder.txt | p line -xu temp_e.txt \\ -xi build')
_.appInfo[focus()]['examples'].append('type file0.txt | p line -xu file1.txt \\  5')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('t v | p line + piller | p line --c -p " " 1 | p line --c -make "t c {} 2018.04.12" | p execute')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('type IronMan4.ino | p line -nospaceclean -noclean -p // 0 > tmp.txt')
_.appInfo[focus()]['examples'].append('type Adafruit_NeoPixel.cpp  | p line + ( { - " if" " while" " for" " print" #')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('type data.adj | p line -p " " 4 [pipe] 1')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('type %tmpf0% | p line --c -make ";\'¶¶¶¶BaaseTabel: {}¶¶;\' & RelationInfo(;\'LINAC_ENG;\';;\'{};\')&"')

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




_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )





######################################################################################## ######################################################################################## ######################################################################################## 
######################################################################################## ######################################################################################## ######################################################################################## 
######################################################################################## ######################################################################################## ######################################################################################## 
# START


def countThisLine(line):
	omitList = _.switches.value('Omit')
	# _.pr('"' + omitList +)
	result = True
	lineOriginal = line
	line = line.replace('Python','')
	line = line.replace('3.6.2','')
	line = _str.replaceAll(line,'_','')
	if _.switches.isActive('NoSpaceClean') == False:
		line = _str.replaceAll(line,' ','')
	line = _str.replaceAll(line,'\n','')
	line = _str.replaceAll(line,'\r','')
	# pattern = re.compile('([^\s\w]|_)+')
	# line = pattern.sub('', line)
	minLength = 1
	if _.switches.isActive('Strict') == True:
		minLength = 2
	if len(line) < minLength:
		result = False
	elif _.showLine(lineOriginal) == False:
		result = False

	return result

def displayLine(line):
	# _.pr(line)
	line = line.replace('\n','')
	if _.switches.isActive('Parse') == True:
		parse = _.switches.value('Parse2')
		p = parse.split(',')
		# p = list(parse)
		# _.pr(p)
		# sys.exit()
		p[0] =  _.ci(str(p[0]))
		p[1] =  _.ci(str(p[1]))


		try:
			p1 = str(p[1])
		except Exception as e:
			p1 = ''

		if p1.count(';mdt') > 0:
			linePart = ''
			# _.pr(line.count('.'))
			found = False
			for lx in line.split(p[0]):
				linePart += lx + p[0]
				if lx.count('.') == 2 and len(lx) == 10 and lx.startswith('20'):
					found = True
					break
			
			if found:
				line = linePart +  p[0]
			else:
				line = ''


		elif p1.count('ee') > 0:
			line2 = line.split(str(p[0]))
			extraEnd = '{7DE8F0C5-C37C-99E7-D115-7D882D68F1AD}*'
			line = str(line) + extraEnd
			try:
				line3 = ''
				i = len(line2) 
				y = len(line2) - int(p[2])
				while i > y:
					line3 += str(p[0])
					line3 += line2[y]
					y += 1
				remove = line3 + extraEnd
				line = line.replace(remove,'') + str(p[0])
				line = line.replace(extraEnd,'')
			except Exception as e:
				end = line2[len(line2) - 1]
				remove = str(p[0]) + end + extraEnd
				line = line.replace(remove,'') + str(p[0]) #######################
				line = line.replace(extraEnd,'')
		elif p1 == 'e':
			line2 = line.split(str(p[0]))
			try:
				line3 = ''
				i = len(line2) 
				y = len(line2) - int(p[2])
				while i > y:
					line3 += str(p[0])
					line3 += line2[y]
					y += 1
				line = line3
			except Exception as e:
				line = line2[len(line2) - 1]

		else:
			try:
				newLine = ''
				line2 = line.split(str(p[0]))
				for xx in p[1].split(';'):
					newLine += p[0]
					if xx == 'e':
						newLine += line2[len(line2) - 1]
					else:
						# newLine += _str.totalStrip(line.split(str(p[0]))[int(xx)])
						newLine += line.split(str(p[0]))[int(xx)]
				line = newLine
			except Exception as e:
				line = ''
	# _.pr(line)
	if _.switches.isActive('Alpha') == True:
		line = _str.cleanFirst(line,' ')
		line = _str.cleanLast(line,' ')
		# line = re.sub(r'([^\s\w]|_)+', '', line)
		# pattern = re.compile('([^\s\w]|_)+')
		# line = pattern.sub(' ', line).replace('  ',' ')
		# line = re.sub(r'\W+', '', line)
		line = _str.totalStrip(line)

	if _.switches.isActive('Word') == True:
		line = _str.cleanFirst(line,' ')
		line = _str.cleanLast(line,' ')
		line = _str.totalStrip(line)
		test = True
		if len(line) == 1 or len(line) == 2:
			test = False
		for char in str(line):
			try:
				char = int(char)
			except Exception as e:
				pass
			if type(char) is int:
				test = False

		if test == False:
			line = ''
		else:
			pass
			line = _str.cleanFirst(line,"'")
			line = _str.cleanLast(line,"'")
			# line = _str.removeAll(line,'*')
			# line = _str.removeAll(line,'[')
			# line = _str.removeAll(line,']')
			# line = _str.removeAll(line,'{')
			# line = _str.removeAll(line,'}')
	if _.switches.isActive('NoSpaceClean') == False:
		line = _str.cleanFirst(line,' ')
		line = _str.cleanLast(line,' ')
	if _.switches.isActive('EndsWith'):
		if not line.endswith(_.ci(_.switches.value('EndsWith'))):
			line = ''
	return line
def parseClean(line):
	if _.switches.isActive('Parse') == True:
		parse = _.switches.value('Parse')
		p = parse.split(',')
		pc =  _.ci(str(p[0]))
		line = _str.cleanLast(line,pc)
		line = _str.cleanFirst(line,pc)
	else:
		line = _str.cleanLast(line,',')
		line = _str.cleanFirst(line,',')
	if _.switches.isActive('NoSpaceClean') == False:
		line = _str.removeAll(line,'"')
	return line
def substitute(string):
	result = string
	# _.pr(string)
	p = _.switches.value('Substitute').split(',')
	p[0] = _.ci(p[0])
	p[1] = _.ci(p[1])
	# _.pr(p)
	# _.pr(p)    
	# os._exit(0)
	# result = _str.replaceAll(str(string),p[0],p[1])
	result = string.replace(p[0],p[1])
	# try:
	#     p = _.ci(_.switches.value('Substitute').split(',')[0])
	#     result = _str.replaceAll(str(string),p[0],p[1])
	# except Exception as e:
	#     pass
	return result
def make(string):
	if _.switches.isActive('Parse') == True:
		p = _.ci(_.switches.value('Parse').split(',')[0])
		i = 0
		stringTMP = string
		string = _.switches.value('Make')
		string = _str.replaceAll(string,";'",'"')
		for l in stringTMP.split(p):
			pp = '{' + str(i) + '}'
			# _.pr(l,pp)
			l = l.replace('\r','')
			l = l.replace('\n','')
			string = string.replace(pp,l)
			i += 1
	else:
		sub = _.switches.value('Make')
		sub =  _str.replaceAll(sub,";'",'"')
		if _.switches.isActive('Quote') == True:
			new = '"' + string + '"'
			string =  sub.replace('{}',new)
		else:
			string = sub.replace('{}',string)
	return string
def get_change(current, previous):
	if current == previous:
		return 100.0
	try:
	return round(100 - (((abs(current - previous))/previous)*100.0),1)
	except ZeroDivisionError:
		return 0

def crossRefBaseAdd(string,table):
	global xRefBase
	cnt = 0
	found = False
	for xRef in xRefBase:
		if xRefBase[cnt]['name'] == string:
			xRefBase[cnt]['count'] += 1
			found = True
		cnt += 1

	if found == False:
		xRefBase.append({'name':string,'table': table, 'count': 1})

def crossRefBaseCount(string,table):
	global xRefBase
	cnt = 0
	result = 0
	i = ''
	for xRef in xRefBase:
		if xRefBase[cnt]['name'] == string:
			result = xRefBase[cnt]['count']
			i = cnt
		cnt += 1

	found = result

	cnt = 0
	total = 0
	for xRef in xRefBase:
		if xRefBase[cnt]['table'] == table:
			total += 1
		cnt += 1
	result = {'id': i, 'found': found, 'total': total}
	return result

def crossRefGetMatch(inLine,line,parse,nameNum):
	line2 = line.split(parse)
	inLine2 = inLine.split(parse)
	cnt = 0
	while 1==1:
		cnt += 1
		if not line2[len(line2) - cnt] == inLine2[len(inLine2) - cnt]:
			break

	result = ''
	# _.pr(cnt)

	cnt = cnt - 1
	while cnt > 0:
		result += str(parse) + str(line2[len(line2) - cnt])
		cnt = cnt - 1
	result = _str.cleanFirst(result,parse)
	if nameNum == 'name':
		crossRefBaseAdd(inLine.replace(result,''),'inLine')
		crossRefBaseAdd(line.replace(result,''),'line')
	else:
		inLineT = crossRefBaseCount(inLine.replace(result,''),'inLine')
		lineT = crossRefBaseCount(line.replace(result,''),'line')
		result = {'inLine': inLineT, 'line': lineT}

	return result

def crossRef_xRef(xRef,line):
	result = False
	for item in xRef:
		# _.pr(item)
		if item == line:
			# _.pr('true')
			result = True
	return result


def crossReference(inLine,file,xRefRev):
	global xRef
	global xRefList

	p = _.switches.value('CrossReference').split(',')
	p[1] = _.ci(p[1])
	files = p[0]
	inLine2 = inLine.split(p[1])
	displayThis = 0
	match = False
	result = []
	try:
		displayThis = int(p[2])
	except Exception as e:
		pass
	if _.switches.isActive('CrossReferenceIntelligent') or _.switches.isActive('CrossReferenceSaveTables'):
		displayThis = 4
	maxCount = 0
	matchType = False
	for line in file:
		line = line.replace('\n','')
		line = line.replace('\r','')
		if _.switches.isActive('xReplace'):
			line = _.switches.value('xReplace')
			inLine = _.switches.value('xReplace')
			
		line2 = line.split(p[1])

		if len(line2) > 1:
			if line2[len(line2) - 1] == inLine2[len(inLine2) - 1] and line2[len(line2) - 2] == inLine2[len(inLine2) - 2]:
				matchType = 'complex'
				xMatch = crossRefGetMatch(inLine,line,p[1],'name')
				xRankCNT = crossRefGetMatch(inLine,line,p[1],'number')
				if xMatch.count(_v.slash) > maxCount:
					maxCount = xMatch.count(_v.slash)
					result = {'negotiated': xMatch,  'files': [{'nStat_id': xRankCNT['inLine']['id'], 'path': inLine},{'nStat_id': xRankCNT['line']['id'],'path': line}] }
				if _.switches.isActive('CrossReferenceUltimate') and crossRef_xRef(xRef,xMatch):
					match = 'Old'
				else:
					match = True
		elif line2[len(line2) - 1] == inLine2[len(inLine2) - 1]:
			matchType = 'simple'
			xMatch = inLine2[len(inLine2) - 1]
			if _.switches.isActive('CrossReferenceUltimate') and crossRef_xRef(xRef,xMatch):
				match = 'Old'
			else:
				match = True
		# HERE
	# HERE!
	if match == True and matchType == 'complex':
		if displayThis == 3:
			_.pr(result['files'][0]['path'],result['files'][1]['path'])
		elif displayThis == 1:
			_.pr(result['files'][0]['path'])
		elif displayThis == 2:
			_.pr(result['files'][1]['path'])
		elif displayThis == 0:
			_.pr(result['negotiated'])
		elif displayThis == 4:
			xRefList.append(result)
		if _.switches.isActive('CrossReferenceUltimate') and xRefRev == False:
			xRef.append(result['negotiated'])
	if match == True and matchType == 'simple':
		if displayThis == 1:
			_.pr(inLine)
		elif displayThis == 0:
			_.pr(xMatch)
		if _.switches.isActive('CrossReferenceUltimate') and xRefRev == False:
			xRef.append(xMatch)
	if displayThis == 5 and match == False:
		_.pr(inLine)

	return match




####################################################################
####################################################################

if _.switches.isActive('Parse'):
	parse = _.switches.value('Parse')
	p = parse.split(',')
	p[0] =  _.ci(str(p[0]))
	p[1] =  _.ci(str(p[1]))
	if p[1] == ';mdt':
		_.switches.fieldSet('Unique','active',True)

if _.switches.isActive('CrossReferenceUltimate') == True:
	_.switches.fieldSet('CrossReference','active',True)
	_.switches.fieldSet('CrossReference','value',_.switches.value('CrossReferenceUltimate'))
	_.switches.fieldSet('CrossReferenceReverse','active',False)

if _.switches.isActive('CrossReference') == True:
	p = _.switches.value('CrossReference').split(',')
	files = p[0]
	crossRef_File = []
	with open(files, 'r', encoding='latin-1') as ins:
		for line in ins:
			line = line.replace('\n','')
			line = line.replace('\r','')
			crossRef_File.append(line)
	ins.close()
def cleanPreSpace(line):
	if _.switches.isActive('NoSpaceClean') == False:
		line = _str.removeAll(line,'\t')
		line = _str.replaceDuplicate(line,' ')
		line = _str.cleanFirst(line,' ')
	line = line.replace('\n','')
	line = line.replace('\r','')
	return line

def fixCSV(line):
	if _.switches.isActive('NoSpaceClean') == False:
		line = _str.replaceDuplicate(line,' ')
		line = _str.cleanFirst(line,' ')
		line = _str.cleanLast(line,' ')
	# _.pr(line[0])
	theSplits = line.split(',')

	result = ''
	for ts in theSplits:
		ts = str(ts)
		if ts == '':
			ts = '""'
		if not ts[0] == '"':
			ts = '"' + ts
		if not ts[-1] == '"':
			ts = ts + '"'
		result += ts + ','
	result = _str.cleanLast(result,',')
	result = _str.replaceAll(result,'{6BEB554C-3FCE-419F-8917-B5A0678F48BA}',',')
	return result
_.delim = ','
if _.switches.isActive('Parse') == True:
	_.switches.fieldSet('ParseClean','active',True)
# _.pr(_.switches.value('Parse'))
# sys.exit()
cnt = 0
lNumber = 1
cntCrossRefG1 = 0
cntCrossRefB1 = 0
xRef = []
xRefBase = []
xRefList = []
############################################################################ ############################################################################
# (START)
if _.switches.isActive('Unique') == True:
	resultList = []
if _.switches.isActive('CrossReferenceReverse') == False:
	if type( _.appData[__.appReg]['pipe'] ) == list:
		for line in _.appData[__.appReg]['pipe']:
			line = str(line)
			line = line.replace('\n','')
			lineOriginal = line
			if _.switches.isActive('Upper') == True:
				line = line.upper()
			if _.switches.isActive('Lower') == True:
				line = line.lower()
			if _.switches.isActive('Character') == True:
				try:
					pass
					line = line.encode('UTF-8').decode('latin-1')
				except Exception as e:
					pass
			#     if _.switches.isActive('Progress') == False:
					# if _.switches.isActive('Count') == False:
			if countThisLine(line) == True:
				parse0 = _.switches.value('Parse')
				parse = parse0.split(',')
				# _.pr()
				# sys.exit()
				# line = displayLine(line)
				if parse0.count(',') == 3:
					line2 = line
					_.switches.fieldSet('Parse2','value',str(parse[0])+','+str(parse[1]))
					# _.pr( _.switches.value('Parse2'))
					line = str(displayLine(line))
					_.switches.fieldSet('Parse2','value',str(parse[2])+','+str(parse[3]))
					# _.pr( _.switches.value('Parse2'))
					# _.pr(line)
					l2 = str(displayLine(line2))
					line += ' - ' + l2.replace(_.ci(parse[2]),'')
					# _.pr(line)
					# sys.exit()
				else:
					_.switches.fieldSet('Parse2','value',_.switches.value('Parse'))
					line = displayLine(line)
				# _.pr(line)

				if _.switches.isActive('x92') == True:
					line = line.encode('UTF-8').decode('latin-1')
					line = _str.replaceAll(line,"'",'\u0092')

				# _.pr(line)
				if _.switches.isActive('Precsv2json') == True:
					slashID = '3D2B7E36-B661-4C46-B37B-7B537663F6BB'
					line = _str.replaceAll(line,_v.slash,slashID)
				# _.pr(line)
				if _.switches.isActive('FixCSV') == True:
					line = fixCSV(line)
				if _.switches.isActive('NoClean') == False:
					try:
						if _.switches.isActive('FixChar') == True:
							pass
							line = _str.cleanSpecial(line,True)
						else:
							pass
							line = _str.cleanSpecial(line)
					except Exception as e:
						pass
					try:
						pass
						# line = cleanPreSpace(line)
					except Exception as e:
						pass

				# _.pr(line)
				if _.switches.isActive('Postcsv2json') == True:
					line = _str.replaceAll(line,'{6BEB554C-3FCE-419F-8917-B5A0678F48BA}',',')
					# slashID = '3D2B7E36-B661-4C46-B37B-7B537663F6BB'
					# line = _str.replaceAll(line,slashID,_v.slash)

				if _.switches.isActive('ParseClean') == True:
					if _.switches.isActive('Unique') == False:
						_.switches.fieldSet('NoCount','active',True)
					line = parseClean(line)
				if _.switches.isActive('Substitute') == True:
					pass
					line = substitute(line)
				if _.switches.isActive('Make') == True:
					pass
					if _.switches.isActive('Original'):
						if len(line) > 0:
							line = make(lineOriginal)
							_.pr(line)
					else:
						if len(line) > 0:
							line = make(line)
							_.pr(line)
					
				else:
					if _.switches.isActive('Unique') == True:
						resultList.append(line)
					if _.switches.isActive('LineNumber') == True:
						if _.switches.isActive('Original'):
							_.pr(lNumber,lineOriginal)
						else:
							_.pr(lNumber,line)
					else:
						if _.switches.isActive('CrossReference') == True:
							if crossReference(line,crossRef_File,False):
								cntCrossRefG1 += 1
							else:
								cntCrossRefB1 += 1
						elif _.switches.isActive('JustCount') == False:
							pass
							if _.switches.isActive('Test') == False and _.switches.isActive('Unique') == False:
								pass
								if not _.switches.isActive('Make'):
									if _.switches.isActive('Original'):
										if _.switches.isActive('Blanks'):
											if len(lineOriginal) > 0:
												_.pr(lineOriginal)
										else: 
											_.pr(lineOriginal)
									else:
										if _.switches.isActive('Blanks'):
											if len(line) > 0:
												_.pr(line)
										else: 
											_.pr(line)
								else:
									_.pr(line)

			cnt += 1
		lNumber += 1

############################################################################ ############################################################################

if _.switches.isActive('CrossReference') == True and _.switches.isActive('NoCount') == False  and _.switches.isActive('CrossReferenceUltimate') == False:
	_.pr('\tGood',cntCrossRefG1,'\tBad',cntCrossRefB1)
	_.pr('Total',cntCrossRefB1 + cntCrossRefG1)






if _.switches.isActive('Count') == False:
	_.pr('')
if _.switches.isActive('NoCount') == False and _.switches.isActive('Progress') == False and _.switches.isActive('Unique') == False and _.switches.isActive('CrossReference') == False:
	_.pr('{}'.format(cnt))
	if _.switches.isActive('CountDiv'):
		divby = int(_.switches.value('CountDiv'))
		ncnt = cnt / divby
		nncnt = round(ncnt,1)
		_.pr(nncnt)



if _.switches.isActive('Progress') == True:
	theTotal = int(_.switches.value('Progress'))
	result = get_change(cnt,theTotal)
	_.pr(result,'%')
	_.pr('\t',cnt,'of',theTotal)

if _.switches.isActive('Unique') == True:
	resultNew = set(resultList)
	cnt = 0
	for r in resultNew:
		_.pr(r)
		cnt += 1
	if _.switches.isActive('NoCount') == False:
		_.pr('\n{}'.format(cnt))







if _.switches.isActive('CrossReferenceUltimate') == True:
	# _.switches.fieldSet('CrossReference','active',True)
	# _.switches.fieldSet('CrossReference','value',_.switches.value('CrossReference'))
	_.switches.fieldSet('CrossReferenceReverse','active',True)



if _.switches.isActive('CrossReferenceReverse') == True:
	cntCrossRefG2 = 0
	cntCrossRefB2 = 0
	cntCrossRefO2 = 0
	cnt2 = 0
	for line in crossRef_File:
		# _.pr(line)
		line = str(line)
		if _.switches.isActive('Character') == True:
			try:
				pass
				line = line.encode('UTF-8').decode('latin-1')
			except Exception as e:
				pass

		if countThisLine(line) == True:
			cnt2 += 1
			test = crossReference(line,_.appData[__.appReg]['pipe'],True)
			if test == 'Old':
				cntCrossRefO2 += 1
			elif test == False:
				cntCrossRefB2 += 1
			else:
				cntCrossRefG2 += 1
	
	linesPipe = cnt
	linesFile = cnt2
	linesTotal = cnt + cnt2
	i = 0
	for xRef in xRefBase:
		xRefBase[i]['value'] = round(((xRefBase[i]['count'] / linesTotal) * 100),4)
		i += 1
	# if _.switches.isActive('CrossReferenceIntelligent'):

	if _.switches.isActive('CrossReferenceIntelligent'):
		thresholdCount = 10
		thresholdPercent = 2
		cntOmited = 0
		for xRef in xRefList:
			if (xRefBase[xRef['files'][0]['nStat_id']]['value'] > thresholdPercent and xRefBase[xRef['files'][1]['nStat_id']]['value'] > thresholdPercent) or xRefBase[xRef['files'][1]['nStat_id']]['count'] > thresholdCount:
				_.pr(xRef['negotiated'])
				pass
			else:
				cntOmited += 1


	if _.switches.isActive('NoCount') == False:
		_.pr('')
		if _.switches.isActive('CrossReferenceIntelligent'):
			_.pr('Omited',cntOmited)
		# linesPipe = len(_.appData[__.appReg]['pipe'])
		# linesFile = len(crossRef_File)
		cnt2 = cntCrossRefG2 + cntCrossRefO2
		if _.switches.isActive('CrossReferenceUltimate') == False:
			_.pr('\tGood',cnt2,'\tBad',cntCrossRefB2)
			_.pr('Total',cntCrossRefB2 + cnt2)
		else:
			if cnt2 > cntCrossRefG1:
				cntGood = cnt2
			else:
				cntGood = cntCrossRefG1

			_.pr('\tGood',cntGood,'\tBad',linesPipe - cntGood)
			_.pr('Pipe',linesPipe,'Lines\n')
			_.pr('\tGood',cntGood,'\tBad',linesFile - cntGood)
			_.pr('File',linesFile,'Lines\n')

			if len(xRefBase) > 1:
				_.switches.fieldSet('Sort','active',True)
				_.switches.fieldSet('Sort','value','desc:name,desc:count')
				_.tables.register('Auto',xRefBase)
				_.tables.print('Auto','name,count,value')
				# _.pr(xRefBase)

if _.switches.value('CrossReferenceIntelligent') == 'save' or _.switches.value('CrossReferenceIntelligent') == 'build' or _.switches.isActive('CrossReferenceSaveTables'):
	if _.switches.isActive('CrossReferenceReverse') == False:
		linesTotal = cnt + len(crossRef_File)
		i = 0
		for xRef in xRefBase:
			xRefBase[i]['value'] = round(((xRefBase[i]['count'] / linesTotal) * 100),4)
			i += 1
	file1 = 'file_negotiation_table.json'
	file2 = 'file_negotiation_statistics.json'
	_.saveTable(xRefList,file1)
	_.saveTable(xRefBase,file2)






