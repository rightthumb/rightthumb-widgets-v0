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

# index search
# 
# 
# 
# 
# pop bad files !!!!! Dont create new array !!!!!
# 
# 
# 
#  
import glob
import os.path
from os.path import join, getsize, isfile, isdir, splitext
import sys
# import mimetypes


import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import _rightThumb._mimetype as _mime

import platform

p = 'Papa_Desktop-Closet'
p = 'Papa_Desktop-eMachine'
p = 'Papa_Drive_1997-2006_(Win98)'
p = 'Papa_Laptop_2017.11.23'
p = 'Papa_*'

# for item in sys.argv:
#     print(item)

_.switches.register('_Raw', '')
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
_.switches.register('NotInFile', '-notinfile,-notin')
_.switches.register('NoCount', '--c')

_.appInfo = {
	'file': 'f.py',
	'description': 'Search in indexes or files',
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p f -i *.py + name -jn')
_.appInfo['examples'].append('p f -papa + \\GLENNALLEN\\ \\AppData\\ - \\Local\\ . | p line --c -p \\ 5 -u')
_.appInfo['examples'].append('p f -bm + tmp -n | p dir -b')
_.appInfo['examples'].append('p file + bm- | p f + { -jn | p line --c -make "xcopy /d/y {} Default(bookmarks)\\" | p execute')

_.appInfo['examples'].append('')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p backupFiles + signature certificates shared.js | p f + resendEmailValidate -jn -notin --c')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('b applog')
_.appInfo['examples'].append("""p f -in *war*.json + "-games" - loadEpoch | p line -p ;' 3""")
_.appInfo['examples'].append('')
_.switches.process()



#################################################################
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


# print(indexFiles)

if _.switches.isActive('SearchIn') == True:
	indexFiles = _.switches.value('SearchIn')
# if _.switches.isActive('Help') == True:

#     _.tables.register('Auto',_.switch)
#     _.tables.print('Auto','name,switch,expected_input_example')
#     sys.exit()

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
		# print(result)
	return result

def executeSearch(filename,files,search):
	global theList
	global foundInFile
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
					print(filename)
				else:
					clean = _v.myBookmarks + _v.slash+'BM-'
					if os.path.isdir(line) == True:
						found = 'Good'
					else:
						found = 'Bad'
					print(found + '\t ' + filename.replace(clean,'').replace('.txt','') + ' = ' + line)
			elif _.switches.isActive('FileName') == True:
				# print(filename + ':' + line)
				newLine = line
				newLine = _str.removeAll(newLine,'\t')
				newLine = newLine.replace('\n','')
				newLine = newLine.replace('\r','')
				newLine = _str.replaceDuplicate(newLine,' ')
				newLine = _str.cleanFirst(newLine,' ')
				theList.append({'filename': filename,'string': newLine,'line': i})
			elif _.switches.isActive('JustName') == True:
				if _.switches.isActive('NotInFile'):
					foundInFile.append(filename)
				else:
					print(filename)
				break
			else:
				print(line)
def takeAction():
	global indexFiles
	global theList
	global foundInFile
	global theFileList
	search = []
	filename = ''
	# print(indexFiles)
	# print(_.switches.value('_Raw'))
	# print(_.switches.value('Plus'))
	# print(_.switches.value('Minus'))
	# print(indexFiles)
	# os._exit(0)
	if type(pipeResults) == list:
		lookIn = indexFiles
	elif not platform.system() == 'Windows' and type(indexFiles) == str and ',' in indexFiles and os.path.isfile(indexFiles.split(',')[0]):
		lookIn = indexFiles.split(',')
	else:
		lookIn = glob.glob( indexFiles )

	# print( lookIn )
	for files in lookIn:
		if _.switches.isActive('Force'):
			mimeTest = True
		else:
			mimeTest = _mime.isText(files)
		if os.path.isfile(files) == True and mimeTest:
			try:
				with open(files, 'r') as ins:
					filename = ins.name
					theFileList.append( filename )
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
						print('Error: ' + str(filename))
			# HERE
	if _.switches.isActive('FileName') == True:
		print()
		_.switches.fieldSet('Long','active',True)
		_.switches.fieldSet('GroupBy','active',True)
		_.switches.fieldSet('GroupBy','value','filename')
		_.tables.register('Auto',theList)
		_.tables.print('Auto','filename,line,string')

	if _.switches.isActive('NotInFile'):
		if not _.switches.isActive('NoCount'):
			print()
		if len( foundInFile ):


			if len(foundInFile) == len(theFileList):
				if not _.switches.isActive('NoCount'):
					print( 'Found in ALL', len(theFileList), 'files' )

			else:
				if not _.switches.isActive('NoCount'):
					print( 'Found in:', len(foundInFile), 'of', len(theFileList), 'files' )
					print( 'Not in', len(theFileList)-len(foundInFile) )
					print()
					print( 'Not In:' )
					print()
				for file in theFileList:
					if not file in foundInFile:
						print( file )
		else:
			if not _.switches.isActive('NoCount'):
				print( 'Not in any of the', len(theFileList), 'files' )


foundInFile = []
theFileList = []

theList = []
pipeResults = ''
if not sys.stdin.isatty():
	pipeResults = sys.stdin.readlines()
	try:
		if not pipeResults[0][0] in _str.safeChar:
			pipeResults[0] = pipeResults[0][1:]
	except Exception as e:
		pass

if type(pipeResults) == list:
	indexFiles = []
	# _.switches.fieldSet('FileName','active',True)
	# _.switches.fieldSet('JustName','active',False)
	i = 0
	for path in pipeResults:
		path = path.replace('\r','')
		path = path.replace('\n','')
		path = str(path)
		if os.path.isfile(path) == True:
			# print(path)
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
	#     path = path.replace('\r','')
	#     path = path.replace('\n','')
	#     if os.path.isfile(path) == True:
	#         # print(path)
	#         shouldUseFile = True
	#         if _.switches.isActive('Text'):
	#             mime = mimetypes.guess_type(path)
	#             if not str(mime) == "('text/plain', None)":
	#                 shouldUseFile = False

	#         if shouldUseFile:
	#             indexFiles.append(str(path))
	takeAction()
else:
	pass
	takeAction()

if _.switches.isActive('Errors') == True:
	_.switches.print()