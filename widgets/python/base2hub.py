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

import os, sys, time
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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Add-app.-FN', '-fn' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'base2hub.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'convert python app to github rightthumb system',
	'categories': [
						'github',
						'convert',
						'rightthumb',
						'rt',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
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
						_.hp('p base2hub -f _switches.py -fn | p countEach'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
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

def replace_text(data):
	global file

	while '\n\n\n' in file:
		file = file.replace( '\n\n\n', '\n' )

	data = _str.cleanBE(data,' ')
	data = _str.cleanBE(data,'\t')
	data = _str.cleanBE(data,'\n')
	data = _str.cleanBE(data,' ')

	parts = data.split( '\n\n' )

	for part in parts:
		prt = part.split('\n')
		# _.pr(prt)
		if prt[0] and len(prt) > 1:
			prt[0] = _str.cleanBE(prt[0],' ')
			prt[1] = _str.cleanBE(prt[1],' ')
			file = file.replace( prt[0], prt[1] )



def convert_class_variables( subject, replace, *items ):
	global file
	# _.pr(file)
	for item in items:
		sub = subject+item
		# _.pr(sub)
		index = _.find_all( file, sub )
		index.reverse()
		# _.pr(index)

		for i in index:
			new = ''
			activeA=False
			activeB=False
			for ii, ch in enumerate(file):
				if ii == i:
					activeA = True
					activeB = True
					new += replace
				if activeB and ch == ')':
					new += ').'+item
					activeB=False
				elif not activeA:
					new += ch
				if ii == i+len(sub):
					new += ch
					activeA=False


			file = new



def convert_class_functions( subject, replace ):
	global file
	# _.pr(file)
	sub = subject
	# _.pr(sub)
	index = _.find_all( file, sub )
	index.reverse()
	# _.pr(index)

	for i in index:
		new = ''
		activeA=False
		activeB=False
		for ii, ch in enumerate(file):
			if ii == i:
				activeA = True
				activeB = True
				new += replace
				iii=ii-1
				done=False
				while not done:
					pass
					##############################################

			if activeB and ch == ')':
				new += ').'+item+'('
				##############################################
				activeB=False
			elif not activeA:
				new += ch
			if ii == i+len(sub):
				new += ch
				activeA=False
				

		file = new

def add_app_to_fn():
	global file
	spent=[]
	index = _.find_all( file, '(' )
	fns = _.find_all( file, 'def ' )
	index.reverse()
	for i in index:
		done=False
		ii = i
		function=[]
		while not done:
			ii-=1
			if not file[ii] in '._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
				done=True
			elif not file[ii] == ' ':
				function.append(file[ii])
		pass
		if not '.' in function:
			# test = ii-len('def ')
			# _.pr(test)
			# _.pr(fns)
			if not ii-len('def ')+1 in fns:
				function.reverse()
				fn = ''.join(function)
				if fn and not fn in ['childScript','__import__','abs','all','any','ascii','bin','bool','breakpoint','bytearray','bytes','callable','chr','classmethod','compile','complex','delattr','dict','dir','divmod','enumerate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','print','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','tuple','type','vars','zip']:
					if not fn in spent:
						spent.append(fn)
						_.pr(fn)
					# _.pr(fn,function)
					new=''
					for i,ch in enumerate(file):
						if i == ii+1:
							new+='app.'
						new+=ch
					file = new
		pass
		# sys.exit()
	pass


def remove_text(data):
	global file
	data = _str.cleanBE(data,' ')
	data = _str.cleanBE(data,'\t')
	data = _str.cleanBE(data,'\n')
	data = _str.cleanBE(data,' ')

	parts = data.split( '\n' )
	new=''
	for i,line in enumerate(file.split('\n')):
		add=True
		for part in parts:
			part = _str.cleanBE(part,' ')
			part = _str.cleanBE(part,'\t')
			# _.pr(i,'part',part.lower() in line.lower(),part,line)
			if part and part.lower() in line.lower():
				add=False
		if add:
			new+=line+'\n'
	file=new

def process(path):
	global file
	file = _.getText( path, raw=True )
	if 'def appSwitches()' in file:
		file = '''#!/usr/bin/python3
import sys
from _rightThumb._hub import _construct as __
from _rightThumb._hub import app
from _rightThumb._hub import _vars as _v
from _rightThumb._hub import _func as _
reg = app.space(__name__, __file__)
app.reg = reg

def appSwitches()'''+file.split('def appSwitches()')[1]

	replace_text('''
_.appInfo[focus()]
reg.documentation

_.appData[focus()]
reg.data

__.thisApp
app.this_app

_.hp(
app.hp(
''')
	pass
	file = file.replace('def appSwitches():','''
reg.rent = app.register(reg)\n__.rent=reg.rent
app.rent = app.focus(reg.rent)
app.switches()
# app.tables()


def appSwitches():
''')
	pass
	replace_text('''
appSwitches()
app_switches()

_.switches.register
app.switch.reg

registerSwitches
sw

_.load()
app.load()

__.constructRegistration
app.construct_registration

_.argvProcess
app.argv_process

registerSwitches()
sw()

fieldSet(
field_set(

theFocus
rent

_.setPipeData
app.set_pipe_data

_.postLoad
app.post_load

__.isExit()
__.isExit(diagram=False)
''')
	pass
	
	# convert_class_variables( '_.switches.', 'app.switch.', 'values','value' )

	replace_text('''
_.switches.
app.switch.

__.
app.

_.
app.

colorThis(
cp(

app.appReg
app.rent

os.sep
app.sep

app.startTime
app.start_time

if not app.appReg == appDBA and appDBA in app.appReg:
if True:

if not app.rent == appDBA and appDBA in app.rent:
if True:

app.appInfo[app.appReg]
reg.documentation

app.appInfo[app.rent]
reg.documentation

app.defaultScriptTriggers()
app.default_script_triggers()

app.appData[app.rent]['pipe']
reg.data['pipe']

app.fields.
app.field.

_.switches.isActive
app.switch.isActive

switches.isActive
app.switch.isActive

colorThis
color_this

payloadCache
payload_cache

app.tables.
app.table.

focus()
reg.rent

app.switch.process()
app.switch.process(arg=True)

appReg
rent

''')
	pass

	replace_text('''


app.find_all
_.find_all

app.find_all_do
_.find_all_do

app.reFormatSize
_.reFormatSize

app.formatSize
_.formatSize

app.unFormatSize
_.unFormatSize

app.timeAgo
_.timeAgo

app.timeAgo_past
_.timeAgo_past

app.timeFuture
_.timeFuture

app.formatPhone00
_.formatPhone00

app.formatPhone1
_.formatPhone1

app.formatPhone2
_.formatPhone2

app.formatColumns_OLD
_.formatColumns_OLD

app.formatColumnsSort
_.formatColumnsSort

app.formatColumnsSortOld
_.formatColumnsSortOld

app.isDate
_.isDate

app.daysDiff
_.daysDiff

app.friendlyDate
_.friendlyDate

app.autoDate
_.autoDate

app.friendlyDate2
_.friendlyDate2

app.onlyNumbers_strip
_.onlyNumbers_strip

app.friendlyDateTouch
_.friendlyDateTouch

app.fileDate
_.fileDate

app.dateAdd2
_.dateAdd2

app.printBold
_.printBold

app.resolveEpochTest
_.resolveEpochTest

app.dateMathEpoch
_.dateMathEpoch

app.txt2Date
_.txt2Date

app.stamp2Date
_.stamp2Date

app.float2Date
_.float2Date

app.float2Date2
_.float2Date2

app.float2Date
3_.float2Date3

app.float2Date3B
_.float2Date3B

app.dateDiff
_.dateDiff

app.dateDiffX
_.dateDiffX

app.dateSub
_.dateSub

app.date2epoch
_.date2epoch

app.validateEmail
_.validateEmail

app.figureOutDate
_.figureOutDate

app.def test
_.def test

app.getMonthData
_.getMonthData

app.getText
_.getText

app.updateLine
_.updateLine

app.linePrint
_.linePrint

app.dateDiffDic
_.dateDiffDic

app.days_in_month
_.days_in_month

app.isLeapYear
_.isLeapYear

app.getTableDB
_.getTableDB

app.monthMath
_.monthMath

app.monthsDiff
_.monthsDiff

app.woy2dates
_.woy2dates

app.days_math
_.days_math

app.woy2datesFriendly
_.woy2datesFriendly

app.dateDiffText
_.dateDiffText

app.getWOY
_.getWOY

app.getYearFromEpoch
_.getYearFromEpoch

app.getWOYFromEpoch
_.getWOYFromEpoch


''')

	remove_text('''
if not app.rent == appDBA and appDBA in app.rent:
app.appInfo[app.appReg] = app.appInfo[appDBA]
appDBA in app.rent
reg.documentation = app.appInfo[appDBA]
app.appData[app.rent] = app.appData[appDBA]
reg.documentation = app.appInfo[appDBA]
app.appInfo[appDBA]
__.appReg_bk

''')

	pass
	if _.switches.isActive('Add-app.-FN'):
		add_app_to_fn()

#     replace_text('''

# _app.
# app.

# ''')

	return file



def action():
	for i,path in enumerate( _.isData(r=1) ):
		f = process(path)
		# _.pr(f)
		_.saveText( f, path )
		_.cp( path, 'green' )

file = ''

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







