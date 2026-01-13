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

# import os
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
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

##################################################

# from lxml import html
# import requests
# import cssselect

##################################################


def appSwitches():
	pass
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	



_.appInfo[focus()] = {
	'file': 'bibleSectionHeadersProcess.py',
	'description': 'Process scraped Bible section headers',
	'categories': [
						'bible',
						'categories',
						'process scraped data',
						'process data',
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

_.appInfo[focus()]['prerequisite'].append('p bibleSectionHeaders')
_.appInfo[focus()]['relatedapps'].append('p bibleGateSectionHeadersFilesInfo')

_.appInfo[focus()]['examples'].append('p bibleSectionHeadersProcess')

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



########################################################################

# def processFolder(folder, qID):
# __.queueLastActivity = time.time()
# __.projectData[focus()][__.pdID[focus()]].append( obj )
# _.threads.add( 'test', testFunction, [{'two':item}], kwargs=True )
# _.threads.add( 'process_folder', processFolder, [ path ] )
# _.threads.spent( qID, sys.getsizeof( 'obj') )
					################
# _.threads.add( 'test', trigger=complete, triggerArg={'hello','test'}, loaded=False )
# _.threads.add( 'test', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
# _.threads.maxThreadsSafe = 250
# _.threads.report = True
# _.threads.projectDataFileSQL = db
# _.threads.auditPrint = False

##################

# _.appData[focus()]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
# _.appInfo[focus()]['instance'] = _.genUUID()
# # _.appData[focus()]['audit'].append( { 'start': True, 'note': '', 'entire': True, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );

# _dir.sqlCreateTable( db, deleteDBFirst=True, close=True )
# obj = _dir.fileInfo( path, sql=True )
# _.pr(   _dir.fileInfo( _.switches.value('Input') )['size']   )

# _.saveLog('queue')
# _.saveLog('audit')

########################################################################

# os.path.isfile(files)
# os.system('cls')

# _.switches.isActive('_File_')
# global

# _.appInfo[focus()]['categories']

# #######################################
# uuidProject = { 'input': _.switches.value('Input'), 'note': 'sample' }
# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[__.appReg]['file'], 'project': uuidProject }
# _.genUUID(project='')
# _.genUUID('temp file')
# _.genUUID({'file':'app.py'})
# #######################################
# import blank
# blank.focus(focus())
# blank.registerSwitches()
# _.switches.fieldSet('Input','active','one')
# _.switches.fieldSet('Input','value','one')
# focus()
# #######################################

# _.switches.fieldSet('_File_','active',True)

# _.switches.dumpSwitches(includeBlank=False)

# _.tables.register('childClassItems',childItems)
# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
# _.tables.print('childClassItems','name')

# backupLog = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )

# _mime.isText(file)
# _mime.isBinary(file)

# books = _.getText(_v.myTables + _v.slash+'bible_books.csv')
# _.saveText(convertedFile,'file.txt')

# 
# _.saveTable(jsonFile,'file.json')
# _.saveTable( jsonFile, 'file.json', printThis=True )

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START

def expandRef(data0):
	global books
	verses = []
	b = books[data0[0]]['name']
	# #####x  _.pr(data0)
	# #####x  _.pr()
	############### dont forget if :
	#####x  _.pr(data0)
	if len(data0[1]) > 0:
		if not ':' in data0[1]:
			data0[1] = '1:' + data0[1]
		if ':' in data0[1]:
			cT = data0[1].split(':')[0]
			iT = data0[1].split(':')[1].split(',')

			# #####x  _.pr('ch',cT)
			for iX in iT:
				if '-' in iX:
					# #####x  _.pr(iX)
					th = iX.split('-')
					for xD in range(int(th[0]),int(th[1])+1):
						r_b = data0[0]
						r_c = cT
						r_v = xD
						verses.append([int(r_b)+1,int(r_c),int(r_v)])
						#####x  _.pr(b,cT,xD)
				else:
					r_b = data0[0]
					r_c = cT
					r_v = iX
					if len(r_v) == 0:
						r_v = 0
					# _.pr(r_b,r_c,r_v)
					# verses.append([data0[0],cT,iX])
					verses.append([int(r_b)+1,int(r_c),int(r_v)])
					#####x  _.pr(b,cT,iX)
		else:
			#####x  _.pr('********************************************')
			
			for bCH in books[data0[0]-1]['chapter_verses']:
				if bCH['chapter'] == int(data0[1]):
					for xD in range(1,int(bCH['verses']) +1):
						r_b = data0[0]
						r_c = data0[1]
						r_v = xD
						# verses.append([data0[0],int(data0[1]),xD])
						verses.append([int(r_b)+1,int(r_c),int(r_v)])
						#####x  _.pr(b,int(data0[1]),xD)

			#####x  _.pr('********************************************')
	return verses


def bibleText(data):
	global theBible

	for tB in theBible['resultset']['row']:
		if int(data[0]) == tB['field'][1] and int(data[1]) == tB['field'][2] and int(data[2]) == tB['field'][3]:
			result = tB['field'][0]
	return result


def getBook( book ):
	global booksNew

	for i,bn in enumerate(booksNew):
		_.pr( bn )
		if book == bn['book']:
			return bn['abbreviation']




def processData():
	global data
	global booksNew
	ix = 0
	for i,b in enumerate(data.keys()):
		theID = str(i)
		if i == 0:

			for ii,row in enumerate(data[theID]['data']):
				ix += 1
				if ii < 10:
					try:
						reference_ids = expandRef( [ i, row['verses'].split(' ')[1] ] )
						data[theID]['reference_ids'] = reference_ids
						verse_ids = bibleIDs( reference_ids )
						data[theID]['verse_ids'] = verse_ids
						data[theID]['expanded_verses'] = booksNew[i]['book'] + ' ' + row['verses'].split(' ')[1]
						data[theID]['biblegateway'] = 'https://www.biblegateway.com/passage/?version=NIV&interface=amp&search=' + data[theID]['expanded_verses'].replace(' ','+')
						_.pr( data[theID]['biblegateway'] )
					except Exception as e:
						_.pr( 'Error:', ix, booksNew[i]['book'], row['verses'] )





	_.pr(ix)
	_.saveTable( data , 'Bible_section_headers.json', printThis=True )

def action():
	
	newAbbreviations()
	processData()

def bibleIDs(reference_ids):
	global theBible
	result = []
	for i,verse in enumerate(theBible['resultset']['row']):
		for ref in reference_ids:
			if ref[0] == verse['field'][1] and ref[1] == verse['field'][2] and ref[2] == verse['field'][3]:
				result.append( verse['field'][0] )

	return result







def newAbbreviations():
	global booksNew
	global booksRaw
	global data

	for i,br in enumerate(booksRaw):
		br = br.replace('\n','').replace('.','')
		# _.pr( br )
		abbreviation = br.split(',')[1]
		n = {
				'book':        br.split(',')[0],
				'abbreviation':    br.split(',')[1],
				'minimal':    data[str(i)]['abbreviation']
		}
		booksNew.append( n )
	# _.saveTable( booksNew , 'Bible_abbreviation_minimal.json', printThis=True )



	
books = _.getTable('bible_chapter_verse_meta.json')
theBible = _.getTable('t_asv.json')
booksRaw = _.getText(_v.myTables + _v.slash+'bible_books.csv')
booksNew = []
data = _.getTable('Bible_section_headers.json')
########################################################################################
if __name__ == '__main__':
	action()