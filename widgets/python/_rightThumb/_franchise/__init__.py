import os

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

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
_omit = _.regImp( __.appReg, 'omitTable' )
##################################################
from operator import itemgetter
from lxml import html
import requests
import cssselect
import webbrowser
import datetime
import arrow
import pickle
import webbrowser
##################################################

def appSwitches():
	_.switches.register('Franchise', '-franchise')
	_.switches.register('Stats', '-stats,-stat')
	_.switches.register('MustInclude', '-include')
	_.switches.register('RefineLists', '-lists')
	
	_.switches.register('RawPrint', '-rprint,-raw')
	_.switches.register('Alias', '-alias')
	
	_.switches.register('ListCount', '-l')
	_.switches.register('ListTypes', '-type', 'f m s tv')
	

	_.switches.register('ListTestOnly', '-test')
	_.switches.register('ListRAW', '-rawlist')

	

_.appInfo[focus()] = {
	'file': '_rightThumb._franchise',
	'description': 'Interact with franchise database',
	'categories': [
						'entertainment',
						'threaded',
						'automatic',
						'auto',
						'franchise',
						'imdb',
						'research',
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

_.appInfo[focus()]['examples'].append('Import this into other apps')
# _.appInfo[focus()]['examples'].append('')

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
# START

def extractUrl(string):
	string = string.replace('/url?q=','')

	stringy = string.split('/')
	theLength = len(stringy)
	result = ''
	i = 0
	for segment in stringy:
		i += 1
		if not i == theLength:
			result += segment + '/'
	return result



def lookupMovie( imdbID ):
	global peopleList
	global theListOfMoviesToSave
	url = __.links['imdb']['cinema']['fullcredits'].replace(__.ID_HERE,imdbID)
	if _.switches.isActive('RawPrint'):
		_.colorThis( [  'lookupMovie:', url  ], 'yellow' )
	try:
		url = __.links['imdb']['cinema']['fullcredits'].replace(__.ID_HERE,imdbID)

		page = requests.get(url)
		tree = html.fromstring(page.content)
		movieTitle = tree.cssselect('h3')


		# if _.switches.isActive('MustInclude'):
		#     found = False
		#     for testFor in _.switches.values('MustInclude'):
		#         if testFor.lower() in movieTitle.lower():
		#             found = True
		#     if not found:
		#         raise Exception('Does not include', _.switches.value('MustInclude'))

				
		movieYear = tree.cssselect('.nobr')
		try:
			theYear = cleanupStringYear4(movieYear[0].text_content())
			# theYear = theYear0.split(' ')[0].replace('(','')
			# theYear = theYear.replace(')','')
			# theYear = theYear.replace(' ','')
		except Exception as e:
			theYear = ''
		theTitle = cleanupString(movieTitle[0].text_content())
		theAlist = tree.cssselect('a')
		# theTitle = ''
		found = False
		for ta in theAlist:
			try:
				linkTest =ta.attrib['href']
				if '/title/tt' in linkTest and not found:
					found =True
					theTitle0 = cleanupString(ta.text_content())
					if len(theTitle0) > 1 and not 'External Sites' in theirName0 and not 'Full Cast' in theirName0:
						theTitle = theTitle0
			except Exception as e:
				pass
		
		# for ty in movieYear:
		#     _.pr(cleanupString(ty.text_content(),False))
		theYearThis = theYear
		theTitleThis = theTitle
		img0 = tree.cssselect('img')
		img = ''
		for img1 in img0:
			img2 = img1.attrib['src']
			if '268_AL_.jpg' in img2:
				img = img2


		# pause = input('pause')
		cast = tree.cssselect('.cast_list')
		tr = cast[0].cssselect('tr')
		people = []


		for e in tr:

			# Set 2
			# 
			props = e.cssselect('td')
			# _.pr(len(props))
			try:
				char = props[3].cssselect('.character')
				character = cleanupString(char[0].text_content())
			except Exception as ee:
				try:
					character = props[3].text_content()
				except Exception as eee:
					character = ''

			try:
				person = cleanupString(props[1].text_content())
			except Exception as ee:
				person = ''
			# # character = props[3].text_content()


			
			try:
				links = e.cssselect('a')
				link0 = str(links[0].attrib['href'])
				link = 'http://www.imdb.com' + extractUrl(link0) + '?ref_=ttfc_fc_cl_t13'
				# _.pr(link)
			except Exception as ee:
				link = ''
			if len(link) > 3:
				personID = getIdFromUrl( link )
				peopleList.append( personID )
				people.append({ 'imdbID': personID, 'name': person, 'link': link, 'character': character })


		obj = { 'imdbID': imdbID, 'year': theYear, 'name': theTitle, 'link': url, 'people': people }
		theListOfMoviesToSave.append(obj)
		obj2 = obj
		obj2['people'] = len(obj['people'])
		if _.switches.isActive('RawPrint'):
			_.pr( obj2 )
		# if not type(qID) == bool:
		#     _.threads.spent( qID, sys.getsizeof( str(obj) ) )
	except Exception as e:
		pass
		# _.threads.spent( qID, sys.getsizeof( '' ) )


	pass



def getIdFromUrl(url):
	urls = url.split('/')
	result = urls[4]
	result = result.split('?')[0]
	return result

def cleanupStringYear4(string):
	# string = cleanupString(string)
	string = _str.onlyDigits2(string)
	string = string.replace(' ','')
	return string

def cleanupStringYear3(string):
	string = cleanupString(string)
	# string = _str.onlyDigits(string)
	string = string.replace(' ','')
	return string
def cleanupStringYear2(string):
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanBE(string,' ')

	# _.pr(string)
	# stringTMP = string.split('(')
	# string = stringTMP[2].replace(')','')
	string = _str.onlyDigits2(string)
	# _.pr(string)
	# sys.exit()
	string = string.replace( ' ', '' )
	return string
def cleanupStringYear(string):
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanBE(string,' ')

	# _.pr(string)
	stringTMP = string.split('(')
	string = stringTMP[2].replace(')','')
	# _.pr(string)
	# sys.exit()
	return string
def cleanupString0(string):
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanBE(string,' ')
	string = _str.cleanChar( string )
	return string
def cleanupString(string,beforeAfter=True):
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.cleanFirst(string,' ')
	string = _str.charFix(string)
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
	string = _str.cleanChar( string )
	return string
def cleanupString1(string):
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.cleanFirst(string,' ')
	string = string.replace(_v.slash+'xe2\\x80\\x93','-')
	string = string.replace(_v.slash+'\\xe2\\\\x80\\\\x93','-')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanBE(string,' ')
	string = _str.cleanChar( string )
	return string



def buildUrlList( url, label='', buildUrlListLast={}, buildUrlListDuplicate=[] ):
	info=False
	# global buildUrlListLast
	# global buildUrlListDuplicate
	global dataDump
	# _.pr( url )
	# sys.exit()

	# __.THE_FRANCHISE_TEST

	# if type(label) == tuple and len(label) > 1:
	#     TEST = '_'+label[1].lower()+'_'
	# if type(label) == str:
	#     TEST = '_'+label.lower()+'_'

	# THIS = 'actor,top,like'

	# for testing in THIS.split(','):
	#     if  '_'+testing+'_' in TEST    and    not '_'+testing+'_' in __.THE_FRANCHISE_TEST: return None



	# print( type(label) )
	# print( type(label) )
	# print( type(label) )
	# print( type(label) )
	# print( label )
	# print( label )
	# print( label )
	# print( label )
	# print( label )

	# sys.exit()
	

	if len(label):
		if _.switches.isActive('RawPrint'):
			_.pr( label )
	franchiseList = []
	try:
		page = requests.get(url)
		tree = html.fromstring(page.content)
		# tables = tree.cssselect('#pagecontent')
		# links = tables[0].cssselect('a')
		main = tree.cssselect('#main')
		h3 = main[0].cssselect('h3')
		links = []
		for h in h3:
			ll = h.cssselect('a')
			for l in ll:
				links.append( l )
		if _.switches.isActive('RawPrint'):
			_.pr( 'url:', url )
		# _.pr(links)
		# sys.exit()
	except Exception as e:
		if _.switches.isActive('RawPrint'):
			_.pr('Bad list link (', url, ')' )

	if info:
		try:
			movieTitle = tree.cssselect('h3')
			for item in movieTitle:
				try:
					linksX = item.cssselect('a')
					link = str(linksX[0].attrib['href'])
					movieURL = 'http://www.imdb.com' + extractUrl(link) + 'fullcredits?ref_=tt_cl_sm#cast'
				except Exception as e:
					movieURL = ''
				name = cleanupString0(item.text_content())
				name2 = name.split(' ')
				name = name.replace(name2[0],'')
				name3 = name.split(' (')
				nameFix = cleanupString0(name3[0])

				try:
					year0 = name3[1].split(' ')
					year = year0[0]
					year = year.replace(')','')
				except Exception as e:
					year = ''
				if len(year) > 4:
					year = str(year)
					yearFix = ''
					for dig in year:
						try:
							int(dig)
							yearFix += str(dig)
							isNumber = True
						except Exception as e:
							isNumber = False
							break
					year = yearFix
				elif len(year) < 4:
					year = ''

				bad = ('Activity','Your Friends','Lists by','Viewed','Everywhere','IMDb on','Lists by chantelssecret')
				if not nameFix in bad and not 'Lists by' in nameFix:
					if len(year) > 2:
						if _.switches.isActive('RawPrint'):
							_.pr(year,nameFix)
					else:
						if _.switches.isActive('RawPrint'):
							_.pr('    ',nameFix)
					# if 'TV Movie' in name and duplicateCheck(getIdFromUrl(movieURL)) == False:
					thisID = getIdFromUrl(movieURL)
					if not thisID in buildUrlListDuplicate:
						buildUrlListDuplicate.append(thisID)
						hallmark.append({'id': thisID, 'name': nameFix, 'year': year, 'link': movieURL, 'people': []})
		except Exception as e:
			pass
			# _.pr('Error:',url)
	else:
		iT = 0
		try:
			for l in links:
				try:
					link = str(l.attrib['href'])
					if '/title/' in link:
						thisID = getIdFromUrl('http://www.imdb.com'+link)
						if not thisID in buildUrlListDuplicate:
							buildUrlListDuplicate.append(thisID)
							# if 'tt1375666' in thisID:
							#     _.pr( 'Error:', url )
							#     sys.exit()
							franchiseList.append(thisID)
						iT += 1
				except Exception as e:
					pass
		except Exception as e:
			# _.pr('buildUrlList: for links(a) & franchiseList.append')
			pass
		# _.pr('iT',iT)



	try:
		pageCheck = tree.cssselect('.pagination-range')
		pageCheck2 = cleanupString(pageCheck[0].text_content())
		L = pageCheck2.split('-')[1].split('of')[0]
		E = pageCheck2.split('of')[1]
		if L == E:
			L = '0'
			E = '0'
	except Exception as e:
		# _.pr('buildUrlList: .pagination-range')
		pass



	for l in tree.cssselect('a'):
		try:
			link = str(l.attrib['href'])


			if '/list/' in link and '?page=' in link:
				item0 = link.split('/?page=')[0]
				item = item0.replace('/list/','')
				try:
					buildUrlListLast[item]
				except Exception as e:
					buildUrlListLast[item] = 1
				if '?page=1' in link or buildUrlListLast[item] == int(link.split('?page=')[1]) or buildUrlListLast[item] > int(link.split('?page=')[1]) or L == E :
					actionX = False
				else:
					actionX = True
					buildUrlListLast[item] = int(link.split('?page=')[1])
				if actionX:
					if _.switches.isActive('RawPrint'):
						_.pr('Page:',buildUrlListLast[item])
					# _.pr(link)
					nextPage = 'http://www.imdb.com'+link
					# nextLabel = label+' page X'
					# _.pr( 'next page' )
					# sys.exit()
					if 'http' in nextPage.lower():


						if GOOD_LIST(label): __.asyn.register( name='franchiseList', category='franchiseList', fn=buildUrlList, k={ 'url':nextPage, 'label':label, 'buildUrlListLast':buildUrlListLast, 'buildUrlListDuplicate':buildUrlListDuplicate }, timeout=120 )
						# _.threads.add( 'franchiseList', buildUrlList, [ { 'url':nextPage, 'label':label, 'buildUrlListLast':buildUrlListLast, 'buildUrlListDuplicate':buildUrlListDuplicate } ], pID=qID, kwargs=True )
		except Exception as e:
			pass




	# try:

	#                 # for xx in buildUrlList( ,  ):
	#                     # if 'tt1375666' in xx:
	#                     #     _.pr( 'Error:', url )
	#                     #     sys.exit()
	#                     # franchiseList.append(xx)
	# except Exception as e:
	#     # _.pr('buildUrlList: for links(a) & .pagination-range')
	#     pass

	obj = franchiseList
	if _.switches.isActive('RawPrint'):
		_.pr(len(set(obj)))
	dataDump.append(obj)

	# if not type(obj) == bool:
	#     if _.switches.isActive('Dump'):
	#         __.projectData[focus()]['folder'][   __.pdID[focus()]['folder']  ]['data'].append( obj )
	#     else:
	#         dataDump.append(obj)
	
	# if not type(qID) == bool:
	#     _.threads.spent( qID, sys.getsizeof( str(obj) ) )



def getUrlList( url, find, omit, obscure=False ):
	# _.pr( 'omit:', omit )
	if _.switches.isActive('RawPrint'):
		_.pr( 'url:', url )
	# sys.exit()
	theList = []
	omitWords = [
					'v',
					'iii',
					'in',
					'day',
					'part',
					'two',
					'me',
					'episode',
					'ii',
					'a',
					'to',
					'pm',
					'and',
					'am',
					'of',
					'the'
	]
	newURL = url.replace(',','+').replace(' ','+')
	# _.pr(newURL)
	# brandNewURL = 'http://www.rightthumb.com/projects/widget/proxy.php?p=' + newURL.replace('&','[and]')
	# _.pr(newURL)
	# sys.exit()

	

	page = requests.get(newURL)
	tree = html.fromstring(page.content)
	tables = tree.cssselect('a')
	for t in tables:
		try:
			item = t.text_content()
		except Exception as e:
			item = ''
		# _.pr(item)
		if 'imdb' in item.lower():
			links = t.cssselect('a')
			link = str(links[0].attrib['href'])
			link = link.replace('/url?q=http:','http:')
			text = t.text_content()
			# _.pr(text)
			# _.pr()
			# _.pr(text)


			# pause = input('pause')
			shouldRun = False
			if obscure:
				shouldRun = True
			if not shouldRun:
				
				fNew = find.lower()
				fNew = fNew.replace( '_', ' ' )
				fNewS = fNew.split(' ')
				for fs in fNewS:
					if not fs in omitWords:
						if fs in text.lower():
							shouldRun = True

			if find.lower() in text.lower():
				shouldRun = True
				if len(omit):
					for ox in omit.split( ',' ):
						if ox.lower() in text.lower():
							shouldRun = False

			# _.pr( 'shouldRun:', shouldRun )
			if shouldRun:
				if 'imdb.com/list/' in link:
					theURL = link.replace('/url?q=','').split('/&sa=U')[0]
					if _.switches.isActive('RawPrint'):
						_.pr(theURL)
					if not theURL in __.spentLists:
						__.spentLists[ theURL ] = 1

						text=text.replace('\u203a','')
						text=text.replace('www.imdb.com\\u203a','')
						text=text.replace('www.imdb.com \\u203a','')
						text=text.replace('www.imdb.com','')
						text=text.replace('\\u203a','')
						text=text.replace('\\u203','')
						text=text.replace('\\u20','')
						text=text.replace('\\u2','')
						text=text.replace('\\u','')
						
						theList.append({'name': text,'link': theURL})
	return theList

def action():
	global franID
	global today
	global didResearch


	global franchiseName
	global franchiseList
	global info
	global franchise
	global specifyList

	__.spentIDs = {}
	__.spentLists = {}



	# _.pr( _.switches.isActive('Alias') )
	# _.pr( _.switches.isActive('RawPrint') )
	# sys.exit()

	p=1
	if _.switches.isActive('RawPrint'):
		p=3
	__.asyn.web( 50, safe=3, p=p, pf=1, po=45 )


	if _.switches.isActive('RawPrint'):
		_.pr()
	if _.switches.isActive('Franchise'):
		franchise = franchiseLabel()
	else:
		franchise = input('franchise: ')




	
	__.franchiseFile__saved = False

	if '!!' in franchise:
		forceList = True
	else:
		forceList = False
	if '!' in franchise:
		force = True
	else:
		force = False
	if '?' in franchise:
		obscure = True
	else:
		obscure = False
	franchise = franchise.replace( '?', '' )
	franchise = franchise.replace( '!', '' )
	franchise = franchise.replace( '!', '' )
	franchise = franchise.replace( '!', '' )
	franchise = franchise.lower()
	franchise = franchise.replace( ',', ' ' )
	# franchise = _str.basic(franchise)
	# franchiseName = franchise.replace(' ','_')
	franchiseName = franchise
	__.THE_FRANCHISE_TEST = '_'+franchise.lower()+'_'
	__.franchiseFile = 'imdb-franchises-'+   franchise.upper().replace(' ','_')   +'.json'
	__.franchises = _.getTable(__.franchiseFile)

	_.pr(franchise)

	_.pr()
	_.pr()
	_.pr('Automatic Inteligent Research', franchise.upper(),'...')
	_.pr()
	_.pr()
	# backupJSON( 'imdb_franchises.json' )

	# _.pr(__.franchises[0][franchiseName])
	# _.pr(__.franchises)

	didResearch = False
	franID = inFranchiseID( franchiseName )
	if force:
		_.pr('Force')
		_.pr()
		_.saveTable(__.franchises,__.franchiseFile+'-'+str(time.time()).split('.')[0]+'-'+'.bk')
		startResearch = True
		if not type(franID) == bool:
			__.franchises.pop(franID)
			franID = False
	else:

		if type(franID) == bool:
			startResearch = True
		else:
			startResearch = False

		##########################
		# Add Expiration Here
		##########################


	global smartOmit
	
	
	theList = []

	franchiseSearch = '+'.join(_.switches.values('Franchise'))



	if startResearch:
		didResearch = True

		
		
		# _.pr( 'listExists:', franID )
		# sys.exit()                # _.pr('startResearch')
		# sys.exit()

		# for xx in franID('https://www.google.com/search?q=imdb+'+franchise+'+franchise+movies'):
		
		if not type(franID) == bool and not forceList:
			theList = __.franchises[franID]['list']
		else:
			manualList = False
			listBases = 'https://www.imdb.com/list/THEID/'
			for sl in specifyList.split( ';' ):
				slData = sl.split( ':' )
				if slData[0].lower() == franchise:
					manualList = True
					for slx in slData[1].split( ',' ):
						theList.append({ 'name': franchise + ' - auto list','link': listBases.replace( 'THEID', slx ) })
 
			if not manualList:
				getLists = [
								'franchise',
								'movies',
								'series',
								'tv show',
								'tv',
								'show',
				]

				if _.switches.isActive('ListTypes'):
					getLists = _.switches.values('ListTypes')
					
				listMax = 100
				if _.switches.isActive('ListCount'):
					listMax = int( _.switches.value('ListCount') )
				# _.pr( 'xx', genOmitLink(franchise),franchise,genOmit(franchise), franchiseSearch )

				if 'franchise' in getLists:
					for xx in getUrlList('https://www.google.com/search?q=imdb+list+'+franchiseSearch+'+franchise'+genOmitLink(franchise),franchise,genOmit(franchise), obscure = obscure ):
						if len(theList) < listMax:
							theList.append(xx)
				if 'movies' in getLists:
					for xx in getUrlList('https://www.google.com/search?q=imdb+list+'+franchiseSearch+'+movies'+genOmitLink(franchise),franchise,genOmit(franchise), obscure = obscure ):
						if len(theList) < listMax:
							theList.append(xx)
					for xx in getUrlList('https://www.google.com/search?q='+franchiseSearch+'+movies+'+'imdb+list'+genOmitLink(franchise),franchise,genOmit(franchise), obscure = obscure ):
						if len(theList) < listMax:
							theList.append(xx)
				if 'series' in getLists:
					for xx in getUrlList('https://www.google.com/search?q=imdb+list+'+franchiseSearch+'+series'+genOmitLink(franchise),franchise,genOmit(franchise), obscure = obscure ):
						if len(theList) < listMax:
							theList.append(xx)
				if 'tv show' in getLists or 'tv' in getLists or 'show' in getLists:
					for xx in getUrlList('https://www.google.com/search?q=imdb+list+'+franchiseSearch+'+tv+show'+genOmitLink(franchise),franchise,genOmit(franchise), obscure = obscure ):
						if len(theList) < listMax:
							theList.append(xx)



			# if not len(theList):


			if _.switches.isActive('RawPrint'):
				_.pr( 'theList:', theList )

			franID = len( __.franchises )
			if _.switches.isActive('RawPrint'):
				_.pr()
				_.pr()
				_.pr()
			info = {}
			info['date_acquired'] = time.time()
			info['epoch'] = time.time()
			info['date'] = str(today)
			info['label'] = labelX( franchiseName )
			info['aliases'] = aliases( info['label'] )
			info['parts'] = parts( info['aliases'] )
			info['movieIDS'] = []
			info['peopleIDS'] = []
			info['movies'] = []
			newList = []

			checkName = []
			for cn in _.switches.values('Franchise'):
				checkName.append( cn.lower() )
			for cn in _.switches.values('Alias'):
				checkName.append( cn.lower() )
			
			for ir,rec in enumerate(theList):
				good = False
				for cn in checkName:
					if cn in str(rec).lower():
						good = True
				# if  in rec['name'].lower():
				if good:
					newList.append(rec)
				# newList.append(rec)
			
			info['list'] = newList



			# sys.exit()


			__.franchises.append( info )

			try:
				_.printVar( info )
			except Exception as e:
				if _.switches.isActive('RawPrint'):
					_.pr( info )

			# sys.exit()
			# _.pr( theList )


		newList = cleanList( theList )
		if _.switches.isActive('RawPrint'):
			_.pr('Initiating research on ',len(newList),'items')
		franchiseList = []


		# _.threads.add( 'franchiseList', trigger=franchiseListComplete, loaded=False, database=False ) # kwargs 
		# _.threads.add( 'processMovies', trigger=moviesComplete, loaded=False, database=False ) # kwargs 

		# _.threads.autoLoadedAfter = 3
		# _.threads.maxThreadsSafe = 20
		# _.threads.maxThreads = 20
		__.asyn.atExit( category='franchiseList', name='franchiseList', fn=franchiseListComplete )
		__.asyn.atExit( category='processMovies', name='processMovies', fn=moviesComplete )
		# _.threads.register( 'franchiseList', c=franchiseListComplete )
		# _.threads.register( 'processMovies', c=moviesComplete )
		# _.threads.register( 'franchiseList', c=franchiseListComplete, t=120 )
		# _.threads.register( 'processMovies', c=moviesComplete, t=120 )

		# _.threads.projectDataMaxLen = 200
		# if _.switches.isActive('Stats'):
		#     _.threads.report = True
		#     _.threads.auditPrint = True
		# else:
		#     _.threads.report = False
		#     _.threads.auditPrint = False

		for lnk in newList:
			if _.switches.isActive('RawPrint'):
				_.pr()
				_.pr(lnk)
				_.pr()
			# _.pr(lnk['name'].replace(' - IMDb','').replace('IMDb','').replace('imdb','').replace('IMDB',''))
			# _.pr(lnk['link'].replace('https://www.imdb.com/','').replace('http://www.imdb.com/',''))
			label = lnk['link'].replace('https://www.imdb.com/','').replace('http://www.imdb.com/',''),lnk['name'].replace(' - IMDb','').replace('IMDb','').replace('imdb','').replace('IMDB','')
			# do = buildUrlList( lnk['link'], label )
			
			# webbrowser.open( lnk['link'], new=2)

			if 'http' in lnk['link'].lower():

				# _.threads.add( 'franchiseList', buildUrlList, [ { 'url':lnk['link'], 'label':label } ], kwargs=True )
				if GOOD_LIST(label): __.asyn.register( name='franchiseList', category='franchiseList', fn=buildUrlList, k={ 'url':lnk['link'], 'label':label }, timeout=120 )

			# for xxx in do:
			#     # if 'tt1375666' in xxx:
			#     #     _.pr( 'Error:', xxx )
			#     #     sys.exit()
			#     franchiseList.append(xxx)
			# # try:
			# # except Exception as e:
			# #     _.pr('Error: buildUrlList')

			# break



	else:
		franchiseList = list(set( __.franchises[franID]['movieIDS'] ))
		if _.switches.isActive('RawPrint'):
			_.pr(len(franchiseList))

		report()


def franchiseListComplete():

	# _.pr()
	# _.pr()
	# _.pr()
	# _.pr()
	# _.pr()
	# _.pr('                                     THIS THING WORKS')
	# _.pr()
	# _.pr()
	# _.pr()
	# _.pr()
	# _.pr()
	# _.pr()


	global franID
	global dataDump

	# _.pr( type(dataDump),dataDump )
	# sys.exit()

	newData = []
	for x in dataDump:
		for y in x:
			newData.append(y)

	for fItem in set(newData):
		if not fItem in __.franchises[franID]['movieIDS']:
			__.franchises[franID]['movieIDS'].append( fItem )
	
	# sys.exit()
	if _.switches.isActive('RawPrint'):
		_.pr( 'Processing:', len( __.franchises[franID]['movieIDS'] ) )
	dataDump = []

	for imdbID in __.franchises[franID]['movieIDS']:
		# _.threads.add( 'processMovies', lookupMovie, [ { 'imdbID': imdbID } ], kwargs=True  )
		if not imdbID in __.spentIDs:
			__.spentIDs[imdbID] = 1
			__.asyn.register( name='processMovies', category='processMovies', fn=lookupMovie, k={ 'imdbID': imdbID }, timeout=120 )



def moviesComplete():
	global franID
	global theListOfMoviesToSave
	global peopleList

	__.franchises[franID]['movies'] = theListOfMoviesToSave
	__.franchises[franID]['peopleIDS'] = peopleList

	report()

def report():

	if  __.franchiseFile__saved:
		return None
	__.franchiseFile__saved = True
	global movies
	global people
	global didResearch

	global franchiseName
	global franchiseList
	global info
	global franchise
	global today
	global franID

	fdtl = __.franchises[franID]['date'].split('-')
	foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	td = str(today).split('-')
	tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
	diff = tdd - foundDate
	# _.pr()


	if didResearch:
		if len( __.franchises[franID]['movieIDS'] ):
			_.saveTable(__.franchises,__.franchiseFile)


	# pause = input('pause')
	if __.should_CLS:
		os.system('cls')
	#################################################################################################### MOVIES
	if len(movies):
		_.pr()
		_.pr(info['theirName'], '\t', info['age'])
		_.pr()
		for ix,r in enumerate(movies):
			# record = {'id': iiii, 'name': title, 'year': year, 'link': link, 'img': img, 'age': gigAge}
			# _.pr((r['link']))
			# _.pr(getIdFromUrl(r['link']))
			if getIdFromUrl(r['link']) in franchiseList:
				# _.pr(r['name'])
				movies[ix][franchiseName] = 'x'
			else:
				movies[ix][franchiseName] = ''
		_.tables.register('Auto',movies)
		_.tables.print('Auto','id,year,age,'+franchiseName+',name')
		_.pr()
		_.pr()
		io = 0
		for ix,r in enumerate(movies):
			if getIdFromUrl(r['link']) in franchiseList:
				io += 1
				_.pr(r['year'],r['name'])
		_.pr()
		if io > 0:
			_.pr(io)

		if io == 0:


			try:
				__.franchises[2][franchiseName]
				moreData = True
			except Exception as e:
				moreData = False

			if moreData:
				try:
					if thisPersonID in  __.franchises[1][franchiseName]:
						moreData = True
					else:
						moreData = False
				except Exception as e:
					moreData = False



			if moreData:
				_.pr('None of these items are',franchiseName)

				_.pr()
				_.pr('')
				_.pr()
				_.pr('However, they are noted in:')
				for fdai,fda in enumerate(__.franchises[2][franchiseName]):
					if thisPersonID in  __.franchises[2][franchiseName][fdai]['people']:
						_.pr('\t\t\t\t',__.franchises[2][franchiseName][fdai]['year'],__.franchises[2][franchiseName][fdai]['title'])
				_.pr()
				_.pr()
				_.pr()
				_.pr()
	#################################################################################################### MOVIES

	_.pr()
	_.pr()
	try:
		ppl = _.addComma(len(set( __.franchises[franID]['peopleIDS'] ))) + ' people\t\t'
	except Exception as e:
		ppl = ''
	try:
		mv = _.addComma(len(set( __.franchises[franID]['movieIDS'] ))) + ' movies\t\t'
	except Exception as e:
		mv = ''
	_.pr('_____________________________________________________________________________________________________________________')
	_.pr(franchise.upper(), '\t\t',ppl,mv,__.franchises[franID]['date'],'\t\t',str(diff.days),'days')
	_.pr()
	_.pr()

		###################################################################################################    



def inFranchiseID( test ):
	test = test.lower()
	test = test.replace( ',', ' ' )
	test = test.replace( '_', ' ' )
	test = _str.cleanBE( test, ' ' )
	# _.pr( 'test:', test )
	for i,franchise in enumerate(__.franchises):

		if franchise['label'].lower() == test.lower():
			return i


		for alias in franchise['aliases']:
			# _.pr( test, alias )
			if alias == test:
				return i
		if ' ' in test:
			cnt = 0
			for part in franchise['parts']:
				for t in test.split( ' ' ):
					if part in t:
						cnt += 1
			if cnt > 1:
				ask = ''
				ask = input( franchise['label']+'? (y): ' )
				if not ask == 'n':
					__.franchises[i]['aliases'].append( test )
					_.saveTable(__.franchises,__.franchiseFile)
					return i
	for i,franchise in enumerate(__.franchises):
		for alias in franchise['aliases']:
			if alias in test:
				ask = input( franchise['label']+'? (y): ' )
				if not ask == 'n':
					__.franchises[i]['aliases'].append( test )
					_.saveTable(__.franchises,__.franchiseFile)
					return i
		if ' ' in test:
			for part in franchise['parts']:
				if not _omit.imp.inTable( part ):
					for t in test.split( ' ' ):
						if part in t:
							ask = ''
							ask = input( franchise['label']+'? (y): ' )
							if not ask == 'n':
								__.franchises[i]['aliases'].append( test )
								_.saveTable(__.franchises,__.franchiseFile)
								return i
	return False


# def inFranchise( test ):
#     for i,franchise in enumerate(__.franchises):
#         for alias in franchise['aliases']:
#             if alias in test:
#                 return i
#         if ' ' in test:
#             cnt = 0
#             for part in franchise['parts']:
#                 for t in test.split( ' ' ):
#                     if part in t:
#                         cnt += 1
#             if cnt > 1:
#                 ask = ''
#                 ask = input( franchise['label']+'? (y): ' )
#                 if not ask == 'n':
#                     __.franchises[i]['aliases'].append( ask )
#                     _.saveTable(__.franchises,__.franchiseFile)
#                     return i
#     return False

def aliases( data ):
	results = []
	results.append( data )
	if _.switches.isActive('Franchise'):
		add = ''
	else:
		add = input( 'Aliases for '+data+' (,): ' )
	for x in add.split(','):
		x = _str.replaceDuplicate( x, ' ' )
		x = _str.cleanBE( x, ' ' )
		if len( x ):
			results.append( s )
	return results

def parts( data ):
	results = []
	for d in data:
		for x in d.split(' '):
			results.append( x )
	return results

def labelX( data ):
	if _.switches.isActive('Franchise'):
		x = ''
	else:
		x = input('Label other than '+data+': ')
		x = _str.replaceDuplicate( x, ' ' )
		x = _str.cleanBE( x, ' ' )
	if len(x):
		data = x
	return data

def cleanList( data ):
	results = []
	newResults = []

	for d in data:
		results.append( d['link'] )

	resultsX = list(set( results ))

	for r in resultsX:
		for d in data:
			if r in d['link']:
				newResults.append( d )


	# _.pr( len(newResults) )
	# sys.exit()
	return newResults

def franchiseLabel():
	if _.switches.isActive('Alias'):
		franchise = _.ci( _.switches.value('Alias') )
	else:
		franchise = _.ci( _.switches.value('Franchise') )
	franchise = franchise.replace( ',', ' ' )
	franchise = franchise.replace( '_', ' ' )
	franchise = _str.replaceDuplicate( franchise, ' ')
	franchise = _str.cleanBE( franchise, ' ')
	return franchise


def printFranchise():
	franchise = franchiseLabel()
	franID = inFranchiseID( franchise )

	# for movie in __.franchises[franID]['movies']:
		# _.pr( movie['imdbID'], movie['year'], movie['name'], movie['link'] )

	_.switches.fieldSet( 'Long', 'active', True )
	_.tables.returnSorted( 'data', 'd.year', __.franchises[franID]['movies'] )
	# _.tables.register('data',__.franchises[franID]['movies'])
	_.tables.print( 'data', 'imdbID,year,name,link' )

def genOmit( franchise ):
	global smartOmit
	franchise = franchise.lower()
	smartOmit = smartOmit.lower()

	for record in smartOmit.split( ';' ):
		data = record.split( ':' )
		if franchise == data[0]:
			return data[1]
	return ''

def genOmitLink( franchise ):
	global smartOmit
	franchise = franchise.lower()
	smartOmit = smartOmit.lower()
	found = False
	result = ''
	for record in smartOmit.split( ';' ):
		data = record.split( ':' )
		if franchise == data[0]:
			found = True
			for omit in data[1].split( ',' ):
				result += '+-"' + omit.replace( ' ', '+' ) + '"'
	if found:
		return result
	else:
		return ''


def GOOD_LIST(label):

	if _.switches.isActive('ListRAW'): return True


	TEST='error, mf'
	if type(label) == tuple and len(label) > 1:
		TEST = '_'+label[1].lower()+'_'
	elif type(label) == str:
		TEST = '_'+label.lower()+'_'

	TEST=TEST.replace( ' ', '_')

	THIS = 'actor,top,like,type'

	GOOD = True

	for testing in THIS.split(','):
		if  '_'+testing+'_' in TEST      and      not '_'+testing+'_' in __.THE_FRANCHISE_TEST:   GOOD = False

	if _.switches.isActive('ListTestOnly')  or   _.switches.isActive('RawPrint'):        
		if GOOD:
			_.pr(GOOD, TEST  , c='Background.green')
		else:
			_.pr(GOOD, TEST  , c='Background.red')

	if _.switches.isActive('ListTestOnly'): return False
	return GOOD


dataDump = []
theListOfMoviesToSave = []

franID = False
smartOmit = 'dc:marvel,stan lee;marvel:dc;spiderman:avengers,captain america;captain america:thor;thor:avengers;batman:justice league,superman;superman:justice league,batman'
specifyList = 'wolverine:ls069189182'
movies = []
people = []
info = {}
# __.franchiseFile = 'imdb-franchises-'+  '_'.join( _.switches.values('Franchise') )  +'.json'
__.franchisesName = _.getTable( 'imdb_franchise_display.json' )
partOmit = [ 'to', 'the', 'a', 's', 'p', 'm', 'of', 'and' ]
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
didResearch = False
peopleList = []
franchiseName = ''
franchiseList = []
franchise = ''
__.ID_HERE = '*THEID*'
__.links = {
				'imdb': {
					'cinema': {
						'fullcredits': 'http://www.imdb.com/title/' + __.ID_HERE + '/fullcredits?ref_=tt_cl_sm#cast',
						'writers': 'https://www.imdb.com/title/' + __.ID_HERE + '/fullcredits?ref_=tt_ov_wr#writers/',
						'parentalguide': 'http://www.imdb.com/title/' + __.ID_HERE + '/parentalguide',
						'ratings': 'http://www.imdb.com/title/' + __.ID_HERE + '/ratings',
						'season': 'http://www.imdb.com/title/' + __.ID_HERE + '/episodes?season=THESEASON&ref_=tt_eps_sn_1',
					},
					'people': {
						'profile': 'https://www.imdb.com/name/' + __.ID_HERE + '/?ref_=ttfc_fc_cl_t13',
						'bio': 'https://www.imdb.com/name/' + __.ID_HERE + '/bio?ref_=nm_ov_bio_sm',
					},
				},
				'rottentomatoes': {}
			}


_async = _.regImp( __.appReg, '_rightThumb._asynchronous' )



__.should_CLS = False
########################################################################################
if __name__ == '__main__':
	action()

# buildUrlList,
	# Bad list link ( 4 )







