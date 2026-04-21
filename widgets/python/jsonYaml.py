import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'json', '-json' )
	_.switches.register( 'yaml', '-yaml,-yml' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'jsonYaml.py',
	'description': 'Convert between JSON and YAML and prints for > save',
	'categories': [
						'convert',
						'json',
						'yaml',
				],
	'examples': [
						_.hp('p jsonYaml -json file.json'),
						_.hp('p jsonYaml -yaml file.yaml'),
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

import json
import yaml

def action():

	if _.switches.isActive('json'):
		data = _.getTable2( _.switches.value('json') )
		print( json.dumps(data, indent=4) )
	if _.switches.isActive('yaml'):
		data = _.getText( _.switches.value('yaml'),raw=True,clean=1)
		data = yaml.safe_load(data)
		print(data)
		# print( json.dumps(data, indent=4) )

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)