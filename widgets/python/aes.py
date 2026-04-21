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


##################################################
# import sys, time
##################################################
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');
##################################################

# app_navigator: switches
def sw():
	pass
	#b)--> examples
		##  -->    p SwitchGroupsExamples   <--
	# #e)--> examples

	_.switches.register( 'Encrypt', '-e,-en,-encrypt','Text To Encrypt / '+_.pr0('Leave Blank if you specify a -file') )
	_.switches.register( 'Decrypt', '-d,-de,-decrypt','Text To Decrypt /'+_.pr0('Leave Blank if you specify a -file') )
	_.switches.register( 'Save', '-save','file.zip.aes file.zip' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.aes files.txt' )
	_.switches.register( 'BinaryFile', '-bin','file.aes files.txt' )
	_.switches.register( 'Clipboard', '-clip,-clipboard' )
	_.switches.register( 'Password', '-p,-password','Password' )
	_.switches.register( 'SecureDeleteFile', '-rm,-del,-delete,--SecureDelete','file.txt: '+_.pr0('If used. Use no other switches') )
	_.switches.register( 'PasswordMD5', '-md5','' )


_._default_settings_()
# __.setting('omit-switch-triggers',['Ago'])
# __.setting('omit-functions',['myFolderLocations','aliasesFo'])
# if not 'Ago' in __.setting('omit-switch-triggers',d=[]): pass
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
# __.setting('receipt-log',True)
# __.setting('receipt-file',True)
# __.setting('myFileLocations-skip-validation',False)
# __.setting('require-pipe',False)
# __.setting('require-pipe||file',False)
# __.setting('pre-error',False)
# __.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'aes.py',
	'description': 'Aes Everywhere, Encryption and Decryption tool',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'examples': [
						'',
						_.hp('p aes -password MySecret -en Here is a string to encrypt'),
						_.hp('p aes -password MySecret -de "U2FsdGVkX19RsryFcznUu5XkDcmF+PEbp9canstZyHX1wRTzAcFVJiI5Vng3iGT2"'),
						'',
						_.hp('p aes -password MySecret -en -f passwords.txt -save passwords.txt.aes'),
						_.hp('p aes --SecureDelete passwords.txt'),
						_.hp('p aes -password MySecret -de -f passwords.txt.aes | p line + Bank of America'),
						_.hp('p aes -password MySecret -de -f passwords.txt.aes -save passwords.txt'),
						'',
						_.pr('Copy a string to encrypt to the clipboard',c='yellow',p=0)+_.pr('     <-------', c='Background.red',p=0)+_.pr(' This', c='green',p=0),
						_.hp('\tp aes -password MySecret -en -clip'),
						_.pr('Then paste the encrypted string where needed', c='yellow',p=0),
						'',
						# _.pr(xx, c='green',p=0),
						_.pr('Copy an encrypted string to the clipboard', c='yellow',p=0),
						_.hp('\tp aes -password MySecret -de -clip'),
						_.pr('Then paste the decrypted string where needed', c='yellow',p=0),
						# _.pr(xx, c='green',p=0),
						'',
						_.hp('p aes -password MySecret -en -bin ZippedFolder.zip -save ZippedFolder.zip.aes'),
						_.hp('p aes -password MySecret -de -bin ZippedFolder.zip.aes -save ZippedFolder.zip'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	# _.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

import urllib.parse


import os

import hashlib

def md5(input_string: str) -> str:
	return hashlib.md5(input_string.encode('utf-8')).hexdigest()




def secure_delete(file_path):
	try:
		# Get the size of the file
		file_size = os.path.getsize(file_path)

		# Open the file in write-binary mode and overwrite with zeros
		with open(file_path, 'wb') as f:
			f.write(b'\x00' * file_size)
		
		# Delete the file
		os.remove(file_path)
		_.pr(f"File {file_path} securely deleted.",c='green')
	except FileNotFoundError:
		_.pr(f"File {file_path} not found.",c='red')
	except Exception as e:
		_.pr(f"An error occurred: {e}",c='red')




def action():
	if _.switches.isActive('SecureDeleteFile'):
		if not len(_.switches.values('SecureDeleteFile')):
			_.e('Error: No file specified')
		file = _.switches.value('SecureDeleteFile')
		if os.path.isdir(file):
			_.e('Only files can be securely deleted','You specified a folder')
		if not os.path.isfile(file):
			_.e('Error: File not found')
		_.pr('Overwriting and deleting:',file,c='yellow')
		secure_delete(file)
		return
	


	if _.switches.isActive('BinaryFile'):
		if not _.switches.isActive('Save'): _.e('Error: -bin requires -save')
		import base64


	shouldPrint = False
	if _.switches.isActive('Password'):
		password = _.switches.value('Password')
	elif 'aes' in _v.fig:
		password = _v.fig['aes']
	else:
		shouldPrint = True
		import random
		random_number = random.randint(10000000, 99999999)
		password = str(random_number)


	if _.switches.isActive('PasswordMD5'):
		password = md5(password)
	
	if shouldPrint:
		print('Password:',password)

	aes=_.aesEverywhere(password)
	
	if _.switches.isActive('Encrypt'):
		if _.switches.isActive('Clipboard'):
			_paste = _.regImp( __.appReg, '-paste' )
			text = _paste.imp.paste()
		elif _.switches.isActive('BinaryFile'):
			with open(_.switches.value('BinaryFile'), 'rb') as binary_file: text = binary_file.read()
			text = base64.b64encode(text).decode('utf-8')
		elif _.switches.isActive('Files'):
			text = _.getText( _.switches.value('Files'), raw=True )
		elif len(_.switches.value('Encrypt')):
			text = ' '.join( _.switches.values('Encrypt') )
		elif len(_.isData(r=0)):
			text = ' '.join( _.isData(r=0) )
		else:
			_.e('No text to encrypt')


		if _.switches.isActive('BinaryFile'):
			en = aes.bEn(text)
			with open( ' '.join(_.switches.values('Save')).strip() , 'wb') as binary_file: binary_file.write(en)
			_.pr('Saved:', ' '.join(_.switches.values('Save')) )
			return
		en = aes.en(text)

		if _.switches.isActive('Clipboard'):
			_copy = _.regImp( __.appReg, '-copy' )
			_copy.imp.copy( en )
		elif _.switches.isActive('Save'):
			_.saveText( en, ' '.join(_.switches.values('Save')).strip() )
			_.pr('Saved:', ' '.join(_.switches.values('Save')) )
		else:
			_.pr(en)

	elif _.switches.isActive('Decrypt'):
		if _.switches.isActive('Clipboard'):
			_paste = _.regImp( __.appReg, '-paste' )
			text = _paste.imp.paste()
		elif _.switches.isActive('Files'):
			text = _.getText( _.switches.value('Files'), raw=True )
		elif _.switches.isActive('BinaryFile'):
			with open(_.switches.value('BinaryFile'), 'rb') as binary_file: text = binary_file.read()
		elif len(_.switches.value('Decrypt')):
			text = ' '.join( _.switches.values('Decrypt') )
		elif len(_.isData(r=0)):
			text = ' '.join( _.isData(r=0) )
		else:
			_.e('No text to decrypt')


		if _.switches.isActive('BinaryFile'):
			de = aes.bDe(text)
			de = base64.b64decode(de)
			with open( ' '.join(_.switches.values('Save')) , 'wb') as binary_file: binary_file.write(de)
			_.pr('Saved:', ' '.join(_.switches.values('Save')) )
			return
		
		de = aes.de(text)

		if _.switches.isActive('Clipboard'):
			_copy = _.regImp( __.appReg, '-copy' )
			_copy.imp.copy( de )
		elif _.switches.isActive('Save'):
			_.saveText( de, ' '.join(_.switches.values('Save')).strip() )
			_.pr('Saved:', ' '.join(_.switches.values('Save')) )
		else:
			_.pr(de)
	else:
		_.help(1)



	
	# en = aes.en('Apples and Bananas')
	# de = aes.de(en)
	# _.pr('py en:',en)
	# _.pr('py de:',de)
	# de2 = _.URL(f'https://sds.sh/aes/?en={urllib.parse.quote(en)}&password={urllib.parse.quote(password)}')
	# _.pr('url de:',de2)
	# en2 = _.URL(f'https://sds.sh/aes/?text={urllib.parse.quote("This is a test")}&password={urllib.parse.quote(password)}')
	# _.pr('url en:',en2)
	# de3 = aes.de(en2)
	# _.pr('py de:',de3)
	# load(); global c3po;

	#n)--> iterate
	# for subject in _.isData(r=0): _.pr(subject)
	# for subject in _.myData(): _.pr(subject)
	

# def load():
# 	global c3po
# 	c3po = _.getTable( 'table' )
# 	#n)--> print table
# 	_.pt(c3po)


##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################
########################################################################################
# import requests # pip install requests
########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action(); _.isExit(__file__);