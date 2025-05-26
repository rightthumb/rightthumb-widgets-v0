import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Clean', '--c' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'totalInt.py',
	'description': 'Calculate total int from pipe data',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p dirDB -db C_Drive.db + C:\vmware\ | p ls -c bytes | p totalInt'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


import re

def clean_and_convert(number_str):
	# Remove all characters except digits and decimal points
	cleaned_str = re.sub(r'[^0-9.]', '', number_str)
	
	# Convert to float if there's a decimal, otherwise to int
	if '.' in cleaned_str:
		return float(cleaned_str)
	elif cleaned_str.isdigit():  # Ensure the result is a number
		return int(cleaned_str)
	else:
		raise ValueError("No valid numeric value found.")



def action():
	total = 0
	for line in _.isData(r=0):
		try:
			total += clean_and_convert(line)
		except ValueError:
			pass
	if _.switches.isActive('Clean'):
		_.pr(total)
	else:
		_.pr(_.addComma(total))

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);