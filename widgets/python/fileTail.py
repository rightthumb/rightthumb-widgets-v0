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

##################################################

##################################################


def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True,  description='Files' )
	_.switches.register( 'Lines', '-l,-lines' )
	_.switches.register( 'Head', '-head' )


	

def toInt(data):
	return int(data)

_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'fileTail.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'file tail',
	'categories': [
						'tool',
						'file',
						'tail',
						'head',
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
						_.hp('p fileTail -f fileBackup.json + backup file -or -l 200'),
						_.hp('p fileTail -f fileBackup.json + backup -or -l 200'),
						'p fileTail -f file.txt -lines 10',
						''
						'p fileTail -f %scrap%  -lines 50| p cryptString -password 123 456 789'
						''
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

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Lines',toInt)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )

########################################################################################
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# _.setPipeData( os.listdir(os.getcwd()), focus() )
# _.showLine(item)
#     if os.path.isdir(row):
#     if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START


import subprocess

# def tail(f, n, offset=0):
#     proc = subprocess.Popen(['tail', '-n', n + offset, f], stdout=subprocess.PIPE)
#     lines = proc.stdout.readlines()
#     return lines[:, -offset]

# def tail(f, n):
#     assert n >= 0
#     pos, lines = n+1, []
#     while len(lines) <= n:
#         try:
#             f.seek(-pos, 2)
#         except IOError:
#             f.seek(0)
#             break
#         finally:
#             lines = list(f)
#         pos *= 2
#     return lines[-n:]


# def tail(f, lines=1, _buffer=4098):
#     """Tail a file and get X lines from the end"""
#     # place holder for the lines found
#     lines_found = []

#     # block counter will be multiplied by buffer
#     # to get the block size from the end
#     block_counter = -1

#     # loop until we find X lines
#     while len(lines_found) < lines:
#         try:
#             f.seek(block_counter * _buffer, os.SEEK_END)
#         except IOError:  # either file is too small, or too many lines requested
#             f.seek(0)
#             lines_found = f.readlines()
#             break

#         lines_found = f.readlines()

#         # we found enough lines, get out
#         # Removed this line because it was redundant the while will catch
#         # it, I left it for history
#         # if len(lines_found) > lines:
#         #    break

#         # decrement the block counter to get the
#         # next X bytes
#         block_counter -= 1

#     return lines_found[-lines:]



# def tail(f, window=20):
#     """
#     Returns the last `window` lines of file `f` as a list.
#     f - a byte file-like object
#     """
#     if window == 0:
#         return []
#     BUFSIZ = 1024
#     f.seek(0, 2)
#     bytes = f.tell()
#     size = window + 1
#     block = -1
#     data = []
#     while size > 0 and bytes > 0:
#         if bytes - BUFSIZ > 0:
#             # Seek back one whole BUFSIZ
#             f.seek(block * BUFSIZ, 2)
#             # read BUFFER
#             data.insert(0, f.read(BUFSIZ))
#         else:
#             # file too small, start from begining
#             f.seek(0,0)
#             # only read what was not read
#             data.insert(0, f.read(bytes))
#         linesFound = data[0].count('\n')
#         size -= linesFound
#         bytes -= BUFSIZ
#         block -= 1
#     return ''.join(data).splitlines()[-window:]

def head(file, n):
	a_file = open(file)

	for i in range(n):

		line = a_file.readline()
		line = line.replace('\n','')
		line = line.replace('\r','')
		_.pr(line)

def tail(fn, n, offset=None):
	"""Reads a n lines from f with an offset of offset lines.  The return
	value is a tuple in the form ``(lines, has_more)`` where `has_more` is
	an indicator that is `True` if there are more lines in the file.
	"""
	f = open(fn, 'r')
	avg_line_length = 74
	to_read = n + (offset or 0)

	while 1:
		try:
			f.seek(-(avg_line_length * to_read), 2)
		except IOError:
			# woops.  apparently file is smaller than what we want
			# to step back, go to the beginning instead
			f.seek(0)
		pos = f.tell()
		lines = f.read().splitlines()
		if len(lines) >= to_read or pos == 0:
			return lines[-to_read:offset and -offset or None], \
				len(lines) > to_read or pos > 0
		avg_line_length *= 1.3



def action():
	n = 20
	if _.switches.isActive('Lines'):
		n = int( _.switches.values('Lines')[0] )


	if _.switches.isActive('Files'):
		f = _.switches.values('Files')[0]

		if _.switches.isActive('Head'):
			sample = head(f, n)
		else:
			sample = tail(f, n)
		if not sample is None:
			for x in sample:
				try:
					for z in x:
						if _.showLine(z):
							_.pr(z)
				except Exception as e:
					pass
	else:

		data = _.isData()
		if _.switches.isActive('Head'):
			for i,line in enumerate(data):
				if i < n:
					if _.showLine(line):
						_.pr(line)
		else:
			data.reverse()
			data0 = []
			for i,line in enumerate(data):
				if i < n:
					data0.append(line)
			data0.reverse()
			for i,line in enumerate(data0):
				if _.showLine(line):
					_.pr(line)




########################################################################################
if __name__ == '__main__':
	action()