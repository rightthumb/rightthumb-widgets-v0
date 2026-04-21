import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'ToUpper', '-u,-upper')
	_.switches.register( 'NewLine', '-n,-l,-nl,-newline,-line,-new' )
	_.switches.register( 'KB', '-kb' )
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

def kb(item):
	index = _.getTable('kb.index')
	if item in index:
		return index[item]
	return False





def process(data):
	if type(data) == str:
		data = data.split('\n')
	spent = []
	table = []
	for line in data:
		if not line.strip():
			continue
		if not line in spent:
			spent.append(line)
			if _.switches.isActive('KB'):
				result =  kb(line.strip())
				if result:
					table.append( result )
			else:
				table.append(line)
	return table
def action():
	if _.switches.isActive('ToUpper'):
		if _.switches.isActive('NewLine'):
			result = '\n'.join(_.isData()).upper().replace(' ','\n').replace('\n\n','\n').replace(' ','')
			
			items = process(result)
			_.pr( '\n'.join(items) )
		else:
			_.pr( '\n'.join(_.isData()).upper() )
	else:
		for line in _.isData():
			good = True
			for c in line:
				if not c in ' ABCDEFGHIJKLMNOPQRSTUVWXYZ':
					good = False
			if good:
				_.pr(line)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);