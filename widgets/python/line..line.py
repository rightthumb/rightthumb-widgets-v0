import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', description='Files', isRequired=False )
	_.switches.register('Clipboard', '-clip,-second','auto activated if not file')
	_.switches.register('Pre', '-pre,-p','rename')
	_.switches.register('Post', '-post,-pp','-aSwitch')
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'line..line.py',
	'description': 'Match lines and put next to each other.',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('cat first.txt | p line..line -f second.txt -pre mv'),
						_.hp('(copy text)'),
						_.hp('first | p line..line -clip -pre rename'),
						_.hp('first | p line..line -pre rename'),
						_.hp(''),
						_.hp('  or'),
						_.hp(''),
						_.hp('(copy text)'),
						_.hp('cpIn'),
						_.hp('(copy text)'),
						_.hp('cpOut | p line..line -clip -pre rename'),
						_.linePrint(label='simple',p=0),
						''
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



	_.switches.trigger( 'Pre', _.ci )
	_.switches.trigger( 'Post', _.ci )
	
	
	
	_.switches.trigger( 'Files', _.myFileLocations, vs=False )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start



def clean(data):
	Type = type(data)
	if Type == str:
		data = data.split('\n')
	lines = []
	for i, line in enumerate(data):
		line = line.strip()
		if line:
			lines.append(line)
	if Type == str:
		lines = '\n'.join(lines)
	return lines



def action():
	if _.switches.isActive('Files'):
		first = _.getText( _.switches.value('Files') )
	else:
		first = _.isData(r=0)

	first = clean(first)
	if _.switches.isActive('Files'):
		second = clean(_.getText( _.switches.value('Files') ))
	else:
		_paste = _.regImp( __.appReg, '-paste' )
		copy = clean(_paste.imp.paste()).split('\n')
	pre = ' '.join(_.switches.values('Pre'))
	post = ' '.join(_.switches.values('Post'))
	for i,line in enumerate(copy):
		items = []
		items.append(pre)
		items.append(first[i])
		items.append(line)
		items.append(post)
		_.pr(' '.join(items).strip())
		


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)