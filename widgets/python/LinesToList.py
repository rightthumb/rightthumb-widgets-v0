import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Indent', '-i,-indent', '' )
	_.switches.register( 'Copy', '--,-cp,-copy', '' )
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
	lines = _.isData()
	output = []
	for line in lines:
		line = line.strip()
		# line = line.replace('\n','')
		# line = line.replace('\r','')
		# line = line.replace('\t','')
		if line != '':
			output.append(line)
	if _.switches.isActive('Indent'):
		json=simplejson.dumps(output, indent=4, default=str)
	else:
		json=simplejson.dumps(output, default=str)
	print(output)
	# _.pr(output)
	if _.switches.isActive('Copy'):
		_copy = _.regImp( __.appReg, '-copy' )
		_copy.imp.copy( output, p=False  )
import simplejson

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);