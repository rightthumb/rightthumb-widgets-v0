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

# import os
import sys
# import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str


import datetime
from datetime import datetime as dt, timedelta
import time


_.switches.register('Strait', '-0,-strait')
_.switches.register('End', '-end')
_.switches.register('Epoch', '-epoch')
_.switches.register('Replace', '-replace')
_.switches.register('Short', '-short')

_.appInfo=    {
	'file': 'resolveIDs.py',
	'description': 'Resolve IDs',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('d | p resolveIDs')
_.appInfo['examples'].append('p generateIdResolution  OR  a.idGen')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})

# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         for col in _.appInfo['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Column',formatColumns)
_.switches.process()

# _.tableProfile.append({
#     'field': 'timestamp', 
#     'script_trigger_external': _.float2Date
#     })

# if _.switches.isActive('Snapple') == False:
#     file = _.switches.value('File')
#     variable = _.getTable(file)
#     _.saveTable(xRefList,file)
#     line = _str.replaceAll(line,'  ',' ')
#     line = _str.cleanFirst(line,' ')
#     line = _str.cleanLast(line,' ')
#     line = _str.cleanSpecial(line)
#     line = _str.totalStrip(line)
#     line = _str.removeAll(line)
#     line = _str.replaceDuplicate(line,' ')
#     if _isSwitchActive('Sort'):
#         xRefList = _.sort(xRefList, _.switches.value('Sort'))
#     _.tables.register('Auto',_.switch)
#     _.tables.print('Auto','name,switch,expected_input_example')
	# _.saveTable(rows,theFile,tableTemp = True,printThis = True)
	# theTable = _.getTable(theFile,tableTemp = True,printThis = False)



	# if _.showLine(string):
		# print(line)
pipeResults = ''

if not sys.stdin.isatty():
	pipeResults = sys.stdin.readlines()
	try:
		if not pipeResults[0][0] in _str.safeChar:
			pipeResults[0] = _str.minimalistClean(pipeResults[0])
	except Exception as e:
		pass
	try:
		pipeResults[0] = pipeResults[0].replace( '\f', '' )
	except Exception as e:
		pass

########################################################################################

def resolveIDsNEW(line,clean=False):
	global idResolution
	theID = ''
	pre = line
	once = False
	records = []
	for idr in idResolution:
		if idr['id'] in line:
			records.append([ idr['id'],idr['name'] ])  
	return records


def resolveIDs(line,clean=False):
	global idResolution
	theID = ''
	pre = line
	once = False
	for idr in idResolution:
		if _.switches.isActive('Strait') == True:
			newName = idr['name']
		else:
			newName = ' { { ' + idr['name'] + ' } } '
		line = line.replace(idr['id'],newName)
		if not pre == line and not once:
			once = True
			theID = idr['name']
	if clean:
		line = theID

	return line

def getLabels(line):
	global idResolution
	result = ' >> '
	for idr in idResolution:
		if not len(line) == len(line.replace(idr['id'],'')):
			result += str(idr['name']) + ', '
	result = _str.cleanLast(result,', ')
	if result == ' >> ':
		result = ''
	return result




def resolveEpoch(line,clean=False):
	epoch = ''
	data = _str.totalStrip9(line)
	result = ''

	for word in data.split(' '):
		if word.count('.') > 1:
			wDots = word.split('.')
			wDots.reverse()
			wDots.pop(0)
			wDots.reverse()
			word = '.'.join( wDots )

		if True:
		# if len(word) > 12 and len(word) < 20:
			# result += str(len(word)) + ' '
			test = word.split('.')
			try:
				float(word)
				good = True
			except Exception as e:
				good = False
			if good:
				pass
				# result += str(len(test[0]))
			if good and len(test[0]) == 10 or len(test[0]) == 13 :

				this_is_a_test = False

				epochTest = _.resolveEpochTest( word, showPrint=this_is_a_test, showPrintTry=this_is_a_test, onlyEpoch=False )
				# [ result, epoch ]
				if this_is_a_test:
					print( 'word:', word )
					print( 'epochTest:', epochTest )
				if type( epochTest ) == list:
					result += epochTest[0]
					epoch = epochTest[1]


	if clean:
		result = epoch
	return result


def resolveEpochNEW(line,clean=False):
	epoch = ''
	data = _str.totalStrip9(line)
	result = ''
	record = []
	for word in data.split(' '):
		if word.count('.') > 1:
			wDots = word.split('.')
			wDots.reverse()
			wDots.pop(0)
			wDots.reverse()
			word = '.'.join( wDots )

		if True:
		# if len(word) > 12 and len(word) < 20:
			# result += str(len(word)) + ' '
			test = word.split('.')
			try:
				float(word)
				good = True
			except Exception as e:
				good = False
			if good:
				pass
				# result += str(len(test[0]))
			if good and len(test[0]) == 10 or len(test[0]) == 13 :

				this_is_a_test = False

				epochTest = _.resolveEpochTest( word, showPrint=this_is_a_test, showPrintTry=this_is_a_test, onlyEpoch=False )
				# [ result, epoch ]
				if this_is_a_test:
					print( 'word:', word )
					print( 'epochTest:', epochTest )
				if type( epochTest ) == list:
					record.append( [word,_.friendlyDate(float(word))] )
					result += epochTest[0]
					epoch = epochTest[1]


	if clean:
		result = epoch
	return record
	return result


def action():
	global pipeResults
	global idResolution
	data = []
	epochCount = 0
	idCount = 0
	for line in pipeResults:
		line2=line
		line=line.replace('.',' ')
		line = line.replace('\n','')
		
		if _.switches.isActive('End'):
			print(line,getLabels(line),resolveEpoch(line))
		elif _.switches.isActive('Replace'):
		
			for rec in resolveEpochNEW(line):
				line = line.replace( str(rec[0]), _.colorThis( [ str(rec[1]) ], 'yellow', p=0 ) )
			for rec in resolveIDsNEW(line):
				new = _.colorThis( [ '( ' ], 'red', p=0 )
				new += _.colorThis( [ rec[0][0:3]+'..'+rec[0][-3:] ], 'blue', p=0 )
				new+= ' '
				new+= _.colorThis( [ str(rec[1]) ], 'green', p=0 )
				new+= _.colorThis( [ ' )' ], 'red', p=0 )
				
				line = line.replace( str(rec[0]), new )

			print(line)
				# data.append({ 'id': str(rec[0]), 'epoch': str(rec[0]), 'line': line })
			# print( 'resolveEpochNEW:', epochs )
			# print(resolveEpoch(line),resolveIDs(line))
		else:
			epoch = resolveEpoch(line,True)
			theID = resolveIDs(line,True)
			if len(epoch) > 0:
				epochCount += 1
			if len(theID) > 0:
				idCount += 1
			data.append({ 'id': theID, 'epoch': epoch, 'line': line2 })

	_.tables.register('resolvedData',data)
	_.tables.fieldProfileSet('resolvedData','id','alignment','right')
	print()


	if not _.switches.isActive('Short'):
		_.switches.fieldSet('Long','active',True)

	if idCount == 0 and epochCount == 0:
		print()
		print('Nothing to resolve')
	elif idCount > 0 and epochCount > 0:
		_.tables.print('resolvedData','epoch,id,line')
	elif idCount > 0 and epochCount == 0:
		_.tables.print('resolvedData','id,line')
	elif idCount == 0 and epochCount > 0:
		_.tables.print('resolvedData','epoch,line')

########################################################################################
idResolution = _.getTable('idResolution.json')

if __name__ == '__main__':
	action()