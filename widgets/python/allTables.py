import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'inFiles', '-in' )
	_.switches.register( 'DB', '-db' )

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
	# _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

__.allTables = {}
__.allTables['getTable'] = {}
__.allTables['getTable2'] = {}
__.allTables['getTableDB'] = {}
__.threads = _.ThreadManager()
  # ak = args, kwargs
def script(path):
	if path.endswith('.py'):
		def myScript(path):
			# _.pr(__.relative)
			lines = _.getText(path)
			content = '\n'.join(lines)
			if '_.getTable' in content:
				for line in lines:
					if '_.getTable(' in line:
						file = line.split('_.getTable(')[1].split(')')[0].strip("'").strip().strip("'")
						if '.' in file:
							if not __.relative in __.allTables['getTable']:
								__.allTables['getTable'][__.relative] = []
							if '_.switches' in file: file += ')'
							__.allTables['getTable'][__.relative].append(file)
					if '_.getTable2(' in line:
						file = line.split('_.getTable2(')[1].split(')')[0].strip("'").strip().strip("'")
						if '.' in file:
							if not __.relative in __.allTables['getTable']:
								__.allTables['getTable2'][__.relative] = []
							if '_.switches' in file: file += ')'
							__.allTables['getTable2'][__.relative].append(file)
					if '_.getTableDB(' in line:
						file = line.split('_.getTableDB(')[1].split(')')[0].strip("'").strip().strip("'")
						if '.' in file:
							if not __.relative in __.allTables['getTable']:
								__.allTables['getTableDB'][__.relative] = []
							if '_.switches' in file: file += ')'
							__.allTables['getTableDB'][__.relative].append(file)

		__.threads.queue(myScript,  ak=(path,), label=path)
			
import simplejson
def action():
	files = _.fo(_v.py,script=script)
	if _.switches.isActive('inFiles'):
		json = simplejson.dumps(__.allTables, indent=4, sort_keys=True)
		_.pr(json.replace('"',''))
	else:
		for key in __.allTables:
			_.pr(line=True,c='green')
			_.pr(key,c='yellow')
			tables = []
			for path in __.allTables[key]:
				for table in __.allTables[key][path]:
					table = table.strip()
					if not table in tables:
						tables.append(table)
			tables.sort()
			for table in tables:
				_.pr('\t',table)





########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)