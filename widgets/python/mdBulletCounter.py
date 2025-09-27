import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'TotalThreshold', '-t,-total' )
	_.switches.register( 'NestedThreshold', '-n,-nested' )
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



def safe_int(value, default=0):
	try:
		return int(value)
	except (TypeError, ValueError):
		return default



import os
import argparse

def count_markdown_dashes(filepath):
	top_level = 0
	nested = 0
	with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
		for line in f:
			stripped = line.lstrip()
			if stripped.startswith('-'):
				if len(line) - len(stripped) == 0:
					top_level += 1
				else:
					nested += 1
	return top_level, nested

def scan_markdown_files(thresh_total=None, thresh_nested=None):
	for root, dirs, files in os.walk('.'):
		for filename in files:
			if filename.endswith('.md'):
				path = os.path.join(root, filename)
				if not _.showLine(path):
					continue
				top, nest = count_markdown_dashes(path)
				total = top + nest
				if (
					(thresh_total is None or total >= thresh_total) and
					(thresh_nested is None or nest >= thresh_nested)
				):
					top = _.pr(top,c='green',p=0)
					nest = _.pr(nest,c='yellow',p=0)
					print(f'{path} — top-level: {top}, nested: {nest}, total: {total}')




def isDataScan(thresh_total=None, thresh_nested=None):
	for path in _.isData(2):
		if path.endswith('.md'):
			if not _.showLine(path):
				continue
			top, nest = count_markdown_dashes(path)
			total = top + nest
			if (
				(thresh_total is None or total >= thresh_total) and
				(thresh_nested is None or nest >= thresh_nested)
			):
				top = _.pr(top,c='green',p=0)
				nest = _.pr(nest,c='yellow',p=0)
				print(f'{path} — top-level: {top}, nested: {nest}, total: {total}')


if __name__ == '__main__':
	# parser = argparse.ArgumentParser(description='Scan Markdown files for "-" line counts.')
	# parser.add_argument('--thresh-total', type=int, help='Minimum total number of dash lines')
	# parser.add_argument('--thresh-nested', type=int, help='Minimum number of nested dash lines')
	# args = parser.parse_args()
	# TotalThreshold =  int(_.switches.value('TotalThreshold'))
	# NestedThreshold = int(_.switches.value('NestedThreshold'))


	TotalThreshold = safe_int(_.switches.value('TotalThreshold'))
	NestedThreshold = safe_int(_.switches.value('NestedThreshold'))

	# if not TotalThreshold:
	#     TotalThreshold = 0
	# if not NestedThreshold:
	#     NestedThreshold = 0
	scan_markdown_files(TotalThreshold, NestedThreshold)


def action():
	pass

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)