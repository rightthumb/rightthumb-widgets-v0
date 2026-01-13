import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data,raw', description='Files', isRequired=False )
	_.switches.register( 'Table', '-t,-table' )
	_.switches.register( 'Index', '-i,-index' )
	_.switches.register( 'NoComments', '-nc' )
	_.switches.register( 'FirstBacktick', '-bt' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'isData.py',
	'description': 'Do things with _.isData(2)',
	'categories': [
						'data',
						'isData',
						'search',
						'tool',
						'utlity',
				],
	'examples': [
						_.hp('p isData -file file.txt + Search Contents'),
						_.hp('cat file | p isData + Search Piped Contents'),
						_.hp('p isData + Search Clipboard Contents'),
						_.hp('p isData'),
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

def action():

	# print(type(_.isData(2))); return None
	# print(_.isData(2)); return None

	data = _.isData(2)
	if type(data) == list:
		data = '\n'.join(data).strip()

	if _.switches.isActive('Table'):
		import json
		data = json.loads(data)
		_.pt(data)
		return None
	if _.switches.isActive('Index'):
		import json
		data = json.loads(data)
		if _.switches.values('Index'):
			for index in _.switches.values('Index'):
				if index in data:
					_.pr(data[index])
				else:
					_.pr(f"Index '{index}' not found in data.")
			return None
		



		if _.switches.isActive('Plus') or _.switches.isActive('Minus'):

			for key in data:
				if _.showLine(key+str(data[key])):
					_.pr(key +': '+ str(data[key]))
			return None
		
		_.pv(data)
		return None
	
	if _.switches.isActive('NoComments'):
		ext = _.EXT
		if _.switches.values('NoComments'):
			ext = _.switches.values('NoComments')[0]
		lang = __.Language(lang=ext)
		data = lang.noComments(data)
	data = data.split('\n')
		
	for line in data:
		if _.showLine(line):
			if _.switches.isActive('FirstBacktick'):
				line = FirstBacktick(line)
				if not line:
					continue
			_.pr(line)
			# return None

def FirstBacktick(line):
	if not '`' in line:
		return False
	return line.split('`')[1].strip() if '`' in line else line.strip()

########################################################################################
if __name__ == '__main__':

	action(); _.isExit(__file__)