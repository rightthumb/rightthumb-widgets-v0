import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
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
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def action():
	if _.switches.isActive('Files'):
		cnt=0
		for path in _.switches.values('Files'):
			path = __.path(path)
			new = float('inf')
			old = float('-inf')
			newest = None
			oldest = None
			db = _.getTable('fileBackup.json')
			for rec in db:
				if rec['file'] != path:
					continue
				cnt += 1
				if rec['timestamp'] < new:
					new = rec['timestamp']
					oldest = rec
				if rec['timestamp'] > old:
					old = rec['timestamp']
					newest = rec
			_.pr()
			_.pr(' Last:', _.friendlyDate(newest['timestamp']),newest['backup'] ,c='cyan')
			_.pr('First:', _.friendlyDate(oldest['timestamp']),oldest['backup'],c='darkcyan')
			_.pr()
			_.pr('',_.addComma(cnt),'backups',c='yellow')
			_.pr()


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);