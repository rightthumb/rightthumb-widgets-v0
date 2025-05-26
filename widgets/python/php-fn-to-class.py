import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=True )
	_.switches.register( 'Save', '-save', 'file.php', description='Save' )
	_.switches.register( 'Class', '-class', 'AppName', isRequired=True )
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
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def stringIDs(main_string, substring):
    start_index = main_string.find(substring)
    if start_index == -1:
        return []
    end_index = start_index + len(substring) - 1
    return [start_index, end_index]

def isAN(character):
	if character == '_': return True
	return character.isalnum()

def fnEx(line):
	line=line.strip()
	if not 'function ' in line: return {}
	if line.startswith('function ') and '(' in line:
		fun = line[len('function '):].split('(')[0].strip()
		wIDs = stringIDs(line,fun)
		return {
			'f': fun,
			'o': wIDs[0],
			'c': wIDs[1],
		}
	return {}

def repID(string, start, end, new_string):
    if start < 0 or end > len(string) or start > end:
        return "Invalid range for replacement."
    return string[:start] + new_string + string[end:]


_Class = '''<?php

class MyClass {
//declaration

    public function __construct() {
//construct
    }

//functions
	
}

'''.strip()

def process(path):
	global _Class
	fi = _.getText2(path)
	fi = fi.replace('\r','')
	fi2=fi
	_code.imp.validator.register( fi, 'javascript' )
	_code.imp.validator.createIndex( fi, 'javascript', skipLoad=True, simple=False )
	status = __.setting('validation-status')
	names = []
	function = []
	globalVars = []
	for i,line in enumerate(fi.split('\n')):
		fn = fnEx(line)
		if 'f' in fn: names.append(fn['f'])
	theEnd = -1
	for i,line in enumerate(fi.split('\n')):
		# if not i: continue

		if line.strip().startswith('global '):
			glo = line[len('global '):].split(';')[0].strip().replace('$','')
			if glo: globalVars.append(glo)
		if line.startswith('function '):
			lineID = _code.imp.validator.carriageIndex['index'][i]
			lineID=lineID+1
			if lineID < theEnd: continue
			ix = i+1
			try: lineIDn = _code.imp.validator.carriageIndex['index'][ix]
			except: lineIDn = len(fi)

			ii=lineIDn
			while not fi[ii] == '{': ii-=1
			o=-1
			if ii in _code.imp.validator.identity['location']['open']:
				o=ii
			if ii+1 in _code.imp.validator.identity['location']['open']:
				o=ii+1
			if ii-1 in _code.imp.validator.identity['location']['open']:
				o=ii-1
			if not o == -1:
				c=_code.imp.validator.identity['location']['open'][o]
				theEnd = c
				snip = _code.imp.validator.assetSnipet( lineID, c )
				function.append(snip.strip())
				fi2=fi2.replace(snip,'')
	def processFi(function):
		lines = []
		if type(function) == str:
			function=[function]
			pre=False
		else:
			pre=True
		for fn in function:
			# print(type(fn))
			# continue
			myGlobe = []
			for i,line in enumerate(fn.split('\n')):
				if pre:
					if not i: line = 'private '+line
				if 'f' in fnEx(line):
					fnA = fnEx(line)['f']
				else:
					fnA = ''

				if line.strip().startswith('global '):
					glo = line.strip()[len('global '):].split(';')[0].strip().replace('$','')
					if glo:
						myGlobe.append(glo)
						cmdX=[]
						for cmd in line.split(';'):
							if not 'global ' in cmd: cmdX.append(cmd)
						line = ';'.join(cmdX)

				for g in globalVars:
					gg='$'+g
					if gg in line:
						gi = stringIDs(line, gg)
						try:
							gx = isAN(line[gi[1]])
						except:
							gx = True
						if not gx:
							fnI = stringIDs(line,gx)
							if not 'function ' in line:
								line = repID(line,gi[0],gi[1]+1,'$this->'+g)


				for n in names:
					if not n == fnA:
						nx = n+'('
						if nx in line:
							adjust = False
							fnI = stringIDs(line,nx)
							if fnI[0] == 0: adjust=True
							else:
								if not isAN(line[fnI[0]-1]):
									adjust=True
						
							if adjust:
								if nx in line:
									fnI = stringIDs(line,nx)
									rep = '$this->' + nx
									if not 'function ' in line:
										line = repID(line, fnI[0], fnI[1]+1, rep)
				# if line.strip():
				lines.append('\t'+line.replace('\t','    ').replace('    ','\t'))
		return '\n'.join(lines)
	

	# built.append(fi2)
	# for iter in f12.split('\n'):
	global _Class
	# globalVars
	lines=[]
	for line in fi2.split('\n'):
		for g in globalVars:
			g=g.strip()
			# print('g:',g)
			gg='$'+g
			if gg in line:
				gi = stringIDs(line, gg)
				try:
					gx = isAN(line[gi[1]])
				except:
					gx = True
				if not gx:
					fnI = stringIDs(line,gx)
					if not 'function ' in line:
						line = repID(line,gi[0],gi[1],'$this->'+g)
		lines.append('            '+line)
	results = '\n'.join(lines).strip().replace('<?php','')
	# print(processFi(fi2))
	Class_ = _Class
	Class_ = Class_.replace('MyClass', _.switches.value('Class'))
	Class_ = Class_.replace('//construct', results)
	Class_ = Class_.replace('//functions', processFi(function))

	Class_ = Class_.strip()
	print(Class_)
	print()
	# built = []
	# built.append('\n'.join(processFi(fi2)))
	# built.append('\n'.join(processFi(function)))
	
	# result = '\n'.join(built)
	# print(result)
	# return result
	pass










	# print(fi2)
			# for x in _code.imp.validator.identity['identity']:
			# 	o = x
			# 	c = _code.imp.validator.identity['location']['open'][o]
			# 	l = _code.imp.validator.getLabel( o, string=True )
			# 	snip = _code.imp.validator.assetSnipet( lineID, c )
			# 	print(snip)
			# 	sys.exit()
	# for ln in _code.imp.validator.carriageIndex['index']: print(ln)

def action():
	for path in _.isData():
		process(path)

import sys
_code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);#################################
if __name__ == '__main__':
	action(); _.isExit(__file__);
