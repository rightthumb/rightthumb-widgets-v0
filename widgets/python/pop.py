import sys
try:
	lines = sys.stdin.read().strip().split('\n')
except:
	lines = []
# Read from stdin and split into lines

# Example: print each line

import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register( 'Unique', '-u,-unique' )
	_.switches.register( 'Pop', '-p,-pop')
	_.switches.register( 'Search', '--s,-search')
	_.switches.register( 'Invert', '-i,-invert')
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	_.switches.register( 'SearchFiles', '-sf')
	_.switches.register( 'Clean', '--c' )
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
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

def action2():
	pop = [_v.slash]
	if _.switches.isActive('Pop'):
		pop = _.switches.values('Pop')
	global lines
	unique = _.switches.isActive('Unique')
	spent = []
	invert = _.switches.isActive('Invert')
	inverted = []
	search = _.switches.values('Search')
	og = []
	if _.isData():
		lines = _.isData()
	for line in lines:
		if _.showLine(line):
			og.append(line)
			for p in pop:
				if p in line:
					line = p.join(line.rsplit(p, 1)[:-1]).rstrip()
					inv = line
					if search:
						for s in search:
							if s.lower() in line.lower():
								x = []
								for k in line.split(p):
									x.append(k)
									if s.lower() in k.lower():
										break
			if unique:
				if line in spent:
					continue

			if line:
				if not invert:
					_.pr(line)
					spent.append(line)
			elif invert:
				_.pr(inv)
				spent.append(inv)




def action():
	cnt = 0
	pop = [_v.slash]
	if _.switches.isActive('Pop'):
		pop = _.switches.values('Pop')

	global lines
	unique = _.switches.isActive('Unique')
	invert = _.switches.isActive('Invert')
	search = _.switches.values('Search')
	SearchFiles = _.switches.isActive('SearchFiles')
	if _.switches.isActive('SearchFiles') and '0' in _.switches.value('SearchFiles'):
		SearchFilesZ = True
		SearchFiles = False
	else:
		SearchFilesZ = False
	# print(SearchFiles, SearchFilesZ)
	# return
	spent = []

	if _.isData():
		lines = _.isData()

	for line in lines:
		if not _.showLine(line):
			continue

		original = line
		modified = line

		for p in pop:
			if p in modified:
				parts = modified.split(p)
				matched = False
				if search:
					for i in reversed(range(len(parts))):
						if any(s.lower() in parts[i].lower() for s in search):
							modified = p.join(parts[:i+1])
							matched = True
							break
				if not matched:
					modified = p.join(parts[:-1])
				break  # use only the first pop delimiter

		if unique and modified in spent:
			continue

		if modified:
			if not invert:
				pr = True
				if original == modified:
					isOg = True
				else:
					isOg = False
				if SearchFilesZ and isOg:
					pr = False
				if SearchFiles and not isOg:
					pr = False
				if pr:
					cnt += 1
					_.pr(modified)
				spent.append(modified)
		elif invert:
			cnt += 1
			_.pr(original)
			spent.append(original)
	if _.switches.isActive('Clean'):
		return
	if cnt == 0:
		_.pr('No matches found',c='yellow')
		return
	if unique or SearchFiles or SearchFilesZ:
		_.pr('\n ',_.addComma(cnt), 'of ', _.addComma(len(lines)),'matches found',c='yellow')
	else:
		_.pr('\n ',_.addComma(cnt)+' matches found',c='yellow')




########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)