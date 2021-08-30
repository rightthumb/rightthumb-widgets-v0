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

# https://www.rottentomatoes.com/m/bird_box
# Rating:	R (for violence, bloody images, language and brief sexuality)
# Genre:	Drama, Mystery & Suspense, Science Fiction & Fantasy
# Directed By:	Susanne Bier
# Written By:	Eric Heisserer
# In Theaters:	Dec 13, 2018  Limited
# On Disc/Streaming:	Dec 21, 2018
# Runtime:	117 minutes
# Studio:	Netflix

# add: https://www.imdb.com/title/tt1248542/fullcredits?ref_=tt_ov_wr#writers/

# add to franchise NOT replace

# type imdb.py | p line + franchiseName -ln - #
# type imdb.py | p line + franchiseNameList -ln - #

import os
import sys
import simplejson as json

import _rightThumb._construct as __
__.appReg = __name__
import _rightThumb._base2 as _


import _rightThumb._vars as _v
import _rightThumb._string as _str

from operator import itemgetter

from lxml import html
import requests
import cssselect

import webbrowser
import time

import datetime
import arrow

import pickle

_.switches.register('Movie', '-movie,-ent,-entertainment')
_.switches.register('Person', '-person')
_.switches.register('Single', '-single')
_.switches.register('Hallmark', '-hallmark','buildPeople')
_.switches.register('HallmarkView', '-view')
_.switches.register('BuildCrossRef', '-xref')
_.switches.register('HallmarkCrossRef', '-hx,-hallmarkxref')
_.switches.register('KevinBacon', '-kevinbacon','build')
_.switches.register('KevinBaconPickUp', '-kbpickup')
_.switches.register('NoPrint', '-noprint')
_.switches.register('Ask', '-ask')
_.switches.register('QuickInfo', '-qi')
_.switches.register('Score', '-score')
_.switches.register('Episode', '-ep,-episode')
_.switches.register('SeasonStarts', '-ss,-seasonstarts','"16 July 2017" dmy')

_.switches.register('ObjectsLoadSkip', '-skipload')

_.switches.register('Case', '-case','tt0436992 , nm2092886, tt0088763')

_.switches.register('Location', '-location','movie_drive, cloud_drive')
_.switches.register('Watched', '-watched','2d, 2w, 1y, 6m, ( or leave blank )')

_.switches.register('Label', '-label')
_.switches.register('MovieFile', '-mfile')

_.switches.trigger('Watched', _.txt2Date)

_.columnTab = ' '
_.appInfo[__name__]=	{
	'file': 'imdb.py',
	'description': 'Lookup movies, shows, and people on imdb',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}
_.appData[__name__]=	{
	'var': '',
	'pipe': [],
	}
_.appInfo[__name__]['examples'].append('p imdb -ent Terminator 2')
_.appInfo[__name__]['examples'].append('p imdb -person Jim Caviezel')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -person lucy lu -ent hackers -xref one')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -entertainment when calls the heart and stargate atlantis -xref')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -person Elisabeth Shue -kevinbacon')
_.appInfo[__name__]['examples'].append('p imdb -person kevin bacon -kevinbacon build -kbpickup')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -hallmark + the sweetest heart')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -hallmark buildPeople')
_.appInfo[__name__]['examples'].append('')
# _.appInfo[__name__]['examples'].append('p dir -cache Movie_Drive.dirCache -c n --c -size g 700mb - downloaded + 2017|p line --c -p ( 0 | p line --c -p . 0 -u |p line --c -make "p imdb -qi -ent {}"|p execute > %tmpf2%')
_.appInfo[__name__]['examples'].append('type List_of_movies.txt | p imdb -case -ent -score | p line -u --c | sort | p line ')
_.appInfo[__name__]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies + 2018 | p movieTitle | p imdb -case -ent -score | p line -u --c | sort | p line ')
_.appInfo[__name__]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies + 2018 | p movieTitle | p imdb -case -ent -score | p line -u --c | sort | p line ')
_.appInfo[__name__]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies -ago 2w | p movieTitle | p imdb -case -ent -score | p line -u --c | sort | p line ')
_.appInfo[__name__]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies -ago 2w | p movieTitle | p line --c -make "p imdb -score -qi -ent {}" | p execute --c | sort | p line')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -ent unleashing mr darcy and Marrying Mr Darcy -xref')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -c n --c + 201 | p movieTitle | p line + 2016 --c | p line --c -make "p imdb -score -qi -ent {}" | p execute --c | sort | p line')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies -ago 2w | p movieTitle | p line --c -make "p imdb -score -qi -ent {}" | p execute --c | sort | p line')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -ent castle -episode 5:21')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -ent full house and family matters -xref -episode')
_.appInfo[__name__]['examples'].append('p imdb -ent chicago med and chicago fire and chicago pd -xref -episode')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -hallmark + The Nine Lives of Christmas -view')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -case -ent doctor  who -ss "16 July 2020" dmy')
_.appInfo[__name__]['examples'].append('p imdb -case -ent doctor  who -ss 0')
_.appInfo[__name__]['examples'].append('p imdb -case -ent doctor  who -seasonstarts 2020-07-16')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p imdb -case -ent smallville -ep')
_.appInfo[__name__]['examples'].append('')




if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True


_.switches.process()

appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f

def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeDataSingle(data):
	__.pipeData = []
	__.pipeData.append(data)
	_.appData[__name__]['pipe'] = []
	_.appData[__name__]['pipe'].append(data)

def setPipeData(data):
	__.pipeData = list(data)
	_.appData[__name__]['pipe'] = list(data)


########################################################################################
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

def registerPerson(people,person,link,character,img=''):
	global hallmark
	global iHallmark
	if _.switches.isActive('HallmarkCrossRef') == True:
		if len(hallmark) < 1:
			hallmark = _.getTable('hallmark.json')
	found = False
	for r in people:
		if r['name'] == person:
			found = True
	if not found:
		cnt = len(people)
		if _.switches.isActive('HallmarkCrossRef') == True:
			foundHallmark = ''
			for hm in hallmark:
				for hmp in hm['people']:
					if hmp['name'] == person:
						foundHallmark = 'H'
		if _.switches.isActive('HallmarkCrossRef') == True:
			if len(foundHallmark) > 0:
				iHallmark += 1
			record = {'id': cnt,'name': person,'character': character,'link': link,'img': img,'hallmark': foundHallmark}
		else:
			record = {'id': cnt,'name': person,'character': character,'link': link,'img': img}
		people.append(record)
		# print(people)
		# pause = input('pause')
	return people
##########################################################################################
##########################################################################################
##########################################################################################
def getUrlList( url, find, omit, obscure=False ):
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
	# print(newURL)
	# brandNewURL = 'http://www.rightthumb.com/projects/widget/proxy.php?p=' + newURL.replace('&','[and]')
	# print(newURL)
	# sys.exit()
	page = requests.get(newURL)
	tree = html.fromstring(page.content)
	tables = tree.cssselect('.r')
	for t in tables:
		try:
			item = t.text_content()
		except Exception as e:
			item = ''
		if 'imdb' in item.lower():
			links = t.cssselect('a')
			link = str(links[0].attrib['href'])
			link = link.replace('/url?q=http:','http:')
			text = t.text_content()
			# print(text)
			print()
			print(text)


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

			if find.lower() in text.lower() and  not omit.lower() in text.lower():
				shouldRun = True
			print( 'shouldRun:', shouldRun )
			if shouldRun:
				if 'imdb.com/list/' in link:
					theURL = link.replace('/url?q=','').split('/&sa=U')[0]
					print(theURL)
					theList.append({'name': text,'link': theURL})
	return theList
buildUrlListLast = {}
buildUrlListDuplicate = []
def buildUrlList(url,info=False):
	global buildUrlListLast
	global buildUrlListDuplicate
	# print( url )
	# sys.exit()
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
		print( 'url:', url )
	except Exception as e:
		print('Bad list link')

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
						print(year,nameFix)
					else:
						print('    ',nameFix)
					# if 'TV Movie' in name and duplicateCheck(getIdFromUrl(movieURL)) == False:
					thisID = getIdFromUrl(movieURL)
					if not thisID in buildUrlListDuplicate:
						buildUrlListDuplicate.append(thisID)
						hallmark.append({'id': thisID, 'name': nameFix, 'year': year, 'link': movieURL, 'people': []})
		except Exception as e:
			pass
			# print('Error:',url)
	else:
		iT = 0
		try:
			for l in links:
				link = str(l.attrib['href'])
				if '/title/' in link:
					thisID = getIdFromUrl('http://www.imdb.com'+link)
					if not thisID in buildUrlListDuplicate:
						buildUrlListDuplicate.append(thisID)
						# if 'tt1375666' in thisID:
						# 	print( 'Error:', url )
						# 	sys.exit()
						franchiseList.append(thisID)
					iT += 1
		except Exception as e:
			# print('buildUrlList: for links(a) & franchiseList.append')
			pass
		# print('iT',iT)



	try:
		pageCheck = tree.cssselect('.pagination-range')
		pageCheck2 = cleanupString(pageCheck[0].text_content())
		L = pageCheck2.split('-')[1].split('of')[0]
		E = pageCheck2.split('of')[1]
		if L == E:
			L = '0'
			E = '0'
	except Exception as e:
		# print('buildUrlList: .pagination-range')
		pass
	try:
		for l in links:
			link = str(l.attrib['href'])


			if '/list/' in link and '?page=' in link:
				item0 = link.split('/?page=')[0]
				item = item0.replace('/list/','')
				try:
					buildUrlListLast[item]
				except Exception as e:
					buildUrlListLast[item] = 1
				if '?page=1' in link or buildUrlListLast[item] == int(link.split('?page=')[1]) or buildUrlListLast[item] > int(link.split('?page=')[1]) or L == E :
					action = False
				else:
					action = True
					buildUrlListLast[item] = int(link.split('?page=')[1])
				if action:
					print('Page:',buildUrlListLast[item])
					# print(link)
					for xx in buildUrlList('http://www.imdb.com'+link,info):
						# if 'tt1375666' in xx:
						# 	print( 'Error:', url )
						# 	sys.exit()
						franchiseList.append(xx)
	except Exception as e:
		# print('buildUrlList: for links(a) & .pagination-range')
		pass
	if info:
		result = hallmark
	else:
		result = franchiseList

	return result
##########################################################################################
##########################################################################################
##########################################################################################
def lookupPerson(url):
	idRegistier(url)
	thisPersonID = getIdFromUrl(url)
	if _.switches.isActive('NoPrint') == False:
		pass
		os.system('cls')
	# print(url)
	# pause = input('pause')
	global hallmark
	# print(url)
	page = requests.get(url)
	tree = html.fromstring(page.content)
	films = tree.cssselect('.filmo-category-section')
	
	movies = []

	personName = tree.cssselect('h1')
	try:
		birthDate0 = tree.cssselect('#name-born-info')
		birthDate1 = birthDate0[0].cssselect('a')
		try:
			birthDate = cleanupString(birthDate1[0].text_content())
		except Exception as e:
			birthDate = ''
		try:
			birthYear = cleanupString(birthDate1[1].text_content())
		except Exception as e:
			birthYear = ''
		try:
			birthLocation = cleanupString(birthDate1[2].text_content())
		except Exception as e:
			birthLocation = ''

		if not len(birthYear) == 4:
			for bd in birthDate1:
				d = cleanupString(bd.text_content())
				try:
					test = int(d)
				except Exception as e:
					test = 0
				if test > 1900:
					birthYear = d

		
		year, month, day, hour, minute = time.strftime("%Y,%m,%d,%H,%M").split(',')
		age = int(year) - int(birthYear)
	except Exception as e:
		age = ''

	# print(birthDate)
	# print(birthYear)
	# print(birthLocation)
	img0 = tree.cssselect('img')
	img = ''
	for img1 in img0:
		img2 = img1.attrib['src']
		if '317_AL_.jpg' in img2:
			img = img2
	for pn in personName:
		theirName0 = cleanupString(pn.text_content())
		if len(theirName0) > 0:
			theirName = theirName0
			print('Processing', theirName,'...')
	# pause = input('pause')
	if _.switches.isActive('Hallmark') == True:
		if len(hallmark) < 1:
			buildHallmarkTable()
	def ageAtTheTime(gigYear):
		gigAge = ''
		if '-' in gigYear:
			gigYearSplit = gigYear.split('-')
			gigAge = str(ageAtTheTime(gigYearSplit[0])) + '-' + str(ageAtTheTime(gigYearSplit[1]))
		else:
			if int(birthYear) > 0 and int(gigYear) > 0:
				gigAge = int(gigYear) - int(birthYear)
		return gigAge

	j = 0
	i = 0
	iHallmark = 0
	for f in films:
		iii = 0
		iiii = 0
		j += 1
		for ff in f.getchildren():
			ii = 0
			for chillin in ff.getchildren():
				if ii == 1:
					title = cleanupString(chillin.text_content())
					links = chillin.cssselect('a')
					link0 = str(links[0].attrib['href'])
					link = 'http://www.imdb.com' + extractUrl(link0) + 'fullcredits?ref_=tt_cl_sm#cast'
					thisID = getIdFromUrl(link)
					year0 = ff.cssselect('.year_column')
					year1 = year0[0].text_content()
					year = cleanupString(year1)
					try:
						gigAge = ageAtTheTime(year)
					except Exception as e:
						pass
						# print(e)
						# sys.exit()
						gigAge = ''
					if j == 1:
						if _.switches.isActive('HallmarkCrossRef') == True:
							hallmarkData = isHallmark(thisID)
							if len(hallmarkData) > 0:
								iHallmark += 1
							record = {'id': iiii, 'name': title, 'year': year, 'link': link, 'img': img, 'hallmark': hallmarkData, 'age': gigAge}
						else:
							record = {'id': iiii, 'name': title, 'year': year, 'link': link, 'img': img, 'age': gigAge}
						movies.append(record)
					iiii += 1
				ii += 1
			iii += 1
		i += 1
	if _.switches.isActive('NoPrint') == False:
		os.system('cls')
		print()
		print(theirName, '\t', age)
		print()
	if _.switches.isActive('NoPrint') == False:
		_.switches.fieldSet('Long','active',True)
		_.switches.fieldSet('Long','value','name')
		if _.switches.isActive('HallmarkCrossRef') == True:
			_.tables.register('Auto',movies)
			_.tables.print('Auto','id,hallmark,year,name')
			print()
			print('    ',iHallmark,'Hallmark')
		else:
			_.tables.register('Auto',movies)
			_.tables.print('Auto','id,year,age,name')
	if _.switches.isActive('BuildCrossRef') == True:
		buildMovies(movies,{'name': theirName, 'url': url})
		theRows = []
		theRows.append({'name': theirName, 'link': url})
		buildPeople(theRows)
		# print()
	# print(birthDate)


	def makeSelection():
		# lookupPerson(url):
		print()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 'h' or selection == '?' or selection == 'help':
			print('id')
			print('(b)io')
			print('(s)earch')
			print('xref')
			print('l','url')
			print('(p)ic')
			print('e(x)it')
			print('description contains (dc)')
			print('show all descriptions (sd)')
			print('save')
			print('(f)ranchise')
			print('search results (sr)')
		if selection == 'sr':
			print()
			sr = input('Search for - ')
			searchResults = []
			for m in movies:
				if sr.lower() in m['name'].lower():
					searchResults.append(m)
			print()
			_.tables.register('searchResults',searchResults)
			_.tables.print('searchResults','id,year,name')
		if selection == 'f':
			print()
			franchise = input('franchise: ')
			if '!' in franchise:
				force = True
			else:
				force = False
			if '?' in franchise:
				obscure = True
			else:
				obscure = False
			franchise = franchise.replace( '?', '' )
			franchise = franchise.lower()
			franchise = _str.basic(franchise)
			franchiseName = franchise.replace(' ','_')
			franchiseNameList = franchise + '_list'
			franchiseDate = franchiseName + '_date'
			print(franchise)
			now = datetime.datetime.now()
			today = now.strftime("%Y-%m-%d")
			print()
			print()
			print('Automatic Inteligent Research', franchise.upper(),'...')
			print()
			print()
			franchiseFile = 'imdb_franchises.json'
			franchiseData = _.getTable(franchiseFile)
			# print(franchiseData[0][franchiseName])
			# print(franchiseData)

			didResearch = False

			if force:
				print('Force')
				print()
				startResearch = True
			else:
				try:
					found = False
					if len(franchiseData[0][franchiseDate]) > 0:
						found = True
						fdtl = franchiseData[0][franchiseDate].split('-')
						foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
						td = str(today).split('-')
						tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
						diff = tdd - foundDate
						# print(diff.days)
					
					global franchiseDaysMax

					if found:
						if int(diff.days) > franchiseDaysMax:
							startResearch = True
						else:
							startResearch = False
					else:
						startResearch = True
				except Exception as e:
					# print('Error')
					startResearch = True







			global smartOmit
			
			
			theList = []
			for sol in smartOmit.split(';'):
				so = sol.split(',')

				if franchise.lower() == so[0].lower():
					franchiseSearch = so[0] + '+-' + so[1]
					franchiseOmit = so[1]
				else:
					franchiseSearch = franchise
					franchiseOmit = ''





			if startResearch:
				didResearch = True
				try:
					franchiseData[0][franchiseNameList]
					if len(franchiseData[0][franchiseNameList]) > 0:
						listExists = True
					else:
						listExists = False
				except Exception as e:
					listExists = False
				print( 'listExists:', listExists )
				sys.exit()				# print('startResearch')
				# sys.exit()

				# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+franchise+movies'):
				if listExists:
					theList = franchiseData[0][franchiseNameList]
				else:
					for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchiseSearch+'+movies',franchise,franchiseOmit, obscure = obscure ):
						theList.append(xx)
					for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchiseSearch+'+series',franchise,franchiseOmit, obscure = obscure ):
						theList.append(xx)
					for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchiseSearch+'+tv+show',franchise,franchiseOmit, obscure = obscure ):
						theList.append(xx)
					franchiseData[0][franchiseNameList] = list(set(theList))
					# for x in xx
				# print(theList)



				print('Initiating research on ',len(theList),'items')
				franchiseList = []
				for lnk in theList:
					print()
					print()
					# print(lnk['name'].replace(' - IMDb','').replace('IMDb','').replace('imdb','').replace('IMDB',''))
					# print(lnk['link'].replace('https://www.imdb.com/','').replace('http://www.imdb.com/',''))
					print(lnk['link'].replace('https://www.imdb.com/','').replace('http://www.imdb.com/',''),lnk['name'].replace(' - IMDb','').replace('IMDb','').replace('imdb','').replace('IMDB',''))
					do = buildUrlList(lnk['link'])
					print(len(set(do)))
					for xxx in do:
						# if 'tt1375666' in xxx:
						# 	print( 'Error:', xxx )
						# 	sys.exit()
						franchiseList.append(xxx)
					# try:
					# except Exception as e:
					# 	print('Error: buildUrlList')


				try:
					franchiseData[0][franchiseName][0]
				except Exception as e:
					franchiseData[0][franchiseName] = []

				try:
					for fItem in set(franchiseList):
						if not fItem in franchiseData[0][franchiseName]:
							franchiseData[0][franchiseName].append( fItem )
					# franchiseData[0][franchiseName] = list(set(franchiseList))
				except Exception as e:
					franchiseData.append({franchiseName: franchiseList})
				try:
					franchiseData[0][franchiseDate] = str(today)
				except Exception as e:
					franchiseData[0] = {franchiseDate: str(today)}

			else:
				franchiseList = list(set(franchiseData[0][franchiseName]))
				print(len(franchiseList))
				# pause = input('pause')
				# for fd in franchiseData:
				# 	if len(fd[franchiseName]) > 0:
				# 		franchiseList = list(set(fd[franchiseName]))






			# print('franchiseList',franchiseList)
			# pause = input('pause')
			fdtl = franchiseData[0][franchiseDate].split('-')
			foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
			td = str(today).split('-')
			tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
			diff = tdd - foundDate
			# print()


			if didResearch:
				if len( franchiseData[0][franchiseName] ):
					print()
					print()
					print(franchiseName.replace( '_', ' ' ).title())
					alias = input('Alias: ')
					_.saveTable(franchiseData,franchiseFile)

					if len( alias ):
						alias = _str.replaceDuplicate(alias,' ')
						alias = _str.cleanBE(alias,' ')
						if len( alias ):
							franchiseDataDisplay = _.getTable( 'imdb_franchise_display.json' )
							franchiseDataDisplay.append( { 'actual': franchiseName, 'proper': alias } )
							_.saveTable( franchiseDataDisplay, 'imdb_franchise_display.json' )
			# pause = input('pause')
			os.system('cls')
			print()
			print(theirName, '\t', age)
			print()
			
			for ix,r in enumerate(movies):
				# record = {'id': iiii, 'name': title, 'year': year, 'link': link, 'img': img, 'age': gigAge}
				# print((r['link']))
				# print(getIdFromUrl(r['link']))
				if getIdFromUrl(r['link']) in franchiseList:
					# print(r['name'])
					movies[ix][franchiseName] = 'x'
				else:
					movies[ix][franchiseName] = ''
			_.tables.register('Auto',movies)
			_.tables.print('Auto','id,year,age,'+franchiseName+',name')
			print()
			print()
			io = 0
			for ix,r in enumerate(movies):
				if getIdFromUrl(r['link']) in franchiseList:
					io += 1
					print(r['year'],r['name'])
			print()
			if io > 0:
				print(io)

			if io == 0:


				try:
					franchiseData[2][franchiseName]
					moreData = True
				except Exception as e:
					moreData = False

				if moreData:
					try:
						if thisPersonID in  franchiseData[1][franchiseName]:
							moreData = True
						else:
							moreData = False
					except Exception as e:
						moreData = False



				if moreData:
					print('None of these items are',franchiseName)

					print()
					print('')
					print()
					print('However, they are noted in:')
					for fdai,fda in enumerate(franchiseData[2][franchiseName]):
						if thisPersonID in  franchiseData[2][franchiseName][fdai]['people']:
							print('\t\t\t\t',franchiseData[2][franchiseName][fdai]['year'],franchiseData[2][franchiseName][fdai]['title'])
					print()
					print()
					print()
					print()


			print()
			print()
			try:
				ppl = str(len(set(franchiseData[1][franchiseName]))) + ' people\t\t'
			except Exception as e:
				ppl = ''
			try:
				mv = str(len(set(franchiseData[0][franchiseName]))) + ' movies\t\t'
			except Exception as e:
				mv = ''
			print('_____________________________________________________________________________________________________________________')
			print(franchise.upper(),len(set(franchiseList)),'\t\t',ppl,mv,franchiseData[1][franchiseDate],'\t\t',str(diff.days),'days')
			print()
			print()

		###################################################################################################	
		if selection == 'sd':
			i = 0
			for m in movies:
				i += 1
				status = str(i) + ' of ' +  str(len(movies))
				_.updateLine(status)
				try:
				    tempXX = m['description']
				    hasDescription = True
				except KeyError:
				    hasDescription = False
				if hasDescription:
					description = m['description']
				else:
					newURL = 'http://www.imdb.com/title/' + getIdFromUrl(m['link']) + '/?ref_=ttfc_fc_tt'
					# print(newURL)
					page = requests.get(newURL)
					tree = html.fromstring(page.content)
					description0 = tree.cssselect('.summary_text')
					description1 = description0[0].text_content()
					description = cleanupString(description1)
					movies[i-1]['description'] = description
				_.updateLine('')
			print('')
			for m in movies:
				if len(m['year']) > 1:
					theTitle = str(m['id']) + '\t' + m['name'] + ' (' + m['year'] + ')'
				else:
					theTitle = str(m['id']) + '\t' + m['name']
				print('_______________________________________________')
				print('')
				print(theTitle)
				print(m['description'])




		if selection == 'dc':
			lookFor = input('description contains:  ')
			lookFor = lookFor.lower()
			allDC = input('show all:  ')
			if len(allDC) == 0:
				allDC = False
			elif 'y' in allDC.lower():
				allDC = True
			else:
				allDC = False


			lookFor = lookFor.lower()
			lfAnd = False
			lfOr = False

			if ' or ' in lookFor:
				lfOr = True

			if ' and ' in lookFor:
				lfAnd = True


			dcResult = []
			i = 0
			done = False
			for m in movies:
				i += 1
				status = str(i) + ' of ' +  str(len(movies))
				_.updateLine(status)
				try:
				    tempXX = m['description']
				    hasDescription = True
				except KeyError:
				    hasDescription = False
				if hasDescription:
					description = m['description']
					description = description.replace('at this time','')
				else:
					newURL = 'http://www.imdb.com/title/' + getIdFromUrl(m['link']) + '/?ref_=ttfc_fc_tt'
					# print(newURL)
					page = requests.get(newURL)
					tree = html.fromstring(page.content)
					description0 = tree.cssselect('.summary_text')
					description1 = description0[0].text_content()
					description = cleanupString(description1)
					movies[i-1]['description'] = description
					description = description.replace('at this time','')
					# print("",lookFor,description.lower())
					if not allDC:
					# print(allDC)
					# sys.exit()
						if lookFor in description.lower():
							_.updateLine("")
							print()
							print()
							print(m['name'])
							done = True
							break
							sys.exit()

					# sys.exit()
				if done:
					sys.exit()
				if lfOr and lfAnd:
					print('')
					print('')
					print('Error: and or, pick one')
					sys.exit()
				if not lfOr and  not lfAnd:
					if lookFor in description:
						# print('single')
						if len(m['year']) > 1:
							dcResult.append(str(m['id']) + '\t' + m['name'] + ' (' + m['year'] + ')')
						else:
							dcResult.append(str(m['id']) + '\t' + m['name'])
				if lfOr:
					fci = 0
					for orX in lookFor.split(' or '):
						if orX in description:
							fci += 1
					if fci > 0:
						if len(m['year']) > 1:
							dcResult.append(str(m['id']) + '\t' + m['name'] + ' (' + m['year'] + ')')
						else:
							dcResult.append(str(m['id']) + '\t' + m['name'])

				if lfAnd:
					andC = len(lookFor.split(' and '))
					fci = 0
					for andX in lookFor.split(' and '):
						if andX in description:
							fci += 1
					if fci == andC:
						if len(m['year']) > 1:
							dcResult.append(str(m['id']) + '\t' + m['name'] + ' (' + m['year'] + ')')
						else:
							dcResult.append(str(m['id']) + '\t' + m['name'])

				_.updateLine('')
			print('')
			if len(dcResult) == 0 and not done:
				print('Nothing Found')
			else:
				print('')
				dci = 0
				for d in dcResult:
					# print(dci, '\t', d)
					print(d)
					dci += 1
				print('')
			if not done:
				print('')
				print(len(dcResult))
				print('')
			dcResult = []
		if selection == 'bio' or selection == 'b':
			newURL = extractUrl(url) + 'bio?ref_=nm_ov_bio_sm'
			page = requests.get(newURL)
			tree = html.fromstring(page.content)
			bio0 = tree.cssselect('.soda p')
			bio1 = bio0[0].text_content()
			bio = cleanupString(bio1)
			print(bio1)
		if selection == 'id':
			print(getIdFromUrl(url))
		if selection == 'xref':
			if _.switches.isActive('Movie') == True and _.switches.isActive('Person') == True:
				crossReferenceDepth(True)
			else:
				crossReference()
		if selection == 's' or selection == 'search':
			personMovie = input('Person OR Movie - ')
			searchFor = input('Search For (p/m)- ')
			if 'p' in personMovie or 'P' in personMovie:
				personMovie = 'person'
			if 'm' in personMovie or 'M' in personMovie:
				personMovie = 'movie'
			if len(searchFor) > 0:
				selectedSomething = True
				google(searchFor,personMovie)
		if selection == 'l' or selection == 'url':
			webbrowser.open(url, new=2)
		if selection == 'x' or selection == 'exit':
			sys.exit()
		if selection == 'p' or selection == 'pic':
			webbrowser.open(img, new=2)
		if selection == 'save':
			global allPeople
			global allMovies
			global relationships
			_.saveTable(allPeople,'imdb_people.json')
			_.saveTable(allMovies,'imdb_movies.json')
			_.saveTable(relationships,'imdb_relationships.json')
		try:
			selectedSomething = True
			selection = int(selection)
			print()
			print(movies[selection]['name'],' - has been selected')
			print()
			lookupMovie(movies[selection]['link'])
		except Exception as e:
			selectedSomething = False
			# print('Unspecified Error')
		if not selectedSomething:
			makeSelection()
	if _.switches.isActive('Single') == False and  _.switches.isActive('BuildCrossRef') == False:
		makeSelection()
	return {'name': theirName, 'link': url, 'movies': movies, 'age': age}
##########################################################################################
def getIdFromUrl(url):
	# http://www.imdb.com/title/tt4460176/fullcredits?ref_=tt_cl_sm#cast
	# http://www.imdb.com/name/nm0000327/?ref_=ttfc_fc_cl_t13

	# result = extractUrl(url)
	# result = result.replace('http://www.imdb.com/title/','')
	# result = result.replace('http://www.imdb.com/name/','')
	# result = result.replace('/fullcredits?ref_=tt_cl_sm#cast','')
	# result = result.replace('/?ref_=ttfc_fc_cl_t13','')
	# result = result.replace('/','')

	urls = url.split('/')
	# i=0
	# for u in urls:
	# 	print(i,u)
	# 	i+=1
	# sys.exit()


	# result = _str.totalStrip(result)
	result = urls[4]
	result = result.split('?')[0]
	return result

def buildPeople(rows,related=False):
	global allPeople
	rel = []
	
	if related == False:
		pass
	else:
		relatedID = getIdFromUrl( related['url'] )
	# buildPeople(people,{'name': theTitle, 'year': theYear, 'url': url})
	# link = 'http://www.imdb.com' + extractUrl(link0) + '?ref_=ttfc_fc_cl_t13'
	# record = {'id': cnt,'name': person,'character': character,'link': link,'img': img,'h': foundHallmark}

	# print(related)
	# rel.append({'name': related['name'], 'year': related['year'], 'link': related['url']})
	# buildMovies(rel,{'name': rows[0]['name'],'url': rows[0]['link']})

	# found = False
	# try:
		
	# 		for peeps1 in allPeople:
	# 			if peeps0['id'] == peeps1['id']:
	# 				found = True
	# except Exception as e:
	# 	pass

	# if not found:
	# print(rows)
	for peeps0 in rows:
		# print(peeps0)
		# pause = input('pause')
		try:
			thisID = getIdFromUrl( peeps0['link'] )
			allPeople.append({ 'id': thisID, 'name': peeps0['name'], 'link': peeps0['link'] })
			# print(thisID)
		except Exception as e:
			pass
		# pause = input('pause')
		if related == False:
			pass
		else:
			try:
				buildRelationships(relatedID,thisID)
			except Exception as e:
				pass
	# pause = input('pausexxx')
	# print('buildPeople')
	# sys.exit()
	# allPeople = set(allPeople)
def buildMovies(rows,related=False):
	# print(rows)
	# pause = input('pause')
	if related == False:
		pass
	else:
		relatedID = getIdFromUrl( related['url'] )
	# buildMovies(movies,{'name': theirName, 'url': url})
	# link = 'http://www.imdb.com' + extractUrl(link0) + 'fullcredits?ref_=tt_cl_sm#cast'
	# record = {'id': iiii, 'name': title, 'year': year, 'link': link, 'h': isHallmark(title,year)}
	global allMovies
	# rel = []
	# rel.append({'name': related['name'],'link': related['url']})
	# buildPeople(rel,{'name': rows[0]['name'],'url': rows[0]['link']})
	# found = False

	for movie0 in rows:
		thisID = getIdFromUrl( movie0['link'] )
		allMovies.append({ 'id': thisID, 'name': movie0['name'], 'link': movie0['link'] })
		if related == False:
			pass
		else:
			buildRelationships(thisID,relatedID)
	# allMovies = set(allMovies)
def buildRelationships(movieID,personID):
	global relationships
	# print('relationships')
	# sys.exit()
	found = False
	for rel in relationships:
		if rel['movieID'] == movieID and rel['personID'] == personID:
			found = True

	if not found:
		relationships.append({ 'movieID': movieID, 'personID': personID })


##########################################################################################
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

	# print(string)
	# stringTMP = string.split('(')
	# string = stringTMP[2].replace(')','')
	string = _str.onlyDigits(string)
	# print(string)
	# sys.exit()

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

	# print(string)
	stringTMP = string.split('(')
	string = stringTMP[2].replace(')','')
	# print(string)
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
	return string
def lookupMovie(url):
	global iHallmark
	iHallmark = 0
	# print(url)
	if _.switches.isActive('Episode'):
		print('Loading...')
		episodeLink(url)
		sys.exit()
	if _.switches.isActive('QuickInfo'):
		movieRating(url)
		sys.exit()
	idRegistier(url)
	if _.switches.isActive('NoPrint') == False:
		pass
		os.system('cls')
	# print(url)
	# pause = input('pause')
	page = requests.get(url)
	tree = html.fromstring(page.content)
	movieTitle = tree.cssselect('h3')
	movieYear = tree.cssselect('.nobr')
	try:
		theYear = cleanupStringYear2(movieYear[0].text_content())
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
		linkTest =ta.attrib['href']
		if '/title/tt' in linkTest and not found:
			found =True
			theTitle0 = cleanupString(ta.text_content())
			if len(theTitle0) > 1 and not 'External Sites' in theirName0 and not 'Full Cast' in theirName0:
				theTitle = theTitle0
	
	# for ty in movieYear:
	# 	print(cleanupString(ty.text_content(),False))
	print('Processing', theYear, theTitle, '...')
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
	print(len(tr))
	people = []
	people2 = []


	for e in tr:

		# Set 2
		# 
		props = e.cssselect('td')
		# print(len(props))
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
			# print(link)
		except Exception as ee:
			link = ''
		if len(link) > 3:
			people = registerPerson(people,person,link,character)
			people2.append({'name': person, 'link': link, 'character': character})


		# Set 1
		# 
		# # props = e.cssselect('.itemprop')
		# i = 0
		# for p in props:
		# 	if i == 0:
		# 		link = ''
		# 		try:
		# 			links = p.cssselect('a')
		# 			link0 = str(links[0].attrib['href'])
		# 			link = 'http://www.imdb.com' + extractUrl(link0) + '?ref_=ttfc_fc_cl_t13'
		# 			# print(link)
		# 		except Exception as ee:
		# 			pass
		# 		person = p.text_content()
		# 		person = cleanupString(person)
		# 		# print(people,person,link,character)
		# 		people = registerPerson(people,person,link,character)
		# 		people2.append({'name': person, 'link': link, 'character': character})
		# 	i += 1
	def doMore():
		if _.switches.isActive('NoPrint') == False:
			os.system('cls')
			print()
			print(theYear,theTitle)
			print()
		if _.switches.isActive('NoPrint') == False:
			if _.switches.isActive('HallmarkCrossRef') == True:
				_.tables.register('Auto',people)
				_.tables.print('Auto','id,hallmark,name,character')
				print()
				print('    ',iHallmark,'Hallmark')
			else:
				_.tables.register('Auto',people)
				_.tables.print('Auto','id,name,character')
		if _.switches.isActive('BuildCrossRef') == True and not _.switches.value('BuildCrossRef') == 'skip':
			# print('test1')
			buildPeople(people,{'name': theTitle, 'year': theYear, 'url': url})
			# print('test2')
			# sys.exit()
			theRows = []
			theRows.append({'name': theTitle, 'year': theYear, 'link': url})
			# print('test3')
			buildMovies(theRows)
			# print('test4')
			# print()
	# if _.switches.isActive('BuildCrossRef') == False:
	doMore()
	def makeSelection():
		# lookupMovie(url):
		print()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 'h' or selection == '?' or selection == 'help':
			# print('(f)ranchise')
			print('id')
			print('(r)ated','why')
			print('(s)earch')
			print('(d)escription')
			print('xref')
			print('l','url')
			print('(p)ic')
			print('(e)pisodes')
			print('e(x)it')
			print('save')
			print('(f)ranchise')
			print('search results (sr)')
		if selection == 'sr':
			print()
			sr = input('Search for - ')
			searchResults = []
			for m in people:
				if sr.lower() in m['name'].lower():
					searchResults.append(m)
			print()
			_.tables.register('searchResults',searchResults)
			_.tables.print('searchResults','id,name,character')
		if selection == 'f':
			print()
			franchise = input('franchise: ')
			if '!' in franchise:
				force = True
			else:
				force = False
			if '?' in franchise:
				obscure = True
			else:
				obscure = False
			franchise = franchise.lower()
			franchise = _str.basic(franchise)
			franchiseName = franchise.replace(' ','_')
			franchiseNameList = franchise + '_list'
			franchiseDate = franchiseName + '_date'
			print(franchise)
			now = datetime.datetime.now()
			today = now.strftime("%Y-%m-%d")
			print()
			print()
			print('Automatic Inteligent Research', franchise.upper(),'...')
			print()
			print()
			global franchiseData
			franchiseFile = 'imdb_franchises.json'
			franchiseData = _.getTable(franchiseFile)
			# print(franchiseData)
			didResearch = False
			if force:
				print('Force')
				print()
				startResearch = True
			else:
				try:
					found = False
					if len(franchiseData[0][franchiseDate]) > 0:
						found = True
						fdtl = franchiseData[0][franchiseDate].split('-')
						foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
						td = str(today).split('-')
						tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
						diff = tdd - foundDate
						# print(diff.days)
						
					global franchiseDaysMax
					if found:
						if int(diff.days) > franchiseDaysMax:
							startResearch = True
						else:
							startResearch = False
					else:
						startResearch = True
				except Exception as e:
					# print('Error')
					startResearch = True


			global smartOmit
			
			theList = []
			for sol in smartOmit.split(';'):
				so = sol.split(',')

				if franchise.lower() == so[0].lower():
					franchiseSearch = so[0] + '+-' + so[1]
					franchiseOmit = so[1]
				else:
					franchiseSearch = franchise
					franchiseOmit = ''
			if startResearch:
				didResearch = True
				try:
					franchiseData[0][franchiseNameList]
					if len(franchiseData[0][franchiseNameList]) > 0:
						listExists = True
					else:
						listExists = False
				except Exception as e:
					listExists = False
				# print( 'listExists:', listExists )
				# sys.exit()
				# print('startResearch')
				# sys.exit()

				# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+franchise+movies'):
				if listExists:
					theList = franchiseData[0][franchiseNameList]
				else:
					for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchiseSearch+'+movies',franchise,franchiseOmit, obscure = obscure ):
						theList.append(xx)
					for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchiseSearch+'+series',franchise,franchiseOmit, obscure = obscure ):
						theList.append(xx)
					for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchiseSearch+'+tv+show',franchise,franchiseOmit, obscure = obscure ):
						theList.append(xx)
						# for x in xx
					# print(theList)



				print('Initiating research on ',len(theList),'items')
				franchiseList = []
				for lnk in theList:
					print()
					print()
					# print(lnk['name'].replace(' - IMDb','').replace('IMDb','').replace('imdb','').replace('IMDB',''))
					# print(lnk['link'].replace('https://www.imdb.com/','').replace('http://www.imdb.com/',''))
					print(lnk['link'].replace('https://www.imdb.com/','').replace('http://www.imdb.com/',''),lnk['name'].replace(' - IMDb','').replace('IMDb','').replace('imdb','').replace('IMDB',''))
					do = buildUrlList(lnk['link'])
					print(len(set(do)))
					for xxx in do:
						franchiseList.append(xxx)
					# try:
					# except Exception as e:
					# 	print('Error: buildUrlList')


				try:
					franchiseData[0][franchiseName][0]
				except Exception as e:
					franchiseData[0][franchiseName] = []

				try:
					for fItem in set(franchiseList):
						if not fItem in franchiseData[0][franchiseName]:
							franchiseData[0][franchiseName].append( fItem )
					# franchiseData[0][franchiseName] = list(set(franchiseList))
				except Exception as e:
					franchiseData.append({franchiseName: franchiseList})
				try:
					franchiseData[0][franchiseDate] = str(today)
				except Exception as e:
					franchiseData[0] = {franchiseDate: str(today)}

			else:
				pass

			

			try:
				franchiseData[1]
			except Exception as e:
				franchiseData.append({})

			try:
				franchiseData[2]
			except Exception as e:
				franchiseData.append({})

			try:
				franchiseData[1][franchiseName]
				hasPeople = True
			except Exception as e:
				hasPeople = False
				franchiseData[1][franchiseName] = []
			try:
				franchiseData[2][franchiseName]
				hasPeople = True
			except Exception as e:
				hasPeople = False
				franchiseData[1][franchiseName] = []
			if len(franchiseData[1][franchiseName]) == 0:
				hasPeople = False
				
			if hasPeople:
				if expireCheck(franchiseData[1][franchiseDate]):
					hasPeople = False


				# try:
				# 	franchiseData[1][franchiseDate]
				# except Exception as e:
				# 	franchiseData[1][franchiseDate] = str(today)

			if not hasPeople:
				try:
					franchiseData[1][franchiseName] = []
				except Exception as e:
					pass
				try:
					franchiseData[2][franchiseName] = []
				except Exception as e:
					pass
				thePeopleY = []
				for fd in set(franchiseData[0][franchiseName]):
					urlP = 'https://www.imdb.com/title/'+fd+'/fullcredits?ref_=tt_cl_sm#cast'
					omitThis = False
					if len(franchiseOmit) > 0:
						try:
							franchiseData[0][franchiseOmit]
							hasOmitData = True
						except Exception as e:
							hasOmitData = False
						
						if hasOmitData:
							if fd in franchiseData[0][franchiseOmit]:
								omitThis = True
					if omitThis:
						print()
						print()
						print('Omit:\t',urlP)
						print()
						print()
					else:
						# print('URL:\t',urlP)
						thePeopleX = []
						
						# print(urlP)

						try:
							page = requests.get(urlP)
							tree = html.fromstring(page.content)
							movieTitle = tree.cssselect('h3')
							movieYear = tree.cssselect('.nobr')
							try:
								theYear0 = cleanupString(movieYear[0].text_content(),False)
								theYearX = theYear0.split(' ')[0].replace('(','')
								theYearX = theYearX.replace(')','')
								theYearX = theYearX.replace(' ','')
							except Exception as e:
								theYearX = ''
							theTitleX = cleanupString(movieTitle[0].text_content())
							theAlist = tree.cssselect('a')
							found = False
							for ta in theAlist:
								linkTest =ta.attrib['href']
								if '/title/tt' in linkTest and not found:
									found =True
									theTitle0 = cleanupString(ta.text_content())
									if len(theTitle0) > 1 and not 'External Sites' in theirName0 and not 'Full Cast' in theirName0:
										theTitle = theTitle0
							
							print('Processing',fd, theYearX, theTitleX, '...')
							cast = tree.cssselect('.cast_list')
							tr = cast[0].cssselect('tr')
							print(len(tr))


							for e in tr:

								try:
									links = e.cssselect('a')
									link0 = str(links[0].attrib['href'])
									link = 'http://www.imdb.com' + extractUrl(link0) + '?ref_=ttfc_fc_cl_t13'

									if 'nm' in link:
										thePeopleY.append(getIdFromUrl(link))
										thePeopleX.append(getIdFromUrl(link))
								except Exception as ee:
									pass
						except Exception as e:
							pass
						if len(thePeopleX) > 0:
							franchiseData[2][franchiseName].append({'year': theYearX, 'title': theTitleX, 'people': thePeopleX, })
				print(len(thePeopleY))
				print(len(set(franchiseData[0][franchiseName])))
				franchiseData[1][franchiseName] = list(set(thePeopleY))
				franchiseData[1][franchiseDate] = str(today)
				# sys.exit()

				# os.system('cls')
				# for fd in franchiseData[0][franchiseName]:
				# 	print( fd )

			if didResearch:
				if len( franchiseData[0][franchiseName] ):
					print()
					print()
					print(franchiseName.replace( '_', ' ' ).title())
					alias = input('Alias: ')
					_.saveTable(franchiseData,franchiseFile)

					if len( alias ):
						alias = _str.replaceDuplicate(alias,' ')
						alias = _str.cleanBE(alias,' ')
						if len( alias ):
							franchiseDataDisplay = _.getTable( 'imdb_franchise_display.json' )
							franchiseDataDisplay.append( { 'actual': franchiseName, 'proper': alias } )
							_.saveTable( franchiseDataDisplay, 'imdb_franchise_display.json' )

			franchiseList = list(set(franchiseData[1][franchiseName]))


			fdtl = franchiseData[1][franchiseDate].split('-')
			foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
			td = str(today).split('-')
			tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
			diff = tdd - foundDate
			print()





			# pause = input('pause')
			os.system('cls')
			print()
			print(theYearThis, '\t', theTitleThis)
			print()
			
			# print(people)
			for ix,r in enumerate(people):
				# record = {'id': cnt,'name': person,'character': character,'link': link,'img': img}
				# print((r['link']))
				# print(getIdFromUrl(r['link']))
				if getIdFromUrl(r['link']) in franchiseList:
					# print(r['name'])
					people[ix][franchiseName] = 'x'
				else:
					people[ix][franchiseName] = ''
			_.tables.register('Auto',people)
			_.tables.print('Auto','id,'+franchiseName+',name,character')
			print()
			print()
			io = 0
			for ix,r in enumerate(people):
				if getIdFromUrl(r['link']) in franchiseList:
					io += 1
					print(r['name'])
			print()
			# print('out of',len(people),'people,',io,'are from the',franchiseName,'franchise')
			print()
			print('\t',franchiseName.replace('_',' ').upper()+': ',io,'of',len(people))

			print()
			print()
			try:
				ppl = str(len(set(franchiseData[1][franchiseName]))) + ' people\t\t'
			except Exception as e:
				ppl = ''
			try:
				mv = str(len(set(franchiseData[0][franchiseName]))) + ' movies\t\t'
			except Exception as e:
				mv = ''
			print('_____________________________________________________________________________________________________________________')
			print(franchise.upper(),len(set(franchiseList)),'\t\t',ppl,mv,franchiseData[1][franchiseDate],'\t\t',str(diff.days),'days')
			print()
			print()

		###################################################################################################	
		if selection == 'id':
			print(getIdFromUrl(url))
		if selection == 'xref':
			crossReference()

		if selection == 'e':
			episodes(url,theYear,theTitle)


								
		if selection == 'r' or selection == 'rated' or selection == 'why':
			movieRating(url)


				# try:
				# 	newURL = 'http://www.imdb.com/title/' + getIdFromUrl(url) + '/parentalguide'
				# 	page = requests.get(newURL)
				# 	tree = html.fromstring(page.content)
				# 	tr = tree.cssselect('#certifications-list')
				# 	td = tr[0].cssselect('li')
				# 	print()
				# 	print('Rating:')
				# 	for item in td:
				# 		data0 = item.text_content()
				# 		data1 = cleanupString(data0)
				# 		# print(data1)
				# 		if 'United' in data1 and 'States' in data1:
				# 			data = data1.split(':')
				# 			print('\t',data[1])
				# 	print()
				# except Exception as e:
				# 	print('Information unavailable')
		if selection == 's' or selection == 'search':
			personMovie = input('Person OR Movie - ')
			searchFor = input('Search For - ')
			if 'p' in personMovie or 'P' in personMovie:
				personMovie = 'person'
			if 'm' in personMovie or 'M' in personMovie:
				personMovie = 'movie'
			if len(searchFor) > 0:
				selectedSomething = True
				google(searchFor,personMovie)
		if selection == 'l' or selection == 'url' :
			webbrowser.open(url, new=2)
		if selection == 'x' or selection == 'exit':
			sys.exit()
		if selection == 'description' or selection == 'd':
			newURL = extractUrl(url) + '?ref_=ttfc_fc_tt'
			page = requests.get(newURL)
			tree = html.fromstring(page.content)
			description0 = tree.cssselect('.summary_text')
			description1 = description0[0].text_content()
			description = cleanupString(description1)
			print()
			print(description)
			print()

		if selection == 'p' or selection == 'pic':
			webbrowser.open(img, new=2)
		if selection == 'xref':
			pass
		if selection == 'save':
			global allPeople
			global allMovies
			global relationships
			print(len(allPeople),'people')
			print(len(allMovies),'movies')
			print(len(relationships),'relationships')
			_.saveTable(allPeople,'imdb_people.json')
			_.saveTable(allMovies,'imdb_movies.json')
			_.saveTable(relationships,'imdb_relationships.json')
		try:
			selectedSomething = True
			selection = int(selection)
			print()
			print(people[selection]['name'],' - has been selected')
			print()
			lookupPerson(people[selection]['link'])
		except Exception as e:
			selectedSomething = False
			# print('Unspecified Error')
		if not selectedSomething:
			makeSelection()
	if _.switches.isActive('Single') == False and  _.switches.isActive('BuildCrossRef') == False:
		makeSelection()
	return {'name': theTitle, 'year': theYear, 'link': url, 'people': people2}
###################################################################################

def monthToNumber(theDate):
	result = theDate
	try:
		theDate = theDate.lower()
		months = 'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec'.lower()
		m = months.split(',')
		d = theDate.split(' ')
		for i,mo in enumerate(m):
			if d[1].lower() == mo:
				dId = str(i+1)
				if len(dId) == 1:
					dId = '0' + dId
		if len(d[0]) == 1:
			d[0] = '0' + d[0]
		result = d[2] + '-' + dId + '-' + d[0]
	except Exception as e:
		pass
	return result



def episodeLink(url):
	eId = _.switches.value('Episode')
	if not ':' in eId:
		print('No Show')
		sys.exit()
	season = eId.split(':')[0]
	_.switches.fieldSet('Episode','active',False)



	page = requests.get(url)
	tree = html.fromstring(page.content)
	movieTitle = tree.cssselect('h3')
	movieYear = tree.cssselect('.nobr')
	try:
		theYear0 = cleanupString(movieYear[0].text_content(),False)
		theYear = theYear0.split(' ')[0].replace('(','')
		theYear = theYear.replace(')','')
		theYear = theYear.replace(' ','')
	except Exception as e:
		theYear = ''
	theTitle = cleanupString(movieTitle[0].text_content())
	# theAlist = tree.cssselect('a')
	# # theTitle = ''
	# found = False
	# for ta in theAlist:
	# 	linkTest =ta.attrib['href']
	# 	if '/title/tt' in linkTest and not found:
	# 		found =True
	# 		theTitle0 = cleanupString(ta.text_content())
	# 		if len(theTitle0) > 1 and not 'External Sites' in theirName0 and not 'Full Cast' in theirName0:
	# 			theTitle = theTitle0



	newURL = 'https://www.imdb.com/title/' + getIdFromUrl(url) + '/episodes?season='
	siteBase = 'https://www.imdb.com'


	page = requests.get(newURL + season)
	tree = html.fromstring(page.content)

	seasons = tree.cssselect('#bySeason option')
	print()
	print('Seasons:',len(seasons))
	print()
	shows = tree.cssselect('a[itemprop="name"]')

	episodeList = []
	episodeListIds = []

	theTitle = _str.cleanBE(theTitle,' ')
	global zeroList
	zeroList = zeroList.lower()
	zeroListX = zeroList.split(',')
	if theTitle.lower() in zeroListX:
		isZero = True
		# print('zero')
	else:
		isZero = False



	for ii,show in enumerate(shows):
		link = show.attrib['href']
		if not isZero:
			seasonZero = False
		if isZero and ii == 0:
			seasonZero = isSeasonZero(siteBase + link)
		# if theTitle.lower() == 'doctor who' and isZero and not season in ['1','8']:
		if seasonZero:
			episodeN = str(ii)
		else:
			episodeN = str(ii+1)
		showId = season + ':' + episodeN
		# link = link0.split('?')[0] + 'fullcredits?ref_=tt_cl_sm#cast'
		showTitle0 = show.text_content()
		showTitle = cleanupString(showTitle0)
		print('\t',showId,'\t',showTitle)
		episodeListIds.append(showId)
		episodeList.append({'id': showId, 'title': showTitle, 'url': siteBase + link })




	if eId in episodeListIds:
		for i,episode in enumerate(episodeList):
			if eId == episode['id']:
				# print(episode['url'])
				# sys.exit()
				lookupEpisode(theYear,theTitle,episode['id'],episode['title'],episode['url'])
	else:
		print('No Episode Found')
		sys.exit()






def isSeasonZero(url):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	data0 = tree.cssselect('.bp_text_only')
	data = cleanupString(data0[0].text_content())
	data = _str.cleanBE(data,' ')
	if data[len(data)-1] == '0':
		result = True
	else:
		result = False
	# print(data)
	# sys.exit()
	return result
	

def airdateAlignRight(theDate):
	global maxDateLength
	# theDate = monthToNumber(theDate)
	diff = maxDateLength - len(theDate)
	i = 0
	space = ''
	while not diff == i:
		i += 1
		space += ' '
	return theDate + space



def episodesCache(theTitle):
	global seasonData
	# print(seasonData)
	# seasonData = [{'year': theYear, 'title': theTitle, 'seasons': seasonList}]
	# seasonList.append({'season': season, 'episodes': episodeSet})
	# episodeList.append({'id': showId, 'title': showTitle, 'url': siteBase + link })
	# print(seasonData[0]['title'])

	for data in seasonData:
		if data['title'] == theTitle:
			print()
			print('Seasons:',len(data['seasons']))
			print()
			episodeListIds = []
			episodeList = []
			for se in data['seasons']:
				print()
				print()
				print('Season:',se['season'])
				print()
				for ep in se['episodes']:
					print('\t',ep['id'],'\t',airdateAlignRight(ep['airdate']),'\t',ep['title'])
					episodeList.append(ep)
					episodeListIds.append(ep['id'])
			print()
			print()
			selection = input('Make Selection - ')
			print()

			if len(selection) == 0:
				selection = 'x'
			if selection.lower() == 'x':
				sys.exit()
			if selection in episodeListIds:
				for i,episode in enumerate(episodeList):
					if selection == episode['id']:
						print(episode['url'])
						# sys.exit()
						lookupEpisode(data['year'],data['title'],episode['id'],episode['title'],episode['url'])
			print()

def expireCheck(theDate):
	global expireCheckDaysMax
	now = datetime.datetime.now()
	today = now.strftime("%Y-%m-%d")
	fdtl = theDate.split('-')
	foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	td = str(today).split('-')
	tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
	diff = tdd - foundDate

	if int(diff.days) > expireCheckDaysMax:
		result = True
	else:
		result = False
	return result
def crossReferenceEpisodes(iDs):
	global seasonData
	# print(iDs)
	os.system('cls')
	data = []
	shows = []
	dateList = []
	for d in seasonData:
		if d['id'] in iDs:
			data.append(d)
			# print(d['title'])
			shows.append({'id': d['id'], 'title': d['title'].replace(',','_'), 'started': d['seasons'][0]['episodes'][0]['airdate']})
			for seasons in d['seasons']:
				for episodes in seasons['episodes']:
					dateList.append(episodes['airdate'])

	shows = sorted(shows, key=itemgetter('started'))
	dateList.sort()
	def findDateMatch(theDate,theId):
		result = ''
		# print(data)
		for d in data:
			if d['id'] == theId:
				for seasons in d['seasons']:
					for episodes in seasons['episodes']:
						# print(episodes)
						if episodes['airdate'] == theDate:
							result = episodes['id']
							break
		return result
	def findIDMatch(theId,theTitle):
		result = ''
		# print(data)
		for d in data:
			if d['title'] == theTitle:
				for seasons in d['seasons']:
					for episodes in seasons['episodes']:
						# print(episodes)
						if episodes['id'] == theId:
							result = episodes['url']
							break
		return result
	dataTable = []
	for dl in dateList:
		row = {}
		if '-' in dl:
			row['date'] = dl
			hasData = 0
			for s in shows:
				showId = findDateMatch(dl,s['id'])
				row[s['title'].lower()] = showId
				if len(showId) > 0:
					hasData += 1
			if hasData > 1:
			# if len(shows) == hasData:
				dataTable.append(row)
	c = 'date,'
	for s in shows:
		c += s['title'] + ','
	c = _str.cleanBE(c,',')
	# print(c)
	_.tables.register('Auto',dataTable)
	_.tables.print('Auto',c)
	print()
	print(len(dataTable))

	def makeSelection():
		print()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 's':
			print()
			# print(0,' All')
			for i,s in enumerate(shows):
				print(i+1,s['title'])
			searchIn = input('Seach In - ')
			print()
			searchFor = input('Seach For - ')
			if searchIn == '0':
				print('Selected:','All')
			else:
				spent = []
				for i,s in enumerate(shows):
					sel = str(i+1)
					if searchIn == sel:
						print('Selected:',s['title'])
						print()
						for dt in dataTable:
							if not dt[s['title'].lower()] in spent:
								spent.append(dt[s['title'].lower()])
								# dt[s['title'].lower()]
								url = findIDMatch(dt[s['title'].lower()],s['title'])
								# print(url)
								page = requests.get(url)
								tree = html.fromstring(page.content)
								data0 = tree.cssselect('.summary_text')
								data = cleanupString(data0[0].text_content())
								data = _str.cleanBE(data,' ')
								found = False
								if len(searchFor) == 0:
									print()
									print(dt[s['title'].lower()],data)
								else:

									for theSearch in searchFor.split(' '):
										if theSearch.lower() in data.lower():
											found = True
											print(dt[s['title'].lower()],data)
											break
									if found:
										pause = input('break? ')
										if 'y' in pause.lower():
											break


								# print(dt[s['title'].lower()])

	makeSelection()
	# for dt in dataTable:
	# 	print(dt)
	# dateList = sorted(dateList, key=itemgetter('started'))
	# for s in shows:
	# 	print(s['started'],s['title'])
def episodes(url,theYear='',theTitle=''):
	if _.switches.isActive('BuildCrossRef'):
		os.system('cls')
		print('Processing...')
	global seasonData
	if theTitle == '':
		page = requests.get(url)
		tree = html.fromstring(page.content)
		movieTitle = tree.cssselect('h3')
		movieYear = tree.cssselect('.nobr')
		try:
			theYear0 = cleanupString(movieYear[0].text_content(),False)
			theYear = theYear0.split(' ')[0].replace('(','')
			theYear = theYear.replace(')','')
			theYear = theYear.replace(' ','')
		except Exception as e:
			theYear = ''
		theTitle = cleanupString(movieTitle[0].text_content())

	theYear = _str.cleanBE(theYear,' ')
	theTitle = _str.cleanBE(theTitle,' ')
	isCached = False
	now = datetime.datetime.now()
	today = now.strftime("%Y-%m-%d")
	# if theYear[len(theYear)-1] == '-':
	# 	print('still running')
	seasonDataFile = 'imdb_season-data.json'
	if len(seasonData) == 0:
		seasonData = _.getTable(seasonDataFile)
	if not len(seasonData) == 0:
		isExpired = False
		newData = []
		for sda in seasonData:

			if theYear[len(theYear)-1] == '-' and expireCheck(sda['date']):
				isExpired = True
			else:
				newData.append(sda)
			if sda['title'] == theTitle:
				isCached = True
		if isExpired:
			seasonData = []
			seasonData = newData
		newData = []

	if isCached:
		if not _.switches.isActive('BuildCrossRef'):
			episodesCache(theTitle)
	else:
		newURL = 'https://www.imdb.com/title/' + getIdFromUrl(url) + '/episodes?season=THESEASON&ref_=tt_eps_sn_1'
		siteBase = 'https://www.imdb.com'
		thisURL = newURL.replace('THESEASON','1')
		# print(thisURL)
		page = requests.get(thisURL)
		tree = html.fromstring(page.content)
		seasons = tree.cssselect('#bySeason option')
		seasonTest0 = seasons[len(seasons)-1].text_content()
		seasonTest = cleanupString(seasonTest0)
		global zeroList
		zeroList = zeroList.lower()
		zeroListX = zeroList.split(',')
		if theTitle.lower() in zeroListX:
			isZero = True
		else:
			isZero = False

		if 'unknown' in seasonTest.lower():
			unknown = True
			print()
			print('Seasons:',len(seasons)-1)
			print()
		else:
			unknown = False
			print()
			print('Seasons:',len(seasons))
			print()
		episodeList = []
		seasonList = []
		episodeListIds = []
		for i,s in enumerate(seasons):
			season = str(i+1)
			if int(season) == len(seasons) and unknown:
				thisURL = newURL.replace('THESEASON','-1')
			else:
				thisURL = newURL.replace('THESEASON',season)

				page = requests.get(thisURL)
				tree = html.fromstring(page.content)
				episodeCode = tree.cssselect('div[itemprop="episodes"]')
				print()
				print()
				if int(season) == len(seasons) and unknown:
					print('Season:',season,' - Unknown')
				else:
					print('Season:',season)
				print()
				episodeSet = []
				for ii,epiCode in enumerate(episodeCode):
					shows = epiCode.cssselect('a[itemprop="name"]')
					show = shows[0]
					link = show.attrib['href']
					if not isZero:
						seasonZero = False
					if isZero and ii == 0:
						seasonZero = isSeasonZero(siteBase + link)
					# if theTitle.lower() == 'doctor who' and isZero and not season in ['1','8']:
					if seasonZero:
						episodeN = str(ii)
					else:
						episodeN = str(ii+1)
					# link = link0.split('?')[0] + 'fullcredits?ref_=tt_cl_sm#cast'
					# episodeN = link.split('ttep_ep')[1]
					
					airdate0 = epiCode.cssselect('.airdate')
					airdate1 = airdate0[0].text_content()
					airdate2 = cleanupString(airdate1)
					airdate3 = airdate2.replace('.','')
					airdate = monthToNumber(airdate3)
					showId = season + ':' + episodeN
					showTitle0 = show.text_content()
					showTitle = cleanupString(showTitle0)
					print('\t',showId,'\t',airdateAlignRight(airdate),'\t',showTitle)
					episodeListIds.append(showId)
					episodeList.append({'id': showId, 'title': showTitle, 'url': siteBase + link, 'airdate': airdate})
					episodeSet.append({'id': showId, 'title': showTitle, 'url': siteBase + link, 'airdate': airdate})
				seasonList.append({'season': season, 'episodes': episodeSet})
		
		seasonData.append({'id': getIdFromUrl(url), 'year': theYear, 'title': theTitle, 'seasons': seasonList, 'date': str(today)})
		_.saveTable(seasonData,seasonDataFile,True,False)
		print()
		print()
		# print(_.switches.isActive('BuildCrossRef'))
		if not _.switches.isActive('BuildCrossRef'):
			selection = input('Make Selection - ')
			selection = selection.replace(' ','')
			print()
			if len(selection) == 0:
				selection = 'x'
			if selection.lower() == 'x':
				sys.exit()
			if selection in episodeListIds:
				for i,episode in enumerate(episodeList):
					if selection == episode['id']:
						print(episode['url'])
						# sys.exit()
						lookupEpisode(theYear,theTitle,episode['id'],episode['title'],episode['url'])
			else:
				print('Error')


			print()

def lookupEpisode(theYear,theTitle,showId,showTitle,url):
	# link = url.split('?')[0] + 'fullcredits?ref_=tt_cl_sm#cast'
	# def lookupMovie
	os.system('cls')
	# print(url)
	# 'https://www.imdb.com/title/tt1998643/?ref_=ttep_ep1'
	# 'https://www.imdb.com/title/tt1998643/fullcredits?ref_=tt_cl_sm#cast'
	page = requests.get(url)
	tree = html.fromstring(page.content)
	shows = tree.cssselect('a[itemprop="name"]')
			

	titleParent = tree.cssselect('.titleParent')
	ta = titleParent[0].cssselect('a')
	parentURL = 'https://www.imdb.com' + str(ta[0].attrib['href'])
	parentURL = parentURL.replace('?ref_=tt_ov_inf','')
	page = requests.get(url)
	tree = html.fromstring(page.content)
	data0 = tree.cssselect('.summary_text')
	data = cleanupString(data0[0].text_content())
	data = _str.cleanBE(data,' ')

	print()
	print(theTitle)
	print()
	print('\t Episode:',showId)
	print()
	print('\t\t',showTitle)
	print()
	print('\t\t\t',data)
	print()
	print()
	page = requests.get(url.split('?')[0] + 'fullcredits?ref_=tt_cl_sm#cast')
	tree = html.fromstring(page.content)

	cast = tree.cssselect('.cast_list')
	tr = cast[0].cssselect('tr')
	# print(len(tr))
	people = []
	people2 = []

	for e in tr:

		# Set 2
		# 
		props = e.cssselect('td')
		# print(len(props))
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
			# print(link)
		except Exception as ee:
			link = ''
		if len(link) > 3:
			people = registerPerson(people,person,link,character)
			people2.append({'name': person, 'link': link, 'character': character})


	_.tables.register('Auto',people)
	_.tables.print('Auto','id,name,character')



	def makeSelection():
		print()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'

		
		try:
			int(selection)
			isNumber = True
		except Exception as e:
			isNumber = False

		if isNumber:
			lookupPerson(people[int(selection)]['link'])

		if selection == 'h' or selection == '?' or selection == 'help':
			print('l','url')
			print('(e)pisodes')
			print('e(x)it')

		if selection == 'e':

			# pause = input('pause')

			
			episodes(parentURL,theYear,theTitle)
								

		if selection == 'l' or selection == 'url' :
			webbrowser.open(url, new=2)
		if selection == 'x' or selection == 'exit':
			sys.exit()
		makeSelection()

	makeSelection()
























def movieRating(url):
	if _.switches.isActive('Score'):
		title = _.switches.value('Movie')

		newURL = 'https://www.imdb.com/title/' + getIdFromUrl(url) + '/ratings'
		# print(newURL)
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		description0 = tree.cssselect('.allText')
		description1 = description0[0].text_content()
		description = cleanupString(description1)

		try:
			print(description.split('vote of ')[1],title.replace(',',' '))
		except Exception as e:
			pass
		sys.exit()


	if _.switches.isActive('QuickInfo'):
		print('______________________________________________________________________________________________________')
		title = _.switches.value('Movie')
		print(title.replace(',',' '))

		newURL = 'https://www.imdb.com/title/' + getIdFromUrl(url) + '/ratings'
		# print(newURL)
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		description0 = tree.cssselect('.allText')
		description1 = description0[0].text_content()
		description = cleanupString(description1)
		print()
		try:
			peoplVoted0 = tree.cssselect('.ratingTable a')
			peoplVoted1 = peoplVoted0[0].text_content()
			peoplVoted = cleanupString(peoplVoted1)
		except Exception as e:
			peoplVoted = ''

		try:
			if not peoplVoted == '':
				print(description.split('vote of ')[1],title.replace(',',' '), '\t',peoplVoted,'people voted')
			else:
				print(description.split('vote of ')[1],title.replace(',',' '))
		except Exception as e:
			pass

		newURL = 'http://www.imdb.com/title/' + getIdFromUrl(url) + '/?ref_=ttfc_fc_tt'
		# print(newURL)
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		description0 = tree.cssselect('.summary_text')
		description1 = description0[0].text_content()
		description = cleanupString1(description1)
		print()
		print(description)
		print()
	newURL = 'http://www.imdb.com/title/' + getIdFromUrl(url) + '/parentalguide'
	# print(newURL)
	try:

		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		try:
			tr = tree.cssselect('#mpaa-rating')
			td = tr[0].cssselect('td')
			description1 = td[1].text_content()
			description = cleanupString(description1)
			print()
			print(description)
			print()
		except Exception as e:
			pass
		try:
			tr = tree.cssselect('#certifications-list')
			td = tr[0].cssselect('li')
			print()
			print('Rating:')
			for item in td:
				data0 = item.text_content()
				data1 = cleanupString(data0)
				# print(data1)
				if 'United' in data1 and 'States' in data1:
					data = data1.split(':')
					print('\t',data[1])
			print()
		except Exception as e:
			pass
		theRatings = []
		try:
			section = tree.cssselect('#advisory-nudity')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			print()
			if not rating == 'Be':
				theRatings.append({'category': 'Sex','rating': rating})
				# print('Sex:       \t',rating)
		except Exception as e:
			pass
		try:
			section = tree.cssselect('#advisory-violence')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			if not rating == 'Be':
				theRatings.append({'category': 'Violence','rating': rating})
				# print('Violence:\t',rating)
		except Exception as e:
			pass
		try:
			section = tree.cssselect('#advisory-profanity')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			if not rating == 'Be':
				theRatings.append({'category': 'Profanity','rating': rating})
				# print('Profanity:\t',rating)
		except Exception as e:
			pass
		try:
			section = tree.cssselect('#advisory-alcohol')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			if not rating == 'Be':
				theRatings.append({'category': 'Alcohol/Drugs','rating': rating})
				# print('Alcohol/Drugs:\t',rating)
		except Exception as e:
			pass
		try:
			section = tree.cssselect('#advisory-frightening')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			if not rating == 'Be':
				theRatings.append({'category': 'Frightening','rating': rating})
				# print('Frightening:\t',rating)
		except Exception as e:
			pass
		try:
			if len(theRatings) > 0:
				_.tables.register('Auto',theRatings)
				_.tables.print('Auto','category,rating')
		except Exception as e:
			pass
	except Exception as e:
		print('Information unavailable')
	print()
###################################################################################
def isHallmark(thisID):
	global hallmark
	if len(hallmark) == 0:
		hallmark = _.getTable('hallmark.json')
	result = ''
	for hmk in hallmark:
		# if movie == hmk['name'] and year == hmk['year']:
		# print(thisID)
		# print(getIdFromUrl(hmk['link']))
		# pause = input('pause')
		if thisID == getIdFromUrl(hmk['link']):
			result = 'H'
	return result

def buildHallmarkTable():
	global hallmarkDataRaw
	global buildUrlListDuplicate
	now = datetime.datetime.now()
	# today = now.strftime("%Y-%m-%d")
	thisYear = int(str(now.strftime("%Y")))
	years = []
	years.append(thisYear+1)
	years.append(thisYear)
	for x in range(1,20):
		years.append(thisYear-x)
		
	# print(years)
	# sys.exit()
	franchise = 'hallmark'
	franchiseOmit = 'lifetime'
	# theList = []
	theList = _.getTable('imdb_hallmark_auto_research_theList.json')
	if len(theList) == 0:
		for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+movies',franchise,franchiseOmit):
			try:
				theList.append(xx)
			except Exception as e:
				pass
		# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+series',franchise,franchiseOmit):
		# 	try:
		# 		theList.append(xx['link'])
		# 	except Exception as e:
		# 		pass
		# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+tv+show',franchise,franchiseOmit):
		# 	try:
		# 		theList.append(xx['link'])
		# 	except Exception as e:
		# 		pass


		for theYear in years:
			theYear = str(theYear)
			for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+movies',franchise,franchiseOmit):
				try:
					theList.append(xx)
				except Exception as e:
					pass
			# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+series',franchise,franchiseOmit):
			# 	try:
			# 		theList.append(xx['link'])
			# 	except Exception as e:
			# 		pass
			# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+tv+show',franchise,franchiseOmit):
			# 	try:
			# 		theList.append(xx['link'])
			# 	except Exception as e:
			# 		pass






	# theList.append('http://www.imdb.com/list/ls025172800/')
	# theList.append('http://www.imdb.com/list/ls056346625/?sort=list_order,asc&st_dt=&mode=detail&page=1')
	# theList.append('http://www.imdb.com/list/ls056346625/?sort=list_order,asc&st_dt=&mode=detail&page=2')
	# theList.append('http://www.imdb.com/list/ls027316430/')
	# theList.append('http://www.imdb.com/list/ls027937692/')
	# print(set(theList))
	# sys.exit()
	_.saveTable(theList,'imdb_hallmark_auto_research_theList.json')
	print('Lists:',len(theList))
	badIDs = 'ls076776375,ls066936786,ls076572568,ls074285945,ls070895912'
	badText = 'feel like,lifetime'
	dup = []
	dup2 = []
	# hallmarkDataRaw = []
	hallmarkDataRaw = _.getTable('imdb_hallmark_auto_tmp.json')
	if len(hallmarkDataRaw) == 0:
		for lnk in theList:
			thisID = getIdFromUrl(lnk['link'])
			# print(thisID)
			if not thisID in dup:
				dup.append(thisID)
				if not lnk['name'].lower() in badText.split(',') and not thisID in badIDs.split(','):
					print(lnk['link'].replace('https://www.imdb.com/','').replace('http://www.imdb.com/',''),lnk['name'].replace(' - IMDb','').replace('IMDb','').replace('imdb','').replace('IMDB',''))
					for xx in buildUrlList(lnk['link'],True):
						# print(xx)
						try:
							if not str(xx['id']) in dup2:
								dup2.append(str(xx['id']))
								hallmarkDataRaw.append(xx)
						except Exception as e:
							pass
					print('Total So Far:',len(buildUrlListDuplicate),len(hallmarkDataRaw))
					_.saveTable(buildUrlListDuplicate,'imdb_hallmark_auto_complated_IDs.json')
					print()
	# print(hallmarkDataRaw)
	print(len(hallmarkDataRaw))
	_.saveTable(hallmarkDataRaw,'imdb_hallmark_auto_tmp.json')
	# pause = input('pause')
	os.system('cls')
	# pause = input('pause')
	# hallmark.append({'name': nameFix, 'year': year, 'link': movieURL, 'people': []})
	# _.tables.register('hallmarkraw',hallmarkDataRaw)
	# _.tables.print('hallmarkraw','year,name,link')
	# sys.exit()
def buildHallmarkTable2():
	global hallmark
	def duplicateCheck(theID):
		result = False
		for hm in hallmark:
			if getIdFromUrl(hm['link']) == theID:
				result = True
		return result
	# def duplicateCheck(name,year):
	# 	result = False
	# 	for hm in hallmark:
	# 		if hm['name'] == name and hm['year'] == year:
	# 			result = True
	# 	return result
	

	def buildTableH(url):
		print(url)
		page = requests.get(url)
		tree = html.fromstring(page.content)
		try:
			movieTitle = tree.cssselect('h3')
			for item in movieTitle:
				try:
					links = item.cssselect('a')
					link = str(links[0].attrib['href'])
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
 
				bad = ('Activity',' Your Friends','Lists by','Viewed','Everywhere','IMDb on','Lists by chantelssecret')
				# if not nameFix in bad:
				if len(year) > 2:
					print(year,nameFix)
				if 'TV Movie' in name and duplicateCheck(getIdFromUrl(movieURL)) == False:
					hallmark.append({'name': nameFix, 'year': year, 'link': movieURL, 'people': []})
		except Exception as e:
			print('Error:',url)
			# sys.exit()
	if len(hallmark) < 1:
		now = datetime.datetime.now()
		# today = now.strftime("%Y-%m-%d")
		thisYear = int(str(now.strftime("%Y")))
		years = []
		years.append(thisYear+1)
		years.append(thisYear)
		for x in range(1,20):
			years.append(thisYear-x)
			
		# print(years)
		# sys.exit()
		franchise = 'hallmark'
		franchiseOmit = 'lifetime'
		theList = []
		for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+movies',franchise,franchiseOmit):
			try:
				theList.append(xx['link'])
			except Exception as e:
				pass
		# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+series',franchise,franchiseOmit):
		# 	try:
		# 		theList.append(xx['link'])
		# 	except Exception as e:
		# 		pass
		# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+tv+show',franchise,franchiseOmit):
		# 	try:
		# 		theList.append(xx['link'])
		# 	except Exception as e:
		# 		pass


		for theYear in years:
			theYear = str(theYear)
			for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+movies',franchise,franchiseOmit):
				try:
					theList.append(xx['link'])
				except Exception as e:
					pass
			# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+series',franchise,franchiseOmit):
			# 	try:
			# 		theList.append(xx['link'])
			# 	except Exception as e:
			# 		pass
			# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+tv+show',franchise,franchiseOmit):
			# 	try:
			# 		theList.append(xx['link'])
			# 	except Exception as e:
			# 		pass






		theList.append('http://www.imdb.com/list/ls025172800/')
		theList.append('http://www.imdb.com/list/ls056346625/?sort=list_order,asc&st_dt=&mode=detail&page=1')
		theList.append('http://www.imdb.com/list/ls056346625/?sort=list_order,asc&st_dt=&mode=detail&page=2')
		theList.append('http://www.imdb.com/list/ls027316430/')
		theList.append('http://www.imdb.com/list/ls027937692/')
		# print(set(theList))
		# sys.exit()
		print('Lists:',len(set(theList)))
		hallmarkIDs = []
		for hlink in set(theList):
			# buildTableH(hlink)
			for xx in buildUrlList(hlink):
				hallmarkIDs.append(xx)
		print(set(hallmarkIDs))
		print(len(set(hallmarkIDs)))
		len(hallmark)


def buildFranchisePeople():
	global hallmark
	global hallmarkDataRaw
	if len(hallmark) < 1:
		buildHallmarkTable()
		hallmark = hallmarkDataRaw
	os.system('cls')
	print()
	i = 0
	for hmk in hallmark:
		print('Building people from: ',hmk['name'])
		try:
			if len(hallmark[i]['people']) == 0:
				peepsX = getHallmarkPeople(hmk['link'])
				hallmark[i]['people'] = peepsX
				_.saveTable(hallmark,'imdb_hallmark_auto_tmp.json',True,False)
			print('People:',len(peepsX))
			print()
		except Exception as e:
			print('Error:',str(hmk['link']))
		i += 1
	hallmark = _.sort(hallmark,'year,name')
	if len(hallmark) > 100:
		print(len(hallmark))
		_.saveTable(hallmark,'hallmark.json')
		_.saveTable(hallmark,'imdb_hallmark_auto_tmp.json')
	else:
		print(len(hallmark))
		print('Unspecified Error')

def buildHallmarkPeople():
	global hallmark
	global hallmarkDataRaw
	if len(hallmark) < 1:
		buildHallmarkTable()
		hallmark = hallmarkDataRaw
	os.system('cls')
	print()
	i = 0
	for hmk in hallmark:
		print('Building people from: ',hmk['name'])
		try:
			if len(hallmark[i]['people']) == 0:
				peepsX = getHallmarkPeople(hmk['link'])
				hallmark[i]['people'] = peepsX
				_.saveTable(hallmark,'imdb_hallmark_auto_tmp.json',True,False)
			print('People:',len(peepsX))
			print()
		except Exception as e:
			print('Error:',str(hmk['link']))
		i += 1
	hallmark = _.sort(hallmark,'year,name')
	if len(hallmark) > 100:
		print(len(hallmark))
		_.saveTable(hallmark,'hallmark.json')
		_.saveTable(hallmark,'imdb_hallmark_auto_tmp.json')
	else:
		print(len(hallmark))
		print('Unspecified Error')
def getHallmarkPeople(url):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	cast = tree.cssselect('.cast_list')
	tr = cast[0].cssselect('tr')

	people = []
	for e in tr:
		try:
			char = e.cssselect('.character')
			character = cleanupString(char[0].text_content())
		except Exception as ee:
			character = ''
		props = e.cssselect('td')
		# print(len(props))
		try:
			link = ''
			links = props[1].cssselect('a')
			link = str(links[0].attrib['href'])
			person = props[1].text_content()
			person = cleanupString(person)
			people = registerPerson(people,person,link,character)
		except Exception as e:
			pass
	return people



# def getHallmarkPeople(url):
# 	page = requests.get(url)
# 	tree = html.fromstring(page.content)
# 	cast = tree.cssselect('.cast_list')
# 	tr = cast[0].cssselect('tr')

# 	people = []
# 	print(url)
# 	print(len(tr))
# 	for e in tr:
# 		try:
# 			char = e.cssselect('.character')
# 			character = cleanupString(char[0].text_content())
# 		except Exception as ee:
# 			character = ''
		
# 		props = e.cssselect('.itemprop')
# 		i = 0
# 		print(len(props))
# 		for p in props:
# 			if i == 0:
# 				link = ''
# 				try:
# 					links = p.cssselect('a')
# 					link = str(links[0].attrib['href'])
# 				except Exception as e:
# 					pass
# 				person = p.text_content()
# 				person = cleanupString(person)
# 				people = registerPerson(people,person,link,character)
# 			i += 1
# 	return people
def google(searchFor,personMovie):
	foundAlias = False
	theAliasID_imdbID = theAliasID(searchFor,personMovie,'imdbID')
	# test = input('alias: ' + theAliasID_imdbID + ' ' + personMovie)
	if len(theAliasID_imdbID) > 0:
		
		if personMovie == 'movie':
			foundAlias = True
			theURL = __.links['imdb']['cinema']['fullcredits'].replace(__.ID_HERE,theAliasID_imdbID)
			# test = input('foundAlias ' + theAliasID_imdbID + ' ' + personMovie)
			result = lookupMovie(theURL)
		if personMovie == 'person':
			foundAlias = True
			theURL = __.links['imdb']['people']['profile'].replace(__.ID_HERE,theAliasID_imdbID)
			# test = input('foundAlias ' + theAliasID_imdbID + ' ' + personMovie)
			result = lookupPerson(theURL)




		
	if not foundAlias:

		url = 'https://www.google.com/search?q=imdb+'
		newURL = url + _str.replaceAll(_str.replaceAll(searchFor,',','+'),' ','+')
		# print(newURL)
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		tables = tree.cssselect('.r')
		result = ''
		i = 0
		theList = {'movies': [],'people': []}
		def checkDup(theID):
			found = False
			for item in theList['movies']:
				if getIdFromUrl(item['link']) == theID:
					found = True
			return found

		for t in tables:
			try:
				item = t.text_content()
			except Exception as e:
				item = ''
			if 'imdb' in item.lower():
				links = t.cssselect('a')
				link = str(links[0].attrib['href'])
				link = link.replace('/url?q=http:','http:')
				text = t.text_content()
				###################################################################################################
				# print(item,link)

				if '/title/' in link:
					theURL = extractUrl(link) + 'fullcredits?ref_=tt_cl_sm#cast'
					if not checkDup(getIdFromUrl(theURL)):
						theList['movies'].append({'name': text,'link': theURL})
						# print(theList)
					
					
				if '/name/' in link:
					theURL = extractUrl(link) + '?ref_=ttfc_fc_cl_t13'
					if _.switches.isActive('KevinBacon') == True:
						kevinBacon(theURL)
					else:
						if not checkDup(getIdFromUrl(theURL)):
							theList['people'].append({'name': text,'link': theURL})
			i += 1
		if personMovie == 'series':
			episodes(theList['movies'][0]['link'])
			return getIdFromUrl(theList['movies'][0]['link'])
			
		if _.switches.isActive('Ask'):
			total = len(theList['people']) + len(theList['movies'])
			if total == 0:
				if not _.switches.isActive('Score'):
					print('0 No Results')
				sys.exit()
			elif total == 1:
				if len(theList['movies']) == 1:
					addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList[0]['link']))
					result = lookupMovie(theList[0]['link'])
				else:
					addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList[0]['link']))
					result = lookupPerson(theList[0]['link'])
			else:
				print()
				ran = False
				
				if personMovie == 'person':
					ran = True
					if len(theList['people']) > 0:
						i = 0
						for item in theList['people']:
							print(i, theList['people'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
							i += 1
						print()
						selection = input('Make Selection - ')
						print()
						if selection == 'x':
							sys.exit()
						elif not selection == 'm':
							addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList['people'][int(selection)]['link']))
							result = lookupPerson(theList['people'][int(selection)]['link'])
					else:
						selection = 'm'
						print()
						print('No people found')
						print()
				if personMovie == 'movie' or selection == 'm':
					ran = True
					if len(theList['movies']) > 0:
						i = 0
						for item in theList['movies']:
							print(i, theList['movies'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
							i += 1
						print()
						selection = input('Make Selection - ')
						print()
						if selection == 'x':
							sys.exit()
						elif not selection == 'm':
							addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList['movies'][int(selection)]['link']))
							result = lookupMovie(theList['movies'][int(selection)]['link'])
					else:
						selection = 'm'
						print()
						print('No movies found')
						print()

				elif not ran and (personMovie == 'person' or selection == 'm'):
					if len(theList['people']) > 0:
						i = 0
						for item in theList['people']:
							print(i, theList['people'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
							i += 1
						print()
						selection = input('Make Selection - ')
						print()
						if selection == 'x':
							sys.exit()
						elif not selection == 'm':
							addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList['people'][int(selection)]['link']))
							result = lookupPerson(theList['people'][int(selection)]['link'])
					else:
						selection = 'm'
						print()
						print('No people found')
						print()
		else:
			try:
				if personMovie == 'movie':
					addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList['movies'][0]['link']))
					result = lookupMovie(theList['movies'][0]['link'])
				else:
					addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList['people'][0]['link']))
					result = lookupPerson(theList['people'][0]['link'])
			except Exception as e:
				pass
			

	# return getIdFromUrl(theURL)
	if result == '':
		pass
		######################################################################################
		if not _.switches.isActive('Score'):
			print('1 No Results')
	return result

def googleID(searchFor,personMovie):

	foundAlias = False
	theAliasID_imdbID = theAliasID(searchFor,personMovie,'imdbID')
	# test = input('alias: ' + theAliasID_imdbID + ' ' + personMovie)
	if len(theAliasID_imdbID) > 0:
		
		if personMovie == 'movie':
			foundAlias = True
			theURL = __.links['imdb']['cinema']['fullcredits'].replace(__.ID_HERE,theAliasID_imdbID)
			# test = input('foundAlias ' + theAliasID_imdbID + ' ' + personMovie)
			result = theAliasID_imdbID
		if personMovie == 'person':
			foundAlias = True
			theURL = __.links['imdb']['people']['profile'].replace(__.ID_HERE,theAliasID_imdbID)
			result = theAliasID_imdbID
			# test = input('foundAlias ' + theAliasID_imdbID + ' ' + personMovie)

		
	if not foundAlias:
		url = 'https://www.google.com/search?q=imdb+'
		newURL = url + _str.replaceAll(_str.replaceAll(searchFor,',','+'),' ','+')
		# print(newURL)
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		tables = tree.cssselect('.r')
		result = ''
		i = 0
		theList = {'movies': [],'people': []}
		def checkDup(theID):
			found = False
			for item in theList['movies']:
				if getIdFromUrl(item['link']) == theID:
					found = True
			return found

		for t in tables:
			try:
				item = t.text_content()
			except Exception as e:
				item = ''
			if 'imdb' in item.lower():
				links = t.cssselect('a')
				link = str(links[0].attrib['href'])
				link = link.replace('/url?q=http:','http:')
				text = t.text_content()
				###################################################################################################
				# print(item,link)

				if '/title/' in link:
					theURL = extractUrl(link) + 'fullcredits?ref_=tt_cl_sm#cast'
					if not checkDup(getIdFromUrl(theURL)):
						theList['movies'].append({'name': text,'link': theURL})
						# print(theList)
					
				if '/name/' in link:
					theURL = extractUrl(link) + '?ref_=ttfc_fc_cl_t13'
					if _.switches.isActive('KevinBacon') == True:
						kevinBacon(theURL)
					else:
						if not checkDup(getIdFromUrl(theURL)):
							theList['people'].append({'name': text,'link': theURL})
			i += 1

		if personMovie == 'movie':
			try:
				result = getIdFromUrl(theList['movies'][0]['link'])
				addAliasID(searchFor,personMovie,'imdbID',result)
			except Exception as e:
				pass
				# print( 'No Movie' )

		if personMovie == 'person':	
			result = getIdFromUrl(theList['people'][0]['link'])
			addAliasID(searchFor,personMovie,'imdbID',result)

	return result

def  rottenTomatoesRank(movie):
	url = 'https://www.google.com/search?q=rotten+tomatoes+rating+'
	newURL = url + _str.replaceAll(_str.replaceAll(movie,',','+'),' ','+')
	page = requests.get(newURL)
	tree = html.fromstring(page.content)
	tables = tree.cssselect('.r')
	result = ''
	i = 0
	theList = {'movies': [],'people': []}
	def checkDup(theID):
		found = False
		for item in theList['movies']:
			if getIdFromUrl(item['link']) == theID:
				found = True
		return found

	for t in tables:
		item = t.text_content()
		if 'imdb' in item.lower():
			links = t.cssselect('a')
			link = str(links[0].attrib['href'])
			link = link.replace('/url?q=http:','http:')
			text = t.text_content()
			if '/title/' in link:
				theURL = extractUrl(link) + 'fullcredits?ref_=tt_cl_sm#cast'
				if not checkDup(getIdFromUrl(theURL)):
					theList['movies'].append({'name': text,'link': theURL})
				
				
			if '/name/' in link:
				theURL = extractUrl(link) + '?ref_=ttfc_fc_cl_t13'
				if _.switches.isActive('KevinBacon') == True:
					kevinBacon(theURL)
				else:
					if not checkDup(getIdFromUrl(theURL)):
						theList['people'].append({'name': text,'link': theURL})
		i += 1
	if _.switches.isActive('Ask'):
		total = len(theList['people']) + len(theList['movies'])
		if total == 0:
			if not _.switches.isActive('Score'):
				print('2 No Results')
			sys.exit()
		elif total == 1:
			if len(theList['movies']) == 1:
				result = lookupMovie(theList[0]['link'])
			else:
				result = lookupPerson(theList[0]['link'])
		else:
			print()
			ran = False
			if personMovie == 'person':
				ran = True
				if len(theList['people']) > 0:
					i = 0
					for item in theList['people']:
						print(i, theList['people'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
						i += 1
					print()
					selection = input('Make Selection - ')
					print()
					if selection == 'x':
						sys.exit()
					elif not selection == 'm':
						result = lookupPerson(theList['people'][int(selection)]['link'])
				else:
					selection = 'm'
					print()
					print('No people found')
					print()
			if personMovie == 'movie' or selection == 'm':
				ran = True
				if len(theList['movies']) > 0:
					i = 0
					for item in theList['movies']:
						print(i, theList['movies'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
						i += 1
					print()
					selection = input('Make Selection - ')
					print()
					if selection == 'x':
						sys.exit()
					elif not selection == 'm':
						result = lookupMovie(theList['movies'][int(selection)]['link'])
				else:
					selection = 'm'
					print()
					print('No movies found')
					print()

			elif not ran and (personMovie == 'person' or selection == 'm'):
				if len(theList['people']) > 0:
					i = 0
					for item in theList['people']:
						print(i, theList['people'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
						i += 1
					print()
					selection = input('Make Selection - ')
					print()
					if selection == 'x':
						sys.exit()
					elif not selection == 'm':
						result = lookupPerson(theList['people'][int(selection)]['link'])
				else:
					selection = 'm'
					print()
					print('No people found')
					print()
	else:
		try:
			if personMovie == 'movie':
				result = lookupMovie(theList['movies'][0]['link'])
			else:
				result = lookupPerson(theList['people'][0]['link'])
		except Exception as e:
			pass
			

	# return getIdFromUrl(theURL)
	if result == '':
		if not _.switches.isActive('Score'):
			print('3 No Results')
	return result
def dataPerson(url):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	films = tree.cssselect('.filmo-category-section')
	personName = tree.cssselect('h1')
	try:
		birthDate0 = tree.cssselect('#name-born-info')
		birthDate1 = birthDate0[0].cssselect('a')
		try:
			birthDate = cleanupString(birthDate1[0].text_content())
		except Exception as e:
			birthDate = ''
		try:
			birthYear = cleanupString(birthDate1[1].text_content())
		except Exception as e:
			birthYear = ''
		try:
			birthLocation = cleanupString(birthDate1[2].text_content())
		except Exception as e:
			birthLocation = ''

		if not len(birthYear) == 4:
			for bd in birthDate1:
				d = cleanupString(bd.text_content())
				try:
					test = int(d)
				except Exception as e:
					test = 0
				if test > 1900:
					birthYear = d
		# birthDate = cleanupString(birthDate1[0].text_content())
		# birthYear = cleanupString(birthDate1[1].text_content())
		# birthLocation = cleanupString(birthDate1[2].text_content())
		year, month, day, hour, minute = time.strftime("%Y,%m,%d,%H,%M").split(',')
		age = int(year) - int(birthYear)
	except Exception as e:
		age = ''
	img0 = tree.cssselect('img')
	img = ''
	found = False
	for img1 in img0:
		img2 = img1.attrib['src']
		if '317_AL_.jpg' in img2 and not found:
			found = True
			img = img2
	for pn in personName:
		theirName0 = cleanupString(pn.text_content())
		if len(theirName0) > 0:
			theirName = theirName0
	return { 'name': theirName, 'age': age, 'img': img }

def dataMovie(url):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	movieTitle = tree.cssselect('h3')
	movieYear = tree.cssselect('.nobr')
	theTitle = cleanupString(movieTitle[0].text_content())
	try:
		theYear0 = cleanupString(movieYear[0].text_content(),False)
		theYear = theYear0.split(' ')[0].replace('(','')
	except Exception as e:
		theYear = ''

	img0 = tree.cssselect('img')
	img = ''
	found = False
	for img1 in img0:
		img2 = img1.attrib['src']
		if '268_AL_.jpg' in img2 and not found:
			found = True
			img = img2

	return { 'name': theTitle, 'year': theYear, 'img': img }
def crossReference():
	global allPeople
	global allMovies
	global relationships
	global xData
	# _.saveTable(allPeople,'imdb_people.json')
	# _.saveTable(allMovies,'imdb_movies.json')
	# _.saveTable(relationships,'imdb_relationships.json')
	relPeople = []
	relMovies = []
	relResults = []
	newResults = []
	os.system('cls')
	print('allPeople:\t',len(allPeople))
	print('allMovies:\t',len(allMovies))
	print('relationships:\t',len(relationships))
	print('xData:       \t',len(xData))
	# sys.exit()
	for rel00 in relationships:
		found = False
		for rm0 in relMovies:
			if rm0 == rel00['movieID']:
				found = True
		if not found:
			relMovies.append(rel00['movieID'])

	for rel01 in relationships:
		found = False
		for rm0 in relPeople:
			if rm0 == rel01['personID']:
				found = True
		if not found:
			relPeople.append(rel01['personID'])

	if _.switches.isActive('Movie') == True:


		for rp in relPeople:
			i = 0
			for rm in relMovies:
				for rel in relationships:
					if rel['movieID'] == rm and rel['personID'] == rp:
						i += 1
			if i == len(relMovies):
				for ap in allPeople:
					if ap['id'] == rp:
						relResults.append(ap['id'])
						# relResults.append(rp)
		os.system('cls')
		print()
		print('Cross referenceing:')
		for rm1 in relMovies:
			for am in allMovies:
				if am['id'] == rm1:
					print('\t',am['name'])
		print()
		print()


		for resID0 in set(relResults):
			found = False
			for ap2 in allPeople:
				if resID0 == ap2['id'] and not found:
					found = True
					newResults.append({'id': ap2['id'], 'name': ap2['name'], 'link': ap2['link'], })
		i = 0
		for result in newResults:
			print(i,result['name'])
			i += 1
		print()
		print(len(newResults))
	if _.switches.isActive('Person') == True:
		for rm in relMovies:
			i = 0
			for rp in relPeople:
				for rel in relationships:
					if rel['movieID'] == rm and rel['personID'] == rp:
						i += 1
			if i == len(relPeople):
				for am in allMovies:
					if am['id'] == rm:
						relResults.append(am['id'])
						# relResults.append(rp)
		os.system('cls')
		print()
		print('Cross referenceing:')
		for rm1 in relPeople:
			for ap in allPeople:
				if ap['id'] == rm1:
					print('\t',ap['name'])
		
		print()
		print()
		for resID1 in set(relResults):
			found = False
			for am2 in allMovies:
				if resID1 == am2['id'] and not found:
					found = True
					newResults.append({'id': am2['id'], 'name': am2['name'], 'link': am2['link'], })
		i = 0
		for result in newResults:
			print(i,result['name'])
			i += 1
		print()
		print(len(newResults))



	_.switches.fieldSet('BuildCrossRef','active',False)

	def makeSelection():
		print()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 'h' or selection == '?' or selection == 'help':
			print('(s)earch')
			print('page')
			print('save')
			print('not')
			print('e(x)it')

		if selection == 's' or selection == 'search':
			personMovie = input('Person OR Movie - ')
			searchFor = input('Search For - ')
			if 'p' in personMovie or 'P' in personMovie:
				personMovie = 'person'
			if 'm' in personMovie or 'M' in personMovie:
				personMovie = 'movie'
			if len(searchFor) > 0:
				selectedSomething = True
				google(searchFor,personMovie)
		if selection == 'x' or selection == 'exit':
			sys.exit()
		if selection == 'not':
			uninvited = []
			i = 0
			for xP in xData[0]['people']:
				found = False
				xPID = getIdFromUrl(xP['link'])
				for xD in xData[1]['people']:
					xDID = getIdFromUrl(xD['link'])
					if xPID == xDID:
						found = True
				if not found:
					xP['id'] = i
					uninvited.append(xP)
					i += 1
			print()
			print('Un-invited')
			print()
			_.tables.register('uninvited',uninvited)
			_.tables.print('uninvited','id,name,character')



		if selection == 'page':
			rows = []
			theFile = 'test.htm'
			file0 = _v.stmp + _v.slash + theFile
			rows.append('<html><head>')
			rows.append('<script type="text/javascript" src="http://www.pillerbeauty.com/js/jquery-1.11.3.js"></script>')
			rows.append('<script type="text/javascript" src="http://www.pillerbeauty.com/js/jquery-ui.min.js"></script>')
			rows.append('<style type="text/css">')
			rows.append('.box { display: inline-block; position: relative; min-width: 100px; margin: 10px; padding: 10px; }')
			# rows.append('.img { display:inline; padding: 10px; }')
			rows.append('</style>')
			rows.append('</head><body>')
			if _.switches.isActive('Movie') == True:
				i = 0
				for nr in newResults:
					i += 1
					status = str(i) + ' of ' +  str(len(newResults))
					_.updateLine(status)
					data = dataPerson(nr['link'])
					rows.append('<div class="box" id="' + nr['id'] + '" >')
					rows.append('<a href="' + nr['link'] + '" target="_blank" >')
					rows.append('<div class="img">')
					rows.append('<img src="' + data['img'] + '" >')
					rows.append('</div>')
					rows.append('<div class="name">')
					if len(str(data['age'])) > 0:
						rows.append(nr['name'] + ' (' + str(data['age']) + ')')
					else:
						rows.append(nr['name'])
					rows.append('</div>')
					rows.append('</a>')
					rows.append('</div>')

			if _.switches.isActive('Person') == True:
				i = 0
				for nr in newResults:
					i += 1
					status = str(i) + ' of ' +  str(len(newResults))
					_.updateLine(status)
					picPath = extractUrl(nr['link']) + '?ref_=ttfc_fc_tt'
					data = dataMovie(picPath)
					rows.append('<div class="box">')
					rows.append('<a href="' + nr['link'] + '" target="_blank" >')
					rows.append('<div class="img">')
					rows.append('<img src="' + data['img'] + '" >')
					rows.append('</div>')
					rows.append('<div class="name">')
					if len(str(data['year'])) > 0:
						rows.append(nr['name'] + ' (' + str(data['year']) + ')')
					else:
						rows.append(nr['name'])
					rows.append('</div>')
					rows.append('</a>')
					rows.append('</div>')
				rows.append('</body></html>')
			_.tempFile(rows,theFile)
			webbrowser.open('file://' + os.path.realpath(file0))
			print()
		if selection == 'save':
			global allPeople
			global allMovies
			global relationships
			_.saveTable(allPeople,'imdb_people.json')
			_.saveTable(allMovies,'imdb_movies.json')
			_.saveTable(relationships,'imdb_relationships.json')
		try:
			selectedSomething = True
			selection = int(selection)
			print()
			print(newResults[selection]['name'],' - has been selected')
			print()
			if _.switches.isActive('Movie') == True:
				lookupPerson(newResults[selection]['link'])
			if _.switches.isActive('Person') == True:
				lookupMovie(newResults[selection]['link'])
			
		except Exception as e:
			selectedSomething = False
			# print('Unspecified Error')
		if not selectedSomething:
			makeSelection()
	makeSelection()

def idRegistier(url):
	global completedIDs
	theID = getIdFromUrl(url)
	if not idCheck(theID):
		completedIDs.append(theID)
	return theID
def idCheck(theID):
	global completedIDs
	result = False
	for cid in completedIDs:
		if cid == theID:
			result = True
	return result
def lookupMini(url):
	page = requests.get(url)
	tree = html.fromstring(page.content)

	thisID = getIdFromUrl(url)
	completed = idCheck(thisID)
	if not completed:
		try:
			if 'tt' in thisID:
				theType = 'entertainment'
			else:
				theType = 'person'
		except Exception as e:
			theType = 'error'
	else:
		theType = 'completed'
	items = []


	if theType == 'person':
		films = tree.cssselect('.filmo-category-section')
		personName = tree.cssselect('h1')
		try:
			birthDate0 = tree.cssselect('#name-born-info')
			birthDate1 = birthDate0[0].cssselect('a')
			birthDate = cleanupString(birthDate1[0].text_content())
			birthYear = cleanupString(birthDate1[1].text_content())
			birthLocation = cleanupString(birthDate1[2].text_content())
			import time
			year, month, day, hour, minute = time.strftime("%Y,%m,%d,%H,%M").split(',')
			age = int(year) - int(birthYear)
		except Exception as e:
			age = ''
		img0 = tree.cssselect('img')
		img = ''
		for img1 in img0:
			img2 = img1.attrib['src']
			if '317_AL_.jpg' in img2:
				img = img2
		for pn in personName:
			theirName0 = cleanupString(pn.text_content())
			if len(theirName0) > 0:
				theName = theirName0
		# print(birthDate)
		# print(birthYear)
		# print(birthLocation)
		# print(theName)
	if theType == 'entertainment':
		movieYear = tree.cssselect('.nobr')
		try:
			theYear0 = cleanupString(movieYear[0].text_content(),False)
			theYear = theYear0.split(' ')[0].replace('(','')
			theYear = theYear.replace(')','')
			theYear = theYear.replace(' ','')
		except Exception as e:
			theYear = ''
		theTitle = cleanupString(movieTitle[0].text_content())
		theAlist = tree.cssselect('a')
		# theTitle = ''
		found = False
		for ta in theAlist:
			linkTest =ta.attrib['href']
			if '/title/tt' in linkTest and not found:
				found =True
				theTitle0 = cleanupString(ta.text_content())
				if len(theTitle0) > 1 and not 'External Sites' in theirName0 and not 'Full Cast' in theirName0:
					theName = theTitle0
		
		print(theName)
		print(theYear)

		img0 = tree.cssselect('img')
		img = ''
		for img1 in img0:
			img2 = img1.attrib['src']
			if '268_AL_.jpg' in img2:
				img = img2

		cast = tree.cssselect('.cast_list')
		tr = cast[0].cssselect('tr')

	idRegistier(url)
	return items
def kevinBacon(url):
	global KevinBaconID
	global allMovies
	global allPeople
	global allMovies
	global relationships
	global allErrors
	global completedIDs
	if _.switches.isActive('KevinBaconPickUp') == True:
		completedIDs = _.getTable('imdb_kevin_bacon_completedIDs.json')
		# allPeople = _.getTable('imdb_kevin_bacon_people.json')
		# allMovies = _.getTable('imdb_kevin_bacon_entertainment.json')
		relationships = _.getTable('imdb_kevin_bacon_relationships.json')
		allErrors = _.getTable('imdb_kevin_bacon_errors.json')
		timeAudit = _.getTable('imdb_kevin_bacon_timeAudit.json')



	millTimeStamp = lambda: int(round(time.time() * 1000))
	timeAudit = []
	timeAudit.append({'stamp': millTimeStamp(),'location': 'start'})
	_.saveTable(timeAudit,'imdb_kevin_bacon_timeAudit.json')
	_.switches.fieldSet('Single','active',True)
	_.switches.fieldSet('NoPrint','active',True)
	_.switches.fieldSet('BuildCrossRef','active',True)
	kbm = []
	kbp = []
	depth = 0
	depthMax = 7
	global errors
	errors = []
	# os.system('cls')
	def isEven(x):
		if x & 1:
		   return False
		else:
		   return True
	def done(timeAudit):
		try:
			global allPeople
			global allMovies
			global relationships
			global allErrors
		except Exception as e:
			pass
		if _.switches.value('KevinBacon') == 'build':
			_.saveTable(allPeople,'imdb_kevin_bacon_people.json')
			_.saveTable(allMovies,'imdb_kevin_bacon_entertainment.json')
			_.saveTable(relationships,'imdb_kevin_bacon_relationships.json')
			_.saveTable(allErrors,'imdb_kevin_bacon_errors.json')
			_.saveTable(timeAudit,'imdb_kevin_bacon_timeAudit.json')
		else:
			_.saveTable(allPeople,'imdb_people.json')
			_.saveTable(allMovies,'imdb_movies.json')
			_.saveTable(relationships,'imdb_relationships.json')
	def autoLink(link):
		global allErrors
		result = []
		thisID = getIdFromUrl(link)
		completed = idCheck(thisID)
		millTimeStamp = lambda: int(round(time.time() * 1000))
		if not completed:
			try:
				if 'tt' in thisID:
					result = lookupMovie(link)
				else:
					result = lookupPerson(link)
			except Exception as e:
				allErrors.append({'location': 'autoLink', 'input': link, 'stamp': millTimeStamp()})
			if len(result) == 0:
				allErrors.append({'location': 'autoLink', 'input': link, 'stamp': millTimeStamp()})
		if len(result) == 0:
			print('\trows: ',len(result))
		else:
			print('rows: ',len(result))
		return {'link': link, 'results': result}
	def getList(rows):
		theList = []
		i = 0
		for row in rows:
				thisID = getIdFromUrl(row['link'])
				completed = idCheck(thisID)
				if not completed:
					i += 1
					if True == True:
						result = autoLink(row['link'])
						if len(result) == 0:
							i = 0
						else:
							theList.append(result)
		return theList
	
	found = False
	even = []
	odd = []
	if _.switches.isActive('KevinBaconPickUp') == True:
		# evenOdd0 = _.getTable('imdb_kevin_bacon_even.json')
		# evenOdd1 = _.getTable('imdb_kevin_bacon_odd.json')
		# if len(evenOdd0) > len(evenOdd1):
		# 	even = evenOdd0
		# 	odd = evenOdd1
		# else:
		# 	odd = evenOdd0
		# 	even = evenOdd1
		# evenOdd0 = []
		# evenOdd1 = []
		odd = []
		even = _.getTable('imdb_kevin_bacon_even.json')
		print('people',len(allPeople))
		print('entertainment',len(allMovies))
		print('relationships',len(relationships))
		print('completedIDs',len(completedIDs))
		print('even',len(even))
		print('odd',len(odd))

	else:
		even.append(autoLink(url))
	# for ev in even:
	# 	print(ev['name'])
	# sys.exit()
	iii = 0
	j = 0
	while not found:
		iii += 1
		print('______________________')
		print('Nest Set:',iii)
		print()
		j += .5
		# jf = str(j).replace('.0','').replace('0.','.')
		
		# print(isEven(i))
		bacon = []
		if isEven(iii):
			total = 0
			for items in odd:
				total += len(items['results'])

			timeAudit.append({'stamp': millTimeStamp(),'location': 'even processing odd creating even','loop': iii, 'count': len(odd), 'dimensionalCount': total, 'degrees': j})
			_.saveTable(timeAudit,'imdb_kevin_bacon_timeAudit.json')
			if _.switches.value('KevinBacon') == 'build':
				if j == 7:
					found = True
			else:
				for LO0 in odd:
					for LOX in LO0['results']:
						try:
							if True == True and getIdFromUrl(LOX['link']) == KevinBaconID or 'Kevin' in LOX['name'] and 'Bacon' in LOX['name']:
								srcID = getIdFromUrl(LO0['link'])
								for am in allMovies:
									if am['id'] == srcID:
										bacon.append(cleanupString0(am['name']))
								found = True
						except Exception as e:
							allErrors.append({'location': 'while', 'input': LOX['link'], 'stamp': millTimeStamp()})
			if not _.switches.value('KevinBacon') == 'build':
				if found:
					print()
					print('Found Kevin Bakon')
					print()
					for kevin in set(bacon):
						print('\t',kevin)
					print()
					print('\t\t',j, 'Degrees to Kevin Bakon')
					sys.exit()
			even=[]
			xx = 0
			if _.switches.value('KevinBacon') == 'build':
				_.saveTable(odd,'imdb_kevin_bacon_odd.json')
			eoi = 0
			isFirst = True
			for LO0 in odd:
				xx += 1
				if len(LO0['results']) > 0:
					if eoi > 0:
						eoi = 0
						_.saveTable({'name': resolveName(LO0['link']), 'count': xx, 'dimensionalCount': len(LO0['results']), },'imdb_kevin_bacon_current.json')
					i = 0
					for LO1 in LO0['results']:

						try:
							i += 1
							if True == True:
								pass
								result = autoLink(LO1['link'])
								eoi += len(result['results'])
								if len(result['results']) == 0:
									i = 0
								else:
									if isFirst:
										isFirst = False
										_.saveTable({'name': resolveName(LO0['link']), 'count': xx, 'dimensionalCount': len(LO0['results']), },'imdb_kevin_bacon_current.json')
									even.append(result)
									print('______________________','\n')
						except Exception as e:
							allErrors.append({'location': 'while', 'input': LOX['link'], 'stamp': millTimeStamp()})
					if len(even) > 0 and eoi > 0 and _.switches.value('KevinBacon') == 'build':
						_.saveTable(completedIDs,'imdb_kevin_bacon_completedIDs.json')
						_.saveTable(odd,'imdb_kevin_bacon_odd.json')
						_.saveTable(allErrors,'imdb_kevin_bacon_errors.json')
						_.saveTable(allPeople,'imdb_kevin_bacon_people.json')
						_.saveTable(relationships,'imdb_kevin_bacon_relationships.json')
				else:
					len(LO0['results'])
		else:
			total = 0
			for items in even:
				total += len(items['results'])

			timeAudit.append({'stamp': millTimeStamp(),'location': 'odd processing even creating odd','loop': iii, 'count': len(even), 'dimensionalCount': total, 'degrees': j})
			_.saveTable(timeAudit,'imdb_kevin_bacon_timeAudit.json')
			if not _.switches.value('KevinBacon') == 'build':
				for LO0 in even:
					for LOX in LO0['results']:
						try:
							if True == True and getIdFromUrl(LOX['link']) == KevinBaconID or 'Kevin' in LOX['name'] and 'Bacon' in LOX['name']:
								srcID = getIdFromUrl(LO0['link'])
								for am in allMovies:
									if am['id'] == srcID:
										bacon.append(cleanupString0(am['name']))
								found = True
						except Exception as e:
							pass
			if not _.switches.value('KevinBacon') == 'build':			
				if found:
					print()
					print('Found Kevin Bakon')
					print()
					for kevin in set(bacon):
						print('\t',kevin)
					print()
					print('\t\t',j, 'Degrees to Kevin Bakon')
					sys.exit()
			if _.switches.isActive('KevinBaconPickUp') == True and iii == 1:
				print('odd',len(odd))
			else:
				odd=[]
			xx = 0
			if _.switches.value('KevinBacon') == 'build':
				_.saveTable(even,'imdb_kevin_bacon_even.json')
			eoi = 0
			isFirst = True
			for LO0 in even:
				xx += 1
				if len(LO0['results']) > 0:
					if eoi > 0:
						eoi = 0
						_.saveTable({'name': resolveName(LO0['link']), 'count': xx, 'dimensionalCount': len(LO0['results']), },'imdb_kevin_bacon_current.json')
					i = 0
					for LO1 in LO0['results']:

						try:
							i += 1
							if True == True:
								pass
								result = autoLink(LO1['link'])
								eoi += len(result['results'])
								if len(result['results']) == 0:
									i = 0
								else:
									if isFirst:
										isFirst = False
										_.saveTable({'name': resolveName(LO0['link']), 'count': xx, 'dimensionalCount': len(LO0['results']), },'imdb_kevin_bacon_current.json')
									odd.append(result)
									print('______________________','\n')
						except Exception as e:
							allErrors.append({'location': 'while', 'input': LOX['link'], 'stamp': millTimeStamp()})
					# print(len(odd),eoi,_.switches.value('KevinBacon'))
					if len(odd) > 0 and eoi > 0 and _.switches.value('KevinBacon') == 'build':
						_.saveTable(completedIDs,'imdb_kevin_bacon_completedIDs.json')
						_.saveTable(odd,'imdb_kevin_bacon_odd.json')
						_.saveTable(allErrors,'imdb_kevin_bacon_errors.json')
						_.saveTable(allPeople,'imdb_kevin_bacon_people.json')
						_.saveTable(relationships,'imdb_kevin_bacon_relationships.json')
				else:
					len(LO0['results'])
				
		if _.switches.value('KevinBacon') == 'build':
			_.saveTable(completedIDs,'imdb_kevin_bacon_completedIDs.json')
			_.saveTable(allPeople,'imdb_kevin_bacon_people.json')
			_.saveTable(allMovies,'imdb_kevin_bacon_entertainment.json')
			_.saveTable(relationships,'imdb_kevin_bacon_relationships.json')
			_.saveTable(allErrors,'imdb_kevin_bacon_errors.json')
			_.saveTable(timeAudit,'imdb_kevin_bacon_timeAudit.json')
	if _.switches.value('KevinBacon') == 'build':
		timeAudit.append({'stamp': millTimeStamp(),'location': 'end'})
		_.saveTable(timeAudit,'imdb_kevin_bacon_timeAudit.json')
	# done(timeAudit)
def resolveName(link_or_id_or_json):
	global allMovies
	global allPeople
	global allErrors

	done = False
	result = ''
	if type(link_or_id_or_json) == str:
		if '/' in link_or_id_or_json:
			srcID = getIdFromUrl(link_or_id_or_json)
		else:
			srcID = link_or_id_or_json
		if 'tt' in srcID:
			allItems = allMovies
		else:
			allItems = allPeople
		thisItemFound = False
		for item in allItems:
			if item['id'] == srcID and not thisItemFound:
				thisItemFound = True
				result = item['name']
	else:
		if type(link_or_id_or_json[0]) == str:
			result = []
			for item in link_or_id_or_json:
				result.append(resolveName(item))
		if not done:
			try:
				if type(link_or_id_or_json[0][0]['link']) == str:
					typeFound = True
				else:
					typeFound = False
			except Exception as e:
				typeFound = False
			if typeFound:
				done = False
				result = []
				for item0 in link_or_id_or_json:
					for item1 in item0:
						result.append(resolveName(item1['link']))
		if not done:
			try:
				if type(link_or_id_or_json[0]['link']) == str:
					typeFound = True
				else:
					typeFound = False
			except Exception as e:
				typeFound = False
			if typeFound:
				done = False
				result = []
				for item in link_or_id_or_json:
					result.append(resolveName(item['link']))
	if result == '':
		millTimeStamp = lambda: int(round(time.time() * 1000))
		allErrors.append({'location': 'resolveName', 'input': link_or_id_or_json, 'stamp': millTimeStamp()})
	return result

def crossReferenceDepth(back):
	global allPeople
	global allMovies
	global relationships
	if not back:
		valueX = _.switches.value('BuildCrossRef')
		_.switches.fieldSet('BuildCrossRef','value','skip')
		misteryPerson = google(_.switches.value('Movie'),'movie')
		_.tables.register('The_Mistery_Person',misteryPerson)
		_.switches.fieldSet('BuildCrossRef','value',valueX)
		person = google(_.switches.value('Person'),'person')
		done = False
		for ent in person['movies']:
			if not done:
				thisMovie = lookupMovie(ent['link'])
				if _.switches.value('BuildCrossRef') == 'one':
					for ap in thisMovie['people']:
						for mp in misteryPerson['people']:
							if not done and getIdFromUrl(ap['link']) == getIdFromUrl(mp['link']):
								os.system('cls')
								print()
								print(ap['name'])
								webbrowser.open(ap['link'])
								selection = input('Continue (y/n)- ')
								if selection == 'n':
									done = True
	os.system('cls')
	print()
	misteryPerson = _.tables.asset('The_Mistery_Person')
	def thisIdCheck(theID):
		found = False
		for nr in newResults:
			if nr['id'] == theID:
				found = True
		return found
	newResults = []
	for ap in allPeople:
		for mp in misteryPerson['people']:
			if ap['id'] == getIdFromUrl(mp['link']):
				if not thisIdCheck(ap['id']):
					newResults.append({'id': ap['id'], 'name': ap['name'], 'link': ap['link']})

	i = 0
	for result in newResults:
		print(i,result['name'])
		i += 1
	print()
	print(len(newResults))



	_.switches.fieldSet('BuildCrossRef','active',False)
	def makeSelection():
		print()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 'h' or selection == '?' or selection == 'help':
			print('(s)earch')
			print('e(x)it')
			print('save')
			print('page')
		if selection == 's' or selection == 'search':
			personMovie = input('Person OR Movie - ')
			searchFor = input('Search For - ')
			if 'p' in personMovie or 'P' in personMovie:
				personMovie = 'person'
			if 'm' in personMovie or 'M' in personMovie:
				personMovie = 'movie'
			if len(searchFor) > 0:
				selectedSomething = True
				google(searchFor,personMovie)
		if selection == 'x' or selection == 'exit':
			sys.exit()
		if selection == 'page':
			rows = []
			theFile = 'test.htm'
			file0 = _v.stmp + _v.slash + theFile
			rows.append('<html><head>')
			rows.append('<script type="text/javascript" src="http://www.pillerbeauty.com/js/jquery-1.11.3.js"></script>')
			rows.append('<script type="text/javascript" src="http://www.pillerbeauty.com/js/jquery-ui.min.js"></script>')
			rows.append('<style type="text/css">')
			rows.append('.box { display: inline-block; position: relative; min-width: 100px; margin: 10px; padding: 10px; }')
			# rows.append('.img { display:inline; padding: 10px; }')
			rows.append('</style>')
			rows.append('</head><body>')
			if _.switches.isActive('Movie') == True:
				i = 0
				for nr in newResults:
					i += 1
					status = str(i) + ' of ' +  str(len(newResults))
					_.updateLine(status)
					data = dataPerson(nr['link'])
					rows.append('<div class="box" id="' + nr['id'] + '" >')
					rows.append('<a href="' + nr['link'] + '" target="_blank" >')
					rows.append('<div class="img">')
					rows.append('<img src="' + data['img'] + '" >')
					rows.append('</div>')
					rows.append('<div class="name">')
					if len(str(data['age'])) > 0:
						rows.append(nr['name'] + ' (' + str(data['age']) + ')')
					else:
						rows.append(nr['name'])
					rows.append('</div>')
					rows.append('</a>')
					rows.append('</div>')

			if _.switches.isActive('Person') == True:
				i = 0
				for nr in newResults:
					i += 1
					status = str(i) + ' of ' +  str(len(newResults))
					_.updateLine(status)
					picPath = extractUrl(nr['link']) + '?ref_=ttfc_fc_tt'
					data = dataMovie(picPath)
					rows.append('<div class="box">')
					rows.append('<a href="' + nr['link'] + '" target="_blank" >')
					rows.append('<div class="img">')
					rows.append('<img src="' + data['img'] + '" >')
					rows.append('</div>')
					rows.append('<div class="name">')
					if len(str(data['year'])) > 0:
						rows.append(nr['name'] + ' (' + str(data['year']) + ')')
					else:
						rows.append(nr['name'])
					rows.append('</div>')
					rows.append('</a>')
					rows.append('</div>')
				rows.append('</body></html>')
			_.tempFile(rows,theFile)
			webbrowser.open('file://' + os.path.realpath(file0))
			print()
		if selection == 'p' or selection == 'pic':
			webbrowser.open(img, new=2)
		if selection == 'save':
			global allPeople
			global allMovies
			global relationships
			_.saveTable(allPeople,'imdb_people.json')
			_.saveTable(allMovies,'imdb_movies.json')
			_.saveTable(relationships,'imdb_relationships.json')
		try:
			selectedSomething = True
			selection = int(selection)
			print()
			print(newResults[selection]['name'],' - has been selected')
			print()
			if _.switches.isActive('Movie') == True:
				lookupPerson(newResults[selection]['link'])
			if _.switches.isActive('Person') == True:
				lookupMovie(newResults[selection]['link'])
			
		except Exception as e:
			selectedSomething = False
			# print('Unspecified Error')
		if not selectedSomething:
			makeSelection()
	makeSelection()

xData = []
def action():
	global xData
	if _.switches.isActive('BuildCrossRef') == True:
		if _.switches.isActive('Episode'):
			iDs = []
			for series in _.switches.value('Movie').split(',and,'):
				iDs.append(google(series,'series'))
			crossReferenceEpisodes(iDs)
		elif _.switches.isActive('Movie') == True and _.switches.isActive('Person') == True:
			crossReferenceDepth(False)

		elif _.switches.isActive('Movie') == True:
			for flick in _.switches.value('Movie').split(',and,'):
				xData.append(google(flick,'movie'))
			# os.system('cls')
			# print(len(xData[0]['people']),len(xData[1]['people']))
			# sys.exit()
			crossReference()
		elif _.switches.isActive('Person') == True:
			for person0 in _.switches.value('Person').split(',and,'):
				google(person0,'person')
			crossReference()

	elif _.switches.isActive('Movie') == True:
		google(_.switches.value('Movie'),'movie')


	elif _.switches.isActive('Person') == True:
		google(_.switches.value('Person'),'person')


	elif _.switches.isActive('Hallmark') == True:
		global hallmark
		if _.switches.isActive('Plus') == True:
			hallmark = _.getTable('hallmark.json')
			hallmark = _.sort(hallmark,'year,name')
			theMovies = []
			for hmk in hallmark:
				if _.showLine(hmk['name']) == True:
					theMovies.append(hmk)

			if len(theMovies) == 1:
				view = 0
				if _.switches.isActive('HallmarkView') == True:
					view = 1
				print()
				print(theMovies[0]['year'],theMovies[0]['name'])
				print()
				peepsLengthMax = 0
				for peeps0 in theMovies[0]['people']:
					length = len(peeps0['name'])
					if length > peepsLengthMax:
						peepsLengthMax = length
				if view == 1:
					for peeps0 in theMovies[0]['people']:
						
						peepsLengthDiff = peepsLengthMax - len(peeps0['name'])
						peepsLengthSpacer = ''
						ix = 0
						while ix < peepsLengthDiff:
							peepsLengthSpacer += ' '
							ix += 1



						print('\t',peeps0['name'],peepsLengthSpacer+'\t','(' + peeps0['character'] + ')')
				else:
					_.tables.register('Auto',theMovies[0]['people'])
					_.tables.print('Auto','name')
				print('_____________________________________________________')
				hallmarkCharecters = []
				for peeps1 in theMovies[0]['people']:
					
					found = False
					jj = 0
					peepsLengthMax = 0
					for hm in hallmark:
						for peeps2 in hm['people']:
							if peeps1['name'] == peeps2['name'] and not hm['name'] == theMovies[0]['name']:
								# print(hm['name'])
								length = len(hm['name'])
								if length > peepsLengthMax:
									peepsLengthMax = length
					for hm in hallmark:
						for peeps2 in hm['people']:
							if peeps1['name'] == peeps2['name'] and not hm['name'] == theMovies[0]['name']:
								if found == False:
									pass
									if view == 1:
										print()
										print('\t',peeps1['name'])
								if view == 1:
									peepsLengthDiff = peepsLengthMax - len(hm['name'])
									peepsLengthSpacer = ''
									ix = 0
									while ix < peepsLengthDiff:
										peepsLengthSpacer += ' '
										ix += 1
									print('\t\t ',hm['year'],hm['name'],peepsLengthSpacer+'\t','(' + peeps2['character'] + ')')
								else:
									hallmarkCharecters.append({'name': str(peeps1['name']), 'year': hm['year'], 'movie': hm['name'], 'character': peeps2['character'], })
								jj += 1
								found = True
					if found:
						pass
						if view == 1:
							print('\t\t',jj)
							print()
					else:
						pass
						# print('\t',peeps1['name'])
				if view == 0:
					_.groupSeparator = ''
					_.switches.fieldSet('Long','active',True)
					_.switches.fieldSet('Long','value','movie,character')
					_.switches.fieldSet('GroupBy','active',True)
					_.switches.fieldSet('GroupBy','value','name')
					_.tables.register('Char',hallmarkCharecters)
					# print(hallmarkCharecters)
					# for hc in hallmarkCharecters:
						# print(hc['name'])
					_.tables.print('Char','name,year,movie,character')
					# _.tables.print('Char','name')


			if len(theMovies) > 1:
				print()
				_.switches.fieldSet('Long','active',True)
				_.switches.fieldSet('Long','value','name')
				_.switches.fieldSet('Sort','active',True)
				_.switches.fieldSet('Sort','value','year')
				_.tables.register('Auto',theMovies)
				_.tables.print('Auto','year,name')
				print()
				print(len(theMovies))
		else:
			if _.switches.value('Hallmark') == 'buildPeople':
				buildHallmarkPeople()
			else:
				hallmark = _.getTable('hallmark.json')

				_.switches.fieldSet('Long','active',True)
				_.switches.fieldSet('Long','value','name')
				_.switches.fieldSet('Sort','active',True)
				_.switches.fieldSet('Sort','value','year')
				_.tables.register('Auto',hallmark)
				_.tables.print('Auto','year,name')
				print()
				print(len(hallmark))



########################################################################################
######################################################################################## ########################################################################################
########################################################################################








class TheFeature:

	def __init__(self, imdbID):
		self.location = []
		if _.switches.isActive('Location'):
			self.location.append(_.switches.value('Location'))

		self.watched = []
		if _.switches.isActive('Watched'):
			self.watched.append( _.switches.value('Watched') )

		self.img_small = ''
		self.img_large = ''

		self.imdbID = imdbID
		self.name = ''

		self.isMovie = True
		self.isTV = False

		self.year = 0
		self.yearStart = 0
		self.yearEnd = 0

		self.expirationDateDefault = 0

		self.pages = []

		self.rating = 0.0

		self.acquisition = {
							'fullcredits': {'acquired': 0,'expires': 0,},
							'seasons': {'acquired': 0,'expires': 0,},
							'rating': {'acquired': 0,'expires': 0,},
						}
	def acquisitionDataReset(self):
		try:
			self.acquisition['seasons']['acquired']
		except Exception as e:
			print('Reset acquisition data')
			self.acquisition = {
								'fullcredits': {'acquired': 0,'expires': 0,},
								'seasons': {'acquired': 0,'expires': 0,},
								'rating': {'acquired': 0,'expires': 0,},
							}
	def setYear(self,year):
		year = str(year)
		year = year.replace(' ','')
		n = '0123456789-'
		y = ''

		for x in year:
			if x in n:
				y += x
		year = y

		if not '-' in year:
			self.isMovie = True
			self.isTV = False
			self.year = year
		else:
			self.isMovie = False
			self.isTV = True
			self.year = year
			self.yearStart = year.split('-')[0]
			if year.endswith('-'):
				self.yearEnd = 0
			else:
				self.yearEnd = year.split('-')[1]



	# def hasExpiration(self):
	# 	result = True
	# 	if not self.isCanceled():


	def dump(self):
		with open(self.objFile(), 'wb') as objSelf:
		    pickle.dump(self, objSelf, pickle.HIGHEST_PROTOCOL)

	def objFile(self):
		return __.objectLocation['objects'].replace(__.ID_HERE,self.imdbID)

	def isCanceled( self ):
		if len(str( self.year )) > 2:
			self.setYear( self.year )
		if self.isTV:
			if len(str(self.year)) > 2:
				if int(self.yearStart) > int(self.yearEnd):
					result = False
				else:
					result = True
			else:
				pass

		else:
			result = True
		return result

	def defaultExpiration( self ):
		shouldSet = False
		try:
			if self.expirationDateDefault < 30:
				shouldSet = True
		except Exception as e:
			shouldSet = True

		if shouldSet:
			if not len(str( self.year )) > 2:
				self.expirationDateDefault = 7
			else:
				
				if self.isCanceled():
					self.expirationDateDefault = 730
		try:
			self.expirationDateDefault
		except Exception as e:
			self.expirationDateDefault = 0

		return _.dateAdd2( time.time() , self.expirationDateDefault )



	def validateFields( self, section='seasons' ):

		
		try:
			self.acquisition[section]['acquired']
			self.acquisition[section]['expires']
		except Exception as e:
			self.acquisitionDataReset()
			
	def isExpired( self, section ):
		done = False
		self.validateFields( section )

		if self.acquisition[section]['acquired'] == 0:
			done = True
			result = True
		if not done:
			dateDiff = _.dateDiff( time.time(), self.defaultExpiration() )
			if dateDiff < 0:
				done = True
				result = True

		if not done:
			expirationDate = self.acquisition[section]['expires']
			if expirationDate == 0:
				result = True
			else:
				tillExpire = _.dateDiff( _.float2Date3B( time.time(), False ), expirationDate, '-' )
				if tillExpire > 0:
					result = False
				else:
					result = True
		return result
	def seasonStartsDate(self,newDate):
		if not newDate == 0:
			newDate = str(newDate)
			newStartDate = _.dateSub(newDate,'-',14)
			sData = self.showInSeason(False)
		# {'inSeason': self.inSeason, 'lastDate': lastDate , 'expiration':  expirationDate}
		if newDate == 0:
			self.acquisition['seasons']['expires'] = 0
			print('Successfully reset expiration ')
		else:
			if not self.inSeason:
				self.acquisition['seasons']['expires'] = str(newStartDate)
				print('Success: set expiration for ', self.acquisition['seasons']['expires'] + ' 14 days before ' + newDate)
	def get_seasons(self):
		# if not 'seasons' in self.pages:
		# if True:
		if self.isExpired('seasons'):
			self.seasonData = get_cinema_seasons(self.imdbID)
			self.pages.append('seasons')
			self.acquisition['seasons']['acquired'] = float(time.time())

		print()
		if self.acquisition['seasons']['acquired'] == 0:
			self.acquisition['seasons']['acquired'] = float(time.time())
		self.setYear(self.seasonData[0]['year'])
		if self.name == '':
			self.name = self.seasonData[0]['title']
		print(self.seasonData[0]['year'],self.seasonData[0]['title'],'\n\n\tSeasons: ',str(len(self.seasonData[0]['seasons'])))

		print()
		for i1,season in enumerate(self.seasonData[0]['seasons']):
			print()
			print('Season: ', season['season'])
			for i2,episodes in enumerate(season['episodes']):
				print('\t',episodes['id'],'\t',airdateAlignRight(episodes['airdate']),'\t',episodes['title'])
		self.showInSeason(True)
	def showInSeason(self,shouldPrint=True):
		if self.isExpired('seasons'):
		# if not 'seasons' in self.pages:
		# if True:
			# print('Looking stuff up')
			self.seasonData = get_cinema_seasons(self.imdbID)
			self.pages.append('seasons')
			self.acquisition['seasons']['acquired'] = float(time.time())

		if self.acquisition['seasons']['acquired'] == 0:
			self.acquisition['seasons']['acquired'] = float(time.time())

		self.setYear(self.seasonData[0]['year'])
		if self.name == '':
			self.name = self.seasonData[0]['title']
		lastDate = ''
		diffList = []
		for i1,season in enumerate(self.seasonData[0]['seasons']):
			for i2,episodes in enumerate(season['episodes']):
				testDate = str(episodes['airdate'])
				try:
					dateDiff = _.dateDiff(lastDate,testDate,'-')
				except Exception as e:
					dateDiff = 0
				# print(dateDiff,lastDate,testDate)
				# print(dateDiff)
				if dateDiff > 100:
					diffList.append(dateDiff)
				if len(testDate) == 10:
					lastDate = testDate
		if shouldPrint:
			print()
			print()
			print('isCanceled:',str(self.isCanceled()))
		if self.isCanceled():
			ldEpoch = float(_.date2epoch(lastDate,'-'))
			if ldEpoch > time.time():
				print('show is in season')
		if not self.isCanceled():
			# print('End of season:',lastDate)
			ldEpoch = float(_.date2epoch(lastDate,'-'))
			if ldEpoch > time.time():
				self.inSeason = True
				expirationDays = 7
				expirationDate = str(_.dateAdd(_.float2Date3B(self.acquisition['seasons']['acquired'],False),'-',expirationDays))
				tillExpire = _.dateDiff(_.float2Date3B(time.time(),False),expirationDate,'-')
				# expirationDate = '2019-01-02'
				if shouldPrint:
					print('show is in season')
					print('expirationDate:',expirationDate)
					print('tillExpire:',tillExpire)
			else:
				self.inSeason = False
				expirationDays = _.listAverage(diffList)
				expirationDate = str(_.dateAdd(lastDate,'-',expirationDays))
				tillExpire = _.dateDiff(_.float2Date3B(time.time(),False),expirationDate,'-')
				if tillExpire < 1:
					expirationDays = 7
					expirationDate = str(_.dateAdd(_.float2Date3B(self.acquisition['seasons']['acquired'],False),'-',expirationDays))
					tillExpire = _.dateDiff(_.float2Date3B(time.time(),False),expirationDate,'-')
				if shouldPrint:
					print('show is not in season')
					print('expirationDate:',expirationDate)
					print('tillExpire:',tillExpire)
			self.acquisition['seasons']['expires'] = expirationDate
			self.expirationDateDefault = _.dateDiff( time.time(), expirationDate )
			print( 'self.expirationDateDefault:', self.expirationDateDefault )
			sys.exit()
			# print('isExpired:',self.isExpired('seasons'))
			result = {'inSeason': self.inSeason, 'lastDate': lastDate , 'expiration':  expirationDate}
			# print(result)
			return result
			# try:
			# 	print(lastDate)
			# 	ldEpoch = float(_.date2epoch(theDate,delim))
			# 	now = float(time.time())
			# 	if ldEpoch > now:
			# 		self.inSeason = True
			# 		print('show is in season')
			# 	else:
			# 		print('show is not in season')
			# 		self.inSeason = False
			# except Exception as e:
			# 	print('Error on lastDate:',lastDate)
	def get_ratings( self, printThis=True ):
		takeAction = False
		if not 'rating' in self.pages:
			takeAction = True
		if not float(self.rating) > 0:
			takeAction = True
		if self.rating == '':
			takeAction = True
		
		# takeAction = True
		if takeAction:

			self.rating_data = (get_cinema_ratings(self.imdbID))
			try:
				self.pages.append('rating')
				# {'rating': rating, 'name': name, 'year': year}
				self.rating = self.rating_data['rating']
				try:
					self.rating = float(self.rating)
				except Exception as e:
					self.rating = 0
			except Exception as e:
				self.rating = 0
		try:
			if len(self.rating_data['show']) > 0:
				self.isMovie = False
				self.isTV = True
				self.setYear(cleanupString(_str.onlyDigits(self.rating_data['year'])))
				if self.name == '':
					self.name = self.rating_data['name']
				if printThis:
					print(self.rating, cleanupString(_str.onlyDigits(self.rating_data['year'])),self.rating_data['show']+': ',self.rating_data['name'])
			else:
				if printThis:
					print(self.rating, cleanupString(_str.onlyDigits(self.rating_data['year'])),self.rating_data['name'])
		except Exception as e:
			if printThis:
				print(self.rating, cleanupString(_str.onlyDigits(self.rating_data['year'])),self.rating_data['name'])
		self.setYear( self.rating_data['year'] )
		# self.year = 
		self.name = self.rating_data['name']

	def get_fullcredits(self):
		shouldRun = False
		# print(self.acquisition['fullcredits']['acquired'])
		# sys.exit()

		if self.isExpired('fullcredits'):
			shouldRun = True

		if self.acquisition['fullcredits']['acquired'] < __.imdbAppearancesCaptured:
			shouldRun = True





		if shouldRun:
			self.fullcredits = get_cinema_fullcredits(self.imdbID)
			# {'name': theTitle, 'year': theYear, 'people': people}
			self.pages.append('fullcredits')
			self.acquisition['fullcredits']['acquired'] = time.time()
			self.acquisition['fullcredits']['expires'] = self.defaultExpiration()





			self.setYear(self.fullcredits['year'])
			if self.name == '':
				self.name = self.fullcredits['name']



		# os.system('cls')

	def print_fullcredits(self):
		os.system('cls')
		print(self.fullcredits['year'],self.name)
		print()
		_.tables.register('Auto',self.fullcredits['people'])
		_.tables.print('Auto','id,name,character')

	def trigger(self,script):
		self.script_trigger = script

	def changeStatus(self,newStatus):
		self.active = newStatus











class TheCinema:

	def __init__(self):

		self.childItemRows = []
		self.childItemList = []
		self.thisRow = 0.01
		self.franchiseData = False
		self.franchiseDataFix = False


	def dump(self):
		with open(__.objectLocation['cinema'], 'wb') as objCinema:
		    pickle.dump(self, objCinema, pickle.HIGHEST_PROTOCOL)

	def objFile(self, imdbID):
		return __.objectLocation['objects'].replace(__.ID_HERE,imdbID)

	def childRow(self, imdbID):
		self.thisRow = 0.01
		for i,row in enumerate(self.childItemRows):
			if self.childItemRows[i].imdbID == imdbID:
				self.thisRow = i

	def locationUpdate(self, location):
		originalLen = len(location)
		self.childItemRowsLocationUpdated = False
		if _.switches.isActive('Location'):
			newData = []
			location.append( _.switches.value('Location') )
			for row in location:
				if not row in newData:
					newData.append( row )
			location = newData
			if not originalLen == len(location):
				self.childItemRowsLocationUpdated = True
				
		# print('location:',location)
		return location


	def watchedUpdate(self, watched):
		originalLen = len(watched)
		self.childItemRowsWatchedUpdated = False
		if _.switches.isActive('Watched'):
			newData = []
			watched.append( _.switches.value('Watched') )
			for row in watched:
				if not row in newData:
					newData.append( row )
			watched = newData
			if not originalLen == len(watched):
				self.childItemRowsWatchedUpdated = True
				watched.append( watchedValue )
		# print('watched:',watched)
		return watched



	def addChild(self, imdbID):
		if not imdbID in self.childItemList:
			takeAction = True
			if not _.switches.isActive('ObjectsLoadSkip'):
				if os.path.isfile(self.objFile(imdbID)):
					objData = loadObject(self.objFile(imdbID))
					if not objData is None:
						objID = len(self.childItemRows)
						self.childItemRows.append(objData)


						try:
							self.childItemRows[objID].location = self.locationUpdate(self.childItemRows[objID].location)
						except Exception as e:
							self.childItemRows[objID].location = self.locationUpdate( [] )


						try:
							self.childItemRows[objID].watched = self.watchedUpdate(self.childItemRows[objID].watched)
						except Exception as e:
							self.childItemRows[objID].watched = self.watchedUpdate( [] )


						if self.childItemRowsLocationUpdated or self.childItemRowsWatchedUpdated:
							self.childItemRows[objID].dump()


						takeAction = False

			
			if takeAction:
				self.childItemRows.append(TheFeature(imdbID))

			self.childItemList.append(imdbID)
	def rating(self, imdbID):
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			print('Error: childRow')
			sys.exit()

		self.childItemRows[self.thisRow].get_ratings()
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
			# self.dump()

	def printLabel( self, imdbID, data=False, franchise=False ):
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			print('Error: childRow')
			sys.exit()
		self.childItemRows[self.thisRow].get_ratings(printThis=False)
		if type( data ) == bool:
			if franchise:
				print( self.inFranchise( imdbID )+'\t'+self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name )
			else:
				print( self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name )
		else:
			# print( self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name+',', data['folder']+',', data['file'] )
			if franchise:
				print( self.inFranchise( imdbID )+__.theDelim+self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name+__.theDelim+data['folder']+__.theDelim+data['file']+__.theDelim+str(data['mod'])+__.theDelim+str(data['bytes'])+__.theDelim+_.formatSize(data['bytes'])+__.theDelim+imdbID )
			else:
				print( self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name+__.theDelim+data['folder']+__.theDelim+data['file']+__.theDelim+str(data['mod'])+__.theDelim+str(data['bytes']) )


	def franchiseProper( self, name ):
		if type( self.franchiseDataFix ) == bool:
			self.franchiseDataFix = _.getTable('imdb_franchise_display.json')

		for fdp in self.franchiseDataFix:
			if name == fdp['actual']:
				return fdp['proper']

		return name.replace( '_', ' ' ).title()

	def inFranchise( self, imdbID ):
		if type( self.franchiseData ) == bool:
			self.franchiseData = _.getTable('imdb_franchises.json')

		franchiseList = []
		omit = [ '_date', '_list' ]
		if len( self.franchiseData ):
			for k in self.franchiseData[0].keys():
				shouldInclude = True
				for ot in omit:
					if ot in k:
						shouldInclude = False
				if shouldInclude:
					franchiseList.append( k )
					# franchiseList.append( { 'actual': k, 'proper': k.replace( '_', ' ' ).title() } )
					# print( self.franchiseProper( k ) )
			if len( franchiseList ):
				for f in franchiseList:
					if imdbID in self.franchiseData[0][f]:
						return self.franchiseProper( f )


			# print( k )

		# _.saveTable( franchiseList,'imdb_franchise_display.json' )
		# sys.exit()
		return ''


	def seasons(self, imdbID):
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			print('Error: childRow')
			sys.exit()

		self.childItemRows[self.thisRow].get_seasons()
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
			# self.dump()

	def seasonsStarts(self, imdbID, theDate, theFormat = 'ymd'):
		if theDate == '0':
			startDate = 0
		else:
			startDate = _.figureOutDate(str(theDate), theFormat)
		
		# print(startDate)
		# print(newStartDate)
		# sys.exit()
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			print('Error: childRow')
			sys.exit()

		self.childItemRows[self.thisRow].seasonStartsDate(startDate)
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
			# self.dump()


	def inSeason(self, imdbID):
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			print('Error: childRow')
			sys.exit()

		self.childItemRows[self.thisRow].showInSeason(True)
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
			# self.dump()

	def register(self, imdbID, shouldPrint):
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			print('Error: childRow')
			sys.exit()

		self.childItemRows[self.thisRow].get_fullcredits()
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
			# self.dump()
		if shouldPrint:
			self.childItemRows[self.thisRow].print_fullcredits()
	def print(self):
		childItems = []
		for ci in self.childItemRows:
			childItems.append({'name':ci.name})
		_.tables.register('childClassItems',childItems)
		_.tables.print('childClassItems','name')
	def printStatus(self):
		childItems = []
		for ci in self.childItemRows:
			if ci.active:
				active = 'True'
			else:
				active = 'False'
			value = ci.value
			if ci.value == True:
				value = 'True'
			elif ci.value == False:
				value = 'False'

			childItems.append({'name':ci.name ,'active':active,'value': value})
		_.tables.register('childClassItems',childItems)
		_.tables.print('childClassItems','name,active,value')
	def status(self,name,newStatus):
		for i,ci in enumerate(self.childItemRows):
			if ci.name == name:
				self.childItemRows[i].changeStatus(newStatus)




######################################################################################## ########################################################################################







class ThePerson:
	
	def __init__(self, imdbID):


		self.img_small = ''
		self.img_large = ''

		self.features = []
		self.imdbID = imdbID
		self.name = ''
		self.birthDate = ''
		self.birthLocation = ''
		self.birthYear = ''
		self.age = 0

	def dump(self):
		with open(self.objFile(), 'wb') as objSelf:
		    pickle.dump(self, objSelf, pickle.HIGHEST_PROTOCOL)
		    
	def objFile(self):
		return __.objectLocation['objects'].replace(__.ID_HERE,self.imdbID)

	def trigger(self,script):
		self.script_trigger = script

	def calculateAge(self):
		year, month, day, hour, minute = time.strftime("%Y,%m,%d,%H,%M").split(',')
		self.age = int(year) - int(self.birthYear)

	def registerFeatures(self, imdbIDF):
		self.childItemRows.append(TheChildItems(name))


# {'id': iiii, 'name': title, 'year': year, 'link': link, 'img': img, 'age': gigAge}









class ThePeople:

	def __init__(self):

		
		self.childItemRows = []
		self.childItemList = []


	def register(self, imdbID):
		if not '' in self.childItemList:
			self.childItemList.append(imdbID)
			self.childItemRows.append(ThePerson(imdbID))
			if not _.switches.isActive('ObjectsLoadSkip'):
				self.childItemRows[self.thisRow].dump()
				# self.dump()



	def dump(self):
		with open(__.objectLocation['people'], 'wb') as objPeople:
		    pickle.dump(self, objPeople, pickle.HIGHEST_PROTOCOL)
		    
	def addChild(self, imdbID):
		if not imdbID in self.childItemList:
			takeAction = True
			if not _.switches.isActive('ObjectsLoadSkip'):
				if os.path.isfile(self.objFile(imdbID)):
					objData = loadObject(self.objFile(imdbID))
					if not objData is None:
						self.childItemRows.append(objData)
						takeAction = False

			self.childItemList.append(imdbID)
			if takeAction:
				self.childItemRows.append(TheFeature(imdbID))

	def print(self):
		childItems = []
		for ci in self.childItemRows:
			childItems.append({'name':ci.name})
		_.tables.register('childClassItems',childItems)
		# tables.trigger('switches','switch,name',test,True)
		_.tables.print('childClassItems','name')
	def printStatus(self):
		childItems = []
		for ci in self.childItemRows:
			if ci.active:
				active = 'True'
			else:
				active = 'False'
			value = ci.value
			if ci.value == True:
				value = 'True'
			elif ci.value == False:
				value = 'False'

			childItems.append({'name':ci.name ,'active':active,'value': value})
		_.tables.register('childClassItems',childItems)
		_.tables.print('childClassItems','name,active,value')
	def status(self,name,newStatus):
		for i,ci in enumerate(self.childItemRows):
			if ci.name == name:
				self.childItemRows[i].changeStatus(newStatus)






########################################################################################
######################################################################################## ########################################################################################
########################################################################################

# NEW FUNC


def get_people_profile(imdbID):
	urlBase = __.links['imdb']['people']['profile']
	url = urlBase.replace(__.ID_HERE,imdbID)
	thisPersonID = imdbID

	page = requests.get(url)
	tree = html.fromstring(page.content)
	films = tree.cssselect('.filmo-category-section')
	
	movies = []

	personName = tree.cssselect('h1')
	try:
		birthDate0 = tree.cssselect('#name-born-info')
		birthDate1 = birthDate0[0].cssselect('a')
		try:
			birthDate = cleanupString(birthDate1[0].text_content())
		except Exception as e:
			birthDate = ''
		try:
			birthYear = cleanupString(birthDate1[1].text_content())
		except Exception as e:
			birthYear = ''
		try:
			birthLocation = cleanupString(birthDate1[2].text_content())
		except Exception as e:
			birthLocation = ''

		if not len(birthYear) == 4:
			for bd in birthDate1:
				d = cleanupString(bd.text_content())
				try:
					test = int(d)
				except Exception as e:
					test = 0
				if test > 1900:
					birthYear = d

		
		year, month, day, hour, minute = time.strftime("%Y,%m,%d,%H,%M").split(',')
		age = int(year) - int(birthYear)
	except Exception as e:
		age = ''

	# print(birthDate)
	# print(birthYear)
	# print(birthLocation)
	img0 = tree.cssselect('img')
	img = ''
	for img1 in img0:
		img2 = img1.attrib['src']
		if '317_AL_.jpg' in img2:
			img = img2
	for pn in personName:
		theirName0 = cleanupString(pn.text_content())
		if len(theirName0) > 0:
			theirName = theirName0
			print('Processing', theirName,'...')
	# pause = input('pause')
	if _.switches.isActive('Hallmark') == True:
		if len(hallmark) < 1:
			buildHallmarkTable()
	def ageAtTheTime(gigYear):
		gigAge = ''
		if '-' in gigYear:
			gigYearSplit = gigYear.split('-')
			gigAge = str(ageAtTheTime(gigYearSplit[0])) + '-' + str(ageAtTheTime(gigYearSplit[1]))
		else:
			if int(birthYear) > 0 and int(gigYear) > 0:
				gigAge = int(gigYear) - int(birthYear)
		return gigAge

	j = 0
	i = 0
	iHallmark = 0
	for f in films:
		iii = 0
		iiii = 0
		j += 1
		for ff in f.getchildren():
			ii = 0
			for chillin in ff.getchildren():
				if ii == 1:
					title = cleanupString(chillin.text_content())
					links = chillin.cssselect('a')
					link0 = str(links[0].attrib['href'])
					link = 'http://www.imdb.com' + extractUrl(link0) + 'fullcredits?ref_=tt_cl_sm#cast'
					thisID = getIdFromUrl(link)
					year0 = ff.cssselect('.year_column')
					year1 = year0[0].text_content()
					year = cleanupString(year1)
					try:
						gigAge = ageAtTheTime(year)
					except Exception as e:
						pass
						# print(e)
						# sys.exit()
						gigAge = ''
					if j == 1:
						record = {'id': iiii, 'name': title, 'year': year, 'thisID': thisID, 'img': img, 'age': gigAge}
						movies.append(record)
					iiii += 1
				ii += 1
			iii += 1
		i += 1
	# get_people_profile(imdbIDF) {'id': iiii, 'name': title, 'year': year, 'thisID': thisID, 'img': img, 'age': gigAge}
	
	return {'name': theTitle, 'year': theYear, }
	# get_people_profile(imdbIDF) {'id': iiii, 'name': title, 'year': year, 'thisID': thisID, 'img': img, 'age': gigAge}



def get_cinema_fullcredits(imdbID):

	urlBase = __.links['imdb']['cinema']['fullcredits']
	url = urlBase.replace(__.ID_HERE,imdbID)

	page = requests.get(url)
	tree = html.fromstring(page.content)
	movieTitle = tree.cssselect('h3')
	movieYear = tree.cssselect('.nobr')
	try:
		theYear0 = cleanupString(movieYear[0].text_content(),False)
		theYear = theYear0.split(' ')[0].replace('(','')
		theYear = theYear.replace(')','')
		theYear = theYear.replace(' ','')
	except Exception as e:
		theYear = ''
	theTitle = cleanupString(movieTitle[0].text_content())
	theAlist = tree.cssselect('a')
	# theTitle = ''
	found = False
	for ta in theAlist:
		linkTest =ta.attrib['href']
		if '/title/tt' in linkTest and not found:
			found =True
			theTitle0 = cleanupString(ta.text_content())
			if len(theTitle0) > 1 and not 'External Sites' in theirName0 and not 'Full Cast' in theirName0:
				theTitle = theTitle0
	
	# for ty in movieYear:
	# 	print(cleanupString(ty.text_content(),False))
	print('Processing', theYear, theTitle, '...')
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
	print(len(tr))
	people = []

	theI = 0
	for e in tr:

		# Set 2
		# 
		props = e.cssselect('td')
		# print(len(props))
		try:
			char = props[3].cssselect('.character')
			character = cleanupString(char[0].text_content())
		except Exception as ee:
			try:
				character = props[3].text_content()
			except Exception as eee:
				character = ''

		try:
			what = props[3]
			testX = what.cssselect('.toggle-episodes')
			# test = cleanupString( testX[0].text_content() )
			onclick = testX[0].attrib['onclick']
			appearances = appearancesOnclick(onclick)
			print( appearances )
		except Exception as e:
			appearances = ''

		try:
			person = cleanupString(props[1].text_content())
		except Exception as ee:
			person = ''
		# # character = props[3].text_content()


		
		try:
			links = e.cssselect('a')
			link0 = str(links[0].attrib['href'])
			link = 'http://www.imdb.com' + extractUrl(link0) + '?ref_=ttfc_fc_cl_t13'
			thisID = getIdFromUrl(link)
		except Exception as ee:
			link = ''
			thisID = ''

		if len(link) > 3:
			try:
				people.append( { 'id': theI, 'name': person, 'thisID': thisID, 'character': character, 'appearances': appearances } )
				theI = theI + 1 
			except Exception as e:
				pass



	return {'name': theTitle, 'year': theYear, 'link': url, 'people': people}
	# get_cinema_fullcredits(imdbID) {'name': theTitle, 'year': theYear, 'link': url, 'people': people}

def get_cinema_ratings(imdbID):
	url = __.links['imdb']['cinema']['ratings'].replace(__.ID_HERE,imdbID)
	# print(url)
	# sys.exit()
	page = requests.get(url)
	tree = html.fromstring(page.content)
	description0 = tree.cssselect('.allText')
	description1 = description0[0].text_content()
	description = cleanupString(description1)

	try:
		rating = description.split('vote of ')[1]
	except Exception as e:
		rating = ''

	try:
		nameStuffShow = tree.cssselect('h4[itemprop="name"]')
		name0 = nameStuffShow[0].cssselect('a')
		nameShow = cleanupString(name0[0].text_content())
	except Exception as e:
		nameShow = ''
	nameStuff = tree.cssselect('h3[itemprop="name"]')
	try:

		name0 = nameStuff[0].cssselect('a')
		name = cleanupString(name0[0].text_content())

	except Exception as e:
		name = ''
	# if not nameShow == '':
	# 	name = nameShow + ': ' + name
	# print(len(nameStuff))
	# nameX = nameStuff[0].text_content()
	# nameY = cleanupString(nameX,False)
	# print(nameY)
	# year0 = nameStuff[0].cssselect('span')
	# year = cleanupString(year0[0].text_content())
	# print('year: ',year)
	# year = year1.replace('(','').replace(')','')
	try:
		year0 = nameStuff[0].cssselect('.nobr')
		year1 = cleanupStringYear(year0[0].text_content())
		# print('year: ',year)
		year = year1.replace('(','').replace(')','')
	except Exception as e:
		year = ''
	if year == '':
		try:
			year0 = nameStuff[0].cssselect('.nobr')
			year1 = cleanupString(year0[0].text_content(),False)
			# print('year: ',year)
			year = year1.replace('(','').replace(')','')
		except Exception as e:
			year = ''
	year = cleanupString(year)
	# print({'imdbID': imdbID, 'rating': rating, 'name': name, 'year': year})
	# if not len(year) > 0:
	# 	sys.exit()
	return {'rating': rating, 'show': nameShow, 'name': name, 'year': year}












def get_cinema_seasons(imdbID):
	theTitle=''
	theYear=''

	url = __.links['imdb']['cinema']['fullcredits'].replace(__.ID_HERE,imdbID)

	if theTitle == '':
		page = requests.get(url)
		tree = html.fromstring(page.content)
		movieTitle = tree.cssselect('h3')
		movieYear = tree.cssselect('.nobr')
		try:
			theYear0 = cleanupString(movieYear[0].text_content(),False)
			theYear = theYear0.split(' ')[0].replace('(','')
			theYear = theYear.replace(')','')
			theYear = theYear.replace(' ','')
		except Exception as e:
			theYear = ''
		theTitle = cleanupString(movieTitle[0].text_content())

	theYear = _str.cleanBE(theYear,' ')
	theTitle = _str.cleanBE(theTitle,' ')
	isCached = False
	now = datetime.datetime.now()
	today = now.strftime("%Y-%m-%d")

	newURL = __.links['imdb']['cinema']['season'].replace(__.ID_HERE,imdbID)
	siteBase = 'https://www.imdb.com'
	thisURL = newURL.replace('THESEASON','1')
	page = requests.get(thisURL)
	tree = html.fromstring(page.content)
	seasons = tree.cssselect('#bySeason option')
	seasonTest0 = seasons[len(seasons)-1].text_content()
	seasonTest = cleanupString(seasonTest0)
	global zeroList
	zeroList = zeroList.lower()
	zeroListX = zeroList.split(',')
	if theTitle.lower() in zeroListX:
		isZero = True
	else:
		isZero = False

	if 'unknown' in seasonTest.lower():
		unknown = True
	else:
		unknown = False
	episodeList = []
	seasonList = []
	episodeListIds = []
	for i,s in enumerate(seasons):
		season = str(i+1)
		if int(season) == len(seasons) and unknown:
			thisURL = newURL.replace('THESEASON','-1')
		else:
			thisURL = newURL.replace('THESEASON',season)

			page = requests.get(thisURL)
			tree = html.fromstring(page.content)
			episodeCode = tree.cssselect('div[itemprop="episodes"]')

			episodeSet = []
			for ii,epiCode in enumerate(episodeCode):
				shows = epiCode.cssselect('a[itemprop="name"]')
				show = shows[0]
				link = show.attrib['href']
				if not isZero:
					seasonZero = False
				if isZero and ii == 0:
					seasonZero = isSeasonZero(siteBase + link)
				# if theTitle.lower() == 'doctor who' and isZero and not season in ['1','8']:
				if seasonZero:
					episodeN = str(ii)
				else:
					episodeN = str(ii+1)
				# link = link0.split('?')[0] + 'fullcredits?ref_=tt_cl_sm#cast'
				# episodeN = link.split('ttep_ep')[1]
				
				airdate0 = epiCode.cssselect('.airdate')
				airdate1 = airdate0[0].text_content()
				airdate2 = cleanupString(airdate1)
				airdate3 = airdate2.replace('.','')
				airdate = monthToNumber(airdate3)
				showId = season + ':' + episodeN
				showTitle0 = show.text_content()
				showTitle = cleanupString(showTitle0)
				
				episodeListIds.append(showId)
				episodeList.append({'id': showId, 'title': showTitle, 'url': siteBase + link, 'airdate': airdate})
				episodeSet.append({'id': showId, 'title': showTitle, 'url': siteBase + link, 'airdate': airdate})
			seasonList.append({'season': season, 'episodes': episodeSet})
	
	seasonData.append({'id': getIdFromUrl(url), 'year': theYear, 'title': theTitle, 'seasons': seasonList, 'date': str(today)})
	return seasonData





######################################################################################## ########################################################################################

maxDateLength = 14
zeroList = 'Doctor Who'
seasonData = []
allPeople = []
allMovies = []
relationships = []
completedIDs = []
errors = []
KevinBaconID = 'nm0000102'
hallmark = []
allErrors = []
hallmarkDataRaw = []
iHallmark = 0
franchiseData = []
smartOmit = 'dc,marvel;marvel,dc'
franchiseDaysMax = 180
expireCheckDaysMax = 180

_.switches.fieldSet('Long','active',True)

# hallmarkDaysMax = 180
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

__.objectLocation = {
						'people': _v.myTables + _v.slash+'imdb_people.objects',
						'cinema': _v.myTables + _v.slash+'imdb_cinema.objects',
						'objects': _v.myTables + _v.slash+'imdb\\imdb_obj_' + __.ID_HERE + '.objects'
					}

# __.objectLocation['cinema']
# __.objectLocation['people']
# __.objectLocation['objects']


# __.links['imdb']['cinema']['fullcredits']
# __.links['imdb']['cinema']['writers']
# __.links['imdb']['cinema']['parentalguide']
# __.links['imdb']['cinema']['ratings']
# __.links['imdb']['cinema']['season']
# __.links['imdb']['people']['profile']
# __.links['imdb']['people']['bio']

def cleanAlias(label):
	label = str(label)
	label = label.replace('\n',' ')
	label = label.replace('\r',' ')
	label = label.replace(',',' ')
	label = _str.replaceDuplicate(label,' ')
	label = _str.cleanBE(label,' ')
	label = label.lower()
	return label


def addAliasID(label,pm,idType,imdbID):
	if len(theAliasID(label,pm,idType)) == 0:
		label = cleanAlias(label)
		__.aliases.append({'label': label, 'pm': pm, idType: imdbID})
		_.saveTable(__.aliases,'imdb_aliases.json',True,False)


def theAliasID(label,pm,idType):
	# theAliasID(searchFor,personMovie,'imdbID')
	result = ''
	if len(idType) == 0:
		idType = 'imdbID'
	if len(__.aliases) > 0:
		label = cleanAlias(label)
		for alias in __.aliases:
			if alias['label'] == label and alias['pm'] == pm and len(alias[idType]) > 0:
				result = alias[idType]
	return result



def caseTest():
	# print('test')
	# sys.exit()
	__.cinema = TheCinema()
	__.people = ThePeople()

	# if _.switches.isActive('ObjectsLoadSkip'):
	# 	__.cinema = TheCinema()
	# 	__.people = ThePeople()
	# else:
	# 	try:
	# 		with open(__.objectLocation['cinema'], 'rb') as objCinema:
	# 			__.cinema = pickle.load(objCinema)
	# 	except Exception as e:
	# 		__.cinema = TheCinema()
	# 	try:
	# 		with open(__.objectLocation['people'], 'rb') as objPeople:
	# 			__.people = pickle.load(objPeople)
	# 	except Exception as e:
	# 		__.people = ThePeople()
		# print('loaded')
		# test = input('pause')
	# print(_.get_size(__.cinema))
	# sys.exit()
	# print(type(__.pipeData))
	focus()
	__.pipeData = _.appData[__name__]['pipe']
	if type(__.pipeData) == list:
		if _.switches.isActive('Movie'):
			if _.switches.isActive('Score') or _.switches.isActive('Label'):
				for pData in __.pipeData:
					try:
						if _.switches.isActive('MovieFile'):
							# print(pData)
							theLabel = pData['title']
						else:
							theLabel = pData

						if not theLabel in __.omitFromMovies:
							# print('   -   ',theLabel)
							imdbID = googleID(theLabel,'movie')
							if _.switches.isActive('Label'):
								if _.switches.isActive('MovieFile'):
									__.cinema.printLabel( imdbID, pData, franchise=True )
								else:
									__.cinema.printLabel( imdbID )
							else:
								__.cinema.rating(imdbID)
					except Exception as e:
						pass
	else:
		imdbID = _.switches.value('Case')
		if not len(imdbID) > 0:
			if _.switches.isActive('Movie'):
				imdbID = googleID(_.switches.value('Movie'),'movie')
			if _.switches.isActive('Person'):
				imdbID = googleID(_.switches.value('Person'),'person')
		if not len(imdbID) > 0:
			print('Google Error')
			sys.exit()
		if _.switches.isActive('Episode'):
			__.cinema.seasons(imdbID)
			# __.cinema.inSeason(imdbID)
		elif _.switches.isActive('SeasonStarts'):
			ssv = _.switches.value('SeasonStarts')
			# print(ssv)
			ssvp = ssv.split(',')
			if len(ssvp) == 1:
				__.cinema.seasonsStarts(imdbID,ssvp[0])
			if len(ssvp) == 2:
				__.cinema.seasonsStarts(imdbID,ssvp[0],ssvp[1])
		else:
			if 'nm' in imdbID:
				# __.people.register(imdbID, False)
				__.people.register(imdbID, shouldPrint=True)
			if 'tt' in imdbID:
				# __.cinema.register(imdbID, False)
				__.cinema.register(imdbID, shouldPrint=False)

			# __.people.dump()
			# __.cinema.dump()

def appearancesOnclick(onclick):
	onclick = onclick.replace( "'", '' )
	urlBase = 'https://www.imdb.com/name/*b*/episodes/_ajax?title=*c*&category=*d*&ref_marker=*e*&start_index=*g*'
	scriptData = onclick.split(',')
	b = scriptData[1]
	c = scriptData[2]
	d = scriptData[3]
	e = scriptData[4]
	g = scriptData[6]
	url = 	urlBase.replace( '*b*', b )
	url = 		url.replace( '*c*', c )
	url = 		url.replace( '*d*', d )
	url = 		url.replace( '*e*', e )
	url = 		url.replace( '*g*', g )
	return url
	# toggleSeeMoreEpisodes(this,'nm1050978','tt0118480','actor','ttfc_fc_cl_i892',0,0,'#episodes-tt0118480-nm1050978-actor', toggleSpan); return false;

def loadObject(file):
	result = None
	with open(file, 'rb') as objThis:
		result = pickle.load(objThis)
	return result
focus()
_.appData[__name__]['pipe'] = ''

if not sys.stdin.isatty():
	_.appData[__name__]['pipe'] = []
	for pd in sys.stdin.readlines():
		# print(pd)
		pd = pd.replace('\n','')
		if not pd == '':
			# print(pd)
			_.appData[__name__]['pipe'].append(pd)
	try:
		if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
			_.appData[__name__]['pipe'][0] = _.appData[__name__]['pipe'][0][1:]
	except Exception as e:
		pass

# def timestamp():
# 	return time.time()


# print(type(__.pipeData))

__.aliases = _.getTable('imdb_aliases.json')
# print(__.aliases)
# test = input('pause')
__.omitFromMovies = []
__.omitFromMovies.append('Scotty\'S 4Th Birthday 7 16 84')
__.imdbAppearancesCaptured = 1553172315.2781389
########################################################################################
if __name__ == '__main__':
	if _.switches.isActive('Watched'):
		print( _.switches.value('Watched') )
		# sys.exit()
	if _.switches.isActive('Case'):
		caseTest()
	else:
		action()





