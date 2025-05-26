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
import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword('string')

import _rightThumb._dir as _dir

_fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
##################################################
import datetime
##################################################

def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Password', '-password','123')
	_.switches.register('NamePassword', '-pn,-np')
	_.switches.register('NameDate', '-nd')
	_.switches.register('UnZip', '-u,-unzip')
	_.switches.register('UnZipNoFolder', '-nf')
	



_.appInfo[focus()] = {
	'file': '7z.py',
	'description': '7zip basics made simple',
	'categories': [
						'compression',
						'encryption',
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

_.appInfo[focus()]['examples'].append('p 7z -f file')
_.appInfo[focus()]['examples'].append('p 7z -f file -nd')
_.appInfo[focus()]['examples'].append('p 7z -f file -p 777 ')
_.appInfo[focus()]['examples'].append('p 7z -f file -p 777 -pn ')
_.appInfo[focus()]['examples'].append('p 7z -f file -p 777 -pn 7x3')
_.appInfo[focus()]['examples'].append('p 7z -f file -p 777 -pn -nd')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p 7z -f file.7z -u')
_.appInfo[focus()]['examples'].append('p 7z -f file.7z -u -nf')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p 7z -nd -pn -p -f file')
_.appInfo[focus()]['examples'].append('')


# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



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

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = True

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
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
# START


def getExtension(string):

	ext0 = string.split('.')
	extId = len(ext0) - 1
	if extId > 0:
		ext = ext0[extId]
	else:
		ext = ''
	return ext
def removeExtension(string):
	if not '.' in string:
		return string
	ext = getExtension(string)
	sl = len(string)
	el = len(ext)
	dl = (sl - el) - 1
	file = ''
	for i,n in enumerate(string):
		if i < dl:
			file += n

	return file
def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y.%m.%d')
	theDate = str(theDate)
	return theDate
def qt(string):
	# _.pr( string )
	# pause=input('pause')
	# sys.exit()
	return '"' + str(string) + '"'
def we(string):
	if not string.endswith('.7z'):
		return string + '.7z'
	else:
		return string

def action():
	# _.pr( 'HERE' )
	if _.switches.isActive('Input'):
		# _.pr( 'HERE' )
		if os.path.isfile( _.switches.value('Input') ):
			fileInfo = _dir.fileInfo( _.switches.value('Input') )
			# _.pr( fileInfo['folder'] )
			# sys.exit()
			os.chdir( fileInfo['folder'] )
		if os.path.isdir( _.switches.value('Input') ):
			folder = _.switches.value('Input')
			# fileInfo = _dir.fileInfo( folder )
			# _.pr( os.walk(fileInfo['folder']) )
			# os.listdir(folder)
			modTime = _.resolveEpochTest(max(os.path.getmtime(root) for root,_,_ in os.walk(folder)))
			for row in os.listdir(folder):
				info = _dir.fileInfo( folder + _v.slash + row )
				break
			fileInfo = {}
			fList = info['folder'].split(_v.slash)
			fList.reverse()
			fileInfo['name'] = fList[0]
			fList.pop(0)
			fList.reverse()
			fileInfo['folder'] = _v.slash.join( fList )
			fileInfo['date_modified'] = modTime
			fileInfo['ext'] = ''
			# _.pr( modTime )
			# sys.exit()


	defaultPassword = _blowfish.genPassword()
	if _.switches.isActive('Password'):
		if not len( _.switches.value('Password') ):
			# _.pr( 'HERE' )
			_.switches.fieldSet( 'Password', 'value', defaultPassword )

	
	
	pass
	# if _.switches.isActive('Input'):
	#     _.setPipeData( _.getText( _.switches.value('Input') ), focus() )
	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#     pass
	# _.pr( _.d2json(_.appData) )


# def action():

	if '_pw(' in _.switches.value('Input'):
		_.switches.fieldSet('UnZip','active',True)
		_.switches.fieldSet('Password','active',False)
		_.switches.fieldSet('NameDate','active',False)
		_.switches.fieldSet('NamePassword','active',False)
		if not _.switches.isActive( 'UnZipNoFolder' ):
			_.switches.fieldSet('UnZipNoFolder','active',True)
			_.switches.fieldSet('UnZipNoFolder','value','auto')

		# if _.switches.value('Input').endswith('.7z'):



	# _.switches.register('Input', '-i,-f,-file','file.txt')
	# _.switches.register('Password', '-p','123')
	# _.switches.register('NamePassword', '-pn,-np')
	# _.switches.register('NameDate', '-nd')
	# _.switches.register('UnZip', '-u,-unzip')
	# _.switches.register('UnZipNoFolder', '-nf')



	if _.switches.isActive('UnZipNoFolder'):
		_.switches.fieldSet('UnZip','active',True)
	if not _.switches.isActive('UnZip') and _.switches.isActive('Input'):
		file = _.switches.value('Input')
		if os.path.isfile(file):

			baseName = removeExtension(fileInfo['name'])
		elif os.path.isdir(file):
			baseName = file
		else:
			_.pr('No File')
			sys.exit()
		
		z7 = _v.app7z()
		password = _.switches.value('Password')
		pwLabel = ''
		if _.switches.isActive('Password') and _.switches.isActive('NamePassword') and len(password) > 0:
			if password == defaultPassword:
				displayPassword = 'AUTO'
			else:
				displayPassword = password
			pwLabel = '_pw(' + displayPassword + ')'

		if _.switches.isActive('NameDate'):
			nameFinal = nameDate( file, removeExtension( fileInfo['name'] ), pwLabel, fileInfo )
			do = z7 + ' a ' + qt( fileInfo['folder'] + _v.slash +  we(nameFinal) ) + ' ' + qt(file)
			
		else:
			do = z7 + ' a ' + qt( fileInfo['folder'] + _v.slash +  we(baseName + pwLabel) ) + ' ' + qt(file)

		if _.switches.isActive('Password'):
			do = do + ' -p"' + password + '"'
		# _.pr()
		# _.pr('do:')
		# _.pr('\t',do)
		# _.pr()
		# _.pr()
		# pause=input('pause')
		os.system('"' + do + '"')

	if _.switches.isActive('UnZip') and _.switches.isActive('Input') and os.path.isfile(_.switches.value('Input')):

		file = _.switches.value('Input')
		baseName = removeExtension( fileInfo['name'] )
		z7 = _v.app7z()
		# _.pr('test')
		if _.switches.isActive('Password'):
			pw = _.switches.value('Password')
			do = z7 + ' e ' + qt(file) + ' -p"' + pw + '" -oc:' +    baseName
		else:
			if '_pw' in baseName:
				pwx = baseName.split('_pw(')
				pw = pwx[1][:-1]
				baseName = pwx[0]
				if pw == 'AUTO':
					pw = defaultPassword
				do = z7 + ' e ' + qt(file) + ' -p"' + pw + '" -oc:' +   baseName
			else:
				do = z7 + ' e ' + qt(file) + ' -oc:' +    baseName
				# do = z7 + ' e ' + qt(file) + ' ' + qt(baseName)
		
		if _.switches.isActive('UnZipNoFolder'):
			preSplitDo = do
			do = do.split('-oc')[0]
			pre_do = do.replace( ' e ', ' l ' )
			pre_do += ' > ' + _v.myTemp + _v.slash+'_7z_temp.txt'
			os.system('"' + pre_do + '"')
			fileContent = _.getText( _v.myTemp + _v.slash+'_7z_temp.txt', raw=True, clean=True )
			iheader = 99999
			for i,row in enumerate(fileContent.split('\n')):
				if 'Date' in row:
					if 'Time' in row:
						if 'Attr' in row:
							if 'Size' in row:
								if 'Compressed' in row:
									if 'Name' in row:
										iheader = i
										header = row
										# _.pr( header )
				# _.pr( row )
				# _.pr( row )

				if i >= (iheader + 2) :
					if '----------------------' in row:
						break

					theFile = getFileFromRows( header, row )
					_.pr( theFile )
					
					if _v.slash in theFile and  _.switches.value('UnZipNoFolder') == 'auto' :
						do = preSplitDo
					else:
						if _v.slash in theFile:
							fSplit = theFile.split(_v.slash)
							fSplit.reverse()
							theFile = fSplit[0]
						try:
							if os.path.isfile(theFile):
								os.rename( theFile, nameDate( theFile, theFile, '', fileInfo, addZip=True ) )
						except Exception as e:
							_.pr( e )
					
			# sys.exit()
			# _.pr( '|'+theFile+'|' )
			# sys.exit()
				# shouldRename = True
				# _.pr( nameDate( theFile, theFile, '' ) )
				# sys.exit()


		# _.pr()
		# _.pr('do:')
		# _.pr('\t',do)
		# _.pr()
		# _.pr()
		# pause=input('pause')
		os.system('"' + do + '"')


def getFileFromRows( header, row ):
	pre = header.split( 'Name' )[0]
	result = ''
	for i,char in enumerate(row):
		if i >= len( pre ):
			result += char
	return result

def nameDate( file, baseName, pwLabel, fileInfo, addZip=False ):
	if _v.slash in file:
		fSplit = file.split(_v.slash)
		fSplit.reverse()
		file = fSplit[0]
	modifiedRaw = os.path.getmtime(file)
	modified = formatDate(modifiedRaw)
	if addZip:
		oldBaseName = baseName
		dotSplit = baseName.split( '.' )
		dotSplit.reverse()
		noExt = baseName[:-(len(dotSplit[0])+1)]
		ext = dotSplit[0]
		baseName = noExt + '(7z).' + ext
		return _fileNameDate.imp.newName( baseName, fileInfo )


	return _fileNameDate.imp.newName( we( baseName + pwLabel ), fileInfo )
	baseNewName = modified + '-' + baseName + pwLabel
	# _.pr(we(baseNewName))
	if not os.path.isfile(we(baseNewName)):
		nameFinal = baseNewName
	else:
		for x in range(1,100000000):
			nw = modified + '-' + str(x) + '-' + baseName + pwLabel
			if not os.path.isfile(we(nw)):
				nameFinal = nw
				break
	return nameFinal


# ToDo: add value to UnZipNoFolder if set auto for if _v.slash in theFile:


########################################################################################
if __name__ == '__main__':
	action()







