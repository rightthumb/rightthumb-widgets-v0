import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Field-List', '-list' )
	_.switches.register( 'Split', '-split', 'space' )
	_.switches.register( 'Index', '-i,-index' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	# _.switches.register( 'Save', '-save', 'index.json' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'json-list_to_index.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p json-list_to_index -f file.txt'),
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
	tables = []
	for path in _.isData():
		table = _.getTable2(path)
		for row in table: tables.append(row)
	if _.switches.isActive('Field-List'):
		for row in tables:
			for field in row:
				_.pr(field)
			_.isExit(__file__)
		return False
	index = None
	if _.switches.isActive('Index'):
		index = ' '.join(_.switches.values('Index'))
	# else:
	subject = None
	for row in tables:
		for field in row:
			if not index:
				index = field
			elif not field == index and subject == None:
				subject = field
		break
	indexed = {}
	for row in tables:
		if _.switches.isActive('Split'):
			split = ' '.join(_.switches.values('Split'))
			if split == 'space':
				split = ' '
			for s in row[index].split(split):
				indexed[s] = row[subject]
		else:
			indexed[row[index]] = row[subject]
	_.pv(indexed)
	# if _.switches.isActive('Save'): pass
	pass

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);