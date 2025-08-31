import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Divisible', '-d,-divisible', '3' )
	_.switches.register( 'Save', '-save', 'path' )
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

import calendar
from datetime import datetime

def is_current_month_days_divisible_by(divisor):
    today = datetime.now()
    current_year = today.year
    current_month = today.month
    days_in_month = calendar.monthrange(current_year, current_month)[1]
    return days_in_month % divisor == 0

def action():
	if _.switches.isActive('Divisible'):
		divisor = int(_.switches.value('Divisible'))
	else:
		divisor = 2
	if is_current_month_days_divisible_by(divisor):
		result = 'Yes'
		color = 'green'
	else:
		result = 'No'
		color = 'red'
	if _.switches.isActive('Save'):
		_.saveText(result, _.switches.value('Save'))
	else:
		_.pr(result,c=color)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)