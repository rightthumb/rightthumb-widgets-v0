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

import os, sys, time
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
	_.switches.register( 'Test', '-test' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='data', description='Files' )
	_.switches.register( 'Delete', '-d,-delete' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'decrypt-docs.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'decrypt registered documentation files',
	'categories': [
						'decrypt',
						'docs',
						'tool',
						'file',
						'text',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p decrypt-docs -file file.txt'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START


def identify(row):
	if 'sUW+UyzaAo1BuzZ/2UahGCp4kHgiwk+xKniQeCLCT7GlpF8/aeR6NXE0uVp6/Kb/w3tFeg3Qb+9KnIbZ+6+nWijD//xIEr3Q' in row:
		return True
	if ' ' in row:
		return False
	if '!V!' in row:
		return False
	if row.endswith('='):
		return True
	# if len(row) > 15:
	#   return True

	n = '0123456789'
	l = 'abcdefghijklmnopqrstuvwxyz'
	u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	aa = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/+='


	hasAlpha=False
	for a in aa:
		if a in row:
			hasAlpha=True
			break
	if not hasAlpha:
		return False


	for ch in row:
		if not ch in chars:
			return False
	if ' ' in row:
		return False
	elif '\\' in row:
		return False
	elif '//' in row:
		return False
	elif 'http' in row:
		return False
	elif '=' in row and not row.endswith('='):
		return False
	elif row.endswith('='):
		return True
	elif len(row) > 15:
		return True
	# elif row.count('/') > 1 or row.count('+') :
	#   return True
	# elif row.count('/') > 5 or row.startswith('/'):
	#   return False

	else:

		if len(row) < 7:
			return False
		
		if row.endswith('='):
			return True

		if len(row) > 40:
			return True

		doc = []
		nn = 0
		ll = 0
		uu = 0
		for ch in row:
			if ch in n:
				doc.append('n')
				nn+=1
			elif ch in l:
				doc.append('l')
				ll+=1
			elif ch in u:
				doc.append('u')
				uu+=1
		if uu == 0 or ll == 0  or nn == 0:
			return False
		if uu > ll and ll > 3:
			return True
		
		if nn < 3 and len(row) < 8:
			return False
		if uu < 3 or ll < 3 :
			return False
		p = _.percentageDiffInt( uu, ll )
		if p > 75:
			return True
		# _.pr( p, uu, ll, row )
		# _.pr( doc )
		return False


	return False

records = {}
maxLen = 0
maxLen2 = 0
def vcrypyAA(file):
	if type(file) == list:
		result = 'list'
		file = '\n'.join(file)
	else:
		result = 'str'

	if '!V!' in file:
		lp = _.find_all(file,'\n')
		v = _.find_all(file,'!V!')
		for i in v:
			pA = -1
			pB = -1
			for l in lp:
				if l < i:
					pB = pA
					pA = l
				else:
					pB = pA
					pA = l
					break
			# _.pr( '___' )
			# _.pr( 747, (pA,pB), file[pB:pA].replace('\n','\n') )
			vcrypyA(file[pB:pA].replace('\n','\n'))

			# _.pr( '___' )
	return file


		

def vcrypyA(row):
	global maxLen2
	# global isMD
	# if not isMD:
	#   return row
	row2 = row
	if '!V!' in row2:
		row2 = row2.replace('!V!','')
		row2 = _str.cleanEnd(row2,'\t')
		row2 = _str.cleanEnd(row2,' ')

		if len(row2) > maxLen2:
			maxLen2 = len(row2)
	return row

def vcrypyB(file):
	global indexP
	global isMD
	# _.pr(505,type(file))
	# return file
	result = 'str'
	if type(file) == list:
		result = 'list'
		file = '\n'.join(file)

	if '!V!' in file:
		has = True
	else:
		has = False
	done = True


	if isMD and indexP:
		done = False
	elif has:
		done = False
	else:
		done = True
	
	if not done:
		file = file.split('\n')
		if isMD and indexP:
			spent=[]
			for oOo in indexP:
				if not oOo in spent:
					spent.append(oOo)

					try:
						file[oOo] = '~~~'+indexP[oOo]
					except Exception as e:
						pass
						# _.pr(329,oOo,len(file),oOo in indexP,'error: indexP[oOo]')


	if not done:
		if has:
			for i,row in enumerate(file):
				if '!V!' in row:
					row = file[i]
					row = row.replace('!V!','')
					row = _str.cleanEnd(row,'\t')
					row = _str.cleanEnd(row,' ')
					row = row + addSpaces2(row) + '!V!'
					file[i] = row
					# _.pr(404,row)
	if __.fn.saveText:
		_.pr('vcrypyB',result,)
	return file
	if result == 'list':
		return file
	else:
		return '\n'.join(file)

def process(row):
	row = _str.cleanEnd(row,' ')
	row = _str.replaceAll(row, '  !V!',' !V!')
	# if '!V!' in row:
	#   return row
	global records
	global maxLen
	if identify(row):
		try:
			row2 = _vault.imp.s.de( row )
			good = True
			if '\n' in row2:
				good = False
			for ch in row2:
				if ch not in _str.printable2:
					good = False
			if good:
				records[row] = row2
				if not row2.startswith('todo:'):
					if len(row2) > maxLen:
						maxLen = len(row2)
				# row = row2
		except Exception as e:
			pass
		# if row.startswith('!VAULT!'):
		#   _.pr( row )

	return row
	
def addSpaces(row):
	global maxLen
	y = maxLen - len(row) + 5
	i=0
	t = ''
	while not i == y:
		i+=1
		t+=' '
	return t

def addSpaces2(row):
	global maxLen2
	y = maxLen2 - len(row) + 5
	i=0
	t = ''
	while not i == y:
		i+=1
		t+=' '
	return t
indexP = {}
def md_clean(theFILE):
	# focus()
	global indexP
	done = False
	while not done:
		theFILE = _str.replaceAll(theFILE,' \n','\n')
		theFILE = _str.replaceAll(theFILE,'----','---')
		theFILE = _str.replaceAll(theFILE,'____','___')
		theFILE = _str.replaceAll(theFILE,'* * * *','* * *')
		theFILE = _str.replaceAll(theFILE,'****','***')
		theFILE = _str.replaceAll(theFILE,'~~~~','~~~')
		theFILE = _str.replaceAll(theFILE,'````','```')

		done = True
		for xXx in ['____','----','* * * *','****','````','~~~~']:
			if xXx in theFILE:
				done = False
		if done:
			while '---' in theFILE:
				theFILE = theFILE.replace( '---', '___' )
			while '* * *' in theFILE:
				theFILE = theFILE.replace( '* * *', '___' )
			while '***' in theFILE:
				theFILE = theFILE.replace( '***', '___' )
			while '```' in theFILE:
				theFILE = theFILE.replace( '```', '~~~' )
	file = theFILE.split('\n')
	spent = []
	for i,row in enumerate(file):
		if '!V!' in row:
			vcrypyA(row)
		if '~~~' in row and len(row) > len('~~~'):
			if not i in spent:
				spent.append(i)
				indexP[i] = row.split('~~~')[1]
			file[i] = '~~~'
	theFILE = '\n'.join(file)



	return theFILE
r = 0
def process_doc_sep(theFILE,doc_sep,doc_seps):
	global isMD
	global r
	r+=1
	segments=[]
	if type(theFILE) == list:
		theFILE = '\n'.join(theFILE)
	preFile = '\n'+doc_sep+'\n#testing\n\n'
	theFILE = preFile + theFILE
	for segment in theFILE.split(doc_sep):
		s0 = segment.split('\n')[0].lower()
		try:
			s1 = segment.split('\n')[1].lower()
		except Exception as e:
			s1 = ''
		choice=1
		for dsep in doc_seps:
			if s0 in dsep:
				choice=0
		if '#crypt' in s0.lower():
			choice=1

		file = []
		fileBK = []
		for i,row in enumerate( segment.replace('!vault!','!V!').replace('!VAULT!','!V!').replace('!v!','!V!').replace('!crypt!','!V!').replace('!CRYPT!','!V!').split('\n') ):
			fileBK.append(row)
			row = process(row)
			file.append(row)
		nFile = []
		for i,row in enumerate(file):
			inRec = False
			test = 999
			if row in records:
				inRec = True
				# _.pr(0,s0)
				# _.pr(1,s1)
				# sys.exit()
				# if '#crypt' in segment:
				test = 111
				original = row

				if '#crypt' in s1 or '#crypt' in s0:
					# _.pr("if '#crypt' in segment:")
					row = records[row]
					test = 222

				else:
					# _.pr("if NOT '#crypt' in segment:")
					if records[row].startswith('todo:'):
						test = 333
						done=False
						for test in ['ai','todo']:
							# _.pr(test)
							if not done:
								if test+': ' in records[row]:
									done=True
									# _.pr(test+': !V!')
									# sys.exit()
									row = records[row].replace( test+': ', test+':  !V!  ' )
								elif test+':x' in records[row]:
									done=True
									row = records[row].replace( test+':x', test+':x !V!  ' )
								elif test+':y' in records[row]:
									done=True
									row = records[row].replace( test+':y', test+':y !V!  ' )
								elif test+':z' in records[row]:
									done=True
									row = records[row].replace( test+':z', test+':z !V!  ' )
						
						if not done:
							done=True
							# row = records[row] + addSpaces(records[row]) + '!V!'
							row = _str.cleanEnd(records[row],' ') + addSpaces(records[row]) + '!V!'
						row=row.replace('!V!   ','!V!  ')
						row=row.replace('!V!   ','!V!  ')
						row=row.replace('   !V!','  !V!')
						row=row.replace('   !V!','  !V!')
						row=vcrypyA(row)
						test = 444
					elif choice:
						test = 555
						row = records[row] + addSpaces(records[row]) + '!V!'
						row=vcrypyA(row)
						# row = records[row]

			# _.pr(test,row)
			# if s0 in doc_sep:
			if choice and inRec:
				if row in records:
					row = records[row]
			if test == 111 or test == 999 or not choice:
				row = fileBK[i]
			vVv = 0
			if ( vVv and 'password' in row ) or ( vVv and '2022-02-04T22:30:00-0500' in row ) or ( vVv and '45.35.203.103' in row ) or ( vVv and 'DNX8ZsjuI1DWelkKipcBZL3j0IB6afSVlAnjXCssy2yIIsn7J9O3Aw==' in row ) or ( vVv and '3Yakcawoid5hXCFWnaYIhgkv5wl5BkdjSAJja5Vifyw=' in row ):
				_.cp(_.linePrint(p=0),'yellow')
				_.pr( s0 )
				_.pr( s1 )
				_.pr(r,choice,test,row,inRec)
			nFile.append(row)
		segments.append('\n'.join(nFile))
	
	data = doc_sep.join(segments)
	data = data[len(preFile):]
	data = vcrypyB(data)
	return data

deleteSpent = {}

def run(path):

	table = _.getTable('crypt-docs.list')
	if _.switches.isActive('Delete'):
		path=__.path(path)


		found=False
		new=[]
		for fi in table:
			if not fi == path: new.append(fi)
			else: found=True

		if found:
			global deleteSpent
			if not path in deleteSpent:
				deleteSpent[path]=1
				appReg=__.appReg
				_bk=_.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'isPreOpen' ); _bk.switch( 'Silent' );
				_bk.switch( 'Input', path ); bkfi = _bk.action();
				__.appReg=appReg
				# decrypt(path)
				_.cp('decrypted and removed from decrypt-docs database','yellow')
				_.saveTable(new,'crypt-docs.list',p=0)
		__.isExit()
		return None
	if _.switches.isActive('Delete'): return None
	if _.switches.isActive('Delete'): return None
	
	appReg=__.appReg
	_secureFiles=_.regImp( __.appReg, 'secureFiles' )
	__.appReg=appReg
	_secureFiles.switch( 'Delete' )
	_secureFiles.switch( 'Files', path )
	_secureFiles.action()
	__.appReg=appReg

	global isMD
	if path.lower().endswith('.md'):
		isMD = True
	else:
		isMD = False
	global records
	global maxLen
	global doc_sep
	global indexP
	indexP = {}
	table = _.getTable('crypt-docs.list')
	test=table.copy()
	if not __.path(path) in table:
		table.append( __.path(path) )
	# _.pv( table )
	newTable = []
	for ntf in table:
		if not ntf in newTable:
			newTable.append(ntf)
	table = newTable
	if not str(table)==str(test):
		_.saveTable( table, 'crypt-docs.list', p=0 )
		_.cp('added to secure docs database','yellow')
	else:
		pass
		_.cp('in secure docs database','yellow')
	theFILE = _.getText( path,raw=True )
	if theFILE.startswith(doc_sep.replace('\n','')):
		theFILE='\n'+theFILE

	doc_seps = [
					'\n__________________________________________________________________________________\n',
					'\n___\n',
					'\n~~~\n',
				]

	doc_sep  = doc_seps[0]
	if path.lower().endswith('.md'):
		theFILE = md_clean(theFILE)
		# if theFILE.startswith('\n'):
		#     _.saveText(theFILE[1:],path)
		# else:
		#     _.saveText(theFILE,path)
		theFILE = process_doc_sep(theFILE, doc_seps[2],doc_seps)
		theFILE = process_doc_sep(theFILE, doc_seps[1],doc_seps)

	else:
		theFILE = process_doc_sep(theFILE, doc_sep,[doc_sep])
		theFILE = _str.cleanFirst(theFILE,'\n')

	_.saveText( theFILE, path )

def action():

	
	if not _.switches.values('Files'):
		_.e('please specify a file')

	if _.switches.isActive('Test'):
		row = ' '.join( _.switches.values('Test') )
		row = process(row)
		return None
	
	for path in _.switches.values('Files'):
		run(path)



doc_sep = '\n__________________________________________________________________________________\n'

# import _rightThumb._vault as _vault

_vault = _.regImp( __.appReg, '_rightThumb._vault' )
focus()

isMD = True

# run(
# vcrypyA
# vcrypyB
# process_doc_sep
# _.pr(329,oOo,len(file),oOo in indexP,'error: indexP[oOo]')

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()