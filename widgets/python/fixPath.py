import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Test', '-t,-test' )
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
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def action():
	paths = os.environ['PATH'].split(';')
	paths = list(set(paths))
	RightThumb = []
	Windows = []
	ProgramFiles = []
	Users = []
	Other = []
	spent = []
	for path in paths:
		if _.switches.isActive('Test'):
			print(path)
			continue
		lPath = path.lower()
		# path = __.path(path)
		if lPath in spent: continue
		spent.append(lPath)
		# if not os.path.isdir(path): continue
		if False: pass
		elif 'c:\\windows' in lPath: Windows.append(path)
		elif 'c:\\program files' in lPath: ProgramFiles.append(path)
		elif 'rightthumb' in lPath: RightThumb.append(path)
		elif 'c:\\users\\' in lPath: Users.append(path)
		else:
			Other.append(path)
	Paths = []
	rt = []
	for path in RightThumb:
		rt.append({'path':path, 'size': len(path)})

	rt.sort(key=lambda x: x['size'], reverse=False)
	for path in rt:
		Paths.append(path['path'])
	# 	print(path['path'])
	# _.isExit(__file__)
	# 	# Paths.append(path)
	for path in ProgramFiles: Paths.append(path)
	for path in Windows: Paths.append(path)
	for path in Users: Paths.append(path)
	for path in Other:Paths.append(path)
	newPath = ';'.join(Paths)
	print('SET PATH='+newPath)

import os
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);