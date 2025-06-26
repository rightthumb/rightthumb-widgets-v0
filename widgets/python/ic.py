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
	_.switches.register('PrintClean', '--c')
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=False )
	_.switches.trigger( 'DB', _.aliasesFi )
	# _.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


import re

# from _rightThumb._base3.library.tools.code.classes.PythonCodeColorizer import PythonCodeColorizer


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
def action():
	# colorizer = PythonCodeColorizer()
	# print(colorizer.colorize(sample_code))
	files = []

	# if _.switches.isActive('Path'):
	# 	if not _.switches.values('Path'):
	# 		_.switches.val('Path','value','m')
	# 		_.switches.val('Path','values',['m'])
	if _.switches.isActive('Files'):
		files = _.switches.values('Files')
	elif _.isData():
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
		path = __.path(path)
		# print(path)
		# continue
		if not os.path.isfile(path): continue
		if not _.switches.isActive('Files'):
			if not _.showLine(path): continue
		if '__pycache__' in path: continue
		if os.sep+'backup'+os.sep in path and not 'os' in path and not 'file' in path: continue
		isData.append(path)

	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	for path in isData:
		
		path = __.path(path)
		
		if len(isData) > 1:
			if not _.switches.isActive('PrintClean'):
				_.pr()
				_.pr(line=1)
				_.pr(path,c='green')
		# try:



	
		relevant = []
		parts = path.split(os.sep)
		active = False
		for part in parts:
			if part == '_rightThumb' or part == 'library':
				active = True
			if active:
				relevant.append(part)
		iPath = '.'.join(relevant)
		iPath = iPath[0:len(iPath)-len('.py')]
		isClass = False
		
		if 'library.classes' in iPath:
			isClass = True
		# print(relevant)
		# print(relevant)
		iName = relevant[-1].replace('.py','')
		iName = iName[0:len(iPath)-len('.py')]
		oName = iName
		# print(iName)
		if isClass or _.switches.isActive('Class'):
			iCode = iClass
			impPath = iClassPath.replace('iPath',iPath).replace('iName',iName)
		else:
			iCode = iFn
			impPath = iFnPath.replace('iPath',iPath).replace('iName',iName)
		

		
		impPath = impPath.replace('library.python.', '')
		iCode = iCode.replace('iPath',iPath)
		iCode = iCode.replace('iName',iName)

		if '.__init__ import  __init__' in impPath:
			impPath = impPath.replace('.__init__ import  __init__', ' as imp')
			impPath = impPath.replace('from ', 'import ')
		if '.__init__ import __init__' in impPath:
			impPath = impPath.replace('.__init__ import __init__', ' as _')
			impPath = impPath.replace('from ', 'import ')
		
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
			# print(file)
			for line in file.split('\n'):
				line = line.split('#')[0]
				st = line.strip()
				if line.startswith('class '):
					# print(line)
					if 'c' in _.switches.value('Path') or 'all' in _.switches.value('Path') or _.switches.value('Path') == '':
						# print(line)
						objects.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
						basic.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
						All.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
				elif line.startswith('def '):
					if 'c' in _.switches.value('Path') or 'all' in _.switches.value('Path'):
						objects.append(st.split('def ')[1].split('(')[0].strip())
						basic.append(st.split('def ')[1].split('(')[0].strip())
						All.append(st.split('def ')[1].split('(')[0].strip())
				elif '='  in line  and not st.startswith('def ') and not '[' in line.split('=')[0] and not '(' in line.split('=')[0]:
					if not line.startswith('\t') and not line.startswith(' '):
						if 'v' in _.switches.value('Path') or 'all' in _.switches.value('Path'):
							objects.append(st.split('=')[0].strip())
						# All.append(line)
						All.append(st.split('=')[0].strip())

			if not basic:
				objects = All
				if len(_.switches.value('Path')):
					_.switches.fieldSet('Path','value','all')
			if '.__init__' in impPath:
				impPath = impPath.replace('.__init__', '')
				# impPath = impPath.replace('from ', 'import ')
			if '.__init__ import __init__' in impPath:
				impPath = impPath.replace('.__init__ import __init__', ' as _')
				# impPath = impPath.replace('from ', 'import ')
			# for o in objects: print(o)
			# return None
			# impPath = _.tailpop(impPath,' ')

			# print(objects)
			objs = []
			for o in objects:
				# print(o)
				if _.switches.isActive('Files'):
					if _.showLine(o):
						objs.append(o)
				else:
					objs.append(o)
			objectItems = '  '+', '.join(objs)

			# print(All)

			if len(_.switches.value('Path')):
				# print(impPath)
				if not objects:
					# impPath += '  '+ iName
					objects = '  '+ iName
				else:
					objs = []
					for o in objects:
						if _.switches.isActive('Files'):
							objs.append(o)
						else:
							if _.showLine(o):
								objs.append(o)
					objects = '  '+', '.join(objs)
					# impPath += '  '+', '.join(objs)
			else:
				# print(impPath)
				if not basic:
					# impPath += '  '+ iName
					objects = '  '+ iName
				elif iName in basic:
					# impPath += '  '+ iName
					objects = '  '+ iName
				else:
					# impPath += '  '+ basic[0]
					objects = '  '+ basic[0]
			impPath += objectItems
			impPath = impPath.replace('import  __init__','as ')
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