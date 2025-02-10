import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'CodeSnippets', '-snip,-snippets' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'uniqueLine.py',
	'description': 'Prints unique lines',
	'categories': [
						'examples',
						'python',
						'unique',
						'line',
				],
	'examples': [
						_.hp('cat  examples.py | p uniqueLine'),
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
	spent = []
	for line in _.isData(r=0):
		if not _.showLine(line): continue
		cl = line.replace('#','').strip()
		if not cl in spent:
			spent.append(cl)
			if _.switches.isActive('CodeSnippets'):
				if  ')-->' in cl:
					_.pr(line)
				elif not '=' in cl:
					_.pr('  ',cl)
				else:
					_.pr(cl)

			else:
				_.pr(line)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);