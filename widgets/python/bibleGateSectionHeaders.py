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

from lxml import html
import requests
import cssselect

##################################################


def appSwitches():
	pass
	_.switches.register('Version', '-v','file.txt')
	



_.appInfo[focus()] = {
	'file': 'bibleGateSectionHeaders.py',
	'description': 'Acquire Bible section headers from biblegateway.com',
	'categories': [
						'bible',
						'categories',
						'scrape',
						'scraping',
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

_.appInfo[focus()]['examples'].append('p bibleGateSectionHeaders')

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




# _.appData[__.appReg]['pipe'] = ''
# if not sys.stdin.isatty():
#     _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
#     pipeCleaner()



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

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')
# _.saveTable( jsonFile, 'file.json', printThis=True )

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START

def cleanupString(string,beforeAfter=True):
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.cleanFirst(string,' ')
	string = string.replace(_v.slash+'xe2\\x80\\x93','-')
	string = string.replace(_v.slash+'\\xe2\\\\x80\\\\x93','-')
	if beforeAfter:
		string = string.split('(')[0]
	else:
		string = string.split('(')[1]
	string = string.split('/')[0]
	string = string.replace(_v.slash+'xbb','')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanBE(string,' ')
	return string


def processSection( bkid, book, chapter, url, qID=0 ):
	global data
	global payload
	page = requests.get(url)
	tree = html.fromstring(page.content)
	h3 = tree.cssselect('h3')
	mem = 0
	for h in h3:
		try:
			s = h.cssselect('span')
			c = str(s[0].get('class'))
			r = c.replace('text ','')
			t = cleanupString(s[0].text_content())
			# _.pr( bkid, book, chapter, url)
			info = { 'book': book, 'chapter': chapter, 'verses': r, 'text': t, 'url': url,  }
			data[bkid]['chapters'][str(chapter)].append( info )
			# _.pr( book, chapter, r )
			payload += 1
			mem += sys.getsizeof( info )
			# mem = 0
		except Exception as e:
			pass
	try:
		lines = len( data[bkid]['chapters'][str(chapter)] )
	except Exception as e:
		lines = 0

	_.threads.spent( qID, mem, lines=lines )


def action():
	global meta
	global data
	global total
	_.threads.add( 'headers', trigger=complete, loaded=False ) # kwargs 
	_.threads.maxThreadsSafe = 250
	_.threads.report = False
	_.threads.auditPrint = False
	_.threads.scheduleLoop = .1
	_.threads.auditLoop = .1
	_.threads.autoLoadedAfter = .5


	if _.switches.isActive('Version'):
		url = 'https://www.biblegateway.com/passage/?version='+_.switches.value('Version').upper()+'&interface=amp&search='
	else:
		url = 'https://www.biblegateway.com/passage/?version=NIV&interface=amp&search='
	# url = 'https://www.biblegateway.com/passage/?version=ASV&interface=amp&search='
	# url = 'https://www.biblegateway.com/passage/?version=NASB&interface=amp&search='
	total = 0
	for mi,m in enumerate(meta):
		# if mi == 0:
		data[mi] = {}
		data[mi]['book'] = m['name']
		
		for ci,c in enumerate(m['chapter_verses']):
			total += 1

	_.threads.statusTotal = total
	_.pr()
	total = 0
	for mi,m in enumerate(meta):
		# if mi == 0:
		data[mi] = {}
		data[mi]['book'] = m['name']
		
		for ci,c in enumerate(m['chapter_verses']):
			total += 1
			try:
				data[mi]['chapters'][ str(c['chapter']) ] = []
			except Exception as e:
				data[mi]['chapters'] = {}
				data[mi]['chapters'][ str(c['chapter']) ] = []
				
			# if ci < 10:
			link = url + m['name'] + '+' + str(c['chapter'])
			_.threads.add( 'headers', processSection, [ mi, m['name'], (c['chapter']), link ] )
	# _.pr(total)


# def action2():
#     global data
#     _.threads.add( 'headers', trigger=complete, loaded=False ) # kwargs 
#     _.threads.maxThreadsSafe = 250
#     _.threads.report = True
#     _.threads.auditPrint = True
#     url = 'https://www.biblegateway.com/passage/?version=NIV&interface=amp&search=' + 'Genesis+9'
#     _.threads.add( 'headers', processSection, [ 0, 'Genesis', 9, url ] )

def complete():
	global data
	global total
	global payload

	_.pr()
	_.pr()
	_.pr('________________________________')
	_.pr()
	_.pr(' All books have been processed')
	_.pr('________________________________')
	_.pr()
	_.pr( 'data:',len(data) )
	_.pr( 'urls:', total)
	_.pr( 'payload:', payload)
	_.pr()
	if _.switches.isActive('Version'):
		_.saveTable( data , 'Bible_section_headers_biblegateway_'+_.switches.value('Version').upper()+'.json', printThis=True )
	else:
		_.saveTable( data , 'Bible_section_headers_biblegateway_NIV.json', printThis=True )

data = {}
# data = _.getTable('Bible_section_headers_biblegateway.json')
meta = _.getTable('bible_chapter_verse_meta.json')
# bibleGateSectionHeaders
payload = 0
########################################################################################
if __name__ == '__main__':
	action()