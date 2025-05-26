import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Recursive', '-r' )
	_.switches.register( 'Recover', '-recover', isData='name' )
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );

def action():
	import os
	Recursion = _.switches.isActive('Recursive')
	Folder = os.getcwd() + os.sep
	spent = []
	Recover = _.switches.isActive('Recover')
	Recovered = {}
	RecoverThis = []
	RecoverRecords = []
	if Recover:
		RecoverThis = _.isData()
		for i,rt in enumerate(RecoverThis):
			# RecoverThis[i] = RecoverThis[i].strip()
			if not Folder in rt:
				RecoverThis[i] = Folder+rt
	for rec in _.getTable('fileBackup.json'):
		fo = os.path.dirname(rec['file']) + os.sep
		if rec['file'] in spent: continue
		if Recover and rec['file'] in RecoverThis:
			RecoverRecords.append(rec)
			# Recovered[_.friendlyDate(rec['timestamp'])] = rec['backup']
			if not rec['file'] in Recovered:
				Recovered[rec['file']] = {
					'epoch': 0,
					'record': rec
				}
			if rec['timestamp'] > Recovered[rec['file']]['epoch']:
				Recovered[rec['file']]['epoch'] = rec['timestamp']
				Recovered[rec['file']]['record'] = rec

		if Folder in fo:
			if Recursion:
				_.pr(rec['file'].replace(Folder,''),c='cyan')
				# _.pr(rec['file'],c='cyan')
				spent.append(rec['file'])
			elif Folder == fo:
				_.pr(rec['file'].replace(Folder,''),c='cyan')
				# _.pr(rec['file'],c='cyan')
				spent.append(rec['file'])
	if Recovered:
		_.pv(RecoverRecords)
		for path in Recovered:
			_.pr('Recovered:',Recovered[path]['record']['backup'])
			copyfile(Recovered[path]['record']['backup'],path)


from shutil import copyfile
if __name__ == '__main__':
	action(); _.isExit(__file__);