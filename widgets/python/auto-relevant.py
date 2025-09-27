import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Ago', '-ago' )
	_.switches.register( 'Extensions', '-ext', 'py' )
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

import sys

def action():
	rel = {'index': {}}
	db = _.tables.returnSorted('backupLog', 'd.timestamp', _.getTable('fileBackup.json'))
	db.reverse()
	# spent = []
	for rec in db:
		rel['ago'] = 1
		rel['ext'] = 1
		if _.switches.isActive('Extensions'):
			rel['ext'] = 0
			for ext in _.switches.values('Extensions'):
				ext = ext.lower()
				if rec['file'].lower().endswith('.' + ext):
					rel['ext'] = 1
		if _.switches.isActive('Ago'):
			if rec['timestamp'] < _.switches.value('Ago'):
				rel['ago'] = 1
			else:
				break
		if rel['ago'] and rel['ext']:
			folder = __.path(rec['file'],pop=True)
			if  not folder == _v.home:
				if folder not in rel['index']:
					rel['index'][folder] = 0
				# if not rec['file'] in spent:
					# spent.append(rec['file'])
				rel['index'][folder] += 1

	rel['index'] = sorted(rel['index'].items(), key=lambda item: item[1], reverse=True)

	if rel['index']:
		first_item = rel['index'][0]
		last_item = rel['index'][-1]
		print("First item:", first_item)
		print("Last item:", last_item)
		print("Total:", len(rel['index']))
		cnt = 0
		thresh = 0
		if _.switches.isActive('Count'): cnt = int(_.switches.value('Count'))
		if _.switches.isActive('Threshold'): thresh = int(_.switches.value('Threshold'))
		rel['relevant'] = []
		for i, item in enumerate(rel['index']):
			if not cnt == 0 and i > 20: break
			if not thresh == 0 and item[1] < thresh: break
			print(i, item)
			rel['relevant'].append(item[0])
		_.saveText(rel['relevant'],'auto-relevant.list')
	else:
		print("No items to display.")


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);