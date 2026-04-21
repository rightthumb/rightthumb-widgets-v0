import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Name', '-n,-name','variable name' )
	_.switches.register( 'Value', '-v,-value','variable value', isData='name' )
	_.switches.register( 'isList', '-list','keeps a list if piped or pasted via --pa', isData='name' )
	_.switches.register( 'Download', '-d,-dl','download', isData='name' )
	_.switches.register( 'Delete', '-delete', isData='name' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'stack.py',
	'description': 'Registered variables',
	'categories': [
						'variables',
						'registered',
						'stack',
				],
	'examples': [
						_.hp('p stack -name test -value 1234'),
						_.hp('p stack -n test -v 1234'),
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
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import sys
import simplejson as json # type: ignore

def action():
	name = None
	if _.switches.isActive('Download'):
		Json = _.URL( _v.fig['stack']+'load.php',{'api':_v.fig['stack-api']})
		if not Json.strip():
			_.pr('No stack found')
			sys.exit(0)
		stack = json.loads(Json)
		_.saveTableDB(stack, 'stack.dex')
		# print(Json)
	stack = _.getTableDB('stack.dex')
	if not stack:
		Json = _.URL( _v.fig['stack']+'load.php',{'api':_v.fig['stack-api']})
		if not Json.strip():
			_.pr('No stack found')
			sys.exit(0)
		stack = json.loads(Json)

	# print(type(stack),stack)
	value = None
	if _.switches.isActive('Name'):
		name = _.switches.value('Name')
	if _.switches.isActive('Delet'):
		if name is None:
			name = _.switches.value('Delete')
		if not name in stack:
			Json = _.URL( _v.fig['stack']+'load.php',{'api':_v.fig['stack-api']})
			if not Json.strip():
				_.pr('No stack found')
				sys.exit(0)
			stack = json.loads(Json)
		if not name in stack:
			_.pr('Variable not found: {}'.format(name))
			sys.exit(0)
		ask = input('Are you sure you want to delete {}? (y/n)'.format(name))
		if ask == 'y':
			del stack[name]
			_.saveTableDB(stack, 'stack.dex')
			x = _.URL( _v.fig['stack']+'save.php',{'stack':json.dumps(stack),'api':_v.fig['stack-api']})
	if _.switches.isActive('Value') or _.isData():
		if _.switches.isActive('isList'):
			value = _.isData()
		else:
			value = ' '.join(_.isData())
		Json = _.URL( _v.fig['stack']+'load.php',{'api':_v.fig['stack-api']})
		stack = json.loads(Json)
		stack[name] = value
		_.saveTableDB(stack, 'stack.dex')
		x = _.URL( _v.fig['stack']+'save.php',{'stack':json.dumps(stack),'api':_v.fig['stack-api']})
		print(x)
		_.pr('Saved: {}'.format(name),c='yellow')
	else:
		if name is None:
			_.pv(stack)
			return None
		if name in stack:
			value = stack[name]
			if type(value) == list:
				for x in value:
					if _.showLine(x):
						_.pr(x,c='cyan')
			else:
				_.pr(value,c='cyan')
		else:
			_.pr('Variable not found: {}'.format(name))
			sys.exit(0)



########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)