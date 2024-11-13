import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Count', '-cnt', '20' )
	_.switches.register( 'Threshold', '-t,-th,-thresh,-threshold', '20' )
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

import os

def action():
	apps = {}
	for path in _.isData():
		path = path.strip()
		if not os.path.isfile(path): continue
		path = __.path(path)
		if not 'execution_receipt-' in path: continue
		part = path.split('execution_receipt-')[1]
		part = part.replace('-2','-1')
		app = part.split('-1')[0]
		if not app in apps:
			apps[app] = 0
		apps[app] += 1
	apps = sorted(apps.items(), key=lambda item: item[1], reverse=True)
	if apps:
		# first_item = apps[0]
		# last_item = apps[-1]
		# print("First item:", first_item)
		# print("Last item:", last_item)
		# print("Total:", len(apps))
		cnt = 0
		thresh = 0
		if _.switches.isActive('Count'): cnt = int(_.switches.value('Count'))
		if _.switches.isActive('Threshold'): thresh = int(_.switches.value('Threshold'))
		relevant = []
		for i, item in enumerate(apps):
			if not cnt == 0 and i > 20: break
			if not thresh == 0 and item[1] < thresh: break
			print(i, item)
			relevant.append(item[0])
		
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);