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
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
import _rightThumb._md5 as _md5
##################################################

def appSwitches():
	_.switches.register( 'Save', '-save' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'Compair', '-compair' )
	_.switches.register( 'Folder', '-f,-fo,-folder' )
	_.switches.register( 'Links', '-l,-link,-links' )
	_.switches.register( 'CopyText', '-copy,-cp' )
	# _.switches.register( 'NoCopy', '-nocopy' )
	



_.appInfo[focus()] = {
	'file': 'file_folder.py',
	'description': 'Print files and folders',
	'categories': [
						'file',
						'files',
						'folder',
						'folders',
						'list',
						'cross reference',
						'xref',
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
						'p file_folder',
						'',
						'p file_folder -save',
						'p file_folder -compair',
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
	_.switches.trigger( 'Folder',_.myFolderLocations )
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

_.postLoad( __file__ )

########################################################################################
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
########################################################################################
# START


def isLink(path):
	if os.path.islink(path): return True
	try: return os.stat(path).st_nlink > 1
	except: return False




def has_hard_links(path):
	try:
		return os.stat(path).st_nlink > 1
	except:
		return False

import pathlib
if not os.path.isfile('.subjects'):
	subjects = []
else:
	subjects = _.getText( '.subjects', raw=True, clean=2 ).split('\n')
__.subItem = 'Background.blue'
__.subLink = 'Background.yellow'
for i,s in enumerate(subjects):
	subjects[i] = s.strip()

def action():
	global copied
	global subjects
	_copy_this=[]
	if _.switches.isActive( 'Folder' ):
		if len( _.switches.values( 'Folder' ) ):
			folder = _.switches.values( 'Folder' )[0]
		else:
			folder = _.switches.value( 'Folder' )
	else:
		folder = os.getcwd()

	# _.pr( 'folder:', folder )


	if _.switches.isActive( 'Compair' ):
		oldList = _.getTable2( _v.myTemp + _v.slash+'file_folder_md5-' + _md5.md5( folder ) + '.json' )
		# _.printVar( oldList )
		if oldList is None:
			_.pr( 'Error: nothing to compair to' )
			return False
	i = 0
	links = []
	links2 = []
	files = []
	folders = []
	totalLink = 0
	totalFile = 0
	totalFolder = 0
	if not folder.strip(): folder = os.getcwd()
	for item in os.listdir(folder):
		path = folder + _v.slash + item
		# _.pr( path )
		if os.path.islink(path) or has_hard_links(path):
			if _.showLine(item):
				links.append({ 'label':  item  })
				links2.append(path)
		if os.path.isfile(path):
			totalFile+=1
			if _.showLine(item):
				files.append({ 'label':  item  })
		if not os.path.isfile(path):
			totalFolder+=1
			if _.showLine(item):
				folders.append({ 'label':  item  })


	if not _.switches.isActive( 'Compair' ):
		if _.switches.isActive( 'Clean' ):
			if _.switches.isActive( 'Save' ):
				newList = {
							'files': [],
							'folders': [],
				}
				
				for f in files:
					newList['files'].append( f['label'] )
				for f in folders:
					newList['folders'].append( f['label'] )

				_.saveTable2( newList, _v.myTemp + _v.slash+'file_folder_md5-' + _md5.md5( folder ) + '.json' )
			else:
				for f in files:
					_.pr( f['label'] )
				for f in files:
					_.pr( f['label'] )
		else:


			for i,item in enumerate(links):
				links[i]['sort_by_field'] = item['label'].replace( '__', '_0_' )
				
			for i,item in enumerate(files):
				files[i]['sort_by_field'] = item['label'].replace( '__', '_0_' )
			global subjects
			# for f in files:
			# 	if f['label'] in subjects:
			# 		_.pr( f['label'], c='green' )
			
			if _.switches.isActive('Links') and links:
				_.pr()
				_.colorThis( 'Links:', 'green' )
				for f in _.tables.returnSorted( 'links', 'a.sort_by_field', links ):
					if f['label'] in subjects:
						_.colorThis( [ '\t',f['label'] ], __.subLink )
					else:
						_.colorThis( [ '\t',f['label'] ], 'yellow' )

			files=_.tables.returnSorted( 'files', 'a.sort_by_field', files )    
			for f in files: _copy_this.append(f['label'])
			_.pr()
			_.colorThis( 'Files:', 'green' )

			# for f in files:
			#     if os.path.islink(f['label']):
			#         _.colorThis( [ '\t',f['label'] ], 'yellow' )
			#     else:
			#         _.colorThis( [ '\t',f['label'] ], 'cyan' )

			
			displayed_files=[]
			for f in files:
				if not os.path.islink(f['label']) and not has_hard_links(f['label']):
					displayed_files.append(f['label'])
					# if 'scrap' in f['label']:
					# 	print(subjects)
					if f['label'] in subjects:
						_.colorThis( [ '\t',f['label'] ], __.subItem )
					else:
						_.colorThis( [ '\t',f['label'] ], 'cyan' )


			for f in files:
				if os.path.islink(f['label']) or has_hard_links(f['label']):
					displayed_files.append(f['label'])
					if f['label'] in subjects:
						_.colorThis( [ '\t',f['label'] ], __.subLink )
					else:
						_.colorThis( [ '\t',f['label'] ], 'yellow' )

			if _.isWin and len(displayed_files) == 1:
				# if not _.switches.isActive('NoCopy'):
				if _.switches.isActive('CopyText'):
					_copy = _.regImp( __.appReg, '-copy' )
					_copy.imp.copy( displayed_files[0], p=0 )



			_.pr()
			if totalFile == len(files):
				_.colorThis( [ '',_.addComma(totalFile) ], 'yellow' )
			else:
				_.pr('',_.colorThis( [ _.addComma(len(files)) ], 'yellow', p=0 ),'of',_.colorThis( [ _.addComma(totalFile) ], 'yellow', p=0 ))
			_.pr()
			_.colorThis( 'Folders:', 'green' )
			for f in _.tables.returnSorted( 'folders', 'a.label', folders ):
				try:
					x=pathlib.Path(f['label']).resolve()
					# print(x)
					islink=False
				except:
					islink=True

				if islink or  os.path.islink(f['label']):
					if f['label'] in subjects:
						_.colorThis( [ '\t',f['label'] ], __.subLink )
					else:
						_.colorThis( [ '\t',f['label'] ], 'yellow' )
				else:
					if f['label'] in subjects:
						_.colorThis( [ '\t',f['label'] ], __.subItem )
					else:
						_.colorThis( [ '\t',f['label'] ], 'cyan' )
			_.pr()
			if totalFolder == len(folders):
				_.colorThis( [ '',totalFolder ], 'yellow' )
			else:
				_.pr('',_.colorThis( [ _.addComma(len(folders)) ], 'yellow', p=0 ),'of',_.colorThis( [ _.addComma(totalFolder) ], 'yellow', p=0 ))
			_.pr()
			if folder in subjects:
				_.colorThis( folder, __.subItem )
			else:
				_.colorThis( folder, 'darkcyan' )
			_.pr()



	if _.switches.isActive( 'Compair' ):
		newList = {
					'files': [],
					'folders': [],
		}
		
		for f in files:
			newList['files'].append( f['label'] )
		for f in folders:
			newList['folders'].append( f['label'] )

		newItems = {
					'files': [],
					'folders': [],
		}
		for test in newList['files']:
			if not test in oldList['files']:
				newItems['files'].append( test )
		for test in newList['folders']:
			if not test in oldList['folders']:
				newItems['folders'].append( test )

		if not _.switches.isActive( 'Clean' ):
			if not len( newItems['files'] ) and not len( newItems['folders'] ):
				_.pr( 'No changes' )
				return False
			_.pr()
			_.colorThis( 'Files:', 'green' )
			for f in newItems['files']:
				if f in subjects:
					_.colorThis( [ '\t',f ], __.subItem )
				else:
					_.colorThis( [ '\t',f ], 'cyan' )
			_.pr()
			if totalFile == len(files):
				_.colorThis( [ '',_.addComma(totalFile) ], 'yellow' )
			else:
				_.pr('',_.colorThis( [ _.addComma(len(folders)) ], 'yellow', p=0 ),'of',_.colorThis( [ _.addComma(totalFolder) ], 'yellow', p=0 ))
			_.pr()
			_.colorThis( 'Folders:', 'green' )
			for f in newItems['folders']:
				if f in subjects:
					_.colorThis( [ '\t',f ], __.subItem )
				else:
					_.colorThis( [ '\t',f ], 'cyan' )
			_.pr()
			if totalFolder == len(folders):
				_.colorThis( [ '',_.addComma(totalFolder) ], 'yellow' )
			else:
				_.pr('',_.colorThis( [ _.addComma(len(folders)) ], 'yellow', p=0 ),'of',_.colorThis( [ _.addComma(totalFolder) ], 'yellow', p=0 ))
			_.pr()
			_.pr(folder)
			_.pr()
		return newItems
	if _.switches.isActive('Copy'):
		if _.isWin:
			# if not _.switches.isActive('NoCopy'):
			if _.switches.isActive('CopyText'):
				_copy.imp.copy( '\n'.join(_copy_this), p=0 ); copied=True;

	if copied: _.pr(' * copied *',c='r')
	if not folder == os.getcwd():
		_.pr()
		_.pr(_.pr0('Location:',c='ColorBold.magenta'),_.pr0(os.getcwd(),c='ColorBold.gray'))

if _.switches.isActive('Copy'):
	_copy = _.regImp( __.appReg, '-copy' )
copied=False

########################################################################################
if __name__ == '__main__':
	action()