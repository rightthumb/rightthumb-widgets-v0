import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'NotSingle', '-ns' )
	_.switches.register( 'Count', '-cnt', '2' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'dot-skim.py',
	'description': 'skim my 100+ domain trees and many domains',
	'categories': [
						'domain tree skimmer',
						'tld-skimmer',
						'tld',
						'.',
						'dot',
						'single dot',
				],
	'examples': [
						_.hp('cat domains.txt | p dot-skim'),
						_.hp('cat domains.txt | p dot-skim -ns'),
						_.hp(''),
						_.hp('load'),
						_.hp('domains | p dot-skim'),
						_.hp('domains | p dot-skim -ns'),
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
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

_copy = _.regImp( __.appReg, '-copy' )

def action():
	cnt = 1
	if _.switches.isActive('Count'):
		cnt = int(_.switches.value('Count'))
	results = []
	if not _.switches.isActive('NotSingle'):
		for line in _.myData():
			line= line.strip()
			if '.' in line and line.count('.') == cnt:
				results.append(line)
	elif _.switches.isActive('NotSingle'):
		for line in _.myData():
			line= line.strip()
			if '.' in line and line.count('.') > cnt:
				results.append(line)
	if _.isGui():
		_copy.imp.copy( '\n'.join(results) )
	else:
		_.pr( '\n'.join(results) )


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);