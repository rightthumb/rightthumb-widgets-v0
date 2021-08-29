#!/usr/bin/python3
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
	_.switches.register( 'Folder', '-f,-folder' )
	



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

def action():
	if _.switches.isActive( 'Folder' ):
		if len( _.switches.values( 'Folder' ) ):
			folder = _.switches.values( 'Folder' )[0]
		else:
			folder = _.switches.value( 'Folder' )
	else:
		folder = os.getcwd()

	# print( 'folder:', folder )


	if _.switches.isActive( 'Compair' ):
		oldList = _.getTable2( _v.myTemp + _v.slash+'file_folder_md5-' + _md5.md5( folder ) + '.json' )
		# _.printVar( oldList )
		if oldList is None:
			print( 'Error: nothing to compair to' )
			return False
	i = 0
	files = []
	folders = []
	totalFile = 0
	totalFolder = 0
	for item in os.listdir(folder):
		path = folder + _v.slash + item
		# print( path )
		if os.path.isfile(path):
			totalFile+=1
			if _.showLine(item):
				files.append({ 'label':  item  })
		if os.path.isdir(path):
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
					print( f['label'] )
				for f in files:
					print( f['label'] )
		else:


			for i,item in enumerate(files):
				files[i]['sort_by_field'] = item['label'].replace( '__', '_0_' )


			print()
			_.colorThis( 'Files:', 'green' )
			for f in _.tables.returnSorted( 'files', 'a.sort_by_field', files ):
				_.colorThis( [ '\t',f['label'] ], 'cyan' )
			print()
			if totalFile == len(files):
				_.colorThis( [ '',_.addComma(totalFile) ], 'yellow' )
			else:
				print('',_.colorThis( [ _.addComma(len(files)) ], 'yellow', p=0 ),'of',_.colorThis( [ _.addComma(totalFile) ], 'yellow', p=0 ))
			print()
			_.colorThis( 'Folders:', 'green' )
			for f in _.tables.returnSorted( 'folders', 'a.label', folders ):
				_.colorThis( [ '\t',f['label'] ], 'cyan' )
			print()
			if totalFolder == len(folders):
				_.colorThis( [ '',totalFolder ], 'yellow' )
			else:
				print('',_.colorThis( [ _.addComma(len(folders)) ], 'yellow', p=0 ),'of',_.colorThis( [ _.addComma(totalFolder) ], 'yellow', p=0 ))
			print()
			_.colorThis( folder, 'darkcyan' )
			print()



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
				print( 'No changes' )
				return False
			print()
			_.colorThis( 'Files:', 'green' )
			for f in newItems['files']:
				_.colorThis( [ '\t',f ], 'cyan' )
			print()
			if totalFile == len(files):
				_.colorThis( [ '',_.addComma(totalFile) ], 'yellow' )
			else:
				print('',_.colorThis( [ _.addComma(len(folders)) ], 'yellow', p=0 ),'of',_.colorThis( [ _.addComma(totalFolder) ], 'yellow', p=0 ))
			print()
			_.colorThis( 'Folders:', 'green' )
			for f in newItems['folders']:
				_.colorThis( [ '\t',f ], 'cyan' )
			print()
			if totalFolder == len(folders):
				_.colorThis( [ '',_.addComma(totalFolder) ], 'yellow' )
			else:

				print('',_.colorThis( [ _.addComma(len(folders)) ], 'yellow', p=0 ),'of',_.colorThis( [ _.addComma(totalFolder) ], 'yellow', p=0 ))
			print()
			print(folder)
			print()
		return newItems



########################################################################################
if __name__ == '__main__':
	action()



