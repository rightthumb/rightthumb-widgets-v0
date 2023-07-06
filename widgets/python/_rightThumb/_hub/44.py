

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

#!/usr/bin/python3
from _rightThumb._hub import _construct as __
from _rightThumb._hub import _vars as _v
from _rightThumb._hub import _string as _str
import time
class d:
	def __init__( self ):
		pass
class dot:
	def __init__( self ):
		pass

class space:
	def __init__( self, *values ):
		pass

import platform
v = d()
if platform.system() == 'Windows':
	sep='\\'
else:
	sep='\\'
field=None
stack=None
myFileLocations=[]
myFolderLocations=[]
def doc_default( *values ):
	# placeholder
	print( 'error: before usinh this, __.documentation()' )
	sys.exit()

def switch( *values ):
	# placeholder
	print( 'error: before usinh this, __.switches()' )
	sys.exit()

def table( *values ):
	# placeholder
	print( 'error: before usinh this, __.tables()' )
	sys.exit()

# class fields:
#     # placeholder
#     def __init__( *values ):
#         print( 'error: before usinh this, __.fields()' )
#         sys.exit()
#     def register( *values ):
#         print( 'error: before usinh this, __.fields()' )
#         sys.exit()



class ColorBold:
	gray = '\033[1;30;40m'
	red = '\033[1;31;40m'
	green = '\033[1;32;40m'
	yellow = '\033[1;33;40m'
	blue = '\033[1;34;40m'
	magenta = '\033[1;35;40m'
	cyan = '\033[1;36;40m'
	white = '\033[1;37;40m'
	underline = '\033[4m'
	end = '\033[0m'


class Color:
	purple = '\033[95m'
	cyan = '\033[96m'
	darkcyan = '\033[36m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	end = '\033[0m'


class Background:
	red = '\033[1;37;41m'
	green = '\033[1;37;42m'
	yellow = '\033[1;37;43m'
	blue = '\033[1;37;44m'
	purple = '\033[1;37;45m'
	light_blue = '\033[1;37;46m'
	grey = '\033[1;37;47m'
	black = '\033[1;37;48m'
	end = '\033[0m'

class BackgroundGrey:
	black = '\033[0;30;47m'
	red = '\033[0;31;47m'
	green = '\033[0;32;47m'
	brown = '\033[0;33;47m'
	blue = '\033[0;34;47m'
	magenta = '\033[0;35;47m'
	cyan = '\033[0;36;47m'
	gray = '\033[0;37;40m'
	end = '\033[0m'
	
class BackgroundGreyBold:
	black = '\033[1;30;47m'
	red = '\033[1;31;47m'
	green = '\033[1;32;47m'
	brown = '\033[1;33;47m'
	blue = '\033[1;34;47m'
	magenta = '\033[1;35;47m'
	cyan = '\033[1;36;47m'
	gray = '\033[1;37;40m'
	end = '\033[0m'
	

row_colors = []

row_colors.append([ 0, Background.blue ])
row_colors.append([ 0, Background.light_blue ])
row_colors.append([ 0, Background.purple ])

row_colors.append([ 1, BackgroundGrey.red ])
row_colors.append([ 1, BackgroundGrey.brown ])
row_colors.append([ 1, BackgroundGrey.blue ])

row_colors.append([ 2, Color.cyan ])
row_colors.append([ 2, Color.green ])

row_colors_ID = 0

colorHelp_colorList = [
	"ColorBold.gray",
	"ColorBold.red",
	"ColorBold.green",
	"ColorBold.yellow",
	"ColorBold.blue",
	"ColorBold.magenta",
	"ColorBold.cyan",
	"ColorBold.white",

	"",

	"Color.purple",
	"Color.cyan",
	"Color.darkcyan",
	"Color.blue",
	"Color.green",
	"Color.yellow",
	"Color.red",
	"Color.bold",
	
	"",

	"Background.red",
	"Background.green",
	"Background.yellow",
	"Background.blue",
	"Background.purple",
	"Background.light_blue",
	"Background.grey",
	"Background.black",

	"",

	"BackgroundGrey.black",
	"BackgroundGrey.red",
	"BackgroundGrey.green",
	"BackgroundGrey.brown",
	"BackgroundGrey.blue",
	"BackgroundGrey.magenta",
	"BackgroundGrey.cyan",
	"BackgroundGrey.gray",

	"",

	"BackgroundGreyBold.black",
	"BackgroundGreyBold.red",
	"BackgroundGreyBold.green",
	"BackgroundGreyBold.blue",
	"BackgroundGreyBold.magenta",
	"BackgroundGreyBold.cyan",
	"BackgroundGreyBold.gray"
]

doc=d()
doc.info = doc_default
doc.frame = doc_default

import sys
from _rightThumb._hub import _construct as __

try:
	start_time
except Exception as e:
	start_time = time.time()
__.argv=sys.argv
def sim(*values):
	__.argv = []
	for val in values:
		for v in val.split(' '):
			__.argv.append(v)
	print(__.argv)

def app(subject):
	pass

def architecture(*values):
	__.architecture()
	return True
def documentation():
	from inspect import currentframe, getframeinfo
	doc.info=getframeinfo
	doc.frame=currentframe
	

	
def switches():
	global switch
	from _rightThumb._hub import _switches
	switch = _switches.Subject()

def tables():
	global table
	from _rightThumb._hub import _tables
	table = _tables.Subject()

def fields():
	global field
	from _rightThumb._hub import _fields
	field = _fields.Subject()

def debug():
	global stack
	from _rightThumb._hub import _stack
	stack = _stack.Subject()




arch = architecture
def clearFocus( name, file ):
	global sep
	f = file.split(sep)
	if name == '__main__':
		x = '__' + f[len(f)-1].replace('.py','') + '__'
	else:
		x = f[len(f)-1].replace('.py','')
	return x

def this_app( file ):
	global sep
	f = file.split(sep)
	x = f[len(f)-1].replace('.py','')
	return x

argvProcess=False

registeredAppsAll=[]
def default_script_triggers():
	global defaultScriptTriggers_run
	defaultScriptTriggers_run = True

default_script_triggers_run = False
def default_script_triggers_do():
	global default_script_triggers_run
	if default_script_triggers_run:
		return None
		# if len(appInfo[__.rent_bk]['columns']) > 0:

		#     switch.trigger('Column',formatColumns)
		#     switch.trigger('Sort',formatColumnsSort)
		#     switch.trigger('GroupBy',formatColumns)
		# switch.trigger('PlusClose',plusCloseClean)
		# switch.trigger('Ago',timeAgo)
		# switch.trigger('PrintEpoch',print_epoch_trigger)
		# # switch.trigger('Aggregate',aggregate_trigger)
		# switch.postScripts.append( aggregate_trigger )
############################################################## copy-fn-class
def url_trigger(url):
	if not '.' in url:
		url = 'http://' + url + '.com'
	elif not url.startswith('http'):
		url = 'http://' + url
	return url
def time_ago( do='', startDate=None ):

	try:
		do = float(do)
		return do
	except Exception as e:
		pass

	global timeAgoBase
	global timeAgoBaseCount
	if not len(timeAgoBase) and timeAgoBaseCount == 0:
		if ',' in do:
			timeAgoBase = do.split(',')
			# print(do)
			# sys.exit()
	timeAgoBaseCount += 1
	# print( do, time_agof(startDate) )
	if len(do) == 19 and do.count('-') == 2 and do.count(':') == 2:
		return time_agoa( do )
	if len(do) == 16 and do.count('-') == 2 and do.count(':') == 1:
		return time_agoa( do )
	if len(do) == 21 and do.count('-') == 4:
		result = []
		for x in do.split(','):
			result.append( time_agot( x, startDate ) )
		return result
	if len(do) == 10 and do.count('-') == 2:
		ts = time_agoa( do )
	else:
		if not do.startswith('+'):
			ts = time_agot(do,startDate)
		elif do.startswith('+'):
			ts = time_agot(do,startDate)
	if len(timeAgoBase) > 1 and do == timeAgoBase[1]:
		if timeAgoBaseCount == 3 or timeAgoBaseCount == 5 :
			pass
			ts += 86400-1
	# print( timeAgoBaseCount, ts )
	return ts
def time_future(do='', startDate=None):
	if startDate is None:
		startDate = time.time()
	global isTime

	if '.' in do:
		dos = do.split('.')
		e = time_futuret( dos[0], startDate )
		# return e
		for di,ds in enumerate(dos):
			if di:
				e = time_futuret( dos[di], e )
		return e
	if do.startswith('+'):
		do = do[1:]
	if do is None:
		time_futurec( '\t Error: Ago is Missing parameters', 'red' )
		sys.exit()
	if type(do) == float:
		return do
	if do.lower() == 'r':
		return 'resent'
	if 're' in do.lower():
		return 'resent'
	if 'a' in do.lower():
		return 'a'
	if 'cd' in do:
		return do.lower()
	if 'md' in do:
		return do.lower()
	if 'mod' in do.lower():
		return 'md'
	if 'crea' in do.lower():
		return 'cd'
	if 'o' in do.lower():
		return 'one'

	if len(do) == 0:
		do = switch.values('Ago')[0]
	do = do.lower()

	if 't' in do:
		one = time_futurer( startDate )
		two = time_futurea( one.split(' ')[0] )
		return two
	if 'mm' in do or 'min' in do:
		each = 60
		units = do
		units = units.replace( 'min', '' )
		units = units.replace( 'm', '' )
		units = int( units )
		remove = units * each
		return startDate + remove  
	if isTime:
		if 'm' in do:
			each = 60
			units = do
			units = units.replace( 'm', '' )
			units = int( units )
			remove = units * each
			return startDate + remove  

	if 'h' in do:
		each = 3600
		units = do
		units = units.replace( 'h', '' )
		units = int( units )
		remove = units * each
		return startDate + remove  
	if 's' in do:
		units = do
		units = units.replace( 's', '' )
		units = int( units )
		return startDate + units
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
		# start_date = time_futured( startDate, 365 * nmb, '+' )
		# start_date = time_futured( startDate, 365 * nmb, '+' )
		start_date = time_futurey( startDate, nmb, do='+' )
	if 'm' in do:
		# start_date = time_futured( startDate, 30 * nmb, '+' )
		start_date = time_futurem( startDate, nmb, do='+' )
	if 'w' in do:
		start_date = time_futured( startDate, 7 * nmb, '+' )
	if 'd' in do:
		start_date = time_futured( startDate, nmb, '+' )
	return start_date
def date_math_epoch( epoch, theDays, do='+' ):
	# print(epoch, theDays)
	epoch = date_math_epocha(epoch)
	# if do == '+':
	#   return epoch + ( theDays*86400 )
	# elif do == '-':
	#   return epoch - ( theDays*86400 )
	date0 = datetime.datetime.fromtimestamp((epoch))
	if do == '+':
		date1 = date0 + datetime.timedelta(days=theDays)
	elif do == '-':
		date1 = date0 - datetime.timedelta(days=theDays)
	else:
		print( "date_math_epochd( epoch, theDays, do='+' )" )
		sys.exit()
	# print(date1.timestamp())
	return date_math_epocha((date1.timestamp()))
def auto_date( theDate ):
	# if type(theDate) == float or type(theDate) == int:
	#   return theDate
	import _rightThumb._date as _date
	return _date.autoDate( theDate )
def month_math( thisDate, months, do='+' ):
	months = abs(months)
	# print( '040', thisDate, month_matha( thisDate ), month_mathf(thisDate) )
	theDateParts = month_mathf( month_matha( thisDate ) ).split(' ')
	theDate = theDateParts[0]
	parts = theDate.split('-')
	parts[0] = int(parts[0])
	parts[1] = int(parts[1])
	parts[2] = int(parts[2])
	i = 0
	while not i == months:
		# print( months, 1, parts )
		if do == '+':
			parts[1]+=1
			if parts[1] == 13:
				parts[1] = 1
				parts[0] += 1
		elif do == '-':
			parts[1]-=1
			if parts[1] == 0:
				parts[1] = 12
				parts[0] -= 1
		i+=1
	# print( '048a' )
	bb = str(parts[1])
	cc = str(parts[2])
	# print( '048b' )
	if parts[1] < 10:
		bb = '0'+bb
	if parts[2] < 10:
		cc = '0'+cc
	# print( '048c' )
	text = str(parts[0])+'-'+bb+'-'+cc +' '+ theDateParts[1]
	# print( '049', text )
	result = month_matha(  text  )
	# print( '050a', text, type( result ) )
	while type( result ) == bool:

		parts[2]-=1

		bb = str(parts[1])
		cc = str(parts[2])
		if parts[1] < 10:
			bb = '0'+bb
		if parts[2] < 10:
			cc = '0'+cc
		text = str(parts[0])+'-'+bb+'-'+cc +' '+ theDateParts[1]
		result = month_matha(  text  )
		# print( '050b', text, type( result ) )

	# print( '050c', text )
	# print( '060', result )
	return result
def friendlyDate( theDate ):
	import _rightThumb._date as _date
	return _date.friendlyDate( theDate )
def year_math( thisDate, years, do='+' ):
	theDateParts = year_mathf( year_matha( thisDate ) ).split(' ')
	theDate = theDateParts[0]
	parts = theDate.split('-')
	parts[0] = int(parts[0])
	i = 0
	while not i == years:
		if do == '+':
			parts[0] += 1
		elif do == '-':
			parts[0] -= 1
		i+=1
				

	return year_matha(  str(parts[0])+'-'+parts[1]+'-'+parts[2] +' '+ theDateParts[1] )
def resolve_epoch_test( theDate, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	import _rightThumb._date as _date
	return _date.resolveEpoch( theDate, test, showPrint, showPrintTry, onlyEpoch, delim, falseBlank )
def color_this( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False, simpleDic=False, colorProfile=None,      p=None, c=None, sd=None, isError=False ):

	if isError:
		color = 'red'

	if not c is None:
		color = c
	if not sd is None:
		simpleDic = sd

	if not p is None:
		shouldPrint = p

	if simpleDic and type(strings) == dict:
		newString = ''
		for k in strings.keys():
			newString += ' ' + k + ': ' + str(strings[k]) + ' '
		strings = newString

	if simpleDic and type(strings) == list:
		for i,thisItem in enumerate(strings):
			if type(thisItem) == dict:
				newString = ''
				for k in thisItem.keys():
					newString += ' ' + k + ': ' + str(thisItem[k]) + ' '
				strings[i] = newString

# [ { 'color': 'red', 'field': 'match', 'i': 0  } ]
# [ { 'color': 'red', 'field': 'match' } ]
# [ { 'color': 'red', 'i': 0  } ]
# { 'color': 'red', 'i': 0  }
# ['red',1]
# [2,'red']
# ['name','yellow']
# 'red,green'
# 'red,green:*'
# '*red,green'
# 'green,red,green:*'
# 'green:2,red:*,green'

# topic_index
#   'float,2'
# ColorBold Color Background BackgroundGrey BackgroundGreyBold

	
	# color_index = color_thisg()
	# colorProfileTmp = []
	# index = {
	#             'i': [],
	#             'keys': [],
	#             'data': {},
	# }
	# if not colorProfile is None:
	#     if type(colorProfile) == str:
	#         if type(strings) == list and ',' in colorProfile:
	#             if colorProfile.count('*') > 1:
	#                 print( ' only 1 * ' )
	#             new_CP = []
	#             cp = colorProfile.split(',')
	#             end = len(strings)-1
	#             leftC = len(cp)-1
	#             leftL = end
	#             for i,xx in enumerate(strings):

	#     if type(colorProfile) == list:
	#         for i,record in enumerate(colorProfile):
	#             if type(record) == dict:
	#                 record['id'] = i
	#                 if 'c' in record.keys():
	#                     record['color'] = record['c']
	#                     del record['c']

	#                 if 'f' in record.keys():
	#                     record['field'] = record['f']
	#                     del record['f']

	#                 if 'column' in record.keys():
	#                     record['field'] = record['column']
	#                     del record['column']
	#                 if 'i' in record.keys():
	#                     index['i'].append( record['i'] )
	#                     index['data'][i] = record
					
	#                 if 'field' in record.keys():
	#                     if ',' in record['field']:
	#                         for ef in record['field'].split(','):
	#                             index['keys'].append( ef )
	#                             index['data'][ ef ] = record
	#                     else:
	#                         index['keys'].append( record['field'] )
	#                         index['data'][record['field']] = record
	#                 colorProfileTmp.append( record )
					
	#             if type(record) == list:
	#                 if len(record) == 2:
	#                     newRecord = { 'id': i }
	#                     if type( record[0] ) == int:
	#                         newRecord['i'] = record[0]
	#                         newRecord['color'] = record[1]

	#                     elif type( record[1] ) == int:
	#                         newRecord['i'] = record[1]
	#                         newRecord['color'] = record[0]
	#                     else:
	#                         if record[0].lower() in color_index:
	#                             newRecord['field'] = record[0]
	#                             newRecord['color'] = record[1]
	#                         if record[1].lower() in color_index:
	#                             newRecord['field'] = record[1]
	#                             newRecord['color'] = record[0]

	#                     if 'color' in newnewRecord.keys():

	#                         if 'i' in newRecord.keys():
	#                             index['i'].append( newRecord['i'] )
	#                             index['data'][i] = newRecord
							
	#                         if 'field' in newRecord.keys():
	#                             if ',' in newRecord['field']:
	#                                 for ef in newRecord['field'].split(','):
	#                                     index['keys'].append( ef )
	#                                     index['data'][ ef ] = newRecord
	#                             else:
	#                                 index['keys'].append( newRecord['field'] )
	#                                 index['data'][newRecord['field']] = newRecord
	#                         colorProfileTmp.append( newRecord )

	#     if type(colorProfile) == dict:
	#         record = colorProfile
	#         if 'c' in record.keys():
	#             colorProfile[i]['color'] = record['c']
	#             record['color'] = record['c']
	#         if 'f' in record.keys():
	#             colorProfile[i]['field'] = record['f']
	#             record['field'] = record['f']
	#         if 'column' in record.keys():
	#             colorProfile[i]['field'] = record['column']
	#             record['field'] = record['column']
	#         if 'i' in record.keys():
	#             index['i'].append( record['i'] )
			
	#         if 'field' in record.keys():
	#             index['keys'].append( record['field'] )
	#         colorProfile = [record]
	if type(strings) == list:

		for i,x in enumerate(strings):

			strings[i] = str( x )

		string = ' '.join( strings )
	else:
		string = str(strings)

	global switch
	if switch.isActive( 'NoColor' ):
		if shouldPrint:
			print(string)
			return string
		else:
			return string

	if ipsum:
		string = color_thisi()

	found = False

	if color == 'help':
		print()
		print()
		print( "__.cp( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False )" )
		print()
		print()
		color_this( ipsum )
	if '.' in color:

		try:
			result = eval( color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True

	else:
		color = color.lower()
	if not found and notBold:
		try:
			result = eval( 'Color.' + color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True
	if not found:
		try:
			result = eval( 'ColorBold.' + color + '+ string + ColorBold.end')
		except Exception as e:
			pass
		else:
			found = True
	if not found:
		try:
			result = eval( 'Color.' + color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True
	if not found:
		try:
			result = eval( 'Background.' + color + '+ string + Background.end')
		except Exception as e:
			pass
		else:
			found = True
	if not found:
		try:
			result = eval( 'BackgroundGrey.' + color + '+ string + BackgroundGrey.end')
		except Exception as e:
			pass
		else:
			found = True
	if not found:
		try:
			result = eval( 'BackgroundGreyBold.' + color + '+ string + BackgroundGreyBold.end')
		except Exception as e:
			pass
		else:
			found = True

	if not found:
		color_this( 'Error: app.colorThis: color not found ' + str(color), 'red' )
		print()
		print( strings )
		print()
		color_this( ipsum )

		sys.exit()

	if shouldPrint:
		try:
			print( result )
		except Exception as e:

			try:
				result = str(result,'utf-8')
			except Exception as e:
				try:
					result = str(result,'iso-8859-1')
				except Exception as e:
					result = result.encode('utf-8')
			result = str(result,'iso-8859-1')
		if isError:
			sys.exit()
		return None

	return result
def color_help( ipsum=False ):
	global colorHelp_colorList
	for sample in colorHelp_colorList:
		if not len( sample ):
			print()
		else:
			result = eval( sample + '+ "THE_TEXT" + Color.end' )
			if ipsum:
				result = result.replace( 'THE_TEXT', color_helpi() )
			else:
				result = result.replace( 'THE_TEXT', sample )
			
			print( result )
	sys.exit()
def ipsum_sentence():
	global ipsum
	if ipsum is None:
		ipsum = ipsum_sentenceg( _v.ipsum, raw=True, clean=2 )
	ipsum = ipsum.replace( '\n', ' ' )
	sentences = []
	for sentence in ipsum.split('.'):
		sentence = _str.replaceDuplicate( sentence, ' ' )
		sentence = _str.cleanBE( sentence, ' ' )
		sentence = sentence + '.'
		sentences.append({ 'sentence': sentence, 'sortBy': ipsum_sentenceg() })

	randomized = tables.returnSorted( 'data', 'd.sortBy', sentences )
	return randomized[0]['sentence']
def genUUID( project='', label='', uniqueTimestamp=False ):
	global appData
	global appInfo
	uuid = __.imp('uuid')
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	try:
		type(appData[__.rent]['uuid'])
		good = True
	except Exception as e:
		good = False
	if good:

		try:
			timestamp = appData[__.rent]['start']
		except Exception as e:
			timestamp = time.time()

		if not project == '' or not label == '':
			if type(appData[__.rent]['uuid']) == str:
				# print()
				# print( '__.rent', __.rent )
				# print()
				# print(genUUIDd( appData ))
				# print()
				appData[__.rent]['uuid'] = {}
				# print(appInfo[__.rent]['file'])
				# sys.exit()
				appData[__.rent]['uuid']['app'] = appInfo[__.rent]['file']

			if not type(appData[__.rent]['uuid']) == str:
				
				appData[__.rent]['uuid']['uuid'] = string
				appData[__.rent]['uuid']['timestamp'] = timestamp
				appData[__.rent]['uuid']['project'] = ''
				appData[__.rent]['uuid']['label'] = ''

				if uniqueTimestamp:
					appData[__.rent]['uuid']['timestamp'] = time.time()

				if not project == '':
					appData[__.rent]['uuid']['project'] = project

				if not label == '':
					appData[__.rent]['uuid']['label'] = label
					
				uuidLog = genUUIDg('uuid_log.json')
				uuidLog.append(appData[__.rent]['uuid'])
				genUUIDs(uuidLog,'uuid_log.json',printThis=False)
			# appData[__.rent]['uuid'] = { 'uuid': theID, 'timestamp': time.time(), 'project': theProject, 'app': 'guid' }
	return string
def save_table( rows, theFile, tableTemp=False, printThis=True, indentCode=True, sort_keys=False, archive=False,                k=0,s=0,tmp=None,here=None,h=None,    p=1, me=0   ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')
	if not h is None: here = True;
	if not here is None: save_tables( rows, theFile ); return None;
	if not tmp is None: tableTemp = True;
	if k or s: sort_keys = True;
	if not p: printThis = False;
		

	
	# defaults to myTables
	px = ''
	if theFile.startswith('temp'+_v.slash):
		theFile = theFile.replace( 'temp'+_v.slash, '' )
		file0 = _v.stmp + _v.slash + theFile
		px = file0
	else:
		if not tableTemp:
			file0 = _v.myTables + _v.slash + theFile
			px = theFile
		else:
			file0 = _v.stmp + _v.slash + theFile
			px = file0

	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys)
	else:
		dataDump = simplejson.dumps(rows)
	
	if archive:
		import _rightThumb._md5 as _md5

		theFileLabel = theFile
		if _v.slash in theFileLabel:
			global appInfo
			tfl = theFileLabel.split(_v.slash)
			tfl.reverse()
			theFileLabel = str(appInfo[__.rent]['liveAppName']) + '__' + tfl[0]
		theFileLabel = theFileLabel.replace( '.json', '' )
		theFileLabel = theFileLabel.replace( '.JSON', '' )

		lastMD5 = None
		if os.path.isfile( file0 ):
			lastMD5 = _md5.md5File( file0 )

			backupFile = _v.stmp + _v.slash+'__archive_temp__' + theFileLabel + '__' + save_tableg() + '.json'
			

	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(theFile)

	if archive:
		shouldDocument = False

		if os.path.isfile( file0 ):
			thisMD5 = _md5.md5File( file0 )
		if lastMD5 is None:
			shouldDocument = True
		else:
			if not lastMD5 == thisMD5:
				shouldDocument = True

		if not shouldDocument:
			if os.path.isfile( backupFile ):
				os.remove( backupFile )
		
		if shouldDocument:
			md5Table = save_tableg( 'table_archive_log.json' )
			found = False
			for i,record in enumerate(md5Table):
				if theFileLabel == record['name']:
					found = True

			theFileLabel
			theFile
			save_tablef( theData )
	if printThis:
		save_tablep('Saved: ' + px, 'blue')
	if me and theFile in v.opened_file_me: save_tablec( theFile, v.opened_file_me[theFile] );
	return file0
def change_m( path, stampM, stampA=None, meta=False, p=0 ):
	if p:
		mn = ''
		if change_mt(stampM) == 'today':
			mn = ', '+str(int((time.time() - stampM) /60)) + ' min'
			if mn == '0 min':
				mn = ', just now'
		print( change_mf(stampM), change_mc( [change_mt(stampM)+ mn], 'yellow', p=0 ), path )
	if stampA is None:
		stampA = stampM
	# print(stampM)
	# print(stampA)
	global changeDate_Table
	global _dir
	global touch_meta

	if _dir is None:
		import _rightThumb._dir as _dir

	if meta:
		touch_meta = change_mg( 'touch.meta' )
		if not path in touch_meta:
			touch_meta[path] = {}
		if not 'epoch' in touch_meta[path]:
			touch_meta[path]['epoch'] = {}
		touch_meta[path]['epoch']['me'] = stampM
		touch_meta[path]['epoch']['ae'] = stampA
		change_ms( touch_meta, 'touch.meta', p=0 )

	if not meta:
		if changeDate_Table is None:
			changeDate_Table = change_mg( 'touch.index' )
		try:
			path = os.path.abspath(path)
		except Exception as e:
			pass
		if os.path.isfile(path):
			if not path in changeDate_Table:
				changeDate_Table[path] = _dir.info(path)
				change_ms( changeDate_Table, 'touch.index', p=0 )
			try:
				os.utime(path,(stampA, stampM))
			except Exception as e:
				pass
def get_table( theFile, tableTemp=False,      isDic=None, isList=None,      tmp=None ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	# defaults to myTables
	if not type( tableTemp ) == bool:
		if tableTemp == 'split':
			file0 = _v.myTables + _v.slash+'tablesets'+_v.slash + theFile
	else:
		if tableTemp == True:
			file0 = _v.stmp + _v.slash + theFile
		else:
			file0 = _v.myTables + _v.slash + theFile
	if not os.path.isfile(file0):
		file0 = theFile
	if os.path.isfile(file0):
		# print( 'theFile', theFile )
		# print( 'file0', file0 )
		# import bigjson
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
		return json_data
		# with open( file0, 'rb' ) as f:
			# json_data = bigjson.load(f)
			# json_data = bigjson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
	else:
		return __.data_default(file=theFile,default=[]).default()
def time_diff(epoch):
	return time_diffd( epoch )
	global _dir
	if _dir is None:
		import _rightThumb._dir as _dir
	return _dir.time_diff(time_diffa(epoch))
def date_diff_text( theDate, epoch=None ):

	y=0
	m=0
	w=0

	theDate = date_diff_texta( theDate )
	if epoch is None:
		epoch = time.time()
	# woy = date_diff_textg( theDate )
	days = abs(date_diff_textd( theDate, epoch ))
	
	if theDate < epoch:
		end = '<'
	else:
		end = '>'

	msDiff = epoch - theDate

	if msDiff > 0 and msDiff <= 86400:
		return 'today'
	elif msDiff > 0 and msDiff <= 82800:
		return 'today'
	elif msDiff > 0 and msDiff <= 169200:
		return 'yesterday'
	elif msDiff > 0 and msDiff <= 604801:
		return 'this week'

	# print( theDate, days, theDate < epoch, theDate > epoch, epoch, time.time() )
	if days == 0:
		return 'today'
	elif theDate < epoch:
		if days == 1:
			return 'yesterday'
		elif days < 7:
			return 'this week'
	elif theDate > epoch:
		if days == 1:
			return 'tommorow'
		elif days < 7:
			return 'next week'

	if days >= 365:
		tmp = float(days / 365)
		y = int(str(tmp).split('.')[0])
		days = days - ( y*365 )
	if days >= 30:
		tmp = float(days / 30)
		m = int(str(tmp).split('.')[0])
		days = days - ( m*30 )
	if days >= 7:
		tmp = float(days / 7)
		w = int(str(tmp).split('.')[0])
		days = days - ( w*7 )

	result = []
	if y:
		result.append( str(y)+'y' )
	if m:
		result.append( str(m)+'m' )
	if w:
		result.append( str(w)+'w' )
	result.append( end )
	return ' '.join( result )
def days_diff( one, two ):
	global date_datetime
	oneA = days_diffa( one )
	twoB = days_diffa( two )
	g = 1
	if two > one:
		g = 2

	if one == two:
		return 0
	elif one > two:
		one = days_difff( oneA ).split(' ')[0]
		two = days_difff( twoB ).split(' ')[0]
	else:
		one = days_difff( twoB ).split(' ')[0]
		two = days_difff( oneA ).split(' ')[0]
	# print( '090', one, two )

	oneB = one.split('-')
	twoB = two.split('-')
	if date_datetime is None:
		from datetime import date as date_datetime
	d0 = days_diffd(int(oneB[0]), int(oneB[1]), int(oneB[2]))
	# print( '080', twoB )
	d1 = days_diffd(int(twoB[0]), int(twoB[1]), int(twoB[2]))
	delta = d1 - d0
	dd = delta.days
	if g == 1:
		dd = abs(dd)
	return dd
def getWOY( theDate ):
	theDate = getWOYa( theDate )
	woy = getWOYg(theDate)
	year = getWOYg(theDate)
	weekAndYear = round(woy * 0.01,2) + year
	weekAndYear = str(weekAndYear)
	if len(weekAndYear) == 6:
		weekAndYear += '0' 
	return weekAndYear
def get_year_from_epoch(theDate):
	theDate = get_year_from_epocha(theDate)
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[0]
def getWOYFrom_epoch(theDate):
	# print('theDate:',theDate)
	theDate = getWOYFrom_epocha(theDate)

	try:
		return datetime.datetime.fromtimestamp( theDate ).isocalendar()[1]
	except Exception as e:
		print( 'Error:', theDate )
		sys.exit()
def print_bold( string, color='white', prefix='' ):
	
	if '\n' in string:
		string = string.replace( '\n', '\n'+prefix )
	else:
		string = prefix + string
	
	global switch
	if switch.isActive( 'NoColor' ):
		print( string )
		return False

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		print( ColorBold.white + string + ColorBold.end )
	elif color == 'red':
		print( ColorBold.red + string + ColorBold.end )
	elif color == 'gray' or color == 'grey':
		print( ColorBold.gray + string + ColorBold.end )
	elif color == 'green':
		print( ColorBold.green + string + ColorBold.end )
	elif color == 'yellow':
		print( ColorBold.yellow + string + ColorBold.end )
	elif color == 'blue':
		print( ColorBold.blue + string + ColorBold.end )
	elif color == 'magenta':
		print( ColorBold.magenta + string + ColorBold.end )
	elif color == 'cyan':
		print( ColorBold.cyan + string + ColorBold.end )
def file_date( theDate ):
	friendly = file_datef( theDate )
	friendly = friendly.replace( ' ', '_' )
	friendly = friendly.replace( ':', '-' )
	return friendly
def save_table2( rows, theFile, printThis=False, sort_keys=False, indentCode=True, p=None, me=0 ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')
	if not p is None:
		printThis = p
	# print('*******************',theFile)
	if theFile.startswith('temp'+_v.slash):
		theFile = theFile.replace( 'temp'+_v.slash, '' )
		theFile = _v.stmp + _v.slash + theFile

	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys)
	else:
		dataDump = simplejson.dumps(rows)

	# dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(theFile)
	if printThis:
		print('Saved: ' + theFile)
	if me and theFile in v.opened_file_me: save_table2c( theFile, v.opened_file_me[theFile] );
def d2json( data, sort_keys=False ):
	simplejson = __.imp('simplejson')
	# d2jsons( data, _v.json_temp )
	# txt = d2jsong( _v.json_temp, raw=True )

	return simplejson.dumps(data, indent=4, sort_keys=sort_keys)
def get_text( theFile, raw=False, clean=False,  e=0, c=0 ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	HD.chmod(theFile)
	lines = None
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
	else:
		if not e:
			return None
		print('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( _v.slash+'n', '\n' )

		if clean:
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		return txt
	elif c > 0:
		if c > 1:
			txt = ''.join( lines )
			TXT = ''
			txt = txt.replace( "'\"\"\"'", '' )
			if '"""' in txt:
				for i,item in enumerate(txt.split('"""')):
					if i % 2 == 0:
						TXT+=item
			elif not '"""' in txt:
				TXT = txt
			while '    ' in TXT:
				TXT = TXT.replace( '    ', '\t' )
			while ' (' in TXT:
				TXT = TXT.replace( ' (', '(' )
			while ' =' in TXT:
				TXT = TXT.replace( ' =', '=' )
			while '= ' in TXT:
				TXT = TXT.replace( '= ', '=' )
			while 'def  ' in TXT:
				TXT = TXT.replace( 'def  ', 'def ' )
			while 'class  ' in TXT:
				TXT = TXT.replace( 'class  ', 'class ' )
			lines = TXT.split('\n')

		newLines = []
		for i,row in enumerate(lines):
			# row = row.replace('\n','')
			row = row.replace('\r','')
			
			if not c > 1:
				newLines.append(row)
			else:
				row = row.split('#')[0]
				test = row
				# while test.startswith(' ') or test.startswith('\t'):
				#   test = _str.cleanBE( test, ' ' )
				#   test = _str.cleanBE( test, '\t' )
				if not test.startswith('#') and len(test):
					newLines.append(row)
			
		return newLines

	elif clean:
		# lines = _str.replaceDuplicate( lines, '\n' )
		# lines = _str.cleanBE( lines, '\n' )
		for i,row in enumerate(lines):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			if type(clean) == int:
				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )
			if clean == 3:
				row = ' ' + row + ' '

			# print( row )
			lines[i] = row
		return lines
	else:
		return lines
def generate_color_index():
	global app_full_color_index
	if not app_full_color_index is None:
		return app_full_color_index
	colorClasses = 'ColorBold Color Background BackgroundGrey BackgroundGreyBold'
	list_of_colors = []
	test = 0
	if test == 0:
		for cc in colorClasses.split(' '):
			for x in dir(  eval(  '__.'+cc  )  ):
				if not x.startswith('_'):
					
					subject = x
					subject = subject.lower()
					if not subject in list_of_colors:
						list_of_colors.append( subject )

					subject = cc+'.'+x
					subject = subject.lower()
					if not subject in list_of_colors:
						list_of_colors.append( subject )
	test = 1
	if test == 1:
		for x in __.colorHelp_colorList:
			if '.' in x:
				p = x.split('.')
				a = p[0]+'.'
				aa = a.lower()
				b = p[1]
				bb = b.lower()

				subject = bb
				if not subject in list_of_colors:
					list_of_colors.append( subject )

				subject = x.lower()
				if not subject in list_of_colors:
					list_of_colors.append( subject )
	app_full_color_index = []

	for x in list_of_colors:
		if not '.' in x:
			app_full_color_index.append( x )

	for x in list_of_colors:
		if '.' in x:
			app_full_color_index.append( x )

	return app_full_color_index
def time_ago_past(do='', startDate=None):
	if startDate is None:
		startDate = time.time()
	global isTime
	# return do
	if '.' in do:
		dos = do.split('.')
		e = time_ago_pastt( dos[0], startDate )
		# return e
		for di,ds in enumerate(dos):
			if di:
				e = time_ago_pastt( dos[di], e )
		return e
	if do.startswith('-'):
		do = do[1:]
	if do is None:
		time_ago_pastc( '\t Error: Ago is Missing parameters', 'red' )
		sys.exit()
	if type(do) == float:
		return do
	if do.lower() == 'r':
		return 'resent'
	if 're' in do.lower():
		return 'resent'
	if 'a' in do.lower():
		return 'a'
	if 'cd' in do:
		return do.lower()
	if 'md' in do:
		return do.lower()
	if 'mod' in do.lower():
		return 'md'
	if 'crea' in do.lower():
		return 'cd'
	if 'o' in do.lower():
		return 'one'

	if len(do) == 0:
		do = switch.values('Ago')[0]
	do = do.lower()

	if 't' in do:
		one = time_ago_pastr( startDate )
		two = time_ago_pasta( one.split(' ')[0] )
		return two
	if isTime:
		if 'm' in do:
			each = 60
			units = do
			units = units.replace( 'm', '' )
			units = int( units )
			remove = units * each
			return startDate - remove  
	if 'mm' in do or 'min' in do:
		each = 60
		units = do
		units = units.replace( 'min', '' )
		units = units.replace( 'm', '' )
		units = int( units )
		remove = units * each
		return startDate - remove  

	if 'h' in do:
		each = 3600
		units = do
		units = units.replace( 'h', '' )
		units = int( units )
		remove = units * each
		return startDate - remove  
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
		# start_date = datetime.date.today() + datetime.timedelta(-365 * nmb)
		# start_date = time_ago_pastd( startDate, 365 * nmb, '-' )
		start_date = time_ago_pasty( startDate, nmb, do='-' )
	if 'm' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-30 * nmb)
		# start_date = time_ago_pastd( startDate, 30 * nmb, '-' )
		start_date = time_ago_pastm( startDate, nmb, do='-' )
	if 'w' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-7 * nmb)
		start_date = time_ago_pastd( startDate, 7 * nmb, '-' )
	if 'd' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-1 * nmb)
		start_date = time_ago_pastd( startDate, nmb, '-' )
	return start_date
def post_load( file, epoch=0, rent=False ):
	return None
	__.post_loadFile = file
	global autoLoadData
	global switch
	global appData
	
	try:
		__.appInfoScan
	except Exception as e:
		pass
	if not type( rent ) == bool:
		rent = rent
	else:
		rent = __.rent

		# print( 'rent:', rent )
		# post_loadp( appData )
		if  rent in appData:
			if type( appData[rent]['pipe'] ) == bool:
				hasPipeData = False
			else:
				hasPipeData = True
		else:
			hasPipeData = False

		# print( type( appData[rent]['pipe'] ) )
		# print( appData[rent]['pipe'] )
		if type( myFileLocation_File ) == bool:
			hasFile = False
		else:
			hasFile = True
		
		# if __.isRequired_Pipe_or_File and not hasFile and not hasPipeData:
		#     if __.pre_error:
		#         print(  )
		#         print( post_loadi('Error:','red')+post_loadi(' Pipe')+' data or '+post_loadi('File')+' is required' )
		#         print(  )
		#         sys.exit()

		# if __.isRequired_Pipe and not hasPipeData:
		#     if __.pre_error:
		#         print(  )
		#         print( 'Error: Pipe data is required' )
		#         print(  )
		#         sys.exit()

		on = switch.records( formating='dic_on-off-v', rent=rent )['on']
		# post_loadp(on)
		metCriteria = True
		if __.isRequired_or_List is None:
			if __.isRequired_Pipe:
				__.isRequired_or_List = ['Pipe']
			if __.isRequired_Pipe_or_File:
				__.isRequired_or_List = ['Pipe','Files']
		if not __.isRequired_or_List is None:
			if __.pre_error:
				fnd = False
				if not metCriteria:
					if not hasPipeData and 'Pipe' in __.isRequired_or_List:
						metCriteria = False
				if not metCriteria:
					for x in __.isRequired_or_List:
						if not x == 'Pipe':
							if x in on:
								fnd = True
					if not fnd:
						metCriteria = False
				
				if not metCriteria:
					help()
		if metCriteria:
			if rent in __.isRequired_index and len( __.isRequired_index[rent] ):
				fnd = False
				for x in __.isRequired_index[rent]:
					if not x == 'Pipe':
						if x in on:
							fnd = True
				if not fnd:
					metCriteria = False
			
			if not metCriteria:
				help()

		# if metCriteria:
		# if not type( __.isRequired_or_List ) == bool and __.registeredApps[0] == __.rent:
		#     meetsRequirements = False
		#     if 'Pipe' in __.isRequired_or_List:
		#         if hasPipeData:
		#             meetsRequirements = True
		#         if not hasFile and not hasPipeData:
		#             pass
		#         else:
		#             meetsRequirements = True
		#     if not meetsRequirements:
		#         for check in __.isRequired_or_List:
		#             if switch.isActive(check):
		#                 meetsRequirements = True
		#         if not meetsRequirements:
		#             if __.pre_error:
		#                 print(  )
		#                 print( post_loadi( 'Error:', 'red' ) + ' One of the following is required:', ', '.join( __.isRequired_or_List ) )
		#                 print(  )

		#                 # print( __.registeredApps )

		#                 sys.exit()
	appDBA = this_app( file )

	if switch.isActive( 'LoadEpoch' ):
		if '.' in switch.value( 'LoadEpoch' ):
			autoLoadData = True
			epoch = float( switch.value( 'LoadEpoch' ) )
	if autoLoadData and epoch == 0:
		if type( autoLoadData ) == str:
			if '.' in autoLoadData:
				epoch = float( autoLoadData )
		if type( autoLoadData ) == float:
			epoch = autoLoadData

		if epoch == 0:
			autoLoadData = False
	if autoLoadData:
		post_load( appDBA, epoch, rent )
	else:
		post_load( appDBA, rent )
def release_acquired_data( appDBA, rent, payload=None ):
	if appDBA == '__init__':
		return None
	if not __.releaseAcquiredData:
		return None
	if not os.name == 'nt':
		return None
	global autoBackupData
	global switch
	global appData
	global myFileLocation_Files
	global switch
	log = _v.appLogs() + _v.slash+'execution_receipt-' + appDBA + '-' + str( __.start_time ) + '.json'
	rebuiltCommandRaw = release_acquired_datat( appDBA, printThis=False, separate=True )
	if len( rebuiltCommandRaw[1] ):
		rebuiltCommand = rebuiltCommandRaw[0] + ' ' + rebuiltCommandRaw[1]
		rebuiltCommandEpoch = rebuiltCommandRaw[0] + ' -loadEpoch ' + str( __.start_time ) + ' ' + rebuiltCommandRaw[1]
	else:
		rebuiltCommand = rebuiltCommandRaw[0]
		rebuiltCommandEpoch = rebuiltCommandRaw[0] + ' -loadEpoch ' + str( __.start_time ) 
	# print( log )
	# print( rebuiltCommandRaw )
	# autoBackupData = True
	info = {
				'epoch': __.start_time,
				'app': appDBA,
				'session': _v.session(),
				'rebuiltCommand': rebuiltCommand,
				'rebuiltCommandEpoch': rebuiltCommandEpoch,
				'files': [],
				'switches': switch.getTable(),
				'errors': [],
	}
	if not payload is None:
		info['payload'] = payload

	if not autoBackupData:
		release_acquired_datas( info, log )

	if autoBackupData:
		if len( myFileLocation_Files ):
			for i,file in enumerate(myFileLocation_Files):
				if os.path.isfile(file):
					thisName = 'files-' + appDBA + '-' + str( __.start_time ) + '_file' + str(i) + '.cache'
					import _rightThumb._dir as _dir
					dirRecord = _dir.info( file, mime=True )
					info['errors'] = []
					fileError = 'Error: File is ' + dirRecord['mime'] + ' and ' + dirRecord['size']
					try:
						if dirRecord['mime'] == 'Text' and dirRecord['bytes'] < 5242880:
							tmpData = release_acquired_datag( file )
							release_acquired_datas( tmpData, _v.myAppLogs + _v.slash + thisName )
							info['files'].append( thisName )
						else:
							info['errors'].append({ 'error': fileError, 'file': _v.myAppLogs + _v.slash + thisName })
							release_acquired_datas( fileError, _v.myAppLogs + _v.slash + thisName )
							

					except Exception as e:
						info['errors'].append({ 'error': fileError, 'file': _v.myAppLogs + _v.slash + thisName })

		# print( rent, type( appData[rent]['pipe'] ) )
		# print('rent',rent)
		if not type( appData[rent]['pipe'] ) == bool:
			thisName = 'files-' + appDBA + '-' + str( __.start_time ) + '_pipe' + '.cache'
			release_acquired_datas( appData[rent]['pipe'], _v.myAppLogs + _v.slash + thisName )
			# print(info)
			info['files'].append( thisName )
			
		

		release_acquired_datas( info, log )
def save_text( rows, theFile, errors=True, me=0 ):
	HD.chmod(theFile)
	# print(type(rows))
	try:
		if type(rows) == bytes:
			rows = str(rows,'utf-8')
		f = open(theFile,'w', encoding='utf-8')
		# if type(rows) == str:

		# print(type(rows))
		# f.write(str(rows))
		# rows = [save_textu(x.strip()) if x is not None else u'' for x in rows]
		# f.write(rows)
		# f.write(rows.encode("iso-8859-1", "replace"))

		# print(type(rows))
		if type(rows) == str:
			# print(rows)
			f.write(rows)
		else:
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						f.write(str(row) + '\n')
				else:
					f.write(str(row) + '\n')
		f.close()
	except Exception as e:
		if type(rows) == list:
			result = ''
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						result += str(row) + '\n'
				else:
					result += str(row) + '\n'

			rows = result
		try:
			open(theFile, 'wb').write(rows)
		except Exception as e:
			try:
				open(theFile, 'w').write(rows)
			except Exception as e:
				new_text = ''
				for x in rows:
					if x in _str.printable:
						new_text+=x
				open(theFile, 'w', encoding='utf-8').write(new_text)
		HD.chmod(theFile)
		# if errors:
		#   print( 'Auto correction when saving text' )
	if me and theFile in v.opened_file_me: save_textc( theFile, v.opened_file_me[theFile] );
def the_command( file='', rent=False, printThis=True, justSwitches=False, separate=False ):
	global switch
	# __.theCommand( __file__, rent=False, printThis=True, justSwitches=False  )
	
	if not type( rent ) == bool:
		rent = rent
	else:
		rent = __.rent
	if len( file ):
		if _v.slash in file or '.py' in file.lower():
			appDBA = this_app( file )
		else:
			appDBA = file
	else:
		appDBA = ''
	theSwitchInfo = switch.rebuild()
	if justSwitches:
		result = theSwitchInfo
	else:
		result = 'p ' + appDBA + ' ' + theSwitchInfo
	if printThis:
		print( result )
	if separate:
		return [ 'p ' + appDBA, theSwitchInfo ]

	return result
def reclaim_acquired_data( appDBA, epoch, rent=False ):
	print( 'reclaimAcquiredData' )
	global switch
	if not type( rent ) == bool:
		rent = rent
	else:
		rent = __.rent

	log = _v.appLogs() + _v.slash+'execution_receipt-' + appDBA + '-' + str( epoch ) + '.json'
	print(  os.path.isfile(log), log )
	if not os.path.isfile(log):
		reclaim_acquired_datac( 'Error: please select a valid backup', 'error' )
		sys.exit()
	info = reclaim_acquired_datag( log )
	__.payloadCache = None
	if 'payload' in info:
		__.payloadCache = info['payload']
	# print( log )
	# print( info )
	# reclaim_acquired_datap( info )

	def pipeFile():
		for file in info['files']:
			if 'pipe' in file:
				return _v.myAppLogs + _v.slash + file
		return False

	def theFiles():
		theFiles = []
		for file in info['files']:
			if not 'pipe' in file:
				theFiles.append( _v.myAppLogs + _v.slash + file )
		return theFiles

	def rebuildSwitches( switchData ):
		# reclaim_acquired_datap( switchData )
		for i,switch in enumerate(switchData):
			if switch['name'] == 'File' or switch['name'] == 'Files':
				switchData[i]['values'] = []
				for file in info['files']:
					if not 'pipe' in file:
						switchData[i]['values'].append( _v.myAppLogs + _v.slash + file )
				switchData[i]['value'] = ','.join( switchData[i]['values'] )
		return switchData

	def rebuildFiles( switchData ):
		data = []
		for i,switch in enumerate(switchData):
			if switch['name'] == 'File' or switch['name'] == 'Files':
				switchData[i]['values'] = []
				for file in info['files']:
					if not 'pipe' in file:
						switchData[i]['values'].append( _v.myAppLogs + _v.slash + file )
				switchData[i]['value'] = ','.join( switchData[i]['values'] )
				data.append( switchData[i] )
		return data
	def rebuildFiles( switchData ):
		for i,switch in enumerate(switchData):
			if switch['name'] == 'File' or switch['name'] == 'Files':
				switchData[i]['values'] = []
				for file in info['files']:
					if not 'pipe' in file:
						switchData[i]['values'].append( _v.myAppLogs + _v.slash + file )
				switchData[i]['value'] = ','.join( switchData[i]['values'] )
				data.append( switchData[i] )
		return data
	if switch.onlyLoadEpoch( rent=rent ):
		switchData = reclaim_acquired_datar( info['switches'] )
	else:
		switchData = reclaim_acquired_datar( info['switches'] )
	# reclaim_acquired_datap( switchData )
	switch.loadTable( switchData, rent=rent )
	# print( 'rent:', rent )

	if not type( reclaim_acquired_datap() ) == bool:
		appData[rent]['pipe'] = reclaim_acquired_datag( reclaim_acquired_datap() )
def print_var( data, sort_keys=False, isDic=None ):
	data = print_varj(data)
	if not isDic is None and isDic and type(data) == str:
		print_vars( data, _v.myTemp + _v.slash+'printVar.json' )
		data = print_varg( _v.myTemp + _v.slash+'printVar.json' )
		result = print_vard( data, sort_keys )
	else:
		result = data
	# print_vars( data, _v.json_temp )
	# result = print_varg( _v.json_temp, raw=True )
	# result = type( result )
	result = print_varp( result )
	print(  )
def print_var_color( data ):
	_code = print_var_colorr( __.rent, '_rightThumb._auditCodeBase' )
	validator = _code.imp.Validator()

	# index = validator.createIndex( data, 'javascript' )
	# validator.colorPrint_old()
	# print(data)
	index = validator.createIndex( data, 'javascript', skipLoad=True, simple=False, A=None, B=True, C=None )
	# print_var_colorp(validator.identity)
	# index = validator.createIndex( data, 'javascript', simple=False, B=True )
	validator.colorPrint()
def print_var_simple( data, sort_keys=False, isDic=None, prefix=None, remove=None ):
	data = print_var_simplej(data)
	if not isDic is None and isDic and type(data) == str:
		print_var_simples( data, _v.myTemp + _v.slash+'printVarSimple.json' )
		data = print_var_simpleg( _v.myTemp + _v.slash+'printVarSimple.json' )
	print_var_simplep( data, sort_keys, prefix=prefix, remove=remove )
def print_var_old( data, sort_keys=False, prefix=None, remove=None ):
	result = print_var_oldd( data, sort_keys )
	# result = type( result )
	result = print_var_oldp( result )
	if not remove is None:
		for x in remove:
			result = result.replace(x,'')
	if prefix is None:
		print( result )
	else:
		for x in result.split('\n'):
			print( prefix+x )
def print_var_color_OLD( data ):
	result = ''
	for char in data:
		result += print_var_color_OLDp( char )
	return result
def print_var_color_char( data ):
	what = '('
	color = 'Background.red'
	if data == what:
		return data.replace( what, print_var_color_charc( what, color, shouldPrint=False ) )

	what = ')'
	color = 'Background.red'
	if data == what:
		return data.replace( what, print_var_color_charc( what, color, shouldPrint=False ) )
	what = '{'
	color = 'green'
	if data == what:
		return data.replace( what, print_var_color_chari( what, color ) )
	
	what = '}'
	color = 'green'
	if data == what:
		return data.replace( what, print_var_color_chari( what, color ) )
	
	what = '['
	color = 'YELLOW'
	if data == what:
		return data.replace( what, print_var_color_chari( what, color ) )

	what = ']'
	color = 'YELLOW'
	if data == what:
		return data.replace( what, print_var_color_chari( what, color ) )

	what = '"'
	color = 'white'
	if data == what:
		return data.replace( what, print_var_color_chari( what, color ) )

	what = "'"
	color = 'white'
	if data == what:
		return data.replace( what, print_var_color_chari( what, color ) )

	what = ':'
	color = 'red'
	if data == what:
		return data.replace( what, print_var_color_chari( what, color ) )

	what = ','
	color = 'Magenta'
	if data == what:
		return data.replace( what, print_var_color_chari( what, color ) )

	what = '='
	color = 'red'
	if data == what:
		return data.replace( what, print_var_color_chari( what, color ) )

	return data
def inline_bold( string, color='white' ):
	global switch
	if switch.isActive( 'NoColor' ):
		return string
	
	string = str(string)
	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		return ColorBold.white + string + ColorBold.end 
	elif color == 'red':
		return ColorBold.red + string + ColorBold.end 
	elif color == 'gray' or color == 'grey':
		return ColorBold.gray + string + ColorBold.end 
	elif color == 'green':
		return ColorBold.green + string + ColorBold.end 
	elif color == 'yellow':
		return ColorBold.yellow + string + ColorBold.end 
	elif color == 'blue':
		return ColorBold.blue + string + ColorBold.end 
	elif color == 'magenta':
		return ColorBold.magenta + string + ColorBold.end 
	elif color == 'cyan':
		return ColorBold.cyan + string + ColorBold.end
	elif color == 'underline':
		return ColorBold.underline + string + ColorBold.end
def inline_color( string, color='red' ):

	global switch
	if switch.isActive( 'NoColor' ):
		return string

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'red':
		return Color.red + string + Color.end
	elif color == 'cyan':
		return Color.cyan + string + Color.end
	elif color == 'darkcyan' or color == 'grey':
		return Color.darkcyan + string + Color.end
	elif color == 'blue':
		return Color.blue + string + Color.end
	elif color == 'green':
		return Color.green + string + Color.end
	elif color == 'yellow':
		return Color.yellow + string + Color.end
	elif color == 'underline':
		return Color.underline + string + Color.end
def get_table2( theFile,     isDic=None, isList=None ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
		isDic = True
	if os.path.isfile(theFile):
		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()
def json_clean(obj):
	if hasattr(obj, '__class__') and '.'  in str(obj.__class__):
		obj = dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('__'))
		obj = json_cleanp(obj)
	return obj
def prep4JSON(d, to_delete=None):
	# remove keys from multidimensional dicts and lists
	def autoFindKeys(d):
		# removes functions and methods
		global autoFindKeys_temp
		if isinstance(d, dict):
			for k in d.keys():
				t = type( d[k] )
				if 'function' in str(t):
					autoFindKeys_temp.append( k )
				elif 'method' in str(t):
					autoFindKeys_temp.append( k )
				
			for k, v in d.items():
				prep4JSONa(v)
		elif isinstance(d, list):
			for i in d:
				prep4JSONa(i)
		return d

	if to_delete is None:
		global autoFindKeys_temp
		autoFindKeys_temp = []
		prep4JSONa(d)
		return prep4JSONp(d, to_delete=autoFindKeys_temp)

	if isinstance(to_delete, str):
		to_delete = [to_delete]
	if isinstance(d, dict):
		for single_to_delete in set(to_delete):
			if single_to_delete in d:
				d[single_to_delete] = ' ** removed ** '
		for k, v in d.items():
			prep4JSONp(v, to_delete)
	elif isinstance(d, list):
		for i in d:
			prep4JSONp(i, to_delete)
	return d
def is_data( data=None, focus=None, pipeClean=True, required=False,     r=None, c=None ):
	if not c is None: pipeClean=c;
	if not r is None: required = r;
	
	if data is None:
		if pipeClean:
			is_datap(0)
		global appData
		if focus is None:
			focus = __.rent
		data = appData[focus]['pipe']

	if r:
		if type(data) == bool:
			help()
			return None
		if not data:
			help()
			return None
	else:
		if type(data) == bool:
			return []
		if not data:
			return []
	
	return data
def pipe_cleaner(clean=0):
	def pipe_cleanerDeep(p):
		while p.startswith(' '):
			p = p[1:]

		while p.endswith(' '):
			p = p[:-1]

		while p.startswith('\r'):
			p = p[1:]

		while p.endswith('\r'):
			p = p[:-1]

		while p.startswith('\n'):
			p = p[1:]

		while p.endswith('\n'):
			p = p[:-1]

		while p.startswith('\t'):
			p = p[1:]

		while p.endswith('\t'):
			p = p[:-1]
		return p
	global appData
	try:
		if not appData[__.rent]['pipe'][0][0] in _str.safeChar:
			appData[__.rent]['pipe'][0] = appData[__.rent]['pipe'][0][1:]
	except Exception as e:
		pass
	try:
		for i,pipeData in enumerate(appData[__.rent]['pipe']):
			p = appData[__.rent]['pipe'][i].replace('\n','')
			if clean:
				while p.startswith(' '):
					p = p[1:]

				while p.endswith(' '):
					p = p[:-1]
			if type(clean) == int and clean > 1:
				p = pipe_cleanerp(p)
				p = pipe_cleanerp(p)
				p = pipe_cleanerp(p)
			appData[__.rent]['pipe'][i] = p
	except Exception as e:
		pass
	return appData[__.rent]['pipe']
def load():
	global switches_loaded
	switches_loaded += 1
	if switches_loaded > 1:
	# if True
		global switch
		global switchDefault

		# global tables

		# switch.trigger('Column',formatColumns)

		# switchDefault = switch.length()
		# switch.register('Help', '?,??,/?,-?,/h,/help,-help,--help', 'copy  OR ids  OR  12  OR  ?? x')
		# switch.register('Column', '-c,-column', 'size, name')
		# switch.register('Sort','-s,-sort', 'Asc:type, Desc:ext')
		# switch.register('Debug', '-debug')
		# switch.register('Errors', '-Error,-Errors', '8,11 OR hide:8,11')
		# switch.register('Timeout', '-t,-Timeout')
		# switch.register('GroupBy', '-g,-group,-groupby', 'ext, month')
		# switch.register('WrapTable', '-wrap', 'n p  OR  2  OR  path')
		# switch.register('NoWrapTable', '-nowrap')
		# switch.register('NoTableLines', '-nolines')
		# switch.register('TableJSON', ',-tjson,-tablejson')
		# switch.register('FieldTotal', '-fieldtotal', 'mem_usage')
		# switch.register('Aggregate', '-aggregate', '" eof-field-len= loada(len(version),len(backup)); loadc(var,eof,isFirst); "')
		# switch.register('GroupSpaces', '-gs,-space,-groupspaces')
		# switch.register('TableProfile', '-tp,-table',' *;c *;l  h;l header;left  size;l,gs')
		# # switch.register('ShortenColumn', '-sc,-shortencolumn')
		# switch.register('WebTable', '-web')
		# switch.register('Long', '-l,-long')
		# switch.register('Short', '-sc,-short')
		# switch.register('Length', '-length','x3')
		# # switch.register('Report', '-report')
		# switch.register('Plus', '+')
		# switch.register('Minus', '-')
		# switch.register('PlusOr', '-or')
		# switch.register('PlusClose', '+close', '90%')
		# switch.register('PlusDuplicate', '+dup,+duplicate', '90%')
		# switch.register('StrictCase', '-strictcase')
		# switch.register('PrintAutoAbbreviations', ',-printa,-aprint')
		# switch.register('NoColor', '-nocolor', space=True)
		# switch.register('LoadEpoch', '-loadepoch')
		# switch.register('PrintEpoch', '-printepoch')
		# # switch.register('SkipColumnTriggers', '-skiptriggers')
		# loadd()

timeAgoBase = []
timeAgoBaseCount = 0
isTime = False
# switches = Switches()
colorHelp_colorList = []
ipsum = None
appData = {}
appInfo = {}
changeDate_Table = None
_dir = None
touch_meta = None
date_datetime = None
app_full_color_index = None
autoLoadData = False
autoBackupData = False
myFileLocation_Files = []
switches_loaded = 0
# tables = Tables()
def register(*values):
	pass
def focus(*values):
	pass
############################################################## copy-fn-class

############################################################## copy-fn-class
def construct_registration( file, dba ):
	global registeredAppsAll
	shouldAdd = True
	for ra in registeredAppsAll:
		if ra['dba'] == dba:
			shouldAdd = False
	if shouldAdd:
		registeredAppsAll.append({ 'file': file, 'dba': dba })

############################################################## copy-fn-class


# switches = Switches()
ciData = (  
			[ '_;192A;_',   ',' ],
			[ '_;192B;_',   ':' ],
			[ ';;',         ',' ],
			[ ';c',         ',' ],
			
			[ ';_',         '-' ],
			[ ';-',         '-' ],

			[ ';p;',        '%' ],
			[ ';p',         '%' ],
			[ ';.',         ':' ],
			[ ";;'",        _v.slash+'"' ],

			[ _v.slash+'n',        '\n' ],
			[ ';n',         '\n' ],
			[ ';return',    '\n' ],
			[ ';t',         '\t' ],

			[ ";'",         '"' ],
			[ ';q;',        '"' ],
			[ '"\'"',       "'" ],
			[ 'null00',     '"",' ],
			[ '"\'", "\'"', "','" ],

			[ '[star]',     '*' ],
			[ '[a]',        '*' ],
			[ '[s]',        '$' ],
			[ '[eq]',       '=' ],
			[ ';opar;',     '[' ],
			[ '[pipe]',     '|' ],
			[ '[p]',     '|' ],
			[ '[htmlopen]', '<' ],
			[ '[htmlclose]','>' ],
			[ '[gtr]',      '>' ],
			[ '[lss]',      '<' ],
			[ ';6',         '^' ],
			[ ';+',         '+' ],

			[ '+--+c',          '--c' ],

			[ '[semi]',         ';' ],
			
			[ '[caret]',    '^' ]  )
plusClose = 70




############################################################## copy-fn-class



class ColorBold:
	gray = '\033[1;30;40m'
	red = '\033[1;31;40m'
	green = '\033[1;32;40m'
	yellow = '\033[1;33;40m'
	blue = '\033[1;34;40m'
	magenta = '\033[1;35;40m'
	cyan = '\033[1;36;40m'
	white = '\033[1;37;40m'
	underline = '\033[4m'
	end = '\033[0m'



row_colors = []
row_colors_ID = 0
colorizeRow_last = None
# switches = Switches()
cp=color_this



############################################################## copy-fn-class


def addComma( data ):
	test = 0
	try:
		int(data)
		test+=1
	except Exception as e:
		pass
	try:
		float(data)
		test+=1
	except Exception as e:
		pass
	
	if not test:
		return data

	txt = str( data )
	if '.' in txt:
		txt = txt.split( '.' )[0]
	n = []
	for x in txt:
		n.append( x )
	n.reverse()
	y = []
	for i,x in enumerate(n):
		y.append( x )
		if ((i+1)%3==0):
			y.append( ',' )
	y.reverse()
	result = ''.join( y )
	result = _str.cleanBE( result, ',' )
	return result

myFileLocation_File=[]




class ColorBold:
	gray = '\033[1;30;40m'
	red = '\033[1;31;40m'
	green = '\033[1;32;40m'
	yellow = '\033[1;33;40m'
	blue = '\033[1;34;40m'
	magenta = '\033[1;35;40m'
	cyan = '\033[1;36;40m'
	white = '\033[1;37;40m'
	underline = '\033[4m'
	end = '\033[0m'


class Color:
	purple = '\033[95m'
	cyan = '\033[96m'
	darkcyan = '\033[36m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	end = '\033[0m'


class Background:
	red = '\033[1;37;41m'
	green = '\033[1;37;42m'
	yellow = '\033[1;37;43m'
	blue = '\033[1;37;44m'
	purple = '\033[1;37;45m'
	light_blue = '\033[1;37;46m'
	grey = '\033[1;37;47m'
	black = '\033[1;37;48m'
	end = '\033[0m'

class BackgroundGrey:
	black = '\033[0;30;47m'
	red = '\033[0;31;47m'
	green = '\033[0;32;47m'
	brown = '\033[0;33;47m'
	blue = '\033[0;34;47m'
	magenta = '\033[0;35;47m'
	cyan = '\033[0;36;47m'
	gray = '\033[0;37;40m'
	end = '\033[0m'
	
class BackgroundGreyBold:
	black = '\033[1;30;47m'
	red = '\033[1;31;47m'
	green = '\033[1;32;47m'
	brown = '\033[1;33;47m'
	blue = '\033[1;34;47m'
	magenta = '\033[1;35;47m'
	cyan = '\033[1;36;47m'
	gray = '\033[1;37;40m'
	end = '\033[0m'
	


row_colors = []

row_colors.append([ 0, Background.blue ])
row_colors.append([ 0, Background.light_blue ])
row_colors.append([ 0, Background.purple ])

row_colors.append([ 1, BackgroundGrey.red ])
row_colors.append([ 1, BackgroundGrey.brown ])
row_colors.append([ 1, BackgroundGrey.blue ])

row_colors.append([ 2, Color.cyan ])
row_colors.append([ 2, Color.green ])

row_colors_ID = 0

colorHelp_colorList = [
	"ColorBold.gray",
	"ColorBold.red",
	"ColorBold.green",
	"ColorBold.yellow",
	"ColorBold.blue",
	"ColorBold.magenta",
	"ColorBold.cyan",
	"ColorBold.white",

	"",

	"Color.purple",
	"Color.cyan",
	"Color.darkcyan",
	"Color.blue",
	"Color.green",
	"Color.yellow",
	"Color.red",
	"Color.bold",
	
	"",

	"Background.red",
	"Background.green",
	"Background.yellow",
	"Background.blue",
	"Background.purple",
	"Background.light_blue",
	"Background.grey",
	"Background.black",

	"",

	"BackgroundGrey.black",
	"BackgroundGrey.red",
	"BackgroundGrey.green",
	"BackgroundGrey.brown",
	"BackgroundGrey.blue",
	"BackgroundGrey.magenta",
	"BackgroundGrey.cyan",
	"BackgroundGrey.gray",

	"",

	"BackgroundGreyBold.black",
	"BackgroundGreyBold.red",
	"BackgroundGreyBold.green",
	"BackgroundGreyBold.blue",
	"BackgroundGreyBold.magenta",
	"BackgroundGreyBold.cyan",
	"BackgroundGreyBold.gray"
]


############################################################## copy-fn-class


def payload_cache( data, file=None, theFocus=None ):
	return None
	# _.payloadCache( saveFile, __file__, payload_cachef() )
	
	if theFocus is None:
		theFocus = __.rent
	if file is None:
		appDBA = this_app( __.postLoadFile )
	else:
		appDBA = this_app( file )
	payload_cacher( appDBA, theFocus, data )





############################################################## copy-fn-class


def unix_auto_columns( asset, columns, focus=None ):
	if not len(asset):
		return asset
		# return columns
	asset = asset.copy()
	# if __.thisOS == 'Windows':

	if not __.terminal.width:
		return columns

	cols = __.terminal.width
	if focus is None:
		focus = __.appReg
	global appInfo
	rec = {}
	for k in asset[0].keys():
		rec[k]=k
	asset.append( rec )
		# cols = 102
	reg = appInfo[focus]['columns'].copy()
	reg.reverse()
	importance = []
	for x in reg:
		importance.append(x['name'])
	# importance = [
	#               'date_accessed',
	#               'week_of_year',
	#               'date_created',
	#               'date_modified',
	#               'ext',
	#               'size',
	# ]
	fields.asset( 'asset', asset )
	lengths = fields.lengths( 'asset' )

	# unix_auto_columnsp( lengths )

	total = 3
	for col in columns.split(','):
		total+=3
		for key in lengths:
			if col.lower() == key.lower():
				total += lengths[key]
	# print( total, columns )
	# print( cols, type(cols) )
	nextDel = 0
	done = False
	newList = []
	while total > cols and not done:
		total = 3
		newCols = []
		for col in columns.split(','):
			if col == importance[nextDel]:
				if not col in newList:
					newList.append(col)
			if not col == importance[nextDel]:
				newCols.append(col)
				total+=3
				for key in lengths:
					if col.lower() == key.lower():
						total += lengths[key]
			columns = ','.join(newCols)
		nextDel += 1
		if not len(newCols):
			done=True
	pass
	if not len(columns):
		columns = newList[ len(newList)-1 ]
	# print( total, columns )


	# print( 'total:', total )

	# sys.exit()
	return columns


class dot:
	def __init__( self ):
		pass

v = dot()
v.opened_file_me = {}
__.switch_skimmer = dot()
__.switch_skimmer.scan = [ '??' ]
__.switch_skimmer.active = []

__.aggregate = dot()
__.aggregate.eof = dot()
__.aggregate.eof.storage = {}
__.aggregate.obj = None
__.aggregate.prefixes = {
							'eot?':  1,
							'eof?':  1,
							'eog?':  1,
							'bog?':  1,
							'eoga?': 1,
							'run?':  1,
						}

__.aggregate.group_prefixes = {
							'eog?':  1,
							'bog?':  3,
							'eoga?': 1,
							'run?':  2,
						}
__.aggregate.fn = dot()
# '?date' '?comma' '?size' '?bytes'
__.aggregate.fn.format = {
							'add': '?comma',
							'isDate': '?date',
						}
__.aggregate.fn.order = {
							'isDate': 1
						}
__.table_prefix_padding = 0
__.color_palette = 0
# if self.groupID_KEY in item and item[self.groupID_KEY].endswith('-B'):


__.terminal = dot()
try:
	# cols, rows
	__.terminal.width, __.terminal.height = list( os.get_terminal_size() )
except Exception as e:
	# try:
	#   __.terminal.height, __.terminal.width = os.popen('stty size', 'r').read().split()
	# except Exception as e:
	__.terminal.width = 0
	__.terminal.height = 0

# print(__.terminal.width)

__.terminal.cols = __.terminal.width



############################################################## copy-fn-class





############################################################## copy-fn-class

v.opened_file_me = {}
__.switch_skimmer = dot()
__.switch_skimmer.scan = [ '??' ]
__.switch_skimmer.active = []

_bm = None
arrow = None
_tz = None
pandas = None
_sd = None
__.table_prefix_padding = 0
changeC_rc_path = False
changeDate_Table = None
touch_meta = None
_dir = None
#     ol = o2.status()
line_length_hash_table = {}
_vault = None
_blowfish = None
pyAesCrypt = None
shutil = None
_md5 = None
readline = None
win32clipboard = None
__.raw_table = None
aggregate_trigger_ran = False
pyperclip = None
# lp = loopPrint
isTar = dot()
# isTar.gz = isGz/
# isTar.bz2 = isBz2
__.nc_histrory = []

__.nc_histrory = []
class NC:

	def build( self, x, y=None ):
		__.nc_histrory.append(x)
		if not y == None:
			exec( 'self.' +x+ ' = y' )
		else:
			exec( 'self.' +x+ ' = NC()' )

	def child( self, xx, y=None ):
		xx = xx.replace( ' ', '' )
		for x in xx.split(','):
			if '.' in x:
				z = x.split('.')
				b = ''
				for w in z:
					b += '.'+w
					b = _str.cleanBE(b,'.')
					if not b in __.nc_histrory:
						# print(b)
						self.build(b)


			self.build(x,y)


nc = NC()
colorama_loaded = False
_code = None
isWin = __.isWin
thisOS = __.thisOS
__.appInfoScan = None
domainIndex = None
traverse_dic_research = {}
bmIndex = []
processWordStem = None
__.loadingVar = {
					'hasLoaded': False,
					'hasCleared': False,
					'isRunning': False,
					'done': False,
}
__.loadingVar['hasLoaded'] = False
__.loadingVar['hasCleared'] = False
__.loadingVar['isRunning'] = False
server_proxy = []
server_proxy.append( 'https://signaturemassagetampa.com/payroll/p.php?p = ' )
appProxy = 'appProxy.json'
ipsum = None
__.color_palette = 0
plusClose = 70
autoBackupData = False
autoLoadData = False
idResolution = []
theExtensionsList = []
relevantFolders = []
setPipeDataRan = False
__.columnAbbreviations = 1
row_colors = []
row_colors_ID = 0
colorizeRow_last = None
app_full_color_index = None
myFileLocation_Print = True
myFileLocation_File = False
myFileLocation_Files = []
myFileLocation_Pipe = []
backup_subject_files = True
adminStatus = ''
_tar = None
updateLine_disable = False
TableProfile_Config = {}
isTime = False
timeAgoBase = []
timeAgoBaseCount = 0
cal_days = None
date_datetime = None
defaultScriptTriggers_run = False
printAutoAbbreviations_scheduled = False
thisTest = 'hello'
errors = []
appInfo = {}
appData = {}
argvProcess = True
# fields = Fields()
# threads = Queue()
# switches = Switches()
# tables = Tables()
# databases = Databases()
# __.databases = Databases()
switches_loaded = 0
regImps = {}
leap_years_table = None
# _cryptFile = _.regImp( __.appReg, 'cryptFile' )
# _cryptFile.imp.appDBA = _cryptFile.focus
# colorPrint = colorThis
# cp = colorThis
# pv = printVarSimple
# vp = printVarSimple
imps = {}
size_group_data = [{"l": "1", "s": "500", "x": "kb"}, {"l": "2", "s": "1", "x": "mb"}, {"l": "3", "s": "5", "x": "mb"}, {"l": "4", "s": "10", "x": "mb"}, {"l": "5", "s": "20", "x": "mb"}, {"l": "6", "s": "50", "x": "mb"}, {"l": "7", "s": "200", "x": "mb"}, {"l": "8", "s": "500", "x": "mb"}, {"l": "9", "s": "1", "x": "gb"}, {"l": "10", "s": "5", "x": "gb"}, {"l": "11", "s": "10", "x": "gb"}, {"l": "12", "s": "20", "x": "gb"}, {"l": "13", "s": "50", "x": "gb"}, {"l": "14", "s": "200", "x": "gb"}, {"l": "15", "s": "500", "x": "gb"}, {"l": "16", "s": "1", "x": "tb"}, {"l": "17", "s": "5", "x": "tb"}, {"l": "18", "s": "10", "x": "tb"}, {"l": "19", "s": "20", "x": "tb"}, {"l": "20", "s": "50", "x": "tb"}, {"l": "21", "s": "200", "x": "tb"}, {"l": "22", "s": "500", "x": "tb"}, {"l": "23", "s": "1", "x": "pb"}, {"l": "24", "s": "5", "x": "pb"}, {"l": "25", "s": "10", "x": "pb"}, {"l": "26", "s": "20", "x": "pb"}, {"l": "27", "s": "50", "x": "pb"}, {"l": "28", "s": "200", "x": "pb"}, {"l": "29", "s": "500", "x": "pb"}, {"l": "30", "s": "1", "x": "eb"}, {"l": "31", "s": "5", "x": "eb"}, {"l": "32", "s": "10", "x": "eb"}, {"l": "33", "s": "20", "x": "eb"}, {"l": "34", "s": "50", "x": "eb"}, {"l": "35", "s": "200", "x": "eb"}, {"l": "36", "s": "500", "x": "eb"}, {"l": "37", "s": "1", "x": "zb"}, {"l": "38", "s": "5", "x": "zb"}, {"l": "39", "s": "10", "x": "zb"}, {"l": "40", "s": "20", "x": "zb"}, {"l": "41", "s": "50", "x": "zb"}, {"l": "42", "s": "200", "x": "zb"}, {"l": "43", "s": "500", "x": "zb"}, {"l": "44", "s": "1", "x": "yb"}, {"l": "45", "s": "5", "x": "yb"}, {"l": "46", "s": "10", "x": "yb"}, {"l": "47", "s": "20", "x": "yb"}, {"l": "48", "s": "50", "x": "yb"}, {"l": "49", "s": "200", "x": "yb"}, {"l": "50", "s": "500", "x": "yb"}]
# hp = history_print
# ph = history_print

def test():
	pass

############################################################## copy-fn-class


class Field:

	def __init__( self, project, name, value, appReg, script, maxField ):
		self.appReg = appReg
		self.project = project
		self.name = name
		self.trigger = script
		self.maxField = maxField



		self.registerValue( value )

	def setTrigger( self, script ):
		self.trigger = script

	def addPadding( self, value, extra, right ):
		value = self.runTrigger( str(value) )
		oValue = value
		addPadding = (extra + self.maxField) - len( value )
		add = ''

		while not len(value) >= self.maxField+extra:
			value += ' '
			add += ' '
		# for x in range(1,addPadding+1):
		#   value += ' '
		# return str(self.maxField)+' '+str(len( value ))+value
		if right:
			value = add + oValue
		return value

	def addPaddingSetSpaces( self, value ):
		value = self.runTrigger( str(value) )
		addPadding = self.maxField - len( value )
		newValue = value
		Zeros = ''
		while not len(newValue) == self.maxField:
			Zeros += ' '
			newValue = Zeros + value
		return newValue

	def addPaddingZeros( self, value ):
		value = self.runTrigger( str(value) )
		addPadding = self.maxField - len( value )
		newValue = value
		Zeros = ''
		while not len(newValue) == self.maxField:
			Zeros += '0'
			newValue = Zeros + value
		return newValue

	def runTrigger( self, value ):
		if type( self.trigger ) == bool:
			return value

		# print( 'HERE' )
		return self.trigger( value )

	def registerValue( self, value ):
		thisLen = len( self.runTrigger( str(value) ) )

		if thisLen > self.maxField:
			self.maxField = thisLen


class Fields:

	def __init__(self):
		self.fields = {}
		self.extra = 0

	def lengths( self, project ):
		result = {}
		for record in self.fields[project]:
			if record.project == project:
				result[record.name] = record.maxField
			
		return result
		

	def register( self, project='', names='', value='', appReg=False, script=False, maxField=None,        p=None, n=None, v=None, m=None, isRegisterDic=False ):

		# if project in self.fields:
		#   if not isRegisterDic:
		#       del self.fields[ project ]

		if not p is None:
			project = p

		if not n is None:
			names = n

		if not v is None:
			value = v

		maxField = 0

		if not maxField is None:
			maxField = maxField
			
		if not m is None:
			maxField = m


		if type(appReg) == bool:
			appReg = __.appReg
		if not project in self.fields:
			self.fields[project] = []
		for name in names.split(','):

			shouldAdd = True

			for i,s in enumerate(self.fields[project]):
				if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
					shouldAdd = False
			if shouldAdd:
				self.fields[project].append( Field( project, name, value, appReg, script, maxField ) )
				if maxField and type(value) == int:
					return self.fields[project][len(self.fields[project])-1].addPaddingZeros(value)
				elif maxField and type(value) == str:
					return self.fields[project][len(self.fields[project])-1].addPadding(value)
			else:
				self.registerValue( project, name, value, appReg )

	def registerValue( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		
		result = False
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				self.fields[project][i].registerValue( value )
				result = True
		return result


	def padZeros( self, project, name, value, extra=None, appReg=False, space=False ):

		if extra is None:
			extra = self.extra

		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				if space:
					return self.fields[project][i].addPaddingSetSpaces( value )
				else:
					return self.fields[project][i].addPaddingZeros( value )
				result = self.fields[project][i].addPaddingZeros( value )
		return result


	def value( self, project, name, value, extra=None, right=False, appReg=False,    r=None ):
		result = value
		if not r is None:
			right = r

		if extra is None:
			extra = self.extra

		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				result = self.fields[project][i].addPadding( value, extra, right )
		return result
	def valuez( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				result = self.fields[project][i].addPaddingZeros( value )
		return result

	def asset( self, project, asset, appReg=False ):
		self.fields[project] = []
		if type(appReg) == bool:
			appReg = __.appReg

		if type( asset ) == dict:
			self.registerDic( project, asset, appReg )

		if type( asset ) == list:
			for row in asset:
				if type( row ) == dict:
					self.registerDic( project, row, appReg )


	def registerDic( self, project, asset, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg

		for name in asset.keys():
			self.register( project, name, asset[name], appReg, isRegisterDic=True )


def showLine( string, plus = '', minus = '', plusOr = False, end=None ):
	# print(plus)
	# print(string)
	global switch
	# print(switch.isActive('Plus'))
	# print(switch.values('Plus'))
	# sys.exit()
	if switch.isActive('Plus') or not plus == '':
		# print('asdf')
		result = positiveResults(string,plus,plusOr,end)
		if not result and switch.isActive('PlusClose'):
			result = closeResults( string )

	else:
		result = True
	if result == True and  (switch.isActive('Minus') or not minus == ''):
		result = minusResults(string,minus)
	# print(result)
	return result


def minusResults(string,minus=''):
	global switch
	if not switch.isActive('StrictCase'):
		string = string.lower()
	result = True
	if not minus == '':
		minusInput = minus
	else:
		minusInput = switch.values('Minus')
	if type( minusInput ) == str:
		if not switch.isActive('StrictCase'):
			minusInput = minusInput.lower()
		else:
			minusInput = minusInput
		minusList = minusInput.split(',')
	else:
		for i,row in enumerate(minusInput):
			if not switch.isActive('StrictCase'):
				minusInput[i] = minusInput[i].lower()

		minusList = minusInput

	try:
		for s in minusList:
			if not switch.isActive('StrictCase'):
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
	return result


def ci(string): 
	#switchValueClean
	global ciData
	# print( ciData )
	# sys.exit()
	for cx in ciData:
		if cx[0] in string:
			# print( 'HERE', cx )
			string = string.replace( cx[0], cx[1] )
	
	string = string.replace( ';d;', __.theDelim )
	string = string.replace( ';delim;', __.theDelim )
	string = string.replace( ';thedelim;', __.theDelim )
	string = string.replace( ';theDelim;', __.theDelim )



	return string


def closeResults( string ):
	global switch
	global plusClose
	
	if len( switch.value('PlusClose') ):
		try:
			plusClose = float( switch.value('PlusClose') )
		except Exception as e:
			pass

	test = patternDiff( string, switch.value('Plus') )
	# print( int(test), string, switch.value('Plus') )
	if test >= plusClose:
		# print( test, string )
		return True
	else:
		return False


def patternDiff(a,b):
	# print('here')
	# a = 'gensslkey'
	# b = 'gensslkey'
	# b = 'gensslkeyz'
	# b = 'ssl_socket_bridge_client_user_administrator_logs_b'
	a = a.lower()
	b = b.lower()
	testing = 0

	if testing:
		print()
		print()
		print('________________________________________________________')
		print()
		print()
		print( a,b )
	x = patternMatch( a, b )
	d = get_change( len(a),len(b) )
	e = get_change( x, d )
	# e = get_change( d, x )
	if testing:
		print('x',x)
		print( 'd',d )
		print( 'e,f',e )
	f = int(100-e)
	f =e
	# print( 'f',f )
	if f == 0:
		f = 100
	# dd = d
	dd = int(100-d)
	if dd == 0:
		dd = 100
	if testing:
		print( 'dd',dd )
	# if d <= f:
	if d >= f:
		aa = dd
		bb = f
	else:
		aa = f
		bb = dd
	alphaTest = 'b'
	if alphaTest == 'a':
		kAA = {}
		kAB = {}
		kBA = {}
		kBB = {}
		for ch0 in a:
			if not ch0 in kAA:
				kAA[ch0] = 0
				kAB[ch0] = 0
			if ch0 in b:
				kAA[ch0] += 1
				for ch1 in b:
					kAB[ch0] += 1

		for ch0 in b:
			if not ch0 in kBA:
				kBA[ch0] = 0
				kBB[ch0] = 0
			if ch0 in a:
				kBA[ch0] += 1
				for ch1 in a:
					kBB[ch0] += 1


		theSetA = []
		theSetB = []
		for kk in kAA:
			theSetA.append( percentageDiffIntAuto( kAA[kk], kAB[kk] ) )
		for kk in kAA:
			try:
				theSetB.append( percentageDiffIntAuto( kBA[kk], kBB[kk] ) )
			except Exception as e:
				print()
				sys.exit()

		# pp = av(theSet)
		pA = av(theSetA)
		pB = av(theSetB)

	elif alphaTest == 'b':
		tA = 0
		tB = 0
		for ch0 in a:
			if ch0 in b:
				tA += 1

		for ch0 in b:
			if ch0 in a:
				tB += 1
		pA = percentageDiffIntAuto( tA, len(a) )
		pB = percentageDiffIntAuto( tB, len(b) )

	if testing:
		print( 'pA', pA )
		print( 'pB', pB )

	zz = xMultiply(  [aa,100], [bb,0]  )
	if zz > 100:
		zz = xMultiply(  [bb,100], [aa,0]  )

	if testing:
		print([aa,100], [bb,0])
		print(  'diff', zz )
		print( [aa,bb, pA,pB] )
		print(  'av', av([aa,bb, pA,pB])  )
	ww = av([aa,bb, pA,pB])
	# if pA > pB:
	#   if pA < ww
	# print( int(ww), [aa,bb, pA,pB], a, b,  )
	return ww


def av( ds ):
	total = 0
	for x in ds:
		total+=x
	return total / len(ds)


def xMultiply( a, b ):
	fail = False
	if not type(a) == list or not type(b) == list or not len(a) == 2 or not len(b) == 2:
		fail=True

	if not b[1]:
		z = (a[1] * b[0]) / a[0]
	elif not b[0]:
		z = (a[0] * b[1]) / a[1]
	elif not a[1]:
		z = (a[0] * b[1]) / a[0]
	elif not a[0]:
		z = (a[1] * b[0]) / a[1]
	else:
		fail=True
	if fail:
		colorThis( 'Error: xMultiply' )
		colorThis( '\texpected:', 'yellow' )
		colorThis( ['\t\t', str([960,540]), str([480,0])], 'yellow' )
		colorThis( '\t\t         or' )
		colorThis( ['\t\t', str([960,540]), str([0,270])], 'yellow' )
		colorThis( '\t\t         or' )
		colorThis( ['\t\t', str([480,270]), str([960,0])], 'yellow' )
		colorThis( '\t\t         or' )
		colorThis( ['\t\t', str([480,270]), str([0,540])], 'yellow' )
		colorThis( 'fail' )
		sys.exit()
	if str(z).endswith('.0'):
		return int(z)
	else:
		return z


def percentageDiffIntAuto( smaller, bigger, isFloat=False ):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	if not isFloat:
		return percentageDiffInt(s, b)
	else:
		result = round(float((s/b)*100), 1)
		r = str(result)
		if '.0' in r:
			result = int(result)
		return result


def get_change(current, previous):

	if current == previous:
		return 100.0

	if current < previous:
		c = current
		p = previous
	else:
		p = current
		c = previous     

	try:
		return (abs(c - p) / p) * 100.0
	except ZeroDivisionError:
		return 0


def patternMatch( one, two, best=True, simple=True, both=False, unsorted=False ):
	# simple=True
	result = []
	result.append( testPatterns( one, two, simple ) )
	result.append( testPatterns( two, one, simple ) )
	if type(both) == int and both == 2:
		return result
	if not both:
		if best:
			return max(result)
		else:
			return min(result)
	else:
		if unsorted:
			return result

		if not simple:
			if result[0][0] > result[1][0]:
				return result[0],result[1]
			else:
				return result[1],result[0]
		else:
			if result[0] > result[1]:
				return result[0],result[1]
			else:
				return result[1],result[0]


def testPatterns( one, two, simple=True ):

	test = False
	spent = []
	patterns = []
	matches = []
	def tempDataset( datasetX ):
		newDataset = []
		for dat in datasetX:
			newDataset.append( dat )
		return newDataset
	def genChars( datasetY, x=False ):
		chars = []
		for d in datasetY:
			chars.append( one[d] )
			if x:
				print( one[d], d )
		return ''.join( chars )
	def addSpent( datasetY ):
		for d in datasetY:
			spent.append( d )

	def addMatch( datasetY ):
		for d in datasetY:
			if not d in matches:
				matches.append( d )

	def testSpent( datasetX ):
		for d in datasetX:
			if d in spent:
				return False
		return True

	def expandTest( datasetX ):
		if testSpent( datasetX ):
			first = datasetX[0]
			last = datasetX[len(datasetX)-1]
			theLast = len(datasetX)-1
			theMax = len(one)-1

			datasetY = tempDataset( datasetX )
			if not datasetX[0] == 0:
				nextFirst = int(first)
				for x in range(1,100000):
					nextFirst = first - 1
					if nextFirst >= 0:
						datasetY.append( nextFirst )
						datasetY.sort()
						if not genChars( datasetY ) in two:
							datasetY.pop(0)
							break
					else:
						break
			if not datasetY[len(datasetY)-1] == theMax:
				nextLast = int(datasetY[len(datasetY)-1])
				# print()
				# print( 'nextLast:', nextLast )
				for x in range(1,100000):
					# print()
					# print( nextLast, x, nextLast + x )
					nextLast = nextLast + 1
					if nextLast <= theMax:
						datasetY.append( nextLast )
						datasetY.sort()
						if not genChars( datasetY, x=False ) in two:
							datasetY.reverse()
							datasetY.pop(0)
							datasetY.reverse()
							addSpent( datasetY )
							addMatch( datasetY )
							patterns.append( genChars( datasetY ) )
							# print( '\t1' )
							break
					else:
						addSpent( datasetY )
						addMatch( datasetY )
						patterns.append( genChars( datasetY ) )
						# print( '\t2' )
						break
			else:
				addSpent( datasetY )
				addMatch( datasetY )
				patterns.append( genChars( datasetY ) )
				# print( '\t3' )

	def runTest( patternLength ):
		data = generatePatterns2( one, 2 )
		# data = generatePatterns( one, 2 )
		# print( len(data) )
		i = 0
		ii = 0
		for dataset in data:
			x = genChars( dataset )
			if x in two:
				addMatch( dataset )
				expandTest( dataset )
				# print( x )
				if test:
					print( x )
				i += 1
			else:
				ii += 1

		result = percentageDiffInt( i, len(data) )
		return result
	resultX = []

	for x in range(2,10):
		if len( one ) > x:
			resultX.append( runTest( x ) )


	newResult = percentageDiffInt( len(matches), len(one) )
	# print( patterns )
	# print( newResult )
	if simple:
		return newResult
	else:
		return newResult, tuple(patterns)


def generatePatterns( string, patternLength=2 ):

	def genP( by ):
		
		offset = 0
		dataset = []
		for offset in range(0,by):
			# print( offset )
			ix = False
			for i,char in enumerate(string):
				if i >= offset:
					ix = ( i + offset )
					
				if not type(ix) == bool:
					# dataset.append( char )
					dataset.append( i )
					if len(dataset) % by == 0:
						if len( dataset ):
							dataset.sort()
							data.append( dataset )
							# print( ''.join( dataset ) )
						dataset = []


	l = len( string )
	data = []
	genP( patternLength )
	return data


def generatePatterns2( data, patternLength=2 ):
	records = []
	m = len(data)
	for n in range(0,len(data)):
		# a = n-1
		good = True
		pl = 0
		rec = []
		new = n
		while not pl == patternLength:
			if not new < m:
				good = False
			rec.append( new )
			new+=1
			pl+=1
		b = n
		c = n+1
		# if a > -1:
		#   records.append([ a,b ])
		# if c < m:
		if good:
			records.append( rec )
	return records


def positiveResults(string,plus='',plusOr=False,end=None):
	global switch

	if plusOr or switch.isActive('PlusOr'):
		plusOr = True
	if not plus == '':
		plusInput = plus
	else:
		plusInput = switch.values('Plus').copy()
	if not end is None:
		if type( plusInput ) == str:
			plusInput += end
		else:
			for i,yh in enumerate(plusInput):
				plusInput[i] += end
		
	pi = []
	for x in plusInput:
		pi.append( ci(x) )
	plusInput = pi
	del pi
	if type( plusInput ) == str:
		if not switch.isActive('StrictCase'):
			plusInput = plusInput.lower()
		plusList = plusInput.split(',')
	else:
		for i,row in enumerate(plusInput):
			if not switch.isActive('StrictCase'):
				plusInput[i] = plusInput[i].lower()
		plusList = plusInput
	length = len(plusList)
	cnt = 0
	result = False
	if not switch.isActive('StrictCase'):
		string = string.lower()
	# print( plusList )
	# sys.exit()
	for s in plusList:
		if not switch.isActive('StrictCase'):
			s = s.lower()
		
		if len(s) > 1 and s[0] == '*':
			s = s.replace('*','')
			if string.endswith(s):
				cnt += 1
		elif len(s) > 1 and s[-1] == '*':
			s = s.replace('*','')
			if string.startswith(s):
				cnt += 1
		elif not switch.isActive('PlusDuplicate') and (  not string.find(ci(s)) == -1 or s in string  ):
			cnt += 1
		elif switch.isActive('PlusDuplicate') and (  string.count(ci(s)) > 1 or string.count(s) > 1 ):
			cnt += 1
		# if 'opus' in string:
		#   print(cnt, string)
		if length == cnt:
			result = True
			break
		if plusOr:
			if cnt > 0:
				result = True
	return result


def stripColor(text):
	if '0m' in text and '[' in text:
		pass
	else:
		return text
	import re
	ansi_escape = re.compile(r'''
		\x1B  # ESC
		(?:   # 7-bit C1 Fe (except CSI)
			[@-Z\\-_]
		|     # or [ for CSI, followed by a control sequence
			\[
			[0-?]*  # Parameter bytes
			[ -/]*  # Intermediate bytes
			[@-~]   # Final byte
		)
	''', re.VERBOSE)
	return ansi_escape.sub('', text)


def colorPlus( data, color='green' ):
	for search in switch.values('Plus'):
		for subject in caseUnspecific( data, search, isPlus=True ):

			if type( subject ) == str:
				data = data.replace( subject, colorThis( subject, color, p=0 ) )
			else:
				if subject['pos'] == 'first':
					data = nth_repl(data, subject['data'], colorThis( subject['data'], color, p=0 ), 1)
				else:
					cx = data.count( subject['data'] )
					data = nth_repl(data, subject['data'], colorThis( subject['data'], color, p=0 ), cx)
	return data


def nth_repl(s, sub, repl, nth):

	# first and only thing a got online

	find = s.find(sub)
	# if find is not p1 we have found at least one match for the substring
	i = find != -1
	# loop util we find the nth or we find no match
	while find != -1 and i != nth:
		# find + 1 means we start at the last match start index + 1
		find = s.find(sub, find + 1)
		i += 1
	# if i  is equal to nth we found nth matches so replace
	if i == nth:
		return s[:find]+repl+s[find + len(sub):]
	return s


def caseUnspecific( data, subject, isPlus=False, minus=None ):

	if not minus is None:
		if type(minus) == list:
			for remove in minus:
				for deleteThis in caseUnspecific( data, remove.lower(), isPlus=False ):
					data = data.replace( deleteThis, '' )
		elif type(minus) == str:
			for deleteThis in caseUnspecific( data, minus.lower(), isPlus=False ):
				data = data.replace( deleteThis, '' )

	results = []
	subject = subject.lower()
	if isPlus:
		if '*' in subject and len(subject) > 1:
			if subject.startswith('*'):
				subject = subject.replace( '*', '' )
				subject = ci(subject)
				if data.lower().endswith( subject ):
					return [{ 'data': data[-len(subject):], 'pos': 'last' }]
				return []
			if subject.endswith('*'):
				subject = subject.replace( '*', '' )
				subject = ci(subject)
				if data.lower().startswith( subject ):
					return [{ 'data': data[:len(subject)], 'pos': 'first' }]
				return []
		subject = ci(subject)
			

	while data.lower().find( subject ) > -1:
		scanning = data.lower().find( subject )
		subjectY = ''
		scanComplete = False
		while not scanComplete:
			if len(subjectY) == len(subject):
				scanComplete = True
			elif scanning > len(data)-1:
				scanComplete = True
			else:
				subjectY += data[ scanning ]
			scanning += 1
		if not subjectY in results:
			results.append( subjectY )
		data = data.replace( subjectY, '' )
	return results


def plusColor( row, color='green' ):
	# row = thePrintLine

	if switch.isActive('Plus'):
		thePrintLine = row
		for plusSearchX in switch.values('Plus'):
			plusSearchX = ci( plusSearchX )

			for subject in caseUnspecific( row, plusSearchX ):
				row = thePrintLine.replace( subject, colorThis( subject, color , p=0 ) )

	return row


def listColor( text, rows, color='green' ):
	return text
	r = text

	# print( 'HERE', r )
	txtCNT = text.lower()
	for row in rows:

		loc = txtCNT.find( row )
		if row in txtCNT:
			print( 'loc:', loc )
			if loc:
				r = ''
				for i,char in enumerate(text):
					if i >= loc and i <= len(row)-1:
						print( char )
						r += colorThis( char, color, p=0 )
					else:
						r+=char
	return r
row_colors = []

row_colors.append([ 0, Background.blue ])
row_colors.append([ 0, Background.light_blue ])
row_colors.append([ 0, Background.purple ])

row_colors.append([ 1, BackgroundGrey.red ])
row_colors.append([ 1, BackgroundGrey.brown ])
row_colors.append([ 1, BackgroundGrey.blue ])

row_colors.append([ 2, Color.cyan ])
row_colors.append([ 2, Color.green ])

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


def colorizeRow( row, tableID=False, prefix='', prefixColor='', haltColorShift=False ):
	global colorizeRow_last
	if len(prefix) and len(prefixColor):
		prefix = colorThis( prefix, prefixColor, p=0 )
	global switch
	if switch.isActive( 'NoColor' ):
		print( row )
		return False

	if type(tableID) == bool:
		tableID = __.color_palette
	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		print( row )
	else:
		if _str.hasVisible(row):
			up =True
		else:
			up =False
		# print( 'tableID:', tableID, colorID( tableID ) )
		# print( str(len(row))+colorID( tableID, up ) + row + Background.end )
		if colorizeRow_last is None or not haltColorShift:
			colorizeRow_last = colorID( tableID, up )
		print( prefix + colorizeRow_last + row + Background.end )


def printColor( string, color='red' ):

	global switch
	if switch.isActive( 'NoColor' ):
		print( string )
		return False

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'red':
		print( Color.red + string + Color.end )
	elif color == 'cyan':
		print( Color.cyan + string + Color.end )
	elif color == 'darkcyan' or color == 'grey':
		print( Color.darkcyan + string + Color.end )
	elif color == 'blue':
		print( Color.blue + string + Color.end )
	elif color == 'green':
		print( Color.green + string + Color.end )
	elif color == 'yellow':
		print( Color.yellow + string + Color.end )
	elif color == 'underline':
		print( Color.underline + string + Color.end )


def inlineColorGroup( row, tableID=False ):

	global switch
	if switch.isActive( 'NoColor' ):
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
		if _str.hasVisible(row):
			up =True
		else:
			up =False
		# print( 'tableID:', tableID, colorID( tableID ) )
		return colorID( tableID, up ) + row + Background.end

# switches = Switches()




############################################################## copy-fn-class


def myFileLocations( file, silent=False, currentBaseVersion=3 ):

	if not type( __.trigger_isPipe ) == bool:
		if 'glob' in __.trigger_isPipe:
			glob = __.imp('glob')
			g = glob.glob(file)
			for f in g:
				myFileLocations( f, silent, currentBaseVersion )
			file = g

	# print(__.myFileLocations_SKIP_VALIDATION)
	# print(os.path.isdir(file))
	# print(file)
	# sys.exit()
	global appData
	if __.myFileLocations_SKIP_VALIDATION:
		if type( appData[__.appReg]['pipe'] ) == bool:
			appData[__.appReg]['pipe'] = []
		appData[__.appReg]['pipe'].append( file )
		return file
	# print( 'HERE HERE HERE HERE ', file )
	if '*' in file:
		import glob
		appData[__.appReg]['pipe'] = glob.glob(file)
		return appData[__.appReg]['pipe']

	global myFileLocation_File
	global backup_subject_files
	if type(__.myFileLocations_SKIP_VALIDATION) == bool and __.myFileLocations_SKIP_VALIDATION:
		# print('here')
		# sys.exit()
		if type( appData[__.appReg]['pipe'] ) == bool:
			appData[__.appReg]['pipe'] = []
			return None
		appData[__.appReg]['pipe'].append( file )
		return None
	# if ',' in file and not os.path.isfile( file ):
	#   nFiles = []
	#   for f in file.split(','):
	#       nFiles.append( myFileLocations2( f, silent, currentBaseVersion ) )
	#   file = ','.join( nFiles )
		
	# else:
	#   myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )

	myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )
	if  not myFileLocation_File in myFileLocation_Files:
		myFileLocation_Files.append( myFileLocation_File )
	try:
		autoAbbreviations()
	except Exception as e:
		pass
	if len( myFileLocation_Files ):
		# print('xxx')
	# if len( myFileLocation_Files ) and type( appData[__.appReg]['pipe'] ) == bool:
		if not type( __.trigger_isPipe ) == bool:
			# print( 'HERE', myFileLocation_Files )
			__.appRegPipe = __.appReg

			if 'name' in __.trigger_isPipe:
				justNames = True
			else:
				justNames = False

			tmpFiles = []
			hasFiles = False
			if justNames:
				# print( 'HERE' )
				# setPipeData( myFileLocation_Files, __.appReg )

				if type( appData[__.appReg]['pipe'] ) == bool:
					appData[__.appReg]['pipe'] = []
				for thisFile in myFileLocation_Files:
					# if os.path.isfile( thisFile ):
					if not thisFile in myFileLocation_Pipe:
						myFileLocation_Pipe.append( thisFile )
						appData[__.appReg]['pipe'].append( thisFile )
			else:
				for thisFile in myFileLocation_Files:
					if os.path.isfile( thisFile ):
						hasFiles = True
						if not thisFile in myFileLocation_Pipe:
							myFileLocation_Pipe.append( thisFile )
							if type( appData[__.appReg]['pipe'] ) == bool:
								appData[__.appReg]['pipe'] = []
							if 'clean' in __.trigger_isPipe:
								for row in getText( thisFile, raw=True, clean=True ).split('\n'):
									appData[__.appReg]['pipe'].append( row )
									# tmpFiles.append( row )
							else:
								for row in getText( thisFile, raw=True ).split('\n'):
									appData[__.appReg]['pipe'].append( row )
									# tmpFiles.append( row )
			# if hasFiles:
			#   if 'clean' in __.trigger_isPipe:
			#       setPipeData( tmpFiles, __.appReg, clean=True )
			#   else:
			#       setPipeData( tmpFiles, __.appReg, clean=False )
			if not hasFiles:
				if type( appData[__.appReg]['pipe'] ) == bool:
					appData[__.appReg]['pipe'] = []
					for row in myFileLocation_Files:
						appData[__.appReg]['pipe'].append( row )



	return myFileLocation_File


def setPipeData( data, theFocus=False, clean=True ):
	global appData
	if type( theFocus ) == bool:
		theFocus = __.appReg
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		appData[theFocus]['pipe'] = []
		if not clean:
			appData[theFocus]['pipe'].append('')
		for pd in data:
			if clean:
				pd = pd.replace('\n','')
				pd = pd.replace('\r','')
				if not pd == '':
					appData[theFocus]['pipe'].append(pd)
			else:
				appData[theFocus]['pipe'].append(pd)
		setPipeDataRan = True


def autoAbbreviations():
	global printAutoAbbreviations_scheduled
	# return False
	global myFileLocation_File
	if not type( myFileLocation_File ) == bool:
		if not len( appInfo[__.appReg]['columns'] ) and myFileLocation_File.lower().endswith('.json'):
			
			printAutoAbbreviations_scheduled = True
			data = []
			groups = {}
			myFileLocation_File_Data = getTable2( myFileLocation_File )
			if type( myFileLocation_File_Data ) == dict:
				myFileLocation_File_Data = [myFileLocation_File_Data]
			for i,key in enumerate( myFileLocation_File_Data[0].keys()):
				# print( key )
				record = {}
				record['id'] = i
				record['key'] = key
				record['first'] = key[:1].lower()
				record['second'] = key[:2].lower()
				record['third'] = key[:3].lower()
				wf = ''
				for w in key.replace( '_', ' ' ).split( ' ' ):
					wf += w[:1].lower()
				record['firstofword'] = wf


				for k in record.keys():
					try:
						if not type(groups[ k ]) == dict:
							groups[ k ] = {}
					except Exception as e:
						groups[ k ] = {}

					try:
						if not type(groups[ k ][ record[k] ]) == dict:
							groups[ k ][ record[k] ] = {}
					except Exception as e:
						groups[ k ][ record[k] ] = {}
						groups[ k ][ record[k] ]['ids'] = []


				for k in record.keys():
					groups[ k ][ record[k] ]['ids'].append( i )
				
				data.append( record )


			approvedAbbreviations= []
			flag = False
			flagged= []

			for k in groups['first'].keys():
				approvedAbbreviations.append({ 'key': data[groups['first'][k]['ids'][0]]['key'], 'abbreviations': k })
				if not len(groups['first'][k]['ids']) == 1:
					flag = True
					for i,idx in enumerate(groups['first'][k]['ids']):
						if not i == 0:
							flagged.append({ 'first': k, 'id': idx, 'assigned': False })

			
			if flag:
				flagsResolved = 0
				for k in groups['firstofword'].keys():
					if len(k) > 1:
						for x in groups['firstofword'][k]['ids']:
							for i,f in enumerate(flagged):
								if not flagged[i]['assigned']:
									if flagged[i]['id'] == x:
										flagsResolved += 1
										flagged[i]['assigned'] = True
										approvedAbbreviations.append({ 'key': data[x]['key'], 'abbreviations': k })

				if not flagsResolved == len(flagged):
					for k in groups['second'].keys():
						for x in groups['second'][k]['ids']:
							for i,f in enumerate(flagged):
								if not flagged[i]['assigned']:
									if flagged[i]['id'] == x:
										flagsResolved += 1
										flagged[i]['assigned'] = True
										approvedAbbreviations.append({ 'key': data[x]['key'], 'abbreviations': k })

				if not flagsResolved == len(flagged):
					for k in groups['third'].keys():
						for x in groups['third'][k]['ids']:
							for i,f in enumerate(flagged):
								if not flagged[i]['assigned']:
									if flagged[i]['id'] == x:
										flagsResolved += 1
										flagged[i]['assigned'] = True
										approvedAbbreviations.append({ 'key': data[x]['key'], 'abbreviations': k })         

				if not flagsResolved == len(flagged):
					for i,f in enumerate(flagged):
						if not flagged[i]['assigned']:
							print( 'Error: abbreviation', data[flagged[i]['id']]['key'] )


			# printVar( groups )
			# printVar( data )

			for aa in approvedAbbreviations:
				appInfo[__.appReg]['columns'].append({'name': aa['key'], 'abbreviation': aa['abbreviations']})
			if switches.isActive('PrintAutoAbbreviations'):
				print()
				print('Columns and abbreviations:')
				result = ''
				for col in appInfo[__.appReg]['columns']:
					result += col['name'] + '(' + col['abbreviation'] + '), '
				result = result[:-2]
				print('\t' + result + '\n')
				print()

			defaultScriptTriggers()


def myFileLocations2( file, silent=False, currentBaseVersion=3 ):
	if __.myFileLocations_SKIP_VALIDATION:
		return file
	global myFileLocation_Print
	silentSetTo = myFileLocation_Print
	if silent:
		silentSetTo = silent

	if os.path.isfile( file ):
		return file

	if 'tmpf' in file.lower():
		fx = file.lower()
		if 'tmpf' == fx:
			return _v.tmpf
		elif 'tmpf0' == fx:
			return _v.tmpf0
		elif 'tmpf1' == fx:
			return _v.tmpf1
		elif 'tmpf2' == fx:
			return _v.tmpf2
		elif 'tmpf3' == fx:
			return _v.tmpf3
		elif 'tmpf4' == fx:
			return _v.tmpf4
		elif 'tmpf5' == fx:
			return _v.tmpf5
		elif 'tmpf6' == fx:
			return _v.tmpf6
		elif 'tmpf7' == fx:
			return _v.tmpf7
		elif 'tmpf8' == fx:
			return _v.tmpf8
		elif 'tmpf9' == fx:
			return _v.tmpf9
		return file

	probableLocations = [
		"_v.myAppsPy + _v.slash+'_rightThumb'+_v.slash + '_' + '*THEFILENAME*' + _v.slash+'__init__.py'",
		"_v.myAppsPy + _v.slash+''+_v.slash + '*THEFILENAME*' + '.py'",
		"_v.myAppsPy + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myTables + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'batch'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'batch'+_v.slash + '*THEFILENAME*' + '.bat'",
		"_v.myDatabases + _v.slash+''+_v.slash + '*THEFILENAME*'",

		"os.environ['USERPROFILE'] + _v.slash+'Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'Downloads'+_v.slash + '*THEFILENAME*'",

		"os.environ['HOME'] + _v.slash+'Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['HOME'] + _v.slash+'Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['HOME'] + _v.slash+'Downloads'+_v.slash + '*THEFILENAME*'",
		
		"_v.myTXT + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'exe'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'php'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'php'+_v.slash + '*THEFILENAME*' + '.php'",
		"_v.myApps + _v.slash+'powershell'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'vbs'+_v.slash + '*THEFILENAME*'",
	]

	if file == 'base':
		file = 'base' + str( currentBaseVersion )

	if True:
		for testThis in probableLocations:
			try:
				theTest = eval( testThis )
				# print()
				# print(theTest)
				theTest = theTest.replace( '*THEFILENAME*', file )
				# print(os.path.isfile( theTest ),theTest)
				if os.path.isfile( theTest ):
					if silentSetTo:
						
						print()
						print( 'File not here but in:', theTest )
						print()

					return theTest
			except Exception as e:
				pass
	
	if not os.path.isfile( _v.relevant_folders ):
		print( 'generateRelevantFolders' )
		import generateRelevantFolders
		generateRelevantFolders.action()

	if os.path.isfile( _v.relevant_folders ):
		for fld in getText( _v.relevant_folders, raw=True, clean=1 ).split('\n'):
			if os.path.isfile( fld  +_v.slash+  file ):
				return fld  +_v.slash+  file
			if 'ext' in __.specifications:
				if os.path.isfile( fld  +_v.slash+  file+ __.specifications['ext'] ):
					return fld  +_v.slash+  file
			# print(fld)

	return file


def myFolderLocations( data ):
	# print(data)
	if type(data) == list:
		for i,d in enumerate(data):
			data[i] = myFolderLocations(d)
		return data

	if os.path.isdir(data):
		return os.path.abspath(data)
	

	global bmIndex
	
	if not len(bmIndex):
		bmIndex = getTable( 'bookmarks.index' )

	# print( bmIndex )
	if data in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data])
	if data.lower() in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data.lower()])
	if data.upper() in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data.upper()])
	if data.title() in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data.title()])


	return data





