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
import platform
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
	_.switches.register('Count', '-c,-count,--c')
	_.switches.register('Path', '-p,-path,-folder')
	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Binary', '-bin')
	_.switches.register('Size', '-size',' g 10mb, L 2kb ')
	_.switches.register('Extensions', '-ext', 'image, video, audio, document')
	_.switches.register('Totals', '-total,-totals')
	_.switches.register('FolderRefine', '-fr')
	_.switches.register('Ago', '-ago', '1m')
	_.switches.register('MaxDepth', '-depth', '3')

_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'fix_dates_from_file_meta_db.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'fix create and modified dates',
	'categories': [
						'tool',
						'date',
						'change date',
						'change epoch',
						'created date',
						'modified date',
						'birth date',
						'birth',
						'created',
						'modified',
						'date created',
						'date modified',
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
						'p fix_dates_from_file_meta_db',
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

import hashlib
import sqlite3
import subprocess
import _rightThumb._dir as _dir
from pathlib import Path



####*************************************************************************



def isText(file):
	return _mime.isText(file)

def whatIsIt(file):
	if isText(file):
		result = 'Text'
	else:
		result = 'Binary'
	return result

def getFolder(folder):
	global i
	global iS
	global baseDepth
	if _.switches.isActive('MaxDepth'):
		if len(_.switches.value('MaxDepth')):
			maxDepth = int(_.switches.values('MaxDepth')[0])
		else:
			maxDepth = 4
		if len( folder.split(_v.slash) ) - baseDepth >= maxDepth:
			if len(_.switches.values('MaxDepth')) > 1 and 'p' in _.switches.values('MaxDepth')[1]:
				_.pr( folder )

			return None
	try:
		dirList = os.listdir(folder)
		takeAction = True
	except Exception as e:
		takeAction = False
	if takeAction:
		if os.path.isdir(folder):
			dirList = os.listdir(folder)
		for item in dirList:
			path = folder + _v.slash + item
			path = path.replace(_v.slash+_v.slash,_v.slash)
			if os.path.isfile(path):
				i = i + 1

				if _.showLine(path):
					shouldPrint = False

					if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
						# _.pr(0,whatIsIt(path),path)
						# _.pr(path)
						shouldPrint = True
					else:
						if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
							# _.pr(1,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True
						if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
							# _.pr(2,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True
						if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
							# _.pr(3,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True
						if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
							# _.pr(4,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True

					pass

					pass


					if _.switches.isActive('Ago'):
						# sys.exit()
						record = _dir.fileInfo( path )
						# _.pr( _.switches.values('Ago'), record['date_modified_raw'], record['date_created_raw'],  )
						# if os.path.isfile(path):
						shouldPrint = False
						run = 'default'
						if len( _.switches.values('Ago') ) > 1:
							if 'a' in _.switches.values('Ago')[1]:
								run = 'a'
							elif 'md' in _.switches.values('Ago')[1]:
								run = 'md'
							elif 'cd' in _.switches.values('Ago')[1]:
								run = 'cd'
							elif 'resent' in _.switches.values('Ago')[1]:
								run = 'resent'

						# _.pr(  len( _.switches.values('Ago') )  )
						# _.pr(  ( _.switches.values('Ago') )  )
						# sys.exit()
						# accessed_raw


						if run == 'default':
							# _.pr(record['date_modified_raw'])
							# _.pr(_.switches.values('Ago'))
							if record['date_modified_raw'] > _.switches.values('Ago')[0] or record['date_created_raw'] > _.switches.values('Ago')[0]:
								shouldPrint = True
						elif run == 'resent':
							if record['date_modified_raw'] > _.switches.values('Ago')[0] or record['date_created_raw'] > _.switches.values('Ago')[0] or record['accessed_raw'] > _.switches.values('Ago')[0]:
								shouldPrint = True
						elif run == 'a':
							if record['accessed_raw'] > _.switches.values('Ago')[0]:
								# _.pr( _.friendlyDate(_.switches.values('Ago')[0]), _.switches.values('Ago')[0], record['accessed_raw'], _.friendlyDate(record['accessed_raw']) )
								shouldPrint = True
						elif run == 'cd':
							# _.pr( 'HERE A' )
							if record['date_created_raw'] > _.switches.values('Ago')[0]:
								# _.pr( 'HERE B' )
								shouldPrint = True
						elif run == 'md':
							if record['date_modified_raw'] > _.switches.values('Ago')[0]:
								shouldPrint = True

					pass

					pass
					if shouldPrint:
						if _.switches.isActive('Size'):
							shouldPrint = False
							shouldPrint_2 = False
							stat = os.stat(path)
							size = stat.st_size
							if 'l' in _.switches.values('Size')[0]:
								if size < _.switches.values('Size')[1]:
									shouldPrint_2 = True
							if 'g' in _.switches.values('Size')[0]:
								if size > _.switches.values('Size')[1]:
									shouldPrint_2 = True

							if shouldPrint_2:
								shouldPrint = False

								if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
									
									shouldPrint = True
								else:
									if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
										shouldPrint = True
									if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
										shouldPrint = True
									if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
										shouldPrint = True
									if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
										shouldPrint = True



							if shouldPrint:
								shouldPrint = False
								
								if _.switches.isActive('Count'):
									# _.pr( _.colorThis( path, 'cyan', p=0 ) )
									process(path)
								else:
									iS+=1

									formatedSize = formatSize( size )
									formatedSize = _.fields.value( 'files', 'name', formatedSize )
									result = ''
									fs = formatedSize.split(' ')
									result += _.colorThis( fs[0], 'Color.purple', p=0 )
									result += ' '
									result += _.colorThis( fs[1], 'Color.darkcyan', p=0 )
									fs.reverse()
									fs.pop()
									fs.pop()
									fs.reverse()
									result += ' '.join(fs)
									result += '\t'
									result += _.colorThis( path, 'cyan', p=0 )

									# _.pr( result )
									process(path)
								
								# _.pr( formatedSize, '\t', path )


					if shouldPrint :

						global extensionList
						if len( extensionList ):
							if '.' in path:
								pathy = path.lower().split('.')
								pathy_test = pathy.pop()
								if not '.'+pathy_test in extensionList:
									shouldPrint = False



					if shouldPrint:
						iS+=1
						if not _.switches.isActive('Totals'):
							if not _.switches.isActive('Plus'):
								# _.colorThis( path, 'cyan' )
								process(path)
							else:
								_.pr( _.colorPlus( path, 'cyan' ) )

			# if os.path.isdir(path) and _.showLine(path):
			if os.path.isdir(path):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):
					shouldRun = True
					if _.switches.isActive('FolderRefine'):
						if not _.showLine(newFolder):
							shouldRun = False
					if shouldRun:
						try:
							getFolder(newFolder)
						except Exception as e:
							pass
				else:
					_.pr('error')

def extensionsDatabank():
	global extensionList
	_db = _.regImp( __.appReg, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )
	_db.switch( 'Plus', _.switches.values('Extensions') )
	extensionList = _db.do( 'action' )
	for i,x in enumerate(extensionList):
		extensionList[i] = x.lower()
	# _.pr( extensionList )


def action():

	global conn
	global c
	db = 'D:\\tech\\hosts\\MSI\\indexes\\D_Drive.db'
	conn = sqlite3.connect(db)
	c = conn.cursor()

	# process( _.switches.values('Input')[0] )

	if _.switches.isActive('Extensions'):
		extensionsDatabank()


	_.fields.register( 'files', 'name', '1000.43 KB' )
	global i
	global iS
	# load()
	if _.switches.isActive('Path') == False:
		folder = os.getcwd()
	else:
		folder = _.switches.value('Path')
	global baseDepth
	baseDepth = len( folder.split(_v.slash) )
	getFolder(folder)
	"""
	if _.switches.isActive('Extensions'):
		folderProfileAttribute( folder=folder, info={
														'recursive': True,
														'count': iS,
														'files': i ,
														'diff': _.pDiff( iS, i, use='less' ) ,
		} )
	"""
	if not iS == i:
		_.folderProfileAttribute( folder=folder, info = {
														'app': 'files',
														'recursive': True,
														'factors': {
																		'Text': _.switches.isActive('Text'),
																		'Binary': _.switches.isActive('Binary'),
																		'Extensions': _.switches.isActive('Extensions'),
																		'Type': _.switches.values('Extensions'),

																		'PlusOr': _.switches.isActive('PlusOr'),
																		'PlusClose': _.switches.isActive('PlusClose'),
																		'Plus': _.switches.isActive('Plus'),
																		'Minus': _.switches.isActive('Minus'),
																		
																		'PlusVals': _.switches.values('Plus'),
																		'MinusVals': _.switches.values('Minus'),
														},
														'percentage': _.pDiff( iS, i, use='less' ),
														'count': iS,
														'files': i,

		} )

	if _.switches.isActive('Count') == False:
		if not i == iS:
		# if _.switches.isActive('Size'):
			_.colorThis( [  '\n', _.addComma(iS), 'of', _.addComma(i), '\n'  ], 'yellow' )
		else:
			_.colorThis( [  '\n{}\n'.format( _.addComma(i) )  ], 'yellow' )
		# _.pr('\n{}\n'.format(i))

extensionList = []

i = 0
iS = 0
baseDepth = 0

if _.switches.isActive('Ago'):
	import _rightThumb._dir as _dir



####*************************************************************************



def modify_timestamp( stamp ):
	d = _.friendlyDate(stamp).replace('-','/')
	parts = d.split(' ')
	day = parts[0]
	tip = parts[1].split(':')
	
	if int(tip[0]) > 12:
		tip[0] = int(tip[0]) - 12
		ap = 'PM'
	else:
		ap = 'AM'
	if not len(tip)> 2:
		f = day + ' ' + str(tip[0])+':'+str(tip[1])+ ' '+ ap
	else:
		f = day + ' ' + str(tip[0])+':'+str(tip[1])+':'+str(tip[2])+ ' '+ ap
	return f



def changeC( path, stamp ):
	# name = Path(path).name
	# parts = path.split(_v.slash)
	# parts.reverse()
	# parts.pop(0)
	# parts.reverse()
	# fld = _v.slash.join(parts)
	# os.chdir(fld)
	# _.pr(path)
	try:

		if _.isWin:
			p = subprocess.Popen(['powershell.exe', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stamp)+'")'], stdout=sys.stdout)
		else:
			if os.path.isfile('/snap/bin/pwsh'):
				p = subprocess.Popen(['/snap/bin/pwsh', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stamp)+'")'], stdout=sys.stdout)
			elif os.path.isfile('/usr/bin/pwsh'):
				p = subprocess.Popen(['/usr/bin/pwsh', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stamp)+'")'], stdout=sys.stdout)
			elif os.path.isfile('/opt/pwsh'):
				p = subprocess.Popen(['/opt/pwsh', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stamp)+'")'], stdout=sys.stdout)
	except Exception as e:
		_.colorThis( path, 'red' )
		time.sleep(1)
		pass
		# raise e
	# time.sleep(.02)
def changeM( path, stamp ):
	# _.pr(path)
	os.utime(path,(stamp, stamp))

def process( path ):
	global threshhold
	global c
	global conn
	global index
	path = os.path.realpath(path)
	info = _dir.info(path)
	f = info['folder'].lower()
	if not info['folder'].lower() in index:
		index[info['folder'].lower()] = {}
		sql = ' SELECT path, date_created_raw, date_modified_raw FROM files WHERE `folder` = "'+info['folder']+'" COLLATE NOCASE'
		# sql = ' SELECT * FROM files'
		# sql = 'SHOW TABLES;'
		c.execute(sql)
		records = c.fetchall()
		for record in records:
			index[f][ record[0].lower() ] = {
				'ce': record[1],
				'me': record[2]
			}


	p = path.lower() 
	if p in index[f]:
		_.pr(path)
		changeM( path, index[f][p]['me'] )
		# changeC( path, index[f][p]['ce'] )
		# if info['ce'] > index[f][p]['ce']:
			# if ( info['ce'] - index[f][p]['ce'] ) > 123521:
			#     changeC( path, index[f][p]['ce'] )
			# elif ( index[f][p]['ce'] -info['ce'] ) > 123521:
			#     changeC( path, index[f][p]['ce'] )

		# if len( records ):
		#     ce = records[0][0]
		#     me = records[0][1]

		#     if info['me'] < threshhold:
		#         _.pr( ce, me )
		#         _.pr( _.friendlyDate(ce), _.friendlyDate(me) )



		# for record in records:
		#     _.pr(record)



# def action():
#     global conn
#     global c
#     db = 'D:\\tech\\hosts\\MSI\\indexes\\D_Drive.db'
#     conn = sqlite3.connect(db)
#     c = conn.cursor()

#     process( _.switches.values('Input')[0] )


threshhold = _.autoDate('2020-11-30 07:51:21')
index = {}


c = None
conn = None
########################################################################################
if __name__ == '__main__':
	action()