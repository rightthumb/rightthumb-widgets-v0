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
# import sys
# import simplejson as json
# import shutil
# import sqlite3
import _rightThumb._construct as __
__.appReg = __name__
import _rightThumb._base2 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

# import _rightThumb._md5 as _md5
import _rightThumb._mimetype as _mime



# _.switches.register('Input', '-i,-f,-file','file.txt')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo[__name__] = {
	'file': 'mime.py',
	'description': '',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo[__name__]['examples'].append('p mime')


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True


_.switches.process()
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f





########################################################################################
# def genGUID():
#     string = str(uuid.uuid4())
#     string = uuid.uuid4().hex
#     string = uuid.uuid4()
#     result = str(string).upper()
#     result = '{' + result + '}'
#     return result

# def isText(file):
#     result = True
#     if _.switches.isActive('Text') == True:
#         mime = mimetypes.guess_type(file)
#         if str(mime) == "('text/plain', None)":
#             result = True
#         else:
#             result = False
#     return result

# def personalMime(file):
#     mime = mimetypes.guess_type(file)
#     print(mime)
#     if len(__.mimeTable) > 0:
#         print('yes')
#     else:
#         print('no')
#         isBinary(file)
#         # getMime(file)

# def newMime(file):
#     if isText(file):


# def isBinary(file):
#     mime = is_binary(file)
#     print(mime)

# def getMime(file):
#     path = os.path.realpath(file)
#     print(path)
#     # print(file)
#     md50 = _md5.md5(path)
#     print(md50)
#     temp = _v.stmp + _v.slash + genGUID()
#     # temp = _v.stmp + _v.slash + genGUID()
#     print(temp)
#     do = 'type "' + path + '" > "' + temp + '"'
#     os.system('"' + do + '"')
#     md51 = _md5.md5(temp)
#     print(md50, md51)



# def action2():

#     if _.switches.isActive('Input'):
#         f = _.ci2(_.switches.value('Input'))
#         # mime = mimetypes.guess_type(f)
#         # print(mime)
#         if os.path.isfile(f):
#             x = os.path.splitext(f)
#             personalMime(f)
#         else:
#             print('file error')

def action():
	folder = os.getcwd()
	dirList = os.listdir(folder)
	mimeTable = []
	i = 0
	for item in dirList:
		path = folder + _v.slash + item
		if os.path.isfile(item):
			mimeTable.append({'mimetype': _mime.what(path),'file': item})
	_.tables.register('mimeTable',mimeTable)
	print()

	_.tables.print('mimeTable','mimetype,file')
# _.switches.fieldSet('Long','active',True)
_.switches.fieldSet('Sort','active',True)
_.switches.fieldSet('Sort','value','mimetype')
########################################################################################
if __name__ == '__main__':
	action()