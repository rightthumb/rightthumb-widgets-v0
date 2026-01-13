import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Replace', '-r,-replace' )
	_.switches.register( 'Strip', '-strip' )

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

def replace(line):
	global _r
	for i in range(0, len(_r), 2):
		old_text = _.ci(_r[i])
		new_text = _r[i + 1]
		line = line.replace(old_text, new_text)
	return line

_r = _.switches.values('Replace')
def action():
	_strip = _.switches.isActive('Strip')
	_replace = _.switches.isActive('Replace')
	for line in _.isData():
		line = line.replace('\n','')
		line = line.replace('\r','')
		if _strip: line = line.strip()
		if _replace: line = replace(line)
		_.pr(line)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);