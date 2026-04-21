import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'InSameLine', '-line' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'PrintLine', '-print' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'BoolSearch.py',
	'description': 'Used in batch files or anytime a boolean result search is needed',
	'categories': [
						'Script Helper',
						'Batch Files',
						'.bat',
				],
	'examples': [
						_.hp('Example from wifi.bat to search wifi passwords:'),
						_.hp('\t call p. BoolSearch -f "%tmpf%" + Profile Password -line > "%tmpf%-BoolSearch"'),
						_.hp('\t set /p PasswordDataValid= < "%tmpf%-BoolSearch"'),
						_.hp('\t if [%PasswordDataValid%]==[False] (call p. DisplayError -title PowerShell Scripts Not Enabled -message To Fix Run -bullets "wifi enable" & goto:end)'),
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
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def action():
	if _.switches.isActive('PrintLine') and not _.switches.isActive('InSameLine'):
		_.switches.fieldSet('InSameLine','active',True)

	if _.switches.isActive('Files'):
		data = ''
		for file in _.switches.values('Files'):
			data += _.getText(file,raw=True)+'\n'
	else:
		data = '\n'.join(_.isData(r=0))

	if not _.switches.isActive('InSameLine'):
		print(_.showLine(data))
	else:
		for line in data.split('\n'):
			if _.showLine(line):
				if _.switches.isActive('PrintLine'):
					print(line)
				else:
					print('True')
				return None
		print('False')
	# print(_.showLine(data),data)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);