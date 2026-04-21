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
	quote = "'"
	quote = '"'
	temp = 'debe7e352856'
	lines = '\n'.join(_.isData(r=1))
	lines = lines.replace('\\'+quote,temp)
	items = _.isData(r=1)
	last = items[-1]
	items.pop()
	lines = []
	for i,line in enumerate(items):
		line = line.rstrip()
		line += '\\'
		lines.append(line)
	lines.append(last)
	lines = '\n'.join(lines)
	lines = lines.replace(quote,'\\'+quote)
	lines = lines.replace(temp,'\\'+quote)
	_.pr(quote+lines+quote)
	
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);