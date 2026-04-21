import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
from CodeIndexerPygments import CodeIndexerPygments
import _rightThumb._base3 as _
import _rightThumb._vars as _v
from os import sep, remove
import importlib.util
import sys
import threading
import time
_.isTesting = False
class liaison:
	def __init__(self, module, pin='-1'):
		self.module = module
		aes = _.aesEverywhere()
		fail = 'Not Authorized'
		_.liaison.epoch = str(time.time())
		_.liaison.pin = pin
		key = _.URL('https://sds.sh/liaison/', {'pin': pin, 'module': module, 'epoch': _.liaison.epoch})
		_.liaison.key = key
		_.liaison.token = _.md5Str(key)
		if key == fail:
			_.e('Not Authorized')
			return False
		exec(aes.decrypt(_.URL('https://sds.sh/liaison/', {'pin': pin, 'module': 'pre', 'epoch': _.liaison.epoch, 'key': key, 'token':_.liaison.token}),_.md5Str(_.liaison.epoch+key)))
		data = _.URL('https://sds.sh/liaison/', {'pin': pin, 'module': module, 'key': key, 'epoch': _.liaison.epoch, 'token':_.liaison.token})
		_.liaison.data = data
		if data == fail:
			_.e('Not Authorized')
			return False
		folder = _v.wprofile+sep+'liaison'
		file = folder +sep+ 'liaison.py'
		_.liaison.file = file
		if _.isTesting:
			print(file)

		def rm():
			remove(_.liaison.file)
		_.liaison.threads = ThreadManager(rm)
		_v.mkdir(file,pop=True)

		exec(aes.decrypt(_.URL('https://sds.sh/liaison/', {'pin': pin, 'module': 'liaison', 'epoch': _.liaison.epoch, 'key': key, 'token':_.liaison.token}),_.md5Str(_.liaison.epoch+key)))
		
		try: del _.liaison.token
		except: pass
		try: del _.liaison.data
		except: pass
		try: del _.liaison.epoch
		except: pass
		try: del _.liaison.pin
		except: pass
		try: del _.liaison.key
		except: pass

		global template
		temp = template.replace('moduleName',module)
		_.saveText(temp, file)
		self.mod = imp(module, file)
		


		del _.liaison.moduleItems
		del _.liaison.top




	def secureModule(self):
		return self.mod
		return eval('self.mod.'+self.module)

	def interact(self,*args,**kwargs):
		mod = eval('self.mod.'+self.module)
		_.liaison.active = time.time()

		def wait():
			while time.time() - _.liaison.active < 1:
				continue
		_.liaison.threads.add(wait)
		_.liaison.threads.wait_for_completion()
		try:
			return mod(*args,**kwargs)
		except:
			_.pr('Error',c='red')
template =  '''
import _rightThumb._base3 as _
for item in _.liaison.moduleItems:
	globals()[item] = _.liaison.moduleItems[item]
'''.strip()


def imp(module_name, file_path):
	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	sys.modules[module_name] = module
	spec.loader.exec_module(module)
	return module

def callables(file):
	file = file.replace('    ','\t')
	table = []
	size = 0
	last = -1
	active = False
	activeLine = ''
	lastType = ''
	lastLineNum = -1
	callableList = []
	variableList = []
	variableChildList = []
	for i,line in enumerate(file.split('\n')):
		line = line.split('#')[0].rstrip()
		st = line.strip()
		if st: size += 1
		if active and st: last = size
		if active and st and not line.startswith('\t'):
			active = False
			size = last
			table.append({  'type': lastType, 'item': activeLine.split('(')[0], 'pre': 0, 'line': lastLineNum, 'size': size })
			size = 0
			if lastType == 'callable':
				callableList.append(activeLine.split('(')[0])
			activeLine = ''
			lastType = ''
			lastLineNum = -1
		if line.startswith('class ') or line.startswith('def ') and ':' in line:
			while '  ' in line: line = line.replace('  ',' ')
			if line.startswith('class '):
				callable = line.replace(':','(').split('(')[0].split(' ')[1]
			else:
				callable = line.split('(')[0].split(' ')[1]
			lastType = 'callable'
			activeLine = callable
			lastLineNum = i
			active = True
			size = 0
		if not st.startswith('class ') and not st.startswith('def ')  and not st.startswith('if ')  and not st.startswith('while ') and '=' in st and not st.index('=')+1 == '=':
			var = st[:st.index('=')].strip()
			pre = len(line.split(var)[0])
			if not var in variableList:
				variableList.append(var)
				if pre:
					variableChildList.append(var)
			table.append({  'type': 'variable', 'item': var, 'pre': pre,  'line': i, 'size': 1 })
	lineSpent = {}
	for i,line in enumerate(file.split('\n')):
		line = line.split('#')[0].rstrip()
		st = line.strip()
		audit = False
		if st == 'h = color_dict[c]': audit = True
		if not st.startswith('class ') and not st.startswith('def ') and not st.startswith('if ')  and not st.startswith('while '):
			for c in callableList:
				pre = ''
				for x in line:
					if not x in '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
						pre += x
					else:
						break
				pre = len(pre)
				if c+'(' in line:
					try:
						if st[st.index(c+'(')-1] in '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
							continue
					except: pass
					var = ''
					if '=' in st and not st.index('=')+1 == '=':
						var = st[:st.index('=')].strip()
					if not i in lineSpent or (i in lineSpent and  not lineSpent[i] == c):
						lineSpent[i] = c
						table.append({  'type': 'called', 'item': c, 'pre': pre,  'line': i, 'size': 1, 'variable': var })
		if not st.startswith('class ') and not st.startswith('def '):
			for c in variableList:
				pre = ''
				for x in line:
					if not x in '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
						pre += x
					else:
						break
				pre = len(pre)
				if pre and c in line and st.startswith('global '):
					table.append({  'type': 'global-usage', 'item': line.split('global ')[1].strip(), 'pre': pre,  'line': i, 'size': 1 })
				# if audit and c == 'color_dict': _.pr(i,c,line,c='yellow')
				if pre and c in line:
					# if audit and c == 'color_dict': _.pr(i,c,line,c='yellow')
					try:
						if st[st.index(c)-1] in '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
							continue
					except: pass
					# if audit and c == 'color_dict': _.pr(i,c,line,st[st.index(c)+len(c)],c='yellow')
					try:
						if st[st.index(c)+len(c)] in '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
							continue
					except: pass
					# if audit and c == 'color_dict': _.pr(i,c,line,c='yellow')
					var = ''
					if '=' in st and not st.index('=')+1 == '=':
						var = st[:st.index('=')].strip()
					prefix = ''
					if c in variableChildList:
						prefix = 'child-'
					else:
						prefix = 'global-'
					if var in variableList and var == c:
							Type = prefix+'reset'
					else:
						Type = prefix+'usage'
					if not i in lineSpent or (i in lineSpent and  not lineSpent[i] == c):
						# if audit and c == 'color_dict': _.pr(i,c,line,{  'type': Type, 'item': c, 'pre': pre,  'line': i, 'size': 1, 'variable': var },c='yellow')
						lineSpent[i] = c
						table.append({  'type': Type, 'item': c, 'pre': pre,  'line': i, 'size': 1, 'variable': var })
	return _.sort2(table,'type,pre,line')
class ThreadManager:

	def __init__(self,callback=None):
		self.threads = []
		self.callback = callback
		self.wait_started = False

	def add(self, func, *args, **kwargs):
		thread = threading.Thread(target=func, args=args, kwargs=kwargs)
		self.threads.append(thread)
		thread.start()

	def wait_for_completion(self):
		if self.wait_started:
			return
		self.wait_started = True
		for thread in self.threads:
			thread.join()
		if self.callback:
			self.callback()
		if _.isTesting:
			print("Complete")

def inject(file):
	file = file.replace('    ','\t')
	lines = []
	for i,line in enumerate(file.split('\n')):
		lines.append(line)
		line = line.split('#')[0].rstrip()
		st = line.strip()
		if st.startswith('class ') or st.startswith('def ') and ':' in line:
			pre = line[0:line.index(st)]+'\t'
			lines.append(pre+'_.liaison.threads.add(_.liaison.wait); _.liaison.threads.wait_for_completion()')
	return '\n'.join(lines)