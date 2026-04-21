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
	_.switches.register( 'First', '-first', 'C:\\WINDOWS\\System32 C:\\WINDOWS' )
	_.switches.register( 'Last', '-last', 'C:\\QMK_MSYS\\mingw64\\bin\\' )
	_.switches.register( 'Implode', '-i,-implode' )
	_.switches.register( 'onLoad', '-load' )
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
import os

def _norm(p: str) -> str:
	# Normalize for comparison: expand vars, strip quotes/space, remove trailing sep,
	# normpath + normcase (Windows = case-insensitive)
	if p is None:
		return ''
	p = p.strip().strip('"').strip("'")
	if not p:
		return ''
	p = os.path.expandvars(os.path.expanduser(p))
	# remove trailing separators without killing root "C:\"
	p = p.rstrip("\\/") or p
	p = os.path.normpath(p)
	p = os.path.normcase(p)
	return p

def _dedupe_preserve_order(paths):
	"""Return (dedup_list, present_map) where present_map[norm] = original casing string."""
	seen = set()
	out = []
	present_map = {}
	for p in paths:
		if not p:
			continue
		n = _norm(p)
		if not n:
			continue
		if n in seen:
			continue
		seen.add(n)
		out.append(p)
		# keep first-seen original presentation
		present_map.setdefault(n, p)
	return out, present_map

def End(paths, where='?'):
	# Pull desired First/Last from your switches
	first_in = _.switches.values('First') or []
	last_in  = _.switches.values('Last')  or []

	# Normalize the First/Last lists (keep their given order)
	first_norms = [_norm(p) for p in first_in if _norm(p)]
	last_norms  = [_norm(p) for p in last_in  if _norm(p)]
	first_set = set(first_norms)
	last_set  = set(last_norms)

	# Start from current PATH entries, deduped w/ original presentation preserved
	dedup_paths, present_map = _dedupe_preserve_order(paths)

	out = []
	seen = set()

	def _add(p: str):
		n = _norm(p)
		if not n or n in seen:
			return
		seen.add(n)
		# If we already had that normed path, use its original presentation,
		# otherwise use the string we were given (lets First/Last insert with their casing)
		out.append(present_map.get(n, p))

	# 1) Put all First items (in the order user supplied), even if not originally in PATH
	for p in first_in:
		_add(p)

	# 2) Add everything that is neither in First nor Last
	for p in dedup_paths:
		n = _norm(p)
		if n in first_set or n in last_set:
			continue
		_add(p)

	# 3) Put all Last items (in the order user supplied), even if not originally in PATH
	for p in last_in:
		_add(p)

	return out

def action():
	if _.switches.isActive('onLoad'):
		cur = os.environ.get('PATH', '').split(os.pathsep)
		new_paths = End(cur, where='onLoad')
		_.pr(f"# before={len(cur)} after={len(new_paths)}")
		_.pr(os.pathsep.join(new_paths))
		return


	if _.switches.isActive('Clean'):
		paths = os.environ['PATH'].split(os.pathsep)
		paths = End(paths,11)
		new = []
		for path in paths:
			path = path.strip()
			path = path.rstrip(os.sep)
			if not path in new and os.path.isdir(path):
				new.append(path)
		paths = new
		print(os.pathsep.join(End(paths,22)))
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

		for path in End(paths,33):
			path = path.strip()
			path = path.rstrip(os.sep)

			if not path in new and os.path.isdir(path):
				new.append(path)


	
		paths = new
		paths = End(paths,44)



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


		paths = End(paths,55)
		print(os.pathsep.join(End(paths,66)))
		return
	



	if _.switches.isActive('Prepend') or _.switches.isActive('Append'):
		_.switches.fieldSet('osPath','active',True)
	paths = []
	_paths = os.environ['PATH'].split(os.pathsep)
	_paths = End(_paths,777)
	for path in End(_paths,77):
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
		paths = End(paths,88)
	if _.switches.isActive('Append'):
		for path in _.switches.values('Append'):
			if not path in paths and os.path.isdir(path):
				paths.append(path)

	# paths = new
	paths = End(paths,99)
	if _.switches.isActive('osPath'):
		_.pr(os.pathsep.join(End(paths,100)))

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