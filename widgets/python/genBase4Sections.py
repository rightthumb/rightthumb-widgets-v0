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
	_.switches.register( 'Save', '-save' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'genBase4Sections.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Construct2 tool this is named wrong',
	'categories': [
						'construct2',
						'base4',
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
						'p genBase4Sections -save %tmpf1%',
						'',
						'p genBase4Sections -save',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START


_func = _.regImp( __.appReg, 'inFunc' )
_func.switch( 'JustReturn' )

def findbase(name):
	global file
	global parts
	global data
	global oc

	r = None
	for record in data:
		if '__'+name+'__' == record['name']:
			r = record
	if r is None:
		return None

	result = ''
	record = r
	result = ''
	isOpen = False
	for i,line in enumerate(file):

		if i == record['start']-1:
			isOpen = True
		if isOpen and i >= record['start'] or isOpen and i <= record['end']:
			
			# result+=str(i)+' '
			result+=line
		

		elif i > record['end']:
			isOpen = False
		if i == record['end']:
			isOpen = False
	return result

def injectFirstRow( row, data ):
	if row == None:
		return data

	result = ''
	for i,line in enumerate(data.split('\n')):
		if not i:
			result += row
		else:
			result += line+'\n'

	return result

def clean_appReg( data ):
	# _.pr( data )
	result = ''
	appReg_spent = False
	for x in data.split('\n'):
		shouldAdd = True
		if 'global appReg'.lower() in x.lower():
			if appReg_spent:
				# _.pr('here')
				shouldAdd = False
			
			appReg_spent = True
		if shouldAdd:
			# _.pr(x)
			result+=x+'\n'
	# _.pr( result )
	# sys.exit()
	return result

def selfCodeClean( code ):
	code = code.replace( ' =', '=' )
	code = code.replace( '= ', '=' )
	code = code.replace( '=None', '' )
	code = code.replace( '=True', '' )
	code = code.replace( '=False', '' )
	code = code.replace( "=''", '' )
	code = code.replace( "='live'", '' )
	code = code.replace( ':', '' )
	code = code.replace( ':', '' )
	# code = code.split(',     ')[0]+' )'
	# code = code.replace( ') )', ')' )
	_.pr( code )

	return code

def process( record ):
	global matixFolder
	global file
	global parts
	global oc

	payload = []

	result = ''
	isOpen = False
	for i,line in enumerate(file):

		if i == record['start']-1:
			isOpen = True
		if isOpen and i >= record['start'] or isOpen and i <= record['end']:
			
			# result+=str(i)+' '
			# if not line.endswith('global appReg') and not not line.endswith('global appReg'):
			result+=line
		

		elif i > record['end']:
			isOpen = False
		if i == record['end']:
			isOpen = False
	
	# payload.append( '\n\n\n\n' )
	payload.append( '#'+oc['open'] )
	separator2 = '\n# ############################# ############################# \n'
	separator = '\n\n\t# ############################# \n\n'
	spentSections = []
	instantiateCode = """
		try:
			theParentItem
		except Exception as e:
			from _rightThumb._matrix import theParentItem
		return theParentItem.thisItem
	"""
	method = 2
	for pline in parts.split('\n'):
		if ';' in pline:
			p = pline.split(';')
			# _.pr( p )
			if not p[0] in spentSections:
				spentSections.append( p[0] )
				new = result
				new = injectFirstRow( findbase(p[0]), new )
				new = new.replace( 'REPLACE_THIS_0', p[0] )
				new = new.replace( 'REPLACE_THIS_1', p[0] )
				new = new.replace( 'REPLACE_THIS_2', p[0] )
				new = new.replace( '__'+p[0]+'__', p[0] )
				new = clean_appReg( new )

				if method == 2:
					parent = '_'+p[0]+'_parent'
					pNew = new.replace( '\tdef '+p[0], 'import _rightThumb._matrix as _matrix\nimport time\ndef '+p[0] ).replace( 'self,','' ).replace('  ',' ')
					pNew = pNew.replace( 'self.', '_matrix.app.' )
					pNew = pNew.replace( 'global appReg', 'appReg = _matrix.appReg' )

					_.saveText( pNew, matixFolder+_v.slash+parent+'.py' )
					selfCode = new.split('\n')[0].replace( 'def ', 'return self.' ).replace( 'self, ','' )
					selfCode = selfCodeClean( selfCode )
					iCode = instantiateCode.replace( 'theParentItem', parent ).replace( 'thisItem', selfCode.replace('return self.','').replace('\t','') )
					selfCode = selfCode.replace( 'return', '\n\t\treturn' )
					# selfCode = _str.replaceDuplicate(selfCode,' ')
					# selfCode = _str.cleanBE(selfCode,' ')

					newX = ''
					for i,x in enumerate(new.split('\n')):
						if not i:
							newX += x
							newX += iCode
					new = newX
					

				
				

				payload.append( '\n' )
				payload.append( separator2 )
				payload.append( '\n' )
				payload.append( new )
				payload.append( separator )

			if not p[1] in spentSections:
				spentSections.append( p[1] )
				new = result
				new = injectFirstRow( findbase(p[0]), new )
				new = new.replace( 'REPLACE_THIS_0', p[0] )
				new = new.replace( 'REPLACE_THIS_1', p[0] )
				new = new.replace( 'REPLACE_THIS_2', p[1] )
				new = new.replace( '__'+p[0]+'__', p[1] )
				new = clean_appReg( new )

				if method == 2:
					parent = '_'+p[0]+'_parent'
					pNew = new.replace( 'def '+p[0], 'class '+p[0] )
					# _.saveText( pNew, matixFolder+_v.slash+parent )
					# iCode = instantiateCode.replace( theParentItem, parent ).replace( thisItem, p[0] )
					newX = ''
					for i,x in enumerate(new.split('\n')):
						if not i:
							newX += x
							newX += selfCode
					new = newX

				payload.append( new )

			if p[2] in spentSections:
				payload.append( '\n' )
			if not p[2] in spentSections:
				payload.append( separator )
				spentSections.append( p[2] )
				new = result
				new = injectFirstRow( findbase(p[0]), new )
				new = new.replace( 'REPLACE_THIS_0', p[0] )
				new = new.replace( 'REPLACE_THIS_1', p[0] )
				new = new.replace( 'REPLACE_THIS_2', p[2] )
				new = new.replace( '__'+p[0]+'__', p[2] )
				new = clean_appReg( new )

				if method == 2:
					parent = '_'+p[0]+'_parent'
					pNew = new.replace( 'def '+p[0], 'class '+p[0] )
					# _.saveText( pNew, matixFolder+_v.slash+parent )
					# iCode = instantiateCode.replace( theParentItem, parent ).replace( thisItem, p[0] )
					newX = ''
					for i,x in enumerate(new.split('\n')):
						if not i:
							newX += x
							newX += selfCode
					new = newX


				payload.append( new )
				payload.append( '\n' )
			payload.append( separator2 )
		# payload.append( '\n\n\n' )
	payload.append( '\n\n\n\n' )
	temp = []
	for pline in parts.split('\n'):
		p = pline.split(';')
		temp.append({ 'data': "self.records['"+p[0]+"']" })
		
	_.fields.asset( 'project', temp )
	for pline in parts.split('\n'):
		p = pline.split(';')
		payload.append( '# \t\t'+  _.fields.value( 'project', 'data', "self.records['"+p[0]+"']" )  +" = {}\n"  )

	payload.append( '\n\n' )
	for pline in parts.split('\n'):
		p = pline.split(';')
		payload.append( '# '+  '_'+p[0]+'_child\n'  )



	temp = []
	for pline in parts.split('\n'):
		p = pline.split(';')
		temp.append({ 'data': "self.indexes['labels']['"+p[0]+"']" })

	_.fields.asset( 'project2', temp )
	payload.append( '\n\n' )
	for pline in parts.split('\n'):
		p = pline.split(';')
		payload.append( '# \t\t'+  _.fields.value( 'project2', 'data', "self.indexes['labels']['"+p[0]+"']" )  +" = []\n"  )
		# payload.append( '# \t\t'+  "self.indexes['labels']['"+p[0]+"']\n"  )

	payload.append( '\n\n' )
	payload.append( '#'+oc['close'] )



	# _.pr(result)
	# _.printVarSimple(record)
	# result
	return payload
	# _.pr(record['name'])
	# _.pr(record['start'])
	# _.pr(record['end'])
def action():
	global file
	global parts
	global data
	global oc
	load()

	for record in data:
		if 'REPLACE_THIS_' in record['name']:
			payload = process( record )


	result = ''

	for section in payload:
		result+=section
		# for line in section:
		#     _.pr( line )
	if _.switches.isActive('Save') and len(_.switches.value('Save')):
		_.saveText( result, _.switches.values('Save')[0] )
	elif not _.switches.isActive('Save'):
		_.pr( result )
	elif _.switches.isActive('Save') and not len(_.switches.value('Save')):
		global filename

		newFile = []
		isOpen = False
		for line in file:
			line = line.replace( '\n', '' )
			line = line.replace( '\r', '' )
			if oc['open'] in line:
				isOpen = True
				newFile.append( result )


			if not isOpen:
				newFile.append( line )


			if oc['close'] in line:
				isOpen = False


		_.saveText( '\n'.join(newFile), filename )
	# _.printVarSimple( data )



def load():
	global file
	global parts
	global data
	global filename
	global template
 
	parts = """
ext;e;external
nuc;n;nucleation
asyn;a;asynchronous
data;d;data
switch;s;switches
table;t;tables
db;db;database
program;p;programs
focus;f;focus
reg;r;registration
process;ps;processes
procedure;pr;procedures
task;tk;tasks
audit;adt;audit
"""

# ext;e;external
# asyn;a;asynchronous
# data;d;data
# switch;s;switches
# focus;f;focus
# process;ps;processes

# table;t;tables
# nuc;n;nucleation
# audit;adt;audit
# db;db;database
# reg;r;registration
# task;tk;tasks
# procedure;pr;procedures


	file = _.getText( filename )
	_func.switch( 'Files', filename )
	data = _func.do( 'action' )

parts = ''
file = ''
data = []
filename = 'D:\\tech\\programs\\python\\_rightThumb\\_matrix\\__init__.py'
template = 'D:\\tech\\programs\\python\\_rightThumb\\_matrix\\template.py'

matixFolder = 'D:\\tech\\programs\\python\\_rightThumb\\_matrix'
oc = {
		'open': '7F21BD8F', 
		'close': 'E61F59D5', 
}


# asyn
# data
# audit
# switch
# table
# db
# ext
# reg
# process
# procedure
# task

# a asyn asynchronous thread

# a
# d
# adt
# s
# t
# db
# e
# r
# ps
# pr
# tk



########################################################################################
if __name__ == '__main__':
	action()