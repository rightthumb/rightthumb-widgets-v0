import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'SearchValue', '-val' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p pyGlobal -f base + .'),
						_.hp('p pyGlobal -f base - .'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=False )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'code', 'classes')))
from CodeIndexerPygments import CodeIndexerPygments

def action():
	fi = _.switches.value('Files')
	_.pr( fi, c='cyan' )
	file = _.getText( fi, raw=True )
	file = file.replace('\r','')
	file = file.replace('    ','\t')

	code = CodeIndexerPygments( file, 'py' )
	data = []
	for k in code.db:
		data.append({'name': k+'  ' })
	_.fields.asset( 'data', data )
	
	for k in code.db:
		x = _.fields.value( 'data', 'name', k+':' )+'  '+str(len(code.db[k]))
		_.pr(x)
		# _.pr( _.pr0(k+':'),'\t', _.pr0(len(code.db[k]),c='cyan') )
	# return False
	cnt = 0
	l = 0
	table = []
	for b in code.db['lines']:
		l += 1
		e = code.db['lines'][b]
		line = code.code[b:e]
		Line = line
		line = line.split('#')[0].rstrip()
		st = line.strip()
		if st and '=' in line and not line.startswith('\t') and not line.startswith('def ') and not '.append(' in line:
			v = b
			value = ''
			while not v == e:
				v+=1
				for k in code.db:
					if v in code.db[k]:
						value = code.code[v:code.db[k][v]+1]
						break
			if not value:
				value = line.split('=')[1].strip()
			preview = ''
			for xx, char in enumerate(value):
				if xx > 30:
					preview += '...'
					break
				preview += char
			var = line.split('=')[0].strip()
			if _.switches.isActive('SearchValue'):
				if not _.showLine(value): continue
			else:
				if not _.showLine(var): continue
			table.append({ 'line': l, 'var': var, 'size': len(value), 'preview': preview })
			# _.pr( '  ',_.pr0(l),len(value), _.pr0(var,c='cyan') )
			cnt += 1
	_.pt( table )
	_.pr()
	_.pr( '', cnt,c='yellow' )

	# for i, line in enumerate(file.split('\n')):
	# 	Line = line
	# 	line = line.split('#')[0].rstrip()
	# 	st = line.strip()
	# 	if st and '=' in line and not line.startswith('\t') and not line.startswith('def ') and not '.append(' in line:
	# 		var = line.split('=')[0].strip()
	# 		if not _.showLine(var): continue
	# 		_.pr( '  ',_.pr0(i), _.pr0(var,c='cyan') )
	# 		cnt += 1
	# _.pr()
	# _.pr( '', cnt,c='yellow' )




# def action():
# 	fi = _.switches.value('Files')
# 	_.pr( fi, c='cyan' )
# 	file = _.getText( fi, raw=True )
# 	file = file.replace('\r','')
# 	file = file.replace('    ','\t')
# 	code = CodeIndexer( file )
# 	# _.pv(code.db)
# 	for k in code.db:
# 		_.pr( k, len(code.db[k]) )
	


########################################################################################
if __name__ == '__main__':

	action(); _.isExit(__file__)