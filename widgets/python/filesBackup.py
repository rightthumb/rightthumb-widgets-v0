import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Force', '-force', isRequired=False )
	# _.switches.register( 'BypassScheduler', '-bs', isRequired=False )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
_._default_settings_(); __.setting('require-list',['Pipe','Files']);
_.appInfo[focus()] = {
	'file': 'filesBackup.py',
	'description': 'Backup files in bulk',
	'categories': [
						'backup',
						'bulk',
				],
	'examples': [
						_.hp('p files + *.md | p filesBackup'),
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
import os
def action():
	_bk = _.regImp( __.appReg, 'fileBackup' )
	_bk.switch( 'Silent' )
	if _.switches.isActive('Force'):
		_bk.switch( 'Force' )
	# if _.switches.isActive('BypassScheduler'):
	_bk.switch( 'BypassScheduler' )
	# myFileLocation_Files = _.isData()
	for path in _.isData():
		if _.showLine(path):
			path = path.strip()
			if not os.path.isfile(path): continue
			_.pr(__.path(path), c='cyan')
			bkfi = _bk.action(path)
			# _.pr(bkfi,c='darkcyan')



# _bk = _.regImp( __.appReg, 'fileBackup' )
# _bk.switch( 'Silent' )
# # _bk[path].switch( 'Input', path )
# bkfi = _bk.action(newFile)


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);