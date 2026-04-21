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
import datetime

# import sys
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

# _.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.switches.register('Input', '-i,-f,-file','file.txt')
_.switches.register('Password', '-password','123')
_.switches.register('NamePassword', '-pn,-np')
_.switches.register('NameDate', '-nd')
_.switches.register('UnZip', '-u,-unzip')
_.switches.register('UnZipNoFolder', '-nf')



_.appInfo=    {
	'file': '7z.py',
	'description': '7zip basics made simple',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p 7z -nd -pn -p 777 -f file')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass
def getExtension(string):
	ext0 = string.split('.')
	extId = len(ext0) - 1
	if extId > 0:
		ext = ext0[extId]
	else:
		ext = ''
	return ext
def removeExtension(string):
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
	return '"' + str(string) + '"'
def we(string):
	return string + '.7z'
########################################################################################
def action():
	if '_pw(' in _.switches.value('File'):
		_.switches.fieldSet('UnZip','active',True)
	if _.switches.isActive('UnZipNoFolder'):
		_.switches.fieldSet('UnZip','active',True)
	if not _.switches.isActive('UnZip') and _.switches.isActive('File'):
		file = _.switches.value('File')
		if os.path.isfile(file):
			baseName = removeExtension(file)
		elif os.path.isdir(file):
			baseName = file
		else:
			print('No File')
			sys.exit()
		
		z7 = _v.app7z()
		password = _.switches.value('Password')
		pwLabel = ''
		if _.switches.isActive('Password') and _.switches.isActive('NamePassword') and len(password) > 0:
			pwLabel = '_pw(' + password + ')'

		if _.switches.isActive('NameDate'):
			modifiedRaw = os.path.getmtime(file)
			modified = formatDate(modifiedRaw)
			baseNewName = modified + '-' + baseName + pwLabel
			# print(we(baseNewName))
			if not os.path.isfile(we(baseNewName)):
				nameFinal = baseNewName
			else:
				for x in range(1,100000000):
					nw = modified + '-' + str(x) + '-' + baseName + pwLabel
					if not os.path.isfile(we(nw)):
						nameFinal = nw
						break
			do = z7 + ' a ' + qt(we(nameFinal)) + ' ' + qt(file)
			
		else:
			do = z7 + ' a ' + qt(we(baseName + pwLabel)) + ' ' + qt(file)

		if _.switches.isActive('Password'):
			do = do + ' -p"' + password + '"'
		os.system('"' + do + '"')

	if _.switches.isActive('UnZip') and _.switches.isActive('File') and os.path.isfile(_.switches.value('File')):
		file = _.switches.value('File')
		baseName = removeExtension(file)
		z7 = _v.app7z()
		# print('test')
		if _.switches.isActive('Password'):
			pw = _.switches.value('Password')
			do = z7 + ' e ' + qt(file) + ' -p"' + pw + '" -oc:' + baseName
		else:
			if '_pw' in baseName:
				pwx = baseName.split('_pw(')
				pw = pwx[1][:-1]
				baseName = pwx[0]
				do = z7 + ' e ' + qt(file) + ' -p"' + pw + '" -oc:' + baseName
			else:
				do = z7 + ' e ' + qt(file) + ' -oc:' + baseName
				# do = z7 + ' e ' + qt(file) + ' ' + qt(baseName)

		if _.switches.isActive('UnZipNoFolder'):
			do = do.split('-oc')[0]
		
		os.system('"' + do + '"')

########################################################################################
if __name__ == '__main__':
	action()