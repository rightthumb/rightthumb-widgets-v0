import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Key', '-k,-key', 'id' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Save', '-save' )
	_.switches.register( 'Epoch', '-e,-epoch,-ts,-timestamp' )
	_.switches.register( 'DictNotList', '-dict' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p JSON-Merge -f indexTable_drives-{A4123F2B-27F9-4DED-8EC5-CEFF4FB19D66}.json indexTable_drives-{E53040AA-2DBD-44D2-9538-8B96AE67D0B4}.json -epoch timestamp'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
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
	if _.switches.isActive('Key'):
		key = _.switches.value('Key')
	else:
		key = 'id'
	if _.switches.isActive('Epoch'):
		epoch = _.switches.value('Epoch')
	else:
		epoch = False
	payload = []
	records = {}
	latest = {}
	if not _.switches.isActive('DictNotList'):
		test = _.getTable2(_.isData(r=1)[0])
		if not type(test) == list:
			_.switches.fieldSet('DictNotList',True)
	if not _.switches.isActive('DictNotList'):
		if not epoch:
			for path in _.isData(r=1):
				db = _.getTable2(path)
				for x in db:
					if not any(y[key] == x[key] for y in payload):
						payload.append(x)
		elif epoch:
			for path in _.isData(r=1):
				db = _.getTable2(path)
				for x in db:
					if not x[key] in records: records[x[key]] = { 'epoch': 0, 'record': None }
					if records[x[key]]['epoch'] < x[epoch]:
						records[x[key]]['epoch'] = x[epoch]
						records[x[key]]['record'] = x
			for z in records:
				payload.append(records[z]['record'])
	if _.switches.isActive('DictNotList'):
		payload = {}
		if not epoch:
			for path in _.isData(r=1):
				db = _.getTable2(path)
				for x in db: payload[x] = db[x]
		elif epoch:
			for path in _.isData(r=1):
				db = _.getTable2(path)
				for x in db:
					if not x[key] in records: records[x] = { 'epoch': 0, 'record': None }
					if records[x]['epoch'] < db[x][epoch]:
						records[x]['epoch'] = db[x][epoch]
						records[x]['record'] = db[x]
			for z in records:
				payload[z] = records[z]['record']
	if _.switches.isActive('Save'):
		_.saveTable2(payload, _.switches.values('Save')[0])
	else:
		_.pv(payload)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);