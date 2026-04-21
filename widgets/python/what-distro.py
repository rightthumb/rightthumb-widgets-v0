import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
_._default_settings_()


_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ))
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

import platform
import distro

def identify_linux_distro():
	try:
		# Get the Linux distribution information using the distro module
		distro_info = distro.linux_distribution(full_distribution_name=False)
		return f"Linux Distribution: {distro_info[0]}, Version: {distro_info[1]}, Codename: {distro_info[2]}"
	except Exception as e:
		return f"An error occurred: {e}"
		return platform.system()

		


def action():
	result = identify_linux_distro()
	print(result)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);