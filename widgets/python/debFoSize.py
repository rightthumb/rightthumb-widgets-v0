import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'debFoSize.py',
	'description': 'Get size of all folders in a directory',
	'categories': [
						'folder',
						'size',
				],
	'examples': [
						_.hp('p debFoSize'),
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

def execute_and_return(command):
	try:
		result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
		return result.stdout
	except subprocess.CalledProcessError as e:
		return e.stderr


import subprocess
import os
folders = []
def isFo(path):
	global folders
	if os.path.isdir(path):
		folders.append(path)

def process(path):
	global table
	base = os.getcwd()+'/'
	fo = path.replace(base,'')
	if _.showLine(fo):
		result = execute_and_return('du -b "'+path+'"')
		result = result.split(' ')[0]
		result = result.split('\t')[0]
		size = _.formatSize(int(result))
		table.append({'size': size, 'bytes': int(result), 'folder': fo})
	# _.pr(result,path.replace(base,''),c='cyan')
def action():
	global table
	global folders
	table=[]
	_.fo(script=isFo)
	for path in folders:
		process(path)
	_.pt(table,'size,folder',sort='bytes')
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);