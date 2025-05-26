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
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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
# import _rightThumb._encryptString as _blowfish
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Count', '-c,-count,--c')
	_.switches.register('Path', '-p,-path,-folder')
	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Binary', '-bin')
	_.switches.register('Size', '-size',' g 10mb, L 2kb ')
	_.switches.register('ViewLog', '-log')
	



_.appInfo[focus()] = {
	'file': 'files.py',
	'description': 'Lists files',
	'categories': [
						'dir',
						'recursive',
						'files',
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
						'p files --c ',
						'p files -text ',
						'',
						'p files -size g 2mb',
						'p files -size L 2mb',
						'p files -size g 2mb --c -folder D:\\techApps\\Python\\Python36-32'+_v.slash,
						'',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
	],
	'aliases': [
					# 'this',
					# 'app',
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



def formatSize(size):
	result = ''
	if size == None:
		result = ''
	elif size < 1024:
		result = str(size) + ' B'
	elif size > 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str(num) + ' KB'
	elif size > 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str(num) + ' MB'
	elif size > 1073741824 and size < 1099511627776    :
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	# if size < 1:
	#     result = ''
	return result

def unFormatSize(size):
	hasNumber = False
	for x in size:
		if x in '0123456789':
			hasNumber = True
	if not hasNumber:
		return size.lower()
	if ',' in size:
		return size

	size = str(size)
	size = size.upper()
	factor = ''

	if 'TB' in size:
		factor = 1099511627776    
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024
	else:
		factor = 1
	size = size.replace('T','')
	size = size.replace('B','')
	size = size.replace('M','')
	size = size.replace('K','')
	size = size.replace('G','')
	size = int(float(size))
	result = round(size * factor,0)
	return result




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

	_.switches.trigger( 'Size' , unFormatSize )
	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
########################################################################################
# START



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

				if _.showLine(path):
					shouldPrint = False

					if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
						i = i + 1
						# _.pr(0,whatIsIt(path),path)
						# _.pr(path)
						shouldPrint = True
					else:
						if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
							i = i + 1
							# _.pr(1,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True
						if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
							i = i + 1
							# _.pr(2,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True
						if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
							i = i + 1
							# _.pr(3,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True
						if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
							i = i + 1
							# _.pr(4,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True



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
								i = i + 1
								shouldPrint = True
							else:
								if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
									i = i + 1
									shouldPrint = True
								if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
									i = i + 1
									shouldPrint = True
								if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
									i = i + 1
									shouldPrint = True
								if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
									i = i + 1
									shouldPrint = True







							if shouldPrint:
								shouldPrint = False
								iS+=1
								if _.switches.isActive('Count'):
									_.pr( _.colorThis( path, 'cyan', p=0 ) )
								else:

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

									_.pr( result )
								
								# _.pr( formatedSize, '\t', path )





					if shouldPrint:
						_dir.fileInfo(path)
						# if not _.switches.isActive('Plus'):
						#     _.colorThis( path, 'cyan' )
						# else:
						#     _.pr( _.colorPlus( path, 'cyan' ) )

			if os.path.isdir(path):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):
					try:
						getFolder(newFolder)
					except Exception as e:
						pass
				else:
					_.pr('error')








def action():
	if not _.switches.isActive('ViewLog'):
		_.fields.register( 'files', 'name', '1000.43 KB' )
		global i
		global iS
		# load()
		if _.switches.isActive('Path') == False:
			folder = os.getcwd()
		else:
			folder = _.switches.value('Path')
		
		getFolder(folder)
		if _.switches.isActive('Count') == False:
			if _.switches.isActive('Size'):
				_.colorThis( [  '\n', iS, 'of', i, '\n'  ], 'yellow' )
			else:
				_.colorThis( [  '\n{}\n'.format(i)  ], 'yellow' )
			# _.pr('\n{}\n'.format(i))
		_.saveTable( _dir.timeAudit, '_dir.timeAudit.json' )
		_.pr( 'Time Logged for', i, 'files' )
	else:
		log = _.getTable( '_dir.timeAudit.json' )
		audit = {}
		theStart = log[0][0]['epoch']
		for rec in log[0]:
			audit[rec['label']] = 0

		for aLog in log:
			since = aLog[0]['epoch']
			for i, thisLog in enumerate(aLog):
				if i:
					audit[thisLog['label']] += thisLog['epoch'] - since
					since = thisLog['epoch']
		_.printVar( audit )
		_.pr()
		_.pr()
		_.pr( 'Total:', since-theStart, 'seconds for', len(log), 'files' )
		

i = 0
iS = 0
# def load():
#     global data
#     data = _.getTable( 'table.json' )
# data = []


import _rightThumb._dir as _dir
_dir.timeAuditCollect = True
# _dir.timeAudit = _.getTable( '_dir.timeAudit.json' )

# Total: 52.27503776550293 seconds for 1792 files
# Total: 0.7076563835144043 seconds for 1792 files
########################################################################################
if __name__ == '__main__':
	action()






