#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import os
import sys
import time
# import platform
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################


def appSwitches():
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Head', '-head', '10' )
	_.switches.register( 'Tail', '-tail', '10' )
	_.switches.register( 'Line', '-l,-ln,-line' )
	_.switches.register( 'NoComment', '-nc' )
	_.switches.register( 'StripPreNumber', '-sn' )
	_.switches.register( 'Comment', '-comment', '"#"' )
	_.switches.register( 'Clean', '--c', 'noline' )
	_.switches.register( 'NotCleanForce', '-pr,-print,--nc,---c,-c-', 'noline' )
	_.switches.register( 'Count', '-cnt,-count' )
	_.switches.register( 'Function', '-fn' )



_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'cat.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'cat encrypted files',
	'categories': [
						'cat',
						'cat',
						'type',
						'file',
						'text',
						'tool',
						'print file',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						'echo null | p lineM -make " this is (n) test>>file.txt" -inc 00 -it 20 | p execute',
						'',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p cat -f example.txt',
						'',
						'p cat -f example.txt 2.txt --c noline',
						'',
						'p cat -f file.txt -tail 3 -head 3',
						'p cat -f file.txt -tail 4',
						'p cat -f file.txt -head 7',
						'',
						'p cat -f /etc/apt/sources.list* -comment "#"',
						'',
	],
	'columns': [
					   # { 'name': 'name', 'abbreviation': 'n' },
					   # { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					   # 'this',
					   # 'app',
	],
	'notes': [
					   # {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] }, 
		},
	}



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	__.myFileLocations_SKIP_VALIDATION = False

	_.switches.trigger( 'Files', _.myFileLocations )
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )

	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

if _.switches.isActive('NotCleanForce') and _.switches.isActive('Clean'): _.switches.fieldSet( 'Clean', 'active', False )

########################################################################################
# START

def cleaner(line):
	line=_str.do('sh', line)
	while line.endswith(' ') or line.endswith('\t') : line=line[:-1]
	return line


def pr(*args):
	global Function
	arg=' '.join(args)
	if Function:
		arg=arg.strip()
		a=''
		for c in arg:
			if c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.': a+=c
			elif c =='(': a+=c+' '
			else: a+=' '
		while '  ' in arg: arg=arg.replace('  ',' ')
		for x in a.split(' '):
			if '(' in x and  _.showLine(x): return x
		return ''
	return arg


def action():
	focus()
	global Function
	Count = []
	Count_=0
	if _.switches.isActive('Count'):
		Count=_.switches.values('Count')
		for i,C in enumerate(Count): Count[i]=_.ci(C)
	# _.pr(_.isData())
	# sys.exit()
	# files = _.switches.values('Files')
	files = _.isData()
	if type(files[0]) == list:
		files = files[0]
	for i,filepath in enumerate(files):
		maxLEN = 5
		midID = 'FCA4D034-357B-444E-B193-328E8E6EA011'
		wasCrypt = False
		try:
			os.path.isfile(filepath)
		except Exception as e:
			_.pr(filepath)
			_.e(e)
		if os.path.isfile(filepath):
			

			if i and not 'noline' in _.switches.value('Clean'):
				_.pr('_________________________________________')
			if not _.isCrypt(filepath):
				if not _.switches.isActive('Clean'):
					if __.path(filepath).startswith( _v.pp+os.sep+'configs'+os.sep ):
						_.colorThis( [filepath.replace('-',os.sep)], 'cyan' )
						_.pr()
					else:
						_.colorThis( [filepath], 'cyan' )
						_.pr()

			else:
				epoch = _dir.info(filepath)['me']
				if not _.switches.isActive('Clean'):
					_.colorThis( ['Encrypted:',filepath], 'red' )
					_.pr()
				wasCrypt = True
				_cryptFile.switch( 'Decrypt' )
				_cryptFile.switch( 'Encrypt', delete=True )
				_cryptFile.switch( 'Files', filepath )
				_cryptFile.do( 'action' )
				# focus()
				while epoch == _dir.info(filepath)['me']:
					time.sleep(.2)
			if False and wasCrypt:
				if not _.switches.isActive('Clean'):
					_.pr('_________________________________________')
					_.pr()
					_.pr()
				
			# sys.exit()
			newFile = []
			theFile = _.getText(filepath,raw=True).split('\n')
			
			for i, line in enumerate(theFile): theFile[i]=cleaner(line)

			lX = 10
			if _.switches.isActive('Head'):
				# _.pr('Head')
				if len(_.switches.value('Head')):
					lX = int(_.switches.value('Head'))
				if len(theFile) > lX:
					for llx,xyz in enumerate(theFile):
						if len(xyz):
							if llx+1 <= lX:
								if len(xyz) > maxLEN:
									maxLEN = len(xyz)
								newFile.append(xyz)
							else:
								break

			if _.switches.isActive('Tail'):
				# _.pr('Tail')
				if len(newFile):
					newFile.append(midID)
				tail = []
				if len(_.switches.value('Tail')):
					lX = int(_.switches.value('Tail'))
				theFile.reverse()
				if len(theFile) > lX:
					# _.pr( 'file right size' )
					for llx,xyz in enumerate(theFile):
						if len(xyz):
							if  llx <= lX:
								if len(xyz) > maxLEN:
									maxLEN = len(xyz)
								tail.append(xyz)
							else:
								break

				tail.reverse()
				# _.pr( 'tail len', len(tail) )
				for xyz in tail:
					newFile.append(xyz)

			if len(newFile):
				# _.pr( 'newFile len', len(newFile) )
				theFile = newFile

			# _.pr(lX,type(lX))
			# sys.exit()

			# maxLEN = 5000

			try:
				cols, rows = list( os.get_terminal_size() )
				cols = int(cols)
				if maxLEN > cols:
					maxLEN = cols - 5
			except Exception as e:
				if maxLEN > 150:
					maxLEN = 150


			for i, row in enumerate(theFile):
				vVv.total += 1
				shouldAdd = _.showLine(row)
				if shouldAdd:
					row=pr(row)
					if Function and not row: continue
					if _.switches.isActive('Plus'):
						for plusSearchX in _.switches.values('Plus'):
							plusSearchX = _.ci( plusSearchX )
							for subject in _.caseUnspecificCode( row, plusSearchX ):
								row = row.replace( subject, _.colorThis( subject, 'green', p=0 ) )
					if _.switches.isActive('StripPreNumber'):
						row2 = simpleClean(row)
						row3 = ''
						startedA = False
						startedB = False
						for ch in row2:
							if not startedB and not startedA:
								if ch == ' ' or ch == '\t':
									startedA = True

							if not startedB and startedA:
								if ch in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
									startedB = True


							if startedB:
								row3 += ch
						row = row3


					if _.switches.isActive('NoComment'):
						row2 = simpleClean(row)
						if not len(row2) or row2.startswith('#'):
							shouldAdd = False





				if shouldAdd:
					if _.switches.isActive('Comment'):
						comment = _.switches.values('Comment')[0]
						row = row.split(comment)[0]

						if not len( simpleClean(row) ):
							shouldAdd = False
				if shouldAdd:
					vVv.print += 1
					if row == midID:
						_.pr( _.genLine( maxLEN, '_', p=0 ) )
					else:
						if _.switches.isActive('Line'):
							_.pr( _.cp(i+1, 'yellow', p=0),'\t', row )
						else:
							if not Count:
								_.pr(row)
							else:
								_cnt=0
								if len(Count)==1: _cnt=row.lower().count(Count[0])
								else:
									_row=row.lower()
									for C in Count:_row+=_row.count(C)
								Count_+=_cnt
								if _cnt:
									_.pr(  _.pr(_.zeros3(_cnt,333),c='yellow',p=0)  ,row)


			if wasCrypt:
				if False and not _.switches.isActive('Clean'):
					_.pr()
					_.pr()
					_.pr('_________________________________________')
				_cryptFile.switch( 'Encrypt' )
				_cryptFile.switch( 'Decrypt', delete=True )
				_cryptFile.switch( 'Files', filepath )
				_cryptFile.do( 'action' )
				pass
	pass
	if not _.switches.isActive('Clean'):
		if Count_:
			_.cp( [ '', _.addComma(Count_) ], 'yellow' )
		else:
			if vVv.total:
				_.pr()
				if vVv.total == vVv.print:
					_.cp( [ '', _.addComma(vVv.total) ], 'yellow' )
				else:
					_.cp( [ '', _.addComma(vVv.print), 'of', _.addComma(vVv.total) ], 'yellow' )


def simpleClean(data):
	i = 0
	while i < 10:
		i+=1
		data = _str.cleanBE(data,' ')
		data = _str.cleanBE(data,'\t')
		data = _str.cleanBE(data,'\n')
		data = _str.cleanBE(data,'\r')
	return data
focus()
vVv = _.dot()
vVv.total = 0
vVv.print = 0
_cryptFile = _.regImp( __.appReg, 'cryptFile' )
_cryptFile.switch( 'NoExt' )
# if _.switches.isActive('Clean'):
_cryptFile.switch( 'Clean' )
_cryptFile.imp.appDBA = _cryptFile.focus
focus()
import _rightThumb._dir as _dir

Function=_.switches.isActive('Function')

355

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







