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
__.registeredApps.append(focus())
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._md5 as _md5
try:
	import _rightThumb._mimetype as _mime
except Exception as e:
	pass
_bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )
##################################################
import datetime
from shutil import copyfile

import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext

from pathlib import Path
##################################################

def appSwitches():

	
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Result', '-result')
	_.switches.register('Flag', '-flag', 'V')
	_.switches.register('Silent', '-silent,--c')
	_.switches.register('DoNotSchedule', '-noschedule')
	_.switches.register('isRunOnce', '-1,-isrunonce,-once,-single,-runonce,-one')
	_.switches.register('PythonDocumentation', '-python')
	_.switches.register('Session', '-session')
	_.switches.register('isPreOpen', '-open,-isPreOpen')
	_.switches.register('Test', '-test')
	_.switches.register('Force', '-force')
	_.switches.register('BypassScheduler', '-bs')
	_.switches.register('BackupRecoverScan', '-bkscan','1,2,3,4,5')	
	_.switches.register('EncryptBackup', '-en,-encrypt')
	# _.switches.register('Session_ID', '-session')

	


_.appInfo[focus()] = {
	'file': 'fileBackup.py',
	'description': 'Auto Backup File Before Open',
	'categories': [
						'research',
						'text manipulation',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}


_.appInfo[focus()]['relatedapps'].append('# Used to encrypt registered crypt files')
_.appInfo[focus()]['relatedapps'].append('\t p fileBackup -flag lock -runonce -noschedule -f file.txt')
_.appInfo[focus()]['relatedapps'].append('p fileRecover')
_.appInfo[focus()]['relatedapps'].append('p fileBackupLogFix')

_.appInfo[focus()]['examples'].append('p fileBackup -file file.txt')



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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	_.switches.trigger( 'Flag', _bkLog.imp.validateFlag )
	_.switches.trigger( 'Input', _.isFile )
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

def setPipeData(data):
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in data:
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')



_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )



########################################################################################
# START


if _.switches.isActive('Session'):
	__.Session_ID = _.switches.values('Session')
else:
	__.Session_ID = os.getenv('Session_ID')


def log_default_fields(record):
	info = {
		"id": "",
		"timestamp": 0,
		"file": "",
		"backup": "",
		"mime": "",
		"status": 0,
		"session": "",
		"version": "0.0.0.0",
		"v": 0, "v1": 0, "v2": 0, "v3": 0,
		"name": "",
		"flag": ""
	}
	for k in info:
		if not k in record:
			record[k] = info[k]
	return record
def generateID(path):
	abPath = os.path.abspath(path)
	md5 = _md5.md5File(abPath)
	# _.pr(md5)
	id = _md5.md52GUID(md5,True)
	bkRecoverListen(id,abPath)
	return id 

def idExist(theID, data, path):
	found = False
	abPath = os.path.abspath(path)
	for d in data:
		if d['id'] == theID and d['file'].lower() == abPath.lower():
			return d['backup']
	return False

def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y_%m_%d-%H_%M_%S')
	theDate = str(theDate)
	return theDate

masterEpoch = None

def genEpoch():
	global masterEpoch
	if not masterEpoch is None:
		return masterEpoch
	else:
		masterEpoch = time.time()
		return masterEpoch

def PRE_BACKUP_PROCESSING( path ):
	# return None
	if path.lower().endswith( '.py' ):
		parts = path.split(os.sep)
		parts.reverse()
		filename = parts[0]
		bk = _v.stmp+os.sep+'_temp_auto_clean_fileBackup_'+filename
		_.pr(bk,c='ColorBold.gray')
		# sys.exit()
		if os.path.isfile( bk ):
			return None


		thisExampleVX = None
		thisBaseVX = None
		for vx in _v.base_versions():
			ex = _v.base_template.replace( _v.import_delim , vx  )
			bf = _v.base_file.replace( _v.import_delim , vx  )
			if path.endswith( bf ):
				thisBaseVX = vx
			if path.endswith( ex ):
				if not isActive('Silent'):
					_.colorThis( 'PROCESSED: registered python template', 'Background.yellow' )
				thisExampleVX = vx
		thisExampleVX_NEW=False
		if thisExampleVX is None:
			if '_rightThumb._base3' in _.getText( path, raw=True ):
				thisExampleVX='3'
				thisExampleVX_NEW=True
			

		if not thisExampleVX is None or thisExampleVX_NEW:
			theExampleLines = []
			template = _.getText( path, raw=True ).split('\n')
			start = '#b)--> examples'
			end = '#e)--> examples'
			# start = '### EXAMPLE: START'
			# end = '### EXAMPLE: END'
			active = False
			theExampleLines.append('# construct registration')
			theExampleLines.append('# appDBA = __name__')
			for row in template:
				row = row.replace( '\n', '' )
				if start in row:
					active = True
				if active:
					original = row
					row = _str.totalClean( row )
					if len(row) and row.startswith('#') and not original in theExampleLines:
						theExampleLines.append( original )
						# print('xXx',row)
				if end in row:
					active = False
			# del template
			if thisExampleVX_NEW:
				lines=[]
				for line in template:
					if not len(line.replace(' ','').replace('\r','').replace('\n','').replace('\t','')): line=''
					if not line in theExampleLines:lines.append(line)
				xFiles = '\n'.join( lines )
				# while '########################################################################################\n\n' in xFiles: xFiles=xFiles.replace('########################################################################################\n\n','########################################################################################\n')
				while '\n\n' in xFiles: xFiles=xFiles.replace('\n\n','\n')
				xFiles=xFiles.replace('########################################################################################\n########################################################################################','########################################################################################')
				# bk = _v.stmp+os.sep+''+filename
				_.saveText( template, bk )

				
				add_line_before = [
										'#b)-->',
										'########################################################################################',
										'_.appInfo[',
										# '',
				]
				add_line_after = [
										'# ## {C3P0D40fAe8B} ##',
										'#!/usr/bin/python3',
										'#e)-->',
										'#n)--> start',
										# '',
				]

				lines = []
				for line in xFiles.split('\n'):
					# cl_test=line.replace(' ','').replace('\r','').replace('\n','').replace('\t','')
					cl_test=_str.do('trim',line)
					for rel_str in add_line_before:
						if cl_test.startswith(rel_str): lines.append('')
					if cl_test.startswith('def') and cl_test.endswith('):'): lines.append('')
					# if line == '##################################################':  lines.append('')

					lines.append(line)

					# if line == '##################################################':  lines.append('')
					for rel_str in add_line_after:
						if cl_test.startswith(rel_str): lines.append('')

				# _.saveText(xFiles,path)
				xFiles = '\n'.join(lines)
				xFiles = xFiles.replace('##################################################\n\n\n##################################################','')
				xFiles = xFiles.replace('##################################################\n\n##################################################','')
				while '\n\n\n' in xFiles: xFiles=xFiles.replace('\n\n\n','\n\n')

				_this_app_ = __.path(path,file=True)
				xFiles=xFiles.replace('thisApp.py',_this_app_)
				if 'Changes the world' in xFiles: xFiles=xFiles.replace('Changes the world',input('Description: '))
				xFiles=xFiles.replace('thisApp ',_this_app_.replace('.py','')+' ')
				if "'created': None," in xFiles:
					# xFiles = xFiles.replace( "'created': '0000-00-00',", "'created': '0000-00-00',".replace('0000-00-00',_.isDate(os.path.getctime(path),f='date')) )
					xFiles = xFiles.replace( "'created': None,", "'created': None,".replace('None',str(os.path.getctime(path))) )
					

				_.saveText(xFiles,path)

				_.pr('cleaned template stuff with new algorithm',c='Background.purple')
				_.pr('bk:',bk,c='Background.purple')
			pass
			if len(theExampleLines):
				# ef = _v.myTables + os.sep + _v.py_examples
				# if os.path.isfile(ef):
				#   record = _.getTable( _v.py_examples )
				#   newExamples = []
				#   for x in record['examples']:
				#       if not x in newExamples:
				#           newExamples.append( x )
				#   for x in theExampleLines:
				#       if not x in newExamples:
				#           newExamples.append( x )
				#   theExampleLines = newExamples
					# del newExamples
				pass

				data = {
							'epoch': genEpoch(),
							'md5': str(_md5.md5File( path )),
							'path': path,
							'examples': theExampleLines,
				}
				# _.pr( data )

				_.saveTable(   data,  _v.py_examples.replace( _v.import_delim , thisExampleVX  ), lock=True   )
				# del data
				# del theExampleLines

		# thisBaseVX = None
		elif thisBaseVX is None:
			md5 = str(_md5.md5File( path ))

			file = _.getText( path, raw=True ).split('\n')
			baseCommand = None
			baseScan = _v.base_import.split( _v.import_delim )

			for row in file:
				if baseScan[0] in row and baseScan[1] in row:
					baseCommand = row
			if baseCommand is None:
				return None

			thisBaseVX = None
			for vx in _v.base_versions():
				bi = _v.base_import.replace( _v.import_delim , vx  )
				if bi in baseCommand:
					thisBaseVX = vx

			if thisBaseVX is None:
				return None
			# _.pr(  )
			# _.pr( _v.py_examples )
			# _.pr(  )
			# _.pr( _v.import_delim )
			# _.pr(  )
			# _.pr( thisBaseVX )
			# _.pr(  )


			examples = _.getTable( _v.py_examples.replace( _v.import_delim , thisBaseVX  ) )
			alpha = checkAlpha( thisBaseVX )
			varSize = _.get_size(examples)
			# varSize2 = _.get_size(  _.getTable('asdflasdfasdfasfasdfasd')  )
			# _.pr(  )
			# _.pr( examples )
			# _.pr(  )
			# _.pr( 'varSize:', varSize, thisBaseVX )
			# _.pr( varSize2 )
			# _.pr(  )
			# _.pr( alpha )
			# _.pr(  )
			if alpha['has'] and not varSize is None and varSize < 100:
				examples = _.getTable( _v.py_examples.replace( _v.import_delim , alpha['int']  ) )
				# _.pr( 'ran' )
			varSize = _.get_size(examples)

			# _.pr( 'varSize:', varSize, alpha )
			if not varSize is None and varSize > 100:

				if md5 == examples['md5']:
					templateLog = _.getTable( '_app_template_log.json' )
					tLog = {
								'epoch': genEpoch(),
								'path': path,
								'template_epoch': examples['epoch'],
								'md5': md5,
					}
					templateLog.append(tLog)
					_.saveTable( templateLog, '_app_template_log.json', lock=True )
					# del templateLog
					return None
				newFile = []
				maxLines = 4
				spaces = 0
				active = False

				method = 1
				if method == 1:

					newFile = []
					spaces = 0
					for row in file:
						row = row.replace( '\n', '' )
						original = row
						row = _str.totalClean( row )
						if not original in examples['examples']:
							if len(row):
								spaces = 0
								newFile.append( original )
							else:
								spaces+=1
								if spaces <= maxLines:
									newFile.append( original )


				if method == 2:

					start = '#b)--> examples'
					end = '#e)--> examples'
					for row in file:
						shouldAdd = False
						row = row.replace( '\n', '' )
						original = row
						if start in row:
							active = True
						if active:
							row = _str.totalClean( row )
							if not original in examples['examples']:
								shouldAdd = True
							

						if not active or shouldAdd:
							if len(row):
								spaces = 0
								newFile.append( original )
							else:
								spaces+=1
								if spaces <= maxSpaces:
									newFile.append( original )
						pass

						if end in row:
							active = False

				if len(newFile):
					tmpName = tempName( path )
					# bk = _v.stmp+os.sep+'_temp_auto_clean_fileBackup_'+_.fileDate(time.time())+tmpName
					bk = _v.stmp+os.sep+'_temp_auto_clean_fileBackup_'+filename
					newFile = postFileCleanup( newFile, path=path, maxLines=maxLines )
					_.saveText( newFile, bk )
					_.saveText( newFile, path )
					_.colorThis( [ 'Backup Temp:', bk ], 'blue' )
				
			# del newFile
			# del examples
			# del file

	# _v.py_examples
	# _v.base_import
	# _v.import_delim
	# _v.base_versions

def loopText( text, cnt ):
	txt = ''
	i = 0
	while not i == cnt:
		i+=1
		txt += text
	return txt

def postFileCleanup( fileLines, path=None, maxLines=4 ):

	file = '\n'.join( fileLines )
	file = _.print_pr(file)
	separator = loopText( '#', 50 )+'\n'
	separator2 = loopText( '#', 88 )+'\n'

	var = """\"\"\"
	_.switches.documentation( 'Test', { 
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	\"\"\""""

	parts = path.split(os.sep)
	parts.reverse()
	filename = parts[0]
	if '__init__.py' == filename:
		filenameDisplay = parts[2]+'.'+parts[1]
		isImport = True
	else:
		isImport = False
		filenameDisplay = parts[0]
	fr = "'file': "
	fr += "'thisApp.py',"
	frX = fr.replace( 'thisApp.py', filename )
	file = file.replace( fr , frX )

	if "\t'description': 'Changes the world'," in file:
		_.pr()
		txt = _.colorThis( [ ' Please add a description for the app ' ] , 'yellow', p=0 )
		txt += _.colorThis( [ filenameDisplay.split('.')[0] ] , 'red', p=0 )
		if not isActive('Silent'):
			_.pr( txt )
		description = ''
		description = input( '\n\tDescription: ' )
		if not isActive('Silent'):
			_.pr()
		file = file.replace( "\t'description': 'Changes the world'," ," \t'description': '"+description+"'," )
	aTag = "\t\t\t\t\t\t'DEFAULT',\n"
	if aTag in file:
		if not isActive('Silent'):
			_.pr()
		txt = _.colorThis( [ ' Please add a hashtags for the app ' ] , 'yellow', p=0 )
		txt += _.colorThis( [ filenameDisplay.split('.')[0] ] , 'red', p=0 )
		if not isActive('Silent'):
			_.pr( txt )
		hashtags = '' 
		hashtags = input( '\n\tHashtags(one,two): ' )
		newTags = []
		if len(hashtags):
			for tag in hashtags.split(','):
				tag = _str.totalClean( tag )
				if len(tag):
					newTags.append( aTag.replace( 'DEFAULT', tag.replace( "'", "'+os.sep" ) ) )
				

			file = file.replace( aTag , ''.join( newTags ) )
		if not isActive('Silent'):
			_.pr()
	if not isImport:
		xExample = 'p thisApp -file file.txt'
		aExample = "\t\t\t\t\t\t_.hp('"+xExample+"'),\n"
		if aExample in file:
			import subprocess
			dataTXT = subprocess.check_output(["doskey", "/history"])
			dataTXT = str(dataTXT,'iso-8859-1', 'ignore')
			# _.pr( dataTXT )
			# do = ' doskey /history > "' + _v.tmpf + '"'
			# do = 'h > %tmpf%'
			# # _.pr( do )
			# os.system( '"' + do + '"' )

			# dataTXT = _.getText( _v.tmpf, raw=True, clean=2 ).split('\n')
			fn  = filename.split('.')[0]

			first = True
			txt = _.colorThis( [ ' Auto add example for app ' ] , 'yellow', p=0 )
			txt += _.colorThis( [ filenameDisplay.split('.')[0] ] , 'red', p=0 )

			newExample = []
			# _.pr('dataTXT',dataTXT)

			for line in dataTXT.split('\n'):
				line = _str.totalClean( line )
				line += ' '
				# _.pr( 'test:', line )
				if line.lower().startswith( 'p '+fn.lower()+' ' ):
					if first:
						first = False
						if not isActive('Silent'):
							_.pr(  )
							_.pr(  )
							_.pr( txt )
					if not isActive('Silent'):
						_.colorThis( [ '\n\tAdd example (y): ' ] , 'cyan' )
					if not 'n' in input( '\n\t\t ?: '+line ):
						addExample = aExample.replace('\\','\\\\')
						addExample = addExample.replace( xExample, line )
						newExample.append( addExample )
						if not isActive('Silent'):
							_.colorThis( [ '\n\t\t\t Added' ] , 'green' )
							_.pr( addExample )
					else:
						if not isActive('Silent'):
							_.colorThis( [ '\n\t\t\t NOT Added' ] , 'red' )

			if len(newExample):
				addExample = aExample.replace('\\','\\\\')
				file = file.replace( addExample , ''.join( newExample ) )

			# sys.exit()

	file = file.replace( var , '' )
	file = file.replace( separator+'\n\n\n'+separator, separator )
	file = _str.replaceAll( file , loopText( '\n', maxLines+1 ) ,  loopText( '\n', maxLines )  )
	file = _str.replaceAll( file , separator+'\n', separator )
	file = _str.replaceAll( file , '\n\n'+separator, '\n'+separator )
	file = _str.replaceAll( file , separator+separator, separator )
	file = file.replace( '\ndef appSwitches()', '\n\n'+'def appSwitches()' )
	file = _str.replaceAll( file , separator2+separator2, separator2 )

	return file.split('\n')
	pass
def tempName( path ):
	parts = path.split(os.sep)
	name = '-'.join(parts)
	name = name.replace( ':', ';' )
	return name

def checkAlpha( data ):
	theBase = None
	text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	found = False
	without = ''
	for x in data:
		if x in text:
			found = True
		else:
			without += x
	pass
	return { 'has': found, 'int': without }


def secureFiles_Decrypt( path, pw=None ):
	if pw is None: pw = _vault.key()
	__.openSecure = True
	if not isActive('Silent'):
		_.cp( 'crypt.de', 'Background.light_blue' )
	_cryptFile.switch( 'Password', delete=True )
	if len(pw):
		# _.pr(_blowfish.decrypt( pw, _vault.key() ))
		_cryptFile.switch( 'Password', _blowfish.decrypt( pw, _vault.key() ) )
	_cryptFile.switch( 'Decrypt' )
	_cryptFile.switch( 'Encrypt', delete=True )
	_cryptFile.switch( 'Files', path )

	epoch = _dir.info(path)['me']
	_cryptFile.action()
	while epoch == _dir.info(path)['me']:
		time.sleep(.2)

def secureFiles_Encrypt( path, pw=None ):
	# if pw is None: pw = _vault.key()
	__.openSecure = False
	if _.isCrypt(path):
		return None
	isTest0=False
	if not isActive('Silent'):
		_.cp( 'crypt.en', 'Background.light_blue' )
	_cryptFile.switch( 'Password', delete=True )
	if len(pw):
		if isTest0: _.pr('pw0')
		_cryptFile.switch( 'Password', _blowfish.decrypt( pw, _vault.key() ) )
	
	if isTest0: _.pr('001')
	_cryptFile.switch( 'Encrypt' )
	_cryptFile.switch( 'Decrypt', delete=True )
	_cryptFile.switch( 'Files', path )

	epoch = _dir.info(path)['me']
	if isTest0: _.pr('002')

	# if isTest0: _cryptFile.switch(dump=True)


	_cryptFile.action()
	if isTest0: _.pr('003')
	done=False
	while not done:
		time.sleep(.2)
		if not epoch == _dir.info(path)['me']: done=True
	if isTest0: _.pr('004')



def secureFiles(path):


	global crypt_docs
	cryptScan=False
	if path.lower() in __.specifications['fileBackup-auto-crypt']['files']:
		cryptScan=True
	elif path.lower() in crypt_docs:
		cryptScan=True
	else:
		fo=_dir.info( path )['folder'].lower()
		if fo in __.specifications['fileBackup-auto-crypt']['folders']:
			cryptScan=True
		else:
			for fTest in __.specifications['fileBackup-auto-crypt']['folders']:
				if fTest+os.sep in fo+os.sep:
					cryptScan=True





	if cryptScan:
		if not __.fileBackup.isPreOpen:
			return False
		global _decrypt_docs
		if _decrypt_docs is None: _decrypt_docs = _.regImp( __.appReg, 'decrypt-docs' )
		if not isActive('Silent'):
			_.cp( [ 'SECURE FILE' ], 'Background.red' )
		__.setting('fileBackup-secure_file',True)
		_decrypt_docs.imp.run(path)
		if __.fileBackup.isPreOpen:
			return True
		else:
			return False
	
	

	if path in __.v.secure.files:
		if not isActive('Silent'):
			_.cp( [ 'SECURE FILE' ], 'Background.red' )
		__.setting('fileBackup-secure_file',True)
		_.v.secure=True
		
		if path in __.v.secure.files:
			secure_record = __.v.secure.files[ path ]
		

		if secure_record['noBackup'] and not secure_record['Encrypt']:
			return True

		elif secure_record['noBackup'] and secure_record['Encrypt']:
			if __.fileBackup.isPreOpen and _.isCrypt(path):
				secureFiles_Decrypt( path, secure_record['Password'] )
			return True
		
		elif secure_record['noBackup']:
			return True

		elif secure_record['Backup'] and  secure_record['Encrypt']:
			if not _.isCrypt(path):
				__.secureFilesID = generateID(path)
			else:
				secureFiles_Decrypt( path, secure_record['Password'] )
				__.secureFilesID = generateID(path)

		elif secure_record['Encrypt'] and __.fileBackup.isPreOpen:
			if _.isCrypt(path):
				try:
					# ...
					secureFiles_Decrypt( path, secure_record['Password'] )
				except:
					_.pr('Error decrypting file:', path)
					_.isExit(__file__)

		# _.pr( 'isPreOpen', __.fileBackup.isPreOpen )


		
		if secure_record['Encrypt']:
			if not __.fileBackup.isPreOpen and not _.isCrypt(path):
				secureFiles_Encrypt( path, secure_record['Password'] )

			elif __.fileBackup.isPreOpen and _.isCrypt(path):
				secureFiles_Decrypt( path, secure_record['Password'] )

		
		


	# return True
	try:
		del _decrypt_docs.imp.indexP
		_decrypt_docs.imp.indexP = {}
		del _decrypt_docs
	except Exception as e:
		pass
	return False


def isActive(switch):
	active=False
	for rec in _.switches.all(False):
		if rec['name'] == switch:
			if rec['active']:
				active=True
	return active


__.fileBackup=_.dot()
__.fileBackup.isPreOpen = _.switches.isActive('isPreOpen')
# __.fileBackup.isPreOpen
# __.fileBackup.isPreOpen

def myFileLocationsRegister(path):
	if True:
		recs = _.getTable('myFileLocations.index')
		if not recs: recs = {}
		if type(path) == str:
			files = [path]
		for path in files:
			path = __.path(path)
			if 'Session_ID' in os.environ:
				Session_ID = os.environ['Session_ID']
			else:
				Session_ID = 'cron'
			recs[path] = {'epoch': time.time(), 'session': Session_ID}
		_.saveTable(recs,'myFileLocations.index',printThis=False, lock=True)

def action(path=None,flag=None,o=None,pre=None):
	# if _.isData():

	if _.switches.isActive('BackupRecoverScan') and '1' in _.switches.values('BackupRecoverScan'):
		bkRecoverScan(); sys.exit();
	if _.switches.isActive('BackupRecoverScan') and '2' in _.switches.values('BackupRecoverScan'):
		bkRecoverScan2(); sys.exit();
	if _.switches.isActive('BackupRecoverScan') and '3' in _.switches.values('BackupRecoverScan'):
		bkRecoverScan3(); sys.exit();
	if _.switches.isActive('BackupRecoverScan') and '4' in _.switches.values('BackupRecoverScan'):
		bkRecoverScan4(); sys.exit();
	if _.switches.isActive('BackupRecoverScan') and '5' in _.switches.values('BackupRecoverScan'):
		bkRecoverScan5(); sys.exit();
	# if _.switches.isActive('Files'):
	# 	_.switches.fieldSet( 'Input', 'active', True )
	# 	_.switches.fieldSet( 'Input', 'value', _.switches.value('Files') )
	# 	_.switches.fieldSet( 'Input', 'values', _.switches.values('Files') )
		
	global INDEX
	global _BYTES_
	global backupLog
	global txtScheduler
	if not flag is None:
		__flag__ = flag
	elif _.switches.isActive('Flag'):
		__flag__ = ' '.join(_.switches.values('Flag'))
	else:
		__flag__=''
	# __.fileBackup=_.dot()
	# print('isPreOpen-o',o)
	# print('isPreOpen',_.switches.isActive('isPreOpen'))
	# print('isPreOpen2',_.switches.isActive2('isPreOpen'))
	if pre is None:
		if _.switches.isActive('isPreOpen'): __.fileBackup.isPreOpen=True
		if _.switches.isActive2('isPreOpen'): __.fileBackup.isPreOpen=True
	else:
		__.fileBackup.isPreOpen=pre
	if not o is None and o:
		__.fileBackup.isPreOpen=True
	# print('isPreOpen3',__.fileBackup.isPreOpen)
	# print('isPreOpen',__.fileBackup.isPreOpen); sys.exit();
	# if not path is None:
	# 	if not os.path.isfile(path): return False
	# 	path = __.path(  os.path.abspath(path)  )
	# 	myFileLocationsRegister(path)
	# 	_.switches.fieldSet( 'Silent', 'active', True )
	# 	_.switches.fieldSet( 'isRunOnce', 'active', True )
	# 	_.switches.fieldSet( 'DoNotSchedule', 'active', True )
	# 	if not flag is None:
	# 		_.switches.fieldSet( 'Flag', 'active', True )
	# 		_.switches.fieldSet( 'Flag', 'value', flag )
	# 		_.switches.fieldSet( 'Flag', 'values', [flag] )



	__.openSecure = False
	__.secureFilesID = None
	# _.pr( 'ran action', __.appReg )
	# millTimeStamp = lambda: int(round(time.time() * 1000))
	# now = millTimeStamp()

	# secureFiles
	# print(_.isData())
	# for path in _.isData():
	# 	print(path)
	# return False

	now = genEpoch()
	# print(path)
	filesToProcess = []
	fromPath = False
	if _.switches.isActive('Input'):
		filesToProcess = _.switches.values('Input')
	elif not path is None:
		fromPath = True
		if not os.path.isfile(path): return False
		path = __.path(  os.path.abspath(path)  )
		myFileLocationsRegister(path)
		_.switches.fieldSet( 'Silent', 'active', True )
		_.switches.fieldSet( 'isRunOnce', 'active', True )
		_.switches.fieldSet( 'DoNotSchedule', 'active', True )
		if not flag is None:
			_.switches.fieldSet( 'Flag', 'active', True )
			_.switches.fieldSet( 'Flag', 'value', flag )
			_.switches.fieldSet( 'Flag', 'values', [flag] )
		filesToProcess.append(path)
	elif _.isData():
		filesToProcess = _.isData()

		# raw = _.isData()
		# filesToProcess = []
		# for path in raw:
		# 	path = path.strip()
		# 	if path and os.path.isfile(path):
		# 		filesToProcess.append(path)
	
	for path in filesToProcess:
		if  not os.path.isfile(path): continue
		if not os.path.getsize(path)    and     False:
			_.pr( 'Error: file empty:', path, c = 'red' )
			continue
		# if not os.path.isfile(path):
		# 	path = _.isFile(path)
		if not os.path.isfile(path):
			_.pr( 'Error: file not found:', path )
		if len(filesToProcess) > 1:
			_.pr()
			_.pr(line=1,c='yellow')
	# if _.switches.isActive('Input') or not path is None:
		# if path is None:
		# 	path = _.switches.value('Input')
		# _.pr( 'path::::', path )
		path = __.path(path)
		# print('path',path)
		# path = path.strip()
		if not os.path.isfile(path): return False
		if os.path.isfile(path):
			path = __.path(  path  )
			myFileLocationsRegister(path)
			if not isActive('Silent'):
				if _.isCrypt(path): _.pr('encrypted <-- yes ',c='red')
				# else: _.pr('encrypted <-- no ',c='green')
			# print(os.stat(path).st_size)
			if True or _.switches.isActive('Test'):
				# if not type(idCheck) == bool:
				# 	_.cp(idCheck,'darkcyan')
				_.v.secure=False
				# _.pv(_.switches.all());sys.exit();
				if secureFiles(path):
					if not __.secureFilesID is None:
						theID = __.secureFilesID
					else:
						theID = generateID(path)
					idCheck = idExist(theID, backupLog, path)
					# _.colorThis( [ 'Secure file' ], 'green' )
					bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']];
					if not isActive('Silent'):
						_.colorThis( path, 'cyan' )
					if bk:
						bk=bk[-1]
						if not isActive('Silent'): _.pr( bk, c='darkcyan' )
					# _.pr(' -- TRUE -- ')
					if not _.switches.isActive('isRunOnce'):
						if _.switches.isActive('isPreOpen'):
							txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
							if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
							if not isActive('Silent'):
								_.colorThis( 'secure open and scheduled', 'yellow' )
						# return None
						continue
				if _.v.secure and not _.switches.isActive('isRunOnce') and not isActive('Force'):
					txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
					if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
					if not isActive('Silent'):
						_.colorThis( 'secure open and scheduled', 'yellow' )
					# return None
					continue
			pathpath=path
			# print(55)
			if path in INDEX and os.path.getmtime(path) == INDEX[path]['timestamp']:
				if not isActive('Silent'):
					_.pr(path, c='cyan')
					_.pr(INDEX[path]['backup'], c='darkcyan')
					_.pr('File not modified since last backup',c='yellow')
				if _.switches.isActive('isPreOpen'):
					txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
					if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
				if fromPath:
					return INDEX[path]['backup']
				continue
			# _.pr('pre')
			# _.pr('post')
			global crypt_docs
			cryptScan=False
			if path.lower() in __.specifications['fileBackup-auto-crypt']['files']:
				cryptScan=True
			elif path.lower() in crypt_docs:
				cryptScan=True
			else:
				fo=_dir.info( path )['folder'].lower()
				if fo in __.specifications['fileBackup-auto-crypt']['folders']:
					cryptScan=True
				else:
					for fTest in __.specifications['fileBackup-auto-crypt']['folders']:
						if fTest+os.sep in fo+os.sep:
							cryptScan=True

			
			




#b)--> backup: 2022-05-07 13:36:14
			# if cryptScan:
			# 	todo = []
			# 	global doc_sep
			# 	if path.lower().endswith('.md'):
			# 		# _decrypt_docs = _.regImp( __.appReg, 'decrypt-docs-md' )
			# 		_decrypt_docs = _.regImp( __.appReg, 'decrypt-docs' )
			# 		doc_sep = '\n~~~\n'
			# 		_decrypt_docs.imp.isMD = True
			# 	else:
			# 		# _decrypt_docs.imp.isMD = False
			# 		_decrypt_docs = _.regImp( __.appReg, 'decrypt-docs' )
			# 		doc_sep = '\n__________________________________________________________________________________\n'
			# 	_.colorThis(  [ 'registered: documentation file' ], 'Background.light_blue'  )
			# 	theFile = '\n'+_.getText( path, raw=True ).replace('!vault!','!V!').replace('!VAULT!','!V!').replace('!v!','!V!').replace('!crypt!','!V!').replace('!CRYPT!','!V!')
			# 	theFile = theFile.replace('\r','')
			# 	# tF = theFile
			# 	if path.lower().endswith('.md'):
			# 		todo.append('\n___\n')
			# 		# _.pr('A')
			# 		theFile = _decrypt_docs.imp.md_clean(theFile)
			# 		# _.pr('B')
			# 		# if not tF == theFile:
			# 		#   _.saveText(theFile,path)
			# 		#   _.cp('FIXED: .md lines','yellow')
			# 	elif not path.lower().endswith('.md'):
			# 		while '___________________________________________________________________________________' in theFile:
			# 			theFile = theFile.replace('___________________________________________________________________________________','__________________________________________________________________________________')
			# 		while '\t\n' in theFile:
			# 			theFile = theFile.replace('\t\n','\n')
			# 		while ' \n' in theFile:
			# 			theFile = theFile.replace(' \n','\n')
			# 		# if not tF == theFile:
			# 		#   _.cp('FIXED: space after line end','yellow')
			# 		#   _.saveText(theFile,path)

			# 	crypy=__.specifications['fileBackup-auto-crypt']['crypt-segment']
				
			# 	todo.append(doc_sep)
			# 	for doc_sep_ in todo:
			# 		segments=theFile.split(doc_sep_)
			# 		newTemp=[]
			# 		crypt_segment = False
			# 		for segment in segments:
			# 			# _.pr(segment.split('\n')[0])
			# 			# if crypy+' ' in segment or crypy+'\n' in segment or crypy+'\t' in segment:
			# 			if crypy+' ' in segment.split('\n')[0] or crypy+'\n' in segment.split('\n')[0]+'\n' or crypy+'\t' in segment.split('\n')[0]:
			# 				segment=segment.replace('!V!','')
			# 				segy=[]
			# 				for si, segsy in enumerate(segment.split('\n')):
			# 					if not si:
			# 						segy.append(  segsy  )
			# 					else:
			# 						if _decrypt_docs.imp.identify(segsy):
			# 							segy.append(  segsy  )
			# 						else:
			# 							segy.append(  _blowfish.encrypt( segsy, _vault.key() )  )

			# 					crypt_segment = True
			# 				segment = '\n'.join( segy )
			# 			newTemp.append(segment)
			# 		theFile=doc_sep_.join(newTemp)
			# 	if path.lower().endswith('.md'):
			# 		# _.pr(1)
			# 		theFile = _decrypt_docs.imp.vcrypyAA(theFile)
			# 		theFile = _decrypt_docs.imp.vcrypyB(theFile)
			# 		# _.pr(2)
#e)--> backup: 2022-05-07 13:36:14

#b)--> backup: 2022-07-26 22:18:12
			# return
			if cryptScan:
				todo = []
				global doc_sep
				if path.lower().endswith('.md'):
					# while theFile.count('~~~~'): theFile=theFile.replace('~~~~','~~~')
					# _decrypt_docs = _.regImp( __.appReg, 'decrypt-docs-md' )
					_decrypt_docs = _.regImp( __.appReg, 'decrypt-docs' )
					doc_sep = '\n~~~\n'
					_decrypt_docs.imp.isMD = True
				else:
					# _decrypt_docs.imp.isMD = False
					_decrypt_docs = _.regImp( __.appReg, 'decrypt-docs' )
					doc_sep = '\n__________________________________________________________________________________\n'
				_.colorThis(  [ 'registered: documentation file' ], 'Background.light_blue'  )
				theFile = '\n'+_.getText( path, raw=True ).replace('!vault!','!V!').replace('!VAULT!','!V!').replace('!v!','!V!').replace('!crypt!','!V!').replace('!CRYPT!','!V!')
				theFile = theFile.replace('\r','')
				while '\t\n' in theFile:
					theFile = theFile.replace('\t\n','\n')
				while ' \n' in theFile: theFile = theFile.replace(' \n','\n')
				

				#b) converting backticks to tildes
					#method:~)--> while '\n```' in theFile: theFile = theFile.replace('\n```','\n~~~')
					#epoch) 1660600468.2705994
				theFile='\n'+theFile
				while '\n```' in theFile: theFile = theFile.replace('\n```','\n~~~')
				theFile=theFile[1:]
					#e) converting backticks to tildes



				# tF = theFile
				if path.lower().endswith('.md'):
					todo.append('\n___\n')
					# _.pr('A')
					theFile = _decrypt_docs.imp.md_clean(theFile)
					# _.pr('B')
					# if not tF == theFile:
					#   _.saveText(theFile,path)
					#   _.cp('FIXED: .md lines','yellow')
				elif not path.lower().endswith('.md'):
					while '___________________________________________________________________________________' in theFile:
						theFile = theFile.replace('___________________________________________________________________________________','__________________________________________________________________________________')
					while '\t\n' in theFile:
						theFile = theFile.replace('\t\n','\n')
					while ' \n' in theFile:
						theFile = theFile.replace(' \n','\n')
					# if not tF == theFile:
					#   _.cp('FIXED: space after line end','yellow')
					#   _.saveText(theFile,path)

				crypy=__.specifications['fileBackup-auto-crypt']['crypt-segment']
				md_cleaner_ran=False
				if path.lower().endswith('.md') and not theFile.count('\n~~~\n') == theFile.count('\n~~~') :
					md_cleaner_ran=True
					md_index={}
					md_lines=[]
					for mdi,line in enumerate(theFile.split('\n')):
						if line.startswith('~~~') and not line.endswith('~~~'): line.replace('~',''); md_index[mdi]=line; line='~~~';
						elif line.startswith('~~~'): line = '~~~'
						md_lines.append(line)
					theFile = '\n'.join(md_lines)

				todo.append(doc_sep)
				for doc_sep_ in todo:
					segments=theFile.split(doc_sep_)
					newTemp=[]
					crypt_segment = False
					for segment in segments:
						# _.pr(segment.split('\n')[0])
						# if crypy+' ' in segment or crypy+'\n' in segment or crypy+'\t' in segment:
						if crypy+' ' in segment.split('\n')[0] or crypy+'\n' in segment.split('\n')[0]+'\n' or crypy+'\t' in segment.split('\n')[0]:
							segment=segment.replace('!V!','')
							segy=[]
							for si, segsy in enumerate(segment.split('\n')):
								if not si:
									segy.append(  segsy  )
								else:
									if _decrypt_docs.imp.identify(segsy):
										segy.append(  segsy  )
									else:
										segy.append(  _blowfish.encrypt( segsy, _vault.key() )  )

								crypt_segment = True
							segment = '\n'.join( segy )
						newTemp.append(segment)
					theFile=doc_sep_.join(newTemp)
				if path.lower().endswith('.md'):
					if md_cleaner_ran:
						md_lines=[]
						for mdi,line in enumerate(theFile.split('\n')):
							if mdi in md_index: line = line+md_index[mdi]
							md_lines.append(line)
						theFile = '\n'.join(md_lines)
					# _.pr(1)
					theFile = _decrypt_docs.imp.vcrypyAA(theFile)
					theFile = _decrypt_docs.imp.vcrypyB(theFile)
					# _.pr(2)
#e)--> backup: 2022-07-26 22:18:12
#b)--> original
			# if cryptScan:
			# 	todo = []
			# 	global doc_sep
			# 	if path.lower().endswith('.md'):
			# 		# while theFile.count('~~~~'): theFile=theFile.replace('~~~~','~~~')
			# 		# _decrypt_docs = _.regImp( __.appReg, 'decrypt-docs-md' )
			# 		_decrypt_docs = _.regImp( __.appReg, 'decrypt-docs' )
			# 		doc_sep = '\n~~~\n'
			# 		_decrypt_docs.imp.isMD = True
			# 	else:
			# 		# _decrypt_docs.imp.isMD = False
			# 		_decrypt_docs = _.regImp( __.appReg, 'decrypt-docs' )
			# 		doc_sep = '\n__________________________________________________________________________________\n'
			# 	_.colorThis(  [ 'registered: documentation file' ], 'Background.light_blue'  )
			# 	theFile = '\n'+_.getText( path, raw=True ).replace('!vault!','!V!').replace('!VAULT!','!V!').replace('!v!','!V!').replace('!crypt!','!V!').replace('!CRYPT!','!V!')
			# 	theFile = theFile.replace('\r','')
			# 	while '\t\n' in theFile:
			# 		theFile = theFile.replace('\t\n','\n')
			# 		while ' \n' in theFile: theFile = theFile.replace(' \n','\n')
			# 	# tF = theFile
			# 	if path.lower().endswith('.md'):
			# 		todo.append('\n___\n')
			# 		# _.pr('A')
			# 		theFile = _decrypt_docs.imp.md_clean(theFile)
			# 		# _.pr('B')
			# 		# if not tF == theFile:
			# 		#   _.saveText(theFile,path)
			# 		#   _.cp('FIXED: .md lines','yellow')
			# 	elif not path.lower().endswith('.md'):
			# 		while '___________________________________________________________________________________' in theFile:
			# 			theFile = theFile.replace('___________________________________________________________________________________','__________________________________________________________________________________')
			# 		while '\t\n' in theFile:
			# 			theFile = theFile.replace('\t\n','\n')
			# 		while ' \n' in theFile:
			# 			theFile = theFile.replace(' \n','\n')
			# 		# if not tF == theFile:
			# 		#   _.cp('FIXED: space after line end','yellow')
			# 		#   _.saveText(theFile,path)

			# 	crypy=__.specifications['fileBackup-auto-crypt']['crypt-segment']
			# 	md_cleaner_ran=False
			# 	if path.lower().endswith('.md') and not theFile.count('\n~~~\n') == theFile.count('\n~~~') :
			# 		md_cleaner_ran=True
			# 		md_index={}
			# 		md_lines=[]
			# 		for mdi,line in enumerate(theFile.split('\n')):
			# 			if line.startswith('~~~') and not line.endswith('~~~'): line.replace('~',''); md_index[mdi]=line; line='~~~';
			# 			elif line.startswith('~~~'): line = '~~~'
			# 			md_lines.append(line)
			# 		theFile = '\n'.join(md_lines)

			# 	todo.append(doc_sep)
			# 	for doc_sep_ in todo:
			# 		segments=theFile.split(doc_sep_)
			# 		newTemp=[]
			# 		crypt_segment = False
			# 		for segment in segments:
			# 			# _.pr(segment.split('\n')[0])
			# 			# if crypy+' ' in segment or crypy+'\n' in segment or crypy+'\t' in segment:
			# 			if crypy+' ' in segment.split('\n')[0] or crypy+'\n' in segment.split('\n')[0]+'\n' or crypy+'\t' in segment.split('\n')[0]:
			# 				segment=segment.replace('!V!','')
			# 				segy=[]
			# 				for si, segsy in enumerate(segment.split('\n')):
			# 					if not si:
			# 						segy.append(  segsy  )
			# 					else:
			# 						if _decrypt_docs.imp.identify(segsy):
			# 							segy.append(  segsy  )
			# 						else:
			# 							segy.append(  _blowfish.encrypt( segsy, _vault.key() )  )

			# 					crypt_segment = True
			# 				segment = '\n'.join( segy )
			# 			newTemp.append(segment)
			# 		theFile=doc_sep_.join(newTemp)
			# 	if path.lower().endswith('.md'):
			# 		if md_cleaner_ran:
			# 			md_lines=[]
			# 			for mdi,line in enumerate(theFile.split('\n')):
			# 				if mdi in md_index: line = line+md_index[mdi]
			# 				md_lines.append(line)
			# 			theFile = '\n'.join(md_lines)
			# 		# _.pr(1)
			# 		theFile = _decrypt_docs.imp.vcrypyAA(theFile)
			# 		theFile = _decrypt_docs.imp.vcrypyB(theFile)
			# 		md_index={'zero':0}
			# 		md_lines=[0,0,0]
			# 		del md_index
			# 		del md_lines
			# 		# _.pr(2)
#e)--> original

				if crypt_segment or __.specifications['fileBackup-auto-crypt']['scanA'] in theFile  or  __.specifications['fileBackup-auto-crypt']['scanB'] in theFile or crypy in theFile:



					# _.pr(  'secure line found'  )
					_.colorThis(  [ 'scan: positive, found sensitive data' ], 'Background.red'  )
					_.colorThis(  [ 'securing data' ], 'Background.green'  )
					newFile = []
					if type(theFile) == list:
						theFile = '\n'.join(theFile)
					for line in theFile.split('\n'):
						if __.specifications['fileBackup-auto-crypt']['scanA'] in line  or  __.specifications['fileBackup-auto-crypt']['scanB'] in line:

							# line = line.replace(  '\t', ''  )
							# line = _str.cleanBE( line, ' ' )
							if __.specifications['fileBackup-auto-crypt']['scanA'] in line:
								line = line.replace(  __.specifications['fileBackup-auto-crypt']['scanA'], ''  )

								# line = _str.cleanBE( line, ' ' )
								# line = _str.cleanBE( line, '\t' )
								# line = _str.cleanBE( line, ' ' )
								# line = _str.cleanBE( line, '\t' )
								line = _blowfish.encrypt(    line    ,    _vault.key()    )

						# elif __.specifications['fileBackup-auto-crypt']['scanB'] in line:
						#   line = line.replace(  __.specifications['fileBackup-auto-crypt']['scanB']+' ', __.specifications['fileBackup-auto-crypt']['scanB']  )
						#   line = line.replace(  __.specifications['fileBackup-auto-crypt']['scanB']+' ', __.specifications['fileBackup-auto-crypt']['scanB']  )
						#   line = line.replace(  __.specifications['fileBackup-auto-crypt']['scanB']+' ', __.specifications['fileBackup-auto-crypt']['scanB']  )
						#   line = line.replace(  __.specifications['fileBackup-auto-crypt']['scanB']+' ', __.specifications['fileBackup-auto-crypt']['scanB']  )
						#   line = line.replace(  ' '+__.specifications['fileBackup-auto-crypt']['scanB'], __.specifications['fileBackup-auto-crypt']['scanB']  )
						#   line = line.replace(  ' '+__.specifications['fileBackup-auto-crypt']['scanB'], __.specifications['fileBackup-auto-crypt']['scanB']  )
						#   line = line.replace(  ' '+__.specifications['fileBackup-auto-crypt']['scanB'], __.specifications['fileBackup-auto-crypt']['scanB']  )
						#   line = line.replace(  ' '+__.specifications['fileBackup-auto-crypt']['scanB'], __.specifications['fileBackup-auto-crypt']['scanB']  )
						#   if '>'+__.specifications['fileBackup-auto-crypt']['scanB'] in line:
						#       lineP = line.split( '>'+__.specifications['fileBackup-auto-crypt']['scanB'] )
						#       # _.pr( lineP )
						#       # _.pr( line )
						#       line = _str.cleanBE( line, ' ' )
						#       line = _str.cleanBE( line, '\t' )
						#       line = _str.cleanBE( line, ' ' )
						#       line = _str.cleanBE( line, '\t' )
						#       line = _blowfish.encrypt(    _str.cleanBE( lineP[1], ' ' )    ,    _str.cleanBE( lineP[0], ' ' )    )
						#   if __.specifications['fileBackup-auto-crypt']['scanB']+'<' in line:
						#       lineP = line.split( __.specifications['fileBackup-auto-crypt']['scanB']+'<' )
						#       # _.pr( lineP )
						#       # _.pr( line )
						#       line = _blowfish.encrypt(    _str.cleanBE( lineP[0], ' ' )    ,    _str.cleanBE( lineP[1], ' ' )    )




						newFile.append(  line  )
					
					pass
					tehFile = '\n'.join(newFile)
					if tehFile.startswith('\n'):
						tehFile = tehFile[1:]
					if tehFile.startswith('\n'):
						tehFile = tehFile[1:]
					
					# focus()
					_.saveText(  tehFile, path  )
		
		library = _.getTableDB( 'library-path.hash' )
		if path in library:
			libFile = library[path]
			tmpA = path.split(os.sep)
			tmpA.reverse()
			tmpB = tmpA.pop(0)

			libFile = _v.library + os.sep + libFile['id']+'-'+libFile['label']+'-'+tmpB
			
			if not __.openSecure:
				copyThis=True
				if _.v.secure and not _.isCrypt(path):copyThis=False
				if copyThis:
					if os.stat(path).st_size > 5242880: # 5mb
						_.compress2( path,  libFile)
					else:
						copyfile( path,  libFile)
						# if _.switches.isActive('EncryptBackup') or isActive('EncryptBackup'):
						# 	_.encrypt( libFile )
						# 	if not isActive('Silent'):
						# 		_.pr('backup encrypted',c='Background.purple')
				else:
					_.pr('not encrypted',c='red')
					if _.switches.isActive('isPreOpen'):
						txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
						if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
					if fromPath:
						return path
					continue
					# sys.exit()

			if os.path.isfile(libFile):
				if os.path.isfile(path):
					fMod = os.path.getmtime( path )
					os.utime(libFile,(fMod, fMod))


		txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
		if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
		if __.openSecure:
			if not isActive('Silent'):
				_.colorThis( 'secure open and scheduled', 'yellow' )

		if not isActive('Silent'):
			_.colorThis( [  path  ], 'cyan' )
			
			# _.pr(path)
			# sys.exit()
			# _.pr(path)


		name = Path(path).name
		if not os.path.isfile(path):
			_.colorThis( [  'Does not exist:', path  ], 'red' )
			continue
			# _.pr('Does not exist')
			# txtScheduler = _.getTable( 'fileBackupSchedule.json' )
			# path = os.path.abspath(path)
			# txtScheduler.append( { 'timestamp': genEpoch(), 'file': path, 'status': 0, 'app': 'fileBackup', 'group': 0 } )
			if not _.switches.isActive('DoNotSchedule'):
				_.colorThis( [  'Scheduled'  ], 'purple' )
				
		else:
			# if _.switches.isActive('PythonDocumentation'): PRE_BACKUP_PROCESSING( path )

			# idCheck = idExist(theID, backupLog, path)
			# if not type(idCheck) == bool:
			# os.stat(path).st_size
			# if path in INDEX and INDEX[path]['id'] == theID:
			modifiedRaw = os.path.getmtime(path)
			byte = os.stat(path).st_size
			T42_HB = False
			if not path in INDEX:
				if pathpath in INDEX: path=pathpath
				elif pathpath.lower() in INDEX: path=pathpath.lower()
				elif __.path(pathpath) in INDEX: path=__.path(pathpath)
			# path=pathpath
			# _.pv(INDEX[list(INDEX.keys())[0]]);sys.exit();
			# if not _.switches.isActive('isRunOnce'):
			# if not path in INDEX:
			# 	txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
			# 	if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
			# 	return None
			if path in INDEX and not os.path.isfile(INDEX[path]['backup']):
				temp=_v.stmp+os.sep+'backup_default'
				if not os.path.isfile(temp):
					_.saveText('{1bf18757-ea88-41fb-b046-2bd2080f1735-c09afdb6-2241-4a49-aa45-da436bbe2abb}',temp)
				INDEX[path]['backup']=temp
			T42_HB = False
			if path in INDEX and path in INDEX and os.stat(INDEX[path]['backup']).st_size  == byte:
				T42_HB = True
				if not byte < _BYTES_:
					if not isActive('Silent'):
						_.colorThis( INDEX[path]['backup'], 'darkcyan' )
						_.pr( 'Has Backup *', c='yellow' )
						# _.pr( 'Has Backup',_.formatSize(byte), c='yellow' )
					if _.switches.isActive('isPreOpen'):
						txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
						if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
					return INDEX[path]['backup']					
				else:
					if not __.secureFilesID is None:
						theID = __.secureFilesID
					else:
						theID = generateID(path)
					if not INDEX[path]['id'] == theID:
						T42_HB = False
			if T42_HB:
				if not isActive('Silent'):
					_.colorThis( INDEX[path]['backup'], 'darkcyan' )
					_.colorThis( 'Has Backup', 'yellow' )
				if _.switches.isActive('isPreOpen'):
					txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
					if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
				if fromPath:
					return INDEX[path]['backup']
				continue
				# if _.switches.isActive('Flag'):
				# 	thisFlag = _.switches.value('Flag')
				# 	_bkLog.switch( 'Flag', thisFlag )
				# 	_bkLog.imp.addFlagIfHasBackup( idCheck )
				# _.pr(idCheck)
			else:
				# print(1005)
				modified = formatDate(modifiedRaw)
				if _mime.isText(path) and _.isTextFi(path,100):
					newname = _v.myTXT + os.sep + str(now) + '-' + modified +  '-' + name
					mime = 'text'
				else:
					mime = 'binary'
					if not isActive('Silent'):
						_.colorThis( [  '********************'  ], 'yellow' )
						_.colorThis( [  '   File is BINARY'  ], 'yellow' )
						_.colorThis( [  '********************'  ], 'yellow' )
					newname = _v.myBIN + os.sep + str(now) + '-' + modified +  '-'+ _md5.string(path,'sha1') +'-'+ name
				if not __.secureFilesID is None:
					theID = __.secureFilesID
				else:
					theID = generateID(path)
				idCheck = idExist(theID, backupLog, path)
				if not type(idCheck) == bool:
					if not isActive('Silent'):
						if path in INDEX:
							_.colorThis( INDEX[path]['backup'], 'darkcyan' )
						_.colorThis( 'Backup ID found in older backup', 'yellow' )
					if _.switches.isActive('isPreOpen'):
						txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
						if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
					if path in INDEX:
						if fromPath:
							return INDEX[path]['backup']
						continue
					else:
						if fromPath:
							return path
						continue

				


				name = ''
				parts = os.path.abspath(path).split(os.sep)
				parts.reverse()
				name = parts.pop(0)

				
				# changed timestamp on 1620919454
				#   previously...    'timestamp': now 


				if _.switches.isActive('isRunOnce'):
					log = { 'id': theID, 'timestamp': modifiedRaw, 'file': os.path.abspath(path), 'backup': newname,'mime': mime, 'status': 100, 'name': name, 'log': '', 'flag':__flag__ }
				else:
					log = { 'id': theID, 'timestamp': modifiedRaw, 'file': os.path.abspath(path), 'backup': newname,'mime': mime, 'status': 1, 'name': name, 'log': '', 'flag':__flag__ }
				log = log_default_fields(log)
				if _.switches.isActive('Session'):
					log['session'] = _.switches.value('Session')
				else:
					log['session'] = __.Session_ID
				if _.switches.isActive('Flag'):
					if len( _.switches.value('Flag')) == 0:
						log['flag'] = 'F'
					else:
						log['flag'] = _.switches.value('Flag')
				log = log_default_fields(log)
				backupLog.append(log)
				# _.saveCSV(   backupLog, 'fileBackup.csv',  p=0 )
				copyThis=True
				if _.v.secure and not _.isCrypt(path):copyThis=False
				if not copyThis:
					_.pr('not encrypted',c='red')

					txtScheduler = _.getTable( 'fileBackupSchedule.json' )
					txtScheduler.append( { 'timestamp': genEpoch(), 'file': __.path(path), 'status': 0, 'app': 'fileBackup', 'group': 0, 'session': __.Session_ID } )
					if not _.switches.isActive('BypassScheduler'): _.saveTable( txtScheduler,'fileBackupSchedule.json', p=0, lock=True )
					if fromPath:
						return path
					continue
					# sys.exit()
				try:
					if os.stat(path).st_size > 5242880: # 5mb
						result = _.compress2( path,  libFile)
					else:
						result = copyfile(path, newname)
						if _.switches.isActive('EncryptBackup') or isActive('EncryptBackup'):
							_.encrypt( newname )
							if not isActive('Silent'):
								_.pr('backup encrypted',c='Background.purple')
					# for i,row in enumerate(backupLog):
					# 	try:
					# 		if not type(backupLog[i]['flag']) == str:
					# 			backupLog[i]['flag'] = ''
					# 	except Exception as e:
					# 		backupLog[i]['flag'] = ''
					# _.pr('logs',c='gray')
					# _.pr('saving',c='gray')
					_.saveTable( backupLog, 'fileBackup.json', p=0, lock=True )
					# _.pr('saving..',c='gray')
					# _.pr('.json',c='gray')
					# _.saveCSV(   backupLog, 'fileBackup.csv',  p=0 )
					# _.pr('saving...',c='gray')
					# _.pr('.csv',c='gray')
					# _.saveYML(   backupLog, 'fileBackup.yml',  p=0 )
					# _.pr('.yml',c='gray')
					# _.pr('db saved',c='gray')
				except Exception as e:
					result = 'Error'
				if _.switches.isActive('Result'):
					_.pr(result)
				else:
					pass
					# _.pr(result)
					INDEX[path]=log
					if not isActive('Silent'):
						_.cp(newname,'darkcyan')
						_.printBold('Backup Successful', 'green')
					# _.pr(newname)
					if fromPath:
						return newname
					continue
	return True




__.specifications['fileBackup-auto-crypt'] = {

										'scanA': '!V!',
										'scanB': '!VAULT!',
										'crypt-segment': '#crypt',


										'files': [
														_v.myHome  +os.sep+  'projects'  +os.sep+  'project-log.txt',
														_v.ww  +os.sep+  'bash'  +os.sep+    'notes'  +os.sep+  'RT-SCRAP-'+ _v.unixIDs[6] +'.txt',
										],

										'folders': [
														# _v.ww  +os.sep+  'documentation'  ,
														_v.ww  +os.sep+  'bash'+os.sep+'notes'  ,
										],
}

temp7 = _.getTable('crypt-docs.list')
for item in temp7:
	__.specifications['fileBackup-auto-crypt']['files'].append(item.lower())
del temp7

# C:\Users\Scott\.rt\profile\projects\project-log.txt

for i,x in enumerate(__.specifications['fileBackup-auto-crypt']['files']):
	__.specifications['fileBackup-auto-crypt']['files'][i] = __.specifications['fileBackup-auto-crypt']['files'][i].lower()
for i,x in enumerate(__.specifications['fileBackup-auto-crypt']['folders']):
	__.specifications['fileBackup-auto-crypt']['folders'][i] = _str.replaceDuplicate(__.specifications['fileBackup-auto-crypt']['folders'][i].lower(),os.sep)

# _.pv(__.specifications)


# for i,x in enumerate(__.specifications['fileBackup-auto-crypt']['files']):
#   _.pr(  'f:', x  )
# _.pr()
# path = _.switches.value('Input')
# path = os.path.abspath(path)
# _.pr( 'i:',path )
# if path.lower() in __.specifications['fileBackup-auto-crypt']['files']:
#   _.pr( 'file match' )
# _.pr()
# sys.exit()

try:
	__.v.secure.files
except Exception as e:
	secure_files = _.regImp( __.appReg, 'secureFiles' )
	secure_files.imp.scanFolders(sync=False, meta=True)
	del secure_files
	




import _rightThumb._vault as _vault
import _rightThumb._encryptString as _blowfish
import _rightThumb._dir as _dir

try:
	_cryptFile = _.regImp( __.appReg, 'cryptFile' )
	_cryptFile.switch( 'NoExt' )
	# if _.switches.isActive('Clean'):
	_cryptFile.switch( 'Clean' )
	_cryptFile.imp.appDBA = _cryptFile.focus
except Exception as e:
	_.colorThis( 'Error: missing pyAesCrypt', 'red' )

_BYTES_ = 10240
crypt_docs = _.getTable('crypt-docs.list')
backupLog = _.getTable('fileBackup.json')
txtScheduler = _.getTable( 'fileBackupSchedule.json' )
INDEX={}
for rec in backupLog:
	if not rec['file'] in INDEX:
		INDEX[rec['file']] = rec
	if rec['timestamp'] > INDEX[rec['file']]['timestamp']:
		INDEX[rec['file']] = rec
focus()
_decrypt_docs = None
doc_sep = '\n__________________________________________________________________________________\n'
########################################################################################
def build2m():
	import _rightThumb._md5 as _md5
	if False:
		b2m = _.getTable('build2m.dex')
		if b2m: return b2m
		fi2m =_.getText2( 'C:\\Users\\Scott\\.rt\\profile\\backup\\txt\\2m','list' )
		bm2 = {}
		for i in fi2m:
			i = i.strip()
			_.pr( i )
			if not os.path.isfile( i ): continue
			if _.IS( i, 'gzip' ):
				gzip=True
				_.decompress( i )
			else:
				gzip=False
			md5 = _md5.md5File( i )
			id = _md5.md52GUID(md5,True)
			if gzip: _.compress( i )
			bm2[id] = {
				'id': id,
				'file': None,
				'backup': i,
				'md5': md5,
			}
		_.saveTable(bm2,'build2m.dex', lock=True)
		return bm2
	b2m =None
def bkRecoverListen(id,path):
	return None
	global b2m
	changed = False
	if b2m is None: b2m = build2m()
	if id in b2m:
		if b2m[id]['file'] is None:
			changed = True
		b2m[id]['file'] = path
	if changed:
		_.saveTable(b2m,'build2m.dex', lock=True)

def bkRecoverScan():
	changed = False
	b2m = build2m()
	dex = {}
	for id in b2m:
		dex[b2m[id]['backup']] = b2m[id]['id']
	disregard = []
	print('build2m')
	backupLog = _.getTable('fileBackup.json')
	print('backupLog')
	for rec in backupLog:
		if rec['backup'] in dex:
			changed = True
			disregard.append(dex[rec['backup']])
		print(rec['file'])
		if rec['id'] in b2m:
			r = b2m[rec['id']]
			if r['file'] is None:
				changed = True
			b2m[rec['id']]['file'] = rec['file']
	if changed:
		if disregard:
			ind = {}
			for id in b2m:
				if not id in disregard:
					ind[id] = b2m[id]
			b2m = ind				
		_.saveTable(b2m,'build2m.dex', lock=True)

def bkRecoverScan2():
	scheduleLog = _.getTable('2024.04.20-fileBackupSchedule.json')
	b2m = build2m()
	dex = {}
	for id in b2m: dex[extract_filename(__.path(b2m[id]['backup'],file=True))] = b2m[id]['id']
	for rec in scheduleLog:
		fi = __.path(rec['file'],file=True)
		if fi in dex:
			md5 = _md5.md5File( rec['file'] )
			id = _md5.md52GUID(md5,True)
			if md5 != dex[fi]:
				if b2m[dex[fi]]['file'] is None:
					bkRecoverListen(id,rec['file'])
			file = b2m[dex[fi]]['backup']
			if is_probable_modified_version(rec['file'],file):
				if b2m[dex[fi]]['file'] is None:
					b2m[dex[fi]]['file'] = rec['file']
					_.saveTable(b2m,'build2m.dex', lock=True)

def extract_filename(backup_filename):
	import re
	match = re.search(r'\d{10}\.\d{7}-\d{4}_\d{2}_\d{2}-\d{2}_\d{2}_\d{2}-(.+)$', backup_filename)
	if match:
		return match.group(1)
	return None

def is_probable_modified_version(file_path, backup_path):


	try:
		# Read and tokenize both files
		with open(file_path, 'r', encoding='utf-8') as file:
			file_words = file.read().split()
			file_length = len(file_words)

		with open(backup_path, 'r', encoding='utf-8') as backup:
			backup_words = backup.read().split()
			backup_length = len(backup_words)

		# Compute the intersection and length percentage
		common_words = set(file_words).intersection(set(backup_words))
		word_match_percentage = (len(common_words) / len(set(backup_words))) * 100
		length_match_percentage = (min(file_length, backup_length) / max(file_length, backup_length)) * 100

		# Determine if the file is a probable modified version
		if word_match_percentage >= 80 and length_match_percentage >= 90:
			print(f"Word Match: {word_match_percentage:.2f}%, Length Match: {length_match_percentage:.2f}%")
			return True
		else:
			print(f"Word Match: {word_match_percentage:.2f}%, Length Match: {length_match_percentage:.2f}%")
			return False
	except Exception as e:
		print(f"An error occurred: {e}")
		return False

def bkRecoverScan3():
	# print('bkRecoverScan3'); sys.exit();
	b2m = build2m()
	dex = {}
	changed = False
	for id in b2m:
		dex[extract_filename(__.path(b2m[id]['backup'],file=True))] = b2m[id]
		epoch, date_str = extract_date_from_filename(b2m[id]['backup'])
		dex[extract_filename(__.path(b2m[id]['backup'],file=True))]['timestamp'] = epoch
		dex[extract_filename(__.path(b2m[id]['backup'],file=True))]['date'] = date_str
		dex[extract_filename(__.path(b2m[id]['backup'],file=True))]['mod'] = _.mod(b2m[id]['backup'])
		dex[extract_filename(__.path(b2m[id]['backup'],file=True))]['bytes'] = _.BYTES(b2m[id]['backup'])
		if not 'date' in b2m[id]: changed = True
		b2m[id]['backedUp'] = float(__.path(b2m[id]['backup'],file=True).strip('-')[0])
		b2m[id]['timestamp'] = epoch
		b2m[id]['date'] = date_str
		b2m[id]['mod'] = _.mod(b2m[id]['backup'])
		b2m[id]['bytes'] = _.BYTES(b2m[id]['backup'])
	if changed:
		_.saveTable(b2m,'build2m.dex', lock=True)
	mod = _.getText2('C:\\Users\\Scott\\.rt\\profile\\backup\\txt\\mod','text')
	mod = mod.strip()
	files = mod.split('\n')
	for path in files:
		if not os.path.isfile(path): continue
		path = path.strip()
		Lfi = __.path(path,file=True)
		if Lfi in dex:
			if dex[Lfi]['file'] is None:
				Lmod = _.mod(path)
				Ldate = format_date_from_epoch(_.mod(path))
				Lbytes = _.BYTES(path)
				if Lbytes > 30 and Lbytes == dex[Lfi]['bytes']:
					b2m[dex[Lfi]['id']]['file'] = path
					_.saveTable(b2m,'build2m.dex', lock=True)
					continue
				if Ldate == dex[Lfi]['date']:
					b2m[dex[Lfi]['id']]['file'] = path
					_.saveTable(b2m,'build2m.dex', lock=True)
					continue
def bkRecoverScan4():
	b2m = build2m()
	found = {
		'valid': 0,
		'None': 0,
	}
	for id in b2m:
		if b2m[id]['file'] is None:
			found['None'] += 1
		else:
			found['valid'] += 1
	_.pv(found)
	_.pr()
	_.pr('',_.percentageDiffIntAuto(found['valid'],found['None']),'%',c='yellow')
def bkRecoverScan5():
	b2m = build2m()
def extract_date_from_filename(backup_filename):
	import re
	import time
	from datetime import datetime
	# Extract the date and time part using regex
	match = re.search(r'-([0-9]{4}_[0-9]{2}_[0-9]{2}-[0-9]{2}_[0-9]{2}_[0-9]{2})-', backup_filename)
	if match:
		date_str = match.group(1)
		# Convert the date string to a datetime object
		date_time_obj = datetime.strptime(date_str, '%Y_%m_%d-%H_%M_%S')
		# Convert datetime object to epoch (float)
		epoch = date_time_obj.timestamp()
		return epoch, date_str
	return None, None

def format_date_from_epoch(epoch):
	import time
	from datetime import datetime
	# Convert epoch to datetime object
	date_time_obj = datetime.fromtimestamp(epoch)
	# Format the datetime object to match the filename style
	formatted_date = date_time_obj.strftime('%Y_%m_%d-%H_%M_%S')
	return formatted_date

def backupRecoverFields(rec):
	fields = {
		"id": rec['id'],
		"timestamp": rec['timestamp'],
		"file": rec['file'],
		"backup": rec['backup'],
		"mime": "text",
		"status": 100,
		"session": "",
		"version": "0.0.0.1",
		"v": 0,
		"v1": 0,
		"v2": 0,
		"v3": 1,
		"name": rec['file'].split(os.sep)[-1],
		"flag": "log recovery"
	}

########################################################################################

# flag validator
# _bkLog.imp.validateFlag

# _decrypt_docs.imp.
# secureFiles (

# fileBackup

# SKIPPED PRE_BACKUP_PROCESSING

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()

# isTextFi