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

# import _rightThumb._getPipe as _getPipe

# NAME             FRIENDLY MONTH         FRIENDLY WEEK    DAY OF THE WEEK    DATE MODIFIED

# ________________________________________________________________________________________________________________________


# crud2.py         0 months ago: Dec      48 weeks ago     Monday             2018-12-03 23:31:02


# crudConfig.py                           51 weeks ago     Saturday           2018-12-29 14:09:25
# ________________________________________________________________________________________________________________________


# crud.py          ( This month: Jan )    ( This week )    Wednesday          2019-01-02 10:09:06

#          3 files 48.95 KB





#                                                    500       dirRows not inline






import sys
import glob
import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext
import uuid
from operator import itemgetter
from datetime import datetime as dt, timedelta
import datetime
import time
from threading import Timer

from datetime import date
from dateutil import rrule
# from dateutil.rrule import rrule, MONTHLY
# from datetime import datetime
from dateutil import relativedelta
import math
import calendar
import ast
import simplejson as json
import _rightThumb._vars as _v


import sqlite3

import hashlib


import colorama
colorama.init()

import _rightThumb._construct as __


##############################################################


##############################################################
# import arrow

# DEFAULT_TIMEOUT = 1

# for x in sys.argv:
#     print(x)
# print('')
# os.listdir(sys.argv[1]) # returns list


################################################################# #################################################################


defaultCachFile = 'ol.c'

__.color_palette = 0
printAltName=True

class Color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

class ColorBold:
	Gray = '\033[1;30;40m'
	Red = '\033[1;31;40m'
	Green = '\033[1;32;40m'
	Yellow = '\033[1;33;40m'
	Blue = '\033[1;34;40m'
	Magenta = '\033[1;35;40m'
	Cyan = '\033[1;36;40m'
	White = '\033[1;37;40m'
	END = '\033[0m'


class BackgroundGrey:
	BLACK = '\033[0;30;47m'
	RED = '\033[0;31;47m'
	GREEN = '\033[0;32;47m'
	BROWN = '\033[0;33;47m'
	BLUE = '\033[0;34;47m'
	MAGENTA = '\033[0;35;47m'
	CYAN = '\033[0;36;47m'
	GRAY = '\033[0;37;40m'
	END = '\033[0m'
	
class BackgroundGreyBold:
	BLACK = '\033[1;30;47m'
	RED = '\033[1;31;47m'
	GREEN = '\033[1;32;47m'
	BROWN = '\033[1;33;47m'
	BLUE = '\033[1;34;47m'
	MAGENTA = '\033[1;35;47m'
	CYAN = '\033[1;36;47m'
	GRAY = '\033[1;37;40m'
	END = '\033[0m'

class Background:
	RED = '\033[1;37;41m'
	GREEN = '\033[1;37;42m'
	YELLOW = '\033[1;37;43m'
	BLUE = '\033[1;37;44m'
	PURPLE = '\033[1;37;45m'
	LIGHT_BLUE = '\033[1;37;46m'
	GREY = '\033[1;37;47m'
	BLACK = '\033[1;37;48m'
	END = '\033[0m'
row_colors = []

row_colors.append([ 0, Background.BLUE ])
row_colors.append([ 0, Background.LIGHT_BLUE ])
row_colors.append([ 0, Background.PURPLE ])

row_colors.append([ 1, BackgroundGrey.RED ])
row_colors.append([ 1, BackgroundGrey.BROWN ])
row_colors.append([ 1, BackgroundGrey.BLUE ])

row_colors.append([ 2, Color.CYAN ])
row_colors.append([ 2, Color.GREEN ])

row_colors.append([ 3, ColorBold.Red ])

row_colors_ID = 0



def buldColorTable( tableID ):
	global row_colors
	newColorTable = []
	for row in row_colors:
		if row[0] == tableID:
			newColorTable.append( row[1] )
	return newColorTable

def colorNext( tableID ):
	row_colors = buldColorTable( tableID )
	global row_colors_ID
	row_colors_ID += 1
	# if row_colors_ID == len(row_colors):
	if row_colors_ID % len(row_colors) == 0:
		row_colors_ID = 0

def colorID( tableID, up=True ):
	row_colors = buldColorTable( tableID )
	global row_colors_ID
	result = row_colors[row_colors_ID]
	if up:
		colorNext( tableID )
	return result

def colorizeRow( row, tableID=False ):

	if isSwitchActive('NoColor'):
		print( row )
		return False


	if type(tableID) == bool:
		tableID = __.color_palette
	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		print( row )
	else:
		if hasVisible(row):
			up =True
		else:
			up =False
		# print( 'tableID:', tableID, colorID( tableID ) )
		print( colorID( tableID, up ) + row + Background.END )

def printBold( string, color='white' ):

	if isSwitchActive('NoColor'):
		print( string )
		return False

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		print( ColorBold.White + string + ColorBold.END )
	elif color == 'red':
		print( ColorBold.Red + string + ColorBold.END )
	elif color == 'gray' or color == 'grey':
		print( ColorBold.Gray + string + ColorBold.END )
	elif color == 'green':
		print( ColorBold.Green + string + ColorBold.END )
	elif color == 'yellow':
		print( ColorBold.Yellow + string + ColorBold.END )
	elif color == 'blue':
		print( ColorBold.Blue + string + ColorBold.END )
	elif color == 'magenta':
		print( ColorBold.Magenta + string + ColorBold.END )
	elif color == 'cyan':
		print( ColorBold.Cyan + string + ColorBold.END )


def inlineColorGroup( row, tableID=False ):

	if isSwitchActive('NoColor'):
		return row

	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		tableID = __.color_palette
	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		print( row )
	else:
		if hasVisible(row):
			up =True
		else:
			up =False
		# print( 'tableID:', tableID, colorID( tableID ) )
		return colorID( tableID, up ) + row + Background.END


def inlineBold( string, color='white' ):

	if isSwitchActive('NoColor'):
		return string
	
	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		return ColorBold.White + string + ColorBold.END 
	elif color == 'red':
		return ColorBold.Red + string + ColorBold.END 
	elif color == 'gray' or color == 'grey':
		return ColorBold.Gray + string + ColorBold.END 
	elif color == 'green':
		return ColorBold.Green + string + ColorBold.END 
	elif color == 'yellow':
		return ColorBold.Yellow + string + ColorBold.END 
	elif color == 'blue':
		return ColorBold.Blue + string + ColorBold.END 
	elif color == 'magenta':
		return ColorBold.Magenta + string + ColorBold.END 
	elif color == 'cyan':
		return ColorBold.Cyan + string + ColorBold.END 

visibleChar = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
def hasVisible( data ):
	global visibleChar
	for char in data:
		if char in visibleChar:
			return True
	return False

################################################################# #################################################################

def getSize(fileobject):
	fileobject.seek(0,2) # move the cursor to the end of the file
	size = fileobject.tell()
	return size

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


def folderDepth(folder):
	global errors
	global folderDepthMax
	getSubFolderData = True
	base = 1
	# print('--- Starting ---\n{}\n'.format(folder))
	try:
		os.listdir(folder)
		continueThis = True
	except Exception as e:
		errors.append({'id': 0, 'function': 'folderDepth()', 'cnt': 1, 'location': 'os.listdir(folder)', 'vars': [{'name': 'folder', 'value': folder}], 'error': e})
		continueThis = False


	if continueThis:
		if os.path.isdir(folder):
			dirList = os.listdir(folder)
			for item in dirList:
				path = folder + _v.slash + item
				if os.path.isdir(item):
					if base <= folderDepthMax:
						base += folderDepth(path)
					else:
						getSubFolderData = False
	return True
	# return base
def folderSizeX(path):
	size = 0
	if os.path.isdir(path):
		for item in os.walk(path):
			for file in item[2]:
				try:
					size += getsize(join(item[0], file))
				except:
					size = 0
					# print("error with file:  " + join(item[0], file))
	return size

def folderSizeX2(folder):
	global errors
	base = 0
	global timeoutKill
	# print('--- Starting ---\n{}\n'.format(folder))

	try:
		os.listdir(folder)
		continueThis = True
	except Exception as e:
		errors.append({'id': 1, 'function': 'folderSizeX()', 'cnt': 1, 'location': 'os.listdir(folder)', 'vars': [{'name': 'folder', 'value': folder}], 'error': e})
		continueThis = False


	if continueThis:
		if os.path.isdir(folder):
			dirList = os.listdir(folder)
			for item in dirList:
				path = folder + _v.slash + item
				if os.path.isdir(item):
					try:
						getSubFolderData = folderDepth(path)
					except Exception as e:
						getSubFolderData = False
					if isSwitchActive('RecursionFolderSize') and timeoutKill == False and getSubFolderData:
						base += folderSizeX(path)
					else:
						pass

				else:
					if os.path.isfile(path):

						try:
							statinfo = os.stat(path)
							size = statinfo.st_size
							# file = open(path, 'rb')
							# size = getSize(file)
							base += size
							# print('---------')
							# print(size)
							# print(base)
							# file.close
						except Exception as e:
							errors.append({'id': 2, 'function': 'folderSizeX()', 'cnt': 2, 'location': "file = open(path, 'rb')", 'vars': [{'name': 'folder', 'value': folder}], 'error': e})
					else:
						try:
							base += folderSizeX(path)
						except Exception as e:
							errors.append({'id': 3, 'function': 'folderSizeX()', 'cnt': 3, 'location': 'base += folderSizeX(path)', 'vars': [{'name': 'folder', 'value': folder}], 'error': e})
		else:
			print('not a folder')
	return base

def attrib(path, a=None, s=None, h=None, r=None, i=None):
	attrs=[]
	if r==True:    attrs.append('+R')
	elif r==False: attrs.append('-R')
	if a==True:    attrs.append('+A')
	elif a==False: attrs.append('-A')
	if s==True:    attrs.append('+S')
	elif s==False: attrs.append('-S')
	if h==True:    attrs.append('+H')
	elif h==False: attrs.append('-H')
	if i==True:    attrs.append('+I')
	elif i==False: attrs.append('-I')

	if attrs: # write attributes
		cmd = attrs
		cmd.insert(0,'attrib')
		cmd.append(path)
		cmd.append('/L')
		return subprocess.call(cmd, shell=False)

	else: # just read attributes
		output = subprocess.check_output(
			['attrib', path, '/L'],
			shell=False, universal_newlines=True
		)[:9]
		attrs = {'A':False, 'S':False, 'H':False, 'R':False, 'I':False}
		for char in output:
			if char in attrs:
				attrs[char] = True
		return attrs

#########################################################
#########################################################

def buildResult(subF,folder):
	global errors
	global timeoutKill
	global dirRows
	global cursor
	global cursor2
	global conn
	global conn2
	try:
		dirList = os.listdir(folder)
	except Exception as e:
		dirList = ''
	
	for item in dirList:
		path = folder + _v.slash + item
		path = cleanAll(path,_v.slash+_v.slash,_v.slash)
		# path = replaceAll(path,_v.slash,_v.slash+_v.slash)
		# print(path)
		ext = ''
		if os.path.isdir(path):
			created = ''
			createdRaw = 0
			modified = ''
			modifiedRaw = 0
			size = 0
			sizeF = ''
			try:
				# getSubFolderData = folderDepth(path)
				getSubFolderData = True
			except Exception as e:
				getSubFolderData = False
			if isSwitchActive('RecursionFolderSize') and timeoutKill == False and getSubFolderData:
				
				
				try:
					# path = path.replace(_v.slash,_v.slash+_v.slash)
					# print(path)
					# path = 'E:\\tech\\scripts\\python'
					# print(path)
					# path = cleanAll(path,_v.slash+_v.slash,_v.slash)
					size = folderSizeX(path)
					sizeF = formatSize(size)
				except Exception as e:
					errors.append({'id': 4, 'function': 'buildResult()', 'cnt': 1, 'location': 'size = folderSizeX(path)', 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item},{'name': 'path', 'value': path}], 'error': e})

				# sizeF += ' *F'
				try:
					sub_dir = glob.glob(path + '/*') # * means all if need specific format then *.csv
					sub_file = max(sub_dir, key=os.path.getctime)
					create_sub_file_path = sub_file
					sub_dir = glob.glob(path + '/*') # * means all if need specific format then *.csv
					sub_file = max(sub_dir, key=os.path.getmtime)
					mod_sub_file_path = sub_file
				except Exception as e:
					errors.append({'id': 5, 'function': 'buildResult()', 'cnt': 2, 'location': 'sub_file = max(sub_dir, key=os.path.getctime)', 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})
				try:
					if os.path.isfile(create_sub_file_path):
						file = open(create_sub_file_path, 'rb')
						createdRaw = os.path.getctime(create_sub_file_path)
						created = formatDate(createdRaw)
					if os.path.isfile(mod_sub_file_path):
						file = open(mod_sub_file_path, 'rb')
						modifiedRaw = os.path.getmtime(mod_sub_file_path)
						modified = formatDate(modifiedRaw)
				except Exception as e:
					errors.append({'id': 6, 'function': 'buildResult()', 'cnt': 3, 'location': "file = open(create_sub_file_path, 'rb')", 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})

			if isSwitchActive('Recursion') and timeoutKill == False and getSubFolderData:
				buildResult(1,path)
			else:
				if modifiedRaw > 100:
					year = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[0]
					woy = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[1]
					dow = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[2]
					currentDate = time.time()
					thisweek = datetime.datetime.fromtimestamp( int(currentDate) ).isocalendar()[1]



					weekAndYear = round(woy * 0.01,2) + year
					# weekAndYear = str(year) + str( round(woy * 0.01,2) )
					dow = dowConvert(dow)
					month = round(int(formatDateMonth(modifiedRaw))* 0.01,2) + year
					month = str(year) + '.' + str(formatDateMonth(modifiedRaw))
				else:
					friendlyMonth1 = ''
					friendlyWeek1 = ''
					woy = ''
					month = 0
					weekAndYear = 0
					dow = dowConvert(0)
					path2 = os.path.realpath(path)
				if isSwitchActive('ResolveIDs'):
					item = resolveIDs(item)
				try:
					if os.path.isdir(path):
						createdRaw = os.stat(path).st_ctime
						created = formatDate(createdRaw)
					if os.path.isdir(path):
						modifiedRaw = os.stat(path).st_mtime
						modified = formatDate(modifiedRaw)
				except Exception as e:
					errors.append({'id': 61, 'function': 'buildResult()', 'cnt': 3, 'location': "file = open(create_sub_file_path, 'rb')", 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})
				try:
					if os.path.isdir(path):
						size = os.stat(path).ST_SIZE
						sizeF = formatSize(size)
				except Exception as e:
					errors.append({'id': 62, 'function': 'buildResult()', 'cnt': 3, 'location': "file = open(create_sub_file_path, 'rb')", 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})
				


				if isSwitchActive('Database'):
					cursor.execute("INSERT INTO files VALUES ('"+str(path2)+"', '"+str(fileNameLength(item, ''))+"', '"+str(item)+"', '"+str(folder)+"', '', '', '"+int(size)+"', '"+str(sizeF)+"', '"+int(createdRaw)+"', '"+int(modifiedRaw)+"', '"+str(created)+"', '"+str(modified)+"', 'Folder', '0', '', '"+woyPad(weekAndYear)+"', '"+str(woy)+"', '"+str(dow)+"', '"+str(month)+"', '"+str(friendlyWeek1)+"', '"+str(friendlyMonth1)+"')")
					conn.commit()
					if isSwitchActive('MD5'):
						try:
							md5 = md5Gen(path)
						except Exception as e:
							md5 = 'Error'
						
						cursor2.execute("INSERT INTO md5 VALUES ('"+str(md5)+"', '"+str(path2)+"',  '"+str(item)+"', '"+str(folder)+"', '"+int(size)+"', '"+int(createdRaw)+"', '"+int(modifiedRaw)+"')")
						conn2.commit()

				else:
					pass
					# friendlyMonth1 = friendlyMonthNew(modifiedRaw)
					# friendlyWeek1 = friendlyWeekNew(modifiedRaw)
					# if isSwitchActive('GroupBy') == False:
					#     # if len(friendlyMonth1) > 0:
					# dirRows.append({'path': path2, 'name_': fileNameLength(item,''), 'name': item, 'folder': folder, 'stat': '', 'attrib': '', 'bytes': size, 'size': sizeF, 'date_created_raw': createdRaw, 'date_modified_raw': modifiedRaw, 'date_created': created, 'date_modified': modified, 'type': 'Folder', 'typesort': 0, 'ext': '', 'week_of_year': weekAndYear, 'week_of_year_': woy, 'day_of_the_week': dow, 'month': month, 'friendly_week': friendlyWeek1, 'friendly_month': friendlyMonth1})



		else:
			if os.path.isfile(path) and pathCheckBase(path):
				attribs = 'H'
				size = 0
				sizeF = ''
				createdRaw = 0
				created = ''
				modifiedRaw = 0
				modified = ''
				try:
					stat = os.stat(path)
					size = stat.st_size
					# file = open(path, 'rb')
					# size = getSize(file)
					sizeF = formatSize(size)
					ext = getExtension(item)

					
					attri = attrib(os.path.join(folder,item))
					attribs = getAttribs(attri)
					# file.close
				except Exception as e:
					errors.append({'id': 7, 'function': 'buildResult()', 'cnt': 4, 'location': "file = open(path, 'rb')", 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})
					

				try:
					if isSwitchActive('Hidden'):
						createdRaw = os.path.getctime(path)
						created = formatDate(createdRaw)
						modifiedRaw = os.path.getmtime(path)
						modified = formatDate(modifiedRaw)
						displayThis = True
					elif attribs.find('H') == -1:
						createdRaw = os.path.getctime(path)
						created = formatDate(createdRaw)
						modifiedRaw = os.path.getmtime(path)
						modified = formatDate(modifiedRaw)
						displayThis = True
					else:
						displayThis = False

				except Exception as e:
					errors.append({'id': 8, 'function': 'buildResult()', 'cnt': 5, 'location': 'createdRaw = os.path.getctime(path)', 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})
				if modifiedRaw > 100:
					year = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[0]
					woy = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[1]
					dow = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[2]
					currentDate = time.time()
					thisweek = datetime.datetime.fromtimestamp( int(currentDate) ).isocalendar()[1]
					# friendlyWeek0 = thisweek - woy

					dow = dowConvert(dow)
					month = round(int(formatDateMonth(modifiedRaw))* 0.01,2) + year
					weekAndYear = round(woy * 0.01,2) + year
					# weekAndYear = str(year) + str( round(woy * 0.01,2) )
					month = str(year) + '.' + str(formatDateMonth(modifiedRaw))
				else:
					friendlyWeek1 = ''
					friendlyMonth1 = ''
					woy = ''
					month = 0
					weekAndYear = 0
					dow = dowConvert(0)
					# woy = datetime.date(modifiedRaw).isocalendar()[1]
				# print(str(year) + str(woy) + str(dow))
				# date.today().isocalendar()[1]
				if displayThis:
					path2 = os.path.realpath(path)
					if isSwitchActive('ResolveIDs'):
						item = resolveIDs(item)
					if isSwitchActive('Database'):
						# print("path2",type(path2))
						# print("fileNameLength(item, ext)",type(fileNameLength(item, ext)))
						# print("item",type(item))
						# print("folder",type(folder))
						# print("stat",type(stat))
						# print("attribs",type(attribs))
						# print("size",type(size))
						# print("sizeF",type(sizeF))
						# print("createdRaw",type(createdRaw))
						# print("modifiedRaw",type(modifiedRaw))
						# print("created",type(created))
						# print("modified",type(modified))
						# print("File",type("File"))
						# print("1",type(1))
						# print("ext",type(ext))
						# print("weekAndYear",type(weekAndYear))
						# print("woy",type(woy))
						# print("dow",type(dow))
						# print("month",type(month))
						# print("friendlyWeek1",type(friendlyWeek1))
						# print("friendlyMonth1",type(friendlyMonth1))
						# sys.exit()
						# print("'"+str(path2)+"', '"+str(fileNameLength(item, ext))+"', '"+str(item)+"', '"+str(folder)+"', 'str(stat)', '"+str(attribs)+"', '"+int(size)+"', '"+str(sizeF)+"', '"+int(createdRaw)+"', '"+int(modifiedRaw)+"', '"+str(created)+"', '"+str(modified)+"', 'File', '1', '"+str(ext)+"', '"+str(weekAndYear)+"', '"+str(woy)+"', '"+str(dow)+"', '"+str(month)+"', '"+str(friendlyWeek1)+"', '"+str(friendlyMonth1)+"'")
						# sys.exit()
						# print('works')
						cursor.execute("INSERT INTO files VALUES ('"+str(path2)+"','"+str(fileNameLength(item, ext))+"','"+str(item)+"','"+str(folder)+"','str(stat)','"+str(attribs)+"','"+str(size)+"','"+str(sizeF)+"','"+str(createdRaw)+"','"+str(modifiedRaw)+"','"+str(created)+"','"+str(modified)+"','File','1','"+str(ext)+"','"+woyPad(weekAndYear)+"','"+str(woy)+"','"+str(dow)+"','"+str(month)+"','"+str(friendlyWeek1)+"','"+str(friendlyMonth1)+"')")
						# cursor.execute("INSERT INTO files VALUES ('"+str(path2)+"', '"+str(fileNameLength(item, ext))+"', '"+str(item)+"', '"+str(folder)+"', 'str(stat)', '"+str(attribs)+"', '"+int(size)+"', '"+str(sizeF)+"', '"+int(createdRaw)+"', '"+int(modifiedRaw)+"', '"+str(created)+"', '"+str(modified)+"', 'File', '1', '"+str(ext)+"', '"+str(weekAndYear)+"', '"+str(woy)+"', '"+str(dow)+"', '"+str(month)+"', '"+str(friendlyWeek1)+"', '"+str(friendlyMonth1)+"')")
						conn.commit()
						# dirRows = []
						if isSwitchActive('MD5'):
							try:
								md5 = md5Gen(path)
							except Exception as e:
								md5 = 'Error'
							# cursor2.execute("""CREATE TABLE md5 (md5 text, path text, name text, folder text, bytes int, date_created_raw int, date_modified_raw int )""")                            
							# cursor2.execute("INSERT INTO md5 VALUES ('"+str(md5)+"', '"+str(path2)+"',  '"+str(item)+"', '"+str(folder)+"', '"+str(size)+"', '"+int(createdRaw)+"', '"+int(modifiedRaw)+"')")
							# conn2.commit()
					else:
						friendlyMonth1 = friendlyMonthNew(modifiedRaw)
						friendlyWeek1 = friendlyWeekNew(modifiedRaw)
						# dirRows.append({'path': path2, 'name_': fileNameLength(item,ext), 'name': item, 'folder': folder, 'stat': stat, 'attrib': attribs, 'bytes': size, 'size': sizeF, 'date_created_raw': createdRaw, 'date_modified_raw': modifiedRaw, 'date_created': created, 'date_modified': modified, 'type': 'File', 'typesort': 1, 'ext': ext, 'week_of_year': weekAndYear, 'week_of_year_': woy, 'day_of_the_week': dow, 'month': month, 'friendly_week': friendlyWeek1, 'friendly_month': friendlyMonth1})
						global defaultCachFile
						if not item == defaultCachFile:
							dirRows.append( {
												'path': path2,
												'name_': fileNameLength(item,ext),
												'name': item,
												'folder': folder,
												'stat': stat,
												'attrib': attribs,
												'bytes': size,
												'size': sizeF,
												'date_created_raw': createdRaw,
												'date_modified_raw': modifiedRaw,
												'date_created': created,
												'date_modified': modified,
												'type': 'File',
												'typesort': 1,
												'ext': ext,
												'week_of_year': woyPad(weekAndYear),
												'week_of_year_': woy,
												'day_of_the_week': dow,
												'month': month,
												'friendly_week': friendlyWeek1,
												'friendly_month': friendlyMonth1
							})

	return dirRows

#########################################################
#########################################################
def friendlyWeekNew(modifiedRaw):
	friendlyWeek1 = ''
	currentDate = time.time()
	currentYear = formatDateYear(currentDate)
	currentWeek = datetime.datetime.fromtimestamp(currentDate).isocalendar()[1]
	# print(date(2018, 12, 28).isocalendar()[1])
	try:
		modifiedRaw = int(modifiedRaw)
		testYear = formatDateYear(modifiedRaw)
		woy = datetime.datetime.fromtimestamp(modifiedRaw).isocalendar()[1]
		# friendlyWeek0 = weeks_between(modifiedRaw, currentDate)
		friendlyWeek0 = weeks_between(modifiedRaw, currentDate)
		# friendlyMonth0 = months_between(modifiedRaw, currentDate)


		if currentYear == testYear and currentWeek == woy:
			# friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
			# friendlyWeek1 += ' (This week)'
			friendlyWeek1 = '( This week )'
		elif (currentYear == testYear and currentWeek == lastWeek(woy)) or str(friendlyWeek0) == '1':
			friendlyWeek1 = '( Last week )'
		else:
			friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
	except Exception as e:
		pass

	return friendlyWeek1

def lastWeek(theNumber):
	theNumber = int(theNumber)
	if theNumber == 1:
		result = 52
	else:
		result = theNumber - 1
	return result


def friendlyMonthNew(modifiedRaw):
	friendlyMonth1 = ''
	currentDate = time.time()
	currentYear = formatDateYear(currentDate)
	try:
		modifiedRaw = int(modifiedRaw)
		testYear = formatDateYear(modifiedRaw)
		friendlyMonth0 = months_between(modifiedRaw, currentDate)
		littleMonth = monthByNumber(formatDateMonth(modifiedRaw))
		testMonth = formatDateMonth(modifiedRaw)
		testMonthThis = formatDateMonth(currentDate)
		if currentYear == testYear and testMonth == testMonthThis:
			friendlyMonth1 = '( This month: ' + littleMonth + ' )'
		elif currentYear == testYear and testMonth == lastMonth(testMonthThis):
			friendlyMonth1 = '( Last month: ' + littleMonth + ' )'

		else:
			if int(friendlyMonth0) > 12:
				years = math.floor(int(friendlyMonth0)/12)
				months = int(friendlyMonth0) - (years * 12)
				friendlyMonth1 = str(years) + ' years ' + str(months) + ' months ago: ' + littleMonth 
			else:
				friendlyMonth1 = str(friendlyMonth0) + ' months ago: ' + littleMonth
	except Exception as e:
		pass

	return friendlyMonth1


def lastMonth(month):
	result = ''
	if month == '01':
		result = '12'

	if month == '02':
		result = '01'

	if month == '03':
		result = '02'

	if month == '04':
		result = '03'

	if month == '05':
		result = '04'

	if month == '06':
		result = '07'

	if month == '07':
		result = '06'

	if month == '08':
		result = '07'

	if month == '09':
		result = '08'

	if month == '10':
		result = '09'

	if month == '11':
		result = '10'

	if month == '12':
		result = '11'
	return result


def fileNameLength(string,ext,l=0):
	global maxFileNameLength
	if l == 0:
		theLength = maxFileNameLength
	else:
		theLength = l

	result = ''
	toLong = False
	try:
		i = 0
		for L in string:
			if i <= theLength:
				result += L
			else:
				toLong = True
			i += 1
		if toLong:
			result += '...'
			if len(ext) > 0:
				result += '  .' + ext
	except Exception as e:
		result = string
	return result
def woyPad( woy ):
	woy = str(woy)
	if len(woy) == 6:
		woy+='0'
	return woy

def buildResultFromPipe():
	global pipeResults
	global totalsizeCalc
	global totalCountItems
	global cursor
	global cursor2
	global conn
	global conn2
	global defaultCachFile

	millTimeStamp = lambda: int(round(time.time() * 1000))
	totalsizeCalc = 0
	totalCountItems = 0
	if isSwitchActive('GroupBy'):
		if getSwitchValue('GroupBy') == 'none':
			updateSwitchField('GroupBy','active',False)
	for path in pipeResults:
		path = path.replace('\n','')
		path = path.replace('\r','')
		# path = path.encode('UTF-8')
		# path = str(path)
		path = pathCheck(path)
		if os.path.isfile(path):
			timeAudit = []
			try:
				# print(path)
				timeAudit.append({'stamp': millTimeStamp(),'where':0,'which':0})
				item = path.split(_v.slash)[-1]
				path2 = os.path.realpath(path)
				folder = path[:-len(item)-1]
				attribs = 'H'
				size = 0
				sizeF = ''
				createdRaw = 0
				created = ''
				modifiedRaw = 0
				modified = ''
				ext = ''
				timeAudit.append({'stamp': millTimeStamp(),'where':0,'which':1})
				try:
					timeAudit.append({'stamp': millTimeStamp(),'where':1,'which':0})
					stat = os.stat(path)
					size = stat.st_size
					# file = open(path, 'rb')
					# size = getSize(file)
					sizeF = formatSize(size)
					ext = getExtension(item)

					attri = attrib(os.path.join(folder,item))
					attribs = getAttribs(attri)
					# file.close
					timeAudit.append({'stamp': millTimeStamp(),'where':1,'which':1})
				except Exception as e:
					errors.append({'id': 7, 'function': 'buildResult()', 'cnt': 4, 'location': "file = open(path, 'rb')", 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})
					
				timeAudit.append({'stamp': millTimeStamp(),'where':2,'which':0})
				try:
					if isSwitchActive('Hidden'):
						createdRaw = os.path.getctime(path)
						created = formatDate(createdRaw)
						modifiedRaw = os.path.getmtime(path)
						modified = formatDate(modifiedRaw)
						displayThis = True
					elif attribs.find('H') == -1:
						createdRaw = os.path.getctime(path)
						created = formatDate(createdRaw)
						modifiedRaw = os.path.getmtime(path)
						modified = formatDate(modifiedRaw)
						displayThis = True
					else:
						displayThis = False
				except Exception as e:
					errors.append({'id': 8, 'function': 'buildResult()', 'cnt': 5, 'location': 'createdRaw = os.path.getctime(path)', 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})
				timeAudit.append({'stamp': millTimeStamp(),'where':2,'which':1})
				
				timeAudit.append({'stamp': millTimeStamp(),'where':3,'which':0})
				if modifiedRaw > 100:
					year = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[0]
					woy = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[1]
					dow = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[2]
					currentDate = time.time()
					thisweek = datetime.datetime.fromtimestamp( int(currentDate) ).isocalendar()[1]

					dow = dowConvert(dow)
					month = round(int(formatDateMonth(modifiedRaw))* 0.01,2) + year
					weekAndYear = round(woy * 0.01,2) + year
					# weekAndYear = str(year) + str( round(woy * 0.01,2) )
					month = str(year) + '.' + str(formatDateMonth(modifiedRaw))
				else:
					friendlyWeek1 = ''
					friendlyMonth1 = ''
					woy = ''
					month = 0
					weekAndYear = 0
					dow = dowConvert(0)
					# woy = datetime.date(modifiedRaw).isocalendar()[1]
				# print(str(year) + str(woy) + str(dow))
				# date.today().isocalendar()[1]
				timeAudit.append({'stamp': millTimeStamp(),'where':3,'which':1})
				if isSwitchActive('isFile'):
					print(path)
				else:
					if displayThis:
						global totalLINE
						totalLINE = '__________________________________'
						totalsizeCalc += size
						totalCountItems += 1
						if folder == '' or folder == None:
							folder = os.getcwd()
						if isSwitchActive('Bookmark'):
							bookmark = ''
							if 'BM-' in item and '.txt' in item:
								bookmark = item.replace('BM-','')
								bookmark = bookmark.replace('.txt','')
								bm_status = ' * No *'
								with open(path, 'r', encoding='latin-1') as bmFile:
									for line in bmFile:
										line = line.replace('\n','')
										line = line.replace('\r','')
										if len(line) > 1:
											bm_path = line
										# print(line)
										if os.path.isdir(line):
											bm_status = 'Works'
								bmFile.close()
							if isSwitchActive('ResolveIDs'):
								item = resolveIDs(item)

							if isSwitchActive('Database'):

								# ***************** timeAudit ERROR no field
								cursor.execute("INSERT INTO files VALUES ("+str(path2)+"','"+str(fileNameLength(item, ext))+"','"+str(bookmark)+"','"+str(bm_status)+"','"+str(fileNameLength(bm_path, '', 90))+"','"+str(item)+"','"+str(folder)+"','str(stat)','"+str(attribs)+"','"+str(size)+"','"+str(sizeF)+"','"+str(createdRaw)+"','"+str(modifiedRaw)+"','"+str(created)+"','"+str(modified)+"','"+str(created.split(' ')[0])+"','"+str(modified.split(' ')[0])+"','File','0','"+str(ext)+"','"+woyPad(weekAndYear)+"','"+str(woy)+"','"+str(dow)+"','"+str(month)+"','"+str(friendlyWeek1)+"','"+str(friendlyMonth1)+"',)")
								conn.commit()
								if isSwitchActive('MD5'):
									try:
										md5 = md5Gen(path2)
									except Exception as e:
										md5 = 'Error'
									
									cursor2.execute("INSERT INTO md5 VALUES ('"+str(md5)+"', '"+str(path2)+"',  '"+str(item)+"', '"+str(folder)+"', '"+str(size)+"', '"+str(createdRaw)+"', '"+str(modifiedRaw)+"')")
									conn2.commit()
							else:
								friendlyMonth1 = friendlyMonthNew(modifiedRaw)
								friendlyWeek1 = friendlyWeekNew(modifiedRaw)
								
								if not item == defaultCachFile:
									dirRows.append({'timeAudit': timeAudit,'path': path2, 'name_': fileNameLength(item,ext), 'bookmark': bookmark, 'bm_status': bm_status, 'bm_path': fileNameLength(bm_path,'',90), 'name': item, 'folder': folder, 'stat': stat, 'attrib': attribs, 'bytes': size, 'size': sizeF, 'date_created_raw': createdRaw, 'date_modified_raw': modifiedRaw, 'date_created': created, 'date_modified': modified, 'date_created_': created.split(' ')[0], 'date_modified_': modified.split(' ')[0],'type': 'File', 'typesort': 1, 'ext': ext, 'week_of_year': woyPad(weekAndYear), 'week_of_year_': woy, 'day_of_the_week': dow, 'month': month, 'friendly_week': friendlyWeek1, 'friendly_month': friendlyMonth1})
						else:
							if isSwitchActive('ResolveIDs'):
								item = resolveIDs(item)
							if isSwitchActive('Database'):

								cursor.execute("INSERT INTO files VALUES ('"+str(path2)+"','"+str(fileNameLength(item, ext))+"','"+str(item)+"','"+str(folder)+"','str(stat)','"+str(attribs)+"','"+str(size)+"','"+str(sizeF)+"','"+str(createdRaw)+"','"+str(modifiedRaw)+"','"+str(created)+"','"+str(modified)+"','File','1','"+str(ext)+"','"+str(weekAndYear)+"','"+str(woy)+"','"+str(dow)+"','"+str(month)+"','"+str(friendlyWeek1)+"','"+str(friendlyMonth1)+"')")
								conn.commit()
								if isSwitchActive('MD5'):
									# print('test')
									try:
										md5 = md5Gen(path2)
									except Exception as e:
										md5 = 'Error'
									# md5 = md5Gen(str(path2))
									# print(md5)
									cursor2.execute("INSERT INTO md5 VALUES ('"+str(md5)+"', '"+str(path2)+"',  '"+str(item)+"', '"+str(folder)+"', '"+str(size)+"', '"+str(createdRaw)+"', '"+str(modifiedRaw)+"')")
									conn2.commit()
							else:
								friendlyMonth1 = friendlyMonthNew(modifiedRaw)
								friendlyWeek1 = friendlyWeekNew(modifiedRaw)
								
								if not item == defaultCachFile:
									dirRows.append({'timeAudit': timeAudit,'path': path2, 'name_': fileNameLength(item,ext), 'name': item, 'folder': folder, 'stat': stat, 'attrib': attribs, 'bytes': size, 'size': sizeF, 'date_created_raw': createdRaw, 'date_modified_raw': modifiedRaw, 'date_created': created, 'date_modified': modified, 'type': 'File', 'typesort': 1, 'ext': ext, 'week_of_year': woyPad(weekAndYear), 'week_of_year_': woy, 'day_of_the_week': dow, 'month': month, 'friendly_week': friendlyWeek1, 'friendly_month': friendlyMonth1})
			except Exception as e:
				pass
	return dirRows
def resolveIDs(name):
	global idResolution
	for idr in idResolution:
		newName = ' { { ' + idr['name'] + ' } } '
		name = name.replace(idr['id'],newName)
	return name
#########################################################
#########################################################

def monthByNumber(month):
	result = ''
	if str(month) == '01':
		result = 'Jan'
	if str(month) == '02':
		result = 'Feb'
	if str(month) == '03':
		result = 'Mar'
	if str(month) == '04':
		result = 'Apr'
	if str(month) == '05':
		result = 'May'
	if str(month) == '06':
		result = 'Jun'
	if str(month) == '07':
		result = 'Jul'
	if str(month) == '08':
		result = 'Aug'
	if str(month) == '09':
		result = 'Sep'
	if str(month) == '10':
		result = 'Oct'
	if str(month) == '11':
		result = 'Nov'
	if str(month) == '12':
		result = 'Dec'
	return result

def weeks_between(start_date, end_date):
	one = datetime.datetime.fromtimestamp(int(start_date)).isocalendar()[1]
	two = datetime.datetime.fromtimestamp(int(end_date)).isocalendar()[1]
	if one > two:
		result = one - two
	else:
		result = two - one
	return result
def weeks_between_old(start_date, end_date):
	start_date = datetime.date(int(formatDateYear(start_date)),int(formatDateMonth(start_date)),int(formatDateDay(start_date)))
	start_date_monday = (start_date - datetime.timedelta(days=start_date.weekday()))
	end_date = datetime.date(int(formatDateYear(end_date)),int(formatDateMonth(end_date)),int(formatDateDay(end_date)))
	num_of_weeks = math.ceil((end_date - start_date_monday).days / 7.0)
	return num_of_weeks - 1
def months_between(start_date, end_date):
	# start_date = int(start_date)
	# end_date = int(end_date)
	# st = str(formatDateYear(start_date)) + '-' + str(formatDateMonth(start_date)) + '-' +  str(formatDateDay(start_date)) 
	# en = str(formatDateYear(end_date)) + '-' + str(formatDateMonth(end_date)) + '-' +  str(formatDateDay(end_date))
	start = datetime.date(int(formatDateYear(start_date)), int(formatDateMonth(start_date)), int(formatDateDay(start_date)) )
	end = datetime.date(int(formatDateYear(end_date)), int(formatDateMonth(end_date)), int(formatDateDay(end_date)) )
	months = calculate_monthdelta(start, end)
	return months 
def calculate_monthdelta(date1, date2):
	def is_last_day_of_the_month(date):
		days_in_month = calendar.monthrange(date.year, date.month)[1]
		return date.day == days_in_month
	imaginary_day_2 = 31 if is_last_day_of_the_month(date2) else date2.day
	monthdelta = (
		(date2.month - date1.month) +
		(date2.year - date1.year) * 12 +
		(-1 if date1.day > imaginary_day_2 else 0)
		)
	# print monthdelta
	return monthdelta
def dowConvert(dow):
	result = ''
	if dow == 1:
		result = 'Monday'
	if dow == 2:
		result = 'Tuesday'
	if dow == 3:
		result = 'Wednesday'
	if dow == 4:
		result = 'Thursday'
	if dow == 5:
		result = 'Friday'
	if dow == 6:
		result = 'Saturday'
	if dow == 7:
		result = 'Sunday'
	return result


def getAttribs(rows):
	result = ''
	if rows['A']:
		result += 'A' 
	if rows['S']:
		result += 'S' 
	if rows['H']:
		result += 'H' 
	if rows['R']:
		result += 'R' 
	if rows['I']:
		result += 'I' 
	return result
def getExtension(string):
	ext0 = string.split('.')
	extId = len(ext0) - 1
	if extId > 0:
		ext = ext0[extId]
	else:
		ext = ''
	return ext
def tabGetMaxSpace(isDir,rows,name):
	global errors
	spacer = 1
	# print('*** ' + name)
	size = len(name) + spacer
	try:
		pass
		rows[0][name]
	except Exception as e:
		errors.append({'id': 9, 'function': 'tabGetMaxSpace()', 'cnt': 1, 'location': 'rows[0][name]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
		printBold('Error:','red')
		printBold('\tBad column input.')
		print(name)
		os._exit(0)
	# print(name)
	for item in rows:
		# print(item)
		text = item[name]
		if isDir:
			typ = item['typesort']
			if isSwitchActive('Yr') and (name == 'date_created' or name == 'date_modified'):
				text = str(text)
				text = text.replace('2017-','')
			if typ == 0 and name == 'name':
				text = formatFolderName(text)
		itemSize = len(str(text)) + spacer
		if itemSize > size:
			size = itemSize
	return size

def addSpace(string,max):
	dif = int(max) - len(string)
	build = ''
	for x in range(dif):
		build = build + ' '
	return build

def showColumn(isDir,rows,column,i):
	global errors
	global lastGroup
	global groupByList
	text = str(rows[i][column])
	groupBy = getSwitchValue('GroupBy')
	global spaces

	if isSwitchActive('GroupBy'):
		if getSwitchValue('GroupBy') == 'none':
			updateSwitchField('GroupBy','active',False)

	try:
		tabFix = spaces[column]
	except Exception as e:
		# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
		tabFix = tabGetMaxSpace(isDir,rows,column)
		spaces[column] = tabFix
	if isDir:
		typ = int(rows[i]['typesort'])
		if isSwitchActive('Yr') and (column == 'date_created' or column == 'date_modified'):
			text = str(text)
			text = text.replace('2017-','')
		if typ == 0 and column == 'name':
			text = formatFolderName(text)
		if isSwitchActive('GroupBy'):
			for gb in groupBy.split(','):
				gb = str(columnNickname2(gb))
				if column == gb:
					if not test(groupByList[gb],text):
						if columnNickname2(groupBy.split(',')[0]) == column:
							print(groupLine())
							for g in groupBy.split(','):
								groupByList[g] = ''
						else:
							print('')
						# if len(groupBy.split(',')) > 1:
						#     print('__________________________________________________________________________________________')
						# else:
						#     print('')
						groupByList[gb] = text
					else:
						text = ''
	result = text + addSpace(text,tabFix)
	return result

def showColumnCSV(isDir,rows,column,i):
	global errors
	text = str(rows[i][column])
	result = '"' + text + '"'
	return result

def groupLine():
	global columnHeaderLength
	global columnList
	columnNumber = len(columnList.split(','))
	loop = 0
	result = ''
	while loop < columnHeaderLength + (columnNumber * 4):
		result += '_'
		loop += 1
	return result
def test(one,two):
	if one == two:
		return True
	else:
		return False
def showColumnHeader(isDir,rows,column):
	global spaces
	global columnTab

	result = ''
	for c in column.split(','):
		c = columnNickname2(c)
		try:
			tabFix = spaces[c]
		except Exception as e:
			# errors.append({'id': 11, 'function': 'showColumn()', 'cnt': 2, 'location': 'tabFix = spaces[c]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}], 'error': e})
			tabFix = tabGetMaxSpace(isDir,rows,c)
			spaces[c] = tabFix
		result += c.replace('_',' ').upper() + addSpace(c,tabFix) + columnTab
	result += '\n'
	if not ',' in getSwitchValue('Column') and isSwitchActive('Column') and isSwitchActive('GroupBy') == False:
		result = ''
	return result

def showColumnHeaderCSV(isDir,rows,column):
	global spaces
	result = ''
	for c in column.split(','):
		c = columnNickname2(c)

		result += '"' + c.replace('_',' ').upper() + '"' + ','
	# result += '\n'
	return result

def showPreHeader(rows):
	global folder
	totalSize = 0
	for row in rows:
		# print(row['bytes'])
		byte = row['bytes']
		if type(byte) == int:
			totalSize += row['bytes']
	result = '-\nList of items in folder: {}\n{}\n-\n'.format(folder,formatSize(totalSize))
	# result = ''
	return result

def dirCacheGet():
	global _dirCache
	global _dirCache_p
	if getSwitchValue('Cache') == 'none' or getSwitchValue('Cache') == '' or getSwitchValue('Cache') == None:

		cacheFile = _dirCache
	else:
		if getSwitchValue('Cache') == '~p' or getSwitchValue('Cache') == 'p':
			cacheFile = _dirCache_p
		else:
			cacheFile = getSwitchValue('Cache')
	if os.path.isfile(cacheFile):
		os.system('attrib -h '+ cacheFile)
	with open(cacheFile,'r', encoding="latin-1") as json_file:
		json_data = json.load(json_file)
	return json_data

def getTable( theFile, tableTemp=False, printThis=False ):
	import _rightThumb._vars as _v
	# defaults to myTables
	if not type( tableTemp ) == bool:
		if tableTemp == 'split':
			file0 = _v.myTables + _v.slash+'tablesets'+_v.slash + theFile
	else:
		if tableTemp == True:
			file0 = _v.stmp + _v.slash + theFile
		else:
			file0 = _v.myTables + _v.slash + theFile

	if printThis:
		print('Loaded: ' + file0)
	if os.path.isfile(file0) == True:
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
	else:
		json_data = []
	return json_data

def saveTable( rows, theFile, tableTemp=False, printThis=True, indentCode=True, sort_keys=False ):
	import _rightThumb._vars as _v
	# defaults to myTables
	p = ''
	if not tableTemp:
		file0 = _v.myTables + _v.slash + theFile
		p = theFile
	else:
		file0 = _v.stmp + _v.slash + theFile
		p = file0
	if indentCode:
		dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
	else:
		dataDump = json.dumps(rows)
	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + p)
	return file0

def dirCacheSave(rows,cacheFile):
	if os.path.isfile(cacheFile):
		os.system('attrib -h '+ cacheFile)
	dataDump = json.dumps(rows, indent=4, sort_keys=True)
	f = open(cacheFile,'w')
	f.write(str(dataDump))
	f.close()
	# os.system('attrib +h '+ cacheFile)

def displayLine(rows):
	# print(type(rows))
	rows = displayLineExclude(rows)
	rows = displayLineIncludePlus(rows)
	rows = displayLineInclude(rows)
	rows = displayLineFolder(rows)
	rows = displayLineSize(rows)
	rows = displayLineAgo(rows)
	return rows

def pathCheck(string):
	string = displayLineExcludeString(string)
	string = displayLineIncludeString(string)
	return string

def pathCheckBase(string):
	string = displayLineExcludeString(string)
	string = displayLineIncludeString(string)
	if string == '':
		result = False
	else:
		result = True

	return result


def displayLineExcludeString_old(string):
	if isSwitchActive('Minus'):
		action = True
		for d in getSwitchValue('Minus').split(','):
			if d.upper() in string.upper():
				show = False
				string = ''
	return string


def displayLineIncludeString_old(string):
	if isSwitchActive('InPath'):
		action = False
		cnt = 0
		for d in getSwitchValue('InPath').split(','):
			if d.upper() in string.upper():
				cnt += 1
				
		# print(cnt,len(getSwitchValue('InPath').split(',')))
		if cnt == len(getSwitchValue('InPath').split(',')):
			show = True
		else:
			string = ''
	return string

def displayLineExclude_old(rows):
	action = False
	rowsNew = []

	if isSwitchActive('Minus'):
		
		action = True
		do = getSwitchValue('Minus').split(',')
		for r in rows:
			show = True
			val = r['path']
			for d in do:
				if d.upper() in val.upper():
					show = False
			if show:
				rowsNew.append(r)
	## END Minus

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows


def displayLineInclude_old(rows):
	action = False
	rowsNew = []

	if isSwitchActive('InPath'):
		action = True
		do = getSwitchValue('InPath').split(',')
		for r in rows:
			show = False
			val = r['path']
			cnt = 0
			for d in do:
				if d.upper() in val.upper():
					cnt += 1
			if cnt == len(do):
				show = True
			if show:
				rowsNew.append(r)
	## END InPath

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows
##############################################
def displayLineExcludeString(string):
	if not minusResults(string):
		string = ''
	return string

def displayLineIncludeString(string):
	if not positiveResults(string):
		string = ''
	return string

def positiveResults( string, plus='', plusOr=False ):
	# if plusOr or isSwitchActive('PlusOr'):
	#     plusOr = True
	
	plusOr = False
	if not plus == '':
		plusInput = plus
	else:
		plusInput = getSwitchValue('InPath')
	# print( )
	# print( plusInput, string )
	plusInput = plusInput.lower()
	string = string.lower()
	result = False
	# print((plusInput))
	plusList = plusInput.split(',')
	length = len(plusList)
	cnt = 0
	for s in plusList:
		s = s.lower()
		
		if len(s) > 1 and s[0] == '*':
			s = s.replace('*','')
			if string.endswith(s):
				cnt += 1
		elif len(s) > 1 and s[-1] == '*':
			s = s.replace('*','')
			if string.startswith(s):
				cnt += 1
		elif not string.find(ci(s)) == -1 or s in string:
			cnt += 1


		if length == cnt:
			result = True
			break
		if plusOr:
			if cnt > 0:
				result = True
	return result


def positiveResultsPlusOr( string, plus='' ):
	plusOr = True
	
	if not plus == '':
		plusInput = plus
	else:
		plusInput = getSwitchValue('PlusOr')

	# print( )
	# print( plusInput, string )
	plusInput = plusInput.lower()
	string = string.lower()
	result = False
	# print((plusInput))
	plusList = plusInput.split(',')
	length = len(plusList)
	cnt = 0
	for s in plusList:
		s = s.lower()
		
		if len(s) > 1 and s[0] == '*':
			s = s.replace('*','')
			if string.endswith(s):
				cnt += 1
		elif len(s) > 1 and s[-1] == '*':
			s = s.replace('*','')
			if string.startswith(s):
				cnt += 1
		elif not string.find(ci(s)) == -1 or s in string:
			cnt += 1


		if length == cnt:
			result = True
			break
		if plusOr:
			if cnt > 0:
				result = True
	return result


def positiveResults_old_2(string):
	if isSwitchActive('InPath'):
		plusInput = getSwitchValue('InPath')
		# print(plusInput)
		plusInput = plusInput.lower()
		string = string.lower()
		result = False
		# print((plusInput))
		plusList = plusInput.split(',')
		length = len(plusList)
		cnt = 0
		for s in plusList:
			s = s.lower()
			
			if len(s) > 1 and s[0] == '*':
				s = s.replace('*','')
				if string.endswith(s):
					cnt += 1
			elif len(s) > 1 and s[-1] == '*':
				s = s.replace('*','')
				if string.startswith(s):
					cnt += 1
			elif not string.find(ci(s)) == -1 or s in string:
				cnt += 1


			if length == cnt:
				result = True
				break
	else:
		result = True

	return result

def minusResults(string):
	if isSwitchActive('Minus'):
		string = string.lower()
		result = True
		try:
			for s in getSwitchValue('Minus').split(','):
				s = s.lower()
				if len(s) > 1 and s[0] == '*':
					s = s.replace('*','')
					if string.endswith(s):
						result = False
						break
				elif len(s) > 1 and s[-1] == '*':
					s = s.replace('*','')
					if string.startswith(s):
						result = False
						break
				if not string.find(ci(s)) == -1 or s in string:
					result = False
					break
		except Exception as e:
			pass
	else:
		result = True
	return result









def displayLineExclude(rows):
	action = False
	rowsNew = []

	if isSwitchActive('Minus'):
		action = True


		for r in rows:
			if minusResults(r['path']):
				rowsNew.append(r)
	## END Minus

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows


def displayLineInclude(rows):
	action = False
	rowsNew = []

	if isSwitchActive('InPath'):
		action = True
		
		for r in rows:
			if positiveResults(r['path']):
				rowsNew.append(r)
	## END InPath

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows

def displayLineIncludePlus(rows):
	action = False
	rowsNew = []

	if isSwitchActive('PlusOr'):
		action = True
		
		for r in rows:
			if positiveResultsPlusOr(r['path']):
				rowsNew.append(r)
	## END InPath

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows


def ci(string): 
	#switchValueClean
	string = string.replace(';;',',')
	string = string.replace(';p;','%')
	string = string.replace(';q;','"')
	string = string.replace(';.',':')
	string = string.replace(";'",'"')
	string = string.replace('_;192A;_',',')
	string = string.replace('_;192B;_',':')
	string = string.replace(_v.slash+'n','\n')
	string = string.replace(';n','\n')
	string = string.replace(';t','\t')
	string = string.replace('"\'"',"'")
	string = string.replace('"\'", "\'"',"','")
	string = string.replace(';return','\n')
	string = string.replace(';-','-')
	string = string.replace('[star]','*')
	string = string.replace('[a]','*')

	string = string.replace('[pipe]','|')

	string = string.replace('null00','"",')

	return string

##############################################






def displayLineFolder(rows):
	action = False
	rowsNew = []

	if isSwitchActive('Folder'):
		
		action = True
		do = getSwitchValue('Folder').split(',')
		for r in rows:
			show = False
			val = r['path']
			for d in do:
				if d.upper() in val.upper():
					show = True
			if show:
				rowsNew.append(r)
	## END Folder

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows

def displayLineAgo(rows):
	action = False
	rowsNew = []
	if isSwitchActive('Ago'):
		do = getSwitchValue('Ago')
		if len( do ):
			action = True
			do = do.lower()
			md = True
			# print(do)
			# sys.exit()
			if ',' in do:
				d = do.lower().split(',')
				do = d[0]
				if 'cd' in d:
					# print( 'cd' )
					md = False
			fnd = 'ymwd'
			nmb = do
			for t in fnd:
				nmb = nmb.replace(t,'')
			if len(nmb) == 0:
				nmb = 1
			try:
				nmb = int(nmb)
			except Exception as e:
				nmb = 1
			if 'y' in do:
				start_date = datetime.date.today() + datetime.timedelta(-365 * nmb)
			if 'm' in do:
				start_date = datetime.date.today() + datetime.timedelta(-30 * nmb)
			if 'w' in do:
				start_date = datetime.date.today() + datetime.timedelta(-7 * nmb)
			if 'd' in do:
				start_date = datetime.date.today() + datetime.timedelta(-1 * nmb)

			for r in rows:
				# print(datetime.date.fromtimestamp(int(r['date_modified_raw']) / 1e3))
				# print(datetime.date.fromtimestamp(int(r['date_modified_raw']) ), start_date)
				if md:
					if datetime.date.fromtimestamp(int(r['date_modified_raw']) ) > start_date:
						rowsNew.append(r)
				else:
					if datetime.date.fromtimestamp(int(r['date_created_raw']) ) > start_date:
						# print( 'cd confirm' )
						rowsNew.append(r)

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows
def displayLineSize(rows):
	action = False
	rowsNew = []

	if isSwitchActive('Size'):
		action = True
		# print(getSwitchValue('Size'))
		do = getSwitchValue('Size').split(',')[0]
		first = unFormatSize(getSwitchValue('Size').split(',')[1])
		if do == 'b' or do == 'B':
			second = unFormatSize(getSwitchValue('Size').split(',')[2])
		for r in rows:
			val = int(r['bytes'])
			show = False
			if do == 'g' or do == 'G':
				if val > first:
					show = True
			if do == 'l' or do == 'L':
				if val < first:
					show = True
			if do == 'b' or do == 'B':
				if val > first and val < second:
					show = True
			if show:
				# print('test')
				rowsNew.append(r)
	## END SIZE

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows

def dirPrintColumn(folder,column):
	global errors
	global dirRows
	global Loop_ActionCnt
	global lastGroup
	global groupByList
	global columnHeaderLength
	global columnList
	global pipeResults
	global totalsizeCalc
	global totalCountItems
	global totalLINE
	global columnTab
	global _dirCache
	global _dirCache_p

	global databaseFile


	if isSwitchActive('GroupBy'):
		if getSwitchValue('GroupBy') == 'none':
			updateSwitchField('GroupBy','active',False)
	groupBy = getSwitchValue('GroupBy')
	columnList = column
	groupByList = {}
	for gb in groupBy.split(','):
		gb = columnNickname2(gb)
		groupByList[str(gb)] = ''

	lastGroup = ''


	if Loop_ActionCnt == 0:
		if type(pipeResults) == list:
			rows = buildResultFromPipe()
			if not isSwitchActive('NoSave'):
				dirCacheSave(rows,_dirCache_p)
			# print('test')
			# rows = buildResultFromPipe()
			# rows = buildResult(0,folder)
		else:
			if not isSwitchActive('Cache'):
				rows = buildResult(0,folder)
			elif os.path.isfile(_dirCache):
				rows = dirCacheGet()
			else:
				rows = buildResult(0,folder)
		if not isSwitchActive('NoSave'):
			dirCacheSave(rows,_dirCache)
		if isSwitchActive('Save'):
			if getSwitchValue('Save') == 'none' or getSwitchValue('Save') == '' or getSwitchValue('Save') == None:
				pass
			else:
				dirCacheSave(rows,getSwitchValue('Save'))
				os.system('attrib -h '+ getSwitchValue('Save'))
	else:
		rows = dirRows

	rows = displayLine(rows)
	if isSwitchActive('Save2'):
		if getSwitchValue('Save2') == 'none' or getSwitchValue('Save2') == '' or getSwitchValue('Save2') == None:
			pass
		else:
			dirCacheSave(rows,getSwitchValue('Save2'))
			os.system('attrib -h '+ getSwitchValue('Save2'))
	if len(rows) < 1:
		if isSwitchActive('Database'):
			print('Saved to database', databaseFile)
			if isSwitchActive('AppTime'):
				global appStarted 
				print()
				print()
				diff = time.time() - appStarted
				print('app time:',round( diff, 2 ))
		else:
			print('No Files')
		os._exit(0)

	if not isSwitchActive('isFile'):
		if isSwitchActive('Sort'):
			rows = sortThis(rows, False)
		elif isSwitchActive('GroupBy'):
			rows = sortThis(rows, getSwitchValue('GroupBy') + ', Desc:date_modified')
		else:
			if isSwitchActive('Recursion'):
				rows = sortThis(rows, 'Asc:type, Asc:folder, Asc:ext, Asc:name')
			else:
				rows = sortThis(rows, 'Asc:type, Asc:ext, Asc:name')
		i = 0
		if not type(pipeResults) == list:
			if not isSwitchActive('CSV') and not isSwitchActive('Cache') and False:
				printBold(showPreHeader(rows))
		if not isSwitchActive('CSV'):
			columnHeader = showColumnHeader(True,rows,column)
		else:
			columnHeader = showColumnHeaderCSV(True,rows,column)
			columnHeader = columnHeader[:-1]
		columnHeaderLength = len(columnHeader)
		printBold(columnHeader)
		titles = []
		for item in rows:
			result = ''    
			for c in column.split(','):
				c = columnNickname2(c)
				try:
					if not isSwitchActive('CSV'):
						result += showColumn(True,rows,c,i) + columnTab
					else:
						result += showColumnCSV(True,rows,c,i) + ','
				except Exception as e:
					errors.append({'id': 12, 'function': 'dirPrintColumn()', 'cnt': 1, 'location': "result += showColumn(True,rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': folder}, {'name': 'column', 'value': column}], 'error': e})
					print('Error:')
					print('\tBad column input.')
					print(c)
					print(12)
					os._exit(0)
			if isSwitchActive('CSV'):
				result = result[:-1]
			if isSwitchActive('MovieTitle'):
				global movieList
				global movieListX
				import movieTitle
				movieTitle.focus()
				movieTitle.pipeData = []
				if isSwitchActive('MovieFile'):
					movieTitle.pipeData.append(item)
				else:
					movieTitle.pipeData.append(result)
				# print()
				# print( item )
				movieTitle.fieldSet('JustVar','active',True)
				movieTitle.action()
				movieList.append(movieTitle.theTitle)
				# if not movieTitle.theTitle in titles:
				#     titles.append( movieTitle.theTitle )
				movieListX.append({ 'label': movieTitle.theTitle, 'data': item })
			else:
				colorizeRow(result)
			i += 1
	# try:
	#     print('\n',totalLINE)
	#     # print('\n\t','Total Size:',formatSize(totalSize(rows)))
	#     # print('\t','Total Count:',len(rows))
	#     print('\n\t',len(rows),'files',formatSize(totalSize(rows)))
	# except Exception as e:
	#     pass
	if not isSwitchActive('CSV') and not isSwitchActive('NoCount'):
		printBold('\n\t '+str(len(rows))+' files ' + formatSize(totalSize(rows)), 'green')

def totalSize(rows):
	total = 0
	for r in rows:
		total += r['bytes']
	return total

def listPrintColumn(rows,column):
	global errors
	global columnTab
	global printAltName
	printAltName=False

	column = cleanLastChar(column,',')
	column = column.replace(' ','')
	i = 0
	columnHeader = ''
	printBold(showColumnHeader(False,rows,column))
	for item in rows:
		result = ''        
		for c in column.split(','):
			try:
				result += showColumn(False,rows,c,i) + columnTab
			except Exception as e:
				errors.append({'id': 14, 'function': 'dirPrintColumn()', 'cnt': 1, 'location': "result += showColumn(False,rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': folder}, {'name': 'column', 'value': column}], 'error': e})
				printBold('Error:','red')
				printBold('\tBad column input.')
				print(c)
				os._exit(0)
		colorizeRow(result)
		i += 1

def replaceAll(string,rWhat,rWith):
	done=False
	tmp = '{C9DCAA81-3B8A-68E9-E4CF-A405E2199CB9}'
	while not done:
		if string.count(rWhat) > 0:
			string = string.replace(rWhat,tmp)
		else:
			done=True

	done=False
	while not done:
		if string.count(tmp) > 0:
			string = string.replace(tmp,rWith)
		else:
			done=True

	return string
def removeAll(string,rWhat):
	string = replaceAll(string,rWhat,'')
	string = string.replace(rWhat,'')
	return string
def cleanAll(string,rWhat,rWith):
	done=False
	while not done:
		if string.count(rWhat) > 0:
			string = string.replace(rWhat,rWith)
		else:
			done=True
	return string
def formatFolderName(text):
	return '*[ ' + text + ' ]'
#################################################################



#################################################################

def updateSwitchField(name,column,value):
	global switch
	if column == 'value':
		if doesFieldExist(name,'script_trigger'):
			script = '{}(\'{}\',\'{}\')'.format(getSwitchField(name,'script_trigger'),name,value)
			value = eval(script)
	i = 0
	for row in switch:
		if row['name'] == name:
			switch[i][column] = value
		i += 1
	return ''
def getSwitchField(name,column):
	global switch
	result = ''
	for row in switch:
		if row['name'] == name:
			result = row[column]
	return result
def doesFieldExist(name,column):
	global switch
	try:
		for row in switch:
			if row['name'] == name:
				row[column]
				result = True
	except Exception as e:
		result = False
	return result
def isSwitchActive(name):
	return getSwitchField(name,'active')
def getSwitchValue(name):
	result = getSwitchField(name,'value')
	if result is None:
		result = ''
	return result
def checkIfSwitch(string):
	global switch
	result = False
	for a in switch:
		for b in a['switch'].split(','):
			if b == string:
				result = True
				# print(b,result)
	return result
def getSwitchValue2(name):
	global errors
	global switchInput
	try:
		switchInput[getSwitchField(name,'pos') + 1]
		i = 0
		
		try:
			result = switchInput[getSwitchField(name,'pos')].split(':')[1]
		except Exception as e:
			# errors.append({'id': 14, 'function': 'getSwitchValue()', 'cnt': 2, 'location': "result = switchInput[getSwitchField(name,'pos')].split(':')[1]", 'vars': [{'name': 'name', 'value': name}], 'error': e})
			result = ''

		for a in switchInput:
			if i > getSwitchField(name,'pos'):
				if checkIfSwitch(switchInput[i]):
					break
				result += str(switchInput[i]) + ','
			i += 1
		result = result[:-1]
		result = cleanAll(result,':,',':')
		result = cleanAll(result,',,',',')

	except Exception as e:
		# errors.append({'id': 15, 'function': 'getSwitchValue()', 'cnt': 1, 'location': "switchInput[getSwitchField(name,'pos') + 1]", 'vars': [{'name': 'name', 'value': name}], 'error': e})
		result = None

	return result
def processSwitches(switchInput):
	global switch
	ii = 0
	for sw in switch:
		switch[ii]['pos'] = None
		switch[ii]['active'] = False
		switch[ii]['value'] = None
		ii += 1
	i = 0
	for a in switchInput:
		a = a.replace(':','')
		ii = 0
		for sw in switch:
			# print(sw['name'])
			for s in sw['switch'].split(','):
				# print(s)
				if s.lower() == a.lower():
					switch[ii]['pos'] = i
					switch[ii]['active'] = True
					switch[ii]['value'] = processSwitchFormatting(switch[ii]['name'])
			ii += 1
		i += 1
def processSwitchFormatting(name):
	value = getSwitchValue2(name)
	if doesFieldExist(name,'script_trigger'):
		script = '{}(\'{}\',\'{}\')'.format(getSwitchField(name,'script_trigger'),name,value)
		value = eval(script)
	return value
def printSwitches():
	global switch
	for s in switch:
		if s['active']:
			print('---------------')
			print('Name: ' + s['name'])
			print('Pos: ' + str(s['pos']))
			print('Value: ' + str(getSwitchValue(s['name'])))
			print('\n')

def sortThis(rows, name):
	global errors
	if not name == False:
		updateSwitchField('Sort','value',name)
	name = getSwitchValue('Sort')
	

	global columnList_test
	# print(columnList_test)
	# print(name)

	# print(name)
	# print('1: ' + getSwitchValue('Sort'))
	# print('2: ' + getSwitchField('Sort','value'))
	# print('3: ' + name)
	sortBy = {}
	sortList = name.split(',')
	sortList.reverse()

	### Check for bad sort input
	for item in sortList:
		item = item
		try:
			if item.count(':') > 0:
				sb = item.split(':')[1]
			else:
				sb = item
			# rows[0][sb]
		except Exception as e:
			errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			# print('Error:')
			# print('\tBad sort input.')
			# print(item)
			# print(16)
			# os._exit(0)


	for item in sortList:
		try:
			direction = item.split(':')[0]
			sb = item.split(':')[1]
			if direction == 'asc':
			# if direction.find('a') == 0:
				rows = sorted(rows, key=itemgetter(sb))
			else:
				rows = sorted(rows, key=itemgetter(sb), reverse=True)
		except Exception as e:
			try:
				pass
				rows = sorted(rows, key=itemgetter(item))
			except Exception as e:
				errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			

		sortBy[item] = str(uuid.uuid4())
		i = 0
		for row in rows:
			rows[i][sortBy[item]] = i
			i += 1

	# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

	sortCode = 'rows = sorted(rows, key=lambda d: ('
	for item in sortList:
		sortCode += "d['" + str(sortBy[item]) + "'],"
	sortCode = sortCode[:-1]
	sortCode += '))'
	# print(sortCode)
	exec(sortCode)
	return rows

def countThis(rows):
	i = 0
	for x in rows:
		i += 1
	return i
def cleanLastChar(string,rWhat):
	string = str(string)
	rWhat = str(rWhat)
	cleanAll(string,rWhat+rWhat,rWhat)
	string +=  '**'
	string = string.replace(rWhat + '**', '')
	string = string.replace('**', '')
	return string
def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y-%m-%d %H:%M:%S')
	theDate = str(theDate)
	return theDate
def formatDateYear(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y')
	# theDate = str(theDate)
	return theDate
def formatDateDay(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%d')
	# theDate = str(theDate)
	return theDate
def formatDateMonth(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%m')
	theDate = str(theDate)
	return theDate
def timeout(start,t):
	# os._exit(0)
	# print('loop')
	global completed
	global killTime
	global timeoutKill
	ts = dt.now()

	if start == 'start':
		timeoutKill = False
		completed = False
		killTime = ts + timedelta(seconds=int(t))

	if not completed and ts < killTime:
		x = Timer(0.0, timeout, ('loop',t))
		x.start()
	elif not completed:
		timeoutKill = True
		completed = True
		print('\n*** Timeout ***()')
		# os._exit(0)

	# print(completed)
def formatSwitchValueHelperA(name,column,typ):
	result = ' '
	column = column.lower()
	column = replaceAll(column,' ','')
	column = replaceAll(column,',,',',')
	for c in column.split(','):
		if c.count(':') > 0:
			if c.split(':')[0].count('a') > 0:
				result += ' asc:'
			else:
				result += ' desc:'

			if typ == 1:
				sb = columnNickname1(c.split(':')[1])
			else:
				sb = columnNickname2(c.split(':')[1])
			result += sb + ' , '
		else:
			if typ == 1:
				sb = columnNickname1(c)
			else:
				sb = columnNickname2(c)
			result += sb + ' , '
	# print(columnList)
	return result
def formatSwitchValueHelperB(result):
	result = replaceAll(result,' ','')
	result = replaceAll(result,',,',',')
	result = cleanLastChar(result,',')
	# ####################################################################  delim to array
	return result
def formatSwitchValueHelperC(column,typ):
	i = 0
	columnList = []
	for c in column.split(','):
		if c.count(':') > 0:
			if c.split(':')[0].count('a') > 0:
				direction = 'asc'
			else:
				direction = 'desc'
			if typ == 1:
				sb = columnNickname1(c.split(':')[1])
			else:
				sb = columnNickname2(c.split(':')[1])
		else:
			direction = 'asc'
			if typ == 1:
				sb = columnNickname1(c)
			else:
				sb = columnNickname2(c)
		if typ == 1:
			columnList.append({'direction': direction, 'column': sb})
		else:
			columnList.append({'column': sb})        
		i += 1
	return columnList
def formatSwitchValueColumn(name,column):
	# script_trigger
	result = formatSwitchValueHelperA(name,column,2)
	result = formatSwitchValueHelperB(result)
	# formatSwitchValueHelperC(column,2)

	# column = 'day_of_the_week'
	return result
def formatSwitchValueSort(name,column):
	global columnList_test
	# script_trigger
	result = formatSwitchValueHelperA(name,column,1)
	result = result.replace(' friendly_week ','desc:date_modified_raw')
	result = result.replace(' friendly_month ','desc:date_modified_raw')
	result = result.replace(' day_of_the_week ','desc:date_modified_raw')
	result = formatSwitchValueHelperB(result)
	columnList_test = formatSwitchValueHelperC(column,1)
	# column = 'day_of_the_week'
	return result

def columnNickname1(column):
	# Sort
	try:
		column = columnNickname2(column)
		column = column.replace('size','bytes')
		if column == 'type':
			column = 'typesort'

		if column == 'date_created':
			column = 'date_created_raw'

		if column == 'date_modified':
			column = 'date_modified_raw'

		if column == 'friendly_week':
			column = 'date_modified_raw'

		if column == 'friendly_month':
			column = 'date_modified_raw'

		if column == 'week_of_year_':
			column = 'date_modified_raw'

		if column == 'week_of_year':
			column = 'date_modified_raw'

	except Exception as e:
		column = 'date_modified_raw'
	
	return column
def columnNickname2(column):
	global printAltName
	if isSwitchActive('GroupBy'):
		if getSwitchValue('GroupBy') == 'none':
			updateSwitchField('GroupBy','active',False)

	try:
		column = column.lower()
		column = replaceAll(column,' ','')
		if (isSwitchActive('GroupBy') and not isSwitchActive('LongFileName')) or isSwitchActive('ShortFileName'):
			if column == 'name' and printAltName:
				column = 'name_'

		if column == 'cd' or column == 'dc' or column == 'datec' or column == 'cdate':
			column = 'date_created'
		if column == 'md' or column == 'dm' or column == 'datem' or column == 'mdate':
			column = 'date_modified'
		if column == 'dow' or column == 'dotw' or column == 'd':
			column = 'day_of_the_week'
		if column == 'woy' or column == 'w':
			column = 'week_of_year'
		if column == 'woy2' or column == 'w2':
			column = 'week_of_year_'
		if column == 's':
			column = 'size'
		if column == 't':
			column = 'type'
		if column == 'p':
			column = 'path'
		if column == 'e':
			column = 'ext'
		if column == 'n':
			column = 'name'
		if column == 'b':
			column = 'bytes'
		if column == 'a':
			column = 'attrib'
		if column == 'm':
			column = 'month'
		if column == 'fw':
			column = 'friendly_week'
		if column == 'fm':
			column = 'friendly_month'
		if column == 'f':
			column = 'folder'

	except Exception as e:
		pass
		column = 'date_modified_raw'
	
	return column

#################################################################
#################################################################
def getMovieExt():
	result = ''
	tf = _v.myTables + _v.slash+'movieExt.txt'
	movieExt = getText( tf )
	if not type( movieExt ) == bool:
		for me in movieExt:
			me = me.replace( '\n', '' )
			me = me.replace( ' ', '' )
			if len( me ) > 1 and  len( me ) <= 5:
				result += '*.'+me + ','
		result += '3FD74EAB82D5'
		result = result.replace( ',3FD74EAB82D5', '')
		result = result.replace( '3FD74EAB82D5', '')
	return result


def getText(theFile):
	lines = False
	if os.path.isfile(theFile):
		try:
			f = open(theFile, 'r', encoding='utf-8')
			lines = f.readlines()
			f.close()
		except Exception as e:
			try:
				f = open(theFile, 'r', encoding='latin-1')
				lines = f.readlines()
				f.close()
			except Exception as e:
				f = open(theFile, 'r')
				lines = f.readlines()
				f.close()

	return lines
#################################################################
#################################################################

def takeAction():
	global errors
	global defaultTimeout
	global folder
	global completed
	global timeoutKill
	global Loop_ActionCnt
	global switchInput
	global switchInputRaw
	global pipeResults
	global idResolution
	
	global cursor
	global cursor2
	global conn
	global conn2
	global databaseFile






	###################
	
	try:
		folder
	except Exception as e:
		folder = os.getcwd()
	try:
		if os.path.isdir(sys.argv[1]):
			folder = sys.argv[1]
	except Exception as e:
		# errors.append({'id': 13, 'function': 'formatFolderName()', 'cnt': 1, 'location': 'folder = sys.argv[1]', 'vars': [{'name': 'text', 'value': text}], 'error': e})
		folder = os.getcwd()
	###################
	if Loop_ActionCnt == 0:
		switchInput = sys.argv
	else:
		switchInputRaw = cleanAll(switchInputRaw,',',' ')
		switchInputRaw = cleanAll(switchInputRaw,'  ',' ')
		switchInput = switchInputRaw.split(' ')

	# print(switchInput)
	try:
		# print(switchInputRaw)
		pass
	except Exception as e:
		pass
	processSwitches(switchInput)

	# printSwitches()
	global defaultCachFile
	if os.path.isfile( defaultCachFile ):
		olc_m = os.path.getmtime( defaultCachFile )
		olc_d = time.time() - olc_m
		if ( olc_d/60 ) < 5 and not isSwitchActive('SkipAgeCheck'):
			updateSwitchField( 'Cache', 'active', True )
			updateSwitchField( 'Cache', 'value', defaultCachFile )
		# global switch
		# for sw in switch:
		#     if sw['active']:
		#         print( sw['name'], sw['value'] )
		# sys.exit()

	if not isSwitchActive('Column') and not isSwitchActive('Sort') and not isSwitchActive('GroupBy') and not isSwitchActive('Report') and not isSwitchActive('ReportDate') and not isSwitchActive('ReportDatePath') and not isSwitchActive('CSV') and not isSwitchActive('Convert') and not isSwitchActive('Timestamp') and not isSwitchActive('Bookmark') and not isSwitchActive('ResolveIDs') and not isSwitchActive('NoCount') and not isSwitchActive('Database') and not isSwitchActive('MD5') and not isSwitchActive('Movies') and not isSwitchActive('MovieFile') and not isSwitchActive('MovieTitle') and not isSwitchActive('MovieScore') and not isSwitchActive('MovieFranchise') and not isSwitchActive('Label') and not isSwitchActive('PrintNewMoviePath') and not isSwitchActive('PrintMovieFilePath'):
		# p dir3 -c woy ext md n -g woy ext
		print()
		updateSwitchField('Column','active',True)
		updateSwitchField('GroupBy','active',True)
		updateSwitchField('Sort','active',True)

		updateSwitchField('Sort','value','ext,desc:md')
		updateSwitchField('Column','value','ext,woy,md,n,size')
		updateSwitchField('GroupBy','value','ext,woy')

	if isSwitchActive('Movies'):
		updateSwitchField('NoCount','active',True)
		updateSwitchField('Minus','active',True)
		updateSwitchField('Minus','value','.srt,.jpg,.jpg,.sub,.idx,.nfo,downloaded,HOME MOVIES')
		me = getMovieExt()
		# print( me )
		if True and '*' in me:
			# addIP = ''
			# if isSwitchActive('InPath'):
			#     addIP += ','
			#     addIP += getSwitchValue('InPath')

			updateSwitchField('PlusOr','active',True)
			# updateSwitchField( 'InPath', 'active', True )
			updateSwitchField( 'PlusOr', 'value', getMovieExt() )

		# updateSwitchField('Minus','value','.srt,.jpg,.jpg,.sub,.idx,.nfo')
		if False and not isSwitchActive('Size'):
			updateSwitchField('Size','active',True)
			# updateSwitchField('Size','value','g,200mb')
			updateSwitchField('Size','value','l,200mb')
		if not isSwitchActive('Column'):
			updateSwitchField('Column','active',True)
			updateSwitchField('Column','value','name')



	if isSwitchActive('Database'):
		if len(getSwitchValue('Database')) > 1:
			databaseFile = getSwitchValue('Database')
		else:
			databaseFile = "defaultDir.db"

		try:
			os.unlink(databaseFile)
		except Exception as e:
			pass

		conn = sqlite3.connect(databaseFile)
		cursor = conn.cursor()         
		cursor.execute("""CREATE TABLE files (path text, name_ text, name text, folder text, stat text, attrib text, bytes int, size text, date_created_raw int, date_modified_raw int, date_created text, date_modified text, type text, typesort text, ext text, week_of_year text, week_of_year_ text, day_of_the_week text, month text, friendly_week text, friendly_month text)""")

		if isSwitchActive('MD5'):
			
			try:
				os.unlink(databaseFile.replace('.db','_MD5.db'))
			except Exception as e:
				pass
			conn2 = sqlite3.connect(databaseFile.replace('.db','_MD5.db'))
			cursor2 = conn2.cursor()         
			cursor2.execute("""CREATE TABLE md5 (md5 text, path text, name text, folder text, bytes int, date_created_raw int, date_modified_raw int )""")


	
	
	###################











	if isSwitchActive('ResolveIDs'):
		idResolution = getTable('idResolution.json')
	if isSwitchActive('Timestamp'):
		print( time.time() )
		# print(int(round(time.time() * 1000)))
		os._exit(0)

	if isSwitchActive('Convert'):
		if getSwitchValue('Convert').split(',')[0] == 'timestamp':
			stamp = int(getSwitchValue('Convert').split(',')[1])
			result = datetime.datetime.fromtimestamp(stamp / 1e3)
			colorizeRow(result)
		else:
			if 'B' in getSwitchValue('Convert') or 'b' in getSwitchValue('Convert'):
				print(unFormatSize(getSwitchValue('Convert')))
			else:
				print(formatSize(int(getSwitchValue('Convert'))))
		os._exit(0)


	if isSwitchActive('Timeout'):
		try:
			defaultTimeout = int(getSwitchValue('Timeout'))
		except Exception as e:
			errors.append({'id': 18, 'function': 'parent', 'cnt': 1, 'location': "defaultTimeout = int(getSwitchValue('Timeout'))", 'vars': [{'name': 'timeout', 'value': getSwitchValue('Timeout')}], 'error': e})
			print('Error:')
			print('\tBad timeout value.')
			os._exit(0)
		x = Timer(0.0, timeout, ('start',defaultTimeout))
		x.start()

	# print(defaultTimeout)

	# groupBy = getSwitchValue('GroupBy')
	# groupBy = columnNickname2(groupBy)
	if isSwitchActive('GroupBy'):
		if getSwitchValue('GroupBy') == 'none':
			updateSwitchField('GroupBy','active',False)
	if isSwitchActive('GroupBy') and not isSwitchActive('Column'):
		updateSwitchField('GroupBy','groupByDefault',True)

	# if isSwitchActive('GroupBy'):
	#     if isSwitchActive('Column'):
	#         groupByDefault = False
	#     elif isSwitchActive('GroupBy'):
	#         groupByDefault = True
	#     else:
	#         groupByDefault = False
	# else:
	#     groupByDefault = False
	#     groupBy = ''








	if isSwitchActive('Bookmark') and not isSwitchActive('Column'):
		updateSwitchField('Column','active',True)
		# updateSwitchField('Column','value','cd, md, bookmark, bm_status,bm_path')
		# updateSwitchField('Column','value','md, bookmark, bm_status,bm_path')
		updateSwitchField('Column','value','date_created_, date_modified_, bookmark, bm_status,bm_path')
		if not isSwitchActive('Sort'):
			updateSwitchField('Sort','active',True)
			updateSwitchField('Sort','value','desc:md')

	if isSwitchActive('Report') and (getSwitchValue('Report') == 'date2' ): # or getSwitchValue('Report') == 'd'
		# -g  -c n fm fw d md -s d:md
		updateSwitchField('GroupBy','active',True)
		updateSwitchField('GroupBy','value','fm, woy2, d')
		# updateSwitchField('GroupBy','value','fm, fw, d')
		updateSwitchField('Column','active',True)
		updateSwitchField('Column','value','n,fm, woy2, d, md')
		# updateSwitchField('Column','value','n,fm, fw, d, md')
		updateSwitchField('Sort','active',True)
		updateSwitchField('Sort','value','d:md')

	if isSwitchActive('Report') and (getSwitchValue('Report') == 'date' ): # or getSwitchValue('Report') == 'd'
		# -g  -c n fm fw d md -s d:md
		updateSwitchField('GroupBy','active',True)
		# updateSwitchField('GroupBy','value','fm, woy2, d')
		updateSwitchField('GroupBy','value','fm, fw, d')
		updateSwitchField('Column','active',True)
		# updateSwitchField('Column','value','n,fm, woy2, d, md')
		updateSwitchField('Column','value','n,fm, fw, d, md')
		updateSwitchField('Sort','active',True)
		updateSwitchField('Sort','value','d:md')

	if isSwitchActive('ReportDate') or isSwitchActive('Report') and (getSwitchValue('Report') == 'date3' or getSwitchValue('Report') == 'd'):
		# -g  -c n fm fw d md -s d:md
		# updateSwitchField('LongFileName','active',True)
		updateSwitchField('GroupBy','active',True)
		# updateSwitchField('GroupBy','value','fm, woy2, d')
		updateSwitchField('GroupBy','value','fm, fw, d')
		updateSwitchField('Column','active',True)
		# updateSwitchField('Column','value','n,fm, woy2, d, md')
		updateSwitchField('Column','value','n,fm, fw, d, md')
		updateSwitchField('Sort','active',True)
		if getSwitchValue('ReportDate') == 'cd':
			updateSwitchField('Sort','value','asc:cd')
		else:
			updateSwitchField('Sort','value','asc:md')
	if isSwitchActive('ReportDatePath'):
		updateSwitchField('GroupBy','active',True)
		updateSwitchField('GroupBy','value','fm, fw, d')
		updateSwitchField('Column','active',True)
		updateSwitchField('Sort','active',True)

		updateSwitchField('Sort','value','asc:md')
		updateSwitchField('Column','value','n,f,fm, fw, d, md')

		# if getSwitchValue('ReportDatePath') == 'cd':
		#     updateSwitchField('Sort','value','asc:cd')
		#     updateSwitchField('Column','value','n,f,fm, fw, d, cd')
		# else:
		#     updateSwitchField('Sort','value','asc:md')
		#     updateSwitchField('Column','value','n,f,fm, fw, d, md')

	if isSwitchActive('Help'):
		print(inlineBold('Description:')+' \tDisplays directory information.\n')
		printBold('Example:\n\tp dir -Column: size, name -Sort: Asc:type, Asc:ext, Asc:name -Errors: hide:8,11 -FolderSize -Timeout: 10 -NoExit')
		colorizeRow('\n\tp dir -c name, week_of_year -s week_of_year -g week_of_year',2)
		colorizeRow('\n\tp dir -c name, ext -s ext -g ext',2)
		colorizeRow('\n\tp dir -g fm fw d -s desc:dm',2)
		colorizeRow('\n\tp dir -cache %mData% -size g 3gb -c p | p line --c + y: | p line --c -p \ ee | p line --c -p \ e 2 -pc',2)
		colorizeRow('\n\tp dir -cache %mData% -c p  + star trek -size g 1gb',2)
		colorizeRow('\n\tp f -bm + tmp -n | p dir -b',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\ttype 01{F8E01519-3977-04B8-3416-1F0048BD97C3} | p dir -db C_Drive.db -md5',2)
		colorizeRow('\n\ttype 01{65E57A88-6471-E426-D878-AD55F117A804} | p dir -db D_Drive.db -md5',2)
		colorizeRow('\n\tp dir + .db - old',2)
		colorizeRow('\n\tp dirdbmd5 -db C_Drive_MD5.db',2)
		colorizeRow('\n\tp dirdb -db C_Drive.db',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\tp dir -cache %mData% -movies -ago 2w -movietitle ',2)
		colorizeRow('\n\tp dir -cache %mData% -movies + 2018 -movietitle ',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -score -movies + 2018  ',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -score -movies -ago 2w  ',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -movies + traveling',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -movies -franchise marvel ',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -movies -franchise "jane austen" ',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -movies -franchise hallmark ',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -movies -path | sort',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\tp dir -cache %mData% -movies -ago 2w -movietitle | p line --c -make "p imdb -score -qi -ent {}" | p execute --c | sort | p line',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\tp dir -save pcr.dirCache',2)
		colorizeRow('\n\tp dir -cache pcr.dirCache + *.json -c s n -s s',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -movies -label',2)
		colorizeRow('\n\tp dir -cache %mcData% -movietitle -movies -label',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\t',2)
		colorizeRow('\tp dir -cache %mData% -movietitle -movies -label  > %tmpf1%',2)
		colorizeRow('\tp dir -cache %mcData% -movietitle -movies -label  > %tmpf2%',2)
		colorizeRow('\tp crossRef -1 %tmpf1% -2 %tmpf2%',2)
		colorizeRow('\n\t',2)
		colorizeRow('\tp dir -cache %mData% -movietitle -movies -label -mfile  | sort > %tmpf1%',2)
		colorizeRow('\tp dir -cache %mcData% -movietitle -movies -label -mfile  | sort > %tmpf2%',2)
		colorizeRow('\tp crossRefMovies -1 %tmpf1% -2 %tmpf2% -report',2)
		colorizeRow('\n\t',2)
		printBold('\t_______________________________________________','red')
		printBold('\n\t update drive data:')
		colorizeRow('\t\t\t\t movieData',2)
		colorizeRow('\t\t\t\t mData',2)
		colorizeRow('',2)
		colorizeRow('\t\t\t\t movieCloudData',2)
		colorizeRow('\t\t\t\t mcData',2)
		colorizeRow('\t\t\t\t m3Data',2)
		printBold('\t_______________________________________________','red')
		colorizeRow('\n\t genDirDB',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -movies -franchise all + batman',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -movies -franchise marvel',2)
		colorizeRow('\n\t',2)
		colorizeRow('\n\tp dir -cache %mData% -movietitle -movies -franchise all save',2)
		colorizeRow('\n\t',2)
		print('\n\t'+inlineBold(' p dir -cache %mData% -movietitle -movies -franchise marvel ','red'))
		colorizeRow('\n\t p dir -cache %m3Data% -movietitle -movies -franchise marvel ',2)
		# colorizeRow('\nColumns:\n\tname, path, size, type, ext, date_created, date_modified, stat, attrib',2)
		printBold('\n\nColumns:\n\tname path size type ext date_created date_modified stat attrib week_of_year')
		print('\n-----------------------------------------------\n'+inlineBold('List of switches:')+'\n')
		listPrintColumn(switch,'name,switch,expected_input_example')
		# for s in switch:
		#     print('{}: {}'.format(s['name'],s['switch']))
	elif isSwitchActive('Debug'):
		printSwitches()
		print(isSwitchActive('ShortFileName'))
	elif isSwitchActive('Test'): 
		cnt = folderSizeX(folder)
		print(cnt)
		print(formatSize(cnt))
	elif isSwitchActive('Column'):
		if getSwitchValue('Column') == None:
			print('dir -c size, name')
			print('\nColumns:\n\tname path size type ext date_created date_modified stat attrib week_of_year')
		else:
			dirPrintColumn(folder,getSwitchValue('Column'))
			if isSwitchActive('MovieTitle'):
				# printSwitches()
				# sys.exit()
				shouldRun = True
				global movieList
				global movieListX
				# print( movieList )
				# sys.exit()
				if not isSwitchActive('MovieFile'):
					movieList = set(movieList)
				if isSwitchActive('MovieFranchise'):
					if getSwitchValue('MovieFranchise') == '':
						updateSwitchField( 'MovieFranchise', 'value', 'all' )
					if getSwitchValue('MovieFranchise') == 'save':
						updateSwitchField( 'MovieFranchise', 'value', 'all save' )
				if isSwitchActive('MovieScore') or isSwitchActive('Label') or isSwitchActive('MovieFranchise') or isSwitchActive('PrintNewMoviePath'):
					import imdb
					if isSwitchActive('NoColor'):
						imdb.fieldSet('NoColor','active',True)
					if isSwitchActive('PrintNewMoviePath'):
						# print( 'HERE' )
						# sys.exit()
						imdb.fieldSet('PrintPath','active',True)
					if isSwitchActive('PrintMovieFilePath'):
						imdb.fieldSet('PrintOldPath','active',True)
						# to be used later

					imdb.focus()
					imdb.fieldSet('Case','active',True)
					imdb.fieldSet('Movie','active',True)
# 
					if isSwitchActive('MovieScore'):
						imdb.fieldSet('Score','active',True)
					if isSwitchActive('Label'):
						imdb.fieldSet('Label','active',True)
					if isSwitchActive('MovieFile'):
						imdb.fieldSet('MovieFile','active',True)
					if isSwitchActive('MovieFranchise'):
						imdb.fieldSet('MovieFranchise','active',True)
						imdb.fieldSet('MovieFranchise','value', getSwitchValue('MovieFranchise'))
						imdb.fieldSet('MovieFranchise','dir',True)

					if isSwitchActive('Cache'):
						if getSwitchValue('Cache') == 'D:\\tech\\hosts\\MSI\\indexes\\Movie_Drive.dirCache':
							imdb.fieldSet( 'Location', 'active', True )
							imdb.fieldSet( 'Location', 'value', 'Movie_Drive' )
						if getSwitchValue('Cache') == 'D:\\tech\\hosts\\MSI\\indexes\\Movies_Cloud.dirCache':
							imdb.fieldSet( 'Location', 'active', True )
							imdb.fieldSet( 'Location', 'value', 'Movies_Cloud' )

					# print( )
					if len( getSwitchValue('MovieFranchise') ):
					# if 'id' in getSwitchValue('MovieFranchise') or 'all' in getSwitchValue('MovieFranchise'):
						# shouldRun = True
						# printFranchiseTable
						franchise_file_data = getTable( 'franchise_file_data.json' )
						franchiseData = []
						inList = []
						if ( 'id' in getSwitchValue('MovieFranchise') or 'all' in getSwitchValue('MovieFranchise')  ):
							for row in movieListX:
								for fran in franchise_file_data:
									if fran['data']['path'] == row['data']['path']:
										# print( row )
										# sys.exit()
										if not row['data']['path'] in inList:
											inList.append( row['data']['path'] )
											franchiseData.append( fran )
						else:
							what = getSwitchValue('MovieFranchise')
							what = what.replace( ',', ' ' )
							what = what.replace( '_', ' ' )
							what = what.replace( ' save', '' )
							for row in movieListX:
								for fran in franchise_file_data:
									if fran['data']['path'] == row['data']['path']:
										# print( row )
										# sys.exit()
										if not row['data']['path'] in inList:

											if what.lower() == fran['first'].lower() or what.lower() == fran['second'].lower():
												inList.append( row['data']['path'] )
												franchiseData.append( fran )

						if len( franchiseData ) == len( movieListX ) or len( franchiseData ) > len( movieListX ) or not 'save' in getSwitchValue('MovieFranchise'):
							shouldRun = False
							imdb.printFranchiseTable( franchiseData )

						if shouldRun:
							imdb.setPipeData(movieListX)
					else:
						imdb.setPipeData(movieList)

					if shouldRun:
						results = imdb.caseTest()

						if 'save' in getSwitchValue('MovieFranchise'):
							saveTable( results, 'franchise_file_data.json' )
				else:
					for thisMLI in movieList:
						print(thisMLI)
	else:
		if isSwitchActive('Recursion') and not isSwitchActive('GroupBy'):
			updateSwitchField('GroupBy','active',True)
			updateSwitchField('GroupBy','groupByDefault',True)
			updateSwitchField('GroupBy','value','folder')
			dirPrintColumn(folder,'size,name,folder')
		else:
			if type(pipeResults) == list and isSwitchActive('GroupBy'):
					dirPrintColumn(folder,'name,' + getSwitchValue('GroupBy'))
			if type(pipeResults) == list and not isSwitchActive('GroupBy'):
				updateSwitchField('GroupBy','active',True)
				updateSwitchField('GroupBy','groupByDefault',True)
				updateSwitchField('GroupBy','value','folder')
				dirPrintColumn(folder,'size,name,folder')
			else:
				if getSwitchField('GroupBy','groupByDefault'):
					dirPrintColumn(folder,'name,' + getSwitchValue('GroupBy'))
				else:
					dirPrintColumn(folder,'size,name')

	completed = True

	if timeoutKill:
		print('\n*** Timeout ***')
		print('\t Folder sizes may be inaccurate')


	if isSwitchActive('Errors'):
		printSwitches()
		# print('*** ' + getSwitchValue('Sort') + ' ***')
		errors = sorted(errors, key=itemgetter('id'))
		print('\n\n-----------------------------------------------\nErrors:\n')
		showHide = getSwitchValue('Errors')
		# showHide = 'hide:8,11'
		if showHide == None:
			showHide = ''
		sh = 'show'
		shList = ''
		try:
			showHide = showHide.lower()
			if len(showHide) > 0:
				if showHide.find(':') == -1:
					sh = 'show'
					shList = showHide
				else:
					sh = showHide.split(':')[0]
					shList = showHide.split(':')[1]
		except Exception as e:
			pass
		if len(shList) > 0:
			print('------------')
			print(sh)
			print(shList)
			print('------------')

		for error in errors:
			if sh == 'show':
				show = False
			else:
				show = True

			if len(shList) == 0:
				show = True


			eId = error['id']
			function = error['function']
			cnt = error['cnt']
			location = error['location']
			e = error['error']
			var = error['vars']
			if len(shList) > 0:
				for f in shList.split(','):
					if int(f) == eId:
						if sh == 'show':
							show = True
						else:
							show = False
			# if not eId == 8 and not eId == 11:
			if show:
				print('\tid: {} function: {} error: {}'.format(eId,function,e))
				for v in var:
					name = v['name']
					value = v['value']
					print('\t\t{}: {}'.format(name,value))


def getTable(theFile,tableTemp = True,printThis = False):
	# defaults to myTables
	if tableTemp:
		file0 = _v.myTables + _v.slash + theFile
	else:
		file0 = _v.stmp + _v.slash + theFile
	if printThis:
		print('Loaded: ' + file0)
	if os.path.isfile(file0):
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
		return json_data

#################################################################
#################################################################
## Timout ##


errors = []
spaces = {}
switch = []
tableProfile = []
dirRows = []
timeoutKill = False
folderDepthMax = 1
defaultTimeout = 60
Loop_ActionCnt = 0
maxFileNameLength = 35
columnTab = ''
columnTab = '   '
_dirCache = _v.myTables + _v.slash+'dirCache.json'
_dirCache_p = _v.myTables + _v.slash+'dirCacheP.json'

# print(_dirCache);
# {'table': 'directory', 'fields': [{}]}

# tableProfile.append()


switch.append({'name': 'Help','switch': '?,/?,-?,/h,help,/help,-help,--help', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Folder','switch': '-f,-folder,+or,-searchor,-so', 'pos': None, 'active': False, 'value': None, 'expected_input_example': 'E:\\tech\\scripts\\python \\tech Y:'})
switch.append({'name': 'InPath','switch': '-inpath,-inand,-searchand,-sa,+', 'pos': None, 'active': False, 'value': None, 'expected_input_example': 'star trek .mkv'})
switch.append({'name': 'Minus','switch': '-minus,-exclude,-', 'pos': None, 'active': False, 'value': None, 'expected_input_example': 'star trek .mkv'})
switch.append({'name': 'PlusOr','switch': '-or', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Column','switch': '-c,-column', 'pos': None, 'active': False, 'value': None, 'expected_input_example': 'size, name', 'script_trigger': 'formatSwitchValueColumn'})
switch.append({'name': 'Sort','switch': '-s,-sort', 'pos': None, 'active': False, 'value': None, 'expected_input_example': 'Asc:type, Desc:ext', 'script_trigger': 'formatSwitchValueSort'})
switch.append({'name': 'Debug','switch': '-d,-debug', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
# switch.append({'name': 'Test','switch': '-tt,-test', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Recursion','switch': '-r,-recursion,-recursive', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'RecursionFolderSize','switch': '-rr,-fs,-rfs,-FolderSize,-RecursionFolderSize', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Hidden','switch': '-h,-hidden', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Errors','switch': '-e,-Error,-Errors', 'pos': None, 'active': False, 'value': None, 'expected_input_example': '8,11 OR hide:8,11'})
switch.append({'name': 'Timeout','switch': '-t,-Timeout', 'pos': None, 'active': False, 'value': None, 'expected_input_example': '5 OR 10 OR 60'})
switch.append({'name': 'NoExit','switch': '-x,-NoExit', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Yr','switch': '-y,-yr,-year,-dont_remove_this_yr', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'GroupBy','switch': '-g,-group,-groupby', 'pos': None, 'active': False, 'value': None,'groupByDefault': False ,'expected_input_example': None, 'script_trigger': 'formatSwitchValueColumn'})
switch.append({'name': 'PipeInput','switch': '-p,-pi,-pipe,-pipeinput', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'LongFileName','switch': '-l,-ln,-LongFileName,-long', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'ShortFileName','switch': '-sn,-ShortFileName', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Report','switch': '-re,-report', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'ReportDate','switch': '-date,-reportdate', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'ReportDatePath','switch': '-datepath', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'isFile','switch': '-isfile', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Cache','switch': '-in,-cache', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Save','switch': '-save', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Save2','switch': '-save2', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'NoSave','switch': '-nosave,-dontsave', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'CSV','switch': '-csv', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Size','switch': '-size', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Convert','switch': '-convert', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Timestamp','switch': '-timestamp', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Bookmark','switch': '-b', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'ResolveIDs','switch': '-idr,-idres,-resolve,-resolveid,-resolveids,', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'NoCount','switch': '--c', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Ago','switch': '-ago', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Database','switch': '-db,-database', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'MD5','switch': '-md5', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})

#################################################################
switch.append({'name': 'Movies','switch': '-movies', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'MovieFile','switch': '-mfile', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})

switch.append({'name': 'MovieTitle','switch': '-movietitle', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})

switch.append({'name': 'MovieScore','switch': '-score', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'MovieFranchise','switch': '-fran,-franchise', 'pos': None, 'active': False, 'value': None, 'expected_input_example': 'Marvel,"Jane Austen"'})

switch.append({'name': 'Label','switch': '-label', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'PrintNewMoviePath','switch': '-path', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'PrintMovieFilePath','switch': '-filepath', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})

#################################################################

#################################################################

# switches to recognise but not do anything because they are for dir3

switch.append({'name': 'Stats', 'switch': '-stats,-stat', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'SkipIsFile', 'switch': '-skip', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Prefix', 'switch': '-prefix', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Dump', 'switch': '-dmp,-dump', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})

switch.append({'name': 'AppTime','switch': '-apptime', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'SkipAgeCheck','switch': '-skipcheck,-force,-update', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'NoColor','switch': '-nocolor', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
#################################################################
#################################################################

movieList = []
movieListX = []

# pipeResults = _getPipe.pipeResults


pipeResults = ''
safaChar = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

if not sys.stdin.isatty():
	pipeResults = sys.stdin.readlines()
	if not pipeResults[0][0] in safaChar:
		pipeResults[0] = pipeResults[0][1:]









# filename = '{80262020-053B-9560-BD50-788984050DC7}'

# def getImport():
#     global filename
#     importedList = []
#     f = open(filename,'r')
#     for line in f:
#         importedList.append(line)
#     f.close()
#     os.remove(filename)
#     return importedList
# if os.path.isfile(filename):
#     pipeResults = getImport()
# if not sys.stdin.isatty() and os.path.isfile(filename):
#     pipeResults = getImport()
# elif not sys.stdin.isatty():
#     pipeResults = sys.stdin.readlines()
#     if pipeResults[0][0].isalnum() == False:
#         pipeResults[0] = pipeResults[0][1:]
#     f = open(filename,'w')
#     for line in pipeResults:
#             f.write(line.replace('\n',''))
#     f.close()
	
# else:
#     pass
#     if os.path.isfile(filename):
#         os.remove(filename)

# print(pipeResults)


# sys.stdin = open('/dev/tty', 'r')
# sys.stdin=open("tmp")
# sys.stdin.flush()

# sys.stdin.seek(0)
# print(pipeResults)
# import importlib
# importlib.reload(sys)
# os._exit(0)
# os._exit(0)
# switchInputRaw = input('\n\n_____________\n\ndo: ')

# result = doesFieldExist('Column','script_trigger')
# print(result)
# result = doesFieldExist('Hidden','script_trigger')
# print(result)
# os._exit(0)
##########################
# switchInput = sys.argv
# processSwitches(switchInput)
# print(unFormatSize(getSwitchValue('Size')))
# os._exit(0)
##########################

def md5Gen(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

appStarted = time.time()
takeAction()
# if __name__ == '__main__':

if isSwitchActive('AppTime'):
	print()
	print()
	diff = time.time() - appStarted
	print('app time:',round( diff, 2 ))


if isSwitchActive('NoExit'):
	Loop_Action = True
	while Loop_Action:
		Loop_ActionCnt += 1
		switchInputRaw = input('\n\n_____________\n\ndo: ')
		if switchInputRaw == 'quit' or switchInputRaw == 'q' or switchInputRaw == 'exit' or switchInputRaw == 'c':
			takeAction()


# isSwitchActive('Help'):


