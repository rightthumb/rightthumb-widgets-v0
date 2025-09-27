import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
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
	index = {}
	dex = {}
	for line in _.isData(r=1):
		line = line.strip()
		line0 = line
		if not '?' in line: continue
		line1 = line.split('?')[1].split('&')[0]
		line2 = line.split('?')[1].split('&')[1]
		if not 'device' in line2:
			line = line1 + '&' + line2
		else:
			line = line1
		if not line in index: index[line] = 0
		if not line in dex: dex[line] = []
		dex[line].append(line0)
		index[line] += 1
	table = []
	if True:
		for line in dex:
			_.pr()
			lines = dex[line]
			lines.sort()
			_.pr(line,c='green')
			for li in lines:
				_.pr('',li,c='cyan')
	else:
		for line in index:
			# _.pr(index[line], line)
			table.append({ 'count': index[line], 'get': line })
		table = _.sort(table, 'count')
		_.pt(table)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);