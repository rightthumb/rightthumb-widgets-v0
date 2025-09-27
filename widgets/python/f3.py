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

# import os
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
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
##################################################
import glob
import os.path
from os.path import join, getsize, isfile, isdir, splitext
##################################################

def appSwitches():
	# _.switches.register('Input', '-i,-f,-file','file.txt')

	# _.switches.register('_Raw', '')
	_.switches.register('Dad', '-d,-dad')
	_.switches.register('Papa', '-papa')
	_.switches.register('Priority', '-p,-pri,-priority')
	_.switches.register('Public', '-pub,-publiccloud')
	_.switches.register('IndexFile', '-if,-indexfile')
	_.switches.register('SearchIn', '-f,-s,-i,-in,-search,-searchin','*.txt')
	_.switches.register('FileName', '-n,-name')
	_.switches.register('JustName', '-jn,-justname')
	_.switches.register('Replace', '-r,-replace','C: G:')
	_.switches.register('One', '-1')
	_.switches.register('Two', '-2')
	_.switches.register('Eight', '-8')
	_.switches.register('Bookmarks', '-bm,-bookmarks')
	_.switches.register('Tickets', '-tick,-tickets,-history,-h')
	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Force', '-force')



_.appInfo[focus()] = {
	'file': 'f3.py',
	'description': 'Search in indexes or files, multi-threaded',
	'categories': [
						'tool',
						'research',
						'file',
						'contents',
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

_.appInfo[focus()]['examples'].append('p f -i *.py + name -jn')
_.appInfo[focus()]['examples'].append('p f -papa + \\GLENNALLEN\\ \\AppData\\ - \\Local\\ . | p line --c -p \\ 5 -u')
_.appInfo[focus()]['examples'].append('p f -bm + tmp -n | p dir -b')
_.appInfo[focus()]['examples'].append('p file + bm- | p f + { -jn | p line --c -make "xcopy /d/y {} Default(bookmarks)\\" | p execute')
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

	# _.switches.trigger('Plus', _.ci)
	# _.switches.trigger('Minus', _.ci)
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


def replaceDo(line):
	global replaceWith
	if _.switches.isActive('Replace') == True:
		line2 = line
		line = line.replace(replaceWith[0],replaceWith[1])
		if line2 == line:
			line = line.replace(upper(replaceWith[0]),upper(replaceWith[1]))
		if line2 == line:
			line = line.replace(lower(replaceWith[0]),lower(replaceWith[1]))
	return line

def searchName(files,line):
	if _.switches.isActive('Bookmarks') == True:
		clean = _v.bookmarkFormat.replace( 'ALIASHERE.txt', '' )
		name = files.replace(clean,'').replace('.txt','')
		nameTest = _.showLine(name)
		lineTest = _.showLine(line)
		if nameTest == True or lineTest == True:
			result = True
		else:
			result = False
	else:
		result = _.showLine(line)
		# _.pr(result)
	return result

def executeSearch(filename,files,search):

	global theList
	i = 0
	for line in search:
		i += 1
		line = line.replace('\n','')
		line = line.replace('\r','')
		if searchName(files,line) == True:
			if _.switches.isActive('Replace') == True:
				line = replaceDo(line)
			if _.switches.isActive('Bookmarks') == True:
				if _.switches.isActive('FileName') == True:
					_.pr(filename)
				else:
					clean = _v.myBookmarks + _v.slash+'BM-'
					if os.path.isdir(line) == True:
						found = 'Good'
					else:
						found = 'Bad'
					_.pr(found + '\t ' + filename.replace(clean,'').replace('.txt','') + ' = ' + line)
			elif _.switches.isActive('FileName') == True:
				# _.pr(filename + ':' + line)
				newLine = line
				newLine = _str.removeAll(newLine,'\t')
				newLine = newLine.replace('\n','')
				newLine = newLine.replace('\r','')
				newLine = _str.replaceDuplicate(newLine,' ')
				newLine = _str.cleanFirst(newLine,' ')
				theList.append({'filename': filename,'string': newLine,'line': i})
			elif _.switches.isActive('JustName') == True:
				_.pr(filename)
				break
			else:
				row=line
				if _.switches.isActive('Plus'):
					for plusSearchX in _.switches.values('Plus'):
						plusSearchX = _.ci( plusSearchX )
						for subject in _.caseUnspecific( row, plusSearchX ):
							row = row.replace( subject, _.colorThis( subject, 'green', p=0 ) )
					_.pr(row)
				else:
					_.pr(line)
def takeAction():
	global indexFiles
	global theList
	search = []
	filename = ''
	# _.pr(indexFiles)
	# _.pr(_.switches.value('_Raw'))
	# _.pr(_.switches.value('Plus'))
	# _.pr(_.switches.value('Minus'))
	# _.pr(indexFiles)
	# os._exit(0)
	# _.pr( indexFiles )
	if type(_.appData[__.appReg]['pipe']) == list:
		lookIn = indexFiles
	else:
		lookIn = glob.glob( indexFiles )
	for files in lookIn:
		# _.pr( files )
		if _.switches.isActive('Force'):
			mimeTest = True
		else:
			mimeTest = _mime.isText(files)
		if os.path.isfile(files) and mimeTest:
			try:
				with open(files, 'r') as ins:
					filename = ins.name
					search = []
					for line in ins:
						search.append(line)
				ins.close()
				executeSearch(filename,files,search)
			except Exception as e:
				try:
					with open(files, 'r', encoding='UTF-8') as ins:
						filename = ins.name
						search = []
						for line in ins:
							search.append(line)
					ins.close()
					executeSearch(filename,files,search)
				except Exception as e:
					try:
						with open(files, 'r', encoding='latin-1') as ins:
							filename = ins.name
							search = []
							for line in ins:
								search.append(line)
						ins.close()
						executeSearch(filename,files,search)
					except Exception as e:
						pass
						_.pr('Error: ' + str(filename))
			# HERE
	if _.switches.isActive('FileName') == True:
		_.pr()
		_.switches.fieldSet('Long','active',True)
		_.switches.fieldSet('GroupBy','active',True)
		_.switches.fieldSet('GroupBy','value','filename')
		_.tables.register('Auto',theList)
		_.tables.print('Auto','filename,line,string')

def action():
	global indexFiles
	
	pass
	# if _.switches.isActive('Input'):
	#   _.setPipeData( _.getText( _.switches.value('Input') ), focus() )
	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#   pass
	# _.pr( _.d2json(_.appData) )


	p = 'Papa_Desktop-Closet'
	p = 'Papa_Desktop-eMachine'
	p = 'Papa_Drive_1997-2006_(Win98)'
	p = 'Papa_Laptop_2017.11.23'
	p = 'Papa_*'

	indexFiles = _v.myIndexes + _v.slash + '0A{*'


	if _.switches.isActive('Priority') == True:
		indexFiles = _v.myIndexes + _v.slash + '0' + _.switches.value('Priority') + '{*'


	if _.switches.isActive('Dad') == True:
		indexFiles = _v.myIndexes + _v.slash + 'Dad_201*'

	if _.switches.isActive('Papa') == True:
		indexFiles = _v.myIndexes + _v.slash + p
		# indexFiles = _v.myIndexes + _v.slash + 'Papa_Laptop_2017.11.23'

	if _.switches.isActive('Public') == True:
		indexFiles = _v.myIndexes + _v.slash + 'Public_*'

	if _.switches.isActive('IndexFile') == True:
		indexFiles = _v.myIndexes + _v.slash + str(_.switches.value('IndexFile')) + '*'

	if _.switches.isActive('One') == True:
		indexFiles = _v.myIndexes + _v.slash + '01{*'

	if _.switches.isActive('Two') == True:
		indexFiles = _v.myIndexes + _v.slash + '02{*'

	if _.switches.isActive('Eight') == True:
		indexFiles = _v.myIndexes + _v.slash + '08{*'

	if _.switches.isActive('Bookmarks') == True:
		indexFiles = _v.myBookmarks + _v.slash + '*.txt'

	if _.switches.isActive('Tickets') == True:
		indexFiles = _v.myTickets + _v.slash + '*.txt'

	if _.switches.isActive('SearchIn') == True:
		indexFiles = _.switches.value('SearchIn')



	theList = []


	if type(_.appData[__.appReg]['pipe']) == list:
		indexFiles = []
		# _.switches.fieldSet('FileName','active',True)
		# _.switches.fieldSet('JustName','active',False)
		i = 0
		for path in _.appData[__.appReg]['pipe']:
			path = path.replace('\r','')
			path = path.replace('\n','')
			path = str(path)
			if os.path.isfile(path) == True:
				# _.pr(path)
				shouldUseFile = True
				if _.switches.isActive('Text'):
					# mime = mimetypes.guess_type(path)
					# if not str(mime) == "('text/plain', None)":
					if _mime.isBinary(path):
						shouldUseFile = False

				if shouldUseFile:
					indexFiles.append(str(path))
			i += 1
		# for path in pipeResults:
		#   path = path.replace('\r','')
		#   path = path.replace('\n','')
		#   if os.path.isfile(path) == True:
		#       # _.pr(path)
		#       shouldUseFile = True
		#       if _.switches.isActive('Text'):
		#           mime = mimetypes.guess_type(path)
		#           if not str(mime) == "('text/plain', None)":
		#               shouldUseFile = False

		#       if shouldUseFile:
		#           indexFiles.append(str(path))
		takeAction()
	else:
		pass
		takeAction()
indexFiles = ''
if _.switches.isActive('Errors') == True:
	_.switches.print()



########################################################################################
if __name__ == '__main__':
	action()