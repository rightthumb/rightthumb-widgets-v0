import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'List-Aliases', '-l,-li,-list' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name' )
	_.switches.register( 'Alias', '-a,-alias','alias', 'if not Remove-File or Delete-Alias then it adds to the alias' )
	_.switches.register( 'Remove-File', '-r,-rem,-remove','uses _.isData (pipe or Files)' )
	_.switches.register( 'Delete-Alias', '-del','' )
	_.switches.register( 'Clean-Missing-Files', '-clean','' )
	_.switches.register( 'Alias-Alias', '-aa','-a FlexOps -aa fo   (an alias for the alias)' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'related.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p file --c + JsonDatabase | p related -a JsonDatabase'),
						_.hp('p related -a JsonDatabase -f JsonDatabase.py'),
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
	_.switches.trigger( 'Remove-File', _.isFile )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import os

def action():
	table = _.getTable('related.py.json')
	if not type(table) == dict: table = {}
	if not 'files' in table: table['files'] = {}
	if not 'aliases' in table: table['aliases'] = {}
	if not 'aliasAliases' in table: table['aliasAliases'] = {}

	if _.switches.isActive('List-Aliases'):
		for alias in table['aliases']:
			_.pr()
			_.pr(alias,c='yellow')
			# for path in table['aliases'][alias]:
			# 	_.pr('\t',path,c='cyan')
		return None

	if not _.switches.isActive('Alias') and not _.switches.isActive('Clean-Missing-Files'): _.e('Alias is required')

	alias = _.switches.value('Alias')

	if not alias in table['aliasAliases']:
		for a in table['aliasAliases']:
			if alias.lower() == a.lower():
				alias = a
				break

	if not alias in table['aliases']:
		for a in table['aliases']:
			if alias.lower() == a.lower():
				alias = a
				break

	
	if _.switches.isActive('Alias-Alias'):
		aliasAlias = _.switches.value('Alias-Alias')
		table['aliasAliases'][aliasAlias] = alias
		_.saveTable(table,'related.py.json')
		_.pr('Alias Alias Added:',aliasAlias,'=',alias)
		return None

	
	if not _.switches.isActive('Remove-File') and not _.switches.isActive('Delete-Alias') and not _.isData():
		_.pr()
		_.pr(alias,c='yellow')
		for path in table['aliases'][alias]:
			_.pr('\t',path,c='cyan')
		_.pr()
		return None


	actionTaken = False
	if _.isData() and not _.switches.isActive('Remove-File') and not _.switches.isActive('Delete-Alias'):
		for path in _.isData():
			path = _.isFile(path)
			if not os.path.isfile(path):
				_.pr('Error: File not found:',path,c='red')
				continue
			# _.pr('Adding:',path,c='green')
			if not alias in table['aliases']:
				table['aliases'][alias] = []
			if not path in table['aliases'][alias]:
				actionTaken = True
				table['aliases'][alias].append(path)
			if not path in table['files']:
				table['files'][path] = []
			if not alias in table['files'][path]:
				actionTaken = True
				table['files'][path].append(alias)
		if not actionTaken:
			_.pr('No Changes Made',c='red')
		else:
			_.pr()
			_.pr(alias,c='yellow')
			for path in table['aliases'][alias]:
				_.pr('\t',path,c='cyan')
			_.pr()
			_.saveTable(table,'related.py.json')
		return None
	


	if _.switches.isActive('Remove-File'):
		activity = {
			'Removed From Aliases': [],
			'Skipped From Aliases': [],
			'Removed From Path': [],
			'Skipped From Path': [],
		}


		activity['Removed From Aliases']
		activity['Skipped From Aliases']
		activity['Removed From Path']
		activity['Skipped From Path']
		activity['Bad File Path']


		if not _.isData(): _.e('Files is required')
		if not alias in table['aliases']:
			_.e('Error: Alias not found')
			return None
		for path in _.isData():
			if not os.path.isfile(path):
				activity['Bad File Path'].append(path)
				continue
			if not path in table['aliases'][alias]:
				activity['Skipped From Aliases'].append(path)
				_.pr('Error: Not in Relationship: Alias',c='red')
				continue
			actionTaken = True
			activity['Removed From Aliases'].append(path)
			table['aliases'][alias].pop(table['aliases'][alias].index(path))
			if not path in table['files']:
				activity['Skipped From Path'].append(path)
				_.pr('Error: File not found',c='red')
				continue
			if not alias in table['files'][path]:
				_.pr('Error: Not in Relationship: File',c='red')
				continue
			actionTaken = True
			activity['Removed From Path'].append(path)
			table['files'][path].pop(table['files'][path].index(alias))
		for key in activity:
			if activity[key]:
				_.pr(key,c='yellow')
				for item in activity[key]:
					_.pr('\t',item,c='cyan')
		if actionTaken:
			_.pr()
			_.saveTable(table,'related.py.json')
		return None
	


	if _.switches.isActive('Delete-Alias'):
		if not alias in table['aliases']:
			_.e('Error: Alias not found')
			return None
		_.pr()
		_.pr('Confirm:',c='yellow')
		related = table['aliases'][alias]
		for path in table['aliases'][alias]:
			_.pr('\t',path,c='red')
		ask = input('Delete Alias? (Y/n): ').lower()
		if ask == '': ask = 'y'
		if ask == 'y':
			actionTaken = True
			del table['aliases'][alias]

			for path in related:
				if not path in table['files']:
					_.pr('Error: File not found',c='Background.red')
				if not alias in table['files'][path]:
					_.pr('Error: Not in Relationship: File',c='Background.red')
				
				table['files'][path].pop(table['files'][path].index(alias))
		if actionTaken:
			_.saveTable(table,'related.py.json')
		else:
			_.pr('No Changes Made',c='red')
		return None

	if _.switches.isActive('Clean-Missing-Files'):
		activity = {
			'aliases': {},
			'files': [],
		}

		activity['aliases']
		activity['files']

		for alias in table['aliases']:
			for path in table['aliases'][alias]:
				if not os.path.isfile(path):
					_.pr('Error: File not found:',path,c='red')
					if not alias in activity['aliases']:
						activity['aliases'][alias] = []
					activity['aliases'][alias].append(path)
					if not path in activity['files']:
						activity['files'].append(path)
					table['aliases'][alias].pop(table['aliases'][alias].index(path))
					actionTaken = True
					if alias in table['files'][path]:
						actionTaken = True
						if not path in activity['files']:
							activity['files'].append(path)
						table['files'][path].pop(table['files'][path].index(alias))
		if activity['aliases']:
			_.pr()
			for alias in activity['aliases']:
				_.pr(alias,c='yellow')
				for path in activity['aliases'][alias]:
					_.pr('\t',path,c='red')
			_.pr()

			_.saveTable(table,'related.py.json')
		else:
			_.pr('No Changes Made',c='red')
		return None
		
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)