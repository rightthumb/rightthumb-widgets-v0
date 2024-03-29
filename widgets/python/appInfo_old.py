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
import simplejson as json
import importlib
import time

##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Folder', '-folder')
	



_.appInfo[focus()] = {
	'file': 'appInfo.py',
	'description': 'Extracts app info',
	'categories': [
						'research',
						'text manipulation',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

_.appInfo[focus()]['examples'].append('p appInfo -i fileRecover.py txtBackup.py txtBackup2.py')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p f -in *.py + "_.appInfo[focus()]" "_.appInfo[__name__]" -or - # -jn | p appInfo > %tmpf0%')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p f -in *.py + appInfo -jn | p appInfo')
_.appInfo[focus()]['examples'].append('')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})





def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		_.argvProcess = True
		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()





def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in sys.stdin.readlines():
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')




_.appData[__.appReg]['pipe'] = ''
if not sys.stdin.isatty():
	_.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



# os.path.isfile(files)
# os.system('cls')

# _.switches.isActive('_File_')
# global

# _.appInfo[focus()]['categories']

# #######################################
# uuidProject = { 'input': _.switches.value('Input'), 'note': 'sample' }
# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[__.appReg]['file'], 'project': uuidProject }
# _.genUUID(project='')
# _.genUUID('temp file')
# _.genUUID({'file':'app.py'})

# #######################################
# import blank
# blank.focus(focus())
# blank.registerSwitches()
# _.switches.fieldSet('Input','active','one')
# _.switches.fieldSet('Input','value','one')
# focus()
# #######################################

# _.switches.fieldSet('_File_','active',True)

# _.switches.dumpSwitches(includeBlank=False)

# _.tables.register('childClassItems',childItems)
# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
# _.tables.print('childClassItems','name')

# backupLog = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )

# _mime.isText(file)
# _mime.isBinary(file)

# books = _.getText(_v.myTables + '\\bible_books.csv')
# _.saveText(convertedFile,'file.txt')

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START

def processText(text):
	depth = 0
	result = {}
	css = []
	start = False
	ranOnce = False
	dataRaw = ''
	for i,line in enumerate(text):
		line = line.replace('\n','')
		# _.pr(i,line)
		if 'appInfo'.lower() in line.lower():
			# _.pr(line)
			start = True
		if start and not ranOnce:
			
			if '}' in line:
				start = False
				depth -= 1
				dataRaw += line.split('}')[0]
				# _.pr(dataRaw)
				# dataRaw = ''
				ranOnce = True
			elif '{' in line:
				dataRaw += line.split('{')[1]
				depth += 1
			else:
				dataRaw += line
	if len(dataRaw) > 0:
		data = '{' + dataRaw + '}'
		# _.pr(dict(data))
		# sys.exit()
		data = data.replace("'",'"')
		data = data.replace('\n','')
		data = data.replace('\t','')
		data = data.replace('\t','')
		data = _str.replaceDuplicate(data,' ')
		data = _str.cleanBE(data,' ')
		data = data.replace(' }','}')
		data = data.replace(' }','}')
		
		data = data.replace('[],}','[]}')
		data = data.replace(',}','}')
		data = data.replace(', }','}')
		data = data.replace(',]',']')
		data = data.replace('#','')
		data = data.replace('True','true')

		if '[],}' in data:
			data = data.split('[],}')[0]
			data += '[]}'
			# sys.exit()

		# _.pr(data)
		# _.pr(result)
		# sys.exit()
		# result = json.loads(data)
		try:
			result = json.loads(data)
		except Exception as e:
			result = False
			_.pr()
			_.pr()
			_.pr()
			_.pr(data)
			sys.exit()
	else:
		result = False
	return result

def test():
	_.pr('test')

def action():
	# test = {       'file': '7z.py',        'description': '7zip basics made simple',       'prerequisite': [], 'examples': [],     'columns': [],  }
	# _.pr(test)
	# _.pr(json.dumps(test))
	# sys.exit()



	# TEST - process list of files piped or by switch 

	# shouldRun = False
	# if _.switches.isActive('Input'):
	#     shouldRun = True
	#     dirList = file.split(',')
	#     file = _.switches.value('Input')

	# if not type(_.appData[__.appReg]['pipe']) == str:
	#     shouldRun = True
	#     dirList = _.appData[__.appReg]['pipe']

	# if shouldRun:
	#     _.pr()
	#     apps = {}
	#     errors0 = 0
	#     for fi in dirList:
	#         fi = fi.replace('\n','')
	#         fi = fi.replace('.py','')
	#         # _.pr('Loading:\t',fi)
	#         try:
	#             apps[fi] = eval('importlib.import_module(fi)')
	#             # _.pr('Loaded')
	#         except Exception as e:
	#             _.pr('Error: ',fi)
	#             errors0 += 1
			
			
	#     _.pr()
	#     _.pr()
	#     errors1 = 0
	#     success = 0
	#     for infoKeys in _.appInfo.keys():
	#         try:
	#             _.pr(_.appInfo[infoKeys]['file'],'\t',_.appInfo[infoKeys]['description'])
	#             success += 1
	#         except Exception as e:
	#             _.pr('Error:',infoKeys)
	#             errors1 += 1
		
	#     _.pr('success:',success)
	#     _.pr('errors0:',errors0)
	#     _.pr('errors1:',errors1)



	# TEST - pipe over file NOT filenames

	# shouldRun = False
	# if not type(_.appData[__.appReg]['pipe']) == str:
	#     shouldRun = True
	#     text = _.appData[__.appReg]['pipe']

	# if shouldRun:
	#     _.pr()
	#     data = processText(text)
	#     _.pr(data)

		
	# TEST - process list of files piped or by switch 

	shouldRun = False
	if _.switches.isActive('Input'):
		shouldRun = True
		dirList = file.split(',')
		file = _.switches.value('Input')

	if not type(_.appData[__.appReg]['pipe']) == str:
		shouldRun = True
		dirList = _.appData[__.appReg]['pipe']

	if shouldRun:
		_.pr()
		apps = {}
		# _.pr(dirList)
		
		errors = 0
		success = 0
		errors0 = 0
		errors1 = 0
		appRegistration = []
		for fi in dirList:
			fi = fi.replace('\n','')
			txtFile = _.getText(fi)
			data = processText(txtFile)
			try:
				if type(data) == bool:
					_.pr('Error:',fi)
					errors += 1
					errors1 += 1
				else:
					data['livefile'] = fi
					appRegistration.append(data)
					# _.pr(data)
					# _.pr(fi,'\t',str(data))
					success += 1
					
			except Exception as e:
				_.pr('Error:',fi)
				errors += 1
				errors0 += 1
		_.pr()
		_.pr('success:',success)
		_.pr('errors:',errors)
		if errors > 0:
			_.pr('errors0:',errors0)
			_.pr('errors1:',errors1)

		_.saveTable(appRegistration,'appRegistration.json')
		_.pr()
		_.pr()
		# for ar in appRegistration:
		#     _.pr(ar.keys())
		#     try:
		#         ar['file']
		#     except Exception as e:
		#         _.pr(ar['livefile'])

		for ar in appRegistration:
			if not ar['file'] == ar['livefile']:
				_.pr(ar['livefile'])




########################################################################################
if __name__ == '__main__':
	action()






