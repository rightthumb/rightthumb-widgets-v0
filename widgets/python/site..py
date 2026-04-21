import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Alias', '-a,-alias' )
	_.switches.register( 'Site', '-u,-url,-site' )
	_.switches.register( 'Add', '-add', 'add to site' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'site..py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p site. -a g -site https://google.com'),
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
	load()
	global sites
	if _.switches.isActive('Add'):
		add = _.switches.value('Add')
	else:
		add = ''
	if _.switches.isActive('Alias') and _.switches.isActive('Site'):
		url = _.switches.value('Site')
		for alias in _.switches.values('Alias'): sites[alias] = url
		_.saveTable( sites, 'site.index', p=0 )
		_.pr('Saved',c='green')
	elif _.switches.isActive('Alias'):
		alias = _.switches.value('Alias')
		try:
			url = sites[alias]+add
			_.pr(url,c='yellow')
			import webbrowser
			webbrowser.open(url)
		except:
			_.e('Alias not found')
	elif _.switches.isActive('Site'):
		import webbrowser
		for site in _.switches.values('Site'):
			webbrowser.open(site+add)
	else:
		_.e('Must specify an alias and/or site/url',['p site. -a g google ggl -site https://google.com','p site. -a g','p site. -url https://google.com'])


def load():
	global sites
	sites = _.getTable( 'site.index' )

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);