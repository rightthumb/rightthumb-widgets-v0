import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	
	_.switches.register('Folder', '-fo,-folder')
	_.switches.register('Recursive', '-r,-recursive')

	_.switches.register('Path', '-p,-path', 'callables variables all') 

	_.switches.register('Class', '-class')
	_.switches.register('Tabs', '-t,-tabs')
	_.switches.register('Spaces', '-sp,-spaces,-print,-printable')
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


__.setting('omit-switch-triggers',['Folder'])


_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


import re

# from _rightThumb._base3.library.tools.classes.code.PythonCodeColorizer import PythonCodeColorizer


iFnPath='from iPath import iName'
iFnPath='from iPath import'
iFn='''
def iName(*args, **kwargs):
	if not 'iName' in intelligent_code.functions:
		from iPath import iName
		intelligent_code.functions['iName'] = iName
	return intelligent_code.functions['iName'](*args, **kwargs)
'''.strip().replace('    ', '\t')

iClassPath='from iPath import iName'
iClassPath='from iPath import'
iClass='''
class iName:
	def __new__(cls, *args, **kwargs):
		if not 'iName' in intelligent_code.classes:
			from iPath import iName as live
			intelligent_code.classes['iName'] = live
		return intelligent_code.classes['iName'](*args, **kwargs)
'''.strip().replace('    ', '\t')


import os
# from _rightThumb._base3.library.classes.index import index as live
# from _rightThumb._base3.library.functions.create_backup_filename import create_backup_filename
def action():
	# colorizer = PythonCodeColorizer()
	# print(colorizer.colorize(sample_code))
	files = []

	if _.isData():
		files = _.isData()
	else:
		folder = os.getcwd()
		if _.switches.isActive('Folder'):
			folder = _.switches.value('Folder')
		if not folder: folder = os.getcwd()
		files = _.fo(folder,r=_.switches.isActive('Recursive'))


	global iFn
	global iFnPath
	global iClass
	global iClassPath
	isData = []
	for path in files:
		# print(path)
		# continue
		if not os.path.isfile(path): continue
		if not _.showLine(path): continue
		if '__pycache__' in path: continue
		if os.sep+'backup'+os.sep in path: continue
		isData.append(path)

	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	for path in isData:
		path = __.path(path)
		
		if len(isData) > 1: _.pr(path,c='green')
		if len(isData) > 1:
			_.pr()
			_.pr(line=1)
		# try:



	
		relevant = []
		parts = path.split(os.sep)
		active = False
		for part in parts:
			if part == '_rightThumb':
				active = True
			if active:
				relevant.append(part)
		iPath = '.'.join(relevant)
		iPath = iPath[0:len(iPath)-len('.py')]
		isClass = False
		
		if 'library.classes' in iPath:
			isClass = True
		iName = relevant[-1].replace('.py','')
		iName = iName[0:len(iPath)-len('.py')]
		if isClass or _.switches.isActive('Class'):
			iCode = iClass
			impPath = iClassPath.replace('iPath',iPath).replace('iName',iName)
		else:
			iCode = iFn
			impPath = iFnPath.replace('iPath',iPath).replace('iName',iName)
		
		if '.__init__ import __init__' in impPath:
			impPath = impPath.replace('.__init__ import __init__', ' as _')
			impPath = impPath.replace('from ', 'import ')
		iCode = iCode.replace('iPath',iPath)
		iCode = iCode.replace('iName',iName)

		
		if _.switches.isActive('Tabs'):
			iCode = iCode.replace('    ', '\t')
		
		if _.switches.isActive('Spaces')  or  len(isData) > 1:
			iCode = iCode.replace('\t', '    ')
		
		# colorized = colorizer.colorize(iCode)
		
		if _.switches.isActive('Path'):
			file = _.getText(path,raw=True)
			file = file.replace('    ','\t')
			objects = []
			basic = []
			All = []
			for line in file.split('\n'):
				line = line.split('#')[0]
				st = line.strip()
				if line.startswith('class '):
					if 'c' in _.switches.value('Path') or 'all' in _.switches.value('Path'):
						objects.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
						basic.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
						All.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
				if line.startswith('def '):
					if 'c' in _.switches.value('Path') or 'all' in _.switches.value('Path'):
						objects.append(st.split('def ')[1].split('(')[0].strip())
						basic.append(st.split('def ')[1].split('(')[0].strip())
						All.append(st.split('def ')[1].split('(')[0].strip())
				if 'v' in _.switches.value('Path') or 'all' in _.switches.value('Path'):
					if '=' in line:
						objects.append(st.split('=')[0].strip())
				if '=' in line:
					All.append(st.split('=')[0].strip())

			if not basic:
				objects = All
				_.switches.fieldSet('Path','value','all')

			# impPath = _.tailpop(impPath,' ')
			if len(_.switches.value('Path')):
				impPath += '  '+', '.join(objects)
			else:
				if iName in basic:
					impPath += '  '+ iName
				else:
					impPath += '  '+ basic[0]
			print(impPath)
			_copy.imp.copy( impPath, p=0 )
		else:
			_.pyColor(iCode)
			_copy.imp.copy( iCode, p=0 )





		# except Exception as e:
		# 	_.e(e,path)
		# if len(isData) > 1:
		# 	_.pr()
		# 	_.pr(line=1)




_copy = _.regImp( __.appReg, '-copy' )


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)