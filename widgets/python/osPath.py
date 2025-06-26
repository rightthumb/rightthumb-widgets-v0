import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'osPath', '-path,-osPath','', isRequired=False )
	_.switches.register( 'Prepend', '-p,-pre,-prepend','', isRequired=False )
	_.switches.register( 'Append', '-a,-post,-append','', isRequired=False )
	_.switches.register( 'AltRepoTempPathSuspention', '-repo','pre | post', isRequired=False )
	_.switches.register( 'Clean', '-clean' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'osPath.py',
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

import sys
import os

def action():
	if _.switches.isActive('Clean'):
		paths = os.environ['PATH'].split(os.pathsep)
		new = []
		for path in paths:
			path = path.strip()
			path = path.rstrip(os.sep)
			if not path in new and os.path.isdir(path):
				new.append(path)
		paths = new
		print(os.pathsep.join(paths))
		return
	
	

	if _.switches.isActive('AltRepoTempPathSuspention'):
		global suspend_for_alt_git_repos
		relevant = []
		for path in suspend_for_alt_git_repos:
			path = path.strip()
			path = path.replace('/',os.sep)
			if path:
				path = _v.resolveFolderIDs(path)
				relevant.append(path)
				# print(path)


		action = _.switches.value('AltRepoTempPathSuspention')
		if not action in ['pre','post']:
			_.pr('Invalid action. Use "pre" or "post".',c='red')
			return



		paths = os.environ['PATH'].split(os.pathsep)
		new = []
		for path in paths:
			path = path.strip()
			path = path.rstrip(os.sep)
			if not path in new and os.path.isdir(path):
				new.append(path)
		paths = new



		new = []
		if action == 'pre':
			for path in paths:
				if not path in relevant:
					new.append(path)
			paths = new
			


		if action == 'post':
			for path in relevant:
				if not path in paths and os.path.isdir(path):
					paths.append(path)



		print(os.pathsep.join(paths))
		return
	



	if _.switches.isActive('Prepend') or _.switches.isActive('Append'):
		_.switches.fieldSet('osPath','active',True)
	paths = []
	for path in os.environ['PATH'].split(os.pathsep):
		path = path.strip()
		if path and _.showLine(path):
			if not path in paths and os.path.isdir(path):
				paths.append(path)
				if not _.switches.isActive('osPath'):
					_.pr(path)
	if _.switches.isActive('Prepend'):
		_paths = _.switches.values('Prepend')
		_paths.reverse()
		for path in _paths:
			if not path in paths and os.path.isdir(path):
				paths.insert(0,path)
	if _.switches.isActive('Append'):
		for path in _.switches.values('Append'):
			if not path in paths and os.path.isdir(path):
				paths.append(path)
	if _.switches.isActive('osPath'):
		_.pr(os.pathsep.join(paths))

# _v.sanitizeFolder(path)
# _v.resolveFolderIDs(path)
suspend_for_alt_git_repos = '''
C:/QMK_MSYS/mingw64/bin
C:/ProgramData/mingw64/mingw64/bin
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/batch
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/bin/Win
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/curl
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/exe
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/File_Metadata
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/platform-tools
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/sqlite3
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/SysinternalsSuite
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/antiword-0_37-windows/antiword
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/ChromeDriver/109.0.5414.25
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/ChromeDriver/114.0.5735.90
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/ChromeDriver/134.0.6998.90
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/ChromeDriver/2.46
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/ChromeDriver/73.0.3683.68
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/ChromeDriver/74.0.3729.6
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/ChromeDriver/75.0.3770.90
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/ChromeDriver/76.0.3809.25
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/ChromeDriver/80.0.3987.16
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/cwrsync_6.3.1_x64/bin
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/exe/gecko/0.24.0
{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/python
{A8693D4B-8A80-898F-83F0-E806D2F36800}
'''.strip().split('\n')



########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)