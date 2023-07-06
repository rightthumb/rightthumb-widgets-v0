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
import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

##################################################

from lxml import html
# import requests
import cssselect

from bs4 import BeautifulSoup

##################################################

def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.htm, https://lxml.de/tutorial.html')
	_.switches.register('Folder', '-folder')
	



_.appInfo[focus()] = {
	'file': 'auditHTML.py',
	'description': 'Report on html stuff',
	'categories': [
						'research',
						'html',
						'local',
						'online',
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
_.appInfo[__name__]['examples'].append('p auditHTML -i Pinterest_Page_Cache_ID-461548661794872237.html')
_.appInfo[__name__]['examples'].append('p auditHTML -i Pinterest_Page_Cache_ID-461548661804503455.html')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p auditHTML -folder + *.html')
_.appInfo[__name__]['examples'].append('')
_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

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



if __name__ == '__main__':
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

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START






def extractID(text):
	global removeThis
	text = str(text)
	text = text.replace('\n','')
	text = text.replace('\r','')
	text = text.replace(' ','')
	before = len(text)
	for rt in removeThis:
		text = text.replace(rt,'')
	after = len(text)
	if before == after:
		text = ''
	return text
def getPage(url):
	global thisWebPage
	if type(thisWebPage) == bool:
		f = open(url, 'r', encoding='UTF-8')
		file = f.read()
		file = file.encode('latin-1','ignore')
		file = file.decode('utf-8','ignore')
		thisWebPage = BeautifulSoup(file,"html.parser")
	return thisWebPage
def getLocal(url):
	_.pr('Not Configured')
	sys.exit()

def getPageTitle(url):
	try:
		thisWebPage = getPage(url)
		pageTitle = thisWebPage.title.string
	except Exception as e:
		pageTitle = 'Error: Title'
	return pageTitle


def getPageStructure(url,report):
	global projectReport
	projectReport = { 'classes': [], 'el': [], 'ids': [], 'timestart': time.time()}
	thisWebPage = getPage(url)
	try:
		first_child = thisWebPage.find("body")

		for i,ch in enumerate(first_child.children):
			data = { 'data': [], 'el': [], 'ids': [], 'timestart': time.time()}
			thinkOfTheChildren(ch,data)
		report['structure'] = projectReport
		return report
	except Exception as e:
		pass
# def getPageStructure(url,report):
#     global projectReport
#     global theCount
#     global duplicateText
#     global thisWebPage

#     projectReport = []
#     thisWebPage = getPage(url)
#     _.pr()
#     _.pr()
#     _.pr(url)
#     _.pr()
#     _.pr()
#     first_child = thisWebPage.find("body")
#     for i,ch in enumerate(first_child.children):
#         data = { 'data': [], 'el': [], 'ids': [], 'timestart': time.time()}
#         thinkOfTheChildren(ch,data)
#     report['structure'] = projectReport
#     # try:
#     # except Exception as e:
#     #     _.pr('children error')
#     #     return ''
#     return report
####################################################################################

# def thinkOfTheChildren(obj,report,path='-'):
#     global projectReport
#     global theCount
#     global pathOmitList
#     global objOmitList
#     global objOmitListContains
#     global duplicateText

#     objLength = 4
#     try:
#         path += ':' + obj.name
#     except Exception as e:
#         path += ':-'
#     try:
#         # if not scriptText in path:
#         #     ids = str(obj.get('id'))
#         #     if not ids == 'None':
#         report['ids'].append()
#     except Exception as e:
#         pass
#     try:
#         # path += ':[' + obj.name + ':' + obj.get('id') + '(' + obj.get('class') + ')]'
#         path += '[' + obj.get('id') + ']'
#     except Exception as e:
#         pass
#     # try:
#     #     if len(str(obj)) > 2:
#     #         report['el'].append({'path': path,'obj': str(obj)})
#     # except Exception as e:
#     #     pass
#     # try:
#     #     # path += ':[' + obj.name + ':' + obj.get('id') + '(' + obj.get('class') + ')]'
#     #     # path += '(' + obj.get('class') + ')'
#     #     try:
#     #         pass
#     #         shouldAdd = True
#     #         for omit in pathOmitList:
#     #             if omit in path:
#     #                 shouldAdd = False

#     #         if shouldAdd and not obj == '\n' and len(obj) > objLength and not obj.startswith('<!'):
#     #             report['data'].append({'path': path,'attrib': dict(obj.attrs.values())})
#     #     except Exception as e:
#     #         try:
#     #             shouldAdd = True
#     #             for omit in pathOmitList:
#     #                 if omit in path:
#     #                     shouldAdd = False

#     #             if shouldAdd and not obj == '\n' and len(obj) > objLength and not obj.startswith('<!'):
#     #                 report['data'].append({'path': path,'attrib': list(obj.attrs.values())})
#     #         except Exception as e:
#     #             pass
#     # except Exception as e:
#     #     pass

#     # try:
#     #     test = 1
#     #     for ch in obj.children:
#     #         pass
#     #         # thinkOfTheChildren(ch,report,path)
#     # except Exception as e:
#     #     test = 0


#     shouldFindChildren = True
#     shouldAdd = True
#     showError = True

#     if not obj.children:
#     # if True:
#     # if False:
#         _.pr('no children')
#         try:
#             obj = cleanText(obj)
#             if showError:
#                 _.pr()
#             if shouldAdd:
#                 for omit in pathOmitList:
#                     if omit in path:
#                         shouldAdd = False
#                         # shouldFindChildren = False
#                         if showError:
#                             _.pr(0)
#             if shouldAdd:
#                 for omit in objOmitListContains:
#                     if omit.lower() in obj.lower():
#                         shouldAdd = False
#                         if showError:
#                             _.pr(1)
#             if shouldAdd:
#                 for omit in objOmitList:
#                     if omit == obj:
#                         shouldAdd = False
#                         # shouldFindChildren = False
#                         if showError:
#                             _.pr(2)
#             if shouldAdd:
#                 for omit in duplicateText:
#                     if omit == obj and not path.endswith('span:-"') and not path.endswith('span"'):
#                         shouldAdd = False
#                         if showError:
#                             _.pr(3)
#             if shouldAdd:
#                 if obj.startswith('.'):
#                     shouldAdd = False
#                     if showError:
#                         _.pr(4)
#             if shouldAdd:
#                 if len(obj) <= objLength:
#                     shouldAdd = False
#                     if showError:
#                         _.pr(5)
#             # if shouldAdd:
#             #     if not obj.startswith('<!'):
#             #         shouldAdd = False
#             #         if showError:
#             #             _.pr(6)
#             if shouldAdd:
#                 if path == '-:-':
#                     shouldAdd = False
#                     if showError:
#                         _.pr(7)
#         except Exception as e:
#             shouldAdd = False





#         if shouldAdd:
#             if showError:
#                 _.pr('attempt')
#             duplicateText.append(obj)
#             # _.pr(obj)
#             report['el'].append({'path': path,'obj': obj})
#             report['timeend'] = time.time()
#             # if theCount <= 100:
#             projectReport.append(report)
#             # _.pr(report)
#             # theCount += 1
#             # report = []
#         if not shouldAdd:
#             pass
#             # report = []



#     try:
#         if shouldFindChildren:
#             for ch in obj.children:
#                 thinkOfTheChildren(ch,report,path)
#     except Exception as e:
#         pass
#         # _.pr(path,obj)



# def checkComplete(pinID):
#     global projectReport
#     result = True
#     for pr in projectReport:
#         if pr['pinID'] == pinID:
#             result = False
#     return result
####################################################################################

####################################################################################
####################################################################################
def thinkOfTheChildren(obj,report,path='-'):
	global projectReport
	global theCount
	global pathOmitList
	global objOmitList
	global objOmitListContains
	global duplicateText
	try:
		path += ':' + obj.name
	except Exception as e:
		path += ':-'
	# try:
	#     ids = str(obj.get('id'))
	#     if not ids == 'None':
	#         report['ids'].append(ids)
	# except Exception as e:
	#     pass
	try:
		path += '[' + obj.get('id') + ']'
	except Exception as e:
		pass

	try:
		classes = []
		for value in obj['class']:
			classes.append( value )

		report['data'].append( { 'path': path, 'pathlength': path.count(':')+1, 'attrib': classes } )
	except Exception as e:
		pass
		# try:
		#     report['data'].append( { 'path': path, 'pathlength': path.count(':'), 'attrib': dict(obj.attrs.values()) } )
		# except Exception as e:
		#     try:
		#         report['data'].append( { 'path': path, 'pathlength': path.count(':'), 'attrib': list(obj.attrs.values()) } )
		#     except Exception as e:
		#         pass



	try:
		test = 1
		for ch in obj.children:
			pass
			# thinkOfTheChildren(ch,report,path)
	except Exception as e:
		test = 0
	# last = time.time()
	if not test:
		objW = shouldThisBeAdded(obj,path)


		# _.pr('obj 3:',type(objW),len(objW),objW)
		obj = objW
		# pause = input('pause')
		if len(obj) > 5:
		# if True:
			# _.pr('added')
			# pause = input('pause')
			# try:
			#     try:
			#         attrib = dict(obj.attrs.values())
			#     except Exception as e:
			#         try:
			#             attrib = list(obj.attrs.values())
			#         except Exception as e:
			#             attrib = False
			# except Exception as e:
			#     attrib = False
			# _.pr(obj)


			

			attribCnt = 0
			relatedClasses = []
			try:
				for rdi,rd in enumerate(report['data']):
					found = False
					for prci,prc in enumerate(projectReport['classes']):
						if rd['path'] in path and rd['path'] == prc['path']:
							relatedClasses.append(prci)
							found = True
							attribCnt += 1
							
					if not found:
						relatedClasses.append( len( projectReport['classes'] ) )
						projectReport['classes'].append( rd )
				

			except Exception as e:
				pass



			duplicateText.append( obj )
			
			projectReport['el'].append( { 'path': path,'obj': obj, 'classids': relatedClasses } )
			projectReport['timeend'] = time.time()
			projectReport['timetotal'] = projectReport['timeend'] - projectReport['timestart']
			if attribCnt == 0:
				report = []
	try:
		test = 1
		for ch in obj.children:
			pass
			thinkOfTheChildren(ch,report,path)
	except Exception as e:
		test = 0
def shouldThisBeAdded(objx,path):
	shouldAdd = True
	showError = False
	pauseError = False
	global obj
	global objW
	try:
		r = json.dumps({'obj':objx})
		d = json.loads(r)
		obj = d['obj']
		# _.pr()
		# _.pr()
		# _.pr('obj 0:',len(obj),obj)
		if len(obj) < 5:
			shouldAdd = False
			# if showError:
			#     _.pr('00 first len')
		else:
			obj = cleanText(obj)
			objW = obj
			if len(obj) > 5:
				# _.pr('obj 1:',len(obj),obj)
				try:
					for omit in pathOmitList:
						if omit in path:
							shouldAdd = False
							if showError:
								_.pr(0,omit,path)
				except Exception as e:
					pass
				try:
					for omit in objOmitListContains:
						if omit.lower() in obj.lower():
							shouldAdd = False
							if showError:
								_.pr(1,omit,obj)
				except Exception as e:
					pass
				try:
					for omit in objOmitList:
						if omit == obj:
							shouldAdd = False
							if showError:
								_.pr(2,omit,obj)
				except Exception as e:
					pass
				try:
					for omit in duplicateText:
						if omit == obj and not path.endswith('span:-"') and not path.endswith('span"'):
							shouldAdd = False
							if showError:
								_.pr(3,omit,obj)
				except Exception as e:
					pass
				try:
					if obj.startswith('.') or obj.startswith('#') or obj.startswith('['):
						shouldAdd = False
						if showError:
							_.pr(4)
				except Exception as e:
					pass
				try:
					if len(obj) >= objLength:
						shouldAdd = False
						if showError:
							_.pr(5)
				except Exception as e:
					pass
				try:
					if path == '-:-':
						shouldAdd = False
						if showError:
							_.pr(6)
				except Exception as e:
					pass

		# _.pr('obj 2:',len(objW),objW)
		if not shouldAdd:
			# _.pr('not shouldAdd')
			objW = ''
		# else:
		#     if pauseError:
		#         pause = input('pause')
		return cleanText(objW)
	except Exception as e:
		obj = ''
		shouldAdd = False
		# _.pr('obj 4:',len(obj),obj)
		return ''
	# if shouldAdd:
	#     _.pr('pass 0')
	#     _.pr('obj:',len(obj),obj)

####################################################################################
####################################################################################
# def thinkOfTheChildren(obj,report,path='-'):
#     global projectReport
#     try:
#         path += ':' + obj.name
#     except Exception as e:
#         path += ':-'
#     try:
#         ids = str(obj.get('id'))
#         if not ids == 'None':
#             report['ids'].append()
#     except Exception as e:
#         pass
#     try:
#         path += '[' + obj.get('id') + ']'
#     except Exception as e:
#         pass
#     try:
#         try:
#             report['data'].append({'path': path,'attrib': dict(obj.attrs.values())})
#         except Exception as e:
#             try:
#                 report['data'].append({'path': path,'attrib': list(obj.attrs.values())})
#             except Exception as e:
#                 pass
#     except Exception as e:
#         pass
#     try:
#         test = 1
#         for ch in obj.children:
#             thinkOfTheChildren(ch,report,path)
#     except Exception as e:
#         test = 0
#     if not test:
#         report['el'].append({'path': path,'obj': obj})
#         report['timeend'] = time.time()
#         projectReport.append(report)
####################################################################################
####################################################################################


def saveResults(data):
	_.pr()
	if type(data) == dict:
		report.append(data)
		_.pr(report)
		_.saveTable(report,'auditHTML.json')
	else:
		_.pr('Not Saved')

def action():
	global thisWebPage
	global projectReport
	global completedIDs
	global projectReport
	global duplicateText
	global thisWebPage

	if _.switches.isActive('Input'):
		duplicateText = []
		url = _.switches.value('Input')
		if 'http' in url:
			saveResults(getRemote(url))
		else:
			# try:
			#     thisWebPage = getPage(url)
			# except Exception as e:
			#     thisWebPage = ''
			pageTitle = getPageTitle(url)
			_.pr('title:',pageTitle)
			pinID = extractID(url)
			report = {'pinID': pinID, 'title': pageTitle, 'structure': [], 'timestart': time.time()}
			pageStructure = getPageStructure(url,report)
			# _.pr(pageStructure)
			_.saveTable2(pageStructure,'auditHTML.json', printThis=True)
			# saveResults()


	if _.switches.isActive('Folder'):
		folder = os.getcwd()
		dirList = os.listdir(folder)
		i = 0

		for tdi,td in enumerate(dirList):
			duplicateText = []
			td = td.replace('\n','')
			if _.showLine(td):
				pinID = extractID(td)

				# if checkComplete(pinID):
				if pinID in completedIDs:
					_.pr('duplicate:',pinID)
				else:
					projectReport = []
					# try:
					_.pr()
						# _.pr(pinID)
					# try:
					#     thisWebPage = getPage(td)
					# except Exception as e:
					#     thisWebPage = ''
					# if thisWebPage == '':
					#     _.pr('get error:',pinID)
					# else:
					# try:
					# except Exception as e:
					#     pass
					_.pr(_dir.formatSize(_dir.getSize(td)),pinID)
					pageTitle = getPageTitle(td)
					# _.pr('title:',pageTitle)
					report = {'pinID': pinID, 'title': pageTitle, 'structure': [], 'timestart': time.time()}

					getPageStructure(td,report)
					
					# except Exception as e:
					#     pass
					thisWebPage = True
					dataPath = 'D:\\Pinterest_Cache_Report\\Pinterest_Page_Cache_Report_ID-THEID.json'
					jsonFile = dataPath.replace('THEID',pinID)
					if len(projectReport) == 0:
						_.pr('projectReport: 0')
					else:
						projectReportSize = sys.getsizeof(projectReport)
						if projectReportSize > 100:
							_.pr('memory:',projectReportSize)
							# _.pr(projectReport)
							_.saveTable2(projectReport,jsonFile, printThis=True    )
						else:
							_.pr('Memory error:',projectReportSize)
						projectReport = []


		# for item in dirList:
		#     path = folder + _v.slash + item
		#     if os.path.isfile(item):
		#     # if os.path.isdir(item) == True:
		#         if _mime.isText(item) and _.showLine(item):
		#             saveResults(getLocal(item))
					
		#             i = i + 1
# saveResults(getLocal(item))
if __name__ == '__main__':
	projectReport = []
	removeThis = []
	removeThis.append('Pinterest_Page_Cache_ID-')
	removeThis.append('.html')
	removeThis.append('.json')
	removeThis.append('Pinterest_Pin_Data_ID-')
	removeThis.append('Pinterest_Page_Cache_Report_ID-')
	removeThis.append('Pinterest_Cache_Report')
	removeThis.append(_v.slash)
	removeThis.append('D:')
	completedIDs = []
	completedIDs.append('461548661795334760')
	completedIDs.append('461548661794872237')
	if os.path.isdir('D:\\Pinterest_Cache_Report'):
		dirList = os.listdir('D:\\Pinterest_Cache_Report')
		for item in dirList:
			completedIDs.append(extractID(item))

	_.pr('completedIDs:', len(completedIDs))

	# auditHTML
	thisWebPage = True
	# projectReport = _.getTable('auditHTML.json')


	theCount = 0
	pathOmitList = []
	pathOmitList.append( ':script' )
	pathOmitList.append( ':form' )
	pathOmitList.append( 'div[registration' )
	pathOmitList.append( 'signin' )
	pathOmitList.append( ':style:' )
	pathOmitList.append( '::style[' )
	pathOmitList.append( ':option:' )
	pathOmitList.append( ':a:' )
	pathOmitList.append( ':article:' )
	pathOmitList.append( 'li[comment-' )
	pathOmitList.append( ':button:' )
	pathOmitList.append( '-tweet-' )
	pathOmitList.append( '-reply-' )

	pathOmitList.append( 'inline-overlay' )
	pathOmitList.append( 'desktop-category-nav' )
	pathOmitList.append( 'a[catnav' )
	pathOmitList.append( ':section[testimonials]:' )
	# pathOmitList.append( ':article[post' )
	pathOmitList.append( '[comments]' )
	pathOmitList.append( ':li[menu-' )
	pathOmitList.append( '-menu]' )
	pathOmitList.append( 'mailchimp' )
	pathOmitList.append( 'menu' )
	pathOmitList.append( 'wrapper' )
	pathOmitList.append( ':symbol[' )

	# pathOmitList.append( '' )

	objOmitList = []
	objOmitList.append( 'Close' )
	objOmitList.append( 'false' )
	objOmitList.append( 'Refresh' )
	objOmitList.append( 'Unmute' )

	objOmitList.append( 'Reply' )
	objOmitList.append( 'Retweet' )
	objOmitList.append( 'Retweeted' )

	objOmitListContains = []
	objOmitListContains.append( ' Twitter' )
	objOmitListContains.append( ' Tweet' )
	objOmitListContains.append( ' retweets' )
	objOmitListContains.append( ' class=\"' )
	objOmitListContains.append( ' class="' )
	objOmitListContains.append( 'Javascript' )
	objOmitListContains.append( 'Plugin' )
	objOmitListContains.append( '(noscript)' )
	objOmitListContains.append( '500.html' )
	objOmitListContains.append( '[if lte IE 9]>' )
	objOmitListContains.append( 'lightbox' )
	objOmitListContains.append( 'navbar' )
	duplicateText = []


def cleanText(string):
	string = string.replace('\t',' ')
	string = string.replace('\n',' ')
	string = string.replace('/',' ')
	string = string.replace('\"',' ')
	string = string.replace('"',' ')
	# string = string.replace('\u2019',"'")
	# string = string.replace('\u2026',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanBE(string,' ')
	return string
########################################################################################
if __name__ == '__main__':
	action()






