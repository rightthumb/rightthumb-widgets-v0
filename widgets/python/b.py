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
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str

##################################################


def appSwitches():
	_.switches.register('Alias', '-a,-i,-alias','d,sendto,docs', isRequired=False)
	_.switches.register('Save', '-save')
	_.switches.register('History', '-h,-hist', 's 1 -15 4-15 (if len = 2 it will show duplicates for backtrack)', isRequired=False)
	_.switches.register('Sanitize', '--s,-san,-sanitize')
	_.switches.register('ResolveSanitization', '--r,-r,-resolve')


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False

# __.isRequired_or_List = ['Pipe','Files','Plus']


_.appInfo[focus()] = {
	'file': 'b.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Lookup bookmark',
	'categories': [
						'command line',
						'enviroment',
						'navigation',
						'cmd',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						'create bookmark to current folder',
						'    p m -a test',
						'list all bookmarks',
						'    p bookmarks',
						'quick generate bookmarks if blank',
						'   p bm-dirty | bash',
						'remove all bookmarks that no longer exist',
						'    p clean-bm -good -save',
						'bookmark location',
						'    p b -a ww',
						# '',
						# 'old not sure what it does',
						# '    p cleanBookmarks -?',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p b -a d',
						'',
						'p b -a d -save',
						'',
						'\t'+_v.myTemp + _v.slash+'bookmark.tmp',
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


def action():
	# Sanitize ResolveSanitization
	if _.switches.isActive('Sanitize'):
		path = _.switches.value('Sanitize')
		path = _v.sanitizeFolder(path)
		_.pr(path)
		return
	if _.switches.isActive('ResolveSanitization'):
		path = _.switches.value('ResolveSanitization')
		path = _v.resolveFolderIDs(path)
		_.pr(path)
		return
	# print()

	if _.switches.isActive('History'):
		
		if _.switches.values('History') and 's' in _.switches.values('History')[0]:

			def extactFolder(line):
				while '  ' in line:
					line = line.replace('  ',' ')
				line = line.strip()
				return line.split(' ')[2]

			log = _v.tt+os.sep+'BookmarksBySession'+os.sep+_v.session()+'.log'
			if not os.path.isfile(log):
				_.e('No log for that session')
			log = _.getText(log)
			spent=[]
			last=''
			log = align_log_lines(log)
			for i,line in enumerate(log):
				if  not i: continue
				if line in spent: continue
				if not len(_.switches.values('History')) == 2:
					spent.append(line)
				if _.showLine(line):
					current= extactFolder(line)
					if current == last and ' - ' in line:
						continue
					_.pr(line,c='cyan')
					last= extactFolder(line)
			return None

		if not _.switches.values('History'):
			when = _.past(0)
		else:
			when = _.switches.values('History')[0]
		if  not os.path.isfile(_v.bmLog):
			_.e('No log for that date')
		log = _.getText(_v.bmLog)
		log.reverse()
		spent=[]
		for i,line in enumerate(log):
			if line in spent: continue
			if not len(_.switches.values('History')) == 2:
				spent.append(line)
			if _.showLine(line):
				# _.pr(i+1, line,c='cyan')
				_.pr(line,c='cyan')
		return None


	# _.pv(_.switches.all())
	# if not _.switches.all():
	# 	print(sys.argv)
	# 	print(sys.executable)
	# 	print('Error: Missing alias')
	# print(_.switches.value('Alias')); sys.exit();
	made={}
	if 'wprofile' in _v.config_hash:
		made['h'] = 1
		h  = _v.config_hash['wprofile']
	if 'ww' in _v.config_hash:
		made['ww'] = 1
		ww = _v.config_hash['ww']
	# _.pr('made',made)
	if 'ww' in made  and 'h' in made:
		a = ww+os.sep+'databank'+os.sep+'tables'+os.sep+'bookmarks.index'
		b = h+os.sep+'tables'+os.sep+'bookmarks.index'
		# _.pr(os.path.isfile(b))
		try:
			if not os.path.isfile(b) and os.path.isfile(a):
				from shutil import copyfile
				copyfile(a,b)
		except Exception as e:
			pass
	# print("_.switches.value('Alias')",_.switches.value('Alias'))
	path = _bm.Bookmarks( _.switches.value('Alias') ).get()
	if path is None:
		_.colorThis( 'Error, Bookmark does not exist', 'red' )
		sys.exit()
	# print(_v.bmLog)
	_.saveLine(_v.bmLog, path)
	# print(_.)
	if _.switches.isActive('Save'):
		if _.switches.value('Save') == '':
			_.saveText( path, _v.myTemp + _v.slash+'bookmark.tmp' )
		else:
			_.saveText( path, _.switches.values('Save')[0] )
	else:
		# _.pr(path)
		if path.count(':'):
			parts = path.split(':')
			parts.reverse()
			path = path[0]+':'+parts[0]

		_.pr(path)



def align_log_lines(lines, delimiter='     ', num_columns=3):

	new = []
	for line in lines:
		line = line.replace(' back ',' - ')
		new.append(line)
	lines = new

	# Split each line into the desired number of columns
	rows = [line.strip().split(delimiter, maxsplit=num_columns - 1) for line in lines]

	# Pad rows with fewer columns
	for row in rows:
		while len(row) < num_columns:
			row.append('')

	# Get maximum width of each column
	col_widths = [
		max(len(row[i]) for row in rows)
		for i in range(num_columns)
	]

	# Create aligned lines
	aligned_lines = [
		'  '.join(row[i].ljust(col_widths[i]) for i in range(num_columns))
		for row in rows
	]

	return aligned_lines



import _rightThumb._bookmarks as _bm

########################################################################################
if __name__ == '__main__':
	action()