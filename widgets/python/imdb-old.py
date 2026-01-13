#!/usr/bin/python3
import os
import sys
import time
import simplejson as json
import platform
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

# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )

_omit = _.regImp( __.appReg, 'omitTable' )
##################################################
from operator import itemgetter
from lxml import html
import requests
import cssselect
import datetime
from inspect import currentframe, getframeinfo
# frameinfo = getframeinfo(currentframe())
# print(frameinfo.filename, frameinfo.lineno)

try:
	import arrow
except Exception as e: pass;
try:
	import pickle
except Exception as e: pass;

try:
	import webbrowser
except Exception as e: pass;
try:
	import native_web_app
except Exception: pass;
##################################################

def appSwitches():
	_.switches.register('Movie', '-movie,-ent,-entertainment,-play,-screenplay')
	_.switches.register('Person', '-person,-who,-actor')
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

	_.switches.register('InSeason', '-is,-inseason')
	_.switches.register('SeasonStarts', '-ss,-seasonstarts','"16 July 2017" dmy')

	_.switches.register('ObjectsLoadSkip', '-skipload,-fresh,-new,-download,-dl,-live','save')
	_.switches.register('Print', '-print')

	_.switches.register('Case', '-case','tt0436992 , nm2092886, tt0088763')

	_.switches.register('Location', '-location','movie_drive, cloud_drive')
	_.switches.register('Watched', '-watched','2d, 2w, 1y, 6m, ( or leave blank )')

	_.switches.register('Label', '-label')
	_.switches.register('MovieFile', '-mfile')

	_.switches.register('MovieFranchise', '-fran,-franchise')

	_.switches.register('PrintPath', '-path')
	_.switches.register('PrintOldPath', '-oldpath')

	_.switches.register('ForceFranchise', '-force')

	_.switches.register('AutoFranchise', '-autofranchise')



	_.switches.register('SeasonsSimple', '-simp,-seasonssimple,-simpleseasons')
	_.switches.register('EpisodeTable', '-et,-eet,-episodetable')


	_.switches.register('xRef-Page-Threaded', '-pt,-threaded,-pthread')

	_.switches.register('JustIDs', '-ids')

	_.switches.register('EpisodeLength', '-length')
	_.switches.register('OnEpisode', '-on')

	_.switches.trigger('Watched', _.txt2Date)


_.columnTab = ' '



_.appInfo[focus()] = {
	'file': 'imdb.py',
	'description': 'Lookup movies, shows, and people on imdb',
	'categories': [
						'research',
						'entertainment',
						'documentation',
						'tool',
						'ent',
						'imdb',
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

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')


_.appInfo[focus()]['examples'].append('p imdb -ent Terminator 2')
_.appInfo[focus()]['examples'].append('p imdb -person Jim Caviezel')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -person lucy lu -ent hackers -xref one')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -entertainment when calls the heart and stargate atlantis -xref')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -person Elisabeth Shue -kevinbacon')
_.appInfo[focus()]['examples'].append('p imdb -person kevin bacon -kevinbacon build -kbpickup')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -hallmark + the sweetest heart')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -hallmark buildPeople')
_.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('p dir -cache Movie_Drive.dirCache -c n --c -size g 700mb - downloaded + 2017|p line --c -p ( 0 | p line --c -p . 0 -u |p line --c -make "p imdb -qi -ent {}"|p execute > %tmpf2%')
_.appInfo[focus()]['examples'].append('type List_of_movies.txt | p imdb -case -ent -score | p line -u --c | sort | p line ')
_.appInfo[focus()]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies + 2018 | p movieTitle | p imdb -case -ent -score | p line -u --c | sort | p line ')
_.appInfo[focus()]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies + 2018 | p movieTitle | p imdb -case -ent -score | p line -u --c | sort | p line ')
_.appInfo[focus()]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies -ago 2w | p movieTitle | p imdb -case -ent -score | p line -u --c | sort | p line ')
_.appInfo[focus()]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies -ago 2w | p movieTitle | p line --c -make "p imdb -score -qi -ent {}" | p execute --c | sort | p line')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append(['p dir -cache %mData% -movietitle -movies -ago 2m | p imdb -case -ent -score -skipload | p line -u --c | sort /R | p line ','red'])
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -ent unleashing mr darcy and Marrying Mr Darcy -xref')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -c n --c + 201 | p movieTitle | p line + 2016 --c | p line --c -make "p imdb -score -qi -ent {}" | p execute --c | sort | p line')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dir -cache %i%\\Movie_Drive.dirCache -movies -ago 2w | p movieTitle | p line --c -make "p imdb -score -qi -ent {}" | p execute --c | sort | p line')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -ent castle -episode 5:21')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -ent full house and family matters -xref -episode')
_.appInfo[focus()]['examples'].append('p imdb -ent chicago med and chicago fire and chicago pd -xref -episode')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -hallmark + The Nine Lives of Christmas -view')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -case -ent doctor  who -ss "16 July 2020" dmy')
_.appInfo[focus()]['examples'].append('p imdb -case -ent doctor  who -ss 0')
_.appInfo[focus()]['examples'].append('p imdb -case -ent doctor  who -seasonstarts 2020-07-16')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p imdb -case -ent smallville -ep')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('____________________________________________________________________________________________________')
_.appInfo[focus()]['examples'].append('type TV_Series.txt | p imdb -case -ep -ent -is')
_.appInfo[focus()]['examples'].append('type DVR_SHOWS.txt | p imdb  -case -ep -ent -is')
# _.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('Note: there is a problem with piping ep data run the below to fix')
# _.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('RUN THIS FIRST:')
# _.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('\ttype %tmpf1% | p line --c -make "echo {} | p imdb -case -ep -ent -is" | p execute')
# _.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('OR THIS AFTER ISSUE:')
# _.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('\ttype %tmpf1% | p line --c -make "echo {} | p imdb -case -ep -ent -is -skipload save" | p execute')
# _.appInfo[focus()]['examples'].append('____________________________________________________________________________________________________')
# _.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['examples'].append('')

_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('type DVR_SHOWS.txt | p imdb -case -ep -ent -inseason -skipload save')
_.appInfo[focus()]['examples'].append('type DVR_SHOWS.txt | p imdb -case -ep -ent -inseason')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('type DVR_TV_SHOWS__NEW_.txt  | p imdb -case -ep -ent -inseason | + true | p line')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append(['p imdb -ent hackers 1995 -person lucy liu -xref one','red'])
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('ee supernatural -live save -simp')
_.appInfo[focus()]['examples'].append('p imdb -case -ep  -live save -simp -ent supernatural')
_.appInfo[focus()]['examples'].append('p imdb -case -ep  -live save -ent supernatural')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('ee fringe + neither')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('ee how i met your mother -length 22 -on 8:18')
_.appInfo[focus()]['examples'].append('')


# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})


def franchiseFixSpace( data ):
	# if not 'save' in data.lower():
	data = data.replace( ',', ' ' )
	return data


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
	_.defaultScriptTriggers()
	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.trigger('MovieFranchise',franchiseFixSpace)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()



_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )



########################################################################################
# START


def print_url(url,c='cyan',frameinfo=None):
	_.pr( 'line:',frameinfo.lineno, c='purple' )
	_.pr(url,c=c)

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
			record = {'id': cnt+1,'name': person,'character': character,'link': link,'img': img,'hallmark': foundHallmark}
		else:
			record = {'id': cnt+1,'name': person,'character': character,'link': link,'img': img}
		people.append(record)
		# _.pr(people)
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
	# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
	# brandNewURL = 'http://www.rightthumb.com/projects/widget/proxy.php?p=' + newURL.replace('&','[and]')
	# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
	# __.xit()

	# page=str(requests.post(newURL, data = {'path':path,'file':new}).content,'iso-8859-1')
	# page = requests.get(newURL).content.decode("utf-8").replace('\\n','\n')
	print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
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
			# _.pr(text)
			_.pr()
			_.pr(text)


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
			_.pr( 'shouldRun:', shouldRun )
			if shouldRun:
				if 'imdb.com/list/' in link:
					theURL = link.replace('/url?q=','').split('/&sa=U')[0]
					_.pr(theURL)
					theList.append({'name': text,'link': theURL})
	return theList
buildUrlListLast = {}
buildUrlListDuplicate = []
def buildUrlList(url,info=False):
	global buildUrlListLast
	global buildUrlListDuplicate
	# _.pr( url )
	# __.xit()
	franchiseList = []
	try:
		page = requests.get(url)
		print_url(frameinfo=getframeinfo(currentframe()), url=url)
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
		_.pr( 'url:', url )
	except Exception as e:
		_.pr('Bad list link')

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
						_.pr(year,nameFix)
					else:
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
				link = str(l.attrib['href'])
				if '/title/' in link:
					thisID = getIdFromUrl('http://www.imdb.com'+link)
					if not thisID in buildUrlListDuplicate:
						buildUrlListDuplicate.append(thisID)
						# if 'tt1375666' in thisID:
						#   _.pr( 'Error:', url )
						#   __.xit()
						franchiseList.append(thisID)
					iT += 1
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
					_.pr('Page:',buildUrlListLast[item])
					# _.pr(link)
					for xx in buildUrlList('http://www.imdb.com'+link,info):
						# if 'tt1375666' in xx:
						#   _.pr( 'Error:', url )
						#   __.xit()
						franchiseList.append(xx)
	except Exception as e:
		# _.pr('buildUrlList: for links(a) & .pagination-range')
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
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

	# print_url(frameinfo=getframeinfo(currentframe()), url=url)
	# pause = input('pause')
	global hallmark
	# print_url(frameinfo=getframeinfo(currentframe()), url=url)
	print_url(frameinfo=getframeinfo(currentframe()), url=url)
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

	# _.pr(birthDate)
	# _.pr(birthYear)
	# _.pr(birthLocation)
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
			_.printBold('Processing '+theirName+' ...')
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
					try:
						title = cleanupString(chillin.text_content())
						links = chillin.cssselect('a')
						link0 = str(links[0].attrib['href'])
						link = 'http://www.imdb.com' + extractUrl(link0) + 'fullcredits?ref_=tt_cl_sm#cast'
						thisID = getIdFromUrl(link)

						year0 = ff.cssselect('.year_column')
						year1 = year0[0].text_content()

						# year1 = str(year1,'utf-8')

						# year1_temp = ''
						# has = '0123456789'
						# good = 0
						# found = False
						# for x in year1:
						#   good += 1
						#   if not x in has:
						#       good = 0
						#       year1_temp = ''
						#   else:
						#       year1_temp += x
						#       good += 1
						#       if good == 4:
						#           break
						# year1 = year1_temp



						year = cleanupString(year1)
					except Exception as e:
						j=0
					try:
						gigAge = ageAtTheTime(year)
					except Exception as e:
						pass
						# _.pr(e)
						# __.xit()
						gigAge = ''
					if j == 1:
						if _.switches.isActive('HallmarkCrossRef') == True:
							hallmarkData = isHallmark(thisID)
							if len(hallmarkData) > 0:
								iHallmark += 1
							record = {'id': iiii+1, 'name': title, 'year': year, 'link': link, 'img': img, 'hallmark': hallmarkData, 'age': gigAge}
						else:
							record = {'id': iiii+1, 'name': title, 'year': year, 'link': link, 'img': img, 'age': gigAge}
						movies.append(record)
					iiii += 1
				ii += 1
			iii += 1
		i += 1
	if _.switches.isActive('NoPrint') == False:
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')
		if _.switches.isActive('JustIDs'):
			_.pr( getIdFromUrl(url) )
		_.pr()
		_.printBold(theirName + '\t' + str(age))
		_.pr()
	if _.switches.isActive('NoPrint') == False:
		if _.switches.isActive('JustIDs'):
			for rec in movies:
				_.pr( getIdFromUrl( rec['link'] ) )
			__.xit()
		else:
			_.switches.fieldSet('Long','active',True)
			_.switches.fieldSet('Long','value','name')
			xXx = len(movies)
			for i,rec in enumerate(movies):
				movies[i]['order'] = xXx
				xXx-=1

			if _.switches.isActive('HallmarkCrossRef') == True:
				_.tables.register('Auto',movies,w=1)
				_.tables.fieldProfileSet( 'Auto', 'name', 'trigger', _.longDashAdd )
				_.tables.print('Auto','id,hallmark,year,name')
				_.pr()
				_.pr('    ',iHallmark,'Hallmark')
			else:
				_.tables.register('Auto',movies,w=1)

				_.tables.fieldProfileSet( 'Auto', 'name', 'trigger', _.longDashAdd )
				_.tables.print('Auto','id,order,year,age,name')
	if _.switches.isActive('BuildCrossRef') == True:
		buildMovies(movies,{'name': theirName, 'url': url})
		theRows = []
		theRows.append({'name': theirName, 'link': url})
		buildPeople(theRows)
		# _.pr()
	# _.pr(birthDate)


	def makeSelection():
		# lookupPerson(url):
		_.pr()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 'h' or selection == '?' or selection == 'help':
			_.pr('id')
			_.pr('(b)io')
			_.pr('(s)earch')
			_.pr('xref')
			_.pr('l','url')
			_.pr('(p)ic')
			_.pr('e(x)it')
			_.pr('description contains (dc)')
			_.pr('show all descriptions (sd)')
			_.pr('save')
			_.pr('(f)ranchise')
			_.pr('search results (sr)')
		if selection == 'sr':
			_.pr()
			sr = input('Search for - ')
			searchResults = []
			for m in movies:
				if sr.lower() in m['name'].lower():
					searchResults.append(m)
			_.pr()
			_.tables.register('searchResults',searchResults,w=1)
			_.tables.fieldProfileSet( 'searchResults', 'name', 'trigger', _.longDashAdd )
			_.tables.print('searchResults','id,year,name')
		if selection == 'f':
			_.pr()
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
			load_franchise_table( franchise )

			fID = inFranchiseID( franchise )
			if type(fID) == bool:
				_.pr( 'No Franchise Data' )
				_.pr()
				_.pr( 'Run:' )
				_.pr( '\tp franchise -f', franchise )
				__.xit()
			if platform.system() == 'Windows':
				os.system('cls')
			else:
				os.system('clear')
			_.pr()
			_.printBold(theirName + '\t' + str(age))
			_.pr()




			for ix,r in enumerate(movies):
				# record = {'id': iiii, 'name': title, 'year': year, 'link': link, 'img': img, 'age': gigAge}
				if getIdFromUrl(r['link']) in __.franchises[fID]['movieIDS']:
					movies[ix][franchise] = 'x'
				else:
					movies[ix][franchise] = ''
			_.tables.register('Auto',movies,w=1)
			_.tables.fieldProfileSet( 'Auto', 'name', 'trigger', _.longDashAdd )
			_.tables.print('Auto','id,year,age,'+franchise+',name')
			_.pr()
			_.pr()
			io = 0

			for ix,r in enumerate(movies):
				if getIdFromUrl(r['link']) in __.franchises[fID]['movieIDS']:
					io += 1
					_.pr(r['id'],'\t',r['year'],r['name'])
			_.pr()
			if io > 0:
				_.pr(io)

			if io == 0:
				pass

			now = datetime.datetime.now()
			today = now.strftime("%Y-%m-%d")

			fdtl = __.franchises[fID]['date'].split('-')
			foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
			td = str(today).split('-')
			tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
			diff = tdd - foundDate


			try:
				ppl = _.addComma( len(set(__.franchises[fID]['peopleIDS'])) ) + ' people\t\t'
			except Exception as e:
				ppl = ''
			try:
				mv = _.addComma( len(set(__.franchises[fID]['movieIDS'])) ) + ' movies\t\t'
			except Exception as e:
				mv = ''
			_.pr('_____________________________________________________________________________________________________________________')
			_.pr( franchise.upper(), ppl, mv, __.franchises[fID]['date'], '\t\t', str(diff.days), 'days' )
			_.pr()
			_.pr()

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
					# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
					print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
					page = requests.get(newURL)
					tree = html.fromstring(page.content)
					description0 = tree.cssselect('.summary_text')
					description1 = description0[0].text_content()
					description = cleanupString(description1)
					movies[i-1]['description'] = description
				_.updateLine('')
			_.pr('')
			for m in movies:
				if len(m['year']) > 1:
					theTitle = str(m['id']) + '\t' + m['name'] + ' (' + m['year'] + ')'
				else:
					theTitle = str(m['id']) + '\t' + m['name']
				_.pr('_______________________________________________')
				_.pr('')
				_.pr(theTitle)
				_.pr(m['description'])



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
					# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
					print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
					page = requests.get(newURL)
					tree = html.fromstring(page.content)
					description0 = tree.cssselect('.summary_text')
					description1 = description0[0].text_content()
					description = cleanupString(description1)
					movies[i-1]['description'] = description
					description = description.replace('at this time','')
					# _.pr("",lookFor,description.lower())
					if not allDC:
					# _.pr(allDC)
					# __.xit()
						if lookFor in description.lower():
							_.updateLine("")
							_.pr()
							_.pr()
							_.pr(m['name'])
							done = True
							break
							__.xit()

					# __.xit()
				if done:
					__.xit()
				if lfOr and lfAnd:
					_.pr('')
					_.pr('')
					_.pr('Error: and or, pick one')
					__.xit()
				if not lfOr and  not lfAnd:
					if lookFor in description:
						# _.pr('single')
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
			_.pr('')
			if len(dcResult) == 0 and not done:
				_.pr('Nothing Found')
			else:
				_.pr('')
				dci = 0
				for d in dcResult:
					# _.pr(dci, '\t', d)
					_.pr(d)
					dci += 1
				_.pr('')
			if not done:
				_.pr('')
				_.pr(len(dcResult))
				_.pr('')
			dcResult = []
		if selection == 'bio' or selection == 'b':
			newURL = extractUrl(url) + 'bio?ref_=nm_ov_bio_sm'
			print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
			page = requests.get(newURL)
			tree = html.fromstring(page.content)
			bio0 = tree.cssselect('.soda p')
			bio1 = bio0[0].text_content()
			bio = cleanupString(bio1)
			_.pr(bio1)
		if selection == 'id':
			_.pr(getIdFromUrl(url))
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
			try:
				webbrowser.open(url, new=2)
			except Exception as e:
				try:
					native_web_app.open(url)
				except Exception as e:
					_.cp( 'Error: unable to open browser', 'red' )
		if selection == 'x' or selection == 'exit':
			__.xit()
		if selection == 'p' or selection == 'pic':

			try:
				webbrowser.open(img, new=2)
			except Exception as e:
				try:
					native_web_app.open(img)
				except Exception as e:
					_.cp( 'Error: unable to open browser', 'red' )


		if selection == 'save':
			global allPeople
			global allMovies
			global relationships
			_.saveTable(allPeople,'imdb_people.json')
			_.saveTable(allMovies,'imdb_movies.json')
			_.saveTable(relationships,'imdb_relationships.json')
		try:
			selectedSomething = True
			selection = int(selection)-1
			_.pr()
			_.pr(movies[selection]['name'],' - has been selected')
			_.pr()
			lookupMovie(movies[selection]['link'])
		except Exception as e:
			selectedSomething = False
			# _.pr('Unspecified Error')
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
	#   _.pr(i,u)
	#   i+=1
	# __.xit()


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

	# _.pr(related)
	# rel.append({'name': related['name'], 'year': related['year'], 'link': related['url']})
	# buildMovies(rel,{'name': rows[0]['name'],'url': rows[0]['link']})

	# found = False
	# try:

	#       for peeps1 in allPeople:
	#           if peeps0['id'] == peeps1['id']:
	#               found = True
	# except Exception as e:
	#   pass

	# if not found:
	# _.pr(rows)
	for peeps0 in rows:
		# _.pr(peeps0)
		# pause = input('pause')
		try:
			thisID = getIdFromUrl( peeps0['link'] )
			allPeople.append({ 'id': thisID, 'name': peeps0['name'], 'link': peeps0['link'] })
			# _.pr(thisID)
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
	# _.pr('buildPeople')
	# __.xit()
	# allPeople = set(allPeople)
def buildMovies(rows,related=False):
	# _.pr(rows)
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
	# _.pr('relationships')
	# __.xit()
	found = False
	for rel in relationships:
		if rel['movieID'] == movieID and rel['personID'] == personID:
			found = True

	if not found:
		relationships.append({ 'movieID': movieID, 'personID': personID })


##########################################################################################

def printClean( string ):
	string = _clean(string)
	for xyz in __.imdb_replace:
		string = string.replace( xyz[0], xyz[1] )

	return _str.printClean( string )

def _clean(string):
	string = str(string)
	string = string.replace('\xe2\x80','-')
	string = string.replace('\\xe2\\x80','-')
	return string

def cleanupStringYear3(string):
	string = _clean(string)
	string = cleanupString(string)
	# string = _str.onlyDigits(string)
	string = string.replace(' ','')
	string = printClean( string )
	return string
def cleanupStringYear2(string):
	string = _clean(string)
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
	string = _str.onlyDigits(string)
	string = printClean( string )
	# _.pr(string)
	# __.xit()

	return string
def cleanupStringYear(string):
	string = _clean(string)
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
	string = printClean( string )
	# _.pr(string)
	# __.xit()
	return string

def formatData( result ):
	try:
		result = str(result,'iso-8859-1', 'ignore')
	except Exception as e:
		pass
	try:
		result = str(result,'ascii', 'ignore')
		return result
	except Exception as e:
		pass
	try:
		result = str(result,'iso-8859-1', 'ignore')
	except Exception as e:
		pass
		try:
			result = str(result,'utf-8', 'ignore')
		except Exception as e:
			try:
				result = str(result,'iso-8859-1', 'ignore')
			except Exception as e:
				result = result.encode('utf-8', 'ignore')
		try:
			result = str(result,'iso-8859-1', 'ignore')
		except Exception as e:
			pass
	result = _clean(result)
	return result



def cleanupString0( string ):
	string = _clean(string)
	for xyz in __.imdb_replace:
		string = string.replace( xyz[0], xyz[1] )
	# string = string.replace( '\\xb1', 'n' ).replace( '\xb1', 'n' )
	string = formatData( string )
	string = string.replace( '\xe2\x80', '-' ).replace( '\\xe2\\x80', '-' )
	for x in txt_clean_list:
		string = string.replace( x, '' )
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanFirst(string,' ')
	string = printClean( string )
	string = _str.cleanBE(string,' ')
	return string
def cleanupString(string,beforeAfter=True):
	string = _clean(string)
	for xyz in __.imdb_replace:
		string = string.replace( xyz[0], xyz[1] )
	# string = string.replace( '\\xb1', 'n' ).replace( '\xb1', 'n' )
	global txt_clean_list
	string = formatData( string )
	string = string.replace( '\xa0', '' ).replace( '\\xa0', '-' )
	string = string.replace( '\xe2\x80', '-' ).replace( '\\xe2\\x80', '-' )
	for x in txt_clean_list:
		string = string.replace( x, '' )
	string = _str.replaceAll(string,'\xc2',' ')
	string = _str.replaceAll(string,'\\xc2',' ')
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.cleanLast(string,' ')
	# string = _str.cleanFirst(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanBE(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.cleanFirst(string,' ')
	string = _str.charFix(string)
	string = string.replace('\\xe2\\x80\\x93','-')
	string = string.replace('\\\\xe2\\\\x80\\\\x93','-')
	if beforeAfter:
		string = string.split('(')[0]
	else:
		string = string.split('(')[1]
	string = string.split('/')[0]
	string = string.replace('\\xbb','')
	string = _str.replaceDuplicate(string,' ')
	string = printClean( string )
	string = _str.cleanBE(string,' ')
	# if string == 'b':
	#   string = ''
	return string
def cleanupString1(string):
	string = _clean(string)
	for xyz in __.imdb_replace:
		string = string.replace( xyz[0], xyz[1] )
	# string = string.replace( '\\xb1', 'n' ).replace( '\xb1', 'n' )
	string = formatData( string )
	string = string.replace( '\xe2\x80', '-' ).replace( '\\xe2\\x80', '-' )
	for x in txt_clean_list:
		string = string.replace( x, '' )
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.cleanFirst(string,' ')
	string = string.replace('\\xe2\\x80\\x93','-')
	string = string.replace('\\\\xe2\\\\x80\\\\x93','-')
	string = _str.replaceDuplicate(string,' ')
	string = printClean( string )
	string = _str.cleanBE(string,' ')
	# if string == 'b':
	#   string = ''
	return string
def lookupMovie(url):


	global iHallmark
	iHallmark = 0
	# print_url(frameinfo=getframeinfo(currentframe()), url=url)
	if _.switches.isActive('Episode'):
		_.pr('Loading...')
		episodeLink(url)
		__.xit()
	if _.switches.isActive('QuickInfo'):
		movieRating(url)
		__.xit()
	idRegistier(url)
	if _.switches.isActive('NoPrint') == False:
		pass
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

	# print_url(frameinfo=getframeinfo(currentframe()), url=url)
	# pause = input('pause')
	print_url(frameinfo=getframeinfo(currentframe()), url=url)
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
	#   _.pr(cleanupString(ty.text_content(),False))
	_.pr('Processing', theYear, theTitle, '...')
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
	_.pr(len(tr))
	people = []
	people2 = []


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
			people = registerPerson(people,person,link,character)
			people2.append({'name': person, 'link': link, 'character': character})


		# Set 1
		#
		# # props = e.cssselect('.itemprop')
		# i = 0
		# for p in props:
		#   if i == 0:
		#       link = ''
		#       try:
		#           links = p.cssselect('a')
		#           link0 = str(links[0].attrib['href'])
		#           link = 'http://www.imdb.com' + extractUrl(link0) + '?ref_=ttfc_fc_cl_t13'
		#           # _.pr(link)
		#       except Exception as ee:
		#           pass
		#       person = p.text_content()
		#       person = cleanupString(person)
		#       # _.pr(people,person,link,character)
		#       people = registerPerson(people,person,link,character)
		#       people2.append({'name': person, 'link': link, 'character': character})
		#   i += 1
	def doMore():
		if _.switches.isActive('NoPrint') == False:
			if platform.system() == 'Windows':
				os.system('cls')
			else:
				os.system('clear')

			if _.switches.isActive('JustIDs'):
				_.pr( getIdFromUrl(url) )
			_.pr()
			_.printBold(theYear+' '+theTitle)
			_.pr()
		if _.switches.isActive('NoPrint') == False:
			if _.switches.isActive('JustIDs'):
				for rec in people:
					_.pr( getIdFromUrl( rec['link'] ) )
				__.xit()
			else:
				if _.switches.isActive('HallmarkCrossRef') == True:
					_.tables.register('Auto',people,w=1)
					_.tables.fieldProfileSet( 'Auto', 'character', 'trigger', _.longDashAdd )
					_.tables.print('Auto','id,hallmark,name,character')
					_.pr()
					_.pr('    ',iHallmark,'Hallmark')
				else:
					_.tables.register('Auto',people,w=1)
					_.tables.fieldProfileSet( 'Auto', 'character', 'trigger', _.longDashAdd )
					_.tables.print('Auto','id,name,character')
		if _.switches.isActive('BuildCrossRef') == True and not _.switches.value('BuildCrossRef') == 'skip':
			# _.pr('test1')
			buildPeople(people,{'name': theTitle, 'year': theYear, 'url': url})
			# _.pr('test2')
			# __.xit()
			theRows = []
			theRows.append({'name': theTitle, 'year': theYear, 'link': url})
			# _.pr('test3')
			buildMovies(theRows)
			# _.pr('test4')
			# _.pr()
	# if _.switches.isActive('BuildCrossRef') == False:
	doMore()
	def makeSelection():
		# lookupMovie(url):
		_.pr()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 'h' or selection == '?' or selection == 'help':
			# _.pr('(f)ranchise')
			_.pr('id')
			_.pr('(r)ated','why')
			_.pr('(s)earch')
			_.pr('(d)escription')
			_.pr('xref')
			_.pr('l','url')
			_.pr('(p)ic')
			_.pr('(e)pisodes')
			_.pr('e(x)it')
			_.pr('save')
			_.pr('(f)ranchise')
			_.pr('search results (sr)')
		if selection == 'sr':
			_.pr()
			sr = input('Search for - ')
			searchResults = []
			for m in people:
				if sr.lower() in m['name'].lower():
					searchResults.append(m)
			_.pr()
			_.tables.register('searchResults',searchResults,w=1)
			_.tables.fieldProfileSet( 'searchResults', 'character', 'trigger', _.longDashAdd )
			_.tables.print('searchResults','id,name,character')
		if selection == 'f':
			_.pr()
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
			load_franchise_table( franchise )
			fID = inFranchiseID( franchise )

			if type(fID) == bool:
				_.pr( 'No Franchise Data' )
				_.pr()
				_.pr( 'Run:' )
				_.pr( '\tp franchise -f', franchise )
				__.xit()
			if platform.system() == 'Windows':
				os.system('cls')
			else:
				os.system('clear')
			_.pr()
			_.pr(theYearThis, '\t', theTitleThis)
			_.pr()



			for ix,r in enumerate(people):
				# record = {'id': cnt,'name': person,'character': character,'link': link,'img': img}
				# _.pr((r['link']))
				# _.pr(getIdFromUrl(r['link']))
				if getIdFromUrl(r['link']) in __.franchises[fID]['peopleIDS']:
					# _.pr(r['name'])
					people[ix][franchise] = 'x'
				else:
					people[ix][franchise] = ''
			_.tables.register('Auto',people,w=1)
			_.tables.fieldProfileSet( 'Auto', 'character', 'trigger', _.longDashAdd )
			_.tables.print('Auto','id,'+franchise+',name,character')
			_.pr()
			_.pr()
			io = 0

			for ix,r in enumerate(people):
				if getIdFromUrl(r['link']) in __.franchises[fID]['peopleIDS']:
					io += 1
					_.pr(r['id'],'\t',r['name'])
			_.pr()
			if io > 0:
				_.pr(io)

			if io == 0:
				pass

			now = datetime.datetime.now()
			today = now.strftime("%Y-%m-%d")

			fdtl = __.franchises[fID]['date'].split('-')
			foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
			td = str(today).split('-')
			tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
			diff = tdd - foundDate


			try:
				ppl = _.addComma( len(set(__.franchises[fID]['peopleIDS'])) ) + ' people\t\t'
			except Exception as e:
				ppl = ''
			try:
				mv = _.addComma( len(set(__.franchises[fID]['movieIDS'])) ) + ' movies\t\t'
			except Exception as e:
				mv = ''
			_.pr('_____________________________________________________________________________________________________________________')
			_.pr( franchise.upper(), ppl, mv, __.franchises[fID]['date'], '\t\t', str(diff.days), 'days' )
			_.pr()
			_.pr()


		###################################################################################################
		if selection == 'id':
			_.pr(getIdFromUrl(url))
		if selection == 'xref':
			crossReference()

		if selection == 'e':
			episodes(url,theYear,theTitle)



		if selection == 'r' or selection == 'rated' or selection == 'why':
			movieRating(url)


				# try:
				#   newURL = 'http://www.imdb.com/title/' + getIdFromUrl(url) + '/parentalguide'
				#   page = requests.get(newURL)
				#   tree = html.fromstring(page.content)
				#   tr = tree.cssselect('#certifications-list')
				#   td = tr[0].cssselect('li')
				#   _.pr()
				#   _.pr('Rating:')
				#   for item in td:
				#       data0 = item.text_content()
				#       data1 = cleanupString(data0)
				#       # _.pr(data1)
				#       if 'United' in data1 and 'States' in data1:
				#           data = data1.split(':')
				#           _.pr('\t',data[1])
				#   _.pr()
				# except Exception as e:
				#   _.pr('Information unavailable')
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

			try:
				webbrowser.open(url, new=2)
			except Exception as e:
				try:
					native_web_app.open(url)
				except Exception as e:
					_.cp( 'Error: unable to open browser', 'red' )


		if selection == 'x' or selection == 'exit':
			__.xit()
		if selection == 'description' or selection == 'd':
			newURL = extractUrl(url) + '?ref_=ttfc_fc_tt'
			print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
			page = requests.get(newURL)
			tree = html.fromstring(page.content)
			description0 = tree.cssselect('.summary_text')
			description1 = description0[0].text_content()
			description = cleanupString(description1)
			_.pr()
			_.pr(description)
			_.pr()

		if selection == 'p' or selection == 'pic':
			webbrowser.open(img, new=2)
		if selection == 'xref':
			pass
		if selection == 'save':
			global allPeople
			global allMovies
			global relationships
			_.pr(len(allPeople),'people')
			_.pr(len(allMovies),'movies')
			_.pr(len(relationships),'relationships')
			_.saveTable(allPeople,'imdb_people.json')
			_.saveTable(allMovies,'imdb_movies.json')
			_.saveTable(relationships,'imdb_relationships.json')
		try:
			selectedSomething = True
			selection = int(selection)-1
			_.pr()
			_.pr(people[selection]['name'],' - has been selected')
			_.pr()
			lookupPerson(people[selection]['link'])
		except Exception as e:
			selectedSomething = False
			# _.pr('Unspecified Error')
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
	# _.pr( 'here' )
	# __.xit()
	eId = ''.join( _.switches.values('Episode') )
	if not ':' in eId:
		_.pr('No Show')
		__.xit()
	season = eId.split(':')[0]
	_.switches.fieldSet('Episode','active',False)


	print_url(frameinfo=getframeinfo(currentframe()), url=url)
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
	#   linkTest =ta.attrib['href']
	#   if '/title/tt' in linkTest and not found:
	#       found =True
	#       theTitle0 = cleanupString(ta.text_content())
	#       if len(theTitle0) > 1 and not 'External Sites' in theirName0 and not 'Full Cast' in theirName0:
	#           theTitle = theTitle0



	newURL = 'https://www.imdb.com/title/' + getIdFromUrl(url) + '/episodes?season='
	siteBase = 'https://www.imdb.com'

	print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
	page = requests.get(newURL + season)
	tree = html.fromstring(page.content)

	seasons = tree.cssselect('#bySeason option')
	_.pr()
	_.pr('Seasons:',len(seasons))
	_.pr()
	shows = tree.cssselect('a[itemprop="name"]')

	episodeList = []
	episodeListIds = []

	theTitle = _str.cleanBE(theTitle,' ')
	global zeroList
	zeroList = zeroList.lower()
	zeroListX = zeroList.split(',')
	if theTitle.lower() in zeroListX:
		isZero = True
		# _.pr('zero')
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
		_.pr('\t',showId,'\t',showTitle)
		episodeListIds.append(showId)
		episodeList.append({'id': showId, 'title': showTitle, 'url': siteBase + link })



	if eId in episodeListIds:
		for i,episode in enumerate(episodeList):
			if eId == episode['id']:
				# _.pr(episode['url'])
				# __.xit()
				lookupEpisode(theYear,theTitle,episode['id'],episode['title'],episode['url'])
	else:
		_.pr('No Episode Found')
		__.xit()



def isSeasonZero(url):
	print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
	page = requests.get(url)
	tree = html.fromstring(page.content)
	data0 = tree.cssselect('.bp_text_only')
	try:
		data = cleanupString(data0[0].text_content())
	except Exception as e:
		_.e('error')
		# data = cleanupString(data0[0].text_content())
	data = _str.cleanBE(data,' ')
	if data[len(data)-1] == '0':
		result = True
	else:
		result = False
	# _.pr(data)
	# __.xit()
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
	# _.pr(seasonData)
	# seasonData = [{'year': theYear, 'title': theTitle, 'seasons': seasonList}]
	# seasonList.append({'season': season, 'episodes': episodeSet})
	# episodeList.append({'id': showId, 'title': showTitle, 'url': siteBase + link })
	# _.pr(seasonData[0]['title'])

	for data in seasonData:
		if data['title'] == theTitle:
			_.pr()
			_.pr('Seasons:',len(data['seasons']))
			_.pr()
			episodeListIds = []
			episodeList = []
			for se in data['seasons']:
				_.pr()
				_.pr()
				_.pr('Season:',se['season'])
				_.pr()
				for ep in se['episodes']:
					_.pr('\t',ep['id'],'\t',airdateAlignRight(ep['airdate']),'\t',ep['title'])
					episodeList.append(ep)
					episodeListIds.append(ep['id'])
			_.pr()
			_.pr()
			selection = input('Make Selection - ')
			_.pr()

			if len(selection) == 0:
				selection = 'x'
			if selection.lower() == 'x':
				__.xit()
			if selection in episodeListIds:
				for i,episode in enumerate(episodeList):
					if selection == episode['id']:
						_.pr(episode['url'])
						# __.xit()
						lookupEpisode(data['year'],data['title'],episode['id'],episode['title'],episode['url'])
			_.pr()

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
	# _.pr(iDs)
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	data = []
	shows = []
	dateList = []
	for d in seasonData:
		if d['id'] in iDs:
			data.append(d)
			# _.pr(d['title'])
			shows.append({'id': d['id'], 'title': d['title'].replace(',','_'), 'started': d['seasons'][0]['episodes'][0]['airdate']})
			for seasons in d['seasons']:
				for episodes in seasons['episodes']:
					dateList.append(episodes['airdate'])

	shows = sorted(shows, key=itemgetter('started'))
	dateList.sort()
	def findDateMatch(theDate,theId):
		result = ''
		# _.pr(data)
		for d in data:
			if d['id'] == theId:
				for seasons in d['seasons']:
					for episodes in seasons['episodes']:
						# _.pr(episodes)
						if episodes['airdate'] == theDate:
							result = episodes['id']
							break
		return result
	def findIDMatch(theId,theTitle):
		result = ''
		# _.pr(data)
		for d in data:
			if d['title'] == theTitle:
				for seasons in d['seasons']:
					for episodes in seasons['episodes']:
						# _.pr(episodes)
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
	# _.pr(c)
	_.tables.register('Auto',dataTable,w=1)
	_.tables.print('Auto',c)
	_.pr()
	_.pr(len(dataTable))

	def makeSelection():
		_.pr()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 's':
			_.pr()
			# _.pr(0,' All')
			for i,s in enumerate(shows):
				_.pr(i+1,s['title'])
			searchIn = input('Seach In - ')
			_.pr()
			searchFor = input('Seach For - ')
			if searchIn == '0':
				_.pr('Selected:','All')
			else:
				spent = []
				for i,s in enumerate(shows):
					sel = str(i+1)
					if searchIn == sel:
						_.pr('Selected:',s['title'])
						_.pr()
						for dt in dataTable:
							if not dt[s['title'].lower()] in spent:
								spent.append(dt[s['title'].lower()])
								# dt[s['title'].lower()]
								url = findIDMatch(dt[s['title'].lower()],s['title'])
								# print_url(frameinfo=getframeinfo(currentframe()), url=url)
								print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
								page = requests.get(url)
								tree = html.fromstring(page.content)
								data0 = tree.cssselect('.summary_text')
								data = cleanupString(data0[0].text_content())
								data = _str.cleanBE(data,' ')
								found = False
								if len(searchFor) == 0:
									_.pr()
									_.pr(dt[s['title'].lower()],data)
								else:

									for theSearch in searchFor.split(' '):
										if theSearch.lower() in data.lower():
											found = True
											_.pr(dt[s['title'].lower()],data)
											break
									if found:
										pause = input('break? ')
										if 'y' in pause.lower():
											break


								# _.pr(dt[s['title'].lower()])

	makeSelection()
	# for dt in dataTable:
	#   _.pr(dt)
	# dateList = sorted(dateList, key=itemgetter('started'))
	# for s in shows:
	#   _.pr(s['started'],s['title'])
def episodes(url,theYear='',theTitle=''):
	if _.switches.isActive('BuildCrossRef'):
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')
		_.pr('Processing...')
	global seasonData
	if theTitle == '':
		print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
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
	#   _.pr('still running')
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
		# _.pr(thisURL)
		print_url(frameinfo=getframeinfo(currentframe()), url=thisURL,c='cyan')
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
			_.pr()
			_.pr('Seasons:',len(seasons)-1)
			_.pr()
		else:
			unknown = False
			_.pr()
			_.pr('Seasons:',len(seasons))
			_.pr()
		episodeList = []
		seasonList = []
		episodeListIds = []
		for i,s in enumerate(seasons):
			season = str(i+1)
			if int(season) == len(seasons) and unknown:
				thisURL = newURL.replace('THESEASON','-1')
			else:
				thisURL = newURL.replace('THESEASON',season)
				print_url(frameinfo=getframeinfo(currentframe()), url=thisURL,c='cyan')
				page = requests.get(thisURL)
				tree = html.fromstring(page.content)
				episodeCode = tree.cssselect('div[itemprop="episodes"]')
				_.pr()
				_.pr()
				if int(season) == len(seasons) and unknown:
					_.pr('Season:',season,' - Unknown')
				else:
					_.pr('Season:',season)
				_.pr()
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
					_.pr('\t',showId,'\t',airdateAlignRight(airdate),'\t',showTitle)
					episodeListIds.append(showId)
					episodeList.append({'id': showId, 'title': showTitle, 'url': siteBase + link, 'airdate': airdate})
					episodeSet.append({'id': showId, 'title': showTitle, 'url': siteBase + link, 'airdate': airdate})
				seasonList.append({'season': season, 'episodes': episodeSet})

		seasonData.append({'id': getIdFromUrl(url), 'year': theYear, 'title': theTitle, 'seasons': seasonList, 'date': str(today)})
		_.saveTable(seasonData,seasonDataFile,True,False)
		_.pr()
		_.pr()
		# _.pr(_.switches.isActive('BuildCrossRef'))
		if not _.switches.isActive('BuildCrossRef'):
			selection = input('Make Selection - ')
			selection = selection.replace(' ','')
			_.pr()
			if len(selection) == 0:
				selection = 'x'
			if selection.lower() == 'x':
				__.xit()
			if selection in episodeListIds:
				for i,episode in enumerate(episodeList):
					if selection == episode['id']:
						_.pr(episode['url'])
						# __.xit()
						lookupEpisode(theYear,theTitle,episode['id'],episode['title'],episode['url'])
			else:
				_.pr('Error')


			_.pr()

def lookupEpisode(theYear,theTitle,showId,showTitle,url):
	# link = url.split('?')[0] + 'fullcredits?ref_=tt_cl_sm#cast'
	# def lookupMovie
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

	# print_url(frameinfo=getframeinfo(currentframe()), url=url)
	# 'https://www.imdb.com/title/tt1998643/?ref_=ttep_ep1'
	# 'https://www.imdb.com/title/tt1998643/fullcredits?ref_=tt_cl_sm#cast'
	print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
	page = requests.get(url)
	tree = html.fromstring(page.content)
	shows = tree.cssselect('a[itemprop="name"]')


	titleParent = tree.cssselect('.titleParent')
	ta = titleParent[0].cssselect('a')
	parentURL = 'https://www.imdb.com' + str(ta[0].attrib['href'])
	parentURL = parentURL.replace('?ref_=tt_ov_inf','')
	print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
	page = requests.get(url)
	tree = html.fromstring(page.content)
	data0 = tree.cssselect('.summary_text')
	data = cleanupString(data0[0].text_content())
	data = _str.cleanBE(data,' ')

	_.pr()
	_.pr(theTitle)
	_.pr()
	_.pr('\t Episode:',showId)
	_.pr()
	_.pr('\t\t',showTitle)
	_.pr()
	_.pr('\t\t\t',data)
	_.pr()
	_.pr()

	print_url(frameinfo=getframeinfo(currentframe()), url=url.split('?')[0] + 'fullcredits?ref_=tt_cl_sm#cast',c='cyan')
	page = requests.get(url.split('?')[0] + 'fullcredits?ref_=tt_cl_sm#cast')
	tree = html.fromstring(page.content)

	cast = tree.cssselect('.cast_list')
	tr = cast[0].cssselect('tr')
	# _.pr(len(tr))
	people = []
	people2 = []

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
			people = registerPerson(people,person,link,character)
			people2.append({'name': person, 'link': link, 'character': character})

	_.tables.register('Auto',people,w=1)
	_.tables.fieldProfileSet( 'Auto', 'character', 'trigger', _.longDashAdd )
	_.tables.print('Auto','id,name,character')



	def makeSelection():
		_.pr()
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
			_.pr('l','url')
			_.pr('(e)pisodes')
			_.pr('e(x)it')

		if selection == 'e':

			# pause = input('pause')


			episodes(parentURL,theYear,theTitle)


		if selection == 'l' or selection == 'url' :
			try:
				webbrowser.open(url, new=2)
			except Exception as e:
				try:
					native_web_app.open(url)
				except Exception as e:
					_.cp( 'Error: unable to open browser', 'red' )


		if selection == 'x' or selection == 'exit':
			__.xit()
		makeSelection()

	makeSelection()



def movieRating(url):
	if _.switches.isActive('Score'):
		title = _.switches.value('Movie')

		newURL = 'https://www.imdb.com/title/' + getIdFromUrl(url) + '/ratings'
		# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)

		print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		description0 = tree.cssselect('.allText')
		description1 = description0[0].text_content()
		description = cleanupString(description1)

		try:
			_.pr(description.split('vote of ')[1],title.replace(',',' '))
		except Exception as e:
			pass
		__.xit()


	if _.switches.isActive('QuickInfo'):
		_.pr('______________________________________________________________________________________________________')
		title = _.switches.value('Movie')
		_.printBold(title.replace(',',' '))

		newURL = 'https://www.imdb.com/title/' + getIdFromUrl(url) + '/ratings'
		# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
		print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		description0 = tree.cssselect('.allText')
		description1 = description0[0].text_content()
		description = cleanupString(description1)
		_.pr()
		try:
			peoplVoted0 = tree.cssselect('.ratingTable a')
			peoplVoted1 = peoplVoted0[0].text_content()
			peoplVoted = cleanupString(peoplVoted1)
		except Exception as e:
			peoplVoted = ''

		try:
			if not peoplVoted == '':
				_.pr(_.ColorBold.White + description.split('vote of ')[1] + _.ColorBold.END, '\t',peoplVoted,'people voted')
			else:
				_.pr(description.split('vote of ')[1],title.replace(',',' '))
		except Exception as e:
			pass

		newURL = 'http://www.imdb.com/title/' + getIdFromUrl(url) + '/?ref_=ttfc_fc_tt'
		# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
		print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		description0 = tree.cssselect('.summary_text')
		description1 = description0[0].text_content()
		description = cleanupString1(description1)
		_.pr()
		# _.printBold( description, 'grey' )
		# _.printBold( description, 'green' )
		# _.printBold( description, 'yellow' )
		# _.printBold( description, 'blue' )
		# _.printBold( description, 'magenta' )
		_.printBold( description, 'cyan' )
# white
# red
# grey
# green
# yellow
# blue
# magenta
# cyan
		_.pr()
	newURL = 'http://www.imdb.com/title/' + getIdFromUrl(url) + '/parentalguide'
	# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
	try:
		print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		try:
			tr = tree.cssselect('#mpaa-rating')
			td = tr[0].cssselect('td')
			description1 = td[1].text_content()
			description = cleanupString(description1)
			_.pr()
			_.pr(description)
			_.pr()
		except Exception as e:
			pass
		try:
			tr = tree.cssselect('#certifications-list')
			td = tr[0].cssselect('li')
			_.pr()
			_.pr('Rating:')
			for item in td:
				data0 = item.text_content()
				data1 = cleanupString(data0)
				# _.pr(data1)
				if 'United' in data1 and 'States' in data1:
					data = data1.split(':')
					ratingColor = 'green'
					data[1] = data[1].upper()
					if 'R' in data[1]:
						ratingColor = 'red'
					if 'MA' in data[1]:
						ratingColor = 'red'
					_.colorThis( '\t'+data[1], ratingColor )


			_.pr()
		except Exception as e:
			pass
		theRatings = []
		try:
			section = tree.cssselect('#advisory-nudity')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			_.pr()
			if not rating == 'Be':
				theRatings.append({'category': 'Sex','rating': rating})
				# _.pr('Sex:       \t',rating)
		except Exception as e:
			pass
		try:
			section = tree.cssselect('#advisory-violence')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			if not rating == 'Be':
				theRatings.append({'category': 'Violence','rating': rating})
				# _.pr('Violence:\t',rating)
		except Exception as e:
			pass
		try:
			section = tree.cssselect('#advisory-profanity')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			if not rating == 'Be':
				theRatings.append({'category': 'Profanity','rating': rating})
				# _.pr('Profanity:\t',rating)
		except Exception as e:
			pass
		try:
			section = tree.cssselect('#advisory-alcohol')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			if not rating == 'Be':
				theRatings.append({'category': 'Alcohol/Drugs','rating': rating})
				# _.pr('Alcohol/Drugs:\t',rating)
		except Exception as e:
			pass
		try:
			section = tree.cssselect('#advisory-frightening')
			rating0 = section[0].cssselect('.advisory-severity-vote')
			rating1 = cleanupString(rating0[0].text_content())
			rating = rating1.split(' ')[0]
			if not rating == 'Be':
				theRatings.append({'category': 'Frightening','rating': rating})
				# _.pr('Frightening:\t',rating)
		except Exception as e:
			pass
		try:
			if len(theRatings) > 0:
				_.tables.register('Auto',theRatings,w=1)
				_.tables.print('Auto','category,rating')
		except Exception as e:
			pass
	except Exception as e:
		_.pr('Information unavailable')
	_.pr()
###################################################################################
def isHallmark(thisID):
	global hallmark
	if len(hallmark) == 0:
		hallmark = _.getTable('hallmark.json')
	result = ''
	for hmk in hallmark:
		# if movie == hmk['name'] and year == hmk['year']:
		# _.pr(thisID)
		# _.pr(getIdFromUrl(hmk['link']))
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

	# _.pr(years)
	# __.xit()
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
		#   try:
		#       theList.append(xx['link'])
		#   except Exception as e:
		#       pass
		# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+tv+show',franchise,franchiseOmit):
		#   try:
		#       theList.append(xx['link'])
		#   except Exception as e:
		#       pass


		for theYear in years:
			theYear = str(theYear)
			for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+movies',franchise,franchiseOmit):
				try:
					theList.append(xx)
				except Exception as e:
					pass
			# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+series',franchise,franchiseOmit):
			#   try:
			#       theList.append(xx['link'])
			#   except Exception as e:
			#       pass
			# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+tv+show',franchise,franchiseOmit):
			#   try:
			#       theList.append(xx['link'])
			#   except Exception as e:
			#       pass



	# theList.append('http://www.imdb.com/list/ls025172800/')
	# theList.append('http://www.imdb.com/list/ls056346625/?sort=list_order,asc&st_dt=&mode=detail&page=1')
	# theList.append('http://www.imdb.com/list/ls056346625/?sort=list_order,asc&st_dt=&mode=detail&page=2')
	# theList.append('http://www.imdb.com/list/ls027316430/')
	# theList.append('http://www.imdb.com/list/ls027937692/')
	# _.pr(set(theList))
	# __.xit()
	_.saveTable(theList,'imdb_hallmark_auto_research_theList.json')
	_.pr('Lists:',len(theList))
	badIDs = 'ls076776375,ls066936786,ls076572568,ls074285945,ls070895912'
	badText = 'feel like,lifetime'
	dup = []
	dup2 = []
	# hallmarkDataRaw = []
	hallmarkDataRaw = _.getTable('imdb_hallmark_auto_tmp.json')
	if len(hallmarkDataRaw) == 0:
		for lnk in theList:
			thisID = getIdFromUrl(lnk['link'])
			# _.pr(thisID)
			if not thisID in dup:
				dup.append(thisID)
				if not lnk['name'].lower() in badText.split(',') and not thisID in badIDs.split(','):
					_.pr(lnk['link'].replace('https://www.imdb.com/','').replace('http://www.imdb.com/',''),lnk['name'].replace(' - IMDb','').replace('IMDb','').replace('imdb','').replace('IMDB',''))
					for xx in buildUrlList(lnk['link'],True):
						# _.pr(xx)
						try:
							if not str(xx['id']) in dup2:
								dup2.append(str(xx['id']))
								hallmarkDataRaw.append(xx)
						except Exception as e:
							pass
					_.pr('Total So Far:',len(buildUrlListDuplicate),len(hallmarkDataRaw))
					_.saveTable(buildUrlListDuplicate,'imdb_hallmark_auto_complated_IDs.json')
					_.pr()
	# _.pr(hallmarkDataRaw)
	_.pr(len(hallmarkDataRaw))
	_.saveTable(hallmarkDataRaw,'imdb_hallmark_auto_tmp.json')
	# pause = input('pause')
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	# pause = input('pause')
	# hallmark.append({'name': nameFix, 'year': year, 'link': movieURL, 'people': []})
	# _.tables.register('hallmarkraw',hallmarkDataRaw)
	# _.tables.print('hallmarkraw','year,name,link')
	# __.xit()
def buildHallmarkTable2():
	global hallmark
	def duplicateCheck(theID):
		result = False
		for hm in hallmark:
			if getIdFromUrl(hm['link']) == theID:
				result = True
		return result
	# def duplicateCheck(name,year):
	#   result = False
	#   for hm in hallmark:
	#       if hm['name'] == name and hm['year'] == year:
	#           result = True
	#   return result


	def buildTableH(url):
		print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
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
					_.pr(year,nameFix)
				if 'TV Movie' in name and duplicateCheck(getIdFromUrl(movieURL)) == False:
					hallmark.append({'name': nameFix, 'year': year, 'link': movieURL, 'people': []})
		except Exception as e:
			_.pr('Error:',url)
			# __.xit()
	if len(hallmark) < 1:
		now = datetime.datetime.now()
		# today = now.strftime("%Y-%m-%d")
		thisYear = int(str(now.strftime("%Y")))
		years = []
		years.append(thisYear+1)
		years.append(thisYear)
		for x in range(1,20):
			years.append(thisYear-x)

		# _.pr(years)
		# __.xit()
		franchise = 'hallmark'
		franchiseOmit = 'lifetime'
		theList = []
		for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+movies',franchise,franchiseOmit):
			try:
				theList.append(xx['link'])
			except Exception as e:
				pass
		# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+series',franchise,franchiseOmit):
		#   try:
		#       theList.append(xx['link'])
		#   except Exception as e:
		#       pass
		# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+tv+show',franchise,franchiseOmit):
		#   try:
		#       theList.append(xx['link'])
		#   except Exception as e:
		#       pass


		for theYear in years:
			theYear = str(theYear)
			for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+movies',franchise,franchiseOmit):
				try:
					theList.append(xx['link'])
				except Exception as e:
					pass
			# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+series',franchise,franchiseOmit):
			#   try:
			#       theList.append(xx['link'])
			#   except Exception as e:
			#       pass
			# for xx in getUrlList('https://www.google.com/search?q=imdb+'+franchise+'+'+theYear+'+tv+show',franchise,franchiseOmit):
			#   try:
			#       theList.append(xx['link'])
			#   except Exception as e:
			#       pass



		theList.append('http://www.imdb.com/list/ls025172800/')
		theList.append('http://www.imdb.com/list/ls056346625/?sort=list_order,asc&st_dt=&mode=detail&page=1')
		theList.append('http://www.imdb.com/list/ls056346625/?sort=list_order,asc&st_dt=&mode=detail&page=2')
		theList.append('http://www.imdb.com/list/ls027316430/')
		theList.append('http://www.imdb.com/list/ls027937692/')
		# _.pr(set(theList))
		# __.xit()
		_.pr('Lists:',len(set(theList)))
		hallmarkIDs = []
		for hlink in set(theList):
			# buildTableH(hlink)
			for xx in buildUrlList(hlink):
				hallmarkIDs.append(xx)
		_.pr(set(hallmarkIDs))
		_.pr(len(set(hallmarkIDs)))
		len(hallmark)


def buildFranchisePeople():
	global hallmark
	global hallmarkDataRaw
	if len(hallmark) < 1:
		buildHallmarkTable()
		hallmark = hallmarkDataRaw
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	_.pr()
	i = 0
	for hmk in hallmark:
		_.pr('Building people from: ',hmk['name'])
		try:
			if len(hallmark[i]['people']) == 0:
				peepsX = getHallmarkPeople(hmk['link'])
				hallmark[i]['people'] = peepsX
				_.saveTable(hallmark,'imdb_hallmark_auto_tmp.json',True,False)
			_.pr('People:',len(peepsX))
			_.pr()
		except Exception as e:
			_.pr('Error:',str(hmk['link']))
		i += 1
	hallmark = _.sort(hallmark,'year,name')
	if len(hallmark) > 100:
		_.pr(len(hallmark))
		_.saveTable(hallmark,'hallmark.json')
		_.saveTable(hallmark,'imdb_hallmark_auto_tmp.json')
	else:
		_.pr(len(hallmark))
		_.pr('Unspecified Error')

def buildHallmarkPeople():
	global hallmark
	global hallmarkDataRaw
	if len(hallmark) < 1:
		buildHallmarkTable()
		hallmark = hallmarkDataRaw
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	_.pr()
	i = 0
	for hmk in hallmark:
		_.pr('Building people from: ',hmk['name'])
		try:
			if len(hallmark[i]['people']) == 0:
				peepsX = getHallmarkPeople(hmk['link'])
				hallmark[i]['people'] = peepsX
				_.saveTable(hallmark,'imdb_hallmark_auto_tmp.json',True,False)
			_.pr('People:',len(peepsX))
			_.pr()
		except Exception as e:
			_.pr('Error:',str(hmk['link']))
		i += 1
	hallmark = _.sort(hallmark,'year,name')
	if len(hallmark) > 100:
		_.pr(len(hallmark))
		_.saveTable(hallmark,'hallmark.json')
		_.saveTable(hallmark,'imdb_hallmark_auto_tmp.json')
	else:
		_.pr(len(hallmark))
		_.pr('Unspecified Error')
def getHallmarkPeople(url):
	print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
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
		# _.pr(len(props))
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
#   page = requests.get(url)
#   tree = html.fromstring(page.content)
#   cast = tree.cssselect('.cast_list')
#   tr = cast[0].cssselect('tr')

#   people = []
#   print_url(frameinfo=getframeinfo(currentframe()), url=url)
#   _.pr(len(tr))
#   for e in tr:
#       try:
#           char = e.cssselect('.character')
#           character = cleanupString(char[0].text_content())
#       except Exception as ee:
#           character = ''

#       props = e.cssselect('.itemprop')
#       i = 0
#       _.pr(len(props))
#       for p in props:
#           if i == 0:
#               link = ''
#               try:
#                   links = p.cssselect('a')
#                   link = str(links[0].attrib['href'])
#               except Exception as e:
#                   pass
#               person = p.text_content()
#               person = cleanupString(person)
#               people = registerPerson(people,person,link,character)
#           i += 1
#   return people
def google(searchFor,personMovie):
	foundAlias = False
	theAliasID_imdbID = theAliasID(searchFor,personMovie,'imdbID')
	# test = input('alias: ' + theAliasID_imdbID + ' ' + personMovie)

	if not type(theAliasID_imdbID) == bool:
		return theAliasID_imdbID

	if not type(theAliasID_imdbID) == bool:

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
		# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
		# print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		# tables = tree.cssselect('.r')
		tables = tree.cssselect('a')
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
			# _.pr(item)
			if 'imdb' in item.lower():
				# links = t.cssselect('a')
				link = str(t.attrib['href'])
				link = link.replace('/url?q=http:','http:')
				text = t.text_content()
				###################################################################################################
				# _.pr(item,link)

				if '/title/' in link:
					theURL = extractUrl(link) + 'fullcredits?ref_=tt_cl_sm#cast'
					if not checkDup(getIdFromUrl(theURL)):
						theList['movies'].append({'name': text,'link': theURL})
						# _.pr(theList)


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
					_.pr('0 No Results')
				__.xit()
			elif total == 1:
				if len(theList['movies']) == 1:
					addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList[0]['link']))
					result = lookupMovie(theList[0]['link'])
				else:
					addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList[0]['link']))
					result = lookupPerson(theList[0]['link'])
			else:
				_.pr()
				ran = False

				if personMovie == 'person':
					ran = True
					if len(theList['people']) > 0:
						i = 0
						for item in theList['people']:
							_.pr(i, theList['people'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
							i += 1
						_.pr()
						selection = input('Make Selection - ')
						_.pr()
						if selection == 'x':
							__.xit()
						elif not selection == 'm':
							addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList['people'][int(selection)]['link']))
							result = lookupPerson(theList['people'][int(selection)]['link'])
					else:
						selection = 'm'
						_.pr()
						_.pr('No people found')
						_.pr()
				if personMovie == 'movie' or selection == 'm':
					ran = True
					if len(theList['movies']) > 0:
						i = 0
						for item in theList['movies']:
							_.pr(i, theList['movies'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
							i += 1
						_.pr()
						selection = input('Make Selection - ')
						_.pr()
						if selection == 'x':
							__.xit()
						elif not selection == 'm':
							addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList['movies'][int(selection)]['link']))
							result = lookupMovie(theList['movies'][int(selection)]['link'])
					else:
						selection = 'm'
						_.pr()
						_.pr('No movies found')
						_.pr()

				elif not ran and (personMovie == 'person' or selection == 'm'):
					if len(theList['people']) > 0:
						i = 0
						for item in theList['people']:
							_.pr(i, theList['people'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
							i += 1
						_.pr()
						selection = input('Make Selection - ')
						_.pr()
						if selection == 'x':
							__.xit()
						elif not selection == 'm':
							addAliasID(searchFor,personMovie,'imdbID',getIdFromUrl(theList['people'][int(selection)]['link']))
							result = lookupPerson(theList['people'][int(selection)]['link'])
					else:
						selection = 'm'
						_.pr()
						_.pr('No people found')
						_.pr()
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
			_.pr('1 No Results')
	return result



def googleID(searchFor,personMovie):

	foundAlias = False
	theAliasID_imdbID = theAliasID(searchFor,personMovie,'imdbID')
	# theAliasID_imdbID = ''
	# test = input('alias: ' + theAliasID_imdbID + ' ' + personMovie)

	if not type(theAliasID_imdbID) == bool:
		# if not len( theAliasID_imdbID ):
		if 'sample' in searchFor.lower():
			_.pr(  )
			_.pr( '______________________________' )
			_.pr( searchFor, theAliasID_imdbID )
			__.xit()
		return theAliasID_imdbID
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
		# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
		# print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		tables = tree.cssselect('a')
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
			# _.pr(item)
			if 'imdb' in item.lower():
				links = t
				link = str(links.attrib['href'])
				link = link.replace('/url?q=http:','http:')
				text = t.text_content()
				###################################################################################################
				# _.pr(item,link)

				if '/title/' in link:
					theURL = extractUrl(link) + 'fullcredits?ref_=tt_cl_sm#cast'
					if not checkDup(getIdFromUrl(theURL)):
						theList['movies'].append({'name': text,'link': theURL})
						# _.pr(theList)

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
				# _.pr( 'No Movie' )

		if personMovie == 'person':
			result = getIdFromUrl(theList['people'][0]['link'])
			addAliasID(searchFor,personMovie,'imdbID',result)

	if result.startswith('tt') or result.startswith('nm'):
		addAliasID(searchFor,personMovie,'imdbID',result)
	return result



def googleID_OLD(searchFor,personMovie):

	foundAlias = False
	theAliasID_imdbID = theAliasID(searchFor,personMovie,'imdbID')
	# theAliasID_imdbID = ''
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
		# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
		print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')
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
			# _.pr(item)
			if 'imdb' in item.lower():
				links = t.cssselect('a')
				link = str(links[0].attrib['href'])
				link = link.replace('/url?q=http:','http:')
				text = t.text_content()
				###################################################################################################
				# _.pr(item,link)

				if '/title/' in link:
					theURL = extractUrl(link) + 'fullcredits?ref_=tt_cl_sm#cast'
					if not checkDup(getIdFromUrl(theURL)):
						theList['movies'].append({'name': text,'link': theURL})
						# _.pr(theList)

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
				# _.pr( 'No Movie' )

		if personMovie == 'person':
			result = getIdFromUrl(theList['people'][0]['link'])
			addAliasID(searchFor,personMovie,'imdbID',result)

	return result

def rottenTomatoesRank(movie):
	url = 'https://www.google.com/search?q=rotten+tomatoes+rating+'
	newURL = url + _str.replaceAll(_str.replaceAll(movie,',','+'),' ','+')
	print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')
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
				_.pr('2 No Results')
			__.xit()
		elif total == 1:
			if len(theList['movies']) == 1:
				result = lookupMovie(theList[0]['link'])
			else:
				result = lookupPerson(theList[0]['link'])
		else:
			_.pr()
			ran = False
			if personMovie == 'person':
				ran = True
				if len(theList['people']) > 0:
					i = 0
					for item in theList['people']:
						_.pr(i, theList['people'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
						i += 1
					_.pr()
					selection = input('Make Selection - ')
					_.pr()
					if selection == 'x':
						__.xit()
					elif not selection == 'm':
						result = lookupPerson(theList['people'][int(selection)]['link'])
				else:
					selection = 'm'
					_.pr()
					_.pr('No people found')
					_.pr()
			if personMovie == 'movie' or selection == 'm':
				ran = True
				if len(theList['movies']) > 0:
					i = 0
					for item in theList['movies']:
						_.pr(i, theList['movies'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
						i += 1
					_.pr()
					selection = input('Make Selection - ')
					_.pr()
					if selection == 'x':
						__.xit()
					elif not selection == 'm':
						result = lookupMovie(theList['movies'][int(selection)]['link'])
				else:
					selection = 'm'
					_.pr()
					_.pr('No movies found')
					_.pr()

			elif not ran and (personMovie == 'person' or selection == 'm'):
				if len(theList['people']) > 0:
					i = 0
					for item in theList['people']:
						_.pr(i, theList['people'][i]['name'].replace(' - IMDb','').replace('IMDb',''))
						i += 1
					_.pr()
					selection = input('Make Selection - ')
					_.pr()
					if selection == 'x':
						__.xit()
					elif not selection == 'm':
						result = lookupPerson(theList['people'][int(selection)]['link'])
				else:
					selection = 'm'
					_.pr()
					_.pr('No people found')
					_.pr()
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
			_.pr('3 No Results')
	return result

def dataPerson(url):
	global _async
	global dataPerson_data


	if __.print_html_page_IDs:
		_.pr( getIdFromUrl(url) )


	if url in dataPerson_data:
		if _.daysDiff( dataPerson_data[url]['timestamp'], time.time() ) < __.data_day_diff:
			try:
				if dataPerson_data[url]['img']:
					return dataPerson_data[url]
			except Exception as e:
				pass
	# 3aaf1206
	print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')

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
	for pn in personName:
		theirName0 = cleanupString(pn.text_content())
		if len(theirName0) > 0:
			theirName = theirName0
	img0 = tree.cssselect('img')
	img = ''
	found = False
	for img1 in img0:
		img2 = img1.attrib['src']
		alt=img1.get('alt')
		if not found:
			if '317_AL_.jpg' in img2 or theirName == alt:
				found = True
				img = img2
	if not found:
		img_element = tree.xpath('//img[@loading="eager"]')
		if img_element:
			found = True
			img = img_element[0].get('src')

	dataPerson_data[url] = { 'name': theirName, 'age': age, 'img': img, 'timestamp': time.time() }
	if _async is None:
		_.saveTable( dataPerson_data, '-imdb-dataPerson.index', p=0 )
	return dataPerson_data[url]

def dataMovie(url):
	global _async
	global dataMovie_data


	if __.print_html_page_IDs:
		_.pr( getIdFromUrl(url) )


	if url in dataMovie_data:
		if _.daysDiff( dataMovie_data[url]['timestamp'], time.time() ) < __.data_day_diff:

			try:
				if dataMovie_data[url]['name']:
					return dataMovie_data[url]
			except Exception as e:
				pass

	print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
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
	dataMovie_data[url] = { 'name': theTitle, 'year': theYear, 'img': img, 'timestamp': time.time() }
	if _async is None:
		_.saveTable( dataMovie_data, '-imdb-dataMovie.index', p=0 )
	return dataMovie_data[url]
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
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	_.pr('allPeople:\t',len(allPeople))
	_.pr('allMovies:\t',len(allMovies))
	_.pr('relationships:\t',len(relationships))
	_.pr('xData:       \t',len(xData))
	# __.xit()
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
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')
		_.pr()
		_.pr('Cross referenceing:')
		for rm1 in relMovies:
			for am in allMovies:
				if am['id'] == rm1:
					_.pr('\t',am['name'])
		_.pr()
		_.pr()


		for resID0 in set(relResults):
			found = False
			for ap2 in allPeople:
				if resID0 == ap2['id'] and not found:
					found = True
					newResults.append({'id': ap2['id'], 'name': ap2['name'], 'link': ap2['link'], })
		i = 0
		for result in newResults:
			__.p(i,result['name'],w=_.switches.value('WebTable'))
			i += 1
		_.pr()
		_.pr(len(newResults))
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
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')
		_.pr()
		_.pr('Cross referenceing:')
		for rm1 in relPeople:
			for ap in allPeople:
				if ap['id'] == rm1:
					_.pr('\t',ap['name'])

		_.pr()
		_.pr()
		for resID1 in set(relResults):
			found = False
			for am2 in allMovies:
				if resID1 == am2['id'] and not found:
					found = True
					newResults.append({'id': am2['id'], 'name': am2['name'], 'link': am2['link'], })
		i = 0
		for result in newResults:
			__.p(i,result['name'],w=_.switches.value('WebTable'))
			i += 1
		_.pr()
		_.pr(len(newResults))



	_.switches.fieldSet('BuildCrossRef','active',False)

	def makeSelection():
		_.pr()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 'h' or selection == '?' or selection == 'help':
			_.pr('(s)earch')
			_.pr('page')
			_.pr('save')
			_.pr('not')
			_.pr('e(x)it')

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
			__.xit()
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
			_.pr()
			_.pr('Un-invited')
			_.pr()
			_.tables.register('uninvited',uninvited,w=1)
			_.tables.fieldProfileSet( 'uninvited', 'character', 'trigger', _.longDashAdd )
			_.tables.print('uninvited','id,name,character')



		if selection == 'page':
			_.pr( 'document.querySelectorAll(\'.box\').length' )
			rows = []
			theFile = 'test.htm'
			file0 = _v.stmp + os.sep + theFile
			rows.append('<html><head>')
			rows.append('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>')
			# rows.append('<script type="text/javascript" src="http://www.pillerbeauty.com/js/jquery-1.11.3.js"></script>')
			# rows.append('<script type="text/javascript" src="http://www.pillerbeauty.com/js/jquery-ui.min.js"></script>')
			rows.append('<style type="text/css">')
			rows.append('.box { display: inline-block; position: relative; min-width: 100px; margin: 10px; padding: 10px; }')
			# rows.append('.img { display:inline; padding: 10px; }')
			rows.append('</style>')
			rows.append('</head><body>')
			pageMoviePersonLabel = ''
			if _.switches.isActive('Movie'):
				pageMoviePersonLabel += ' '.join( _.switches.values('Movie') ) + ' '
			if _.switches.isActive('Person'):
				pageMoviePersonLabel += ' '.join( _.switches.values('Person') ) + ' '
			rows.append('<h4>')
			rows.append(pageMoviePersonLabel)
			rows.append('</h4>')
			temp_file_label = '-imdb-xREF-__'+pageMoviePersonLabel.replace(' ','_').replace('_and_','__AND__')+'.htm'
			temp_file_label_path = _v.stmp +os.sep+ temp_file_label
			if os.path.isfile(  temp_file_label_path  ):
				e5de297b=str(requests.post('https://etc.ac/a/imdb/upload.php', data = { 'data': '\n'.join(_.getText(temp_file_label_path)) }).content,'iso-8859-1')
				print('https://etc.ac/a/imdb/')
				print(e5de297b)
				_.pr( temp_file_label_path )
				try:
					webbrowser.open(  'file://' + os.path.realpath(temp_file_label_path) , new=2)
				except Exception as e:
					try:
						native_web_app.open(  'file://' + os.path.realpath(temp_file_label_path)  )
					except Exception as e:
						_.cp( 'Error: unable to open browser', 'red' )
				__.xit()








			global dataPerson_data
			if dataPerson_data is None:
				dataPerson_data = _.getTable( '-imdb-dataPerson.index' )
			global dataMovie_data
			if dataMovie_data is None:
				dataMovie_data = _.getTable( '-imdb-dataMovie.index' )

			if _.switches.isActive('xRef-Page-Threaded'):


				stuff = 0
				if _.switches.isActive('Movie'):
					_.pr(len(newResults))
					for nr in newResults:
						if not nr['link'] in dataPerson_data:
							stuff += 1
						# data = dataPerson()
				if _.switches.isActive('Person'):
					_.pr(len(newResults))
					for nr in newResults:
						if not nr['link'] in dataMovie_data:
							stuff += 1
						# data = dataMovie(nr['link'])


				if stuff > 5:
					global _async
					if _async is None:
						_async = _.regImp( __.appReg, '_rightThumb._asynchronous' )
					# __.asyn.cp( 'data', 2 )
					try:
						__.asyn.web( 30, safe=3, p=1 )
					except Exception as e:
						_async = _.regImp( __.appReg, '_rightThumb._asynchronous' )

					__.asyn.web( 30, safe=3, p=1 )

					__.asyn.atExit( category=None, name=None, fn=threads_done )

					if _.switches.isActive('Movie'):
						_.pr(len(newResults))
						for nr in newResults:
							if not nr['link'] in dataPerson_data:
								__.asyn.register( name='dataPerson', category='scan', fn=dataPerson, a=nr['link'], timeout=120 )
							# data = dataPerson()
					if _.switches.isActive('Person'):
						_.pr(len(newResults))
						for nr in newResults:
							if not nr['link'] in dataMovie_data:
								__.asyn.register( name='dataMovie', category='scan', fn=dataMovie, a=nr['link'], timeout=120 )
							# data = dataMovie(nr['link'])

					while not __.threads_complete:
						time.sleep(.5)
						pass
					time.sleep(1)

					_.saveTable( dataPerson_data, '-imdb-dataPerson.index', p=0 )
					_.saveTable( dataMovie_data, '-imdb-dataMovie.index', p=0 )




			if _.switches.isActive('Movie'):

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

			if _.switches.isActive('Person'):
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

			_.saveTable( dataPerson_data, '-imdb-dataPerson.index', p=0 )
			_.saveTable( dataMovie_data, '-imdb-dataMovie.index', p=0 )
			_.tempFile(rows, temp_file_label )
			_.tempFile(rows,theFile)
			e5de297b=str(requests.post('https://etc.ac/a/imdb/upload.php', data = { 'data': '\n'.join(rows) }).content,'iso-8859-1')
			print('https://etc.ac/a/imdb/')
			print(e5de297b)

			_.saveTable( dataPerson_data, '-imdb-dataPerson.index', p=0 )
			_.saveTable( dataMovie_data, '-imdb-dataMovie.index', p=0 )

			try:
				webbrowser.open(  'file://' + os.path.realpath(file0) , new=2)
			except Exception as e:
				try:
					native_web_app.open(  'file://' + os.path.realpath(file0)  )
				except Exception as e:
					_.cp( 'Error: unable to open browser', 'red' )


			_.pr()
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
			_.pr()
			_.pr(newResults[selection]['name'],' - has been selected')
			_.pr()
			if _.switches.isActive('Movie') == True:
				lookupPerson(newResults[selection]['link'])
			if _.switches.isActive('Person') == True:
				lookupMovie(newResults[selection]['link'])

		except Exception as e:
			selectedSomething = False
			# _.pr('Unspecified Error')
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
	print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
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
		# _.pr(birthDate)
		# _.pr(birthYear)
		# _.pr(birthLocation)
		# _.pr(theName)
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

		_.pr(theName)
		_.pr(theYear)

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
			_.pr('\trows: ',len(result))
		else:
			_.pr('rows: ',len(result))
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
		#   even = evenOdd0
		#   odd = evenOdd1
		# else:
		#   odd = evenOdd0
		#   even = evenOdd1
		# evenOdd0 = []
		# evenOdd1 = []
		odd = []
		even = _.getTable('imdb_kevin_bacon_even.json')
		_.pr('people',len(allPeople))
		_.pr('entertainment',len(allMovies))
		_.pr('relationships',len(relationships))
		_.pr('completedIDs',len(completedIDs))
		_.pr('even',len(even))
		_.pr('odd',len(odd))

	else:
		even.append(autoLink(url))
	# for ev in even:
	#   _.pr(ev['name'])
	# __.xit()
	iii = 0
	j = 0
	while not found:
		iii += 1
		_.pr('______________________')
		_.pr('Nest Set:',iii)
		_.pr()
		j += .5
		# jf = str(j).replace('.0','').replace('0.','.')

		# _.pr(isEven(i))
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
					_.pr()
					_.pr('Found Kevin Bakon')
					_.pr()
					for kevin in set(bacon):
						_.pr('\t',kevin)
					_.pr()
					_.pr('\t\t',j, 'Degrees to Kevin Bakon')
					__.xit()
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
									_.pr('______________________','\n')
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
					_.pr()
					_.pr('Found Kevin Bakon')
					_.pr()
					for kevin in set(bacon):
						_.pr('\t',kevin)
					_.pr()
					_.pr('\t\t',j, 'Degrees to Kevin Bakon')
					__.xit()
			if _.switches.isActive('KevinBaconPickUp') == True and iii == 1:
				_.pr('odd',len(odd))
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
									_.pr('______________________','\n')
						except Exception as e:
							allErrors.append({'location': 'while', 'input': LOX['link'], 'stamp': millTimeStamp()})
					# _.pr(len(odd),eoi,_.switches.value('KevinBacon'))
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
		_.tables.register('The_Mistery_Person',misteryPerson,w=1)
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
								if platform.system() == 'Windows':
									os.system('cls')
								else:
									os.system('clear')
								_.pr()
								_.pr(ap['name'])

								try:
									webbrowser.open(  ap['link']  , new=2)
								except Exception as e:
									try:
										native_web_app.open(  ap['link']  )
									except Exception as e:
										_.cp( 'Error: unable to open browser', 'red' )

								selection = input('Continue (y/n)- ')
								if selection == 'n':
									done = True
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	_.pr()
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
		_.pr(i,result['name'])
		i += 1
	_.pr()
	_.pr(len(newResults))



	_.switches.fieldSet('BuildCrossRef','active',False)
	def makeSelection():
		_.pr()
		selectedSomething = False
		selection = input('Make Selection - ')
		selection = selection.lower()
		if len(selection) == 0:
			selection = 'x'
		if selection == 'h' or selection == '?' or selection == 'help':
			_.pr('(s)earch')
			_.pr('e(x)it')
			_.pr('save')
			_.pr('page')
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
			__.xit()
		if selection == 'page':
			_.pr( 'document.querySelectorAll(\'.box\').length' )
			rows = []
			theFile = 'test.htm'
			file0 = _v.stmp + os.sep + theFile
			rows.append('<html><head>')
			rows.append('<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>')
			# rows.append('<script type="text/javascript" src="http://www.pillerbeauty.com/js/jquery-1.11.3.js"></script>')
			# rows.append('<script type="text/javascript" src="http://www.pillerbeauty.com/js/jquery-ui.min.js"></script>')
			rows.append('<style type="text/css">')
			rows.append('.box { display: inline-block; position: relative; min-width: 100px; margin: 10px; padding: 10px; }')
			# rows.append('.img { display:inline; padding: 10px; }')
			rows.append('</style>')
			rows.append('</head><body>')
			pageMoviePersonLabel = ''
			if _.switches.isActive('Movie'):
				pageMoviePersonLabel += ' '.join( _.switches.values('Movie') ) + ' '
			if _.switches.isActive('Person'):
				pageMoviePersonLabel += ' '.join( _.switches.values('Person') ) + ' '
			rows.append('<h4>')
			rows.append(pageMoviePersonLabel)
			rows.append('</h4>')
			temp_file_label = '-imdb-xREF-__'+pageMoviePersonLabel.replace(' ','_').replace('_and_','__AND__')+'.htm'
			temp_file_label_path = _v.stmp +os.sep+ temp_file_label
			if os.path.isfile(  temp_file_label_path  ):
				e5de297b=str(requests.post('https://etc.ac/a/imdb/upload.php', data = { 'data': '\n'.join(_.getText(temp_file_label_path)) }).content,'iso-8859-1')
				print('https://etc.ac/a/imdb/')
				print(e5de297b)
				_.pr( temp_file_label_path )
				try:
					webbrowser.open(  'file://' + os.path.realpath(temp_file_label_path) , new=2)
				except Exception as e:
					try:
						native_web_app.open(  'file://' + os.path.realpath(temp_file_label_path)  )
					except Exception as e:
						_.cp( 'Error: unable to open browser', 'red' )
				__.xit()













			global dataPerson_data
			if dataPerson_data is None:
				dataPerson_data = _.getTable( '-imdb-dataPerson.index' )
			global dataMovie_data
			if dataMovie_data is None:
				dataMovie_data = _.getTable( '-imdb-dataMovie.index' )

			if _.switches.isActive('xRef-Page-Threaded'):


				stuff = 0
				if _.switches.isActive('Movie'):
					_.pr(len(newResults))
					for nr in newResults:
						if not nr['link'] in dataPerson_data:
							stuff += 1
						# data = dataPerson()
				if _.switches.isActive('Person'):
					_.pr(len(newResults))
					for nr in newResults:
						if not nr['link'] in dataMovie_data:
							stuff += 1
						# data = dataMovie(nr['link'])


				if stuff > 5:
					global _async
					if _async is None:
						_async = _.regImp( __.appReg, '_rightThumb._asynchronous' )
					# __.asyn.cp( 'data', 2 )
					__.asyn.web( 10, safe=3, p=1 )

					__.asyn.atExit( category=None, name=None, fn=threads_done )

					if _.switches.isActive('Movie'):
						_.pr(len(newResults))
						for nr in newResults:
							if not nr['link'] in dataPerson_data:
								__.asyn.register( name='dataPerson', category='scan', fn=dataPerson, a=nr['link'], timeout=120 )
							# data = dataPerson()
					if _.switches.isActive('Person'):
						_.pr(len(newResults))
						for nr in newResults:
							if not nr['link'] in dataMovie_data:
								__.asyn.register( name='dataMovie', category='scan', fn=dataMovie, a=nr['link'], timeout=120 )
							# data = dataMovie(nr['link'])

					while not __.threads_complete:
						time.sleep(.5)
						pass
					time.sleep(1)
					_.saveTable( dataPerson_data, '-imdb-dataPerson.index', p=0 )
					_.saveTable( dataMovie_data, '-imdb-dataMovie.index', p=0 )














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
			_.saveTable( dataPerson_data, '-imdb-dataPerson.index', p=0 )
			_.saveTable( dataMovie_data, '-imdb-dataMovie.index', p=0 )
			_.tempFile(rows, temp_file_label)
			_.tempFile(rows,theFile)

			_.saveTable( dataPerson_data, '-imdb-dataPerson.index', p=0 )
			_.saveTable( dataMovie_data, '-imdb-dataMovie.index', p=0 )

			try:
				webbrowser.open(  'file://' + os.path.realpath(file0)  , new=2)
			except Exception as e:
				try:
					native_web_app.open(  'file://' + os.path.realpath(file0)  )
				except Exception as e:
					_.cp( 'Error: unable to open browser', 'red' )


			_.pr()
		if selection == 'p' or selection == 'pic':
			# webbrowser.open(img, new=2)

			try:
				webbrowser.open(  img  , new=2)
			except Exception as e:
				try:
					native_web_app.open(  img  )
				except Exception as e:
					_.cp( 'Error: unable to open browser', 'red' )



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
			_.pr()
			_.pr(newResults[selection]['name'],' - has been selected')
			_.pr()
			if _.switches.isActive('Movie') == True:
				lookupPerson(newResults[selection]['link'])
			if _.switches.isActive('Person') == True:
				lookupMovie(newResults[selection]['link'])

		except Exception as e:
			selectedSomething = False
			# _.pr('Unspecified Error')
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
			# _.pr(len(xData[0]['people']),len(xData[1]['people']))
			# __.xit()
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
				_.pr()
				_.pr(theMovies[0]['year'],theMovies[0]['name'])
				_.pr()
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



						_.pr('\t',peeps0['name'],peepsLengthSpacer+'\t','(' + peeps0['character'] + ')')
				else:
					_.tables.register('Auto',theMovies[0]['people'],w=1)
					_.tables.print('Auto','name')
				_.pr('_____________________________________________________')
				hallmarkCharecters = []
				for peeps1 in theMovies[0]['people']:

					found = False
					jj = 0
					peepsLengthMax = 0
					for hm in hallmark:
						for peeps2 in hm['people']:
							if peeps1['name'] == peeps2['name'] and not hm['name'] == theMovies[0]['name']:
								# _.pr(hm['name'])
								length = len(hm['name'])
								if length > peepsLengthMax:
									peepsLengthMax = length
					for hm in hallmark:
						for peeps2 in hm['people']:
							if peeps1['name'] == peeps2['name'] and not hm['name'] == theMovies[0]['name']:
								if found == False:
									pass
									if view == 1:
										_.pr()
										_.pr('\t',peeps1['name'])
								if view == 1:
									peepsLengthDiff = peepsLengthMax - len(hm['name'])
									peepsLengthSpacer = ''
									ix = 0
									while ix < peepsLengthDiff:
										peepsLengthSpacer += ' '
										ix += 1
									_.pr('\t\t ',hm['year'],hm['name'],peepsLengthSpacer+'\t','(' + peeps2['character'] + ')')
								else:
									hallmarkCharecters.append({'name': str(peeps1['name']), 'year': hm['year'], 'movie': hm['name'], 'character': peeps2['character'], })
								jj += 1
								found = True
					if found:
						pass
						if view == 1:
							_.pr('\t\t',jj)
							_.pr()
					else:
						pass
						# _.pr('\t',peeps1['name'])
				if view == 0:
					_.groupSeparator = ''
					_.switches.fieldSet('Long','active',True)
					_.switches.fieldSet('Long','value','movie,character')
					_.switches.fieldSet('GroupBy','active',True)
					_.switches.fieldSet('GroupBy','value','name')
					_.tables.register('Char',hallmarkCharecters,w=1)
					# _.pr(hallmarkCharecters)
					# for hc in hallmarkCharecters:
						# _.pr(hc['name'])
					_.tables.print('Char','name,year,movie,character')
					# _.tables.print('Char','name')


			if len(theMovies) > 1:
				_.pr()
				_.switches.fieldSet('Long','active',True)
				_.switches.fieldSet('Long','value','name')
				_.switches.fieldSet('Sort','active',True)
				_.switches.fieldSet('Sort','value','year')
				_.tables.register('Auto',theMovies,w=1)
				_.tables.print('Auto','year,name')
				_.pr()
				_.pr(len(theMovies))
		else:
			if _.switches.value('Hallmark') == 'buildPeople':
				buildHallmarkPeople()
			else:
				hallmark = _.getTable('hallmark.json')

				_.switches.fieldSet('Long','active',True)
				_.switches.fieldSet('Long','value','name')
				_.switches.fieldSet('Sort','active',True)
				_.switches.fieldSet('Sort','value','year')
				_.tables.register('Auto',hallmark,w=1)
				_.tables.print('Auto','year,name')
				_.pr()
				_.pr(len(hallmark))



########################################################################################
######################################################################################## ########################################################################################
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
			_.pr('Reset acquisition data')
			self.acquisition = {
								'fullcredits': {'acquired': 0,'expires': 0,},
								'seasons': {'acquired': 0,'expires': 0,},
								'rating': {'acquired': 0,'expires': 0,},
							}
	def setYear(self,year):
		year = _clean(year)
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
	#   result = True
	#   if not self.isCanceled():


	def dump(self):
		with open(self.objFile(), 'wb') as objSelf:
			pickle.dump(self, objSelf, pickle.HIGHEST_PROTOCOL)

	def objFile(self):
		# print('loaded');sys.exit();
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
		# print('self.isExpired(section)',self.expirationDateDefault); sys.exit();
		done = False
		self.validateFields( section )
		try:
			if self.expirationDateDefault == 'never':
				return False
		except Exception as e:
			pass
		if self.acquisition[section]['acquired'] == 0:
			done = True
			result = True
		if not done:
			dateDiff = _.dateDiff( time.time(), self.defaultExpiration() )

			# _.pr( '\nError: isExpired', time.time(), self.defaultExpiration(), dateDiff )
			# __.xit()
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
			_.pr('Successfully reset expiration ')
		else:
			if not self.inSeason:
				self.acquisition['seasons']['expires'] = str(newStartDate)
				_.pr('Success: set expiration for ', self.acquisition['seasons']['expires'] + ' 14 days before ' + newDate)

	def pathGen( self ):
		# { 'first': first, 'second': second, 'path': p }
		self.name = cleanName( self.name )
		first = ''
		second = ''
		test = False
		if test:
			try:
				fh = franchiseHierarchy( self.imdbID )
			except Exception as e:
				_.pr( 'Error' )
		if test:
			_.pr( fh )
			return True

		fh = franchiseHierarchy( self.imdbID )

		if type( fh ) == bool:
			fh = inFranchiseID( self.name )

		if type( fh ) == int:
			first = fixCase( cleanName( cleanNamePathPrep( __.franchises[fh]['label']) ).title() )
			p = __.movieDrivePath  + first + os.sep  + cleanNamePathPrep( self.year_name() ) + '.mkv'
			fh = { 'first': first, 'second': second, 'path': p }

		elif type( fh ) == bool:
			p = __.movieDrivePath  + 'Single'+os.sep + cleanNamePathPrep( self.name ) + os.sep + cleanNamePathPrep( self.year_name() ) + '.mkv'
			fh = { 'first': first, 'second': second, 'path': p }

		if not test:
			# _.pr( fh )
			fh['label'] = self.year_name()
			fh['year'] = str(self.year)
			fh['name'] = self.name
			fh['path'] = cleanName2( fh['path'] )
			fh['imdbID'] = self.imdbID
			# fh['path'] = ''
			# fh['name2'] = cleanNamePathPrep( self.name )
			# fh['print2'] = cleanNamePathPrep( self.year_name() )
			return fh

	def inFranchiseNew( self, theFranchise ):
		fID = inFranchiseID( theFranchise )
		if not type(fID) == bool:
			return { 'year': self.year, 'name': cleanName(self.name), 'key': self.year_name() }
		return False


	def inFranchise( self, theFranchise ):
		theFranchise = theFranchise.replace( ' ', '_' )
		theFranchise = theFranchise.replace( ',', '_' )

		if not len( __.franchises ):
			__.franchises = _.getTable( 'imdb_franchises.json' )
			__.franchisesName = _.getTable( 'imdb_franchise_display.json' )

		found = False
		for search in __.franchisesName:
			if search['actual'].lower() == theFranchise.lower():
				found = search['proper']

		if not type( found ) == bool:
			franchise = found

		for franchise in __.franchises:
			for key in franchise.keys():
				if not '_date' in key:
					if theFranchise.lower() in key.lower():
						# _.pr( theFranchise.lower(), key.lower() )
						# return True
						if self.imdbID in franchise[key]:
							_.pr( self.year, self.name )
							return True
		return False



	def get_seasons( self, printMinimal ):
		# _.pr('here',printMinimal)
		# __.xit()
		# if not 'seasons' in self.pages:
		# if True:
		# if 'tt4154858' == self.imdbID:
		#   _.pr( '_____________________________________________________________' )
		#   for row in dir(self):
		#       try:
		#           _.printVar( eval( 'self.' + str(row) ) )
		#       except Exception as e:
		#           pass
		#       _.pr( row )
		#   _.pr( '_____________________________________________________________' )

		if self.isExpired('seasons'):
			self.seasonData = []
			self.seasonData = get_cinema_seasons( self.imdbID )
			self.pages.append('seasons')
			self.acquisition['seasons']['acquired'] = float(time.time())
		if not printMinimal:
			_.pr()
		if self.acquisition['seasons']['acquired'] == 0:
			self.acquisition['seasons']['acquired'] = float(time.time())
		self.setYear(self.seasonData[0]['year'])
		if self.name == '':
			self.name = self.seasonData[0]['title']
		if not printMinimal:
			# _.pr(self.seasonData[0]['year'],self.seasonData[0]['title'],'\n\n\tSeasons: ',str(len(self.seasonData[0]['seasons'])))
			# _.printBold(self.seasonData[0]['year']+' '+self.seasonData[0]['title']+' '+'\n\n\tSeasons: '+' '+str(len(self.seasonData[0]['seasons'])))

			self.seasonData[0]['year'] = _clean(self.seasonData[0]['year'])
			# for x in _.tinydic(self.seasonData,skim=None,lan='py',prev=True,dump=None,list0=True):
			#     _.pr(x)
			_.cp(_clean(self.seasonData[0]['year'])+' '+self.seasonData[0]['title']+' '+self.seasonData[0]['id'], 'yellow')
			_.cp( '\n\tSeasons: '+' '+str(len(self.seasonData[0]['seasons'])), 'green' )
			_.pr()
		for i1,season in enumerate(self.seasonData[0]['seasons']):
			for i2,episodes in enumerate(season['episodes']):
				if not printMinimal:
					_.fields.register( 'episodes', 'episode', '\t'+' '+episodes['id']+' '+'\t'+' '+airdateAlignRight(episodes['airdate'])+' '+'\t'+' '+episodes['title'] )

		season_records = []
		for i1,season in enumerate(self.seasonData[0]['seasons']):
			season_printed = False
			for i2,episodes in enumerate(season['episodes']):
				if int(season['season']) < 10:
					seasonXYZ = '0'+str(season['season'])
				else:
					seasonXYZ = str(season['season'])
				season_records.append({ 'season': 'Season: '+seasonXYZ, 'id': episodes['id'], 'date': airdateAlignRight(episodes['airdate']), 'title': episodes['title'], 'imdb': getIdFromUrl(episodes['url']) })
				if not printMinimal:
					printRow = '\t'+' '+episodes['id']+' '+'\t'+' '+airdateAlignRight(episodes['airdate'])+' '+'\t'+' '+episodes['title']
					if _.showLine( printRow ):
						if not season_printed:
							season_printed = True
							if not printMinimal:
								if not _.switches.isActive('EpisodeTable'):
									_.pr()
									_.printBold('Season: ' +' '+ season['season'])


						if not _.switches.isActive('EpisodeTable'):
							if _.switches.isActive('SeasonsSimple'):
								_.pr( printRow )
							else:
								_.colorizeRow( _.fields.value( 'episodes', 'episode', printRow ) )


		if _.switches.isActive('EpisodeTable'):
			_.switches.fieldSet( 'Long', 'active', True )
			_.switches.fieldSet( 'GroupBy', 'active', True )
			_.switches.fieldSet( 'GroupBy', 'value', 'season' )
			_.switches.fieldSet( 'GroupBy', 'values', ['season'] )
			_.tables.register( 'seasons', season_records ,w=1)
			if _.switches.isActive('Column'):
				_.tables.print( 'seasons', _.switches.value('Column') )
			else:
				_.tables.print( 'seasons', 'season,id,date,imdb,title' )
			# _.tables.fieldProfileSet( 'seasons', 'season', 'alignment', 'center' )

			# _.tables.r_.pr( season_records, 'season,id,date,title' )
		_.cp( [ '\n', len(season_records), 'episodes' ], 'yellow' )
		showLen = ''
		if _.switches.isActive('EpisodeLength'):
			mins = int( _.switches.values('EpisodeLength')[0] )
			_.cp( [ ' ',
								_.addComma((mins*len(season_records))/60) + ' hrs'
			], 'red' )
			if _.switches.isActive('OnEpisode'):
				on = _.switches.values('OnEpisode')[0]
				i=0
				w=0
				started = False
				for rec in season_records:
					if rec['id'] == on:
						started = True
					if started:
						i+=1
					else:
						w+=1
				_.cp( [ '  ',
								str(round((mins*w)/60,2)) + ' hrs watched, ending on '+ on
				], 'yellow' )
				_.cp( [ '  ',
								str(round((mins*i)/60,2)) + ' hrs left, starting on '+ on
				], 'green' )




		if printMinimal:
			self.showInSeason( printMinimal, shouldPrint=False )
		else:
			self.showInSeason( printMinimal, shouldPrint=True )
		return False
	def showInSeason( self, printMinimal=False, shouldPrint=True ):
		if self.isExpired('seasons'):
		# if not 'seasons' in self.pages:
		# if True:
			# _.pr('Looking stuff up')
			self.seasonData = []
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
					dateDiff = _.dateDiffX(lastDate,testDate,'-')
					# _.pr( 'dateDiff:', dateDiff )
					# __.xit()
				except Exception as e:
					dateDiff = 0
				# _.pr(dateDiff,lastDate,testDate)
				# _.pr(dateDiff)
				if dateDiff > 100:
					diffList.append(dateDiff)
				if len(testDate) == 10:
					lastDate = testDate
		# _.pr( len( self.seasonData ) )
		# _.pr( _.printVar(self.seasonData) )
		# __.xit()
		if shouldPrint:
			_.pr()
			_.pr()
			if self.isCanceled():
				_.printBold('isCanceled:'+' '+str(self.isCanceled()),'red')
			else:
				_.printBold('isCanceled:'+' '+str(self.isCanceled()),'green')
		if self.isCanceled():
			# self.expirationDateDefault = 'never'
			ldEpoch = float(_.date2epoch(lastDate,'-'))
			if ldEpoch > time.time():
				_.printBold('show is in season')
			if printMinimal:
				_.printBold('inSeason: '+ ' CNL  ' +' '+ self.name, 'red')
		if not self.isCanceled():
			# _.pr('End of season:',lastDate)
			ldEpoch = float(_.date2epoch(lastDate,'-'))
			if ldEpoch > time.time():
				self.inSeason = True
				expirationDays = 7
				expirationDate = str(_.dateAdd(_.float2Date3B(self.acquisition['seasons']['acquired'],False),'-',expirationDays))
				tillExpire = _.dateDiff(_.float2Date3B(time.time(),False),expirationDate,'-')
				# expirationDate = '2019-01-02'
				if shouldPrint:
					_.printBold('show is in season')
					_.pr('expirationDate:'+' '+expirationDate,'')
					_.pr('tillExpire:'+' '+str(tillExpire),'')
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
					_.printBold('show is not in season')
					_.pr('expirationDate: '+expirationDate,'')
					_.pr('tillExpire: '+str(tillExpire),'')
			self.acquisition['seasons']['expires'] = expirationDate
			self.expirationDateDefault = _.dateDiff( time.time(), expirationDate )
			if printMinimal:
				_.printBold('inSeason: '+ str(self.inSeason) +' '+ self.name)
			else:
				_.printBold( 'self.expirationDateDefault: '+str(self.expirationDateDefault) )
			# __.xit()
			# _.pr('isExpired:',self.isExpired('seasons'))
			result = {'inSeason': self.inSeason, 'lastDate': lastDate , 'expiration':  expirationDate}
			# _.pr(result)
			return result
			# try:
			#   _.pr(lastDate)
			#   ldEpoch = float(_.date2epoch(theDate,delim))
			#   now = float(time.time())
			#   if ldEpoch > now:
			#       self.inSeason = True
			#       _.pr('show is in season')
			#   else:
			#       _.pr('show is not in season')
			#       self.inSeason = False
			# except Exception as e:
			#   _.pr('Error on lastDate:',lastDate)
	def year_name( self ):
		addYear = True
		if type(self.year) == int:
			if self.year == 0:
				addYear = False
		elif not len(self.year):
			addYear = False
		if addYear:
			year = str(self.year)
			# year = year.replace( '-', '' )
			year = year.replace( ' ', '' )
			result = year + ' ' + cleanName(self.name)
		else:
			result = self.name
		return result
	def roger_ebert( self ):
		# _.pr( 'HERE' )
		url = 'https://www.google.com/search?q=site%3Arogerebert.com+' + self.year_name()
		newURL = _str.replaceAll(_str.replaceAll(url,',','+'),' ','+')

		# _.pr(  )
		# _.pr( '_______________' )
		# _.pr(  )
		# _.pr( newURL )
		print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')
		page = requests.get( newURL )
		tree = html.fromstring(page.content)
		film = tree.cssselect('a')
		for row in film:
			found = 0
			for test in self.year_name().split( ' ' ):
				data = cleanupString(row.text_content())
				if test in data:
					if found > 1:
						# _.pr()
						# _.pr( data )
						# _.pr( row.attrib['href'] )
						print_url(frameinfo=getframeinfo(currentframe()), url=url,c='cyan')
						page2 = requests.get( row.attrib['href'] )
						tree2 = html.fromstring(page2.content)
						_.pr( page2.content )
						__.xit()
						try:
							full = tree2.cssselect('.icon-star-full')
						except Exception as e:
							full = []
						try:
							half = tree2.cssselect('.icon-star-half')
						except Exception as e:
							half = []
						stars = len( full )
						if len( half ):
							stars += .5
						_.pr( stars, self.year_name() )
						return False
						__.xit()
					found += 1

		# _.pr( page.content )
		# __.xit()

		# _.pr( data )

	def get_ratings( self, printThis=True, imdb=False ):


		if not imdb:
			self.roger_ebert()


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
					_.pr(self.rating, cleanupString(_str.onlyDigits(self.rating_data['year'])),self.rating_data['show']+': ',self.rating_data['name'])
			else:
				if printThis:
					_.pr(self.rating, cleanupString(_str.onlyDigits(self.rating_data['year'])),self.rating_data['name'])
		except Exception as e:
			if printThis:
				_.pr(self.rating, cleanupString(_str.onlyDigits(self.rating_data['year'])),self.rating_data['name'])
		self.setYear( self.rating_data['year'] )
		# self.year =
		self.name = self.rating_data['name']

	def get_fullcredits(self):
		shouldRun = False
		# _.pr(self.acquisition['fullcredits']['acquired'])
		# __.xit()

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



		if _.switches.isActive( 'ForceFranchise', theFocus='__imdb__' ):
			franchiseName = self.fullcredits['name']
			fi = inFranchiseID( franchiseName )
			if not type(fi) == bool:
				__.franchises.pop( fi )
			people = []
			for person in self.fullcredits['people']:
				people.append( person['imdbID'] )

			aliase = aliases(franchiseName)
			record = {
						'date_acquired': time.time(),
						'epoch': time.time(),
						'date': _.resolveEpochTest( time.time() ).split( ' ' )[0],
						'label': franchiseName,
						'aliases': aliase,
						'parts': parts(aliase),
						'movieIDS': __.episodeIDs,
						'peopleIDS': people,
						'movies': [],
						'list': []
			}

			__.franchises.append( record )
			_.saveTable( __.franchises, 'imdb_franchises_NEW.json' )

			# _.printVar( self.fullcredits )


		# os.system('cls')

	def print_fullcredits(self):
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')
		_.pr()
		_.pr(self.fullcredits['year'],self.name)
		_.pr()
		_.pr()

		_.tables.register('Auto',self.fullcredits['people'],w=1)
		_.tables.fieldProfileSet( 'Auto', 'character', 'trigger', _.longDashAdd )
		_.tables.print('Auto','id,name,character')
		if not _.switches.isActive( 'Single' ):
			movieMakeSelection( self.fullcredits )

	def trigger(self,script):
		self.script_trigger = script

	def changeStatus(self,newStatus):
		self.active = newStatus



def aliases( data ):
	results = []
	results.append( data )
	add = ''
	# if _.switches.isActive('Franchise'):
	#     add = ''
	# else:
	#     add = input( 'Aliases for '+data+' (,): ' )
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

		# _.pr('location:',location)
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
		# _.pr('watched:',watched)
		return watched



	def addChild(self, imdbID):

		if not imdbID in self.childItemList:
			takeAction = True
			if not _.switches.isActive('ObjectsLoadSkip'):
				if os.path.isfile(self.objFile(imdbID)):
					objData = loadObject(self.objFile(imdbID))
					if not objData.imdbID == imdbID or objData.name == '' or 'sample' in objData.name.lower():
						takeAction = True
						objData is None


					if not objData is None:
						try:
							if 'sample' in objData.rating_data['name'].lower():
								takeAction = True
								objData is None
						except Exception as e:
							pass



					if not objData is None:
						# _.pr( imdbID, self.objFile(imdbID) )
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
	def rating(self, imdbID, imdb=False):
		# _.pr(imdbID)
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			_.pr('Error: childRow')
			__.xit()
		if not self.shouldSkip( self.childItemRows[self.thisRow] ):
			self.childItemRows[self.thisRow].imdbID = imdbID
			self.childItemRows[self.thisRow].get_ratings(imdb=False)

		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
		elif _.switches.value('ObjectsLoadSkip') == 'save':
			self.childItemRows[self.thisRow].dump()
			# self.dump()
	def shouldSkip( self, objData ):
		try:
			if 'sample' in objData.name.lower():
				return True
		except Exception as e:
			pass
		try:
			if 'sample' in objData.rating_data['name'].lower():
				return True
		except Exception as e:
			pass
		return False
	def printLabel( self, imdbID, data=False, franchise=False ):
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			_.pr('Error: childRow')
			__.xit()
		self.childItemRows[self.thisRow].imdbID = imdbID
		self.childItemRows[self.thisRow].get_ratings(imdb=False,printThis=False)

		if type( data ) == bool:
			if franchise:
				_.pr( self.inFranchise( imdbID )+'\t'+self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name )
			else:
				_.pr( self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name )
		else:
			# _.pr( self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name+',', data['folder']+',', data['file'] )
			if franchise:
				_.pr( self.inFranchise( imdbID )+__.theDelim+self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name+__.theDelim+data['folder']+__.theDelim+data['file']+__.theDelim+str(data['mod'])+__.theDelim+str(data['bytes'])+__.theDelim+_.formatSize(data['bytes'])+__.theDelim+imdbID )
			else:
				_.pr( self.childItemRows[self.thisRow].year, self.childItemRows[self.thisRow].name+__.theDelim+data['folder']+__.theDelim+data['file']+__.theDelim+str(data['mod'])+__.theDelim+str(data['bytes']) )


	def franchiseProper( self, name ):
		if type( self.franchiseDataFix ) == bool:
			self.franchiseDataFix = _.getTable('imdb_franchise_display.json')

		for fdp in self.franchiseDataFix:
			if name == fdp['actual']:
				return fdp['proper']

		return name.replace( '_', ' ' ).title()

	def inFranchise( self, imdbID ):
		if type( self.franchiseData ) == bool:
			# backupJSON( 'imdb_franchises.json' )
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
					# _.pr( self.franchiseProper( k ) )
			if len( franchiseList ):
				for f in franchiseList:
					if imdbID in self.franchiseData[0][f]:
						return self.franchiseProper( f )


			# _.pr( k )

		# _.saveTable( franchiseList,'imdb_franchise_display.json' )
		# __.xit()
		return ''

	def pathGen( self, imdbID ):
		self.addChild(imdbID)
		self.childRow(imdbID)
		# _.pr(imdbID)
		if type(self.thisRow) == float:
			_.pr('Error: childRow')
			__.xit()
		if not self.childItemRows[self.thisRow].imdbID:
			_.pr( 'Error: imdbID')
			__.xit()
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
		elif _.switches.value('ObjectsLoadSkip') == 'save':
			self.childItemRows[self.thisRow].dump()

		return self.childItemRows[self.thisRow].pathGen()

	def inFranchiseNew(self, imdbID, franchise ):
		self.addChild(imdbID)
		self.childRow(imdbID)
		# _.pr(imdbID)
		if type(self.thisRow) == float:
			_.pr('Error: childRow')
			__.xit()
		if not self.childItemRows[self.thisRow].imdbID:
			_.pr( 'Error: seasons')
			__.xit()
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
		elif _.switches.value('ObjectsLoadSkip') == 'save':
			self.childItemRows[self.thisRow].dump()

		return self.childItemRows[self.thisRow].inFranchiseNew(franchise)
			# self.dump()



	def seasons(self, imdbID, printMinimal=False):
		# return False
		self.addChild(imdbID)
		self.childRow(imdbID)
		# _.pr(imdbID)
		if type(self.thisRow) == float:
			_.pr('Error: childRow')
			__.xit()

		# _.pr( 'self.thisRow:', self.thisRow )

		if not self.childItemRows[self.thisRow].imdbID:
			_.pr( 'Error: seasons')
			__.xit()

		self.childItemRows[self.thisRow].get_seasons(printMinimal)


		focus()
		if _.switches.isActive( 'ForceFranchise' ):
			__.episodeIDs = []
			for seasons in self.childItemRows[self.thisRow].seasonData[0]['seasons']:
				for episodes in seasons['episodes']:
					try:
						__.episodeIDs.append( getIdFromUrl( episodes['url'] ) )
					except Exception as e:
						pass
			self.childItemRows[self.thisRow].get_fullcredits()


		# _.pr( 'the show:', self.childItemRows[self.thisRow].seasonData[0]['title'] )

			# _.printVar( self.childItemRows[self.thisRow].seasonData )



		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
		elif _.switches.value('ObjectsLoadSkip') == 'save':
			self.childItemRows[self.thisRow].dump()
			# self.dump()

	def seasonsStarts(self, imdbID, theDate, theFormat = 'ymd'):

		if theDate == '':
			theDate = '0'
		if theDate == '0':
			startDate = 0
		else:
			try:
				startDate = _.figureOutDate(str(theDate), theFormat)
			except Exception as e:
				_.pr( 'Error:' ,theDate )
				__.xit()

		# _.pr(startDate)
		# _.pr(newStartDate)
		# __.xit()
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			_.pr('Error: childRow')
			__.xit()

		self.childItemRows[self.thisRow].seasonStartsDate(startDate)
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
		elif _.switches.value('ObjectsLoadSkip') == 'save':
			self.childItemRows[self.thisRow].dump()
			# self.dump()


	def inSeason(self, imdbID):
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			_.pr('Error: childRow')
			__.xit()

		self.childItemRows[self.thisRow].showInSeason(True)
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
		elif _.switches.value('ObjectsLoadSkip') == 'save':
			self.childItemRows[self.thisRow].dump()
			# self.dump()

	def register(self, imdbID, shouldPrint):
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			_.pr('Error: childRow')
			__.xit()

		self.childItemRows[self.thisRow].get_fullcredits()
		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
		elif _.switches.value('ObjectsLoadSkip') == 'save':
			self.childItemRows[self.thisRow].dump()
			# self.dump()
		if shouldPrint or _.switches.isActive('Print'):
			self.childItemRows[self.thisRow].print_fullcredits()
	def print(self):
		childItems = []
		for ci in self.childItemRows:
			childItems.append({'name':ci.name})
		_.tables.register('childClassItems',childItems,w=1)
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
		_.tables.register('childClassItems',childItems,w=1)
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

		self.location = ''
		self.date = ''
		self.year = 0
		self.age = 0

		self.pages = []

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

	def defaultExpiration( self ):
		return 30

	def acquisitionDataReset(self):
		try:
			self.acquisition['seasons']['acquired']
		except Exception as e:
			_.pr('Reset acquisition data')
			self.acquisition = {
								'fullcredits': {'acquired': 0,'expires': 0,}
							}
	def validateFields( self, section='seasons' ):


		try:
			self.acquisition[section]['acquired']
			self.acquisition[section]['expires']
		except Exception as e:
			self.acquisitionDataReset()

	def isExpired( self, section ):
		done = False
		self.validateFields( section )
		try:
			if self.expirationDateDefault == 'never':
				return False
		except Exception as e:
			pass
		if self.acquisition[section]['acquired'] == 0:
			done = True
			result = True
		if not done:
			dateDiff = _.dateDiff( time.time(), self.defaultExpiration() )

			# _.pr( '\nError: isExpired', time.time(), self.defaultExpiration(), dateDiff )
			# __.xit()
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

	def get_fullcredits( self ):
		_.pr( 'HERE:', 1 )
		shouldRun = False
		# _.pr(self.acquisition['fullcredits']['acquired'])
		# __.xit()

		if self.isExpired('fullcredits'):
			shouldRun = True

		if self.acquisition['fullcredits']['acquired'] < __.imdbAppearancesCaptured:
			shouldRun = True


		if shouldRun:
			_.pr( 'HERE:', 2 )
			self.fullcredits = get_people_fullcredits(self.imdbID)
			# _.printVar( self.fullcredits )
			# {'name': theTitle, 'year': theYear, 'people': people}
			self.pages.append('fullcredits')
			self.acquisition['fullcredits']['acquired'] = time.time()
			self.acquisition['fullcredits']['expires'] = self.defaultExpiration()

			self.setYear(self.fullcredits['year'])

			if self.name == '':
				self.name = self.fullcredits['name']

			if self.date == '':
				self.date = self.fullcredits['date']

			if self.location == '':
				self.location = self.fullcredits['location']
		_.pr( 'HERE:', 3 )

# { 'name': x, 'date': x, 'year': x, 'location': x, 'link': x, 'movies': movies }

	def setYear( self, year=False ):
		year = _clean(year)
		self.age = 0
		if not type(year) == bool:
			try:
				self.year = int(year)
			except Exception as e:
				self.year = 0


		# if self.year:
		#   data = _.resolveEpochTest( time.time() )
		#   thisYear = int(data.split( '-' )[0])
		#   self.age = thisYear - self.year
		#   _.pr( 'age:', self.age )


	def print_fullcredits( self ):
		_.pr( 'HERE:', 100 )
		# __.xit()
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')
		_.pr()
		_.pr(self.fullcredits['year'],self.name)
		_.pr()
		_.pr()

		_.tables.register('Auto',self.fullcredits['movies'],w=1)
		_.tables.print('Auto','id,age,name')
		if not _.switches.isActive( 'Single' ):
			personMakeSelection( self.fullcredits )

# {'id': iiii, 'name': title, 'year': year, 'link': link, 'img': img, 'age': gigAge}



class ThePeople:

	def __init__(self):


		self.childItemRows = []
		self.childItemList = []


	def register( self, imdbID, shouldPrint=False ):
		_.pr( 'HERE:', 0 )
		self.addChild(imdbID)
		self.childRow(imdbID)
		if type(self.thisRow) == float:
			_.pr('Error: childRow')
			__.xit()

		self.childItemRows[self.thisRow].get_fullcredits()

		_.pr( 'HERE:', 4 )

		if not _.switches.isActive('ObjectsLoadSkip'):
			self.childItemRows[self.thisRow].dump()
		elif _.switches.value('ObjectsLoadSkip') == 'save':
			self.childItemRows[self.thisRow].dump()

		if shouldPrint or _.switches.isActive('Print'):
			self.childItemRows[self.thisRow].print_fullcredits()

	def dump(self):
		with open(__.objectLocation['cinema'], 'wb') as objCinema:
			pickle.dump(self, objCinema, pickle.HIGHEST_PROTOCOL)

	def objFile(self, imdbID):
		return __.objectLocation['objects'].replace(__.ID_HERE,imdbID)


	def childRow( self, imdbID ):
		self.thisRow = 0.01
		for i,row in enumerate(self.childItemRows):
			if self.childItemRows[i].imdbID == imdbID:
				self.thisRow = i

	def addChild( self, imdbID ):

		if not imdbID in self.childItemList:
			takeAction = True
			if not _.switches.isActive('ObjectsLoadSkip'):
				objData = None
				if os.path.isfile(self.objFile(imdbID)):
					objData = loadObject(self.objFile(imdbID))
					if not objData.imdbID == imdbID or objData.name == '' or 'sample' in objData.name.lower():
						takeAction = True
						objData is None

					if not objData is None:
						objID = len(self.childItemRows)
						self.childItemRows.append(objData)

						takeAction = False


			if takeAction:
				self.childItemRows.append(ThePerson(imdbID))

			self.childItemList.append(imdbID)

	def print(self):
		childItems = []
		for ci in self.childItemRows:
			childItems.append({'name':ci.name})
		_.tables.register('childClassItems',childItems,w=1)
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
		_.tables.register('childClassItems',childItems,w=1)
		_.tables.print('childClassItems','name,active,value')
	def status(self,name,newStatus):
		for i,ci in enumerate(self.childItemRows):
			if ci.name == name:
				self.childItemRows[i].changeStatus(newStatus)



########################################################################################
######################################################################################## ########################################################################################
# NEW FUNC

def get_people_fullcredits(imdbID):
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

	# _.pr(birthDate)
	# _.pr(birthYear)
	# _.pr(birthLocation)
	img0 = tree.cssselect('img')
	img = ''
	for img1 in img0:
		img2 = img1.attrib['src']
		if '317_AL_.jpg' in img2:
			img = img2
	for pn in personName:
		theirName0 = cleanupString(pn.text_content())
		if len(theirName0) > 0:
			theirName = cleanName(theirName0)
			_.pr('Processing', theirName,'...')
	# pause = input('pause')

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
						# _.pr(e)
						# __.xit()
						gigAge = ''
					if j == 1:
						movies.append( {'id': iiii, 'name': cleanName(title), 'year': year, 'thisID': thisID, 'img': img, 'age': gigAge} )
						iiii += 1
				ii += 1
			iii += 1
		i += 1

	return { 'name': theirName, 'date': birthDate, 'year': birthYear, 'location': birthLocation, 'link': url, 'movies': movies }

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
	#   _.pr(cleanupString(ty.text_content(),False))
	theTitle = cleanName(theTitle)
	_.pr('Processing', theYear, theTitle, '...')
	theYearThis = theYear
	theTitleThis = theTitle
	img0 = tree.cssselect('img')
	img = ''
	for img1 in img0:
		img2 = img1.attrib['src']
		if '268_AL_.jpg' in img2:
			img = img2


	cast = tree.cssselect('.cast_list')
	tr = cast[0].cssselect('tr')
	people = []
	ip = 0


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
			record = { 'id': ip, 'imdbID': personID, 'name': person, 'link': link, 'character': character }
			# _.pr( record )
			people.append( record )
			ip += 1



	return {'name': theTitle, 'year': theYear, 'link': url, 'people': people}

def get_cinema_ratings(imdbID):
	url = __.links['imdb']['cinema']['ratings'].replace(__.ID_HERE,imdbID)
	# print_url(frameinfo=getframeinfo(currentframe()), url=url)
	# __.xit()
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
	#   name = nameShow + ': ' + name
	# _.pr(len(nameStuff))
	# nameX = nameStuff[0].text_content()
	# nameY = cleanupString(nameX,False)
	# _.pr(nameY)
	# year0 = nameStuff[0].cssselect('span')
	# year = cleanupString(year0[0].text_content())
	# _.pr('year: ',year)
	# year = year1.replace('(','').replace(')','')
	try:
		year0 = nameStuff[0].cssselect('.nobr')
		year1 = cleanupStringYear(year0[0].text_content())
		# _.pr('year: ',year)
		year = year1.replace('(','').replace(')','')
	except Exception as e:
		year = ''
	if year == '':
		try:
			year0 = nameStuff[0].cssselect('.nobr')
			year1 = cleanupString(year0[0].text_content(),False)
			# _.pr('year: ',year)
			year = year1.replace('(','').replace(')','')
		except Exception as e:
			year = ''
	year = cleanupString(year)
	# _.pr({'imdbID': imdbID, 'rating': rating, 'name': name, 'year': year})
	# if not len(year) > 0:
	#   __.xit()
	return {'rating': rating, 'show': nameShow, 'name': name, 'year': year}



def get_cinema_seasons(imdbID):
	# _.pr(imdbID)
	# __.xit()
	seasonData = []
	theTitle=''
	theYear=''

	url = __.links['imdb']['cinema']['fullcredits'].replace(__.ID_HERE,imdbID)

	if theTitle == '':
		# print(url);sys.exit();
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
	theTitle = cleanName(theTitle)
	isCached = False
	now = datetime.datetime.now()
	today = now.strftime("%Y-%m-%d")

	newURL = __.links['imdb']['cinema']['season'].replace(__.ID_HERE,imdbID)
	siteBase = 'https://www.imdb.com'
	thisURL = newURL.replace('THESEASON','1')
	# print(thisURL);sys.exit();
	try:
		page = requests.get(thisURL)
		tree = html.fromstring(page.content)
		seasons = tree.cssselect('#bySeason option')
		try:
			seasonTest0 = seasons[len(seasons)-1].text_content()
		except: _.e('Nothing Found','No Episode Information Available')
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
	except Exception as e:
		pass

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
						'people': _v.myTables + os.sep+'imdb_people.objects',
						'cinema': _v.myTables + os.sep+'imdb_cinema.objects',
						'objects': _v.myTables + os.sep+'imdb'+os.sep+'imdb_obj_' + __.ID_HERE + '.objects'
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
	if not type(theAliasID(label,pm,idType)) == bool:
		label = cleanAlias(label)
		__.aliases.append({'label': label, 'pm': pm, idType: imdbID})
		# _.pr(__.aliases)
		_.saveTable(__.aliases,'imdb_aliases.json',printThis=False)


def theAliasID(label,pm,idType):
	# theAliasID(searchFor,personMovie,'imdbID')
	result = False
	if len(idType) == 0:
		idType = 'imdbID'
	if len(__.aliases) > 0:
		label = cleanAlias(label)
		for alias in __.aliases:
			if alias['label'].lower() == label.lower() and alias['pm'] == pm and len(alias[idType]) > 0:
				result = alias[idType]
	return result



def caseTest():
	# _.pr('test')
	# __.xit()
	__.cinema = TheCinema()
	__.people = ThePeople()

	# if _.switches.isActive('ObjectsLoadSkip'):
	#   __.cinema = TheCinema()
	#   __.people = ThePeople()
	# else:
	#   try:
	#       with open(__.objectLocation['cinema'], 'rb') as objCinema:
	#           __.cinema = pickle.load(objCinema)
	#   except Exception as e:
	#       __.cinema = TheCinema()
	#   try:
	#       with open(__.objectLocation['people'], 'rb') as objPeople:
	#           __.people = pickle.load(objPeople)
	#   except Exception as e:
	#       __.people = ThePeople()
		# _.pr('loaded')
		# test = input('pause')
	# _.pr(_.get_size(__.cinema))
	# __.xit()
	# _.pr(type(__.pipeData))
	# focus()
	# _.pr( 'MovieFranchise:', _.switches.value('MovieFranchise') )
	# __.xit()
	__.pipeData = _.appData[__.appReg]['pipe']

	# _.pr(__.appReg)
	# _.printVar( _.appData )
	# _.pr(__.appReg)
	# _.pr(__.appReg,_.appData)
	if type(__.pipeData) == list:
		if _.switches.isActive('Movie'):
			if _.switches.isActive('Score') or _.switches.isActive('Label') or _.switches.isActive('Episode') or _.switches.isActive('MovieFranchise') or _.switches.isActive('PrintPath'):
				# _.pr( __.pipeData )


				# _.pr( 'HERE' )

				if _.switches.isActive('PrintPath') or ( _.switches.isActive('MovieFranchise') and (  'all' in _.switches.value('MovieFranchise') or 'id' in _.switches.value('MovieFranchise')  ) ):
					# _.pr( 'HERE' )
					# __.xit()


					__.results = []

					for pData in __.pipeData:
						imdbID = googleID(pData['label'],'movie')
						if len( imdbID ) > 0:
							try:
								r = __.cinema.pathGen( imdbID )
								if type( r ) == dict:
									# _.pr( pData['data']['path'] )
									r['data'] = pData['data']
									__.results.append( r )
							except Exception as e:
								pass
					pass
					# newData = _.tables.returnSorted( 'Path', 'd:xfirst,d.xsecond,d.year', data )
					if 'all' in _.switches.value('MovieFranchise') or 'id' in _.switches.value('MovieFranchise'):
						printFranchiseTable( __.results )




						# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



					else:
						for i,row in enumerate( franchiseYear( printData ) ):
							# _.pr( row )
							_.pr( row['year'], row['path'] )
							# _.pr( row['path'] )
						# __.xit()


					return __.results

				elif _.switches.isActive('MovieFranchise'):
					try:
						_.switches.fieldGet( 'MovieFranchise', 'dir' )
						isDir = True
					except Exception as e:
						isDir = False

					if isDir:
						__.results = []
						for pData in __.pipeData:
							imdbID = googleID(pData,'movie')
							if len( imdbID ) > 0:
								try:
									r = __.cinema.inFranchiseNew( imdbID, _.switches.value('MovieFranchise') )
									if type( r ) == dict:
										__.results.append( r )
									pass
								except Exception as e:
									pass
						# __.results

						newResults = []
						spent = []
						for row in __.results:
							if not row['key'] in spent:
								spent.append( row['key'] )
								newResults.append( row )

						__.results = _.tables.returnSorted( 'MovieFranchise', 'a.year', newResults )
						x = len( __.results )
						for i,row in enumerate(__.results):
							if _.switches.isActive( 'PrintPath' ):
								_.pr( row['path'] )
							else:
								_.pr( row['year'], row['name'] )
							# _.pr( row['path'], row['year'], row['name'] )
						_.pr()
						_.pr(x)




				elif _.switches.isActive('Episode'):
					for pData in __.pipeData:
						# _.pr()
						# _.pr( pData, googleID(pData,'movie') )
						try:
							imdbID = googleID(pData,'movie')
							if len( imdbID ) > 0:
								try:
									if not imdbID in __.noSeasonData:
										# _.pr()
										# _.pr( 'imdbID:', imdbID )
										# __.xit()
										__.cinema.seasons( imdbID, printMinimal=True)
									else:
										_.pr( 'Error: InSeason', pData )
								except Exception as e:
									__.noSeasonData.append( imdbID )
									_.saveTable( __.noSeasonData, 'imdb_no_season_data.json', printThis=False)
									# last item should be:  tt0426347
									_.pr( 'Error: InSeason', pData )
						except Exception as e:
							_.pr( 'Error: googleID', pData )

				else:



					for pData in __.pipeData:
						if _.switches.isActive('MovieFile'):
							# _.pr(pData)
							theLabel = pData['title']
						else:
							theLabel = pData

						if not theLabel in __.omitFromMovies:
							# _.pr('   -   ',theLabel)
							imdbID = googleID(theLabel,'movie')
							if len( imdbID ) > 0:
								# _.pr( theLabel, imdbID )
								if _.switches.isActive('Label'):
									if _.switches.isActive('MovieFile'):
										__.cinema.printLabel( imdbID, pData, franchise=True )
									else:
										__.cinema.printLabel( imdbID )
								else:
									try:
										__.cinema.rating( imdbID )
									except Exception as e:
										pass
						try:
							pass
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
			_.pr('Google Error')
			__.xit()
		if _.switches.isActive('Episode'):
			__.cinema.seasons(imdbID)
			# __.cinema.inSeason(imdbID)
		elif _.switches.isActive('SeasonStarts'):
			ssv = _.switches.value('SeasonStarts')
			# _.pr(ssv)
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
	url =   urlBase.replace( '*b*', b )
	url =       url.replace( '*c*', c )
	url =       url.replace( '*d*', d )
	url =       url.replace( '*e*', e )
	url =       url.replace( '*g*', g )
	return url
	# toggleSeeMoreEpisodes(this,'nm1050978','tt0118480','actor','ttfc_fc_cl_i892',0,0,'#episodes-tt0118480-nm1050978-actor', toggleSpan); return false;



###################################################################### ######################################################################
def personMakeSelection( data ):
	_.pr()
	_.pr( 'personMakeSelection' )
	selectedSomething = False
	selection = input('Make Selection - ')
	selection = selection.lower()
	if len(selection) == 0:
		selection = 'x'
	if selection == 'h' or selection == '?' or selection == 'help':
		_.pr('id')
		_.pr('(b)io')
		_.pr('(s)earch')
		_.pr('l','url')
		_.pr('e(x)it')
		_.pr('description contains (dc)')
		_.pr('show all descriptions (sd)')
		_.pr('(f)ranchise')
		_.pr('search results (sr)')
		_.pr('dump')
	if selection == 'dump':
		_.printVar( data )
	if selection == 'sr':
		_.pr()
		sr = input('Search for - ')
		searchResults = []
		for m in data['movies']:
			if sr.lower() in m['name'].lower():
				searchResults.append(m)
		_.pr()
		_.tables.register('searchResults',searchResults,w=1)
		_.tables.fieldProfileSet( 'searchResults', 'name', 'trigger', _.longDashAdd )
		_.tables.print('searchResults','id,year,name')
	if selection == 'f':
		_.pr()
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
		load_franchise_table( franchise )
		fID = inFranchiseID( franchise )
		if type(fID) == bool:
			_.pr( 'No Franchise Data' )
			_.pr()
			_.pr( 'Run:' )
			_.pr( '\tp franchise -f', franchise )
			__.xit()

		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')
		_.pr()
		_.pr(data['name'], '\t', data['age'])
		_.pr()




		for ix,r in enumerate(data['movies']):
			# record = {'id': iiii, 'name': title, 'year': year, 'link': link, 'img': img, 'age': gigAge}
			if getIdFromUrl(r['link']) in __.franchises[fID]['movieIDS']:
				data['movies'][ix][franchise] = 'x'
			else:
				data['movies'][ix][franchise] = ''
		_.tables.register('Auto',data['movies'],w=1)
		_.tables.fieldProfileSet( 'Auto', 'name', 'trigger', _.longDashAdd )
		_.tables.print('Auto','id,year,age,'+franchise+',name')
		_.pr()
		_.pr()
		io = 0

		for ix,r in enumerate(data['movies']):
			if getIdFromUrl(r['link']) in __.franchises[fID]['movieIDS']:
				io += 1
				_.pr( r['id'],'\n', r['year'],r['name'])
		_.pr()
		if io > 0:
			_.pr(io)

		if io == 0:
			pass

		now = datetime.datetime.now()
		today = now.strftime("%Y-%m-%d")

		fdtl = __.franchises[fID]['date'].split('-')
		foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
		td = str(today).split('-')
		tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
		diff = tdd - foundDate


		try:
			ppl = _.addComma( len(set(__.franchises[fID]['peopleIDS'])) ) + ' people\t\t'
		except Exception as e:
			ppl = ''
		try:
			mv = _.addComma( len(set(__.franchises[fID]['movieIDS'])) ) + ' movies\t\t'
		except Exception as e:
			mv = ''
		_.pr('_____________________________________________________________________________________________________________________')
		_.pr( franchise.upper(), ppl, mv, __.franchises[fID]['date'], '\t\t', str(diff.days), 'days' )
		_.pr()
		_.pr()

	##################################                        ##################################
	if selection == 'sd':
		i = 0
		for m in data['movies']:
			i += 1
			status = str(i) + ' of ' +  str(len(data['movies']))
			_.updateLine(status)
			try:
				tempXX = m['description']
				hasDescription = True
			except KeyError:
				hasDescription = False
			if hasDescription:
				description = m['description']
			else:
				newURL = 'http://www.imdb.com/title/' + getIdFromUrl(data['link']) + '/?ref_=ttfc_fc_tt'
				# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
				page = requests.get(newURL)
				tree = html.fromstring(page.content)
				description0 = tree.cssselect('.summary_text')
				description1 = description0[0].text_content()
				description = cleanupString(description1)
				data['movies'][i-1]['description'] = description
			_.updateLine('')
		_.pr('')
		for m in data['movies']:
			if len(m['year']) > 1:
				theTitle = str(m['id']) + '\t' + m['name'] + ' (' + m['year'] + ')'
			else:
				theTitle = str(m['id']) + '\t' + m['name']
			_.pr('_______________________________________________')
			_.pr('')
			_.pr(theTitle)
			_.pr(m['description'])



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
		for m in data['movies']:
			i += 1
			status = str(i) + ' of ' +  str(len(data['movies']))
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
				newURL = 'http://www.imdb.com/title/' + getIdFromUrl(data['link']) + '/?ref_=ttfc_fc_tt'
				# print_url(frameinfo=getframeinfo(currentframe()), url=newURL)
				page = requests.get(newURL)
				tree = html.fromstring(page.content)
				description0 = tree.cssselect('.summary_text')
				description1 = description0[0].text_content()
				description = cleanupString(description1)
				data['movies'][i-1]['description'] = description
				description = description.replace('at this time','')
				# _.pr("",lookFor,description.lower())
				if not allDC:
				# _.pr(allDC)
				# __.xit()
					if lookFor in description.lower():
						_.updateLine("")
						_.pr()
						_.pr()
						_.pr(m['name'])
						done = True
						break
						__.xit()

				# __.xit()
			if done:
				__.xit()
			if lfOr and lfAnd:
				_.pr('')
				_.pr('')
				_.pr('Error: and or, pick one')
				__.xit()
			if not lfOr and  not lfAnd:
				if lookFor in description:
					# _.pr('single')
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
		_.pr('')
		if len(dcResult) == 0 and not done:
			_.pr('Nothing Found')
		else:
			_.pr('')
			dci = 0
			for d in dcResult:
				# _.pr(dci, '\t', d)
				_.pr(d)
				dci += 1
			_.pr('')
		if not done:
			_.pr('')
			_.pr(len(dcResult))
			_.pr('')
		dcResult = []
	if selection == 'bio' or selection == 'b':
		newURL = extractUrl(data['link']) + 'bio?ref_=nm_ov_bio_sm'
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		bio0 = tree.cssselect('.soda p')
		bio1 = bio0[0].text_content()
		bio = cleanupString(bio1)
		_.pr(bio1)
	if selection == 'id':
		_.pr(getIdFromUrl(data['link']))
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

		try:
			webbrowser.open(  data['link']  , new=2)
		except Exception as e:
			try:
				native_web_app.open(  data['link']  )
			except Exception as e:
				_.cp( 'Error: unable to open browser', 'red' )


	if selection == 'x' or selection == 'exit':
		__.xit()

	try:
		selectedSomething = True
		selection = int(selection)
		_.pr()
		_.pr(movies[selection]['name'],' - has been selected')
		_.pr()
		__.cinema.register(imdbID, shouldPrint=True)
		__.xit()
	except Exception as e:
		selectedSomething = False
		# _.pr('Unspecified Error')
	if not selectedSomething:
		personMakeSelection( data )


######################################################################
def movieMakeSelection( data ):
	_.pr()
	_.pr( 'movieMakeSelection' )
	selectedSomething = False
	selection = input('Make Selection - ')
	selection = selection.lower()
	if len(selection) == 0:
		selection = 'x'
	if selection == 'h' or selection == '?' or selection == 'help':
		# _.pr('(f)ranchise')
		_.pr('id')
		_.pr('(r)ated','why')
		_.pr('(s)earch')
		_.pr('(d)escription')
		_.pr('xref')
		_.pr('l','url')
		_.pr('(p)ic')
		_.pr('(e)pisodes')
		_.pr('e(x)it')
		_.pr('save')
		_.pr('(f)ranchise')
		_.pr('search results (sr)')
		_.pr('dump')
	if selection == 'dump':
		_.printVar( data )
	if selection == 'sr':
		_.pr()
		sr = input('Search for - ')
		searchResults = []
		for m in data['people']:
			if sr.lower() in m['name'].lower():
				searchResults.append(m)
		_.pr()
		_.tables.register('searchResults',searchResults,w=1)
		_.tables.fieldProfileSet( 'searchResults', 'character', 'trigger', _.longDashAdd )
		_.tables.print('searchResults','id,name,character')
	if selection == 'f':
		_.pr()
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
		load_franchise_table( franchise )
		fID = inFranchiseID( franchise )

		if type(fID) == bool:
			_.pr( 'No Franchise Data' )
			_.pr()
			_.pr( 'Run:' )
			_.pr( '\tp franchise -f', franchise )
			__.xit()

		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')
		_.pr()
		_.pr( data['year'], '\t', data['name'] )
		_.pr()



		for ix,r in enumerate(data['people']):
			# record = {'id': cnt,'name': person,'character': character,'link': link,'img': img}
			# _.pr((r['link']))
			# _.pr(getIdFromUrl(r['link']))
			if getIdFromUrl(r['link']) in __.franchises[fID]['peopleIDS']:
				# _.pr(r['name'])
				data['people'][ix][franchise] = 'x'
			else:
				data['people'][ix][franchise] = ''
		_.tables.register('Auto',data['people'],w=1)
		_.tables.fieldProfileSet( 'Auto', 'character', 'trigger', _.longDashAdd )
		_.tables.print('Auto','id,'+franchise+',name,character')
		_.pr()
		_.pr()
		io = 0

		for ix,r in enumerate(data['people']):
			if getIdFromUrl(r['link']) in __.franchises[fID]['peopleIDS']:
				io += 1
				_.pr(r['id'],'\t',  r['name'])
		_.pr()
		if io > 0:
			_.pr(io)

		if io == 0:
			pass

		now = datetime.datetime.now()
		today = now.strftime("%Y-%m-%d")

		fdtl = __.franchises[fID]['date'].split('-')
		foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
		td = str(today).split('-')
		tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
		diff = tdd - foundDate


		try:
			ppl = _.addComma( len(set(__.franchises[fID]['peopleIDS'])) ) + ' people\t\t'
		except Exception as e:
			ppl = ''
		try:
			mv = _.addComma( len(set(__.franchises[fID]['movieIDS'])) ) + ' movies\t\t'
		except Exception as e:
			mv = ''
		_.pr('_____________________________________________________________________________________________________________________')
		_.pr( franchise.upper(), ppl, mv, __.franchises[fID]['date'], '\t\t', str(diff.days), 'days' )
		_.pr()
		_.pr()


	##################################                        ##################################
	if selection == 'id':
		_.pr(getIdFromUrl(data['link']))
	if selection == 'xref':
		crossReference()

	if selection == 'e':
		episodes(data['link'],theYear,theTitle)



	if selection == 'r' or selection == 'rated' or selection == 'why':
		movieRating(data['link'])


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

		try:
			webbrowser.open(  data['link']  , new=2)
		except Exception as e:
			try:
				native_web_app.open(  data['link']  )
			except Exception as e:
				_.cp( 'Error: unable to open browser', 'red' )


	if selection == 'x' or selection == 'exit':
		__.xit()
	if selection == 'description' or selection == 'd':
		newURL = extractUrl(data['link']) + '?ref_=ttfc_fc_tt'
		page = requests.get(newURL)
		tree = html.fromstring(page.content)
		description0 = tree.cssselect('.summary_text')
		description1 = description0[0].text_content()
		description = cleanupString(description1)
		_.pr()
		_.pr(description)
		_.pr()


	try:
		selectedSomething = True
		selection = int(selection)
		_.pr()
		_.pr(data['people'][selection]['name'],' - has been selected')
		_.pr()
		__.people.register( getIdFromUrl( data['people'][selection]['link'] ), shouldPrint=True )
		__.xit()
	except Exception as e:
		selectedSomething = False
	if not selectedSomething:
		movieMakeSelection( data )

###################################################################### ######################################################################
def loadObject(file):
	result = None
	try:
		with open(file, 'rb') as objThis:
			result = pickle.load(objThis)
	except Exception as e:
		pass
	return result
focus()
# _.appData[__.appReg]['pipe'] = ''


# def timestamp():
#   return time.time()


# _.pr(type(__.pipeData))

__.aliases = _.getTable('imdb_aliases.json')
__.noSeasonData = _.getTable('imdb_no_season_data.json')
# _.pr(__.aliases)
# test = input('pause')
__.omitFromMovies = []
__.omitFromMovies.append('Scotty\'S 4Th Birthday 7 16 84')
__.imdbAppearancesCaptured = 1553172315.2781389

__.results = []
__.franchises = []
__.franchiseFile = 'imdb-franchises.json'
__.franchiseFileDic = 'imdb-franchises-x.json'
__.franchisesDic = {}

# __.franchiseFile = 'imdb-franchises-'+  '_'.join( _.switches.values('Franchise') )  +'.json'

fileBackup = _.regImp( focus(), 'fileBackup' )
fileBackup.switch( 'Silent' )
fileBackup.switch( 'Flag', 'imdb' )
fileBackup.switch( 'isRunOnce' )
fileBackup.switch( 'DoNotSchedule' )

__.movieDrivePath = 'E:\\MOVIES'+os.sep

def backupJSON( name ):
	global fileBackup
	json_abspath = _v.myTables + os.sep + name
	fileBackup.switch( 'Input', json_abspath )
	# fileBackup.imp.action()
	fb = fileBackup.action()
	_.pr( fb )
	# fileBackup.do( fileBackup.imp.action )
# backupJSON( 'imdb_franchises.json' )
# type imdb.py | p line - # kev tmp + _.saveTable -ln
# "hallmark_date": "2019-02-13",
# "hallmark_date": "2019-05-20",

# b tt
# p fileBackup -i imdb_franchises.json

def setPipeData( data, theFocus=False ):
	if type( theFocus ) == bool:
		theFocus = __.appReg
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[theFocus]['pipe'] = []
		for pd in data:
			try:
				pd = pd.replace('\n','')
			except Exception as e:
				pass
			if not pd == '':
				_.appData[theFocus]['pipe'].append(pd)

def fixCase( data ):
	wordsUpper = 'dc'
	wordsLower = 'of,the,in'
	wordsSpecial = 'xxx:xXx'
	for word in wordsUpper.split( ',' ):
		data = data.replace( ' ' + word.title() + ' ', ' ' + word.upper() + ' ' )

		if data.lower() == word.lower():
			return word.upper()
	for word in wordsLower.split( ',' ):
		data = data.replace( ' ' + word.title() + ' ', ' ' + word.lower() + ' ' )
	for word in wordsSpecial.split( ',' ):
		z = word.split( ':' )
		data = data.replace( z[0].title(), z[1] )
	return data

def franchiseHierarchy( imdbID ):
	omit = 'Horror,horror,Fantasy,fantasy,disney,hallmark,stan lee'
	mustHave = 'avengers'

	if not len( __.franchises ):
		__.franchises = _.getTable( 'imdb_franchises_NEW.json' )

	records = []
	foundFranchise = False
	for i,row in enumerate(__.franchises):
		if imdbID in __.franchises[i]['movieIDS']:
			shouldAdd = True
			for test in omit.split( ',' ):
				if test.lower() == __.franchises[i]['label'].lower():
					shouldAdd = False
			if shouldAdd:
				if not len(__.franchises[i]['movies']):
					return i
				else:
					for movies in __.franchises[i]['movies']:
						if movies['imdbID'] == imdbID:
							movie = cleanName( movies['name'] )
							year = movies['year']

					records.append({ 'cnt': len(__.franchises[i]['movieIDS']), 'label': __.franchises[i]['label'] })
					foundFranchise = True

	if not foundFranchise:
		return False
	results = _.tables.returnSorted( 'Hierarchy', 'd:cnt', records )
	hasName = False
	for i,record in enumerate(results):
		if not i == 0:
			if record['label'].lower() in movie.lower():
				hasName = True
	if hasName:
		for i,record in enumerate(results):
			if not i == 0:
				if not record['label'].lower() in movie.lower():
					results.pop( i )
		# _.pr()
		# _.pr( movie )
		# _.printVar( results )

	first = cleanNamePathPrep( fixCase( results[0]['label'].title() ) )
	second = ''

	# return results

	if len(results) < 2 or 0 == len(results)-1:
		p = __.movieDrivePath + first + os.sep + year + ' ' + movie + '.mkv'
	else:
		second = cleanNamePathPrep( fixCase( results[ len(results)-1 ]['label'].title() ) )
		useSecond = True
		for test in mustHave.split( ',' ):
			if test.lower() in second.lower():
				# _.pr( test.lower(), second.lower(), movie.lower() )
				if not test.lower() in movie.lower():
					useSecond = False

		if useSecond:
			p = __.movieDrivePath + first + os.sep + second + os.sep + year + ' ' + movie + '.mkv'
		else:
			second = ''
			p = __.movieDrivePath + first + os.sep + year + ' ' + movie + '.mkv'
	# _.printVar( results )
	p = p.replace( os.sep+' ', os.sep )
	return { 'first': first, 'second': second, 'path': p }
	# _.pr( p )



	# __.xit()




def inFranchiseID( test ):
	if not len( __.franchises ):
		__.franchises = _.getTable( 'imdb_franchises_NEW.json' )
	test = test.lower()
	test = test.replace( ',', ' ' )
	test = test.replace( '_', ' ' )
	for i,franchise in enumerate(__.franchises):
		for alias in franchise['aliases']:
			# _.pr( test, alias )
			if alias == test:
				return i
		if _.switches.isActive( 'AutoFranchise' ):
			if ' ' in test:
				cnt = 0
				for part in franchise['parts']:
					if not _omit.imp.inTable( part ):
						for t in test.split( ' ' ):
							if part in t:
								cnt += 1
				if cnt > 1:
					ask = ''
					_.pr( '\n','Part:',test )
					ask = test + ': ' + input( franchise['label']+'? (y): ' )
					if not ask == 'n':
						__.franchises[i]['aliases'].append( test )
						_.saveTable(__.franchises,__.franchiseFile)
						return i
		if _.switches.isActive( 'AutoFranchise' ):
			for i,franchise in enumerate(__.franchises):
				for alias in franchise['aliases']:
					if alias in test:
						_.pr( '\n','Alias:',test )
						ask = test + ': ' + input( franchise['label']+'? (y): ' )
						if not ask == 'n':
							__.franchises[i]['aliases'].append( test )
							_.saveTable(__.franchises,__.franchiseFile)
							return i
				for part in franchise['parts']:
					if not _omit.imp.inTable( part ):
						for t in test.split( ' ' ):
							if part in t:
								ask = ''
								_.pr( '\n','Part:',test )
								ask = test + ': ' + input( franchise['label']+'? (y): ' )
								if not ask == 'n':
									__.franchises[i]['aliases'].append( test )
									_.saveTable(__.franchises,__.franchiseFile)
									return i
	return False

def cleanName( data ):
	for xyz in __.imdb_replace:
		data = data.replace( xyz[0], xyz[1] )
	# data = data.replace( '\\xb1', 'n' ).replace( '\xb1', 'n' )
	return _str.cleanBE( _str.replaceDuplicate( _str.cleanChar( data ), ' ' ) ,' ')

def cleanNamePathPrep( data ):
	data = data.replace( '&', ' and ' )
	data = cleanName( data )
	return data

def cleanName2( data ):
	for xyz in __.imdb_replace:
		data = data.replace( xyz[0], xyz[1] )
	# data = data.replace( '\\xb1', 'n' ).replace( '\xb1', 'n' )
	data = cleanName( data )
	data = data.replace( os.sep+' ', os.sep )
	data = data.replace( ' '+os.sep, os.sep )
	return data

def cleanName_old( data ):
	for xyz in __.imdb_replace:
		data = data.replace( xyz[0], xyz[1] )
	# data = data.replace( '\\xb1', 'n' ).replace( '\xb1', 'n' )
	remove = [
				os.sep+'xb*',
	]
	for r in remove:
		if '*' in r:
			for x in _str.safeChar:
				data = data.replace( r.replace( '*', x ), '' )
		else:
			data = data.replace( r, '' )
	return data

def franchiseYearField( year, field, sortby, data ):
	franchises = []
	for row in data:
		if not row[field] in franchises:
			franchises.append( row[field] )

	for row in franchises:
		tmp = []
		nData = []
		for rowX in data:
			if row == rowX[field]:
				tmp.append( rowX )
		nData = _.tables.returnSorted( 'tmp', 'd:'+year, tmp )
		for i,rowX in enumerate(data):
			if row == rowX[field]:
				try:
					str( data[i][sortby] )
					addThis = False
				except Exception as e:
					addThis = True
				try:
					text = str(nData[0][year]) + data[i][field]
				except Exception as e:
					text = ''
				if not len( data[i][field] ):
					text = ''
				if addThis:
					data[i][sortby] = text
					# _.pr( data[i][sortby] )
	return data


def franchiseYear( data ):
	data = franchiseYearField( 'year', 'first', 'xfirst', data )
	data = franchiseYearField( 'year', 'second', 'xsecond', data )
	data = _.tables.returnSorted( 'Path', 'd:xfirst,d:xsecond,d.year', data )
	return data

def uniqueIMDBID( data ):
	printData = []
	inList = []
	for row in data:
		# printData.append( row )
		if not row['imdbID'] in inList:
			inList.append( row['imdbID'] )
			printData.append( row )
	return printData

def printFranchiseTable( data ):
	printData = uniqueIMDBID( data )
	# _.printVar( printData )
	_.switches.fieldSet( 'Long', 'active', True )
	_.switches.fieldSet( 'Sort', 'active', True )
	_.switches.fieldSet( 'Sort', 'value', 'd:first,d:xsecond,d.year' )
	_.switches.fieldSet( 'GroupBy', 'active', True )
	_.switches.fieldSet( 'GroupBy', 'value', 'first,second' )
	_.tables.register( 'data', franchiseYear( printData ) ,w=1)
	if 'id' in _.switches.value('MovieFranchise'):
		_.tables.print( 'data', 'first,second,label,imdbID' )
	else:
		_.tables.print( 'data', 'first,second,label' )
	_.pr()
	_.pr( len( printData ) )


def load_franchise_table( franchise ):
	if not franchise in __.franchisesDic:
		__.franchisesDic[ franchise ] = 1
		file = __.franchiseFileDic.replace( 'x', franchise.upper().replace(' ','_') )
		for rec in _.getTable(file):
			__.franchises.append( rec )

def load_all_franchises():
	import glob
	tt = _v.myTables + os.sep
	for fran_file in glob.glob( tt + 'imdb-franchises-*' ):
		if not os.sep in fran_file:
			fran_file = tt+fran_file
		for rec in _.getTable2( fran_file ):
			__.franchises.append(rec)





txt_clean_list = [
					'\xc3', os.sep+'xc3',
					'\xad', os.sep+'xad',
					'\xc3', os.sep+'xc3',
					'\xb3', os.sep+'xb3',
					'\xc3', os.sep+'xc3',
					'\x93', os.sep+'x93',
]

__.imdb_replace = [
						['\\xb1', 'n'],
						['\xb1', 'n'],
]
__.data_day_diff = 400
dataPerson_data = None
dataMovie_data = None










__.threads_complete = False
_async = None
def threads_done():
	__.threads_complete = True






__.print_html_page_IDs = False






# {'first': 'Star Wars', 'second': '', 'path': '', 'print': '1977 Star Wars', 'year': '1977', 'name': 'Star Wars'}
########################################################################################
if __name__ == '__main__':
	_.switches.fieldSet( 'xRef-Page-Threaded', 'active', True )
	_.switches.fieldSet( 'EpisodeTable', 'active', True )
	if _.switches.isActive('Watched'):
		_.pr( _.switches.value('Watched') )
		# __.xit()
	if _.switches.isActive('Case'):
		caseTest()
	else:
		action()

# __.pipeData = _.appData[__.appReg]['pipe']
# pathGen


# print_fullcredits
# def register(
# get_fullcredits

# get_cinema_fullcredits

# movieMakeSelection( people )

# {'name': theTitle, 'year': theYear, 'link': url, 'people': people}
# { 'id': ip, 'imdbID': personID, 'name': person, 'link': link, 'character': character }

# data['name']
# data['people']
# getIdFromUrl

# __.people.register(imdbID, shouldPrint=True)
# __.cinema.register(imdbID, shouldPrint=True)


#   def register(self, imdbID, shouldPrint):
#       self.addChild(imdbID)
#       self.childRow(imdbID)
#       if type(self.thisRow) == float:
#           _.pr('Error: childRow')
#           __.xit()

#       self.childItemRows[self.thisRow].get_fullcredits()

# get_people_fullcredits

# {'id': iiii, 'name': cleanName(title), 'year': year, 'thisID': thisID, 'img': img, 'age': gigAge}
# { 'name': x, 'date': x, 'year': x, 'location': x, 'link': x, 'movies': movies }

# get_work_history
# data['movies']
# data['age']

# p imdb -case -ent alien 3 -print -skipload save
# 0
# x


# def rating(
# def seasons(
# franchiseHierarchy
# PrintPath

# ForceFranchise
# get_cinema_fullcredits

# print('self.isExpired(section)',self.expirationDateDefault); sys.exit();
# self.expirationDateDefault = 'never'
# __.objectLocation['objects']
# print_url(frameinfo=getframeinfo(currentframe()), url=newURL,c='cyan')

# e5de297b upload
# 3aaf1206 page url
# def dataPerson(