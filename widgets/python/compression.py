import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Status', '-is','', isRequired=False )
	_.switches.register( 'Encrypt', '-en','', isRequired=False )
	_.switches.register( 'Decrypt', '-de','', isRequired=False )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
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
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	pass
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

import os



def action():

	if _.switches.isActive('Status'):
		for path in _.isData():
			path = path.strip()
			if not os.path.isfile(path): continue
			if _.IS(path,'gzip'):
				_.pr('gzipped:',path,c='red')
			else:
				_.pr('not gzipped:',path,c='green')
		return None
	if len(_.isData()) == 1 and not _.switches.isActive('Encrypt') and not _.switches.isActive('Decrypt'):
		for path in _.isData():
			path = path.strip()
			if not os.path.isfile(path): continue
			if _.IS(path,'gzip'):
				_.decompress(path)
			else:
				_.compress(path)	

	elif _.switches.isActive('Encrypt'):
		for path in _.isData():
			path = path.strip()
			if not os.path.isfile(path): continue
			_.compress(path)
	elif _.switches.isActive('Decrypt'):
		for path in _.isData():
			path = path.strip()
			if not os.path.isfile(path): continue
			_.decompress(path)
	else:
		_.e('action not specified','-en or -de')

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);