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

import os, sys, time
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
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Subject', '-subject' )

_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'unicode.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'unicode to string',
	'categories': [
						'icons',
						'tool',
						'unicode',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] }, 
		},
	}



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
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
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


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START
import urllib.parse

# def cleanupString0( string ):
#     string = formatData( string )
#     string = string.replace( '\xe2\x80', '-' ).replace( _v.slash+'xe2\\x80', '-' )
#     for x in txt_clean_list:
#         string = string.replace( x, '' )
#     string = _str.replaceAll(string,'\n',' ')
#     string = _str.replaceDuplicate(string,' ')
#     string = _str.cleanLast(string,' ')
#     string = _str.cleanFirst(string,' ')
#     string = _str.cleanSpecial(string)
#     string = _str.replaceDuplicate(string,' ')
#     string = _str.cleanFirst(string,' ')
#     string = printClean( string )
#     string = _str.cleanBE(string,' ')
#     return string
def cleanupString(string,beforeAfter=True):
	# string = formatData( string )
	string = string.replace( '\xa0', '' ).replace( _v.slash+'xa0', '-' )
	string = string.replace( '\xe2\x80', '-' ).replace( _v.slash+'xe2\\x80', '-' )
	string = _str.replaceAll(string,'\xc2',' ')
	string = _str.replaceAll(string,_v.slash+'xc2',' ')
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.cleanLast(string,' ')
	# string = _str.cleanFirst(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanBE(string,' ')
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
	# if string == 'b':
	#     string = ''
	return string

def download(subject):
	requests = __.imp('requests')
	html = __.imp('lxml.html')
	url = 'https://graphemica.com/' + urllib.parse.quote(subject)
	page = requests.get(url)
	tree = html.fromstring(page.content)
	tables = tree.cssselect('#c-java-javascript-and-json')
	text = ''
	for table in tables:
		text += table.text_content()

	text = cleanupString(text)
	text = text.split(' ')[0]
	return text

def process(subject):
	# _.pr(subject)
	# _.pr(download(subject))
	return { 'text': subject.replace(' ','') }
	# return { 'text': subject, 'hex': subject.encode("utf-8").hex(), 'code': download(subject) }
	return subject.encode("utf-8").hex(), download(subject)
	return subject.encode("utf-8")
	return subject.encode()
	# return unicode(subject.encode("utf-8"))

def JSON(data):
	simplejson = __.imp('simplejson')
	return simplejson.dumps(data, indent=4, sort_keys=False)

def action():

	if _.switches.isActive('Subject'):
		for item in _.switches.values('Subject'):
			# _.pr(item)
			x = eval(item)
			_.pr(x)
		return None

	for i,subject in enumerate( _.isData(r=1) ):
		sub = _.getText( subject, raw=True )
		# s = s.replace( chr(10), '\n' )
		# s = s.replace( chr(27), '' )
		for s in sub:

			rec = process(s)
			t = rec['text']
			if t:
				# json = _.pv(rec,p=0)
				json = JSON( rec )
				# _.pr(json)
				# sys.exit()
				code = json.split('"')[3]
				_.pr( s, code )

			# _.pr( rec )



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







