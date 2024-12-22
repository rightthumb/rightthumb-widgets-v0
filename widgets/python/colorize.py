import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Text', '-i,-t,-text', isData='name', isRequired=True )
	_.switches.register( 'Color', '-color', isRequired=True )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'colorize.py',
	'description': 'Used in shell scripts, batch files, etc. to colorize text',
	'categories': [
						'colorize',
						'Script Helper',
						'Batch Files',
						'Shell Scripts',
						'Utility',
				],
	'examples': [
						_.hp('p colorize -text "Error: Invalid Input" "Example: script valid/folder" -color red yellow'),
						_.pr('   Error: Invalid Input',c='red',p=0)+' '+_.pr('Example: script.sh valid/folder',c='yellow',p=0),
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

def action():
	if len(_.switches.values('Color')) == 1:
		color = _.switches.value('Color')
		text = ' '.join(_.switches.values('Text'))
		_.pr(text,c=color)
	else:
		text = []
		colors = _.switches.values('Color')
		color = colors[0]
		for i,txt in enumerate(_.switches.values('Text')):
			try:
				color = colors[i]
			except: pass
			text.append( _.pr(txt,c=color,p=0) )
		final = ' '.join(text)
		print(final)

if __name__ == '__main__':
	action(); _.isExit(__file__);