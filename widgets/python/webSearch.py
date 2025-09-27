import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'URL', '-u,-url,-urls', isData='data', description='URL', isRequired=False )
	_.switches.register( 'ShowFoundUrls', '--c,--urls' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def action():
	import requests
	urls = 0
	found = 0
	spent = []
	for url in _.isData():
		printed = False
		if not url.strip(): continue
		if not '://' in url.strip(): continue
		if not _.switches.isActive('ShowFoundUrls'):
			_.pr(url,c='cyan')
		page = requests.get(url).text
		
		# print(page)
		for line in page.split('\n'):
			# for plus in _.switches.values('Plus'):
			# 	if plus.lower() in line.lower():
			# 		_.pr(line)
			if _.showLine(line):
				for plusSearchX in _.switches.values('Plus'):
					plusSearchX = _.ci( plusSearchX )
					for subject in _.caseUnspecificCode( line, plusSearchX ):
						line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )
				if not _.switches.isActive('ShowFoundUrls'):
					print( line )
				else:
					if not printed:
						_.pr(url,c='cyan')
						printed = True
				found += 1
				if not url in spent:
					spent.append(url)
					urls += 1
	_.pr()
	_.pr(' found:',found, c='yellow')
	_.pr('  urls:',urls, c='yellow')
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);