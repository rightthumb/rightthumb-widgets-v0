import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'ID', '-i,-id','' )
	_.switches.register( 'Name', '-n,-name','' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'id.py',
	'description': 'Register strings to resolve in `cmd | p resolveIDs`',
	'categories': [
						'idResolution.json',
				],
	'examples': [
						_.hp('p id -id name'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=False )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

def findID(index, name):
	for rec in index:
		if rec['id'] == name:
			return rec['id']
	return None

def action():
	# print(_.switches.all()); _.isExit(__file__)
	# print(_.switches.values('ID'),_.switches.values('Name'))
	# return True
	index = _.getTable('idResolution.json')
	# _.pv(index); _.isExit(__file__)
	if _.switches.isActive('ID') and not _.switches.isActive('Name'):
		name = findID(index, _.switches.value('ID'))
		if name:
			_.pr( name, c='yellow' )
		else:
			_.pr('ID not found: ' + _.switches.value('ID'), c='red')
		return None
	if not _.switches.isActive('Name'):
		_.pr('Missing required switch','-id','-id -name')
		return None
	index.append({'id': _.switches.value('ID'), 'name': _.switches.value('Name')})
	_.saveTable(index,'idResolution.json',printThis=True)
	

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)