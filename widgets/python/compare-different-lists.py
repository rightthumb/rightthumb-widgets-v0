import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'FileOne', '-f1' )
	_.switches.register( 'FileTwo', '-f2' )
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

def lists(one,two):
	one = one.split('\n')
	two = two.split('\n')
	_.pr('not in two', c='yellow')
	for i, line in enumerate(one):
		if line not in two:
			_.pr(line,c='cyan')
	_.pr('',len(one))
	_.pr(line=1)
	_.pr('not in one', c='yellow')
	for i, line in enumerate(two):
		if line not in one:
			_.pr(line,c='darkcyan')
			# print('two',i,line)
	_.pr('',len(two))

def action():
	one = _.getText(_.switches.value('FileOne'),raw=True,clean=2)
	two = _.getText(_.switches.value('FileTwo'),raw=True,clean=2)
	lists(one,two)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);