import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	_.switches.register( 'Threshold', '-t,-threshold' )
	_.switches.register( 'Index', '-i,-index' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'composer_git.py',
	'description': 'Find source folder of composer and git and vendor folders',
	'categories': [
						'composer',
						'git',
						'vendor',
						'server',
						'admin',
				],
	'examples': [
						_.hp('cat composer_git.txt | p composer_git -i -t 400'),
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
	if _.switches.isActive('Threshold'):
		_threshold = int( _.switches.value('Threshold') )
	else:
		_threshold = 300
	spent = []
	v = '/vendor/'
	c = '/composer/'
	g = '/.git/'
	index = {}
	for line in _.isData(r=1):
		if v in line: line = line.split(c)[0]+v
		if c in line: line = line.split(c)[0]+c
		if g in line: line = line.split(g)[0]+g
		if not line in index: index[line] = 0
		index[line] += 1
		if line not in spent:
			spent.append(line)
			if not _.switches.isActive('Index'):
				_.pr(line)
	if _.switches.isActive('Index'):
		dex = {}
		table = []
		for i in index:
			if index[i] > _threshold:
				dex[i] = index[i]
				table.append({ 'folder': i, 'count': index[i] })
		table = sorted(table, key=lambda x: x['count'], reverse=True)

		index = {}
		for rec in table:
			index[rec['folder']] = rec['count']
		dex = index
		for p in dex:
			if dex[p] < 10: pre = '   '
			elif dex[p] < 100: pre = '  '
			elif dex[p] < 1000: pre = ' '
			elif dex[p] < 10000: pre = ''
			cnt = pre + str(dex[p])
			if _.showLine(p):
				print( _.pr(cnt,c='darkcyan',p=0) ,_.pr(p,c='cyan',p=0))
		# _.pv(dex)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);