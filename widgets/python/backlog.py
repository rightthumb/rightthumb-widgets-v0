import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'StartFrom', '-start', '25')
	_.switches.register( 'ClearSpent', '-spent', 'save'  )
	_.switches.register( 'ClearOmit', '-omit', 'save' )
	_.switches.register( 'Project', '-p,-project', 'subdomain audit' )
	_.switches.register( 'PythonDocumentation', '-py' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'backlog.py',
	'description': 'Iterate through fileBackup.json',
	'categories': [
						'fileBackup.json',
						'review',
						'research',
						'backup log',
				],
	'examples': [
						_.hp('p backlog -spent -omit + public_html\index.php'),
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


'''
'thisApp.py'
'Changes the world'
'DEFAULT'


'''

'''
5300 2025-04-10 20:50:41         1744332641.611327
D:\websites\domains\eyeformeta.com\public_html\apps\sms\index.php

p backlog - .bat -p init review
'''

py = _.dot()
py.name = 'thisApp.py'
py.description = 'Changes the world'
py.categories = "'DEFAULT',"
py.categories2 = "						'DEFAULT',"
py.examples = "_.hp('p thisApp -file file.txt'),"
py.examples2 = "						_.hp('p thisApp -file file.txt'),"
py.all = [
	py.name,
	py.description,
	py.categories,
	py.examples
]

def openFile(path):
	_open = _.regImp( __.appReg, 'file-open' )
	_open.switch('Backup','secure')
	_open.switch('Files',path); _open.action();

# possibly add a back feature and switch to while loop
def backup(path):
	appReg=__.appReg
	_bk = _.regImp( __.appReg, 'fileBackup' )
	# _bk.switch( 'Silent' )
	# _bk.switch( 'isPreOpen' )
	_bk.switch( 'Input', path )
	bkfi = _bk.action()
	__.appReg=appReg
def pyAsk(what):
	print()
	print()
	if what == 'name': return input('name: ')
	if what == 'description': return input('description: ')
	if what == 'categories':
		val = '0'
		values = []
		while val:
			val = input('category/tag 1: ')
			val = val.strip()
			if val:
				values.append(py.categories2.replace('DEFAULT',val))
		return '\n'+'\n'.join(values)+'\n'
	if what == 'examples':
		val = '0'
		values = []
		while val:
			val = input('usage example: ')
			val = val.strip()
			if val:
				values.append(py.examples2.replace('p thisApp -file file.txt',val))
		return '\n'+'\n'.join(values)+'\n'

def pythonDocumentation(rec):
	global backlog
	global backupFile
	path = rec['file']
	changed = False

	contents = _.getText(path,raw=True)
	if not "_.appInfo[focus()]" in contents: return True
	valid = True
	for test in py.all:
		if test in contents:
			valid = False
	if valid: return
	_.pr()
	_.pr('path:',path)
	_.pr()
	a = input('Add documentation?: ').lower().strip()
	if not 'o' in a:
		backlog['omit'].append(path)
		_.saveTable(backlog,backupFile)
	if not 'y' in a:
		return False
	
	openFile(path)

	if py.name in contents:
		val = pyAsk('name').strip()
		if val:
			contents = contents.replace(py.name,val)
			changed = True

	if py.description in contents:
		val = pyAsk('description').strip()
		if val:
			contents = contents.replace(py.description,val)
			changed = True

	if py.categories in contents:
		val = pyAsk('categories').strip()
		if val:
			contents = contents.replace(py.categories,val)
			changed = True

	if py.examples in contents:
		val = pyAsk('examples').strip()
		if val:
			contents = contents.replace(py.examples,val)
			changed = True

	if changed:
		backup(path)
		_.saveText(contents,path)
		_.pr('saved:',path)
		os.system('cls')
	return True

def action():
	global backlog
	global backupFile
	db='todo'
	if _.switches.isActive('Project'):
		db = '_'.join(_.switches.values('Project'))

	noteFile = f'backlog-{db}-notes.hash'
	backupFile = f'backlog-{db}.hash'

	backlog = _.getTable(backupFile)
	
	if not 'omit' in backlog: backlog['omit'] = []
	if not 'spent' in backlog: backlog['spent'] = []
	if not 'epochs' in backlog: backlog['epochs'] = {}
	if not 'start' in backlog['epochs']: backlog['epochs']['start'] = 0
	if not 'last' in backlog['epochs']: backlog['epochs']['last'] = 0

	if _.switches.isActive('PythonDocumentation'):
		backlog['omit'].append('D:\.rightthumb-widgets\widgets\python\_rightThumb\_base3\__init__.py')
	
	if _.switches.isActive('ClearSpent'):
		backlog['spent'] = []
		if 'save' in _.switches.values('ClearSpent'):
			_.saveTable(backlog,backupFile)

	if _.switches.isActive('ClearOmit'):
		backlog['omit'] = []
		if 'save' in _.switches.values('ClearOmit'):
			_.saveTable(backlog,backupFile)



	os.system('cls')
	bk = _.getTable('fileBackup.json')
	bk = _.sort(bk,'timestamp')
	
	bk.reverse()
	
	
	start = -1
	if _.switches.isActive('StartFrom'):
		start = int(_.switches.value('StartFrom'))
	notes = _.getTable(noteFile)
	if backlog['epochs']['last'] == 0:
		initSkip = True
	else:
		initSkip = False
	def addNote(x):
		if x == 'save' or x == 's':
			_.saveTable(backlog, backupFile)
			_.saveTable(notes, noteFile)
			x=''
		if x == '': return False
		if x == 'x': return False
		shouldOmit = True
		y = x.split(' ')
		for path in y:
			path = path.strip()
			if os.path.isfile(path) and os.sep in path:
				if path in notes:
					n = notes[path]['note']
				else:
					n=''
				shouldOmit = False
				note = {
					'file': path,
					'date': date,
					'note': input('note: '+n),
					'important': False
				}
				if '!!' in note['note']:
					note['note'] = note['note'].replace('!!','')
					note['important'] = True

				notes[path] = note
				_.saveTable(notes, noteFile)
				backlog['epochs']['last'] = timestamp
				if _.switches.isActive('ClearOmit') and not len(_.switches.value('ClearOmit') and not _.switches.isActive('Project')):
					pass
				else:
					_.saveTable(backlog, backupFile)
				addNote(input(': '))
		if x == '+':
			addNote(input(': '))
		return shouldOmit
	cnt = 0
	for i, rec in enumerate(bk):
		if _.switches.isActive('PythonDocumentation'):
			if not rec['file'].endswith('.py'): continue
			if rec['file'] in backlog['omit']: continue
			if pythonDocumentation(rec):
				pass
				# backlog['spent'].append(rec['file'])
				# _.saveTable(backlog, backupFile)
			continue
		if i < start: continue
		file = rec['file']
		if not os.path.isfile(file): continue
		if not _.showLine(file): continue
		if not _.showLine(file,'',backlog['omit']): continue
		if not _.validLine(file,None,backlog['omit']): continue
		timestamp = rec['timestamp']
		date = _.friendlyDate(timestamp)
		if not initSkip and timestamp < backlog['epochs']['last'] and not backlog['epochs']['last'] == 0:
			# _.pr('skipping:', file,c='red')
			initSkip = True
			continue
		if backlog['epochs']['start'] == 0:
			backlog['epochs']['start'] = timestamp
			if _.switches.isActive('ClearOmit') and not len(_.switches.value('ClearOmit') and not _.switches.isActive('Project')):
				pass
			else:
				_.saveTable(backlog, backupFile)
		if file in backlog['spent']: continue
		
		# _.saveTable(backlog, backupFile,p=0)
		if cnt % 5 == 0:
			x =input(': ')
			if x.strip():
				shouldOmit = addNote(x)
				if shouldOmit:
					print('omitting',x.strip())
					backlog['omit'].append(x.strip())
					_.pv(backlog['omit'])
					if _.switches.isActive('ClearOmit') and not len(_.switches.value('ClearOmit') and not _.switches.isActive('Project')):
						pass
					else:
						_.saveTable(backlog, backupFile)
					addNote(input(': '))
			os.system('cls')
				

		if file in backlog['spent']: continue
		_.pr(i, date,'\t',timestamp, c='cyan')
		_.pr(file, c='green')
		_.pr()
		if _.switches.isActive('ClearSpent') and not len(_.switches.value('ClearSpent') and not _.switches.isActive('Project')):
			pass
		else:
			backlog['spent'].append(file)
		cnt += 1
import os
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)