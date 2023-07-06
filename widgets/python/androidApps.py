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

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Who', '-who','mom')
	_.switches.register('Get', '-get')
	_.switches.register('Ask', '-ask')
	_.switches.register('Stats', '-stats,-stat')
	_.switches.register('Manual', '-manual')
	_.switches.register('CrossRef', '-xref')

	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'androidApps.py',
	'description': 'Report about apps on andoid devices',
	'categories': [
						'research',
						'mobile',
						'phone',
						'log',
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

_.appInfo[focus()]['examples'].append('p androidApps -c c g n -g c')
_.appInfo[focus()]['examples'].append('p androidApps ')
_.appInfo[focus()]['examples'].append('p androidApps -get -stats')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p androidApps -who mom -get')
_.appInfo[focus()]['examples'].append('p androidApps -who mom')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p androidApps -who dad -get')
_.appInfo[focus()]['examples'].append('p androidApps -who dad')
_.appInfo[focus()]['examples'].append('p androidApps -who dad -manual')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p androidApps -who dad -s s')
_.appInfo[focus()]['examples'].append('p androidApps -who dad -c c g n -g c')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p androidApps -who me -xref mom -g x rs -c x rs c g n -s x rs c g')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')

_.appInfo[focus()]['columns'].append({'name': 'company', 'abbreviation': 'c'})
_.appInfo[focus()]['columns'].append({'name': 'genre', 'abbreviation': 'g'})
_.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})
_.appInfo[focus()]['columns'].append({'name': 'description', 'abbreviation': 'd'})
_.appInfo[focus()]['columns'].append({'name': 'stars', 'abbreviation': 's'})
_.appInfo[focus()]['columns'].append({'name': 'xref', 'abbreviation': 'x'})
_.appInfo[focus()]['columns'].append({'name': 'r_stars', 'abbreviation': 'rs'})





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

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = True

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

_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
########################################################################################
# START

def action():
	global masterData
	if _.switches.isActive('CrossRef'):
		xRef()
		sys.exit()
	if _.switches.isActive('Get'):

		hack = """
function acquirePayload() {
	console.log( 'acquirePayload' );
	hackElements = [];
	$( '.card' ).each(function( index ) {
		theLink = ''
		$(this).find('a').each(function( index ) {
			var testLink = $(this).attr('href');
			if (testLink.includes('/store/')) { theLink=testLink; }
		});

		var thisName = $(this).find('.title').text().trim();
		var thisURL = 'https://play.google.com'+theLink;

		var thisDescription = $(this).find('.description').text().trim();
		var ts = $(this).find('.tiny-star').attr('aria-label').trim();
		try {
			var tss = ts.split( ' ' );
			var thisStars = tss[1];
		} catch(err) {
			var thisStars = '';
		}
		

		hackElements.push({ 'name': thisName, 'url': thisURL, 'description': thisDescription, 'stars': thisStars });
	});
	// copy( hackElements )
	
	console.log( '' );
	console.log( 'Done' );
	console.log( '' );
	console.log( 'Execute:    copy( hackElements );' );
	
}
function scrollEnd() {
	console.log( 'scrollEnd' );
	setTimeout(function(){
		$( 'html, body' ).scrollTop($(document).height());
		setTimeout(function(){
			$( 'html, body' ).scrollTop($(document).height()-1000); 
			setTimeout(function(){
				$( 'html, body' ).scrollTop($(document).height());
				setTimeout(function(){

					if ( $( '#show-more-button' ).css( 'display' ) !== 'none' ) {
						$( '#show-more-button' ).click();
						setTimeout(function(){ scrollEnd(); }, 1500);
					} else {
						if (checkLen()) {
							setTimeout(function(){ acquirePayload(); }, 1500);
						} else {
							setTimeout(function(){ scrollEnd(); }, 1500);
						}
					}
					
				}, 1500);
			}, 1500);

		}, 1500);

	}, 1500);

	
}


function checkLen() {
	hackElements = [];
	$( '.id-card-list .title' ).each(function( index ) {
			hackElements.push( $(this).text() );
	});
	if (lastLength == hackElements.length) {
		return true;
	} else {
		lastLength = hackElements.length
		return false;
	}
}



lastLength = 0;

setTimeout(function(){ scrollEnd(); }, 800);

// acquirePayload();
// copy( hackElements );
		"""

		
		_.copyVar( hack )
		if _.switches.isActive('Who'):
			do = 'n ' + _v.myTables + _v.slash+'android_apps_'+_.switches.value('Who')+'.json'
		else:
			do = 'n ' + _v.myTables + _v.slash+'android_apps.json'
		os.system('"' + do + '"')
		_.openURL( 'https://play.google.com/apps' )
		pause = input( 'pause ' )




	if _.switches.isActive('Get'):
		_.threads.add( 'genre', trigger=complete, loaded=False, database=False ) # kwargs 
		_.threads.maxThreadsSafe = 100
		_.threads.autoLoadedAfter = .5
		_.threads.scheduleLoop = .01
		_.threads.auditLoop = .1
		# _.threads.projectDataMaxLen = 500

		if _.switches.isActive('Stats'):
			_.threads.report = True
			_.threads.auditPrint = True
		else:
			_.threads.report = False
			_.threads.auditPrint = False

	global apps

	if _.switches.isActive('Who'):
		apps = _.getTable( 'android_apps_'+_.switches.value('Who')+'.json' )
	else:
		apps = _.getTable( 'android_apps.json' )

	selectedApps = []
	# _.pr( 'HERE' )
	if _.switches.isActive('Get'):
		for i,app in enumerate(apps):
			# _.pr( app )
			_.threads.add( 'genre', scheduleX, [ app ] )
			# if _.showLine( app['genre'] + ' ' + app['company'] + ' ' + app['name'] + ' ' + app['description'] + ' ' + app['stars'] ):
	else:
		complete()




def complete():
	# _.pr( 'HERE: complete 0' )
	global apps
	global masterData


	try:
		_.saveTable( masterData, _v.androidMaster, printThis=False )
	except Exception as e:
		pass
	# _.pr( 'HERE: complete 1' )

	selectedApps = []
	for i,app in enumerate(apps):
		r = androidMaster( app )
		if _.showLine( r['genre'] + ' ' + r['company'] + ' ' + r['name'] + ' ' + r['description'] + ' ' + r['stars'] ):
			r['id'] = i
			selectedApps.append( r )

	# if _.switches.isActive('Get') or _.switches.isActive('Manual'):

	_.pr()
	_.pr()

	# for i,app in enumerate(selectedApps):
	#     _.pr( i, '\t', app['name'] )
	_.switches.fieldSet( 'Long', 'active', True )

	if not _.switches.isActive('GroupBy') and not _.switches.isActive('Sort'):
		_.switches.fieldSet( 'GroupBy', 'active', True )
		_.switches.fieldSet( 'GroupBy', 'value', 'g' )
	_.tables.register('apps',selectedApps)
	_.tables.fieldProfileSet('apps','company,genre,name,description','trigger',_.printSafe)
	if _.switches.isActive('Column'):
		# _.pr( _.switches.value('Column') )
		# sys.exit()
		# _.tables.print('apps', 'company,genre,name' )
		_.tables.print('apps', _.switches.value('Column') )
	else:
		if _.switches.isActive('Ask'):
			_.tables.print('apps','genre,id,name,company')
		else:
			_.tables.print('apps','genre,company,stars,name')


	_.pr()
	_.pr( 'Apps:', len( apps ) )

	
	if _.switches.isActive('Ask'):
		loopList( selectedApps )
def loopList( selectedApps ):
	ask = ''

	_.pr()
	_.pr()

	while not 'x' in ask.lower():
		_.pr()
		ask = input( 'View app webpage: ' )
		if not 'x' in ask.lower():
			try:
				_.openURL( selectedApps[int(ask)]['url'] )
			except Exception as e:
				_.pr( 'Error: bad id' )

def androidMaster( data ):
	global masterData


	found = False
	for i,rec in enumerate(masterData):
		if rec['url'] == data['url']:
			found = True

			try:
				rec['skip']
			except Exception as e:
				rec['skip'] = False
				masterData[i]['skip'] = False
			if _.switches.isActive('Manual'):
			# if True:
				if rec['company'] == '' or rec['genre'] == '':
					if not rec['skip']:
						gc = getGenre( data['url'] )
						masterData[i]['genre'] = gc[0]
						masterData[i]['company'] = gc[1]
						if _.switches.isActive('Manual'):
							if masterData[i]['genre'] == '' or masterData[i]['company'] == '' :
								_.openURL( data['url'] )
								_.pr()
								copyManual()
								gc = input( ' Manual input: ' )
								if '{' in gc:
									gc = eval( gc )
									masterData[i]['genre'] = gc['g']
									masterData[i]['company'] = gc['c']
								else:
									masterData[i]['skip'] = True
						_.saveTable( masterData, _v.androidMaster, printThis=False )
							
			data['genre'] = rec['genre']
			data['company'] = rec['company']

	if not found:
		gc = getGenre( data['url'] )
		data['genre'] = gc[0]
		data['company'] = gc[1]
		# _.pr( 'genre:', data['genre'] )
		masterData.append( data )
		# _.saveTable( masterData, _v.androidMaster, printThis=False )
		# _.pr( 'NOT FOUND:', data['genre'],'\t', data )
		# sys.exit()
		# sys.exit()


	return data


def check( data ):
	global masterData

	for i,rec in enumerate(masterData):
		if rec['url'] == data['url']:
			return True

	return False



def scheduleX( data, qID=False ):
	global masterData

	if not check( data ):
		gc = getGenre( data['url'] )
		data['skip'] = False
		data['genre'] = gc[0]
		data['company'] = gc[1]

		# _.pr( 'genre:', data['genre'] )
		masterData.append( data )
		_.saveTable( masterData, _v.androidMaster, printThis=False )
		# _.saveTable( masterData, _v.androidMaster )
	if not type(qID) == bool:
		_.threads.spent( qID, sys.getsizeof( str(data) ) )



def getGenre( url ):
	genre = ''
	company = ''

	page = requests.get(url)
	tree = html.fromstring(page.content)
	tables = tree.cssselect('a[itemprop]')
	tablesX = tree.cssselect('a')
	for t in tables:
		if 'genre' in str(t.attrib['itemprop']):
			genre = cleanupString0( t.text_content() )
			break
	for t in tablesX:
		try:
			if 'https://play.google.com/store/apps/dev?id=' in str(t.attrib['href']) or 'https://play.google.com/store/apps/developer?id=' in str(t.attrib['href']) :
				company = cleanupString0( t.text_content() )
				break
		except Exception as e:
			pass

	# try:
	#     page = requests.get(url)
	#     tree = html.fromstring(page.content)
	#     tables = tree.cssselect('a[itemprop]')
	#     for t in tables:
	#         if 'genre' in str(t.attrib['itemprop']):
	#             result = cleanupString0( t.text_content() )
	#             break
	# except Exception as e:
	#     pass
	
	# https://play.google.com/store/apps/dev?id=

	return [ genre, company ]

def copyManual():
	m = """
function acquirePayload() {
	var genre='';
	var company='';

	var links = document.querySelectorAll('a');
	for(var i = 0; i < links.length; i++){
		if ( links[i].href.includes('https://play.google.com/store/apps/dev?id=') || links[i].href.includes('https://play.google.com/store/apps/developer?id=') ) {
			console.log( links[i].text.trim() );
			company = links[i].text.trim();
			if ( company.length > 0) {
				break
			}
		}
	};
	var links = document.querySelectorAll('a[itemprop="genre"]');
	genre = links[0].text.trim();
	
	return { 'g': genre, 'c': company }
}
copy( JSON.stringify(acquirePayload())+_v.slash+'n' );
	"""
	_.copyVar( m )
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

apps = []
masterData = _.getTable( _v.androidMaster )


from lxml import html
import requests
import cssselect

# if _.switches.isActive('Get'):

def xExist( test, data ):
	for row in data:
		if test == row['url']:
			return True
	return False

def mData( test, data ):
	global masterData
	for row in masterData:
		if test == row['url']:
			return row
	return False

def roundStar( stars ):
	s = float( stars )
	t = str( s )
	p = t.split( '.' )
	result = p[0] + '.'
	if int(p[1]) < 5:
		result += '0'
	else:
		result += '5'
	return result

def glimps( data ):
	p = _.printSafe( str( data ) )
	return p.split( ' ' )[0]

def xRef():
	one = _.getTable( 'android_apps_'+_.switches.value('Who')+'.json' )
	two = _.getTable( 'android_apps_'+_.switches.value('CrossRef')+'.json' )
	data = []

	for md in one:
		# md['xref'] = 'No, not in ' + _.switches.value('CrossRef').upper() + ' database'
		md['xref'] = 'Not in xref'
		if xExist( md['url'], two ):
			# md['xref'] = 'Yes, in ' + _.switches.value('CrossRef').upper() + ' database'
			md['xref'] = 'Yes, in xref'

		record = mData( md['url'], data )
		record['xref'] = md['xref']
		record['r_stars'] = roundStar( md['stars'] )
		data.append( record )
				


	_.switches.fieldSet( 'Long', 'active', True )

	if not _.switches.isActive('GroupBy') and not _.switches.isActive('Sort'):
		_.switches.fieldSet( 'GroupBy', 'active', True )
		_.switches.fieldSet( 'GroupBy', 'value', 'x,g' )

	# _.tables.maxNameLength = 20
	_.tables.register('apps',data)
	_.tables.fieldProfileSet('apps','company,genre,name,description','trigger',_.printSafe)
	_.tables.fieldProfileSet('apps','company','trigger',_.printSafe)
	# _.tables.fieldProfileSet('apps','company','trigger',glimps)
	if _.switches.isActive('Column'):
		_.tables.print('apps', _.switches.value('Column') )
	else:
		_.tables.print('apps','xref,genre,company,stars,company,name')

  # {
  #   "name": "Amazon Kindle",
  #   "url": "https://play.google.com/store/apps/details?id=com.amazon.kindle",
  #   "description": "Your library in your pocket. Anytime, anywhere.",
  #   "stars": "4.2"
  # }

# google LLC, Productivity
########################################################################################
if __name__ == '__main__':
	action()






