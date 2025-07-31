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
	_.switches.register('EnforceName', '-n', 'pyColor')
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






'''

def create_backup_filename(*args, **kwargs):
import importlib.util
	if 'create_backup_filename' not in intelligent_code.functions:
		path = '/opt/rightthumb-widgets-v0/widgets/python/library/tools/os/file/create_backup_filename.py'
		spec = importlib.util.spec_from_file_location('create_backup_filename', path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		intelligent_code.functions['create_backup_filename'] = module.create_backup_filename
	return intelligent_code.functions['create_backup_filename'](*args, **kwargs)

'''







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




iFn = '''
def iName(*args, **kwargs):
\timport importlib.util
\tif 'iName' not in intelligent_code.functions:
\t\timport importlib.util
\t\tpath = os.path.normpath(_v.w+'iFullPath')
\t\tspec = importlib.util.spec_from_file_location('iName', path)
\t\tmodule = importlib.util.module_from_spec(spec)
\t\tspec.loader.exec_module(module)
\t\tintelligent_code.functions['iName'] = module.iName
\treturn intelligent_code.functions['iName'](*args, **kwargs)
'''.strip().replace('    ', '\t')
iClass = '''
class iName:
\tdef __new__(cls, *args, **kwargs):
\t\timport importlib.util
\t\tif 'iName' not in intelligent_code.classes:
\t\t\timport importlib.util
\t\t\tpath = os.path.normpath(_v.w+'iFullPath')
\t\t\tspec = importlib.util.spec_from_file_location('iName', path)
\t\t\tmodule = importlib.util.module_from_spec(spec)
\t\t\tspec.loader.exec_module(module)
\t\t\tintelligent_code.classes['iName'] = module.iName
\t\treturn intelligent_code.classes['iName'](*args, **kwargs)
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





		# impPath = impPath.replace('library.python.', '')
		# iCode = iCode.replace('iPath',iPath)
		# iCode = iCode.replace('iName',iName)

		# if '.__init__ import  __init__' in impPath:
		# 	impPath = impPath.replace('.__init__ import  __init__', ' as imp')
		# 	impPath = impPath.replace('from ', 'import ')
		# if '.__init__ import __init__' in impPath:
		# 	impPath = impPath.replace('.__init__ import __init__', ' as _')
		# 	impPath = impPath.replace('from ', 'import ')
		
		# if _.switches.isActive('Tabs'):
		# 	iCode = iCode.replace('    ', '\t')
		
		# if _.switches.isActive('Spaces')  or  len(isData) > 1:
		# 	iCode = iCode.replace('\t', '    ')


		if isClass or _.switches.isActive('Class'):
			# print('isClass')
			iCode = iClass
			impPath = iClassPath.replace('iPath',iPath).replace('iName',iName)
		else:
			iCode = iFn
			impPath = iFnPath.replace('iPath',iPath).replace('iName',iName)

		
		# colorized = colorizer.colorize(iCode)
		
		# if _.switches.isActive('Path'):
		if True:
			file = _.getText(path,raw=True)
			file = file.replace('    ','\t')
			objects = []
			basic = []
			classes = []
			functions = []
			All = []
			# print(file)
			for line in file.split('\n'):
				line = line.split('#')[0].rstrip()
				# st = line.strip()
				st = line

				if st.startswith('class '):
					isClass = True
					name = st[6:].split('(')[0].split(':')[0].strip()
					if any(x in _.switches.value('Path') for x in ['c', 'all']) or _.switches.value('Path') == '':
						classes.append(name)
						objects.append(name)
						basic.append(name)
						All.append(name)

				elif st.startswith('def '):
					name = st[4:].split('(')[0].strip()
					# print(name)
					if not _.switches.isActive('Path') or any(x in _.switches.value('Path') for x in ['c', 'all']):
						functions.append(name)
						objects.append(name)
						basic.append(name)
						All.append(name)

				elif '=' in st and not st.startswith('def ') and not st.startswith('class '):
					left = st.split('=')[0].strip()
					if not any(c in left for c in ['[', '(', '{']) and not line.startswith((' ', '\t')):
						if any(x in _.switches.value('Path') for x in ['v', 'all']):
							objects.append(left)
						All.append(left)


			# for line in file.split('\n'):
			# 	line = line.split('#')[0]
			# 	st = line.strip()
			# 	if line.startswith('class '):
			# 		isClass = True
			# 		# print(line)
			# 		if 'c' in _.switches.value('Path') or 'all' in _.switches.value('Path') or _.switches.value('Path') == '':
			# 			# print(line)
			# 			objects.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
			# 			basic.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
			# 			All.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
			# 	elif line.startswith('def '):
			# 		if 'c' in _.switches.value('Path') or 'all' in _.switches.value('Path'):
			# 			objects.append(st.split('def ')[1].split('(')[0].strip())
			# 			basic.append(st.split('def ')[1].split('(')[0].strip())
			# 			All.append(st.split('def ')[1].split('(')[0].strip())
			# 	elif '='  in line  and not st.startswith('def ') and not '[' in line.split('=')[0] and not '(' in line.split('=')[0]:
			# 		if not line.startswith('\t') and not line.startswith(' '):
			# 			if 'v' in _.switches.value('Path') or 'all' in _.switches.value('Path'):
			# 				objects.append(st.split('=')[0].strip())
			# 			# All.append(line)
			# 			All.append(st.split('=')[0].strip())

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
			if _.switches.isActive('Path'):
				print(impPath)
				_copy.imp.copy( impPath, p=0 )
		# else:
		if True:

			if oName in functions:
				isClass = False

			
			if isClass or _.switches.isActive('Class'):
				iCode = iClass
				iName = classes[0]

			if oName in classes:
				# print('oName in All')
				iName = oName
			elif oName in functions:
				iName = oName
			# print(All)
			# iCode = iCode.replace('iName', 'asdf')
			if _.switches.isActive('EnforceName'):
				iCode = iCode.replace('iName', _.switches.value('EnforceName'))
			else:
				iCode = iCode.replace('iName', iName)

			iCode = iCode.replace('iFullPath', __.wPath(path))
			# iCode = iCode.replace('iName', iName)
			


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