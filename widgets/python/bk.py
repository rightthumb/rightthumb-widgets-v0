import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Folder', '-fo,-folder','-bk, folderName' )
	_.switches.register( 'Label', '-l,-label','preChangeLabel' )
	_.switches.register( 'PathID', '-p,-md5,,-md5ID,-path,-pathID',' can be resolved to a path with:  | p resolveIDs' )
_._default_settings_()
__.setting('omit-switch-triggers',['Folder','Folders'])
__.setting('omit-functions',['myFolderLocations','aliasesFo'])
_.appInfo[focus()] = {
	'file': 'bk.py',
	'description': 'Copy files to specified folder (creates if needed). Default to current folder',
	'categories': [
						'backup',
						'copy files',
				],
	'examples': [
						_.hp('p bk -file file.txt'),
						_.hp('   bk/file.txt__bk__2024-12-21_1734823675.txt'),
						_.hp('p file -ago 1w | p bk -fo bk'),
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
	PathID = _.switches.isActive('PathID')
	import os
	folder = None
	if _.switches.isActive('Folder'):
		folder = _.switches.value('Folder')
	if folder == '-bk':
		folder = _v.wprofile+os.sep+'bk'
		PathID = True
	from shutil import copyfile
	for path in _.isData(r=0):
		if not os.path.isfile(path): continue
		if _.switches.isActive('Label'):
			backup = _.backupName(path,folder=folder,mkdir=True,label=' '.join(_.switches.values('Label')),md5=PathID)
		else:
			backup = _.backupName(path,folder=folder,mkdir=True,md5=PathID)
		# print(backup); return
		copyfile(path, backup)
		_.pr()
		_.pr(line=1,c='yellow')
		_.pr(path,c='green')
		_.pr(backup,c='cyan')
		_.pr(line=1,c='yellow')
		_.pr()

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);