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
	pass
	_.switches.register( 'Split', '-split', ' ":" 0  OR  ":" new ' )
	_.switches.register( 'Remove', '-r,-remove' )
	_.switches.register( 'Unique', '-u,-unique' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='data,clean',  description='Files' )
	_.switches.register( 'Save', '-save' )
	_.switches.register( 'Paste', '-p,-paste' )
	_.switches.register( 'Flatten', '-flat,-flatten', ';sp' )
	_.switches.register( 'Case', '-case', ' upper OR lower' )
	_.switches.register( 'WordStems', '-stems' )
	_.switches.register( 'JustTotal', '-total' )
	_.switches.register( 'Table', '-table' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = True
__.isRequired_or_List = ['Pipe','Files','Paste']

_.appInfo[focus()] = {
	'file': 'simpleList.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Pipe or file: Text to list, list to text',
	'categories': [
						'convert',
						'tool',
						'list',
						'pipe',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						'p word_stem_indices -i simpleList.tiktok + develop interviewer intelligence manager',
						'p word_stem_indices -i simpleList.tiktok',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p traverse -f 5e-SRD-Spells.json + storm -field name | p simpleList -split : 1 | p simpleList',
						'p traverse -f 5e-SRD-Spells.json + storm -field name | p simpleList -remove name:',
						'p traverse -f 5e-SRD-Spells.json + storm -field name | p simpleList -remove name :',
						'p traverse -f 5e-SRD-Spells.json + storm -field name | p simpleList -split : n ',
						'p traverse -f 5e-SRD-Spells.json + storm -field name | p simpleList -split : -unique',
						'',
						'type %tmpf8% | p line + : - http --c | p simpleList -split " " n -remove : "," -case lower -stems tiktok | p simpleList | p countEach',
						'',
						'echo %path% | p simpleList -split ; | p simpleList',
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
# START


processWordStem = None
index_of_word_stems = {}
def wordStem(word):
	global processWordStem
	global index_of_word_stems
	if processWordStem is None:
		import nltk
		from nltk.stem import PorterStemmer
		from nltk.tokenize import word_tokenize
		processWordStem = PorterStemmer()
	stem = processWordStem.stem(word)
	if not stem in index_of_word_stems:
		index_of_word_stems[stem] = {}
	index_of_word_stems[stem][word] = {}

	return stem

def process( data ):


	if _.switches.isActive('WordStems'):
		for i,x in enumerate(data):
			data[i] = wordStem(x)
		# _.pr('here')
		return data
	if _.switches.isActive('Split'):
		new = []
		if not len( _.switches.values('Split') ) > 1:
			s = 'n'
		elif 'n' in _.switches.values('Split')[1].lower():
			s = 'n'
		else:
			s = int(_.switches.values('Split')[1])
		
		for x in data:

			hadSplit = False
			if _.switches.values('Split')[0] == ' ':
				for xSp in x.split(' '):
					new.append(xSp)
			else:
				for sp in _.caseUnspecific( x, _.ci(_.switches.values('Split')[0]) ):
					hadSplit = True
					xSp = x.split(sp)
					if s == 'n':
						for y in xSp:
							new.append(y)
					elif not s == 'n':
						new.append(xSp[s])
				if not hadSplit:
					new.append(x)
		
		data = new

	if _.switches.isActive('Remove'):
		for i,x in enumerate(data):
			for rm in _.switches.values('Remove'):
				for sp in _.caseUnspecific( x, _.ci(rm) ):
					data[i] = data[i].replace( sp, '' )



	new = []
	for i,row in enumerate(data):
		if len( row ) and _.showLine(row):

			row = row.replace( '\t', ' ' )
			row = _str.replaceDuplicate( row, ' ' )
			row = _str.cleanBE( row, ' ' )

			new.append(row)

	data = new

	if _.switches.isActive('Case'):
		if 'u' in _.switches.value('Case').lower():
			upper = True
		else:
			upper = False
		for i,x in enumerate(data):
			if upper:
				data[i] = x.upper()
			else:
				data[i] = x.lower()


			# _.pr( data[i] )


	if _.switches.isActive('Unique'):
		new = []
		for x in data:
			if not x in new:
				new.append(x)
		data = new

	
	return data
 # Remove Unique

def action():

	if _.switches.isActive('Table'):
		records = []
		for i,row in enumerate( _.isData(r=1) ):
			records.append({ 'i': i, 'line': row })

		_.tables.r_.pr( records, 'line' )
		return None
		sys.exit()

	load()
	global data


	itIS = None
	if data[0][0] == '[':
		itIS = 'list'
	else:
		itIS = 'text'

	if itIS == 'text':
		new = []

		for i,row in enumerate(data):
			if len( row ):

				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )

				new.append(row)

		data = new
	elif itIS == 'list':
		_.saveText( data, _v.stmp+_v.slash+'simpleList.list' )
		data = _.getTable2( _v.stmp+_v.slash+'simpleList.list' )
		# data = eval( ''.join( data ) )



	data = process( data )

	if _.switches.isActive('JustTotal'):
		_.colorThis( _.addComma(len(data)), 'yellow' )
	elif not _.switches.isActive('JustTotal'):

		if not _.switches.isActive('Flatten'):
			if itIS == 'text':
				_.printVarSimple( data )
			elif itIS == 'list':
				for i,row in enumerate(data):
					_.pr( row )
		elif _.switches.isActive('Flatten'):
			if not _.switches.value('Flatten') is None and len( _.switches.value('Flatten') ):
				# _.pr( len( _.switches.value('Flatten') ), type( _.switches.value('Flatten') ), _.switches.value('Flatten') )
				by = _.switches.values('Flatten')[0]
			else:
				by = ','
			if by == ';sp':
				by = ' '
			_.pr(  by.join( data )  )

		if _.switches.isActive('Save'):
			_.saveText( '\n'.join(data), _.switches.values('Save')[0] )


		if _.switches.isActive('WordStems'):
			global index_of_word_stems
			if len( _.switches.value('WordStems') ):
				save_file = _.switches.values('WordStems')[0]
				if not '.' in save_file:
					save_file += '.index'
				if not 'simpleList.' in save_file:
					save_file = 'simpleList.' + save_file
				_.saveTableProject( 'nltk.word_stems', index_of_word_stems, save_file )

def load():
	global data

	if _.switches.isActive('Paste'):
		new = []
		last = ''
		while not last == '-exit':
			row = input( ' Enter data when done type -exit :  ' )
			row = row.replace( '\t', ' ' )
			row = _str.replaceDuplicate( row, ' ' )
			row = _str.cleanBE( row, ' ' )
			last = row
			if len(row) and not row == '-exit':
				new.append(row)
		data = new

	elif not _.switches.isActive('Paste'):
		data = _.isData(r=1);



########################################################################################
if __name__ == '__main__':
	action()







