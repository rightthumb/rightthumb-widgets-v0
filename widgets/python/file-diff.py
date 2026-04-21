import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'file-diff.py',
	'description': 'File differences, PIPE only for now',
	'categories': [
						'file',
						'text',
						'diff',
						'differences',
				],
	'examples': [
						_.hp('p file + one two -or --c | p file-diff '),
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


def compare():
	global index
	matches = []
	missing = []
	paths = []
	index2 = {}
	for path in index:
		if not path in index2: index2[path] = {}
		for line in index[path]:
			index2[path][line.strip()] = 1
	for path in index:
		paths.append(path)
		for line in index[path]:
			# print(line)
			for pth in index:
				if pth == path: continue
				if line.strip() in index2[pth]:
					matches.append(line)
				else:
					missing.append(line)
				# print(line)
	_.pr('Missing',c='yellow')
	for line in missing:
		_.pr('\t',line)
	paths.reverse()
	matches = []
	missing = []
	paths = []
	for path in paths:
		paths.append(path)
		for line in index[path]:
			for pth in index:
				if pth == path: continue
				if line in index[pth]:
					matches.append(line)
				else:
					missing.append(line)
	_.pr('Added',c='yellow')
	for line in missing:
		_.pr('\t',line)

			# print(index[path][line],line)
		# _.isExit(__file__)
def action():
	global index
	index = {}
	for path in _.isData():
		# print(path)
		index[path] = {}
		for i,line in enumerate(_.getText2(path,'list')):
			line = line.rstrip()
			index[path][line] = i
	compare()
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);