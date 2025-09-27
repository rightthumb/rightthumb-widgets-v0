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

# import arrow

# DEFAULT_TIMEOUT = 1

# for x in sys.argv:
#     print(x)
# print('')
# os.listdir(sys.argv[1]) # returns list


#################################################################

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


	if continueThis == True:
		if os.path.isdir(folder) == True:
			dirList = os.listdir(folder)
			for item in dirList:
				path = folder + _v.slash + item
				if os.path.isdir(item) == True:
					if base <= folderDepthMax:
						base += folderDepth(path)
					else:
						getSubFolderData = False
	return True
	# return base
def folderSizeX(path):
	size = 0
	if os.path.isdir(path) == True:
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


	if continueThis == True:
		if os.path.isdir(folder) == True:
			dirList = os.listdir(folder)
			for item in dirList:
				path = folder + _v.slash + item
				if os.path.isdir(item) == True:
					try:
						getSubFolderData = folderDepth(path)
					except Exception as e:
						getSubFolderData = False
					if isSwitchActive('RecursionFolderSize') == True and timeoutKill == False and getSubFolderData == True:
						base += folderSizeX(path)
					else:
						pass

				else:
					if os.path.isfile(path) == True:

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
		if os.path.isdir(path) == True:
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
			if isSwitchActive('RecursionFolderSize') == True and timeoutKill == False and getSubFolderData == True:
				
				
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
					if os.path.isfile(create_sub_file_path) == True:
						file = open(create_sub_file_path, 'rb')
						createdRaw = os.path.getctime(create_sub_file_path)
						created = formatDate(createdRaw)
					if os.path.isfile(mod_sub_file_path) == True:
						file = open(mod_sub_file_path, 'rb')
						modifiedRaw = os.path.getmtime(mod_sub_file_path)
						modified = formatDate(modifiedRaw)
				except Exception as e:
					errors.append({'id': 6, 'function': 'buildResult()', 'cnt': 3, 'location': "file = open(create_sub_file_path, 'rb')", 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})

			if isSwitchActive('Recursion') == True and timeoutKill == False and getSubFolderData == True:
				buildResult(1,path)
			else:
				if modifiedRaw > 100:
					year = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[0]
					woy = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[1]
					dow = datetime.datetime.fromtimestamp( int(modifiedRaw) ).isocalendar()[2]
					currentDate = time.time()
					thisweek = datetime.datetime.fromtimestamp( int(currentDate) ).isocalendar()[1]
					friendlyWeek0 = weeks_between(modifiedRaw, currentDate)
					friendlyMonth0 = months_between(modifiedRaw, currentDate)
					littleMonth = monthByNumber(formatDateMonth(modifiedRaw))
					if friendlyMonth0 == 0:
						# friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
						# friendlyWeek1 += ' (This week)'
						friendlyMonth1 = '( This month: ' + littleMonth + ' )'
					elif friendlyMonth0 == 1:
						friendlyMonth1 = '( Last month: ' + littleMonth + ' )'

					else:
						if int(friendlyMonth0) > 12:
							years = math.floor(int(friendlyMonth0)/12)
							months = int(friendlyMonth0) - (years * 12)
							friendlyMonth1 = str(years) + ' years ' + str(months) + ' months ago: ' + littleMonth
						else:
							friendlyMonth1 = str(friendlyMonth0) + ' months ago: ' + littleMonth
						

					if friendlyWeek0 < 0:
						friendlyWeek0 = 0
					if friendlyWeek0 == 0:
						# friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
						# friendlyWeek1 += ' (This week)'
						friendlyWeek1 = '( This week )'
						
					else:
						friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
					weekAndYear = round(woy * 0.01,2) + year
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
				if isSwitchActive('ResolveIDs') == True:
					item = resolveIDs(item)
				try:
					if os.path.isdir(path) == True:
						createdRaw = os.stat(path).st_ctime
						created = formatDate(createdRaw)
					if os.path.isdir(path) == True:
						modifiedRaw = os.stat(path).st_mtime
						modified = formatDate(modifiedRaw)
				except Exception as e:
					errors.append({'id': 61, 'function': 'buildResult()', 'cnt': 3, 'location': "file = open(create_sub_file_path, 'rb')", 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})
				try:
					if os.path.isdir(path) == True:
						size = os.stat(path).ST_SIZE
						sizeF = formatSize(size)
				except Exception as e:
					errors.append({'id': 62, 'function': 'buildResult()', 'cnt': 3, 'location': "file = open(create_sub_file_path, 'rb')", 'vars': [{'name': 'folder', 'value': folder},{'name': 'item', 'value': item}], 'error': e})

				dirRows.append({'path': path2, 'name_': fileNameLength(item,''), 'name': item, 'folder': folder, 'stat': '', 'attrib': '', 'bytes': size, 'size': sizeF, 'date_created_raw': createdRaw, 'date_modified_raw': modifiedRaw, 'date_created': created, 'date_modified': modified, 'type': 'Folder', 'typesort': 0, 'ext': '', 'week_of_year': weekAndYear, 'week_of_year_': woy, 'day_of_the_week': dow, 'month': month, 'friendly_week': friendlyWeek1, 'friendly_month': friendlyMonth1})
		else:
			if os.path.isfile(path) == True and pathCheckBase(path) == True:
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
					if isSwitchActive('Hidden') == True:
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
					friendlyWeek0 = weeks_between(modifiedRaw, currentDate)
					# friendlyMonth0 = int(formatDateMonth(currentDate)) - int(formatDateMonth(modifiedRaw))
					friendlyMonth0 = months_between(modifiedRaw, currentDate)
					littleMonth = monthByNumber(formatDateMonth(modifiedRaw))
					if friendlyMonth0 == 0:
						# friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
						# friendlyWeek1 += ' (This week)'
						friendlyMonth1 = '( This month: ' + littleMonth + ' )'
					elif friendlyMonth0 == 1:
						friendlyMonth1 = '( Last month: ' + littleMonth + ' )'

					else:
						if int(friendlyMonth0) > 12:
							years = math.floor(int(friendlyMonth0)/12)
							months = int(friendlyMonth0) - (years * 12)
							friendlyMonth1 = str(years) + ' years ' + str(months) + ' months ago: ' + littleMonth
						else:
							friendlyMonth1 = str(friendlyMonth0) + ' months ago: ' + littleMonth
					if friendlyWeek0 < 0:
						friendlyWeek0 = 0
					if friendlyWeek0 == 0:
						# friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
						# friendlyWeek1 += ' (This week)'
						friendlyWeek1 = '( This week )'
					elif friendlyWeek0 == 1:
						friendlyWeek1 = '( Last week )'

					else:
						friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
					dow = dowConvert(dow)
					month = round(int(formatDateMonth(modifiedRaw))* 0.01,2) + year
					weekAndYear = round(woy * 0.01,2) + year
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
				if displayThis == True:
					path2 = os.path.realpath(path)
					if isSwitchActive('ResolveIDs') == True:
						item = resolveIDs(item)
					dirRows.append({'path': path2, 'name_': fileNameLength(item,ext), 'name': item, 'folder': folder, 'stat': stat, 'attrib': attribs, 'bytes': size, 'size': sizeF, 'date_created_raw': createdRaw, 'date_modified_raw': modifiedRaw, 'date_created': created, 'date_modified': modified, 'type': 'File', 'typesort': 1, 'ext': ext, 'week_of_year': weekAndYear, 'week_of_year_': woy, 'day_of_the_week': dow, 'month': month, 'friendly_week': friendlyWeek1, 'friendly_month': friendlyMonth1})
	return dirRows

#########################################################
#########################################################

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
		if toLong == True:
			result += '...'
			if len(ext) > 0:
				result += '  .' + ext
	except Exception as e:
		result = string
	return result

def buildResultFromPipe():
	global pipeResults
	global totalsizeCalc
	global totalCountItems
	millTimeStamp = lambda: int(round(time.time() * 1000))
	totalsizeCalc = 0
	totalCountItems = 0
	if isSwitchActive('GroupBy') == True:
		if getSwitchValue('GroupBy') == 'none':
			updateSwitchField('GroupBy','active',False)
	for path in pipeResults:
		path = path.replace('\n','')
		path = path.replace('\r','')
		# path = path.encode('UTF-8')
		# path = str(path)
		path = pathCheck(path)
		if os.path.isfile(path) == True:
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
					if isSwitchActive('Hidden') == True:
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
					friendlyWeek0 = weeks_between(modifiedRaw, currentDate)
					friendlyMonth0 = months_between(modifiedRaw, currentDate)
					littleMonth = monthByNumber(formatDateMonth(modifiedRaw))
					if friendlyMonth0 == 0:
						# friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
						# friendlyWeek1 += ' (This week)'
						friendlyMonth1 = '( This month: ' + littleMonth + ' )'
					elif friendlyMonth0 == 1:
						friendlyMonth1 = '( Last month: ' + littleMonth + ' )'

					else:
						if int(friendlyMonth0) > 12:
							years = math.floor(int(friendlyMonth0)/12)
							months = int(friendlyMonth0) - (years * 12)
							friendlyMonth1 = str(years) + ' years ' + str(months) + ' months ago: ' + littleMonth 
						else:
							friendlyMonth1 = str(friendlyMonth0) + ' months ago: ' + littleMonth
					if friendlyWeek0 < 0:
						friendlyWeek0 = 0
					if friendlyWeek0 == 0:
						# friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
						# friendlyWeek1 += ' (This week)'
						friendlyWeek1 = '( This week )'
					elif friendlyWeek0 == 1:
						friendlyWeek1 = '( Last week )'

					else:
						friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
					dow = dowConvert(dow)
					month = round(int(formatDateMonth(modifiedRaw))* 0.01,2) + year
					weekAndYear = round(woy * 0.01,2) + year
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
				if isSwitchActive('isFile') == True:
					print(path)
				else:
					if displayThis == True:
						global totalLINE
						totalLINE = '__________________________________'
						totalsizeCalc += size
						totalCountItems += 1
						if folder == '' or folder == None:
							folder = os.getcwd()
						if isSwitchActive('Bookmark') == True:
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
										if os.path.isdir(line) == True:
											bm_status = 'Works'
								bmFile.close()
							if isSwitchActive('ResolveIDs') == True:
								item = resolveIDs(item)
							dirRows.append({'timeAudit': timeAudit,'path': path2, 'name_': fileNameLength(item,ext), 'bookmark': bookmark, 'bm_status': bm_status, 'bm_path': fileNameLength(bm_path,'',90), 'name': item, 'folder': folder, 'stat': stat, 'attrib': attribs, 'bytes': size, 'size': sizeF, 'date_created_raw': createdRaw, 'date_modified_raw': modifiedRaw, 'date_created': created, 'date_modified': modified, 'date_created_': created.split(' ')[0], 'date_modified_': modified.split(' ')[0],'type': 'File', 'typesort': 1, 'ext': ext, 'week_of_year': weekAndYear, 'week_of_year_': woy, 'day_of_the_week': dow, 'month': month, 'friendly_week': friendlyWeek1, 'friendly_month': friendlyMonth1})
						else:
							if isSwitchActive('ResolveIDs') == True:
								item = resolveIDs(item)
							dirRows.append({'timeAudit': timeAudit,'path': path2, 'name_': fileNameLength(item,ext), 'name': item, 'folder': folder, 'stat': stat, 'attrib': attribs, 'bytes': size, 'size': sizeF, 'date_created_raw': createdRaw, 'date_modified_raw': modifiedRaw, 'date_created': created, 'date_modified': modified, 'type': 'File', 'typesort': 1, 'ext': ext, 'week_of_year': weekAndYear, 'week_of_year_': woy, 'day_of_the_week': dow, 'month': month, 'friendly_week': friendlyWeek1, 'friendly_month': friendlyMonth1})
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
	if rows['A'] == True:
		result += 'A' 
	if rows['S'] == True:
		result += 'S' 
	if rows['H'] == True:
		result += 'H' 
	if rows['R'] == True:
		result += 'R' 
	if rows['I'] == True:
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
		print('Error:')
		print('\tBad column input.')
		print(name)
		os._exit(0)
	# print(name)
	for item in rows:
		# print(item)
		text = item[name]
		if isDir == True:
			typ = item['typesort']
			if isSwitchActive('Yr') == True and (name == 'date_created' or name == 'date_modified'):
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

	if isSwitchActive('GroupBy') == True:
		if getSwitchValue('GroupBy') == 'none':
			updateSwitchField('GroupBy','active',False)

	try:
		tabFix = spaces[column]
	except Exception as e:
		# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
		tabFix = tabGetMaxSpace(isDir,rows,column)
		spaces[column] = tabFix
	if isDir == True:
		typ = int(rows[i]['typesort'])
		if isSwitchActive('Yr') == True and (column == 'date_created' or column == 'date_modified'):
			text = str(text)
			text = text.replace('2017-','')
		if typ == 0 and column == 'name':
			text = formatFolderName(text)
		if isSwitchActive('GroupBy') == True:
			for gb in groupBy.split(','):
				gb = str(columnNickname2(gb))
				if column == gb:
					if not test(groupByList[gb],text) == True:
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
	if not ',' in getSwitchValue('Column') and isSwitchActive('Column') == True and isSwitchActive('GroupBy') == False:
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
	if os.path.isfile(cacheFile) == True:
		os.system('attrib -h '+ cacheFile)
	with open(cacheFile,'r', encoding="latin-1") as json_file:
		json_data = json.load(json_file)
	return json_data

def dirCacheSave(rows,cacheFile):
	if os.path.isfile(cacheFile) == True:
		os.system('attrib -h '+ cacheFile)
	dataDump = json.dumps(rows, indent=4, sort_keys=True)
	f = open(cacheFile,'w')
	f.write(str(dataDump))
	f.close()
	# os.system('attrib +h '+ cacheFile)

def displayLine(rows):
	# print(type(rows))
	rows = displayLineExclude(rows)
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


def displayLineExcludeString(string):
	if isSwitchActive('Minus') == True:
		action = True
		for d in getSwitchValue('Minus').split(','):
			if d.upper() in string.upper():
				show = False
				string = ''
	return string


def displayLineIncludeString(string):
	if isSwitchActive('InPath') == True:
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

def displayLineExclude(rows):
	action = False
	rowsNew = []

	if isSwitchActive('Minus') == True:
		
		action = True
		do = getSwitchValue('Minus').split(',')
		for r in rows:
			show = True
			val = r['path']
			for d in do:
				if d.upper() in val.upper():
					show = False
			if show == True:
				rowsNew.append(r)
	## END Minus

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows


def displayLineInclude(rows):
	action = False
	rowsNew = []

	if isSwitchActive('InPath') == True:
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
			if show == True:
				rowsNew.append(r)
	## END InPath

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows

def displayLineFolder(rows):
	action = False
	rowsNew = []

	if isSwitchActive('Folder') == True:
		
		action = True
		do = getSwitchValue('Folder').split(',')
		for r in rows:
			show = False
			val = r['path']
			for d in do:
				if d.upper() in val.upper():
					show = True
			if show == True:
				rowsNew.append(r)
	## END Folder

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows

def displayLineAgo(rows):
	action = False
	rowsNew = []
	if isSwitchActive('Ago') == True:
		action = True
		do = getSwitchValue('Ago')
		do = do.lower()
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
			if datetime.date.fromtimestamp(int(r['date_modified_raw']) ) > start_date:
				rowsNew.append(r)

	if action:
		rows = rowsNew
	# print(rowsNew)
	return rows
def displayLineSize(rows):
	action = False
	rowsNew = []

	if isSwitchActive('Size') == True:
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
			if show == True:
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
	if isSwitchActive('GroupBy') == True:
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
			if isSwitchActive('NoSave') == False:
				dirCacheSave(rows,_dirCache_p)
			# print('test')
			# rows = buildResultFromPipe()
			# rows = buildResult(0,folder)
		else:
			if isSwitchActive('Cache') == False:
				rows = buildResult(0,folder)
			elif os.path.isfile(_dirCache) == True:
				rows = dirCacheGet()
			else:
				rows = buildResult(0,folder)
		if isSwitchActive('NoSave') == False:
			dirCacheSave(rows,_dirCache)
		if isSwitchActive('Save') == True:
			if getSwitchValue('Save') == 'none' or getSwitchValue('Save') == '' or getSwitchValue('Save') == None:
				pass
			else:
				dirCacheSave(rows,getSwitchValue('Save'))
				os.system('attrib -h '+ getSwitchValue('Save'))
	else:
		rows = dirRows

	rows = displayLine(rows)
	if isSwitchActive('Save2') == True:
		if getSwitchValue('Save2') == 'none' or getSwitchValue('Save2') == '' or getSwitchValue('Save2') == None:
			pass
		else:
			dirCacheSave(rows,getSwitchValue('Save2'))
			os.system('attrib -h '+ getSwitchValue('Save2'))
	if len(rows) < 1:
		print('No Files')
		os._exit(0)

	if isSwitchActive('isFile') == False:
		if isSwitchActive('Sort') == True:
			rows = sortThis(rows, False)
		elif isSwitchActive('GroupBy') == True:
			rows = sortThis(rows, getSwitchValue('GroupBy') + ', Desc:date_modified')
		else:
			if isSwitchActive('Recursion') == True:
				rows = sortThis(rows, 'Asc:type, Asc:folder, Asc:ext, Asc:name')
			else:
				rows = sortThis(rows, 'Asc:type, Asc:ext, Asc:name')
		i = 0
		if not type(pipeResults) == list:
			if isSwitchActive('CSV') == False and isSwitchActive('Cache') == False and False == True:
				print(showPreHeader(rows))
		if isSwitchActive('CSV') == False:
			columnHeader = showColumnHeader(True,rows,column)
		else:
			columnHeader = showColumnHeaderCSV(True,rows,column)
			columnHeader = columnHeader[:-1]
		columnHeaderLength = len(columnHeader)
		print(columnHeader)
		for item in rows:
			result = ''    
			for c in column.split(','):
				c = columnNickname2(c)
				try:
					if isSwitchActive('CSV') == False:
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
			if isSwitchActive('CSV') == True:
				result = result[:-1]        
			print(result)
			i += 1
	# try:
	#     print('\n',totalLINE)
	#     # print('\n\t','Total Size:',formatSize(totalSize(rows)))
	#     # print('\t','Total Count:',len(rows))
	#     print('\n\t',len(rows),'files',formatSize(totalSize(rows)))
	# except Exception as e:
	#     pass
	if isSwitchActive('CSV') == False and isSwitchActive('NoCount') == False:
		print('\n\t',len(rows),'files',formatSize(totalSize(rows)))

def totalSize(rows):
	total = 0
	for r in rows:
		total += r['bytes']
	return total

def listPrintColumn(rows,column):
	global errors
	global columnTab

	column = cleanLastChar(column,',')
	column = column.replace(' ','')
	i = 0
	columnHeader = ''
	print(showColumnHeader(False,rows,column))
	for item in rows:
		result = ''        
		for c in column.split(','):
			try:
				result += showColumn(False,rows,c,i) + columnTab
			except Exception as e:
				errors.append({'id': 14, 'function': 'dirPrintColumn()', 'cnt': 1, 'location': "result += showColumn(False,rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': folder}, {'name': 'column', 'value': column}], 'error': e})
				print('Error:')
				print('\tBad column input.')
				print(c)
				os._exit(0)
		print(result)
		i += 1

def replaceAll(string,rWhat,rWith):
	done=False
	tmp = '{C9DCAA81-3B8A-68E9-E4CF-A405E2199CB9}'
	while done == False:
		if string.count(rWhat) > 0:
			string = string.replace(rWhat,tmp)
		else:
			done=True

	done=False
	while done == False:
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
	while done == False:
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
		if doesFieldExist(name,'script_trigger') == True:
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
				if checkIfSwitch(switchInput[i]) == True:
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
	if doesFieldExist(name,'script_trigger') == True:
		script = '{}(\'{}\',\'{}\')'.format(getSwitchField(name,'script_trigger'),name,value)
		value = eval(script)
	return value
def printSwitches():
	global switch
	for s in switch:
		if s['active'] == True:
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

	if completed == False and ts < killTime:
		x = Timer(0.0, timeout, ('loop',t))
		x.start()
	elif completed == False:
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
	if isSwitchActive('GroupBy') == True:
		if getSwitchValue('GroupBy') == 'none':
			updateSwitchField('GroupBy','active',False)

	try:
		column = column.lower()
		column = replaceAll(column,' ','')
		if (isSwitchActive('GroupBy') == True and isSwitchActive('LongFileName') == False) or isSwitchActive('ShortFileName') == True:
			if column == 'name':
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




	###################
	
	try:
		folder
	except Exception as e:
		folder = os.getcwd()
	try:
		if os.path.isdir(sys.argv[1]) == True:
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
		
	
	###################

	if isSwitchActive('ResolveIDs') == True:
		idResolution = getTable('idResolution.json')
	if isSwitchActive('Timestamp') == True:
		print(int(round(time.time() * 1000)))
		os._exit(0)

	if isSwitchActive('Convert') == True:
		if getSwitchValue('Convert').split(',')[0] == 'timestamp':
			stamp = int(getSwitchValue('Convert').split(',')[1])
			result = datetime.datetime.fromtimestamp(stamp / 1e3)
			print(result)
		else:
			if 'B' in getSwitchValue('Convert') or 'b' in getSwitchValue('Convert'):
				print(unFormatSize(getSwitchValue('Convert')))
			else:
				print(formatSize(int(getSwitchValue('Convert'))))
		os._exit(0)


	if isSwitchActive('Timeout') == True:
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
	if isSwitchActive('GroupBy') == True:
		if getSwitchValue('GroupBy') == 'none':
			updateSwitchField('GroupBy','active',False)
	if isSwitchActive('GroupBy') == True and isSwitchActive('Column') == False:
		updateSwitchField('GroupBy','groupByDefault',True)

	# if isSwitchActive('GroupBy') == True:
	#     if isSwitchActive('Column') == True:
	#         groupByDefault = False
	#     elif isSwitchActive('GroupBy') == True:
	#         groupByDefault = True
	#     else:
	#         groupByDefault = False
	# else:
	#     groupByDefault = False
	#     groupBy = ''

	if isSwitchActive('Bookmark') == True and isSwitchActive('Column') == False:
		updateSwitchField('Column','active',True)
		# updateSwitchField('Column','value','cd, md, bookmark, bm_status,bm_path')
		# updateSwitchField('Column','value','md, bookmark, bm_status,bm_path')
		updateSwitchField('Column','value','date_created_, date_modified_, bookmark, bm_status,bm_path')
		if isSwitchActive('Sort') == False:
			updateSwitchField('Sort','active',True)
			updateSwitchField('Sort','value','desc:md')

	if isSwitchActive('Report') == True and (getSwitchValue('Report') == 'date2' ): # or getSwitchValue('Report') == 'd'
		# -g  -c n fm fw d md -s d:md
		updateSwitchField('GroupBy','active',True)
		updateSwitchField('GroupBy','value','fm, woy2, d')
		# updateSwitchField('GroupBy','value','fm, fw, d')
		updateSwitchField('Column','active',True)
		updateSwitchField('Column','value','n,fm, woy2, d, md')
		# updateSwitchField('Column','value','n,fm, fw, d, md')
		updateSwitchField('Sort','active',True)
		updateSwitchField('Sort','value','d:md')

	if isSwitchActive('Report') == True and (getSwitchValue('Report') == 'date' ): # or getSwitchValue('Report') == 'd'
		# -g  -c n fm fw d md -s d:md
		updateSwitchField('GroupBy','active',True)
		# updateSwitchField('GroupBy','value','fm, woy2, d')
		updateSwitchField('GroupBy','value','fm, fw, d')
		updateSwitchField('Column','active',True)
		# updateSwitchField('Column','value','n,fm, woy2, d, md')
		updateSwitchField('Column','value','n,fm, fw, d, md')
		updateSwitchField('Sort','active',True)
		updateSwitchField('Sort','value','d:md')

	if isSwitchActive('ReportDate') == True or isSwitchActive('Report') == True and (getSwitchValue('Report') == 'date3' or getSwitchValue('Report') == 'd'):
		# -g  -c n fm fw d md -s d:md
		updateSwitchField('GroupBy','active',True)
		# updateSwitchField('GroupBy','value','fm, woy2, d')
		updateSwitchField('GroupBy','value','fm, fw, d')
		updateSwitchField('Column','active',True)
		# updateSwitchField('Column','value','n,fm, woy2, d, md')
		updateSwitchField('Column','value','n,fm, fw, d, md')
		updateSwitchField('Sort','active',True)
		updateSwitchField('Sort','value','asc:md')


	if isSwitchActive('Help') == True:
		print('Displays directory information.\n')
		print('Example:\n\tp dir -Column: size, name -Sort: Asc:type, Asc:ext, Asc:name -Errors: hide:8,11 -FolderSize -Timeout: 10 -NoExit')
		print('\n\tp dir -c name, week_of_year -s week_of_year -g week_of_year')
		print('\n\tp dir -c name, ext -s ext -g ext')
		print('\n\tp dir -g fm fw d -s desc:dm')
		print('\n\tp dir -cache Movies_Cloud.dirCache -size g 3gb -c p | p line --c + y: | p line --c -p \ ee | p line --c -p \ e 2 -pc')
		print('\n\tp dir -cache Movies_Cloud.dirCache -c p  + star trek -size g 1gb')
		print('\n\tp f -bm + tmp -n | p dir -b')
		# print('\nColumns:\n\tname, path, size, type, ext, date_created, date_modified, stat, attrib')
		print('\n\nColumns:\n\tname path size type ext date_created date_modified stat attrib week_of_year')
		print('\n-----------------------------------------------\nList of switches:\n')
		listPrintColumn(switch,'name,switch,expected_input_example')
		# for s in switch:
		#     print('{}: {}'.format(s['name'],s['switch']))
	elif isSwitchActive('Debug') == True:
		printSwitches()
		print(isSwitchActive('ShortFileName'))
	elif isSwitchActive('Test') == True: 
		cnt = folderSizeX(folder)
		print(cnt)
		print(formatSize(cnt))
	elif isSwitchActive('Column') == True:
		if getSwitchValue('Column') == None:
			print('dir -c size, name')
			print('\nColumns:\n\tname path size type ext date_created date_modified stat attrib week_of_year')
		else:
			dirPrintColumn(folder,getSwitchValue('Column'))
	else:
		if isSwitchActive('Recursion') == True and isSwitchActive('GroupBy') == False:
			updateSwitchField('GroupBy','active',True)
			updateSwitchField('GroupBy','groupByDefault',True)
			updateSwitchField('GroupBy','value','folder')
			dirPrintColumn(folder,'size,name,folder')
		else:
			if type(pipeResults) == list and isSwitchActive('GroupBy') == True:
					dirPrintColumn(folder,'name,' + getSwitchValue('GroupBy'))
			if type(pipeResults) == list and isSwitchActive('GroupBy') == False:
				updateSwitchField('GroupBy','active',True)
				updateSwitchField('GroupBy','groupByDefault',True)
				updateSwitchField('GroupBy','value','folder')
				dirPrintColumn(folder,'size,name,folder')
			else:
				if getSwitchField('GroupBy','groupByDefault') == True:
					dirPrintColumn(folder,'name,' + getSwitchValue('GroupBy'))
				else:
					dirPrintColumn(folder,'size,name')

	completed = True

	if timeoutKill == True:
		print('\n*** Timeout ***')
		print('\t Folder sizes may be inaccurate')


	if isSwitchActive('Errors') == True:
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
			if show == True:
				print('\tid: {} function: {} error: {}'.format(eId,function,e))
				for v in var:
					name = v['name']
					value = v['value']
					print('\t\t{}: {}'.format(name,value))


def getTable(theFile,tableTemp = True,printThis = False):
	# defaults to myTables
	if tableTemp == True:
		file0 = _v.myTables + _v.slash + theFile
	else:
		file0 = _v.stmp + _v.slash + theFile
	if printThis:
		print('Loaded: ' + file0)
	if os.path.isfile(file0) == True:
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
switch.append({'name': 'LongFileName','switch': '-ln,-LongFileName', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'ShortFileName','switch': '-sn,-ShortFileName', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Report','switch': '-re,-report', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'ReportDate','switch': '-date,-reportdate', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
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
#################################################################




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
# if os.path.isfile(filename) == True:
#     pipeResults = getImport()
# if not sys.stdin.isatty() and os.path.isfile(filename) == True:
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
#     if os.path.isfile(filename) == True:
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


takeAction()

if isSwitchActive('NoExit') == True:
	Loop_Action = True
	while Loop_Action == True:
		Loop_ActionCnt += 1
		switchInputRaw = input('\n\n_____________\n\ndo: ')
		if switchInputRaw == 'quit' or switchInputRaw == 'q' or switchInputRaw == 'exit' or switchInputRaw == 'c':
			takeAction()