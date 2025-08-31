import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	swGrp = 1
	_.switches.register( 'Text', '-i,-t,-txt,-text', isData='name', isRequired=True, group=[swGrp,'Text Input'] )
	swGrp += 1
	_.switches.register( 'Color', '-color', isRequired=False, group=[swGrp,'Colors per Text arg'] )
	_.switches.register( 'HexColor', '-h,-hex', isRequired=False, group=[swGrp,'Colors per Text arg'] )
	swGrp += 1
	_.switches.register( 'Copy', '-cp,-copy', isRequired=False, group=[swGrp,'Extra'] )
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
						_.hp('p colorize -text List Colors -color list'),
						_.hp('p colorize -text List Colors -hex list'),
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

def clean(data):
	Type = type(data)
	if Type == str:
		data = data.split('\n')
	lines = []
	for i, line in enumerate(data):
		line = line.strip().replace("'",'"').replace('"','')
		if line:
			lines.append(line)
	if Type == str:
		lines = '\n'.join(lines)
	return lines


def action():
	if len(_.switches.values('Color')) == 1:
		color = _.switches.value('Color')
		text = ' '.join(_.switches.values('Text'))
		_.pr(text,c=color)
	else:
		text = []
		colors = _.switches.values('Color')
		if _.switches.isActive('HexColor'):
			colors = _.switches.values('HexColor')
		color = colors[0]
		for i,txt in enumerate(_.switches.values('Text')):
			try:
				color = colors[i]
			except: pass
			if _.switches.isActive('HexColor'):
				text.append( _.pr(txt.replace("'",'"'),h=color,p=0) )
			else:
				text.append( _.pr(txt.replace("'",'"'),c=color,p=0) )
		final = ' '.join(text).replace('\\n','\n')
		print(final)
		if _.switches.isActive('Copy'):
			txt = ' '.join(_.switches.values('Text'))
			_copy = _.regImp( __.appReg, '-copy' )
			if '\\n' in txt:
				_copy.imp.copy(   '\n'.join(  clean(txt.strip().split('\\n'))  ), p=0 )
			else:
				_copy.imp.copy( txt.strip(), p=0 )


if __name__ == '__main__':
	action(); _.isExit(__file__);