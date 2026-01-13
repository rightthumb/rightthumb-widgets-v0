import sys

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
from os.path import isfile, isdir
import uuid
from operator import itemgetter
from datetime import datetime as dt, timedelta
import datetime
import time
from threading import Timer
from datetime import date
import simplejson as json
import sqlite3

import pyperclip

import colorama
colorama.init()


import _rightThumb._construct as __
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._profileVariables as _profile

# oc = list(filter(lambda data: data['open'] == pos, record['oc']))
__.loadingVar = {
					'hasLoaded': False,
					'hasCleared': False,
					'isRunning': False,
					'done': False,
}


__.loadingVar['hasLoaded'] = False
__.loadingVar['hasCleared'] = False
__.loadingVar['isRunning'] = False

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




def LoadingDone(done=None):
	if not done is None:
		__.loadingVar['done'] = done
	__.loadingVar['hasLoaded'] = True
	
	global threads
	while not __.loadingVar['hasCleared']:
		time.sleep( .2 )
	time.sleep( .7 )
	print( '                                                        ', end='\r' )
	time.sleep( 2 )
	__.loadingVar['hasCleared'] = False
	__.loadingVar['hasLoaded'] = False
	__.loadingVar['isRunning'] = False
	del threads
	threads = Queue()

def loadingAnimation(loading='Searching',done='Found' ):
	__.loadingVar['done'] = done
	if not __.loadingVar['isRunning']:
		__.loadingVar['isRunning'] = True
		global threads
		theID = 'loadingAnimation_'+loading+'_' + genUUID()
		threads.add( theID ) # kwargs 
		threads.maxThreadsSafe = 225
		threads.autoLoadedAfter = .1
		threads.scheduleLoop = .01
		threads.auditLoop = .1
		threads.projectDataMaxLen = 500
		threads.report = False
		threads.auditPrint = False
		threads.add( theID, loadingGif, [loading] )


def loadingGif(loading, qID=False):
	global threads
	gif = [
			'       *',
			'      **',
			'     ***',
			'    *** ',
			'   ***  ',
			'  ***   ',
			' ***    ',
			'***     ',
			'**      ',
			'*       ',
			'**      ',
			'***     ',
			' ***    ',
			'  ***   ',
			'   ***  ',
			'    *** ',
			'     ***',
			'      **',
	]
	print( '                                                                                                                                                                                                      ', end='\r' )
	while not __.loadingVar['hasLoaded']:
		print( '                                                                                                                                                                                                      ', end='\r' )
		for x in gif:
			animate = colorThis( x, 'red', p=0 )
			print( '                                                                                                                                                                                                                                                                                          ', end='\r' )
			print( '        {' + animate + '} '+loading+'...', end='\r' )
			time.sleep( .4 )
		print( '                                                                                                                                                                                                      ', end='\r' )
	print( '                                                                                                                                                                                                      ', end='\r' )
	print( '        '+colorThis( __.loadingVar['done'], 'green', p=0 ), end='\r' )
	if not type(qID) == bool:
		threads.spent( qID, sys.getsizeof( 'obj') )
	__.loadingVar['hasCleared'] = True

		


server_proxy = []
server_proxy.append( '' )
server_proxy.append( 'http://www.rightthumb.com/projects/widget/proxy.php?p=' )
server_proxy.append( 'http://rephrecruiting.com/proxy.php?p=' )
server_proxy.append( 'http://www.pillerbeauty.com/proxy.php?p=' )
server_proxy.append( 'http://signaturemassageandfacialspa.com/p.php?p=' )
server_proxy.append( 'https://signaturemassagetampa.com/payroll/p.php?p=' )

appProxy = 'appProxy.json'

ipsum = None
def ipsumSentence():
	global ipsum
	if ipsum is None:
		ipsum = getText( _v.ipsum, raw=True, clean=2 )
	ipsum = ipsum.replace( '\n', ' ' )
	sentences = []
	for sentence in ipsum.split('.'):
		sentence = _str.replaceDuplicate( sentence, ' ' )
		sentence = _str.cleanBE( sentence, ' ' )
		sentence = sentence + '.'
		sentences.append({ 'sentence': sentence, 'sortBy': genUUID() })

	randomized = tables.returnSorted( 'data', 'd.sortBy', sentences )
	return randomized[0]['sentence']

def ipsumParagraph( count=1, shouldPrint=False, returnList=False, lorem=True ):
	global ipsum
	if ipsum is None:
		ipsum = getText( _v.ipsum, raw=True, clean=2 )
	paragraphs = []
	for item in ipsum.split('\n'):
		item = _str.replaceDuplicate( item, ' ' )
		item = _str.cleanBE( item, ' ' )
		item = item + '.'
		item = _str.replaceDuplicate( item, '.' )
		paragraphs.append({ 'paragraph': item, 'sortBy': genUUID() })

	randomized = tables.returnSorted( 'data', 'd.sortBy', paragraphs )

	result = []

	i=0
	while not i == count:
		result.append( randomized[i]['paragraph'] )
		i+=1

	if lorem:
		result[0] = 'Lorem ipsum ' + result[0][0].lower() + result[0][1:]

	

	if shouldPrint:
		data = '\n\n'.join( result )
		print( data )

	if returnList:
		return result
	else:
		return '\n\n'.join( result )


def csv(file, save=False, json_file='',printThis=True):
	import csv
	if type(save) == str:
		json_file = save
		save = True

	elif len(json_file):
		save = True
	elif save and json_file == '':
		json_file = changeExtension( row, 'json' )
	csv_rows = []
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		title = reader.fieldnames
		# print( title )
		# for t in title:
		#     print( t )
		for row in reader:
			csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
		csv_rows = convertTimestamp( csv_rows )
		if save:
			saveTable2(csv_rows,json_file)
			if printThis:
				printBold( json_file, 'green' )
		return csv_rows
	return False

def convertTimestamp( data ):
	if not len( data ):
		return data
	if not 'timestamp' in data[0].keys():
		return data
	if 'datetime' in data[0].keys():
		hasDateTime = True
	else:
		hasDateTime = False
	for i,record in enumerate(data):
		try:
			if len( record['timestamp'] ):
				if isFloat( str(record['timestamp']) ):
					if not hasDateTime:
						data[i]['datetime'] = resolveEpoch( data[i]['timestamp'] )
					else:
						return data
				else:
					data[i]['timestamp'] = autoDate( record['timestamp'] )
					if not hasDateTime:
						data[i]['datetime'] = resolveEpoch( data[i]['timestamp'] )
		except Exception as e:
			return data
	return data

def changeExtension( file, ext ):
	f = removeExtension( file )
	if not '.' in ext:
		return f + '.' + ext
	else:
		return f + ext

def getExtension(string):

	ext0 = string.split('.')
	extId = len(ext0) - 1
	if extId > 0:
		ext = ext0[extId]
	else:
		ext = ''
	return ext
def removeExtension(string):
	if not '.' in string:
		return string
	ext = getExtension(string)
	sl = len(string)
	el = len(ext)
	dl = (sl - el) - 1
	file = ''
	for i,n in enumerate(string):
		if i < dl:
			file += n

	return file


def registerSpent( app, spentID ):
	global appProxy
	data = getTable( appProxy )
	for i,record in enumerate(data):
		if record['app'] == app:
			pass
	saveTable( appProxy )

# colorizeRow
# printBold

__.color_palette = 0

# from timeout import timeout
plusClose = 70
autoBackupData = False
autoLoadData = False

idResolution = []

theExtensionsList = []
relevantFolders = []
setPipeDataRan = False

__.columnAbbreviations = 1

# print( 'make pattern algorithm for pattern IDs' )

# def testPatterns( two, one ):

def saveData( rows, theFile, printThis=True ):

	if theFile.lower().endswith( '.json' ):
		if _v.slash in theFile:
			saveTable2( rows, theFile, printThis )
			if printThis:
				print( 'Saved: ', theFile )
		else:
			saveTable( rows, theFile, printThis )
		return True

	if theFile.lower().endswith( '.txt' ):
		if _v.slash in theFile:
			saveText( rows, theFile )
			if printThis:
				print( 'Saved: ', theFile )
		else:
			if os.path.isfile( _v.myTables + _v.slash + theFile ):
				saveText( rows, _v.myTables + _v.slash + theFile )
			else:
				saveText( rows, _v.myTables + _v.slash + theFile )
			if printThis:
				print( 'Saved: ', _v.myTables + _v.slash + theFile )
		return True

	location = theFile
	if os.path.isfile( theFile ):
		found = True
	
	if not os.path.isfile( theFile ):
		found = False
		if not _v.slash in theFile:
			if not '.' in theFile:
				if os.path.isfile( _v.myTables + _v.slash + theFile + '.json' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.json'
				elif os.path.isfile( _v.myTables + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.txt'
				elif os.path.isfile( _v.myTables + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.txt'
			else:
				if os.path.isfile( _v.myTables + _v.slash + theFile ):
					found = True
					location = _v.myTables + _v.slash + theFile
				elif os.path.isfile( _v.myTables + _v.slash + theFile ):
					found = True
					location = _v.myTables + _v.slash + theFile


	if found:
		if location.lower().endswith( '.json' ):
			saveTable2( rows, location, printThis )
			if printThis:
				print( 'Saved: ', location )
			return True

		if location.lower().endswith( '.txt' ):
			saveText( rows, location )
			if printThis:
				print( 'Saved: ', location )
			return True


	t = type( rows )
	if t == str:
		location = _v.myTables + _v.slash + theFile + '.txt'
		saveText( rows, location )
		if printThis:
			print( 'Saved: ', location )
		return True

	if t == dict:
		saveTable( rows, theFile+'.json', printThis )
		return True
	if t == list:
		if len(rows) == 0:
			print( 'Error: no data to save' )
			return False

		t = type( rows[0] )
		if t == dict:
			saveTable( rows, theFile+'.json', printThis )
			return True
		pass
		if t == str:
			location = _v.myTables + _v.slash + theFile + '.txt'
			saveText( rows, location )
			if printThis:
				print( 'Saved: ', location )
			return True

	print( 'Error: unable to save file' )
	return False







def getData( theFile, exitOnError=False ):
	location = theFile
	if os.path.isfile( theFile ):
		found = True
	
	if not os.path.isfile( theFile ):
		found = False
		if not _v.slash in theFile:
			if not '.' in theFile:
				if os.path.isfile( _v.myTables + _v.slash + theFile + '.json' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.json'
				elif os.path.isfile( _v.myTXT + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTXT + _v.slash + theFile + '.txt'
				elif os.path.isfile( _v.myTables + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.txt'
			else:
				if os.path.isfile( _v.myTables + _v.slash + theFile ):
					found = True
					location = _v.myTables + _v.slash + theFile
				elif os.path.isfile( _v.myTXT + _v.slash + theFile ):
					found = True
					location = _v.myTXT + _v.slash + theFile

		if not found:
			print( 'Error: unable to locate file' )
			if exitOnError:
				sys.exit()
			return []



	if not os.path.isfile( theFile ):
		if location.lower().endswith( '.json' ):
			return getTable2( location )



	file = getText( location, raw=True, clean=1 )
	textList = file.split('\n')
	if '[' in textList or '{' in textList:
		data = eval( file )
	else:
		data = textList
	return data



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


def colorHelp( ipsum=False ):
	colorList = [
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
	for sample in colorList:
		if not len( sample ):
			print()
		else:
			result = eval( sample + '+ "THE_TEXT" + Color.end' )
			if ipsum:
				result = result.replace( 'THE_TEXT', ipsumSentence() )
			else:
				result = result.replace( 'THE_TEXT', sample )
			
			print( result )
	sys.exit()


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

	global switches
	if switches.isActive( 'NoColor' ):
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
		print( colorID( tableID, up ) + row + Background.end )





def colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False,    p=True ):

	if not p:
		shouldPrint = False

	if type(strings) == list:

		for i,x in enumerate(strings):
			strings[i] = str( x )

		string = ' '.join( strings )
	else:
		string = str(strings)

	if ipsum:
		string = ipsumSentence()

	found = False

	if color == 'help':
		print()
		print()
		print( "_.colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False )" )
		print()
		print()
		colorHelp( ipsum )


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
		printBold( 'Error: _.colorThis: color not found ' + str(color), 'red' )
		colorHelp( ipsum )

		sys.exit()

	if shouldPrint:
		print( result )

	return result






def inlineColor( string, color='red' ):

	global switches
	if switches.isActive( 'NoColor' ):
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


def printColor( string, color='red' ):

	global switches
	if switches.isActive( 'NoColor' ):
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


def printBold( string, color='white' ):

	global switches
	if switches.isActive( 'NoColor' ):
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


def inlineColorGroup( row, tableID=False ):

	global switches
	if switches.isActive( 'NoColor' ):
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


def inlineBold( string, color='white' ):

	global switches
	if switches.isActive( 'NoColor' ):
		return string
	
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

def patternMatch( one, two, best=True, simple=True, both=False, unsorted=False ):
	# simple=True
	result = []
	result.append( testPatterns( one, two, simple ) )
	result.append( testPatterns( two, one, simple ) )
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
		data = generatePatterns( one, 2 )
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



def generatePatterns( string, patternLength ):

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
							data.append( dataset )
							# print( ''.join( dataset ) )
						dataset = []


	l = len( string )
	data = []
	genP( patternLength )
	return data



def stringDiff( one, two ):
	one = one.lower()
	two = two.lower()
	appropriate = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

	if len(one) > len(two):
		a = len(one)
		b = len(two)
	else:
		b = len(one)
		a = len(two)
	d = a - b
	# if d > 2:
	#     return False
	setA = 0
	theTotal_one = 0
	theTotal_two = 0
	for x in appropriate:
		if x in two:
			theTotal_two += 1
		if x in one:
			theTotal_one += 1
		if x in one and x in two:
			setA += 1

	resultX = []
	resultX.append(percentageDiffInt( setA, theTotal_one ))
	resultX.append(percentageDiffInt( theTotal_one, theTotal_two ))
	resultX.append(percentageDiffInt( theTotal_one, theTotal_two ))
	resultX.append( testPatterns( one, two ) )
	result = max(resultX)
	
	# resultY = []
	# resultY.append(min(resultX))
	# resultY.append(patternMatch( one, two ))
	# result = max(resultY)
	# print()
	# print( setA, theTotal_one )
	# print( resultX, one, two )

	return result



def fromEpoch( epoch ):
	return datetime.datetime.fromtimestamp(epoch).strftime('%c')

def postLoad( file, epoch=0, theFocus=False ):
	global autoLoadData
	global switches
	global appData
	


	try:
		__.appInfoScan
	except Exception as e:
		if not type( theFocus ) == bool:
			theFocus = theFocus
		else:
			theFocus = __.appReg

		# print( 'theFocus:', theFocus )
		# printVar( appData )
		if type( appData[theFocus]['pipe'] ) == bool:
			hasPipeData = False
		else:
			hasPipeData = True

		if type( myFileLocation_File ) == bool:
			hasFile = False
		else:
			hasFile = True

		if __.isRequired_Pipe_or_File and not hasFile and not hasPipeData:
			print(  )
			print( inlineBold('Error:','red')+inlineBold(' Pipe')+' data or '+inlineBold('File')+' is required' )
			print(  )
			sys.exit()

		if __.isRequired_Pipe and not hasPipeData:
			print(  )
			print( 'Error: Pipe data is required' )
			print(  )
			sys.exit()

		if not type( __.isRequired_or_List ) == bool:
			meetsRequirements = False


			if 'Pipe' in __.isRequired_or_List and not hasFile and not hasPipeData:
				pass
			else:
				meetsRequirements = True
			for check in __.isRequired_or_List:
				if switches.isActive(check):
					meetsRequirements = True
			if not meetsRequirements:
				print(  )
				print( inlineBold( 'Error:', 'red' ) + ' One of the following is required:', ', '.join( __.isRequired_or_List ) )
				print(  )
				sys.exit()


		


		appDBA = __.thisApp( file )

		if switches.isActive( 'LoadEpoch' ):
			if '.' in switches.value( 'LoadEpoch' ):
				autoLoadData = True
				epoch = float( switches.value( 'LoadEpoch' ) )
		if autoLoadData and epoch == 0:
			if type( autoLoadData ) == str:
				if '.' in autoLoadData:
					epoch = float( autoLoadData )
			if type( autoLoadData ) == float:
				epoch = autoLoadData

			if epoch == 0:
				autoLoadData = False


		if autoLoadData:
			reclaimAcquiredData( appDBA, epoch, theFocus )
		else:
			releaseAcquiredData( appDBA, theFocus )



def releaseAcquiredData( appDBA, theFocus ):
	global autoBackupData
	global switches
	global appData
	global myFileLocation_Files
	global switches
	log = _v.appLogs() + _v.slash+'execution_receipt-' + appDBA + '-' + str( __.startTime ) + '.json'
	rebuiltCommandRaw = theCommand( appDBA, printThis=False, separate=True )
	if len( rebuiltCommandRaw[1] ):
		rebuiltCommand = rebuiltCommandRaw[0] + ' ' + rebuiltCommandRaw[1]
		rebuiltCommandEpoch = rebuiltCommandRaw[0] + ' -loadEpoch ' + str( __.startTime ) + ' ' + rebuiltCommandRaw[1]
	else:
		rebuiltCommand = rebuiltCommandRaw[0]
		rebuiltCommandEpoch = rebuiltCommandRaw[0] + ' -loadEpoch ' + str( __.startTime ) 
	# print( log )
	# print( rebuiltCommandRaw )


	# autoBackupData = True



	info = {
				'epoch': __.startTime,
				'app': appDBA,
				'rebuiltCommand': rebuiltCommand,
				'rebuiltCommandEpoch': rebuiltCommandEpoch,
				'files': [],
				'switches': switches.getTable(),
	}

	if not autoBackupData:
		saveTable2( info, log )

	if autoBackupData:
		if len( myFileLocation_Files ):
			for i,file in enumerate(myFileLocation_Files):
				try:
					thisName = 'files-' + appDBA + '-' + str( __.startTime ) + '_file' + str(i) + '.cache'
					tmpData = getText( file )
					saveText( tmpData, _v.myAppLogs + _v.slash + thisName )
					info['files'].append( thisName )

				except Exception as e:
					pass

		# print( theFocus, type( appData[theFocus]['pipe'] ) )
		if not type( appData[theFocus]['pipe'] ) == bool:
			thisName = 'files-' + appDBA + '-' + str( __.startTime ) + '_pipe' + '.cache'
			saveText( appData[theFocus]['pipe'], _v.myAppLogs + _v.slash + thisName )
			info['files'].append( thisName )
		

		saveTable2( info, log )

		# print()
		# print()
		# printVar( info )

	# 
# _.theCommand( __file__ )
# file0 = _v.myTables + _v.slash+'applogs'+_v.slash + log

def reclaimAcquiredData( appDBA, epoch, theFocus=False ):
	global switches
	if not type( theFocus ) == bool:
		appReg = theFocus
	else:
		appReg = __.appReg

	log = _v.appLogs() + _v.slash+'execution_receipt-' + appDBA + '-' + str( epoch ) + '.json'
	info = getTable2( log )
	# print( log )
	# print( info )
	# printVar( info )

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
		# printVar( switchData )
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


	if switches.onlyLoadEpoch( theFocus=appReg ):
		switchData = rebuildSwitches( info['switches'] )
	else:
		switchData = rebuildFiles( info['switches'] )
	# printVar( switchData )
	switches.loadTable( switchData, theFocus=appReg )
	# print( 'theFocus:', theFocus )

	if not type( pipeFile() ) == bool:
		appData[appReg]['pipe'] = getText( pipeFile() )





def theCommand( file='', theFocus=False, printThis=True, justSwitches=False, separate=False ):
	global switches
	# _.theCommand( __file__, theFocus=False, printThis=True, justSwitches=False  )
	
	if not type( theFocus ) == bool:
		appReg = theFocus
	else:
		appReg = __.appReg
	if len( file ):
		if _v.slash in file or '.py' in file.lower():
			appDBA = __.thisApp( file )
		else:
			appDBA = file
	else:
		appDBA = ''
	theSwitchInfo = switches.rebuild()
	if justSwitches:
		result = theSwitchInfo
	else:
		result = 'p ' + appDBA + ' ' + theSwitchInfo
	if printThis:
		print( result )
	if separate:
		return [ 'p ' + appDBA, theSwitchInfo ]

	return result

def triggerSpace( data ):
	data = data.replace( ',', ' ' )
	return data

def longDashAdd( data ):
	data = _str.clean_latin1( data )
	data = data.replace( ' :', ':' )
	data = data.replace( '-', '—' )
	return data

def longDashRemove( data ):
	data = data.replace( '—', '-' )
	return data


def inRelevantFolder( file ):
	found = inRelevantFolderSearch( file )
	if type( found ) == bool:
		return file
	if os.path.isfile( found ):
		myFileLocation_Files.append( found )
	return found
def inRelevantFolderSearch( file ):
	if os.path.isfile( file ):
		return os.getcwd() +_v.slash+ file

	probableLocations = [
		"_v.myAppsPy + _v.slash+_v.slash + '*THEFILENAME*' + '.py'",
		"_v.myAppsPy + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myTables + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\batch'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\batch'+_v.slash + '*THEFILENAME*' + '.bat'",
		"_v.myDatabases + _v.slash+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Downloads'+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\exe'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\php'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\php'+_v.slash + '*THEFILENAME*' + '.php'",
		"_v.myApps + _v.slash+'\\powershell'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\vbs'+_v.slash + '*THEFILENAME*'",
	]

	for test in probableLocations:
		f = test.replace( '*THEFILENAME*', file )
		if os.path.isfile( f ):
			return f



	global relevantFolders
	if not len( relevantFolders ):
		rf = getText( _v.relevant_folders, raw=True, clean=2 )
		relevantFolders = rf.split('\n')
	# 

	for folder in relevantFolders:
		f = folder +_v.slash+ file
		if os.path.isfile( f ):
			return f
	return False


def hasExtion( data, wild=False, free=False ):
	global theExtensionsList
	if not len( theExtensionsList ):
		if not wild and not free:
			ext = getText( _v.myTables + _v.slash+'extensions.txt', raw=True, clean=2 )
		elif free:
			ext = getText( _v.myTables + _v.slash+'extensions_free.txt', raw=True, clean=2 )
		else:
			ext = getText( _v.myTables + _v.slash+'extensions_wild.txt', raw=True, clean=2 )
		theExtensionsList = ext.split('\n')
	if not free:
		if '.' in data:
			end0 = data[(-4):]
			end1 = data[(-5):]
			if '.' == end0[0] or '.' == end1[0]:
				testX = data.split('.')
				test = testX[len(testX)-1].lower()
				if test in theExtensionsList:
					return True
	else:
		for ext in theExtensionsList:
			if data.lower().endswith( '.'+ext ):
				return True

	return False





def popDelim( data, delim, pop=1 ):
	data = str( data )
	dataX = data.split( delim )
	i = 0
	while not i == pop:
		dataX.pop()
		i+=1
	return delim.join( dataX )


def addComma( data ):
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






def genAppName( file ):
	if file.lower().endswith( '.py' ):
		x = file.split( '.' )
		x.pop( len(x)-1 )
		result = '.'.join( x )
	else:
		result = file
	return result

def printFields( data, depth=1 ):
	if depth == 1:
		print()
	def tabLoop( depth ):
		result = ''
		i=0
		while not i == depth:
			i+=1
			result += '\t'
		return result
	if type( data ) == list:

		if len(data) and type(data[0]) == dict:
			for row in data[0].keys():
				print( tabLoop( depth ), row )
				printFields( data[0][row], depth+1 )
	elif type( data ) == dict:
		for row in data.keys():
			print( tabLoop( depth ), row )
			printFields( data[row], depth+1 )

def removeReturn( data ):
	for i,row in enumerate(data):
		data[i] = data[i].replace( '\n', '' )
	return data

def flattenList( data ):
	result = ''
	for row in data:
		row = row.replace( '\n', '' )
		result += row + '\n'
	result = _str.cleanBE( result, '\n' )
	return result

def resolveIDs( data ):
	global idResolution
	data = str(data)
	# if len( idResolution ) == 0:
	if not len( idResolution ):
		idResolution = getTable('idResolution.json')
	# idResolution = getTable('idResolution.json')
	for idx in idResolution:
		if data in idx['id']:
			return ' ** ' + idx['name'] + ' ** '
	return data

def printSafe( data ):
	data = str( data )
	result = ''
	for ch in data:
		if ch in _v.safeChar:
			result += ch
	return result

def setUmlData( data, openUML=True ):
	saveTable2( data, _v.umlJson )

	with open(_v.umlJson, 'r+') as f:
		content = f.read()
		f.seek(0, 0)
		f.write("theData=" + content)

	# f=open(_v.umlJson,'a')
	# f.seek(0,0)
	# f.write("theData=")
	# f.close()

	if openUML:
		import webbrowser
		webbrowser.open( _v.umlHtml, new=2)
def setPipeData( data, theFocus=False, clean=True ):
	global appData
	if type( theFocus ) == bool:
		theFocus = __.appReg
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		appData[theFocus]['pipe'] = []
		for pd in data:
			if clean:
				pd = pd.replace('\n','')
				pd = pd.replace('\r','')
				if not pd == '':
					appData[theFocus]['pipe'].append(pd)
			else:
				appData[theFocus]['pipe'].append(pd)
		setPipeDataRan = True

def pipeCleaner():
	global appData
	try:
		if not appData[__.appReg]['pipe'][0][0] in _str.safeChar:
			appData[__.appReg]['pipe'][0] = appData[__.appReg]['pipe'][0][1:]
	except Exception as e:
		pass
	try:
		for i,pipeData in enumerate(appData[__.appReg]['pipe']):
			appData[__.appReg]['pipe'][i] = appData[__.appReg]['pipe'][i].replace('\n','')
	except Exception as e:
		pass
	return appData[__.appReg]['pipe']


def copyVar( data ):
	return pyperclip.copy( str(data) )

def openURL( data ):
	import webbrowser
	webbrowser.open( data, new=2 )

def cleanDic( data ):
	nowJSON_TXT = d2json( data )
	nowDic = json2d( nowJSON_TXT, True )

def copyDicAsJSON( data, openUML=False ):
	txt = copyVar( d2json( data ) )
	if openUML:
		import webbrowser
		webbrowser.open('https://vanya.jp.net/vtree/', new=2)
	return txt
def d2json( data, sort_keys=False ):
	# saveTable2( data, _v.json_temp )
	# txt = getText( _v.json_temp, raw=True )

	return json.dumps(data, indent=4, sort_keys=sort_keys)

def printVar1( data ):
	print( d2json( data ) )


def printVar( data, sort_keys=False ):
	result = d2json( data, sort_keys )
	# saveTable2( data, _v.json_temp )
	# result = getText( _v.json_temp, raw=True )
	# result = type( result )
	result = printVarColor( result )
	print(  )

def printTest( data, color='white', line=None, isPrint=1, shouldExit=1, validate=1, raw=0, profile=False, sort_keys=False,     r=0, v=1, val=1, l=None, x=1, s=False, sk=False ):

	if s or sk:
		sort_keys = True

	if not x:
		shouldExit = 0


	if r:
		raw = True
	if not l is None:
		line = l
	if not v or not val:
		validate = False
	if raw:
		validate = False
	isCode = False



	if not line is None:
		colorThis( [ 'Line:', line ], 'green' )
	if type( data ) == dict:
		isCode = True
	elif type( data ) == list and len(data) and type( data[0] ) == dict:
		isCode = True
	elif type( data ) == list and not isPrint:
		isCode = True
	elif type( data ) == list and isPrint:
		isCode = False
	else:
		isCode = False

	if not validate:
		isCode = False

	if profile:
		import _rightThumb._profileVariables as _profile
		profile = _profile.records.audit( 'printTest_profile', data )
		data = profile
		isCode = True
	


	if isCode:
		if validate:
			printVar( data, sort_keys )
		else:
			printVarSimple( data, sort_keys )
	else:
		if raw:
			colorThis( str(data), color )
		else:
			colorThis( data, color )

	if shouldExit:
		sys.exit()

def printVarSimple( data, sort_keys=False ):
	printVarOld( data, sort_keys )

def printVarOld( data, sort_keys=False ):
	result = d2json( data, sort_keys )
	# result = type( result )
	result = printVarColor_OLD( result )
	print( result )
	
def printVar2( data, sort_keys=False ):
	result = d2json( data, sort_keys )
	result = printVarColor_OLD( result )
	print( result )


def printVarColor( data ):
	_code = regImp( __.appReg, '_rightThumb._auditCodeBase' )
	validator = _code.imp.Validator()
	index = validator.createIndex( data, 'javascript' )
	validator.colorPrint()
	


def printVarColor_OLD( data ):
	result = ''
	for char in data:
		result += printVarColorChar( char )
	return result


	# Gray = '\033[1;30;40m'
	# Red = '\033[1;31;40m'
	# Green = '\033[1;32;40m'
	# Yellow = '\033[1;33;40m'
	# Blue = '\033[1;34;40m'
	# Magenta = '\033[1;35;40m'
	# Cyan = '\033[1;36;40m'
	# White = '\033[1;37;40m'
	# END = '\033[0m'


# def inlineColor( string, color='RED' ):
#     color = color.upper()
#     if not type(string) == str:
#         string = str(string)
#     if color == 'RED':
#         return Color.RED + string + Color.END
#     elif color == 'CYAN':
#         return Color.CYAN + string + Color.END
#     elif color == 'DARKCYAN' or color == 'grey':
#         return Color.DARKCYAN + string + Color.END
#     elif color == 'BLUE':
#         return Color.BLUE + string + Color.END
#     elif color == 'GREEN':
#         return Color.GREEN + string + Color.END
#     elif color == 'YELLOW':
#         return Color.YELLOW + string + Color.END
#     elif color == 'UNDERLINE':
#         return Color.UNDERLINE + string + Color.END


def printVarColorChar( data ):


	what = '('
	color = 'Background.red'
	if data == what:
		return data.replace( what, colorThis( what, color, shouldPrint=False ) )

	what = ')'
	color = 'Background.red'
	if data == what:
		return data.replace( what, colorThis( what, color, shouldPrint=False ) )


	what = '{'
	color = 'green'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )
	
	what = '}'
	color = 'green'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )
	
	what = '['
	color = 'YELLOW'
	if data == what:
		return data.replace( what, inlineColor( what, color ) )

	what = ']'
	color = 'YELLOW'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = '"'
	color = 'white'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = "'"
	color = 'white'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = ':'
	color = 'red'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = ','
	color = 'Magenta'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = '='
	color = 'red'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	return data




def class2Dic( data ):
	saveTable2( data, _v.json_temp )
	txt = getTable2( _v.json_temp )
	return txt

def json2d( data, formatOnline=False ):
	saveText( data, _v.json_temp )
	dic = getTable2( _v.json_temp )
	if formatOnline:
		copyVar( dic )
		
		import webbrowser
		webbrowser.open('https://beautifier.io/', new=2)
	return dic


myFileLocation_Print = True
myFileLocation_File = False
myFileLocation_Files = []
myFileLocation_Pipe = []
def myFileLocations( file, silent=False, currentBaseVersion=3 ):
	global myFileLocation_File
	# if ',' in file and not os.path.isfile( file ):
	#     nFiles = []
	#     for f in file.split(','):
	#         nFiles.append( myFileLocations2( f, silent, currentBaseVersion ) )
	#     file = ','.join( nFiles )
		
	# else:
	#     myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )

	myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )
	if os.path.isfile( myFileLocation_File ) and not myFileLocation_File in myFileLocation_Files:
		myFileLocation_Files.append( myFileLocation_File )
	autoAbbreviations()
	if len( myFileLocation_Files ):
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
					if os.path.isfile( thisFile ):
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
			#     if 'clean' in __.trigger_isPipe:
			#         setPipeData( tmpFiles, __.appReg, clean=True )
			#     else:
			#         setPipeData( tmpFiles, __.appReg, clean=False )
			if not hasFiles:
				if type( appData[__.appReg]['pipe'] ) == bool:
					appData[__.appReg]['pipe'] = []
					for row in myFileLocation_Files:
						appData[__.appReg]['pipe'].append( row )






	return myFileLocation_File
def myFileLocations2( file, silent=False, currentBaseVersion=3 ):
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

	probableLocations = [
		"_v.myAppsPy + _v.slash+'\\_rightThumb\\\\_' + '*THEFILENAME*' + _v.slash+'\\__init__.py'",
		"_v.myAppsPy + _v.slash+_v.slash + '*THEFILENAME*' + '.py'",
		"_v.myAppsPy + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myTables + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\batch'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\batch'+_v.slash + '*THEFILENAME*' + '.bat'",
		"_v.myDatabases + _v.slash+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Downloads'+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\exe'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\php'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\php'+_v.slash + '*THEFILENAME*' + '.php'",
		"_v.myApps + _v.slash+'\\powershell'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\vbs'+_v.slash + '*THEFILENAME*'",
	]

	if file == 'base':
		file = 'base' + str( currentBaseVersion )

	for testThis in probableLocations:
		theTest = eval( testThis )
		theTest = theTest.replace( '*THEFILENAME*', file )
		if os.path.isfile( theTest ):
			if silentSetTo:
				
				print()
				print( 'File not here but in:', theTest )
				print()

			return theTest
	return file



def cleanList( data ):
	for i,d in enumerate(data):
		data[i] = data[i].replace( '\n', '' )
	return data

adminStatus = ''
def isAdmin():
	global adminStatus
	if type(adminStatus) == str:
		tempFile = _v.stmp + _v.slash + genUUID()
		do = 'echo %isAdmin%>'+tempFile
		test = os.system('"' + do + '"')
		isAdmin0 = getText(tempFile)
		isAdmin1 = isAdmin0[0].replace('\n','')
		os.remove(tempFile)
		if 'True' in isAdmin1:
			adminStatus = True
		else:
			adminStatus = False
	return adminStatus

def autoDate( data ):
	import _rightThumb._date as _date
	return _date.autoDate( data )

def resolveEpoch( string, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	return resolveEpochTest( string, test, showPrint, showPrintTry, onlyEpoch, delim, falseBlank )


def resolveEpochTest( string, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	# onlyEpoch = True, False, 'day' 

	import _rightThumb._date as _date
	auto = _date.autoDate( string )
	if not type( auto ) == bool:
		string = auto


	rData = False

	try:
		float( string )
	except Exception as e:
		test = 0

	word = string
	if test == 1:

		if showPrintTry:
			print( 'try:', 1 )
		try:
			if showPrint:
				print( 'success:', 1 )
			result = ' { { ' + str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S')) + ' } } '
			epoch = str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S'))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpochTest( string, 2, showPrint, showPrintTry, onlyEpoch, delim )
	

	if test == 2:

		if showPrintTry:
			print( 'try:', 2 )
		try:
			if showPrint:
				print( 'success:', 2 )
			result = ' { { ' + str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(float(word)/1000.))) + ' } } '
			epoch = str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(float(word)/1000.)))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpochTest( string, 3, showPrint, showPrintTry, onlyEpoch, delim )



	if test == 3:

		if showPrintTry:
			print( 'try:', 3 )
		try:
			if showPrint:
				print( 'success:', 3 )
			result = ' { { ' + str(datetime.datetime.utcfromtimestamp(float(word)/1000.)) + ' } } '
			epoch = str(datetime.datetime.utcfromtimestamp(float(word)/1000.))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpochTest( string, 4, showPrint, showPrintTry, onlyEpoch, delim )


	if test == 4:

		if showPrintTry:
			print( 'try:', 4 )
		try:
			if showPrint:
				print( 'success:', 4 )
			result = ' { { ' + str(time.ctime(float(word))) + ' } } '
			epoch = str(time.ctime(float(word)))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpochTest( string, 5, showPrint, showPrintTry, onlyEpoch, delim )



	if test == 5:

		if showPrintTry:
			print( 'try:', 5 )
		try:
			if showPrint:
				print( 'success:', 5 )
			result = ' { { ' + str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(float(word)/1000.))) + ' } } '
			epoch = str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(float(word)/1000.)))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpochTest( string, 6, showPrint, showPrintTry, onlyEpoch, delim )

	if test == 6:

		if showPrintTry:
			print( 'try:', 6 )
		try:
			if showPrint:
				print( 'success:', 6 )
			result = ' { { ' + str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S')) + ' } } '
			epoch = str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S'))
			rData = [ result, epoch ]
		except Exception as e:
			pass

	if not type( rData ) == bool:
		if not type( onlyEpoch ) == bool:
			rData = rData[1].split(' ')[0].replace( '-', delim )
		elif onlyEpoch == True:
			rData = rData[1].replace( '-', delim )
		else:
			rData[1] = rData[1].replace( '-', delim )

	if falseBlank and type( rData ) == bool:
		rData = ''
	return rData

def dateAdd2( theDate, addDays, delim='-' ):
	
	theDate = str( theDate )

	if not delim in theDate:
		try:
			float( theDate )
			theDate = resolveEpochTest( theDate, onlyEpoch='day', delim=delim )
			if type(theDate) == bool:
				print( 'Error:', theDate )
				sys.exit()
		except Exception as e:
			printBold( 'Error: '+ theDate, 'red' )
			sys.exit()

	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 + datetime.timedelta(days=addDays)

def txt2Date(text):
	# _.switches.trigger('Watched', _.txt2Date)

	try:
		if not type(text) == str:
			text = ''
	except Exception as e:
		text = ''

	if text == '':
		theDate = datetime.date.today()
		result = str( theDate ).split()[0]
	elif '-' in text:
		if text.count('-') == 2:
			try:
				textSplit = text.split('-')
				# print(textSplit)
				theDate = datetime.datetime( int(textSplit[0]), int(textSplit[1]), int(textSplit[2]), 0, 0 )
				result = str( theDate ).split()[0]
			except Exception as e:
				printBold('Date error: using today\'s date','red')
				theDate = datetime.date.today()
				result = str( theDate ).split()[0]
		else:
			print('Date error: using today\'s date')
			theDate = datetime.date.today()
			result = str( theDate ).split()[0]
	else:
		fnd = 'ymwd'
		do = text.lower().replace(' ','')
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
			theDate = datetime.date.today() + datetime.timedelta(-365 * nmb)
		if 'm' in do:
			theDate = datetime.date.today() + datetime.timedelta(-30 * nmb)
		if 'w' in do:
			theDate = datetime.date.today() + datetime.timedelta(-7 * nmb)
		if 'd' in do:
			theDate = datetime.date.today() + datetime.timedelta(-1 * nmb)
		result = str( theDate ).split()[0]
	return result

def genUUID( project='', label='', uniqueTimestamp=False ):
	global appData
	global appInfo
	
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	try:
		type(appData[__.appReg]['uuid'])
		good = True
	except Exception as e:
		good = False
	if good:

		try:
			timestamp = appData[__.appReg]['start']
		except Exception as e:
			timestamp = time.time()

		if not project == '' or not label == '':
			if type(appData[__.appReg]['uuid']) == str:
				# print()
				# print( '__.appReg', __.appReg )
				# print()
				# print(d2json( appData ))
				# print()
				appData[__.appReg]['uuid'] = {}
				# print(appInfo[__.appReg]['file'])
				# sys.exit()
				appData[__.appReg]['uuid']['app'] = appInfo[__.appReg]['file']

			if not type(appData[__.appReg]['uuid']) == str:
				
				appData[__.appReg]['uuid']['uuid'] = string
				appData[__.appReg]['uuid']['timestamp'] = timestamp
				appData[__.appReg]['uuid']['project'] = ''
				appData[__.appReg]['uuid']['label'] = ''

				if uniqueTimestamp:
					appData[__.appReg]['uuid']['timestamp'] = time.time()

				if not project == '':
					appData[__.appReg]['uuid']['project'] = project

				if not label == '':
					appData[__.appReg]['uuid']['label'] = label
					
				uuidLog = getTable('uuid_log.json')
				uuidLog.append(appData[__.appReg]['uuid'])
				saveTable(uuidLog,'uuid_log.json',printThis=False)
			# appData[__.appReg]['uuid'] = { 'uuid': theID, 'timestamp': time.time(), 'project': theProject, 'app': 'guid' }
	return string

def saveText( rows, theFile, errors=True ):
	# print(type(rows))
	try:
		if type(rows) == bytes:
			rows = str(rows,'utf-8')
		f = open(theFile,'w', encoding='utf-8')
		# if type(rows) == str:

		# print(type(rows))
		# f.write(str(rows))
		# rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
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
		open(theFile, 'wb').write(rows)
		if errors:
			print( 'Auto correction when saving text' )

def getText( theFile, raw=False, clean=False ):
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

def getSize(fileobject):
	fileobject.seek(0,2) # move the cursor to the end of the file
	size = fileobject.tell()
	return size

# def formatSize(size):
#     result = ''
#     if size == None:
#         result = ''
#     elif size < 1024:
#         result = str(size) + ' B'
#     elif size > 1024 and size < 1048576:
#         num = round(size / 1024, 2)
#         result = str(num) + ' KB'
#     elif size > 1048576 and size < 1073741824:
#         num = round(size / 1048576, 2)
#         result = str(num) + ' MB'
#     elif size > 1073741824 and size < 137438953472:
#         num = round(size / 1073741824, 2)
#         result = str(num) + ' GB'
#     # if size < 1:
#     #     result = ''
#     return result

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
	import math
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
	import calendar
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

def processTimeout():
	global switches
	global defaultTimeout
	if switches.isActive('Timeout') == True:
		try:
			defaultTimeout = int(switches.value('Timeout'))
		except Exception as e:
			errors.append({'id': 18, 'function': 'parent', 'cnt': 1, 'location': "defaultTimeout = int(switches.value('Timeout'))", 'vars': [{'name': 'timeout', 'value': switches.value('Timeout')}], 'error': e})
			printBold('Error:','red')
			print('\tBad timeout value.')
			os._exit(0)

	# print(defaultTimeout)
	x = Timer(0.0, timeout, ('start',defaultTimeout))
	x.start()


def showLine( string, plus = '', minus = '', plusOr = False ):
	# print(plus)
	# print(string)
	
	global switches
	if switches.isActive('Plus') or not plus == '':
		# print('asdf')
		result = positiveResults(string,plus,plusOr)
		if not result and switches.isActive('PlusClose'):
			result = closeResults( string )

	else:
		result = True
	if result == True and  (switches.isActive('Minus') or not minus == ''):
		result = minusResults(string,minus)
	# print(result)
	return result
def closeResults( string ):
	global switches
	global plusClose
	
	if len( switches.value('PlusClose') ):
		try:
			plusClose = float( switches.value('PlusClose') )
		except Exception as e:
			pass

	test = patternMatch( string, switches.value('Plus') )
	if test >= plusClose:
		# print( test, string )
		return True
	else:
		return False



def positiveResults(string,plus='',plusOr=False):
	global switches
	if plusOr or switches.isActive('PlusOr'):
		plusOr = True
	if not plus == '':
		plusInput = plus
	else:
		plusInput = switches.values('Plus')
	if type( plusInput ) == str:
		plusInput = plusInput.lower()
		plusList = plusInput.split(',')
	else:
		for i,row in enumerate(plusInput):
			plusInput[i] = plusInput[i].lower()
		plusList = plusInput
	length = len(plusList)
	cnt = 0
	result = False
	string = string.lower()
	# print( plusList )
	# sys.exit()
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

def minusResults(string,minus=''):
	global switches
	string = string.lower()
	result = True
	if not minus == '':
		minusInput = minus
	else:
		minusInput = switches.values('Minus')
	if type( minusInput ) == str:
		minusInput = minusInput.lower()
		minusList = minusInput.split(',')
	else:
		for i,row in enumerate(minusInput):
			minusInput[i] = minusInput[i].lower()
		minusList = minusInput

	try:
		for s in minusList:
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

def saveLog( logname, rows=[], focus=True, printThis=True ):
	global appInfo
	global appData
	
	indentCode = True
	log = 'app_audit_log_TIMESTAMP__FILENAME__LOGNAME__INSTANCE.json'

	if type(focus) == bool:
		focus = __.appReg
		
	if not len(rows) and logname == 'threads':
		global threads
		rows = threads.log()
	if not len(rows) and logname == 'audit':
		for ad in __.structure():
			if len(appData[ad]['audit']) > 0:
				rows.append( { 'app': appInfo[ad]['file'], 'focus': ad, 'records': appData[ad]['audit'] } )
	try:
		if len(appInfo[focus]['instance']) > 0:
			log = log.replace('INSTANCE',appInfo[focus]['instance'])
		else:
			log = log.replace('__INSTANCE','')
	except Exception as e:
		log = log.replace('__INSTANCE','')
	
	log = log.replace('TIMESTAMP',str(appData[focus]['start']))
	log = log.replace('FILENAME',appInfo[focus]['file'])
	log = log.replace('LOGNAME',logname)
	
	file0 = _v.myTables + _v.slash+'applogs'+_v.slash + log

	if indentCode:
		dataDump = json.dumps(rows, indent=4, sort_keys=True)
	else:
		dataDump = json.dumps(rows)
	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + file0)

def saveTable( rows, theFile, tableTemp=False, printThis=True, indentCode=True, sort_keys=False ):
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
		printBold('Saved: ' + p, 'blue')
	return file0


def getTable( theFile, tableTemp=False, printThis=False ):
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

def getTable3(theFile):
	if os.path.isfile(theFile) == True:
		with open(theFile,'r') as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		return json_data

def getTable2(theFile):
	if os.path.isfile(theFile) == True:
		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
def saveTable2( rows, theFile, printThis=False, sort_keys=False ):
	# print('*******************',theFile)
	dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + theFile)

def saveTable3( rows, theFile, printThis=False ):
	# print('*******************',theFile)
	dataDump = json.dumps(rows)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + theFile)


def tempFile(rows,theFile):
	file0 = _v.stmp + _v.slash + theFile
	file = open(file0,'w')
	for r in rows:
		file.write(r)                 
	file.close()

def stamp2Date(ts):
	# print(ts)
	# print(datetime.datetime.fromtimestamp(int(ts) / 1e3))
	return datetime.datetime.fromtimestamp(int(ts) / 1e3)
def float2Date(ts):
	import _rightThumb._date as _date
	auto = _date.autoDate( ts )
	if type(ts) == str:
		ts = ts.replace('_','.')
		if '.' in ts:
			ts = float(ts)
		else:
			ts = int(ts)
		# print(type(ts))
		# print( stamp2Date(ts) )
	return stamp2Date(ts)
def float2Date2(ts):
	if type(ts) == str:
		ts = ts.replace('_','.')
		if '.' in ts:
			ts = float(ts)
		else:
			ts = int(ts)
		# print(type(ts))
	return str(datetime.datetime.fromtimestamp(ts)).split('.')[0]
	# return str(datetime.datetime.fromtimestamp(ts / 1e3))
	# return str(ts)
	# return str(datetime.datetime.fromtimestamp(ts)).split('.')[0] + '\t' + str(ts)
	# return str(ts).split('.')[0] + '\t' + str(datetime.datetime.fromtimestamp(ts)).split('.')[0]
def float2Date3(ts):
	return str(datetime.datetime.fromtimestamp(float(ts)).strftime('%Y-%m-%d %H:%M:%S'))
def float2Date3B(ts,isJson = True):
	stmp = float2Date3(ts)
	dt = stmp.split(' ')[0]
	preResult = {'year': dt.split('-')[0],'month': dt.split('-')[1],'day': dt.split('-')[2]}
	if isJson:
		result = preResult
	else:
		result = str(preResult['year']) + '-' + str(preResult['month']) + '-' + str(preResult['day'])

	return result

def expireCheck(theDate,delim):
	now = datetime.datetime.now()
	today = now.strftime("%Y-%m-%d")
	fdtl = theDate.split(delim)
	foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	td = str(today).split('-')
	tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
	diff = tdd - foundDate
	return int(diff.days)

def dateDiff( theDate0, theDate1, delim='-' ):
	theDate0 = str(theDate0)
	theDate1 = str(theDate1)


	if not delim in theDate0:
		try:
			theDate0 = resolveEpochTest( theDate0, onlyEpoch='day', delim=delim )
			if type(theDate0) == bool:
				printBold( 'Error: _.dateDiff '+ str(theDate0), 'red' )
				sys.exit()
		except Exception as e:
			printBold( 'Error: _.dateDiff '+ str(theDate0), 'red' )
			sys.exit()


	if not delim in theDate1:
		try:
			theDate1 = resolveEpochTest( theDate1, onlyEpoch='day', delim=delim )
			if type(theDate1) == bool:
				printBold( 'Error: _.dateDiff '+ str(theDate1), 'red' )
				sys.exit()
		except Exception as e:
			printBold( 'Error: _.dateDiff '+ str(theDate1), 'red' )
			sys.exit()

	# print(theDate0,theDate1,delim)
	# sys.exit()
	fdtl0 = theDate0.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))

	fdtl1 = theDate1.split(delim)
	date1 = datetime.date(int(fdtl1[0]), int(fdtl1[1]), int(fdtl1[2]))

	diff = date1 - date0
	return (int(diff.days))
	
def dateDiffX( theDate0, theDate1, delim='-' ):
	theDate0 = str(theDate0)
	theDate1 = str(theDate1)


	if not delim in theDate0:
		theDate0 = resolveEpochTest( theDate0, onlyEpoch='day', delim=delim )



	if not delim in theDate1:
		theDate1 = resolveEpochTest( theDate1, onlyEpoch='day', delim=delim )



	# print(theDate0,theDate1,delim)
	# sys.exit()
	fdtl0 = theDate0.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))

	fdtl1 = theDate1.split(delim)
	date1 = datetime.date(int(fdtl1[0]), int(fdtl1[1]), int(fdtl1[2]))

	diff = date1 - date0
	return (int(diff.days))

def dateAdd(theDate,delim,addDays):
	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 + datetime.timedelta(days=addDays)

def dateSub(theDate,delim,addDays):
	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 - datetime.timedelta(days=addDays)

def listAverage(theList):
	total = 0
	for item in theList:
		total += item
	result =  total / len(theList)
	return result 
def date2epoch(theDate,delim='-'):
	theDate = str(theDate)
	if len( theDate ) == 0:
		return ''
	theDate = theDate.replace(delim,'-')
	fdtl = theDate.split(' ')[0].split('-')
	if ':' in theDate:
		theDate = theDate.replace('.',':')
		if theDate.count(':') == 2:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M:%S')
		elif theDate.count(':') == 1:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M')
		elif theDate.count(':') == 3:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M:%S:%f')
		else:
			print('Error: date2epoch')
			sys.exit()

	else:
		stmp = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	# stmp = datetime.datetime.strptime(theDate, '%Y-%m-%d')
	return float(time.mktime(stmp.timetuple()))

def validateEmail(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip(data)
	good = True
	# if not '@' in data:
	if not data.count('@') == 1:
		good = False
	if good:
		if not '.' in data.split('@')[1]:
			good = False
	# if data.count('@') == 1:
	if not good and len(data) > 0:
		data = ' ___________ * BAD * ___________'
	return data

def figureOutDate(theDate, theFormat):
	theFormat = str(theFormat)
	theFormat = _str.replaceDuplicate(theFormat,' ')
	theFormat = _str.cleanBE(theFormat,' ')
	theFormat = theFormat.lower()

	theFormatExp = 'dmy'
	if not len(theFormat) == 3:
		print('format error, expected: dmy, ymd')
		sys.exit()
	if theFormat[0] in theFormatExp and theFormat[1] in theFormatExp and theFormat[2] in theFormatExp:
		pass
	else:
		print('format error, expected: dmy, ymd')
		sys.exit()
	# theFormat = 'dmy'
	theDate = str(theDate)
	theDate = _str.replaceDuplicate(theDate,' ')
	theDate = _str.cleanBE(theDate,' ')

	
	n = '0123456789'
	a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
	autoDelim = ''
	for d in theDate:
		if d in n:
			pass
		elif d in a:
			pass
		else:
			autoDelim = d
			break

	theDateDe = theDate.split(autoDelim)
	info = {}

	info[theFormat[0]] = theDateDe[0]
	info[theFormat[1]] = theDateDe[1]
	info[theFormat[2]] = theDateDe[2]
	if info['m'][0] in a:
		m = info['m']
		m = m.lower()
		found = False
		for monththeDate in getMonthData():
			# print(monththeDate)
			# sys.exit()
			full = monththeDate['month']
			abbrev = monththeDate['abbrev']
			mNumber = monththeDate['number']
			full = full.lower()
			abbrev = abbrev.lower()
			if m == full or m == abbrev:
				found = True
				info['m'] = mNumber
		if not found:
			ans = input('What Month? ')
			if len(ans) == 0:
				print('Month error')
				sys.exit()
			try:
				int(ans)
			except Exception as e:
				printBold('Month error','red')
				sys.exit()
			if len(ans) == 1:
				info['m'] = 0 + ans
			elif len(ans) == 2:
				info['m'] = ans
			else:
				printBold('Month error','red')
				sys.exit()

	ifoy = info['y']
	ifom = info['m']
	ifod = info['d']
	pResult = info['y'] + '-' + info['m'] + '-' + info['d']
	hasDup = False
	if pResult.count(ifoy) > 1:
		hasDup = True
	if pResult.count(ifom) > 1:
		hasDup = True
	if pResult.count(ifod) > 1:
		hasDup = True


	changed = []
	def test(l):
		result = ''
		if int(l) > 1000:
			result = 'y'
		elif int(l) > 12:
			result = 'd'
		return result
	fList = ''
	if test(ifom) == 'y':
		fList += 'y'
		info['y'] = ifom
		# info['m'] = ifoy
	if test(ifod) == 'y':
		fList += 'y'
		info['y'] = ifod
		# info['d'] = ifoy
	if test(ifod) == 'd':
		fList += 'd'
	if test(ifoy) == 'd':
		fList += 'd'
		info['d'] = ifoy
	if test(ifom) == 'd':
		fList += 'd'
		info['d'] = ifom
	if test(ifoy) == '' and 'd' in fList:
		fList += 'm'
		info['m'] = ifoy
	if test(ifoy) == '' and 'd' in fList:
		fList += 'm'
		info['m'] = ifoy
	if test(ifoy) == 'd':
		fList += 'd'
		info['d'] = ifoy
	if test(ifod) == '' and 'd' in fList:
		info['m'] = ifod
	# print(test(ifoy))
	# print(fList)

	result = info['y'] + '-' + info['m'] + '-' + info['d']
	# print(result)
	if not hasDup:
		hasDup = False
		if result.count(ifoy) > 1:
			hasDup = True
		if result.count(ifom) > 1:
			hasDup = True
		if result.count(ifod) > 1:
			hasDup = True
		if hasDup:
			print('Error please specify format: ymd')
			sys.exit()
	else:
		if result.count(info['y']) > 1:
			print('Error please specify format: ymd')
			sys.exit()

	print(result)
	sys.exit()
	return result



def getMonthData():
	monthData = getText(_v.myTables + _v.slash+'month.txt')
	monthList = []
	for md in monthData:
		md = md.replace('\n','')
		mds = md.split(',')
		monthList.append({'month': mds[0], 'abbrev': mds[1], 'number': mds[2]})
	return monthList



def formatPhone00(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)
	data = _str.cleanBE(data,'.')
	return data

def formatPhone0(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = '(' + data[0] + data[1] + data[2] + ') ' + data[3] + data[4] + data[5] + '-' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

def formatPhone1(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = data[0] + data[1] + data[2] + '-' + data[3] + data[4] + data[5] + '-' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

def formatPhone2(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = data[0] + data[1] + data[2] + '.' + data[3] + data[4] + data[5] + '.' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

def updateLine(string):
	string = str(string)
	sys.stdout.write("\b" * len(string))
	sys.stdout.write(" " * len(string))
	sys.stdout.write("\b" * len(string))
	sys.stdout.write(string)
	sys.stdout.flush()

def getLastTableSplit(theFile,tableTemp = 'split'):
	if tableTemp == 'split':
		basePath = _v.myTables + _v.slash+'tablesets'
	else:
		basePath = _v.stmp
	# print(basePath)
	dirList = os.listdir(basePath)
	fileList = []
	for d in dirList:
		if d.startswith(theFile):
			fileList.append(d)
	# print(fileList)
	fileList.sort()
	# print(fileList)
	# print()
	# print(fileList[len(fileList)-1])
	# print(fileList)
	# file0 = basePath + _v.slash + fileList[len(fileList)-1]
	# print(file0)
	return getTable(fileList[len(fileList)-1],tableTemp)

def saveTableSplitNew( rows,theFile,tableTemp = True,printThis = True, project=False ):
	# defaults to myTables
	print( 'save size:', len(rows))
	if tableTemp:
		file0 = _v.myTables + _v.slash+'tablesets' + _v.slash + theFile
	elif project:
		file0 = _v.myTables + _v.slash+'projects' + _v.slash + theFile

	else:
		file0 = _v.stmp + _v.slash + theFile

	def count(cnt):
		char = 6
		cnt = str(cnt)
		lencnt = len(cnt)
		if lencnt == 1:
			cnt = '00000' + cnt
		if lencnt == 2:
			cnt = '0000' + cnt
		if lencnt == 3:
			cnt = '000' + cnt
		if lencnt == 4:
			cnt = '00' + cnt
		if lencnt == 5:
			cnt = '0' + cnt
		cnt = '_' + cnt
		return cnt

	suffix = '.json'
	cnt = 0
	path = file0 + count(cnt) + suffix
	while os.path.isfile(path) == True:
		cnt += 1
		path = file0 + count(cnt) + suffix

	dataDump = json.dumps(rows, indent=4, sort_keys=True)
	f = open(path,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + path)

def sort(rows, name):
	global errors
	tempFields = []
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
		except Exception as e:
			errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})



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
		tempFields.append( sortBy[item] )
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
	if len( tempFields ):
		# print( tempFields )
		for ix,r in enumerate(rows):
			for tmp in tempFields:
				try:
					del rows[ix][tmp]
				except Exception as e:
					pass

	return rows


class Switch:

	def __init__(self, name, switch, expected_input_example, description):
		self.appReg = __.appReg
		self.name = name
		self.switch = switch
		self.pos = 0
		self.active = False
		self.value = None
		self.values = []
		self.expected_input_example = expected_input_example
		self.documentation = { 'description': description, 'examples': [], 'required': [], 'related': [] }

		# print()
		# print()

		# for key in dir(self):
		#     if not key.startswith('_'):
		#         x = 'self.'+key
		#         print( x, eval(x) )

	def trigger(self,script):
		self.script_trigger = script




class Switches:

	def __init__(self):
		self.switches = []
		self.index = {}
		self.appRegDefault = None
		self.appReg = __.appReg
		self.hasRequired = []
		self.isRequired = {}


	def documentation( self, name, data ):
		result = False
		try:
			for i,row in enumerate(self.switches):
				if row.name == name:
					# print( 'SET' )
					if self.switches[i].appReg == __.appReg:

						try:
							if len( data['description'] ):
								self.switches[i].documentation['description'] = data['description']
						except Exception as e:
							pass

						try:
							if len( data['examples'] ):
								self.switches[i].documentation['examples'] = data['examples']
						except Exception as e:
							pass

						try:
							if len( data['required'] ):
								self.switches[i].documentation['required'] = []
								self.switches[i].documentation['related'] = []
								for record in data['required']:
									if record == 'Pipe':
										__.isRequired_Pipe = True
									else:
										self.switches[i].documentation['required'].append( record )
										self.switches[i].documentation['related'].append( record )
										if not name in self.hasRequired:
											self.hasRequired.append( name )
								

						except Exception as e:
							pass

						try:
							if len( data['related'] ):
								for record in data['related']:
									self.switches[i].documentation['related'].append( record )
						except Exception as e:
							pass

						try:
							if type( data['isRequired'] ) == bool:
								if data['isRequired']:
									if not name in self.isRequired[__.appReg]:
										self.isRequired[__.appReg].append( name )
						except Exception as e:
							pass



		except Exception as e:
			result = False
		return result


	def record( self, name ):
		result = False
		try:
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						return i
		except Exception as e:
			result = False
		return result
	def dumpSwitches(self,includeBlank=False):
		data = []
		for i,row in enumerate(self.switches):
			# if not row.value is None:
			if includeBlank:
				data.append({ 'name': row.name, 'value': row.value, 'appreg': row.appReg })
			else:
				if not row.value is None or row.active:
					data.append({ 'name': row.name, 'value': row.value, 'appreg': row.appReg })
			# print(row.name,'\t',row.value,'\t',row.appReg)
		tables.register('data',data)
		tables.print('data','appreg,name,value')
	def register(self, name, switch, expected_input_example = None, isRequired=False, isPipe=False, description=''):

		self.switches.append(Switch(name, switch, expected_input_example, description))

		try:
			if not type(self.isRequired[__.appReg]) == list:
				self.isRequired[__.appReg] = []
		except Exception as e:
			self.isRequired[__.appReg] = []
		
		

		switch = switch.replace( ' ', '' )

		if not type( isPipe ) == bool:
			if 'name' in isPipe and ( 'data' in isPipe or 'clean' in isPipe ):
				pass
			elif 'name' in isPipe:
				__.trigger_isPipe = 'name'
			elif 'data' in isPipe or 'clean' in isPipe:
				if 'clean' in isPipe:
					__.trigger_isPipe = 'data,clean'
				else:
					__.trigger_isPipe = 'data'
		elif isPipe:
			__.trigger_isPipe = 'data'


		if isRequired:
			if not name in self.isRequired[__.appReg]:
				self.isRequired[__.appReg].append( name )



	def fieldSet( self, name, column, value, theFocus=False ):# updateSwitchField

		if type( theFocus ) == bool:
			theFocus = __.appReg

		if column == 'value':
			if self.fieldExists( name, 'script_trigger', theFocus ):
				value = self.scriptTrigger( name, value, theFocus  )
				# self.fieldGet(name,'script_trigger')(value)
			elif self.fieldExists( name, 'script_trigger', theFocus ) == True:
				script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)# script_trigger_external
				value = eval(script)
		# print( name, column, value )
		# sys.exit()
		for i,row in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				if row.name == name:
					if column == 'active':
						if value == True:
							self.switches[i].active = True
						else:
							self.switches[i].active = False
					elif column == 'value':
						if value == True:
							self.switches[i].value = True
						elif value == False:
							self.switches[i].value = False
						else:
							self.switches[i].value = value

					else:
						# self.switches[i][column] = value
						exec('self.switches[i].' + column + '= value')
						# value = str(value)
						# try:
						#     exec('self.switches[i].' + column + '=str(\'' + value + '\')')
						# except Exception as e:
						#     exec('self.switches[i].' + column + '=\'' + value + '\'')
			
		return ''



	def fieldExists( self, name, column, theFocus=False ):# doesFieldExist
		result = False
		try:
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						eval('row.' + column)
						result = True
		except Exception as e:
			result = False
		return result
	def scriptTrigger( self, name, value, theFocus=False ):# externalScriptTrigger
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					value = self.switches[i].script_trigger(value)# script_trigger_external
		return value

	def fieldGet2(self,name,column):# getSwitchField
		# print(name,column)
		result = ''
		for i,row in enumerate(self.switches):
			if row.name == name:
				result = eval('row.' + column)
		return result

	def fieldGet( self, name, column, theFocus=False ):# getSwitchField
		# print(name,column)
		result = ''
		if not column == 'pos':

			if name == 'NoColor' and column == 'active':

				found = False

				for i,row in enumerate(self.switches):
					if row.name == name:
						# print( row.name, row.active )
						if row.active:
							found = True

				result = found
						
				# print( 'here', name, found )
				# sys.exit()


			else:


				i = self.searchIndex( name, theFocus )
				if i is None:

					if column == 'active':
						return False

					if column == 'value':
						return ''

					if column == 'values':
						return []

					printBold( 'Error: Nonexistent Switch', 'red' )
					print( name, column, theFocus )
					printVar( self.index )
					sys.exit()
				row = self.switches[i]
				result = eval('row.' + column)

		else:
			if type( theFocus ) == bool:
				theFocus = __.appReg
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == theFocus:
					if row.name == name:
						result = eval('row.' + column)
		return result

	def isActive( self, name, theFocus=False ):# isSwitchActive
		return self.fieldGet( name, 'active', theFocus )

	def getField( self, name, field, theFocus=False ):
		return self.fieldGet( name, field, theFocus )

	def value( self, name, theFocus=False ):# getSwitchValue
		result = self.fieldGet( name, 'value', theFocus )
		if result is None:
			result = ''
		return result

	def values( self, name, theFocus=False ):# getSwitchValue
		result = self.fieldGet( name, 'values', theFocus )
		if result is None:
			result = []
		return result


	def trigger(self,name,script):
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					self.switches[i].trigger(script)


	def value2(self,name):
		switchInput = sys.argv

		try:
			switchInput[self.fieldGet(name,'pos') + 1]
			result = ''

			i = 0
			for a in switchInput:
				if i > self.fieldGet(name,'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					else:

						if switchInput[i] == ':':
							switchInput[i] = switchInput[i].replace(':','_;192B;_')
						if switchInput[i] == ',':
							switchInput[i] = switchInput[i].replace(',','_;192A;_')
						result += str(switchInput[i]) + ','
				i += 1
			result = result[:-1]
			result = _str.cleanAll(result,'"','')
			result = _str.cleanAll(result,':,',':')
			result = _str.cleanAll(result,',,',',')

		except Exception as e:
			result = None
		return result


	def value3(self,name):
		switchInput = sys.argv
		data = []
		try:
			switchInput[self.fieldGet(name,'pos') + 1]
			result = ''

			for i,a in enumerate(switchInput):
				if i > self.fieldGet(name,'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					else:

						data.append( a )


		except Exception as e:
			data = None
		return data

	def isSwitch(self,string):# checkIfSwitch
		result = False
		for i,a in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				for b in a.switch.split(','):
					if b == string:
						result = True
					# print(b,result)
		return result

	def format(self,name):# processSwitchFormatting
		value = self.value2(name)
		if self.fieldExists(name,'script_trigger') == True:
			value = self.scriptTrigger(name,value)
		elif self.fieldExists(name,'script_trigger') == True:
			script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)
			value = eval(script)
		return value

	def format2( self, name ):

		values = self.value3(name)
		if values is None:
			values = []
		else:
			for i,value in enumerate(values):
				if self.fieldExists(name,'script_trigger') == True:
					values[i] = self.scriptTrigger(name,value)
				elif self.fieldExists(name,'script_trigger') == True:
					script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)
					values[i] = eval(script)

		return values

	def exists(self,name):# checkSwitchExist
		result = False
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.name == name:
					result = True
		return result

	def process( self, helpx=False ):
		global customHelp
		global argvProcess
		global printAutoAbbreviations_scheduled
		for ii,sw in enumerate(self.switches):
			if self.switches[ii].appReg == __.appReg:
				self.switches[ii].pos = None
				self.switches[ii].active = False
				self.switches[ii].value = None
		switchHelp = []
		isActiveList = []
		hasActiveRequireList = []
		isActiveRequireList = []

		if argvProcess:
			for i,a in enumerate(sys.argv):
				a = a.replace(':','')
				for ii,sw in enumerate(self.switches):
					for s in sw.switch.split(','):
						if s.lower() == a.lower():
							if self.switches[ii].appReg == __.appReg:
								self.switches[ii].pos = i
								self.switches[ii].active = True
								self.switches[ii].value = self.format(self.switches[ii].name)
								self.switches[ii].values = self.format2(self.switches[ii].name)

								isActiveList.append( ii )
								if self.switches[ii].name in self.hasRequired:
									hasActiveRequireList.append( ii )
								if self.switches[ii].name in self.isRequired[__.appReg]:
									isActiveRequireList.append( ii )

								if type( self.switches[ii].value ) == str:
									if '-??' in self.switches[ii].value:
										switchHelp.append(ii)

		if self.exists('_Raw') == True:
			# print('test')
			self.fieldSet('_Raw','pos',1)
			self.fieldSet('_Raw','active',True)
			self.fieldSet('_Raw','value',self.format('_Raw'))


		for i,record in enumerate(self.switches):
			if self.appRegDefault is None:
				self.appRegDefault = self.switches[i].appReg
			self.index[ self.switches[i].appReg ] = {}
		for i,record in enumerate(self.switches):
			self.index[ self.switches[i].appReg ][self.switches[i].name] = i






		if len( switchHelp ):
			somethingPrinted = False
			for i in switchHelp:
				if len( self.switches[i].documentation['description'] ):
					somethingPrinted = True
					print()
					print( inlineBold('Description:\t'), self.switches[i].documentation['description'] )
					print()
				if len( self.switches[i].documentation['examples'] ):
					printBold( 'Examples:' )
					for example in self.switches[i].documentation['examples']:
						colorizeRow( '\t\t'+ example , 2)



			if somethingPrinted:
				sys.exit()

		if self.isActive('Help') or helpx:
			global appInfo
			global fields
			# os.system('cls')
			print('')
			try:
				
				print( inlineBold('Description: \t'), appInfo[__.appReg]['description'] + '\n')
				configured = True
			except Exception as e:
				configured = False
			try:
				if len(appInfo[__.appReg]['prerequisite']) > 0:
					printBold('Prerequisite:')
					for prereq in appInfo[__.appReg]['prerequisite']:
						colorizeRow('\t' + prereq,2)
					print('\n')
			except Exception as e:
				pass
			try:
				if len(appInfo[__.appReg]['relatedapps']) > 0:
					printBold('Related Apps:')
					for relapps in appInfo[__.appReg]['relatedapps']:
						colorizeRow('\t' + relapps,2)
					print('\n')
			except Exception as e:
				pass

			if configured:
				if len(appInfo[__.appReg]['examples']) > 0:
					printBold('Examples:')
					for ex in appInfo[__.appReg]['examples']:
						colorizeRow('\t' + ex,2)
					print('\n')
				if len(appInfo[__.appReg]['columns']) > 0:
					printBold('Columns and abbreviations:')
					result = ''
					if len( appInfo[__.appReg]['columns'] ):
						# fields.register( 'columns', 'name,abbreviation', script=__.triggerTest )
						fields.asset( 'columns', appInfo[__.appReg]['columns'] )
						print()

					if __.columnAbbreviations == 0:
						for col in appInfo[__.appReg]['columns']:
							result += col['name'] + '(' + col['abbreviation'] + '), '
						result = result[:-2]
						colorizeRow('\t' + result + '\n',2)

					if __.columnAbbreviations == 1:
						for col in appInfo[__.appReg]['columns']:
							abbreviation =  fields.value( 'columns', 'abbreviation', col['abbreviation'] )
							name =          fields.value( 'columns', 'name', col['name'] )
							colorizeRow( '\t' + abbreviation + '\t' + name )
							# print( '\t', col['abbreviation'], '\t', col['name']  )

					if len( appInfo[__.appReg]['columns'] ):
						print()
						print()
					# print('\n')
			self.print()
			sys.exit()


		if len( self.isRequired[__.appReg] ):
			allSatisfied = True
			
			for req in self.isRequired[__.appReg]:
				satisfied = False
				for i in isActiveRequireList:
					if self.switches[i].name.lower() == req.lower():
						satisfied = True

				try:
					__.appInfoScan
				except Exception as e:
					if not satisfied:
						allSatisfied = False
						print()
						print( 'Error:\t\t missing required switch:', req )
						sys.exit()


		if len( hasActiveRequireList ):
			allSatisfied = True
			for i in hasActiveRequireList:
				satisfied = False
				for r in self.switches[i].documentation['required']:
					for ia in isActiveList:
						if self.switches[i].name.lower() == r.lower():
							satisfied = True
				if not satisfied:
					if not i in switchHelp:
						switchHelp.append( i )
						print()
						print( 'Error:\t\t missing required switch' )
					allSatisfied = False






		if self.isActive('Debug') == True or self.isActive('Errors') == True:
			# self.print()
			self.printStatus()
			sys.exit()
		
		if printAutoAbbreviations_scheduled:
			printAutoAbbreviations()

		# theErrors()
		pass
		pass
		# for i,record in enumerate(self.switches):
		#     self.index[ self.switches[i].name +'._.'+ self.switches[i].appReg ] = i

		
		
	def searchIndex( self, name, appReg ):
		if type(appReg) == bool or appReg is None:
			appReg = __.appReg
		try:
			result = self.index[ appReg ][ name ]
			
			# result = self.index[ name +'._.'+ appReg ]
		except Exception as e:
			try:
				result = self.index[ self.appRegDefault ][ name ]
			except Exception as e:
				# print( name, appReg, self.appRegDefault )
				result = None

		return result


	def print(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				switch.append({'name':sw.name ,'switch':sw.switch,'expected_input_example': sw.expected_input_example})
		# def test(value):
		#     value = value + '_V_'
		#     return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,switch,expected_input_example')
	def printStatus(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.active:
					active = 'True'
				else:
					active = 'False'
				value = sw.value
				if sw.value == True:
					value = 'True'
				elif sw.value == False:
					value = 'False'

				switch.append({'name':sw.name ,'active':active,'value': value})
		# def test(value):
		#     value = value + '_V_'
		#     return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,active,value')
	def length(self):
		ii = 0
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				ii += 1
		return ii

	def rebuild( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		data = []
		for i,row in enumerate(self.switches):
			# if not row.value is None:
			if row.appReg == appReg:
				if row.active:
					sX = row.switch.split(',')
					if row.value is None:
						r = sX[0]
					else:
						r = sX[0] + ' ' + str(row.value)
					data.append( r )
			# print(row.name,'\t',row.value,'\t',row.appReg)
		return ' '.join( data )
	def getTable( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		data = []
		for i,row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active:

					info = {
								'name': row.name,
								'value': row.value,
								'values': row.values,
					}

					data.append( info )
		return data


	def loadTable( self, data, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		for i,row in enumerate(self.switches):
			for info in data:
				if row.appReg == appReg:
					if row.name == info['name']:

						self.switches[i].value = info['value']
						self.switches[i].values = info['values']
						self.switches[i].active = True

	def onlyLoadEpoch( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		for i,row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active and not row.name == 'LoadEpoch':
					return False


		return True



#     def getSelf(self,name):
#         result = ''
#         for sw in self.switches:
#             if sw.name == name:
#                 result = sw
#         return result
# def getSwitchSelf(name):
#     global switches
#     return switches.getSelf(name)
def ci2(string):
	string = ci(string)
	string = _str.replaceAll(string,',',' ')
	return string

class TableView:

	def __init__(self,name,table,fields,sort):
		self.name = name
		self.fields = fields
		self.sort = sort
		self.table = table
		# print(self.name)



class Table:

	def __init__(self,name,asset=[]):
		self.name = name
		self.asset = asset
		self.fields = []
		self.views = []
		self.spaces = {}
		self.maxNameLength = 35
		self.columnTab = '\t'
		self.groupSeparator = '_'
		self.tableProfile = []
		self.tableProfileDefaultAlignment = 'left'
		self.tableProfileDefaultAlignmentHeader = ''
		self.tableProfileDefaultAlignmentChanged = False
		self.tableProfileDefaultAlignment = False
		self.tableProfileDefaultSupersedes = False
		self.views = []
		self.universalSpacing = False

	def registerView(self,name,fields,sort = ''):
		self.views.append(TableView(name,self.name,fields,sort))

	def printView(self,name):
		global switches
		i=0
		for tp in self.views:
			# print()
			# for x in dir(self.views[i]):
			#     print(x)

			if self.views[i].name == name:
				# print('found')
				switches.fieldSet('Sort','active',True)
				switches.fieldSet('Sort','value',str(self.views[i].sort))
				# print(switches.value('Sort'))
				# try:
					
				# except Exception as e:
				#     pass
				# print('name:',name)
				self.print(self.views[i].fields)
			i += 1

	# def trigger(self,field,script,includes):
	#     self.views.append({'name': field, 'script_trigger': script , 'includes': includes })


	def nameLength(self,string,suffix):
		result = ''
		toLong = False
		if switches.isActive('Length'):
			result = self.nameLengthFix(string,switches.value('Length'),'')
		else:
			try:
				i = 0
				for L in string:
					if i <= self.maxNameLength:
						result += L
					else:
						toLong = True
					i += 1
				if toLong == True:
					result += '...'
					if len(suffix) > 0:
						result += '  .' + suffix
			except Exception as e:
				result = string
		return result

	def nameLengthFix(self,string,change,suffix):
		result = ''
		toLong = False
		change = change.lower()
		old = self.maxNameLength
		if 'x' in change:
			change = change.replace('x','')
			newLength = self.maxNameLength * int(change)
		else:
			newLength = self.maxNameLength + int(change)
		try:
			i = 0
			for L in string:
				if i <= newLength:
					result += L
				else:
					toLong = True
				i += 1
			if toLong == True:
				result += '...'
				if len(suffix) > 0:
					result += '  .' + suffix
		except Exception as e:
			result = string
		return result

	def tabGetMaxSpace(self,name):
		global errors
		global switches
		rows = self.asset
		spacer = 1
		# print('*** ' + name)
		size = len(name) + spacer
		
		# print(name,00)
		# rows[0][name]
		try:
			pass
			rows[0][name]
		except Exception as e:
			errors.append({'id': 9, 'function': 'tabGetMaxSpace()', 'cnt': 1, 'location': 'rows[0][name]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			printBold('Error:','red')
			printBold('\tBad column input.')
			print(9)
			print(name)
			print(rows[0])
			os._exit(0)
		# print(name)
		for item in rows:
			shorten = True
			if switches.isActive('Long') == True:
				shorten = False
				if switches.isActive('ShortenColumn') == True:
					shortenColumn = switches.value('ShortenColumn')
					for sc in shortenColumn.split(','):
						if sc == name:
							shorten = True
				
			if shorten == True and not switches.isActive('Length'):
				try:
					text = self.nameLength( str(self.scriptTriggerField(name,item[name])) ,'')
				except Exception as e:
					text = self.nameLength(str(item[name]),'')
			else:
				if switches.isActive('Length'):
					# print('asdf')
					# sys.exit()
					try:
						
						text = self.nameLengthFix(  str(self.scriptTriggerField(name,item[name])) ,switches.value('Length'),'')
					except Exception as e:
						text = self.nameLengthFix(str(item[name]),switches.value('Length'),'')
				else:
					# sys.exit()
					try:
						text = str(self.scriptTriggerField(name,item[name]))
					except Exception as e:
						text = str(item[name])
						
			
			itemSize = len(str(text)) + spacer
			if itemSize > size:
				size = itemSize
			# print(item)
		return size

	def addSpace(self,string,max):
		dif = int(max) - len(string)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def addSpace2(self,max):
		dif = int(max)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def scriptTriggerField(self,field,value):
		i = 0
		for s in self.tableProfile:
			try:
				if self.tableProfile[i]['includes'] == True:
					if ',' in self.tableProfile[i]['name']:
						found = False
						for n in self.tableProfile[i]['name'].split(','):
							if n in field:
								found = True
						if found:
							value = self.tableProfile[i]['script_trigger'](value)
					else:
						if self.tableProfile[i]['name'] in field:
							value = self.tableProfile[i]['script_trigger'](value)
				else:
					if field == self.tableProfile[i]['name']:
						value = self.tableProfile[i]['script_trigger'](value)
			except Exception as e:
				pass
			i += 1
		return value
	def triggerExecute(self,field,value):
		i = 0
		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i]['trigger'](value)
				except Exception as e:
					pass
			i += 1
		return value

	def fieldProfileSet(self,field,propertyName,value):
		field = field.lower()
		if field == '*' and propertyName == 'alignment':
			self.tableProfileDefaultAlignment = value
			self.tableProfileDefaultAlignmentChanged = True
		if field == '_header_' and propertyName == 'alignment':
			self.tableProfileDefaultAlignmentHeader = value
		else:
			if ',' in field:
				for n in field.split(','):
					self.fieldProfileSet(n,propertyName,value)

			found = False
			i = 0
			for s in self.tableProfile:
				if self.tableProfile[i]['name'] == field:
					found = True
					self.tableProfile[i][propertyName] = value
				i += 1

			if not found:
				item = len(self.tableProfile)
				self.tableProfile.append({'name': field, propertyName: value})

	def fieldProfileGet(self,field,propertyName,isHeader = False):
		# print('ran')
		field = field.lower()
		i = 0
		value = ''
		if propertyName == 'alignment':
			value = self.tableProfileDefaultAlignment

		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i][propertyName]
				except Exception as e:
					pass
			i += 1
		if self.tableProfileDefaultAlignmentChanged and self.tableProfileDefaultSupersedes:
			value = self.tableProfileDefaultAlignment
		if isHeader and len(self.tableProfileDefaultAlignmentHeader) > 0:
			value = self.tableProfileDefaultAlignmentHeader
		elif isHeader:
			value = 'center'
		if propertyName == 'alignment' and value == '':
			value = 'left'
		return value
	def showColumn(self,column,i,columnHeaderLength):
		# print(column)
		global errors
		global lastGroup
		global switches
		def test(one,two):
			# print(one,two)
			if (one) == (two):
				return True
			else:
				return False
		groupByList = self.groupByList
		rows = self.asset
		# print(rows)

		columnList = column
		value = self.triggerExecute(column,str(rows[i][column]))
		# value = rows[i][column]
		# print(column,value)
		value = value.replace('\n','')
		# value = self.scriptTriggerField(column,rows[i][column])
		try:
			pass
		except Exception as e:
			pass

		shorten = True
		if switches.isActive('Long') == True:
			shorten = False
			if switches.isActive('ShortenColumn') == True:
				shortenColumn = switches.value('ShortenColumn')
				for sc in shortenColumn.split(','):
					if sc == column:
						shorten = True
		text = str(value)
		if shorten == True:
			text = self.nameLength(str(value),'')
		else:
			text = str(value)


		groupBy = switches.value('GroupBy')
		try:
			tabFix = self.spaces[column]
		except Exception as e:
			# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
			tabFix = self.tabGetMaxSpace(column)
			self.spaces[column] = tabFix

		if switches.isActive('GroupBy') == True:
			for gb in groupBy.split(','):
				gb = str(gb)
				if column == gb:
					# print('- -',last,text)
					if not test(groupByList[gb],text) == True:
						if groupBy.split(',')[0] == column:
							print(self.groupLine(columnList,columnHeaderLength))
							for g in groupBy.split(','):
								groupByList[g] = ''
						else:
							print('')
						groupByList[gb] = text
					else:
						pass
						text = ''
		alignment = self.fieldProfileGet(column,'alignment')
		# print(alignment)
		# if alignment == 'left':
		result = text + self.addSpace(text,tabFix)
		if alignment == 'left':
			result = text + self.addSpace(text,tabFix)
		if alignment == 'right':
			result = self.addSpace(text,tabFix) + text
		if alignment == 'center':
			totalSpace = int(tabFix) - len(text)
			if totalSpace > 0:
				if totalSpace % 2 == 0:
					div2 = totalSpace/2
					theLeft = div2
					theRight = div2
				else:
					divTMP = totalSpace - 1
					div2 = divTMP/2
					theLeft = div2 + 1
					theRight = div2
			else:
				theLeft = 0
				theRight = 0
			result = self.addSpace2(theLeft) + text + self.addSpace2(theRight)
			# print(column,theLeft,theRight,'0' + result + '0')
			# print(totalSpace,theLeft,theRight)
		#     result = theLeft + text + theRight
		return result

	def groupLine(self,columnList,columnHeaderLength):
		columnNumber = len(columnList.split(','))
		loop = 0
		result = ''
		while loop < columnHeaderLength + (columnNumber * 4):
			result += self.groupSeparator
			loop += 1
		return result

	def showColumnHeader(self,column):
		# rows = self.asset
		result = ''
		if type(self.universalSpacing) == dict:
			self.spaces = self.universalSpacing
		for c in column.split(','):
			try:
				tabFix = self.spaces[c]
			except Exception as e:
				# errors.append({'id': 11, 'function': 'showColumn()', 'cnt': 2, 'location': 'tabFix = spaces[c]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}], 'error': e})
				tabFix = self.tabGetMaxSpace(c)
				self.spaces[c] = tabFix
				# print(tabFix)
			# x
			# alignment = 'center'
			alignment = self.fieldProfileGet(c,'alignment',True)
			if alignment == '':
				########## Default Alignment ##########
				alignment = 'right'


			if alignment == 'center':
				totalSpace = int(tabFix) - len(c)
				if totalSpace > 0:
					if totalSpace % 2 == 0:
						div2 = totalSpace/2
						theLeft = div2
						theRight = div2
					else:
						divTMP = totalSpace - 1
						div2 = divTMP/2
						theLeft = div2 + 1
						theRight = div2
				else:
					theLeft = 0
					theRight = 0
				result += self.addSpace2(theLeft) + c.replace('_',' ').upper() + self.addSpace2(theRight) + self.columnTab
			if alignment == 'left':
				result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
			if alignment == 'right':
				result += self.addSpace(c,tabFix) + c.replace('_',' ').upper() + self.columnTab
			# else:
				# result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
		result += '\n'
		return result

	def findColumName( self, column ):
		for k in self.asset[0].keys():
			if k.lower() == column.lower():
				return k

	def print(self,column,fieldLengths=False):
		self.groupByTrigger()
		if type(fieldLengths) == dict:
			self.universalSpacing = fieldLengths
		# print(column)
		# print(self.assets)
		# rows = self.asset
		if not type(self.asset) == list or len(self.asset) == 0:
			print('Table Blank')
			sys.exit()
		global errors
		global switches
		global switchDefault
		column = column.lower()
		columnSearch = column
		column = ''
		for cs in columnSearch.split(','):
			try:
				column += self.findColumName(cs.split('=')[0]) + ','
			except Exception as e:
				column += cs + ','
				# print( 'Error: print column', cs )
				# sys.exit()
			# print(cs.split('=')[0])
		column = _str.cleanBE(column,',')
		# print(column)
		newData = []
		oldData = []
		if ':' in column or '=' in columnSearch:
			oldData = self.asset
		if ':' in column:
			depth = []
			flat = []
			for c in column.split(','):
				if not ':' in c:
					flat.append(c)
				else:
					try:
						found = False
						i=0
						for dp in depth:
							if depth[i]['parent'] == c.split(':')[0]:
								found = True
								dpID = i
							i+=1
					except Exception as e:
						found = False
					if found:
						depth[dpID]['children'].append(c.split(':')[1])
					else:
						depth.append({'parent': c.split(':')[0],'children': [c.split(':')[1]]})
			
			i = 0
			for data in self.asset:
				r = {}
				for f in flat:
					r[f] = data[f]
				x = []
				hasRecords = False
				for dp in depth:
					if len(data[dp['parent']]) > 0:
						hasRecords = True
						for dpi in data[dp['parent']]:
							y = {}
							hasData = False
							for dpic in dp['children']:
								if len(str(dpi[dpic])) > 1:
									hasData = True
								y[str(dp['parent']) + ':' + str(dpic)] = dpi[dpic]
							for f in flat:
								y[f] = r[f]
							if hasData:
								newData.append(y)
				if not hasRecords:
					for dpi in data[dp['parent']]:
						for dpic in dp['children']:
							r[str(dp['parent']) + ':' + str(dpic)] = ''
					newData.append(r)
				i+=1
			self.asset = newData
			# print(newData)
			# print('dasfdasdfasdfadsf')


		newData = []
		if '=' in columnSearch:
			for data in self.asset:
				rowInclude = True
				for c in columnSearch.split(','):
					if rowInclude:
						if '=' in c:
							cc = c.split('=')
							string = data[cc[0]]
							string = _str.cleanBE(string.lower(),' ')
							cc[1] = _str.cleanBE(cc[1],' ')
							try:
								dataYes = _str.cleanBE(cc[1].split('-')[0],' ')
							except Exception as e:
								dataYes = ''
							try:
								dataNo = _str.cleanBE(cc[1].split('-')[1],' ')
							except Exception as e:
								dataNo = ''
							if len(dataYes) > 0:
								# print('IS')
								# print(dataYes)
								length = 0

								for s in dataYes.split(' '):
									if rowInclude:
										rowInclude = False
										if len(s) > 0:
											length += 1
											# print(string)
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
													rowInclude = True
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													# print(s,string)
													cnt += 1
													rowInclude = True
											elif s in string:
												cnt += 1
												rowInclude = True
								# print(length,cnt)
								# if length == cnt:
								# if cnt > 0:
									# rowInclude = True
										# if switches.isActive('PlusOr') == True:
										#     if cnt > 0:
										#         rowInclude = True
							if len(dataNo) > 0 and rowInclude:
								# print('ISNOT')
								rowInclude = True
								try:
									for s in dataNo.split(' '):
										if len(s) > 0:
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													cnt += 1
											elif not string.find(ci(s)) == -1:
												cnt += 1
											# if not string.find(ci(s)) == -1:
											if cnt > 0:
												rowInclude = False
												break
								except Exception as e:
									pass
				if rowInclude:
					newData.append(data)
			self.asset = newData
			# print(self.asset)






		if not type(self.asset) == list or len(self.asset) == 0:
			print('Table Blank')
			sys.exit()



		# if not len(groupByList):
		self.groupByList = {}
		try:
			for gb in switches.value('GroupBy').split(','):
				self.groupByList[str(gb)] = ''
		except Exception as e:
			pass


		# if not column == False:
			# switches.fieldSet('Column','value',column)
			# column = switches.value('Column')
		if switches.isActive('Sort') == True:
			self.asset = self.sort()
		elif switches.isActive('GroupBy') == True:
			
			switches.fieldSet('Sort','active',True)
			switches.fieldSet('Sort','value',switches.value('GroupBy'))
			self.asset = self.sort()
		# print('-',column)
		columnHeader = self.showColumnHeader(column)
		columnHeaderLength = len(columnHeader)
		# print(columnHeader)
		printBold(columnHeader)
		i = 0
		# print(self.asset)
		for item in self.asset:
			# print(item)
			result = ''    
			for c in column.split(','):
				try:
					pass
					# result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					pass
				# print(result)
				try:
					pass
					result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					errors.append({'id': 12, 'function': 'print()', 'cnt': 1, 'location': "result += showColumn(rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': 'folder'}, {'name': 'column', 'value': column}], 'error': e})
					printBold('Error:','red')
					printBold('\tBad column input.')
					print(12)
					print(c)
					print(12)
					os._exit(0)
			# print(_str.totalStrip5(result)) #TESTING
			if len(result) > 0:
				# print(result)
				colorizeRow(result)
			i += 1
			if 'expected_input_example' in column and 'switch' in column and  switchDefault == i:

				print('')
		if len(oldData) > 0:
			self.asset = oldData
	def sort(self,fields=''):# sortThis
		rows = self.asset
		global errors
		global switches
		# self.sort = name
		tempFields = []
		delim = '.'
		if fields == '':
			name = switches.value('Sort')
		else:
			name = fields
		name = name.replace(':',delim)
		# if not name:
		sortBy = {}
		sortList = name.split(',')
		sortList.reverse()

		### Check for bad sort input
		for item in sortList:
			item = item
			try:
				if item.count(delim) > 0:
					sb = item.split(delim)[1]
				else:
					sb = item
			except Exception as e:
				errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})


		for item in sortList:
			try:
				direction = item.split(delim)[0]
				sb = self.findColumName(item.split(delim)[1])
				if 'a' in direction:
				# if direction.find('a') == 0:
					self.asset = sorted(self.asset, key=itemgetter(sb))
				else:
					self.asset = sorted(self.asset, key=itemgetter(sb), reverse=True)
			except Exception as e:
				try:
					pass
					self.asset = sorted(self.asset, key=itemgetter(self.findColumName(item)))
				except Exception as e:
					errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
				

			sortBy[item] = str(uuid.uuid4())
			tempFields.append( sortBy[item] )
			i = 0
			for row in self.asset:
				self.asset[i][sortBy[item]] = i
				i += 1

		# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

		sortCode = 'rows = sorted(rows, key=lambda d: ('
		for item in sortList:
			sortCode += "d['" + str(sortBy[item]) + "'],"
		sortCode = sortCode[:-1]
		sortCode += '))'
		exec(sortCode)
		if len( tempFields ):
			# print( tempFields )
			for ix,r in enumerate(rows):
				for tmp in tempFields:
					try:
						del rows[ix][tmp]
					except Exception as e:
						pass
		return self.asset

	def countThis(self):
		rows = self.asset
		i = 0
		for x in self.asset:
			i += 1
		return i

	def file(self,file):
		self.file = file

	def save(self,theFile = '',tableTemp = True,printThis = True):
		if theFile == '':
			theFile = str(self.file)
		self.file = theFile
		# print(theFile)
	# def saveTable(rows,theFile,tableTemp = True,printThis = True):
		# defaults to myTables
		if tableTemp == True:
			file0 = str(_v.myTables) + str(_v.slash) + str(theFile)
		else:
			file0 = _v.stmp + _v.slash + theFile
		dataDump = json.dumps(self.asset, indent=4, sort_keys=True)
		f = open(file0,'w')
		f.write(str(dataDump))
		f.close()
		if printThis:
			print('Saved: ' + file0)
	def get(self,theFile = '',tableTemp = True,printThis = False):
		if theFile == '':
			theFile = self.file
		self.file = theFile
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
				# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		else:
			json_data = []
		self.asset = json_data
		return json_data

	def assets(self):
		return self.asset

	def set(self,asset):
		self.asset = asset
		return self.asset

	def groupByTrigger( self ):
		try:
			if switches.isActive('GroupBy') and len(self.asset):
				newValues = []
				keys = []
				for key in self.asset[0].keys():
					keys.append( key )
				for val in switches.value('GroupBy').split( ',' ):
					for key in keys:
						if key.lower() == val.lower():
							newValues.append( key )
				if len(newValues):
					switches.fieldSet( 'GroupBy', 'value', ','.join(newValues) )
		except Exception as e:
			pass





class Tables:

	def __init__(self):
		self.tables = []

		self.maxNameLength = 35
		self.columnTab = '\t'
		self.groupSeparator = '_'




	def register(self,name,asset = []):
		found = False
		thisID = False
		for i,t in enumerate(self.tables):
			if t.name == name:
				found = True
				self.tables[i].maxNameLength = self.maxNameLength
				if len(asset) > 0:
					self.tables[i].set(asset)
		if not found:
			self.tables.append(Table(name,asset))
			self.tables[ len( self.tables )-1 ].maxNameLength = self.maxNameLength

	def trigger(self,name,field,script,includes = False):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].trigger(field,script,includes)
			i += 1

	def registerView(self,table,name,fields,sort):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].registerView(name,fields,sort)
			i += 1

	def fieldProfileSet(self,table,field,propertyName,value):
		i = 0
		found = False
		for t in self.tables:
			if t.name == table:
				found = True
				self.tables[i].fieldProfileSet(field,propertyName,value)
			i += 1
		if not found:
			self.tables.append(Table(table,[]))
			i = 0
			for t in self.tables:
				if t.name == table:
					self.tables[i].fieldProfileSet(field,propertyName,value)
				i += 1

	def print(self,name,fields,fieldLengths=False):
		# print(name,fields)
		i = 0
		for t in self.tables:
			if t.name == name:
				if len(self.tables[i].asset) > 0:
					self.tables[i].print(fields,fieldLengths)
				else:
					print('Table Blank')
			i += 1

	def sort(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
			i += 1

	def returnSorted(self,name,fields,asset = []):
		if len(asset) > 0:
			self.register(name,asset)

		result = []
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
				result = self.tables[i].asset
			i += 1
		return result
	def view(self,table,name):
		i = 0
		for t in self.tables:
			if t.name == table:
				try:
					self.tables[i].printView(name)
				except Exception as e:
					pass
			i += 1

	def save(self,table,theFile = '',tableTemp = True,printThis = True):
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].save(theFile,tableTemp,printThis)
			i += 1

	def get(self,table,theFile = '',tableTemp = True,printThis = False):
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].get(theFile,tableTemp,printThis)
			i += 1

	def asset(self,table):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].assets()
			i += 1

	def file(self,table,theFile):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].file(theFile)
			i += 1

	def set(self,table,asset):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].set(asset)
			i += 1

	def alignmentMasterSupersedes(self,table,value):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].tableProfileDefaultSupersedes = value
			i += 1
		
	def getLength(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		total = 0
		for r in result.keys():
			total += result[r]
			total += 5
		# print(result)
		return total

	def getFieldLengths(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		###### How it works:
		# totalColumnWidth = 0
		# for m in self.meta['data']:
		#     tables.register(m['table'],m['fields'])
		#     spaces = tables.getLength(m['table'],'type,field,max,min,average')
		#     if spaces > totalColumnWidth:
		#         totalColumnWidth = spaces


		# fieldLengths = 0
		# for m in self.meta['data']:
		#     tables.register(m['table'],m['fields'])
		#     data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#     if not type(fieldLengths) == dict:
		#         fieldLengths = data
		#     for name in fieldLengths.keys():
		#         if data[name] > fieldLengths[name]:
		#             fieldLengths[name] = data[name]




		# for m in self.meta['data']:
		#     genLine(totalColumnWidth,'=')
		#     print('Table:\t',m['table'])
		#     print('Parent:\t',m['parent'])
		#     print('Records:',m['count'])
		#     print()
		#     tables.register(m['table'],m['fields'])
		#     tables.fieldProfileSet(m['table'],'*','alignment','center')
		#     tables.print(m['table'],'type,field,max,min,average',fieldLengths)

		#     genLine(totalColumnWidth,'=')
		# print()
		# print('Records:',self.meta['records'])
		# print()
		# print('Errors:')
		# for e in self.meta['errors']:
		#     print('\t',e)

		return result

###########################################################################################
def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()
	return hash_md5.hexdigest()


def formatSize(size):
	try:
		size = int(size)
	except Exception as e:
		size = float(size)
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
	size = float(size)
	result = round(size * factor,0)
	return result

def timeAgo(do=''):
	if len(do) == 0:
		do = switches.value('Ago')
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
	dT = str(start_date)
	# print(dT)
	# print(dT)
	# print(dT)
	# print(dT)
	d = dT.split('-')
	result = datetime.datetime(int(d[0]),int(d[1]),int(d[2]),0,0).timestamp()

	# print(start_date)
	# print(result)]
	# print(result)
	return result
def epoch(string,end=False):
	string = str(string)
	if '.' in string:
		d = string.split('.')
	elif _v.slash in string:
		d = string.split(_v.slash)
	elif '-' in string:
		d = string.split('-')
	elif len(string) == 6:
		t = string[:4] + '-' + string[-2:]
		d = t.split('-')
	elif len(string) == 8:
		x = string[-4:]
		t = string[:4] + '-' + x[:2] + '-' + x[-2:]
		d = t.split('-')

	if not len(d) == 3:
		day = 1
	else:
		day = d[2]
	# print(d)
	# sys.exit()
	if end:
		y = int(d[0])
		m = int(d[1])
		if m == 12:
			y += 1
			m = 1
		else:
			m += 1
		start_date = datetime.datetime(y,m,1,0,0) + datetime.timedelta(-1)
		result = start_date.timestamp()
	else:
		result = datetime.datetime(int(d[0]),int(d[1]),int(day),0,0).timestamp()
	# result = d
	return result
def isNu(string):
	result = True
	for s in string:
		try:
			int(s)
		except Exception as e:
			result = False
	return result
def isNu2(string):
	result = True
	string = str(string).replace('.','').replace('-','').replace(_v.slash,'').replace('/','')
	try:
		try:
			int(string)
		except Exception as e:
			float(string)
	except Exception as e:
		result = False
	return result
def number2Words(n):
	global numberWords
	try:
		numberWords
		if len(numberWords) == 0:
			numberWords = getText(_v.myTables + _v.slash+'numberWords.txt')
	except Exception as e:
		numberWords = getText(_v.myTables + _v.slash+'numberWords.txt')
	numberWords = getText(_v.myTables + _v.slash+'numberWords.txt')
	if type(n) == int:
		result = numberWords[n].replace(' ','_').replace('-','_').replace('\n','')
	else:
		result = n.replace(' ','_')
	return result
###########################################################################################
###########################################################################################
def checkKey(dict, key):
	if key in dict.keys():
		return True
	else:
		return False

class Databases:

# FOREIGN KEY (project_id) REFERENCES projects (id)

	def __init__( self ):
		
		self.databases = []


	def register( self, name=False, file=False, table=False, records=False, fields=False, delete=False, description=False, project=False, auto=False, printFileActivity=False ):

		idx = len( self.databases )
		self.databases.append( Database( name=name, file=file, table=table, records=records, fields=fields, delete=delete, description=description, project=project, auto=auto, printFileActivity=printFileActivity ) )


	def search( self, name=False, info=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].search( info )

	def getFields( self, name=False, table=False, exclude=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].getFields( table, exclude )

	def update( self, name=False, info=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].update( info )

	def add( self, name=False, info=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].add( info )

	def insertRecords( self, name, table, records ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].insertRecords( table=table, records=records )
							
	def trigger( self, name, table, field, trigger ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].addTrigger( table, field, trigger )


class Database:
	
	def __init__( self, name=False, file=False, table=False, records=False, fields=False, delete=False, description=False, project=False, auto=False, printFileActivity=False ):
		self.initialized = []
		self.initializedDB = False
		self.tableInfo = []
		self.tables = []
		self.relationships = []

		self.name = name
		self.file = _v.myDatabases + _v.slash + file
		self.delete = delete
		self.printFileActivity = printFileActivity

		self.project = project
		self.description = description
		self.apps = False

		self.table = table
		self.records = records
		
		self.fieldsManual = fields
		self.fields = {}

		if type( table ) == bool:
			auto = True
		if not type( self.records ) == bool:
			for i,r in enumerate(self.records):
				self.records[i]['date_created'] = time.time()
				self.records[i]['date_modified'] = ''
				# print( self.records[i] )

		if self.delete and os.path.isfile( self.file ):
			os.unlink( self.file )
			if self.printFileActivity:
				print( ' file deleted ')
		if os.path.isfile( self.file ):
			if self.printFileActivity:
				print( ' file exists ')

		if auto and os.path.isfile( self.file ):
			self.genInfo( process=True )
		else:
			if not type( table ) == bool:
				if not type( self.records ) == bool:
					self.insertRecords( table )
					


	def generateStructure( self, table ):
		if not table in self.initialized:
			self.initialized.append( table )
			if os.path.isfile( self.file ):
				self.genInfo( process=True )
			else:
				fieldsData = self.processRecords()
				self.create( table, fieldsData )

				self.genInfo( process=True )

			

	def addTrigger( self, table, field, trigger ):
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for ii,fieldX in enumerate(self.tables[i].fields):
					if fieldX.name == field:
						self.tables[i].fields[ii].info['trigger'] = trigger




	def updateFieldInfo( self, table, field, label, data ):
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for ii,fieldX in enumerate(self.tables[i].fields):
					if fieldX.name == field:
						self.tables[i].fields[ii].info['label'] = data
	def updateManualFieldInfo( self ):
		if not type( self.fieldsManual ) == bool:
			for i,f in enumerate(self.fieldsManual):
				for k in f.keys():
					if not k == 'name' and not k == 'type' and not k == 'table':
						self.updateFieldInfo( f['table'], f['name'], k, f[k] )

	def getFields( self, table, exclude=False ):
		result = []
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for field in self.tables[i].fields:
					add = True
					if not type( exclude ) == bool:

						if type( exclude ) == str:
							ex = exclude.split(',')
						else:
							ex = exclude

						for x in ex:
							if len( x ) > 0:
								if x in field.name:
									add = False
					if add:
						result.append( field.name )

		return result

	def getFieldType( self, table, field ):
		result = ''
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for fieldX in self.tables[i].fields:
					if fieldX.name == field:
						result = fieldX.info['type']
		return result

	# def update( self, info ):

	#     sql = "update "+info['table']+" set [x] where " + info['update'] + " "
	#     u = ''
	#     for f in info['record'].keys():
	#         t = self.getFieldType( info['table'], f )
	#         if 'int' in t:
	#             u += f + " = " + str(info['record'][f]) + ","
	#         else:
	#             u += f + " = '" + str(info['record'][f]) + "',"
	#     u = _str.cleanBE( u, ',' )

	#     sql = sql.replace( '[x]', u )

	#     conn = sqlite3.connect( self.file )
	#     cursor = conn.cursor()
	#     tables = []
	#     rows = cursor.execute( sql )

	#     fields = self.getFields( info['table'] )
	#     results = []
	#     for row in (rows):
	#         d = {}
	#         for i,column in enumerate(row):
	#             d[ fields[i] ] = row[i]
	#         results.append( d )
	#     conn.commit()
	#     conn.close()

	def update( self, info ):

		sql = "update "+info['table']+" set [x] where " + info['update'] + " "
		u = ''
		for f in info['record'].keys():
			t = self.getFieldType( info['table'], f )
			if 'int' in t:
				u += f + " = " + str(info['record'][f]) + ","
			else:
				u += f + " = '" + str(info['record'][f]) + "',"
		u = _str.cleanBE( u, ',' )

		sql = sql.replace( '[x]', u )

		conn = sqlite3.connect( self.file )
		cursor = conn.cursor()
		tables = []
		rows = cursor.execute( sql )

		fields = self.getFields( info['table'] )
		results = []
		for row in (rows):
			d = {}
			for i,column in enumerate(row):
				d[ fields[i] ] = row[i]
			results.append( d )
		conn.commit()
		conn.close()

	def search( self, info ):
		if not self.initializedDB:
			print( 'no data' )
			sys.exit()

		if not type( info['custom'] ) == bool and not info['force']:
			sql = "select * from "+info['table']+" where "+info['custom']
		elif info['force'] and not type( info['custom'] ) == bool:
			sql = info['custom']
		else:
			if info['type'] == 'text':
				sql = "select * from "+info['table']+" where "+info['field']+" like '"+info['search']+"'"
			else:
				sql = "select * from "+info['table']+" where "+info['field']+" "+info['search']

		conn = sqlite3.connect( self.file )
		cursor = conn.cursor()
		tables = []
		rows = cursor.execute( sql )

		fields = self.getFields( info['table'] )
		results = []
		for row in (rows):
			d = {}
			for i,column in enumerate(row):
				# d[ fields[i] ] = row[i]
				d[ fields[i] ] = self.trigger( info['table'], fields[i], row[i] )
			results.append( d )

		conn.close()

		return results
		# print( info )
	def trigger( self, table, field, data ):
		result = data
		if field == 'date_created':
			return resolveEpochTest( data )
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for fieldX in self.tables[i].fields:
					if fieldX.name == field:
						if not type( fieldX.info['trigger'] ) == bool:
							result = fieldX.info['trigger']( data )
		return result


	def insertRecords( self, table, records=[] ):
		if len( records ) > 0:
			self.records = records
			for i,r in enumerate(self.records):
				self.records[i]['date_created'] = time.time()
				self.records[i]['date_modified'] = ''
		self.generateStructure( table )

		conn = sqlite3.connect(self.file)
		cursor = conn.cursor()
		for record in self.records:
			# self.records[i]['date_created'] = time.time()
			record['date_created'] = time.time()
			record['date_modified'] = ''
			sql = self.genRecordInsert( table, record )
			# n = ''

			# for field in fields:
			#     n += field['name'] + ' ' + field['type'] + ','

			# n = _str.cleanBE( n, ',' )
			# sql = sql.replace( '[n]', n )


			cursor.execute( sql )
			conn.commit()
		conn.close()






	def genRecordInsert( self, table, record ):
		b = "'insert into [table] ( [names] ) values ( [dataDel] )'.format( [data] )"
		n = ''
		dd = ''
		d = ''
		b = b.replace( '[table]', table )
		x = []

		for k in record.keys():
			n += k + ','
			d += "record['"+k+"'],"
			dd += '"{}",'
			x.append( record[k] )
		n = _str.cleanBE( n, ',' )
		dd = _str.cleanBE( dd, ',' )
		d = _str.cleanBE( d, ',' )

		b = b.replace( '[names]', n )
		b = b.replace( '[dataDel]', dd )
		b = b.replace( '[data]', d )
		# print( b )
		return eval( b )


	def genInfo( self, process=False ):
		if os.path.isfile( self.file ) and not self.initializedDB:
			self.initializedDB = True
			self.tableInfo = []
			sql = "select name from sqlite_master where type = 'table'"

			conn = sqlite3.connect( self.file )
			cursor = conn.cursor()
			tables = []
			tablesRaw = cursor.execute( sql )
			for table in tablesRaw:
				for data in table:
					if len( data ) > 1 and not 'sqlite' in data:
						tables.append( data )

			# print( tables )

			for table in tables:
				sql = 'PRAGMA table_info('+table+')'
				fieldsRaw = cursor.execute( sql )
				fields = []
				for fieldsX in fieldsRaw:

					if not type( self.fieldsManual ) == bool:
						data = list(filter(lambda itemX: itemX['name'] == fieldsX[1], self.fieldsManual))
						if len( data ) > 0:
							data[0][ 'type' ] = fieldsX[2]
							fields.append( data[0] )
						else:
							fields.append({ 'name': fieldsX[1], 'type': fieldsX[2],  })
					else:
						fields.append({ 'name': fieldsX[1], 'type': fieldsX[2],  })

					
				
				self.tableInfo.append({ 'name': table, 'fields': fields })

			conn.close()
			if process:
				self.addGeneratedTables()
			return self.tableInfo

	def addGeneratedTables( self ):
		dataOK = True
		if not type( self.records ) == bool:

			for record in self.processRecords():
				found = False
				for table in self.tableInfo:
					for field in table['fields']:
						if record['name'] == field:
							found = True
				if not found:
					dataOK = False
			
		for table in self.tableInfo:
			self.tables.append( DatabaseTables( table['name'], table['fields'] ) )
			self.updateManualFieldInfo()

	def processRecords( self ):
		autoFieldType = []
		for record in self.records:

			for field in record.keys():
				if len(list(filter(lambda itemX: itemX['name'] == field, autoFieldType))) == 0:
					if isText( record[ field ] ):
						t = 'text'
						if 'date_' in field:
							t = 'date'
						if not type( self.fieldsManual ) == bool:
							data = list(filter(lambda itemX: itemX['name'] == field, self.fieldsManual))
							if len( data ) > 0:
								data[0][ 'type' ] = t
								autoFieldType.append( data[0] )
							else:
								autoFieldType.append({ 'name': field, 'type': t })
						else:
							autoFieldType.append({ 'name': field, 'type': t })
					if isNum( record[ field ] ):
						t = 'integer'
						if 'date_' in field:
							t = 'date'
						if not type( self.fieldsManual ) == bool:
							data = list(filter(lambda itemX: itemX['name'] == field, self.fieldsManual))
							if len( data ) > 0:
								data[0][ 'type' ] = t
								autoFieldType.append( data[0] )
							else:
								autoFieldType.append({ 'name': field, 'type': t })
						else:
							autoFieldType.append({ 'name': field, 'type': t })
					if isFloat( record[ field ] ):
						t = 'real'
						if 'date_' in field:
							t = 'date'
						if not type( self.fieldsManual ) == bool:
							data = list(filter(lambda itemX: itemX['name'] == field, self.fieldsManual))
							if len( data ) > 0:
								data[0][ 'type' ] = t
								autoFieldType.append( data[0] )
							else:
								autoFieldType.append({ 'name': field, 'type': t })
						else:
							autoFieldType.append({ 'name': field, 'type': t })


		return autoFieldType

	def fieldInfo( self, table, field, fType ):
		self.fields[ field ] = fType

	def create( self, table=False, fields=False ):
			
		if os.path.isfile(self.file):
			print( 'Database exists' )
		else:
			conn = sqlite3.connect(self.file)
			cursor = conn.cursor()
			# sql =  'CREATE TABLE '+table+' ([n])'
			sql =  'CREATE TABLE '+table+' (id integer primary key autoincrement not null, [n])'
			n = ''
			nn = ''
			for field in fields:
				n += field['name'] + ' ' + field['type'] + ','
				if not 'date_modified' == field['name']:
					nn += field['name'] + ','

			n = _str.cleanBE( n, ',' )
			nn = _str.cleanBE( nn, ',' )
			sql = sql.replace( '[n]', n )
			cursor.execute( sql )
			sql =    "CREATE TRIGGER UpdateLastTime UPDATE OF "+nn+" ON "+table+" "\
					" BEGIN"\
					"  UPDATE "+table+" SET date_modified=datetime('now','localtime') WHERE id=old.id;"\
					" END;"
			cursor.execute( sql )

			conn.close()





class DatabaseTables:
	def __init__( self, table=False, fields=False ):
		
		self.fields = []

		self.table = table

		if not type( fields ) == bool:
			for i,field in enumerate(fields):
				idx = len( self.fields )
				self.fields.append( DatabaseFields( field['name'], field['type'] ) )
				for label in field.keys():
					if not label == 'name' and not label == 'type' and not label == 'table':
						self.fields[ idx ].addFieldInfo( label, field[ label ] )

	def setInfo( self, field, label, info ):
		for i,row in enumerate(self.fields):
			if self.fields[i].name == field:
				self.fields[i].info[ label ] = info


	def setFields( self, fields=False ):
		if not type( fields ) == bool:
			for i,field in enumerate(fields):
				idx = len( self.fields )
				self.fields.append( DatabaseFields( field['name'], field['type'] ) )
				for label in field.keys():
					if not label == 'name' and not label == 'type' and not label == 'table':
						self.fields[ idx ].addFieldInfo( label, field[ label ] )

	def updateFieldInfo( self, field, label, data ):
		for i,f in enumerate(self.fields):
			if self.fields[i].name == field:
				self.fields[i].info[ label ] = data


class DatabaseFields:
	def __init__( self, name=False, fieldType='text' ):
		self.name = name

		self.info = {
						'name': name,
						'type': fieldType,
						'trigger': False,
						'default': False,
		}

	def addFieldInfo( self, label, info ):
		self.info[ label ] = info

	def fieldInfo( self, label ):
		if label in list( self.info.keys() ):
			return self.info[ label ]
		else:
			return False



###########################################################################################
###########################################################################################

class Database2:

	def __init__(self, data):

		appDB = '_Generated_App_Database.db'
		appJSON = '_Generated_App_Database_Config.json'
		appPyRaw = '_Gen_App_Database_Data'
		appPy = appPyRaw + '.py'
		self.appPyDefault = _v.myDatabases + _v.slash+'_default.py'


		self.data = {}
		self.tables = []
		self.name = data.replace(appDB,'').replace(appJSON,'').replace(appPy,'').replace('.json','')
		if os.path.isfile(self.name + appDB):
			self.appDB =   self.name + appDB
			self.appJSON = self.name + appJSON
			self.appPy =   self.name + appPy

		else:
			self.appDB = _v.myDatabases + _v.slash + self.name + appDB
			self.appJSON = _v.myDatabases + _v.slash + self.name + appJSON
			self.appPy = _v.myDatabases + _v.slash + self.name + appPy
		self.appPyRaw = self.name + appPyRaw

		self.tableDelim = '_x_'

		self.meta = []

	def registerTable(self, name):
		self.tables.append(TablesDB(name))

	def TableFieldCount(self):
		result = 0
		for i,ci in enumerate(self.tables):
			if ci.name == name:
				result = self.tables[i].getCount()
		return result
# {
#     'table': 'table,name',
#     'fields': [
#         {'names': 'one,two'},
#         {'names': 'three', 'table': 'name', 'as': 'threeish'}
#     ],
#     'action': [
#        { 'type': 'text', 'names': 'field', 'table': 'your_mom', 'search': '*.txt,desktop'},
#        { 'type': 'text', 'names': 'testy', 'and_or': 'or', 'table': 'or_test', 'search': '*.py,*.txt'},
#         { 'type': 'field_type(text)', 'table': 'name', 'names': 'field,names', 'and_or': 'and',  'search': '*.py,tech'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': '1000,2000'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'g,1000'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'l,1000'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(ago(2000))'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(epoch(2018.07))'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(epoch(2018.07)),str(epoch('2018.10',True))'},
#         { 'type': 'field_type(sort)', 'names': 'field', 'order': 'asc'},
#         { 'type': 'field_type(sort)', 'names': 'field', 'order': 'desc'},
#     ]
# }    

	def queryBuilder(self,data): # queryBuilder
		self.data = data
		# print(data['fields'])
		# sys.exit()
		self.qbFields = []
		tbls = data['table'].split(',')
		if len(tbls) > 1:
			multi_Table = True
		else:
			multi_Table = False
		if multi_Table:
			sql = 'SELECT '
			# print(data['fields'])
			for field in data['fields']:
				for name in field['names'].split(','):
					thisT = ''
					try:
						thisT = field['table']
					except Exception as e:
						thisT =  tbls[0]
					try:
						asF = field['as']
					except Exception as e:
						asF =  name
					name = "" + thisT + '.' + name + " AS " + asF
					self.qbFields.append(asF)
					sql += name + ', '
			sql = _str.cleanLast(sql,', ')
			sql += ' FROM ' + tbls[0] + ' '
			for iJ,tJ in enumerate(tbls):
				if iJ > 0:
					sql += ' JOIN ' + tJ + ' ON ' + tJ + '.id_parent = ' + tbls[0] + '.id_uuid '
				
			sql += ' WHERE '
		else:
			sql = 'SELECT '
			for field in data['fields']:
				for name in field['names'].split(','):
					thisT = ''
					try:
						thisT = field['table']
					except Exception as e:
						thisT =  tbls[0]
					try:
						asF = field['as']
					except Exception as e:
						asF =  name
					name = "" + thisT + '.' + name + " AS " + asF
					self.qbFields.append(asF)
					sql += name + ', '
			sql = _str.cleanLast(sql,', ')
			sql += ' FROM ' + tbls[0] + ' WHERE '
		# JOIN albums ON albums.albumid = tracks.albumid
		orderBy = False
		for i,action in enumerate(data['action']):
			if action['type'] == 'text':
				sql += '('
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "" + thisT + '.' + name + ""
					try:
						and_or = action['and_or']
					except Exception as e:
						and_or =  'and'
					for tv in action['search'].split(','):
						if tv.startswith('*'):
							tv = tv.replace('*','')
							sql += ' ' + name + " like '%" + tv + "' " + and_or + ' '
						elif tv.endswith('*'):
							tv = tv.replace('*','')
							sql += ' ' + name + " like '" + tv + "%' " + and_or + ' '
						else:
							sql += ' ' + name + " like '%" + tv + "%' " + and_or + ' '
				sql = _str.replaceDuplicate(sql,' ')
				sql = _str.cleanLast(sql,' and ')
				sql = _str.cleanLast(sql,' or ')
				sql += ') and '
			sql = sql.replace('WHERE and ','WHERE ')
			if action['type'] == 'number':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if not len(coin) == 2:
						print('bad input')
						sys.exit()
					if isNu(coin[0]):
						do = 'b'
					else:
						do = coin[0]
					if do == 'b':
						sql += name + ' > ' + str(coin[0]) + " and " + name + " < " + str(coin[1]) + ' and '
					if do == 'l':
						sql += name + ' < ' + str(coin[1]) + ' and '
					if do == 'g':
						sql += name + ' > ' + str(coin[1]) + ' and '












			if action['type'] == 'date':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if not len(coin) == 2:
						if isNu2(coin[0]):
							sql += name + ' > ' + str(epoch(coin[0])) + ' and '
						else:
							sql += name + ' > ' + str(timeAgo(coin[0])) + ' and '
					else:
						if isNu2(coin[0]):
							do = 'b'
						else:
							do = coin[0]
						if do == 'b':
							sql += name + ' > ' + str(epoch(coin[0])) + " and " + name + " < " + str(epoch(coin[1],True)) + ' and '
						if do == 'l':
							sql += name + ' < ' + str(epoch(coin[1])) + ' and '
						if do == 'g':
							sql += name + ' > ' + str(epoch(coin[1])) + ' and '




			if action['type'] == 'bytes':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if coin[0] == 'l':
						sql += name + ' < ' + str(unFormatSize(coin[1])) + ' and '
					elif coin[0] == 'g':
						sql += name + ' > ' + str(unFormatSize(coin[1])) + ' and '
					else:
						sql += name + ' > ' + str(unFormatSize(coin[0])) + " and " + name + " < " + str(unFormatSize(coin[1])) + ' and '














			if action['type'] == 'sort':
				orderBy = True
		sql = _str.cleanLast(sql,' and ')
		sql = _str.cleanLast(sql,' or ')
		if orderBy:
			sql += ' ORDER BY '
			for i,action in enumerate(data['action']):
				if action['type'] == 'sort':
					try:
						if 'a' in action['order'].lower():
							order = 'ASC'
						else:
							order = 'DESC'
					except Exception as e:
						order = 'ASC'
					for name in action['names'].split(','):
						if multi_Table:
							try:
								thisT =  action['table']
							except Exception as e:
								thisT =  tbls[0]
							name = "'" + thisT + '.' + name + "'"
						sql += name + ' ' + order + ', '

		sql = _str.cleanLast(sql,' and ')
		sql = _str.cleanLast(sql,' or ')
		sql = _str.cleanLast(sql,', ')
		sql = _str.replaceDuplicate(sql,' ')
		sql = _str.cleanLast(sql,' ')
		sql += ';'
		sql = sql.replace('WHERE;',';')
		return sql
	def metaGen(self):
		import re
		import numpy as np
		meta = []
		con = sqlite3.connect(self.appDB)
		for line in con.iterdump():
			if 'CREATE TABLE' in line and not 'INSERT INTO' in line:
				# print(line)
				one = line.split('CREATE TABLE ')[1]
				two = one.split(' (')
				table = two[0]
				# print(table)
				fieldRaw = two[1].split(')')[0]
				f = []
				for field in fieldRaw.split(', '):
					# print('\t',field)
					fd = field.split(' ')
					f.append({'type': fd[1], 'field': fd[0], 'max': 0, 'min': 0, 'average': 0})


				if self.tableDelim in table:
					parent = ''
					mx = len(table.split(self.tableDelim))-1
					for iT,tX in enumerate(table.split(self.tableDelim)):
						if iT < mx:
							parent += tX + self.tableDelim
					parent = _str.cleanLast(parent,self.tableDelim)
				else:
					parent = ''


				meta.append({'table': table, 'parent': parent, 'fields': f})
			elif 'INSERT INTO' in line:
				pass
				# break
		average = {}
		for im,m in enumerate(meta):
			sql = 'SELECT * FROM ' + m['table']
			conn = sqlite3.connect(self.appDB)
			c = conn.cursor()
			c.execute(sql)
			rows = c.fetchall()
			for row in rows:
				# print(row)
				for fi,field in enumerate(m['fields']):
					# print(field['field'],row[fi])
					aKey = str(m['table']) + '-' + str(number2Words(field['field']))
					# print(aKey)
					
					try:
						if not type(average[aKey]['datapoints']) == list:
							average[aKey] = {'max': 0, 'min': 'first', 'average': 0, 'datapoints': [], 'count': 0}

						# print(type())                        
					except Exception as e:
						average[aKey] = {'max': 0, 'min': 'first', 'average': 0, 'datapoints': [], 'count': 0}
					average[aKey]
					# print(aKey)
					if field['type'] == 'int':
						if type(row[fi]) == int:
							size = row[fi]
						else:
							string = re.sub('[^0-9]', '', str(row[fi]))
							# print(type(string),string)
							# print(string)
							if len(string) == 0:
								size = 0
							else:
								size = int(string)
					if field['type'] == 'str':
						size = len(str(row[fi]))
					# print()
					# print(type(average[aKey]['max']),average[aKey]['max'])
					# print(type(size),size)
					if average[aKey]['max'] < size:
						average[aKey]['max'] = size
					if average[aKey]['min'] == 'first':
						average[aKey]['min'] = size
					elif average[aKey]['min'] > size:
						average[aKey]['min'] = size
					average[aKey]['datapoints'].append(size)

		errors = []
		totalCount = 0
		for im,m in enumerate(meta):

			for row in rows:
				# print(row)
				for fi,field in enumerate(m['fields']):
					# print(meta[im]['fields'][fi]['max'])
					aKey = m['table'] + '-' + number2Words(field['field'])
					# print(aKey)
					try:
						# print(average[aKey]['max'])
						meta[im]['fields'][fi]['max'] = average[aKey]['max']
						meta[im]['fields'][fi]['min'] = average[aKey]['min']
						meta[im]['fields'][fi]['average'] = int(np.mean(average[aKey]['datapoints']))
						meta[im]['count'] = len(average[aKey]['datapoints'])
						total = meta[im]['count']
					except Exception as e:
						errors.append(aKey)
				totalCount += total

		self.meta = {'data': meta, 'records': totalCount, 'errors': errors}
		saveTable2(meta,'database_meta.json')

		return meta
	def metaPrint(self):
		if self.meta == []:
			self.metaGen()

		totalColumnWidth = 0
		for m in self.meta['data']:
			tables.register(m['table'],m['fields'])
			spaces = tables.getLength(m['table'],'type,field,max,min,average')
			if spaces > totalColumnWidth:
				totalColumnWidth = spaces



		# fieldLengths = 0
		# for m in self.meta['data']:
		#     tables.register(m['table'],m['fields'])
		#     data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#     if not type(fieldLengths) == dict:
		#         fieldLengths = data
		#     for name in fieldLengths.keys():
		#         if data[name] > fieldLengths[name]:
		#             fieldLengths[name] = data[name]




		for m in self.meta['data']:
			genLine(totalColumnWidth,'=')
			print('Table:\t',m['table'])
			print('Parent:\t',m['parent'])
			print('Records:',m['count'])
			print()
			tables.register(m['table'],m['fields'])
			# tables.fieldProfileSet(m['table'],'*','alignment','center')
			# tables.print(m['table'],'type,field,max,min,average',fieldLengths)
			tables.print(m['table'],'type,field,max,min,average')

			genLine(totalColumnWidth,'=')
		print()
		print('Records:',self.meta['records'])
		print()
		print('Errors:')
		for e in self.meta['errors']:
			print('\t',e)
		print()
		print()
		print('Example:')
		print('\t p dba -app',self.name)
		print()
		print()
	def findParent(self,table):
		# parent = 'Error'
		# for m in self.meta['data']:
		#     if m['table'] == table:
		#         parent = m['parent']
		#         break
		if self.tableDelim in table:
			parent = ''
			mx = len(table.split(self.tableDelim))-1
			for iT,tX in enumerate(table.split(self.tableDelim)):
				if iT < mx:
					parent += tX + self.tableDelim
			parent = _str.cleanLast(parent,self.tableDelim)
		else:
			parent = ''
		return parent

	def findChildren(self,table):
		if self.meta == []:
			self.metaGen()
		children = []
		for m in self.meta['data']:
			if m['parent'] == table:
				children.append(m['table'])

		return children

	def findType(self,column):
		mainTable = self.data['table'].split(',')[0]
		found = False
		nm = ''
		result = ''

		for action in self.data['fields']:
			for name in action['names'].split(','):
				if name == column:
					try:
						if action['type'] == 'date' or 'byte' in action['type']:
							result = action['type']
					except Exception as e:
						pass

		if len(result) == 0:
			for action in self.data['action']:
				for name in action['names'].split(','):
					if name == column:
						if action['type'] == 'date' or 'byte' in action['type']:
							result = action['type']

		if len(result) == 0:
			for field in self.data['fields']:
				try:
					table = field['table']
				except Exception as e:
					table = mainTable
				if ',' in field['names']:
					for name in field['names'].split(','):
						if name == column:
							nm = name
							found = True
				else:
					try:
						newName = field['as']
					except Exception as e:
						newName = field['names']
					if newName == column:
						nm = newName
						found = True
				# print(field)
				if found:
					break

			result = self.checkConfig(table,nm)
		# print(mainTable)
		return result
	def checkConfig(self,tbl,nm):
		self.appJSON
		# print(self.appJSON)
		# print(tbl,nm)
		structure = getTable2(self.appJSON)
		result = ''
		if tbl == structure['name']:
			for zs in structure['zstructure']:
				if zs['field'] == nm:
					result = zs['type']
					break
		return result

	def executeSQL(self,sql,group=0):
		conn = sqlite3.connect(self.appDB)
		c = conn.cursor()
		c.execute(sql)
		all_rows = c.fetchall()
		records = []
		for f in all_rows:
			row = {}
			for ic,c in enumerate(self.qbFields):
				row[c] = f[ic]

			records.append(row)
		col = ''
		for c in self.qbFields:
			col += c + ','
		col = _str.cleanLast(col,',')
		tables.register('sql',records)
		for ic,c in enumerate(self.qbFields):
			if self.findType(c) == 'date':
				tables.fieldProfileSet('sql',c,'trigger',float2Date2)
			if 'byte' in self.findType(c):
				tables.fieldProfileSet('sql',c,'trigger',formatSize)
			if self.findType(c) == 'bytes':
				tables.fieldProfileSet('sql',c,'trigger',formatSize)
			# print(self.findType(c))
		tables.print('sql',col)


















class TablesDB:

	def __init__(self):
		self.columns = []

	def register(self, name):
		self.columns.append(ColumnsDB(name))
		self.fieldCount = len(self.columns)

	def getCount(self):
		return self.fieldCount


class ColumnsDB:

	def __init__(self, name, kind):
		self.name = name
		self.active = False
		self.kind = kind

	# def trigger(self,script):
	#     self.script_trigger = script

	# def changeStatus(self,newStatus):
	#     self.active = newStatus

	# def print(self):
	#     childItems = []
	#     for ci in self.columns:
	#         childItems.append({'name':ci.name})
	#     tables.register('childClassItems',childItems)
	#     # tables.trigger('switches','switch,name',test,True)
	#     tables.print('childClassItems','name')


	#         childItems.append({'name':ci.name ,'active':active,'value': value})
	#     tables.register('childClassItems',childItems)
	#     tables.print('childClassItems','name,active,value')

	# def status(self,name,newStatus):
	#     for i,ci in enumerate(self.columns):
	#         if ci.name == name:
	#             self.columns[i].changeStatus(newStatus)


###########################################################################################
def get_size(obj, seen=None):
	# https://medium.com/@alexmaisiura/python-how-to-reduce-memory-consumption-by-half-by-adding-just-one-line-of-code-56be6443d524
	# From https://goshippo.com/blog/measure-real-size-any-python-object/
	# Recursively finds size of objects
	size = sys.getsizeof(obj)
	if seen is None:
		seen = set()
	obj_id = id(obj)
	if obj_id in seen:
		return 0


###########################################################################################
def genLine(count,what):
	count = int(count)
	what = str(what)
	cnt = 0
	result = ''
	while cnt < count:
		result += what
		cnt += 1
	print(result)
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



def randomTrueFalse(fix=2):
	import random

	global randomTrueFalseLast
	global randomTrueFalseCount
	global randomTrueFalseSame
	try:
		randomTrueFalseLast
	except Exception as e:
		randomTrueFalseLast = True
		randomTrueFalseSame = 0
		randomTrueFalseCount = 0

	ran = random.randint(1,101)
	result = ran % 2 == 0
	i = 0
	while i < fix:
		i+=1
		if result == randomTrueFalseLast:
			ran = random.randint(1,101)
			result = ran % 2 == 0

	if result == randomTrueFalseLast:
		randomTrueFalseSame += 1
	randomTrueFalseCount += 1
	randomTrueFalseLast = result
	return result
def randomizeCase(string):
	import random

	result = ''
	for ch in string:
		if ch.isalnum():
			try:
				int(ch)
			except Exception as e:
				ran = random.randint(1,101)
				test = ran % 2 == 0
				if randomTrueFalse():
					ch = ch.lower()
				else:
					ch = ch.upper()
		result += ch
	return result

def onlyAlpha(string):
	result = ''
	for ch in string:
		if ch.isalnum():
			try:
				int(ch)
			except Exception as e:
				result += ch
	return result

def onlyNumbers(string):
	result = ''
	for ch in string:
		if ch.isalnum():
			try:
				int(ch)
				result += ch
			except Exception as e:
				pass
	return result
def onlyAlphaNumeric(string):
	result = ''
	for ch in string:
		if ch.isalnum():
			result += ch
	return result
def longID(howMany=2):
	result = ''
	i = 0
	while i < howMany:
		result += genUUID()
		i += 1
	result = result.replace('}{','-')
	return result


# def resolveLocal(file):
#     if os.path.isfile(file):
# %python%\%*.py
# %phpFiles%\%*.php
# %scriptroot%\%*.bat
# %powershell%\%*.ps1
# D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1
# %myPhp%\%*.php
# %myPowershell%\%*.ps1
# %myPython%\%*.py
# %myTables%\%*
# %myTables%\%*.json
# %myDatabases%\%*
# %myWebApp%\%*
# %USERPROFILE%\Desktop\%*






def formatColumns(columns):
	# print(__.appReg)
	# print(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if '.' in c or ':' in c:
				hasPre = True
				c = c.replace(':','.')
				preDataR = c.split('.')
				preData = preDataR[0]
				c = preDataR[1]

			for col in appInfo[__.appReg]['columns']:
				for a in col['abbreviation'].split(','):
					if a == c:
						c = col['name']
			if hasPre:
				c = preData + '.' + c
			result += c + ','
		result = result[:-1]
	return result

def defaultScriptTriggers():
	if len(appInfo[__.appReg]['columns']) > 0:
		switches.trigger('Column',formatColumns)
		switches.trigger('Sort',formatColumns)
		switches.trigger('GroupBy',formatColumns)

printAutoAbbreviations_scheduled = False
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
			# sys.exit()
			# print(first)


def printAutoAbbreviations():
	global printAutoAbbreviations_scheduled
	if printAutoAbbreviations_scheduled and switches.isActive('PrintAutoAbbreviations'):
		print()
		print('Columns and abbreviations:')
		result = ''
		for col in appInfo[__.appReg]['columns']:
			result += col['name'] + '(' + col['abbreviation'] + '), '
		result = result[:-2]
		print('\t' + result + '\n')
		print()











#########################################################################################################################################################

class Threads:
	# Threads.openCnt
	# Threads.closedCnt
	openCnt = 0
	closedCnt = 0
	def __init__( self, name, func, arg, kwargs, focus, qID, addID, pID ):
		global appInfo
		# Threads.openCnt += 1
		self.active = False
		
		self.created = time.time()
		self.app = appInfo[focus]['file']
		self.name = name
		self.func = func
		self.focus = focus
		self.arg = arg
		self.kwargs = kwargs
		self.qID = qID
		self.addID = addID
		self.created = time.time()
		self.status = True
		self.instance = ''
		self.bottom = False
		self.timeout = False
		self.pID = pID



		self.data = False
		# self.trigger = False
		# self.triggerArg = False
		self.executed = False
		self.triggerError = False
		
		__.threadActivity[self.qID] = {}
		__.threadActivity[self.qID]['error'] = False
		__.threadActivity[self.qID]['activity'] = time.time()
		__.threadActivity[self.qID]['log'] = False

		# try:
		#     self.instance = appInfo[focus]['instance']
		# except Exception as e:
			


		self.log = { 
						'id':       self.qID,
						'parent':    self.pID,
						'app':      self.app,
						'func':     self.func.__name__,
						'arg':      self.arg,
						'instance': self.instance,
						'focus':    self.focus,
						'start':    0,
						'end':      0,
						'runtime':  0,
						'mem':      0,
						'lines':      0,
						'wait':     0,
						'qcount':   0
		}




		try:
			self.argID = self.arg
			self.argID.append( self.qID )
		except Exception as e:
			self.argID = False

	def getLog( self ):
		self.log['error'] = __.threadActivity[self.qID]['error']
		self.log['activity'] = __.threadActivity[self.qID]['activity']
		self.log['errorlog'] = __.threadActivity[self.qID]['log']
		return self.log

		

	def open( self ):
		__.queueLastActivity = time.time()
		self.active = True
		self.log['start'] = time.time()
		self.log['qcount'] = __.queueCount

		if self.kwargs:
			if self.addID:
				data = [{ 'func': self.func, 'args': self.arg[:-1] }]
				data[0]['args'][0]['qID']=self.qID
				threadTimer( .0001, threadKwargs, data, qID=self.qID )
			else:
				data = [[{ 'func': self.func, 'args': self.arg }]]
				threadTimer( .0001, threadKwargs, data, qID=self.qID )
		else:
			if self.addID:
				threadTimer( .0001, self.func, self.argID, qID=self.qID )
			else:
				threadTimer( .0001, self.func, self.arg, qID=self.qID )

	def close( self, mem=0, data=False, trigger=False, triggerArg=False, kwargs=False, lines=0 ):
		__.queueLastActivity = time.time()
		if not type(trigger) == bool:
			try:
				triggerName = trigger.__name__
			except Exception as e:
				triggerName = ''

			try:




				if type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger )
				elif not type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger, data )
				elif type(data) == bool and not type(triggerArg) == bool:
					threadTimer( .0001, trigger, triggerArg )
				elif not type(data) == bool and not type(triggerArg) == bool and kwargs:
					args = [{ 'func': trigger, 'args': triggerArg }]
					args[0]['args'][0]['data'] = data
					threadTimer( .0001, threadKwargs, args )
				elif not type(data) == bool and not type(triggerArg) == bool and not kwargs:
					try:
						triggerArg.append(data)
						threadTimer( .0001, threadKwargs, triggerArg )
					except Exception as e:
						try:
							triggerArg[0].append(data)
							threadTimer( .0001, threadKwargs, triggerArg )
						except Exception as e:
							printBold('close trigger error '+str(self.focus)+' '+ str(self.name) +' '+ str(self.func)+' '+ str(triggerName), 'red' )
							self.triggerError = True


				self.executed = True
				if self.triggerError:
					self.executed = False
			except Exception as e:
				printBold('close trigger error '+str(self.focus)+' '+ str(self.name) +' '+ str(self.func)+' '+ str(triggerName), 'red')
				self.triggerError = True

		

		# Threads.closedCnt += 1
		# print('Closed:',self.qID,'\tTotal Closed:',Threads.newCounter,'\tScheduler:',__.queueCountScheduleAudit,__.queueCountSchedule,'\tTimers:',__.queueCountTimer)
		self.status = False
		self.log['end'] = time.time()
		self.log['runtime'] = self.log['end'] - self.log['start']
		self.log['mem'] = mem
		self.log['lines'] = lines
		if not type(data) == bool:
			self.data = data
		return self.qID

	def openCnt( self ):
		return Threads.openCnt

	def closedCnt( self ):
		return Threads.closedCnt
#########################################################################################################################################################
class Queue:

	def __init__( self ):

		self.created = time.time()
		self.loadedBy = 0
		self.loadTime = 0
		self.completionTime = 0
		self.lastActivity = 0
		

		self.records = {}
		self.nextID = 0
		self.opened = 0
		self.closed = 0
		self.notstarted = 0
		self.maxInQueue = 0
		self.maxThreads = 100
		self.maxThreadsSafe = 100
		self.minThreads = 50
		self.table = {'focus': [], 'name': []}
		self.schedulerInitialized = False


		self.auditPrint = True
		self.maxThreadsAuto = True
		self.auditInitialized = False
		self.auditPercentChangeMax = 30
		self.auditPercentChangeMin = 10
		self.auditPercentReduceBy = 5
		self.auditPercentReduceByDrastic = 15
		self.auditPercentDrasticThreshold = 3
		self.auditWatchMax = 5
		self.auditPercentSample = 10
		self.auditMaxFailuresBeforeAction = 3
		self.auditLogInternal = []
		self.auditLogExternal = []
		self.auditAutoAdjust = False


		##
		self.scheduleLoop = .01
		self.auditLoop = .1
		self.autoLoadedAfter = 5
		self.statusTotal = 0
		self.prefix = False
		##


		self.autoLoaded = True

		self.report = False
		self.reportPrinted = False


		self.timeout = False
		self.timeoutAsk = False


		self.saveLog = True
		self.isLoaded = False

		self.appStructure = __.structure()

		__.totalTask = 0
		__.queueCount = 0
		__.queueCountSchedule = 0
		__.queueCountAudit = 0
		__.queueCountScheduleAudit = 0
		__.queueCountAuditAudit = 0
		__.queueLastActivity = time.time()
		__.queueCountTimer = 0

		__.threadActivity = {}

		self.projectDataMaxLen = 2000
		self.projectDataDetected = False
		__.datadumps = 0
		__.projectData = {}
		__.pdID = {}
		__.saveInitiated = False

		self.listeningFor = False

	def add( self, name, func=False, arg=False, kwargs=False, focus=False , addID=True , trigger=False, triggerArg=False, triggerKwargs=False, loaded=False, timeout=False, database=False, pID=False ):
		# print('arg:',arg)
		# print( name, type( trigger ) )
		# sys.exit()
		nextID = False
		global appInfo
		self.lastActivity = time.time()

		if type(focus) == bool:
			focus = __.appReg
		try:
			self.records[focus]['threads']
			self.records[focus]['names'][name]['loaded'] = loaded
		except Exception as e:

			try:
				__.projectData[focus]
			except Exception as e:
				__.projectData[focus] = {}

			__.projectData[focus][name] = {}
			# if not 'folder' in name:
			#     print( 'zero' )
			#     sys.exit()

			__.projectData[focus][name][0] = {}
			__.projectData[focus][name][0]['saveInitiated'] = False
			# print( 'check3:', focus, name, 0 )
			__.projectData[focus][name][0]['data'] = []

			__.projectData[focus][name][1] = {}
			__.projectData[focus][name][1]['saveInitiated'] = False
			# print( 'check4:', focus, name, 1 )
			__.projectData[focus][name][1]['data'] = []

			try:
				__.pdID[focus]
			except Exception as e:
				__.pdID = {}
				__.pdID[focus] = {}


			__.pdID[focus][name] = 0

			if self.maxThreadsAuto:
				maxThreads = self.maxThreadsSafe
			else:
				maxThreads = self.maxThreads
			try:
				self.records[focus]['names'][name] = {
														'timeout': timeout,
														'loaded': loaded,
														'trigger': trigger,
														'maxThreads': maxThreads,
														'failure': 0,
														'changes': 0,
														'watch': 0,
														'closed': 0,
														'database': database,
														'executed': False,
														'projectSaveInitiated': False,
													}
			except Exception as e:
				self.records[focus] = {
											'threads': [],
											'open': 0,
											'app': appInfo[focus]['file'],
											'names': {
													name: {
														'timeout': timeout,
														'loaded': loaded,
														'trigger': trigger,
														'maxThreads': maxThreads,
														'failure': 0,
														'changes': 0,
														'watch': 0,
														'closed': 0,
														'database': database,
														'executed': False,
														'projectSaveInitiated': False,
													}
											}
				}

		self.isLoaded = False
		self.records[focus]['names'][name]['loaded'] = loaded
		if not self.auditAutoAdjust:
			# print(focus,name)
			if self.maxThreadsAuto:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreadsSafe
			else:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreads


		if not loaded:
			self.records[focus]['names'][name]['loaded'] = False

		if not type(trigger) == bool:
			self.records[focus]['names'][name]['trigger'] = trigger
			if not type(triggerArg) == bool:
				self.records[focus]['names'][name]['triggerArg'] = triggerArg
			else:
				self.records[focus]['names'][name]['triggerArg'] = False

		if not type(func) == bool:
			self.table['focus'].append(focus)
			# self.table['name'].append(name)
			nextID = self.nextID
			self.records[focus]['threads'].append( Threads( name, func, arg, kwargs, focus, nextID, addID, pID=pID ) )

			shouldOpen = False
			if not self.records[focus]['names'][name]['maxThreads']:
				shouldOpen = True
			elif self.opened > self.records[focus]['names'][name]['maxThreads']:
				shouldOpen = True
			if not shouldOpen:
				self.notstarted += 1
			else:
				pass
				# self.records[focus]['threads'][nextID].open()
				# self.cnt( focus, True )
			self.nextID += 1
			if not self.schedulerInitialized and True:
				self.schedulerInitialized = True
				threadTimer( self.scheduleLoop, threadSchedule )
				# Timer( self.scheduleLoop, threadSchedule ).start()

		if not self.auditInitialized and self.maxThreadsAuto:
			self.auditInitialized = True
			threadTimer( self.auditLoop, threadAudit )
			# Timer( .3, threadAudit ).start()

		return nextID
	def loaded( self, name=False , focus=False ):
		self.isLoaded = True
		if type(focus) == bool:
			focus = __.appReg
		if not type(name) == bool:
			self.records[focus]['names'][name]['loaded'] = True
			# name = str(list(self.records[focus]['names'].keys())[0])
		else:
			for f in self.records.keys():
				for n in self.records[f]['names'].keys():
					if not self.records[f]['names'][n]['loaded']:
						self.records[f]['names'][n]['loaded'] = True

	def spent( self, qID, mem=0, data=False, trigger=False, triggerArg=False, kwargs=False, lines=0 ):
		qID = int(qID)
		focus = False
		result = False
		for i,t in enumerate(self.records[self.table['focus'][qID]]['threads']):
			if self.records[self.table['focus'][qID]]['threads'][i].qID == qID:
				result = self.records[self.table['focus'][qID]]['threads'][i].close( mem, data, trigger, triggerArg, kwargs, lines )
				focus = self.table['focus'][qID]
				name = self.records[self.table['focus'][qID]]['threads'][i].name
		if not type(focus) == bool:
			self.cnt( focus, False )

			if self.records[focus]['open'] == 0 and self.isEverythingLoaded() and self.notstarted == 0:
				self.spendFocus( name, focus )
				self.printReport()
		return result
	def printReport( self ):
		if not self.reportPrinted:
			self.completionTime = time.time() - self.created
			if self.report:
				self.reportPrinted = True
				print('__________________________________________')
				print()
				print('opened:',self.opened)
				# print('records open:',self.records[focus]['open'])
				print('isEverythingLoaded:',time.time()-self.loadedBy,time.time()-self.lastActivity)
				print('spendFocus')
				print('queueCountSchedule:',__.queueCountSchedule)
				print('queueCountAudit:',__.queueCountAudit)
				print('audit:',__.queueCountAudit)
				print()
				print('load time:\t', int(self.loadTime))
				print('time after load:\t', int(time.time()-self.loadedBy))
				print()
				print('app time:\t', int(self.completionTime))
				print()
				print('maxInQueue:',self.maxInQueue)
				# str((self.completionTime/1000)%60)
				print()
				print('timeouts:',self.timeoutCount())
				# print("Average of the list =", round(average, 2)) 
				print()
				print('__________________________________________')
			elif self.statusTotal > 0:
				cTime = round(self.completionTime,2)
				if cTime > 60:
					ncTime = str(round((self.completionTime/60),2)) + ' min'
				else:
					ncTime = str(round(self.completionTime,2)) + ' sec'
				print('App time: ' + str(ncTime), end='\r', flush=True)
				# sys.stdout.flush()

	def spendFocus( self, name, focus ):
		# print( 'HERE: 0' )
		self.saveData()
		# print( 'HERE: 1' )

		if not self.records[focus]['names'][name]['executed']:
			# print( '\tnot executed', type( self.records[focus]['names'][name]['trigger'] ) )
			if not type( self.records[focus]['names'][name]['trigger'] ) == bool:
				if not type( self.records[focus]['names'][name]['triggerArg'] ) == bool:
					# Timer(.0001, self.records[focus]['names'][name]['trigger'], self.records[focus]['names'][name]['triggerArg']).start()
					# print( '\trunning 0' )
					self.records[focus]['names'][name]['trigger'](**self.records[focus]['names'][name]['triggerArg'])

				else:
					# print( '\trunning 1' )
					self.records[focus]['names'][name]['trigger']()
			self.records[focus]['names'][name]['executed'] = True
		# print( 'HERE: 2' )


	def log( self, name=False, focus=False ):
		if type(focus) == bool:
			focus = __.appReg
		log = []
		if not type(name) == bool:
			for i,t in enumerate(self.records[focus]['threads']):
				if self.records[focus]['threads'][i].name == name:
					log.append(self.records[focus]['threads'][i].getLog())
		else:
			for i,t in enumerate(self.records[focus]['threads']):
				for n in self.records[focus]['names']:
					if self.records[focus]['threads'][i].name == n:
						log.append(self.records[focus]['threads'][i].getLog())

		for f in self.records:
			self.records[f]['threads'] = False
			for n in self.records[f]['names']:
				if not type(self.records[f]['names'][n]['trigger']) == bool:
					self.records[f]['names'][n]['trigger'] = True




		return {
					'created': self.created,
					'loadedby': self.loadedBy,
					'loadtime': self.loadTime,
					'lastactivity': self.lastActivity,
					'completiontime': self.completionTime,
					'nextid': self.nextID,
					'maxinqueue': self.maxInQueue,
					'totaltask': __.totalTask,
					'records': self.records,
					'maxthreadssafe': self.maxThreadsSafe,
					'projectdatamaxlen': self.projectDataMaxLen,
					'datadumps': __.datadumps,
					'appstructure': __.structure(),
					'threadlog': log
		}

	def cnt( self, focus, up ):
		# self.maxThreadsSafe
		# self.maxThreads
		if up:
			if self.opened > self.maxInQueue:
				self.maxInQueue = self.opened
			self.lastActivity = time.time()
			self.records[focus]['open'] += 1
			self.opened += 1
			__.queueCount += 1
		else:
			self.closed += 1
			self.records[focus]['open'] -= 1
			self.opened -= 1
			__.queueCount -= 1

	def schedule( self ):
		__.queueCountSchedule += 1
		__.queueCountScheduleAudit -= 1

		if self.opened > self.maxThreads and self.notstarted > 0:
			pass
			# Timer( self.scheduleLoop, threadSchedule ).start()
		else:

			i = 0 
			while self.opened < self.maxThreads and i < self.notstarted:
				chosen = self.nextInQueue()
				if type(chosen) == bool:
						return False
				else:
					self.records[chosen['focus']]['threads'][chosen['qID']].open()
					self.notstarted -= 1
					self.cnt( chosen['focus'], True )
					i += 1

		if self.notstarted > 0:
			Timer( self.scheduleLoop, threadSchedule ).start()



	def nextInQueue( self ):
		chosen = False
		try:
			for key in self.records.keys():
				for i,q in enumerate(self.records[key]['threads']):
					if not self.records[key]['threads'][i].active:
						chosen = { 'focus': key, 'qID': self.records[key]['threads'][i].qID }
			if type(chosen) == bool:
				# print('active:',self.checkActive())
				return False
		except Exception as e:
			chosen = False
		return chosen

	def checkActive( self ):
		active = 0
		for key in self.records.keys():
			for i,q in enumerate(self.records[key]['threads']):
				if not self.records[key]['threads'][i].active:
					active += 1
		return active

	def isEverythingLoaded( self ):
		loaded = True
		shouldRun = True
		if self.loadedBy > 0:
			if self.loadedBy > self.lastActivity:
				shouldRun = False
		
		if shouldRun:
			for f in self.records.keys():
				for n in self.records[f]['names'].keys():
					if not self.records[f]['names'][n]['loaded']:
						loaded = False
			if loaded:
				self.loadedBy = time.time()
				self.loadTime = self.loadedBy - self.created
				self.isLoaded = True
		return loaded





	def getRuntimeMemoryFocus( self, focus ):
		runtime = []
		memory = []
		runtimeMemory = []
		for i,q in enumerate(self.records[focus]['threads']):
			if not self.records[key]['threads'][i].status:
				run = self.records[focus]['threads'][i].log['runtime']
				mem = self.records[focus]['threads'][i].log['mem']
				runtime.append( run )
				memory.append( mem )
				runtimeMemory.append({ 'runtime': run, 'mem': mem })

		return { 'runtime': runtime, 'mem': memory, 'runmem': runtimeMemory, 'averagemem': self.calcAverage(memory), 'averageruntime': self.calcAverage(runtime)  }

	def getRuntimeMemoryNameFocus( self, name, focus ):
		runtime = []
		runtimebottom = []
		memory = []
		runtimeMemory = []
		self.numberClosed()
		if self.records[focus]['names'][name]['closed'] < 5:
			return False

		for i,q in enumerate(self.records[focus]['threads']):
			if not self.records[focus]['threads'][i].status and self.records[focus]['threads'][i].name == name:
				run = self.records[focus]['threads'][i].log['runtime']
				mem = self.records[focus]['threads'][i].log['mem']
				runtime.append( run )
				memory.append( mem )
				runtimeMemory.append({ 'runtime': run, 'mem': mem })
			if not self.records[focus]['threads'][i].status and self.records[focus]['threads'][i].name == name and not self.records[focus]['threads'][i].bottom:
				self.records[focus]['threads'][i].bottom = True
				runtimebottom.append( run )

			if len(runtime) == 0 or len(memory) == 0 or len(runtimebottom) == 0 :
				return False

		try:

			data = {
					'runtime': runtime,
					'runtimebottom': runtimebottom,
					'mem': memory,
					'runmem': runtimeMemory,
					'averagemem': self.calcAverage(memory),
					'averageruntime': self.calcAverage(runtime)
		}

		except Exception as e:
			data = False
			# print(memory)

		return data

	def getRuntimeMemoryReport( self ):
		self.runtime = []
		self.mem = []
		self.runtimeMemory = []
		self.averagemem = 0
		self.averageruntime = 0
		for key in self.records.keys():
			for i,q in enumerate(self.records[key]['threads']):
				if not self.records[key]['threads'][i].status:
					run = self.records[key]['threads'][i].log['runtime']
					mem = self.records[key]['threads'][i].log['mem']

					self.runtime.append( run )
					self.mem.append( mem )
					self.runtimeMemory.append({ 'runtime': runtime, 'mem': mem })

		self.averagemem = self.calcAverage(mem)
		self.averageruntime = self.calcAverage(runtime)
		return { 'runtime': runtime, 'mem': mem, 'runmem': self.runtimeMemory, 'averagemem': self.averagemem, 'averageruntime': self.averageruntime }


	def calcAverage( data ):
		return round(data, 2)

	def saveData( self ):

		for focus in __.projectData:
			try:
				del __.projectData[focus][0]
			except Exception as e:
				pass
			for name in __.projectData[focus].keys():
				logName = 'auto_' + self.records[focus]['app'] + '_' + name + '_' + str(self.created)
				for pdID in __.projectData[focus][name].keys():
					if len(__.projectData[focus][name][pdID]['data']):
						__.datadumps += 1
						if type(self.records[focus]['names'][name]['database']) == bool:
							if len(__.projectData[focus][name][pdID]['data']) > 0:
								
								saveTableSplitNew( __.projectData[focus][name][pdID]['data'], logName, project=True )
								print( 'check0:', focus, name, pdID )
								if not 'folder' in name:
									print( 'zero' )
									sys.exit()
								__.projectData[focus][name][pdID]['data'] = []
						else:
							print()
							print('Data saved to:',self.records[focus]['names'][name]['database'])
							print()


							if len(__.projectData[focus][name][pdID]['data']) > 0:
								try:
									conn = sqlite3.connect(self.records[focus]['names'][name]['database'])
									cursor = conn.cursor()
									errors = []
									for sql in __.projectData[focus][name][pdID]['data']:
										try:
											cursor.execute( sql )
										except Exception as e:
											errors.append( sql )
									conn.commit()
									conn.close()
									if len(errors) > 0:
										saveTableSplitNew( errors, logName+'__ERRORS__', project=True )
								except Exception as e:
									saveTableSplitNew( __.projectData[focus][name][pdID]['data'], logName, project=True )
									print( 'check1:', focus, name, pdID )
								if not 'folder' in name:
									print( 'zero' )
									sys.exit()
								__.projectData[focus][name][pdID]['data'] = []



					



	def manageData( self ):
		self.data = {}
		self.data[0] = 0
		self.data[1] = 0
		for focus in __.projectData:
			# print( 'focus:', focus )
			try:
				del __.projectData[focus][0]
			except Exception as e:
				pass
			for name in __.projectData[focus].keys():
				logName = 'auto_' + self.records[focus]['app'] + '_' + name + '_' + str(self.created)
				for pdID in __.projectData[focus][name].keys():
					if not type(__.projectData[focus][name][pdID]['saveInitiated']) == bool:
						# print('saveInitiated:',__.projectData[focus][name][pdID]['saveInitiated'])
						# print()
						# print(len( __.projectData[focus][name][ __.projectData[focus][name][pdID]['saveInitiated']['pdID'] ]['data'] ), __.projectData[focus][name][pdID]['saveInitiated']['size'] )
						# print()
						if len( __.projectData[focus][name][ __.projectData[focus][name][pdID]['saveInitiated']['pdID'] ]['data'] ) > __.projectData[focus][name][pdID]['saveInitiated']['size']:
							__.projectData[focus][name][pdID]['saveInitiated']['timeSizeChange'] = time.time()
						else:
							# print()
							# print('got here')
							# print()

							diff = time.time() - __.projectData[focus][name][pdID]['saveInitiated']['timestamp']
							print()
							# print()
							# print('diff:',diff)
							# print()
							print( 'diff:', diff )
							print( __.projectData[focus][name][pdID]['saveInitiated']['size'], len(__.projectData[focus][name][  __.projectData[focus][name][pdID]['saveInitiated']['pdID']  ]['data']))
							if diff > __.projectData[focus][name][pdID]['saveInitiated']['startAfterNoChangeFor']:
								__.datadumps += 1
								if type(self.records[focus]['names'][name]['database']) == bool:
									tmpData = __.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data']
									print( 'save started' )
									saveTableSplitNew( tmpData, __.projectData[focus][name][pdID]['saveInitiated']['logname'], project=True )
									tmpData = []
									print( 'post split save:', len(__.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data']) )
									__.projectData[__.projectData[focus][name][pdID]['saveInitiated']['focus']][__.projectData[focus][name][pdID]['saveInitiated']['pdID']] = []
									if not 'folder' in name:
										print( 'zero' )
										sys.exit()
									__.projectData[focus][name][pdID]['saveInitiated'] = False
									threadTimer( .5, enableThreadDataSwap )
							
								else:
									print()
									print('Data saved to:',self.records[focus]['names'][name]['database'])
									print()
									# try:
									conn = sqlite3.connect(self.records[focus]['names'][name]['database'])
									cursor = conn.cursor()
									errors = []
									for sql in __.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data']:
										try:
											cursor.execute( sql )
										except Exception as e:
											errors.append( sql )
									conn.commit()
									conn.close()
									if len(errors) > 0:
										saveTableSplitNew( errors, logName+'__ERRORS__', project=True )
									# except Exception as e:
									#     saveTableSplitNew( __.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data'], __.projectData[focus][name][pdID]['saveInitiated']['logname'], project=True )
									



									# __.projectData[focus][name][  __.projectData[focus][name][pdID]['saveInitiated']['pdID']  ]['data'] = []
									if not 'folder' in name:
										print( 'zero' )
										sys.exit()
									__.projectData[focus][name][pdID]['saveInitiated'] = False
									threadTimer( .5, enableThreadDataSwap )



									

		tmpData = []

		if not __.saveInitiated:
			for focus in __.projectData:
				try:
					del __.projectData[focus][0]
				except Exception as e:
					pass
				for name in __.projectData[focus].keys():
					for pdID in __.projectData[focus][name].keys():
						# print('data len:',len(__.projectData[focus][name][pdID]['data']))
						# print('projectDataMaxLen:',self.projectDataMaxLen)
						if len(__.projectData[focus][name][pdID]['data']):
							self.projectDataDetected = True

							# print()
							# print( len(__.projectData[focus][name][pdID]['data']), self.projectDataMaxLen )
							# print()

							if len(__.projectData[focus][name][pdID]['data']) >= self.projectDataMaxLen:
								
								if __.pdID[focus][name] == 0:
									__.pdID[focus][name] = 1
									print( 'NOW: 1' )
								else:
									__.pdID[focus][name] = 0
									print( 'NOW: 0' )
								
								logname = 'auto_' + self.records[focus]['app'] + '_' + str(self.created)
								__.saveInitiated = True

								__.processing = [ focus, name, pdID ]

								__.projectData[focus][name][pdID]['saveInitiated'] = {
															'logname': logname,
															'pdID': pdID,
															'focus': focus,
															'timestamp': time.time(),
															'size': len(__.projectData[focus][name][pdID]['data']),
															'startAfterNoChangeFor': 3,
															'timeSizeChange': 0,

								}


			# self.timeout = False
			# self.timeoutAsk = False
			


	def listen( self, qID, trigger=False, triggerArg=False, kwargs=False, data=False  ):
		try:
			self.listeningFor['active']
		except Exception as e:
			self.listeningFor = []
		self.listeningFor.append( { 'active': True, 'qID': qID, 'trigger': trigger, 'triggerArg': triggerArg, 'kwargs': kwargs, 'data': data } )

	def listener( self ):
		for li,listen in enumerate(self.listeningFor):
			if self.listeningFor[li]['active']:
				for focus in self.records.keys():
					for i,q in enumerate(self.records[focus]['threads']):
						if self.records[focus]['threads'][i].qID == listen['qID'] and not self.records[focus]['threads'][i].status:
							thisData0 = self.records[focus]['threads'][i].data
							thisData1 = self.listeningFor[li]['data']
							thisData = False
							if sys.getsizeof(thisData0) > sys.getsizeof(thisData1):
								thisData = thisData0
							elif sys.getsizeof(thisData0) < sys.getsizeof(thisData1):
								thisData = thisData1
							self.listeningFor[li]['data'] = False
							self.listeningFor[li]['active'] = False
							self.records[focus]['threads'][i].data = False
							self.listenActivated( self.listeningFor[li]['trigger'], self.listeningFor[li]['triggerArg'], self.listeningFor[li]['kwargs'], thisData )


	def listenActivated( self, trigger=False, triggerArg=False, kwargs=False, data=False  ):

		__.queueLastActivity = time.time()
		if not type(trigger) == bool:
			try:
				triggerName = trigger.__name__
			except Exception as e:
				triggerName = ''

			try:

				if type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger )
				elif not type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger, [data] )
				elif type(data) == bool and not type(triggerArg) == bool:
					threadTimer( .0001, trigger, triggerArg )
				elif not type(data) == bool and not type(triggerArg) == bool and kwargs:
					args = [{ 'func': trigger, 'args': triggerArg }]
					try:
						args[0]['args'][0]['data'] = data
					except Exception as e:
						args[0]['args']['data'] = data

					
					# print(args)
					threadTimer( .0001, threadKwargs, args )
				elif not type(data) == bool and not type(triggerArg) == bool and not kwargs:
					try:
						triggerArg.append(data)
						threadTimer( .0001, threadKwargs, triggerArg )
					except Exception as e:
						try:
							triggerArg[0].append(data)
							threadTimer( .0001, threadKwargs, triggerArg )
						except Exception as e:
							print('listener trigger error')


			except Exception as e:
				print('listener trigger error')


	def printStatus( self ):
		pDone = str(int(percentageDiffInt(self.closed, self.statusTotal)))
		if not type( self.prefix ) == bool:
			print(' ' + self.prefix + ':', pDone + '%' , end='\r')
		else:
			print(' ' + pDone + '%' , end='\r')
		sys.stdout.flush()

	def timeoutCount( self ):
		cnt = 0
		for focus in self.records.keys():
			for i,q in enumerate(self.records[focus]['threads']):

				if self.records[focus]['threads'][i].timeout:
					cnt += 1
		return cnt

				

	def checkTimeout( self ):
		
		if not type( self.timeout ) == bool:
			for focus in self.records.keys():
				for i,q in enumerate(self.records[focus]['threads']):
					if self.records[focus]['threads'][i].status:
						diff = time.time() - self.records[focus]['threads'][i].created
						if diff > self.timeout:
							self.records[focus]['threads'][i].timeout = True
							__.threadQueue[  self.records[focus]['threads'][i].qID  ]._stop()

		for focus in self.records.keys():
			for name in self.records[focus]['names'].keys():
				if not type( self.records[focus]['names'][name]['timeout'] ) == bool:
					for i,q in enumerate(self.records[focus]['threads']):
						if name == self.records[focus]['threads'][i].name:
							if self.records[focus]['threads'][i].status:
								diff = time.time() - self.records[focus]['threads'][i].created
								if diff > self.records[focus]['names'][name]['timeout']:
									self.records[focus]['threads'][i].timeout = True
									__.threadQueue[  self.records[focus]['threads'][i].qID  ]._stop()
							

		
	def audit( self ):
		if not type(self.listeningFor) == bool:
			self.listener()
		self.schedule()
		self.checkTimeout()
		self.isEverythingLoaded()
		__.queueCountAudit += 1
		__.queueCountAuditAudit -= 1
		self.numberClosed()
		if not self.isLoaded:
			if self.autoLoaded:

				diff2 = int(time.time() - __.queueLastActivity)
				diff = int(time.time() - self.lastActivity)
				if diff > self.autoLoadedAfter:
					if diff2 > self.autoLoadedAfter:
						if self.auditPrint:
							print('Auto Loaded:', diff)
						self.loaded()
						self.numberClosed()


		self.manageData()



		if self.auditPrint:
			if self.projectDataDetected:

				if False:
					print()
					print()
					print('Opened:',self.opened,'\tClosed:',self.totalClosed,'\tClosed 2:',self.closed,'\tTotal:',self.nextID,'\tMax in queue:',self.maxInQueue,'\tTotal Task:',__.totalTask,'\tTotal Audit:',__.queueCountScheduleAudit+__.queueCountSchedule )
					print()
				for focus in __.projectData:
					try:
						del __.projectData[focus][0]
					except Exception as e:
						pass
					for name in __.projectData[focus].keys():
						print( 'pre:', focus, name, __.projectData[focus].keys() )
						print( '0:', len(__.projectData[focus][name][0]['data']), focus, name )
						print( '1:', len(__.projectData[focus][name][1]['data']), focus, name )
						if len(__.projectData[focus][name][0]['data']) or len(__.projectData[focus][name][1]['data']):
							if False:
								print('Name:',name, '\tProject 0 Length:', len(__.projectData[focus][name][0]['data']), '\tProject 1 Length:', len(__.projectData[focus][name][1]['data']),'\tdb:',self.records[focus]['names'][name]['database'] )
							if True:
								print('Name:',name, '\tOpened:',self.opened,'\tClosed:',self.totalClosed,'\tClosed 2:',self.closed,'\tTotal:',self.nextID,'\tMax in queue:',self.maxInQueue,'\tTotal Task:',__.totalTask, '\tProject 0 Length:', len(__.projectData[focus][name][0]['data']), '\tProject 1 Length:', len(__.projectData[focus][name][1]['data']),'\tdb:',self.records[focus]['names'][name]['database'] )
			else:
				print('Opened:',self.opened,'\tClosed:',self.totalClosed,'\tClosed 2:',self.closed,'\tTotal:',self.nextID,'\tMax in queue:',self.maxInQueue,'\tTotal Task:',__.totalTask,'\tTotal Audit:',__.queueCountScheduleAudit+__.queueCountSchedule )
			# print( self.opened, self.isLoaded, self.notstarted )
			if False:
				print()
				print( self.opened, self.isLoaded, self.notstarted )
				print()

		elif self.statusTotal > 0:
			self.printStatus()

		pass
		if self.opened == 0 and self.isLoaded and self.notstarted <= 0:
			if self.auditPrint:
				print('audit:',__.queueCountAudit)
			self.printReport()
			self.saveData()
			if self.saveLog:
				threadTimer( 1, saveThreadsLog )

			for f in self.records.keys():
				for n in self.records[f]['names'].keys():
					self.spendFocus( n, f )


		else:
			diff = self.nextID - self.opened

			if diff < 5:
				threadTimer( self.auditLoop, threadAudit )
				# Timer( .5, threadAudit ).start()
			else:
				for f in self.records.keys():
					for n in self.records[f]['names'].keys():

						data = self.getRuntimeMemoryNameFocusTopBottom( n, f )
						if type(data) == bool:
							threadTimer( self.auditLoop, threadAudit )
							# Timer( .5, threadAudit ).start()
							return False
						else:
							diff = percentageDiffInt(data['top'], data['bottom'])
							diff2 = percentageDiffInt(data['top'], data['freshbottom'])

							if diff < self.auditPercentChangeMax or diff2 < self.auditPercentChangeMax:
								self.records[f]['names'][n]['failure'] = 0
								self.records[f]['names'][n]['changes'] = 0
								self.records[f]['names'][n]['watch'] = 0
								shouldAct = False
							else:
								if not self.records[f]['names'][n]['watch'] >= self.auditWatchMax:
									self.records[f]['names'][n]['watch'] += 1
								else:
									self.records[f]['names'][n]['failure'] += 1
									self.records[f]['names'][n]['changes'] += 1
								shouldAct = True

							if shouldAct:
								
								if self.records[f]['names'][n]['failure'] >= self.auditMaxFailuresBeforeAction:
									lastMax = self.records[f]['names'][n]['maxThreads']
									if self.records[f]['names'][n]['changes'] >= self.auditPercentDrasticThreshold:
										changeBy = self.auditPercentReduceByDrastic
									else:
										changeBy = self.auditPercentReduceBy

									newMax = percentageInt(self.opened, changeBy)

									if newMax < self.minThreads:
										newMax = self.minThreads
									if newMax > self.maxThreadsSafe:
										newMax = self.maxThreadsSafe
									self.auditAutoAdjust = True
									self.records[f]['names'][n]['maxThreads'] = newMax
									print('_________________________________________')
									print()
									print('Changed max threads from:', lastMax,'to:',newMax)

				threadTimer( self.auditLoop, threadAudit )
				# Timer( .5, threadAudit ).start()
	# self.auditWatchMax

# watch

#                             if self.records[f]['names'][n]['maxThreads'] == 0:
#                                 newMax = self.opened
#                         percentageInt(percent, whole)
#                         if not self.records[f]['names'][n]['loaded']:
#                             self.records[f]['names'][n]['maxThreads'] = True

#                             self.records[f]['names'][n]['maxThreads'] = 


#         self.auditPercentReduceByOverMax = 15        self.maxThreads = 1000
#         self.auditPercentReduceByOverMaxBy = 30


# self.auditPercentReduceByDrastic
#         self.auditPercentChangeMin = 10
#         self. = 5

#         self.auditPercentChangeMin = 10
#         self.auditPercentReduceBy = 5

# self.records[focus]['names'][name]['maxThreads']
# self.auditPercentChangeMax
#             __.queueCountAudit += 1
#             Timer( .5, threadSchedule ).start()

# threadTimer
# thread = Timer( .0001, threadKwargs, data ).start()
# thread = Timer( .0001, threadKwargs, data ).start()
# thread = Timer( .0001, self.func, self.argID ).start()
# thread = Timer( .0001, self.func, self.arg ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( .3, threadAudit ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( .5, threadAudit ).start()
# Timer( .5, threadAudit ).start()
# Timer( .5, threadAudit ).start()


# __.queueCountScheduleAudit = 0
# __.queueCountAuditAudit = 0


	def numberClosed( self ):
		self.isEverythingLoaded()
		totalClosed = 0
		for f in self.records.keys():
			for i,t in enumerate(self.records[f]['threads']):
				for n in self.records[f]['names'].keys():
					if not self.records[f]['threads'][i].name == n:
						self.records[f]['names'][n]['closed'] = 0 


		info = {}
		for f in self.records.keys():
			for i,t in enumerate(self.records[f]['threads']):
				if not self.records[f]['threads'][i].status:
					for n in self.records[f]['names'].keys():
						if self.records[f]['threads'][i].name == n:
							try:
								info[n]['total'] += 1
								info[n]['closed'] += 1
							except Exception as e:
								info[n] = {}
								info[n]['total'] = 0
								info[n]['closed'] = 0
								info[n]['total'] += 1
								info[n]['closed'] += 1
							if not self.records[f]['threads'][i].status:
								self.records[f]['names'][n]['closed'] += 1
								totalClosed += 1
						# if info[n]['total'] == info[n]['closed'] and info[n]['total'] > 0 and self.opened == 0 and self.isEverythingLoaded() and self.notstarted == 0:
							if self.opened == 0 and self.isLoaded and self.notstarted == 0:
								if not type( self.records[f]['names'][n]['trigger'] ) == bool:
									self.spendFocus( n, f )
								

		self.totalClosed = totalClosed





	def getRuntimeMemoryNameFocusTopBottom( self, name, focus ):
		topruntime = []
		bottomruntime = []
		bottomruntimeFresh = []
		
		length = len(self.records[focus]['threads'])
		sampleSize = percentageInt( self.auditPercentSample, length )
		bottom = length - sampleSize
		data = self.getRuntimeMemoryNameFocus( name, focus )
		if type(data) == bool:
			return False
		if len(data['runtimebottom']) < 5:
			return False
		else:

			for i,row in enumerate(data['runtime']):
				if i <= sampleSize:
					topruntime.append(row)
				if i >= bottom:
					bottomruntime.append(row)
			for i,row in enumerate(data['runtimebottom']):
					bottomruntimeFresh.append(row)

			topaverageruntime = self.calcAverage(topruntime)
			bottomaverageruntime = self.calcAverage(bottomruntime)
			freshbottomaverageruntime = self.calcAverage(bottomruntimeFresh)

			return { 'top': topaverageruntime, 'bottom': bottomaverageruntime, 'freshbottom': freshbottomaverageruntime }


	def getRuntimeMemoryFocusTopBottom( self, focus ):
		topruntime = []
		bottomruntime = []
		
		length = len(self.records[focus]['threads'])
		sampleSize = percentageInt( self.auditPercentSample, length )
		bottom = length - sampleSize
		data = self.getRuntimeMemoryFocus( focus )

		for i,row in enumerate(data['runtime']):
			if i <= sampleSize:
				topruntime.append(row)
			if i >= bottom:
				bottomruntime.append(row)

		topaverageruntime = self.calcAverage(topruntime)
		bottomaverageruntime = self.calcAverage(bottomruntime)

		return { 'top': topaverageruntime, 'bottom': bottomaverageruntime }




def enableThreadDataSwap():
	print( 'key test00:', __.projectData[ __.processing[0] ].keys() )
	print( 'enableThreadDataSwap: initiated' )
	# print( __.processing )
	print( 'post process size:', len(__.projectData[ __.processing[0] ][ __.processing[1] ][   __.processing[2]   ]['data']) )
	__.saveInitiated = False
	
	# __.projectData[focus][name][0]['data'] = []
	print( 'key test0:', __.projectData[ __.processing[0] ].keys() )
	# __.projectData[ __.processing[0] ][ __.processing[1] ][   __.processing[2]   ]['data'] = []
	# __.projectData[ '__main__' ][ 'folder' ][   __.processing[2]   ]['data'] = []
	print( 'key test1:', __.projectData[ __.processing[0] ].keys() )

# def hasTimedOut():
#     print( 'hasTimedOut' )

# @timeout( 10, hasTimedOut() )
def threadTimer( tim, func, args=False, qID=False ):
	__.totalTask += 1
	# print(func.__name__)
	shouldRun = True
	if func.__name__ == 'threadSchedule':
		if __.queueCountScheduleAudit > 4:
			shouldRun = False
		else:
			__.queueCountScheduleAudit += 1

	if func.__name__ == 'threadAudit':
		if __.queueCountAuditAudit > 4:
			shouldRun = False
		else:
			__.queueCountAuditAudit += 1

	if shouldRun:
		if tim < .01:
			tim = .01

		try:
			if type(args) == bool:
				if not type(qID) == bool:
					__.threadQueue[qID] = Timer( tim, func )
					__.threadQueue[qID].start()
				else:
					Timer( tim, func ).start()
			else:
				if not type(qID) == bool:
					__.threadQueue[qID] = Timer( tim, func, args )
					__.threadQueue[qID].start()
				else:
					Timer( tim, func, args ).start()
			__.queueCountTimer += 1
			# https://stackoverflow.com/questions/34562473/most-pythonic-way-to-kill-a-thread-after-some-period-of-time
			# __.threadQueue[qID].join(30)
			# if __.threadQueue[qID].is_alive():
			#     print( 'Has Timed Out' )
			#     e.set()
			# else:
			#     pass
		except Exception as e:
			print('Thread Error:',__.queueCountTimer)


def threadAudit():
	global threads
	threads.audit()

def threadSchedule():
	global threads
	threads.schedule()

def threadKwargs( data=False ):
	# print(data)
	try:
		data['func'](**data['args'][0])
	except Exception as e:
		try:
			data[0]['func'](**data['args'][0])
		except Exception as e:
			print('Error: kwargs')






def percentageInt( percent, whole, isFloat=False ):
	# return int((percent * whole) / 100.0)
	if not isFloat:
		return int(round( (percent * whole) / 100.0 , 0))
	else:
		return round( (percent * whole) / 100.0 , 1)

def percentageDiffInt( smaller, bigger, isFloat=False ):
	# return int((smaller/bigger)*100)
	if not isFloat:
		return int(round((smaller/bigger)*100, 0))
	else:
		return round((smaller/bigger)*100, 1)

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






###################################################################################################################
def loadingGraphic():
	# return False
	import tkinter as tk
	from PIL import Image, ImageTk
	from itertools import count, cycle

	global theLoadingGraphic

	class ImageLabel(tk.Label):
		"""
		A Label that displays images, and plays them if they are gifs

		:im: A PIL Image instance or a string filename
		"""
		def load(self, im):
			if isinstance(im, str):
				im = Image.open(im)
			frames = []

			try:
				for i in count(1):
					frames.append(ImageTk.PhotoImage(im.copy()))
					im.seek(i)
			except EOFError:
				pass
			self.frames = cycle(frames)

			try:
				self.delay = im.info['duration']
			except:
				self.delay = 100

			if len(frames) == 1:
				self.config(image=next(self.frames))
			else:
				self.next_frame()

		def unload(self):
			self.config(image=None)
			self.frames = None

		def next_frame(self):
			if self.frames:
				self.config(image=next(self.frames))
				self.after(self.delay, self.next_frame)

	theLoadingGraphic = tk.Tk()
	theLoadingGraphic.wait_visibility(theLoadingGraphic)
	lbl = ImageLabel(theLoadingGraphic)
	lbl.pack()
	lbl.load( _v.dance )
	theLoadingGraphic.mainloop()

def loadingGraphicEnd():
	# return False
	global theLoadingGraphic
	print('got here 1')
	# theLoadingGraphic.destroy()
	# theLoadingGraphic.quit()
	print('got here 2')

###################################################################################################################

def isText( data ):
	if type( data ) == str:

		return True
	else:
		return False

def isNum( data ):
	if type( data ) == int:
		return True
	else:
		return False

def isFloat( data ):
	if type( data ) == float:
		return True
	else:
		return False

###################################################################################################################


class Field:

	def __init__( self, project, name, value, appReg, script ):
		self.appReg = appReg
		self.project = project
		self.name = name
		self.trigger = script
		self.maxField = 0

		self.registerValue( value )

	def setTrigger( self, script ):
		self.trigger = script

	def addPadding( self, value ):
		value = self.runTrigger( str(value) )
		addPadding = self.maxField - len( value )
		while not len(value) == self.maxField:
			value += ' '
		# for x in range(1,addPadding+1):
		#     value += ' '
		# return str(self.maxField)+' '+str(len( value ))+value
		return value

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
		self.fields = []


	def register( self, project, names, value='', appReg=False, script=False ):
		if type(appReg) == bool:
			appReg = __.appReg

		for name in names.split(','):

			shouldAdd = True
			for i,s in enumerate(self.fields):
				if self.fields[i].appReg == appReg and project == self.fields[i].project and name == self.fields[i].name:
					shouldAdd = False
			if shouldAdd:
				self.fields.append( Field( project, name, value, appReg, script ) )
			else:
				self.registerValue( project, name, value, appReg )

	def registerValue( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		
		result = False
		for i,s in enumerate(self.fields):
			if self.fields[i].appReg == appReg and project == self.fields[i].project and name == self.fields[i].name:
				self.fields[i].registerValue( value )
				result = True
		return result


	def value( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields):
			if self.fields[i].appReg == appReg and project == self.fields[i].project and name == self.fields[i].name:
				result = self.fields[i].addPadding( value )
		return result
	def valuez( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields):
			if self.fields[i].appReg == appReg and project == self.fields[i].project and name == self.fields[i].name:
				result = self.fields[i].addPaddingZeros( value )
		return result

	def asset( self, project, asset, appReg=False ):
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
			self.register( project, name, asset[name], appReg )

# _.fields.register( 'project', 'name', script=_.resolveEpochTest )
# _.fields.asset( 'project', {} )
# _.fields.asset( 'project', [{}] )
# _.fields.register( 'project', 'name', value, appReg=focus() )
# _.fields.register( 'project', 'name', value )
# _.fields.value( 'project', 'name', value )

###################################################################################################################




thisTest = 'hello'




errors = []
appInfo = {}
appData = {}

argvProcess = True

fields = Fields()

threads = Queue()
switches = Switches()
tables = Tables()
databases = Databases()
__.databases = Databases()


def appInfoDump():
	global appInfo
	for k in appInfo.keys():
		print()
		print(k,appInfo[k])



def appInfoDump2():
	global appInfo
	for k in appInfo.keys():
		print()
		print(k,appInfo[k])



# def appInfoDump2():
#     global appInfo
#     for k in appInfo.keys():
#         print(k,appInfo[k]['columns'])


def load():
	global switches
	global switchDefault
	# global tables
	switches.register('Help', '?,/?,-?,/h,help,/help,-help,--help')
	switches.register('Column', '-c,-column', 'size, name')
	switches.register('Sort','-s,-sort', 'Asc:type, Desc:ext')
	switches.register('Debug', '-d,-debug')
	switches.register('Errors', '-e,-Error,-Errors', '8,11 OR hide:8,11')
	switches.register('Timeout', '-t,-Timeout')
	switches.register('GroupBy', '-g,-group,-groupby', 'ext, month')
	switches.register('ShortenColumn', '-sc,-shortencolumn')
	switches.register('Long', '-l,-long')
	switches.register('Length', '-length','x3')
	switches.register('Report', '-report')
	switches.register('Plus', '+')
	switches.register('Minus', '-')
	switches.register('PlusOr', '-or')
	switches.register('PlusClose', '+close')
	switches.register('PrintAutoAbbreviations', ',-printa,-aprint')
	switches.register('LoadEpoch', '-loadepoch')
	switches.register('NoColor', '-nocolor')
	switchDefault = switches.length()





import importlib



regImps = {}



##############################

class regImp:

	def __init__( self, focus, app, argvProcessForce=False ):
		global regImps
		global appInfo

		regImps[focus] = {}

		# self.functions = autoKwargsGetArgsFromApp(app)

		self.app = app
		self.parent = focus

		self.imp = importlib.import_module(app)

		self.focus = self.imp.focus( parentApp=focus )
		self.focusPop = focus
		
		self.saveLog = True

		load()
		self.imp.registerSwitches( argvProcessForce=False)

		appInfo[self.imp.focus(focus)] = appInfo[self.imp.focus()]
		appData[self.imp.focus(focus)] = appData[self.imp.focus()]
		__.constructRegistration(appInfo[self.imp.focus(focus)]['file'],self.imp.focus(focus))

		regImps[focus] = {}
		regImps[focus][app] = self.imp

		__.appReg = self.focusPop

		# self.provideImport()

	def provideImport( self ):
		return self.imp

	def listFunctions( self ):
		self.functions
		for func in self.functions:
			print( func['name'], func['args'] )

	def pipe( self, data=[], xfer=False, clear=True, appReg=False ):
		global appData
		if type(data) == bool:
			return appData[self.focus]['pipe']

		if type(appReg) == bool:
			appReg = self.focusPop

		if not len( data ):
			if xfer:
				data = appData[appReg]['pipe']
				if clear:
					appData[appReg]['pipe'] = []

		appData[self.focus]['pipe'] = data

		try:
			appData[self.focus]['data']['table']['received']
			
			profile = _profile.records.audit( 'pipe', data, appReg=[appReg,self.focus] )
			appData[appReg]['data']['table']['sent'].append( profile )
			appData[self.focus]['data']['table']['received'].append( profile )
		except Exception as e:
			pass

	def switch( self, names, value=None, appReg=False ):
		global appData
		global switches

		if type(appReg) == bool:
			appReg = self.focusPop

		for name in names.split(','):
			if not value is None:
				try:
					appData[self.focus]['data']['field']['received']
					profile = _profile.records.audit( name, value, appReg=[appReg,self.focus] )
					appData[appReg]['data']['field']['sent'].append( profile )
					appData[self.focus]['data']['field']['received'].append( profile )
				except Exception as e:
					pass




			__.appReg = self.focus

			switches.fieldSet( name, 'active', True )

			# if not type ( value ) == bool:
			if not value is None:
				switches.fieldSet( name, 'value', value )
				if type( value ) == list:
					switches.fieldSet( name, 'values', value )
				else:
					switches.fieldSet( name, 'values', [value] )
		__.appReg = self.focusPop

	def deleteSwitch( self, name ):
		global switches
		__.appReg = self.focus

		switches.fieldSet( name, 'active', False )

		__.appReg = self.focusPop

	def action( self, focusPop=True ):
		__.appReg = self.focus

		result = self.imp.action()

		if focusPop:
			__.appReg = self.focusPop

		return result


	def do( self, func, arg=False, focusPop=True ):

		__.appReg = self.focus

		if type( func ) == str:
			theFunction = eval( 'self.imp.' + func )
		else:
			theFunction = func

		if type( arg ) == bool:
			result = theFunction()
		elif type( arg ) == dict:
			result = theFunction(**arg)
		elif type( arg ) == list:
			result = theFunction(*arg)

		

		if focusPop:
			__.appReg = self.focusPop

		return result

	def execute( self, func, arg=False, nofocus=False ):
		global threads
		theFunc = eval('self.imp.'+func)

		shouldRun = True
		if not nofocus and  type(arg) == bool:
			args = [ self.focus ]
		elif not nofocus and  not type(arg) == bool:
			args = [ arg, self.focus ]

		if nofocus and  type(arg) == bool:
			shouldRun = False
			theID = threads.add( 'execute', theFunc, loaded=True )
		elif nofocus and  not type(arg) == bool:
			args = [ arg ]


		if shouldRun:

			theID = threads.add( 'execute', theFunc, args, loaded=True )

		# if self.saveLog:
		# else:
		#     theID = threads.add( 'execute', theFunc, [ arg, self.focus ], trigger=saveThreadsLog, loaded=True )

		return theID

##############################
# _regImpEXAMPLE = _.regImp( focus(), '_rightThumb._auditCodeBase' )

# _regImpEXAMPLE.do( 'functionTest' )
# _regImpEXAMPLE.do( _codeX.imp.functionTest )
# _regImpEXAMPLE.do( 'functionTestKwargs', ['Scott','Alpha'] )
# _regImpEXAMPLE.do( 'functionTestKwargs', { 'one': 'Scott', 'two': 'Alpha' } )

# _regImpEXAMPLE.switch( 'Long' )
# _regImpEXAMPLE.switch( 'GroupBy', 'appreg' )

# _regImpEXAMPLE.imp.focus( focus() )
# _.switches.dumpSwitches()
# _regImpEXAMPLE.imp.action()
##############################
##############################
# txtBackup = _.regImp( __.appReg, 'txtBackup' )
# txtBackup = _.regImp( focus(), 'txtBackup' )
# txtBackup.switch( 'Silent' )
# txtBackup.switch( 'Input', 'appreg' )

# txtBackup.do( txtBackup.imp.action )
# txtBackup.do( 'action' )
# txtBackup.action()
##############################


def saveThreadsLog():
	global threads
	# log = threads.log('execute')
	saveLog( 'threads', printThis=False )





def autoKwargsGetArgsFromApp(app):
	if not '.py' in app:
		app = app + '.py'
	appText = getText(_v.myAppsPy + _v.slash + app)
	func = []
	for row in appText:
		if 'def ' in row:
			fr = row.split('def ')[1].replace(' ','')
			name = fr.split('(')[0]
			if name+'():' in fr:
				args = []
			else:
				tmp = fr.replace(name+'(','')
				arg = tmp.split('):')[0]
				args = []
				for x in arg.split(','):
					if '=' in x:
						args.append( { 'arg': x.split('=')[0], 'default': x.split('=')[1] } )
					else:
						args.append( { 'arg': x, 'default': '' } )


			func.append( { 'name': name, 'args': args } )
	return func





###############################################
####### imported into functions as needed
	# math
	# calendar
	# re
	# np
	# random

####### deleted
# glob
# subprocess
# join
# getsize
# splitext
# rrule
# ast
# OrderedDict
###############################################

### NOTES ###
	# types of timestamps:
	#                         1522705321.1137724        file create, modification
	#                         1517338060740            int(round(time.time() * 1000))
	


# _.regImps( focus(), 'app' )
# _.regImps[focus()]['app']

# class Threads
# class Queue
# def add(
# def printReport(
# def checkTimeout(
# def audit

# class regImp:


# 2B-C3P0-AF i: {id} 
# 2B-R2D2-AF
# r: {relatedid}

{ '2B100AF': 0, 'id': 0, 'genfrom': 0,  'created': 1558456773.7885933 }

############################################### ###############################################

ciData = (    [ ';;',            ',' ],
			[ ';c',            ',' ],
			[ '_;192A;_',    ',' ],
			
			[ ';_',            '-' ],
			[ ';-',            '-' ],

			[ ';p',            '%' ],
			[ ';p;',        '%' ],
			[ ';.',            ':' ],
			[ '_;192B;_',    ':' ],
			[ ";;'",        _v.slash+'"' ],

			[ _v.slash+'n',        '\n' ],
			[ ';n',            '\n' ],
			[ ';return',    '\n' ],
			[ ';t',            '\t' ],

			[ ";'",            '"' ],
			[ ';q;',        '"' ],
			[ '"\'"',        "'" ],
			[ 'null00',        '"",' ],
			[ '"\'", "\'"',    "','" ],

			[ '[star]',        '*' ],
			[ '[a]',        '*' ],
			[ '[eq]',        '=' ],
			[ ';opar;',        '[' ],
			[ '[pipe]',        '|' ],
			[ '[htmlopen]', '<' ],
			[ '[htmlclose]','>' ],
			[ '[gtr]',        '>' ],
			[ '[lss]',        '<' ],
			[ ';6',            '^' ],
			[ ';+',            '+' ],
			[ '[caret]',    '^' ]  )

############################################### ###############################################

# testlist = [1, 2, 3, 5, 3, 1, 2, 1, 6]
# test = [i for i,x in enumerate(testlist) if x == 1]




# _.fields.register( 'project', 'name', script=_.resolveEpochTest )
# _.fields.asset( 'project', {} )
# _.fields.asset( 'project', [{}] )
# _.fields.register( 'project', 'name', value, appReg=focus() )
# _.fields.register( 'project', 'name', value )
# _.fields.value( 'project', 'name', value )

# fields = Fields()
















