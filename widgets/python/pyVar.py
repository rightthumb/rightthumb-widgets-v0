import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	_.switches.register( 'ValueEquals', '-v','file.txt' )
	_.switches.register( 'FromCallable', '--c' )
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
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'ValueEquals', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

def action():
	vars = {}
	vals = []
	if _.switches.isActive('ValueEquals'):
		vals = _.getText(_.switches.value('ValueEquals'), raw=True, clean=2).split('\n')
		if _.switches.isActive('FromCallable'):
			new = []
			for v in vals:
				v = v.split('.')[0]
				v = v.split(':')[0]
				new.append(v)
			# unique values
			vals = list( set(new) )
			# return
	
	for line in _.isData(2):
		line = line.split('#')[0]
		if line.startswith(' ') or line.startswith('\t'): continue
		if not '=' in line: continue
		while ' =' in line: line = line.replace(' =','=')
		while '= ' in line: line = line.replace('= ','=')
		key, value = line.split('=', 1)
		key = key.strip()
		value = value.strip()
		if not key: continue
		if not value: continue
		if not vals:
			vars[key] = value
		else:
			if value in vals:
				if not '.' in key:
					vars[key] = value

	_.pv(vars)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)