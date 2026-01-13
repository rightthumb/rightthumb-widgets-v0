import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'URL', '-url' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'open-url.py',
	'description': 'Open URL',
	'categories': [
						'url',
				],
	'examples': [
						_.hp('p open-url -url https://google.com'),
						_.hp('p open-url -url index.php'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
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

import webbrowser

def action():
	url = _.switches.values('URL')[0]
	url = url.replace('index.php','')
	url = url.replace('index.html','')
	url = url.replace('index.htm	','')
	if 'http' not in url:
		webbrowser.open(url)
	else:
		import os
		import sys
		try:
			# Dynamically import the `site` module
			site = _.rImp("site")
			# Call meta_scan
			xurl = site.meta_scan(os.getcwd())
			xurl += '/' + url.replace('\\', '/')
			xurl = xurl.replace('http://','')
			print(xurl)
			webbrowser.open(xurl)
			# webbrowser.open(url)
		except Exception as e:
			print(f"Error: {e}")

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);