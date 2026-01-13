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
import time
# import simplejson as json
# from threading import Timer


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
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	



_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
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

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

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
	_.defaultScriptTriggers()
	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
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

def setPipeData(data):
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in data:
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




_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )
	# _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



########################################################################################

# def processFolder(folder, qID):
# __.queueLastActivity = time.time()
# __.projectData[focus()][__.pdID[focus()]].append( obj )
# _.threads.add( 'test', testFunction, [{'two':item}], kwargs=True )
# _.threads.add( 'process_folder', processFolder, [ path ] )
# _.threads.spent( qID, sys.getsizeof( 'obj') )
					################
# _.threads.add( 'test', trigger=complete, triggerArg={'hello','test'}, loaded=False )
# _.threads.add( 'test', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
# _.threads.maxThreadsSafe = 250
# _.threads.report = True
# _.threads.projectDataFileSQL = db
# _.threads.auditPrint = False

##################

# _.appData[focus()]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
# _.appInfo[focus()]['instance'] = _.genUUID()
# # _.appData[focus()]['audit'].append( { 'start': True, 'note': '', 'entire': True, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );

# _dir.sqlCreateTable( db, deleteDBFirst=True, close=True )
# obj = _dir.fileInfo( path, sql=True )
# _.pr(   _dir.fileInfo( _.switches.value('Input') )['size']   )

# _.saveLog('queue')
# _.saveLog('audit')

########################################################################

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
# _.saveTable( jsonFile, 'file.json', printThis=True )

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:
# os.system('"' + do + '"')

########################################################################################
########################################################################################
# NEW database stuff

# def testTrigger( data ):
#     return data * 5

# def dateScramble( data ):
#     d = _.date2epoch( data )
#     if len( str(data) ) > 0:
#         _.pr( data, d )
#     return _.resolveEpochTest( d, falseBlank=True )

	# data = [
	#             {
	#                         'first': 'Scott',
	#                         'last': 'Reph',
	#                         'test': 3,
	#             },
	#             {
	#                         'first': 'Alpha',
	#                         'last': 'Reph',
	#                         'test': 7,
	#             },
	# ]
	# fieldConfig = [{
	#             'table': 'test_table',
	#             'name': 'test',
	#             'trigger': testTrigger,
	#     },{
	#             'table': 'test_table',
	#             'name': 'date_modified',
	#             'trigger': dateScramble,
	#     }]

	# testSet = 0
	# if testSet == 1:
	#     __.databases.register(
	#                             name='test',
	#                             table='test_table',
	#                             file='__first_test.db',
	#                             records=data,
	#                             delete=True,
	#                             fields=fieldConfig,
	#                             # printFileActivity=True,
	#     )
	# elif testSet == 0:
	#     __.databases.register(
	#                             name='test',
	#                             file='__first_test.db',
	#     )
	# elif testSet == 2:
	#     testSet = 1
	#     __.databases.register(
	#                             name='test',
	#                             file='__first_test____X.db',
	#                             fields=fieldConfig,
	#     )
	# elif testSet == 3:
	#     testSet = 1
	#     __.databases.register(
	#                             name='test',
	#                             file='__first_test____X.db',
	#                             delete=True,
	#     )







	# if testSet == 1:
	#     records = []

	#     records.append({
	#                                     'first': 'Jessica',
	#                                     'last': 'Reph',
	#                                     'test': 55,
	#     })

	#     records.append({
	#                                     'first': 'Nana',
	#                                     'last': 'Reph',
	#                                     'test': 100,
	#     })

	#     __.databases.insertRecords( name='test', table='test_table', records=records )


	#     __.databases.update(
	#                             name='test',
	#                             info={
	#                                     'table': 'test_table',
	#                                     'record': {
	#                                                     'first': 'Sam',
	#                                                     'last': 'Test',
	#                                                     'test': 99,
	#                                     },
	#                                     'update': 'id=1',
	#                             }
	#     )









	# results = __.databases.search(
	#                         name='test',
	#                         info={
	#                                 'table': 'test_table',
	#                                 'custom': 'select * from test_table',
	#                                 'force': True,
	#                         }
	# )

	###################
	# __.databases.trigger(
	#                         name='test',
	#                         table='test_table',
	#                         field='test',
	#                         trigger=testTrigger,
	# )

	# results = __.databases.search(
	#                         name='test',
	#                         info={
	#                                 'table': 'test_table',
	#                                 'type': 'text',
	#                                 'field': 'first',
	#                                 'search': 'Scott',
	#                                 'custom': False,
	#                                 'force': False,

	#                         }
	# )

	# results = __.databases.search(
	#                         name='test',
	#                         info={
	#                                 'table': 'test_table',
	#                                 'custom': 'test<10 and test>5',
	#                                 'force': False,
	#                         }
	# )
	###################

	# try:
	#     _.pr()

	#     fieldList = ','.join(__.databases.getFields( 'test', 'test_table', exclude='' ))
	#     _.tables.register('results_table',results)
	#     _.tables.print('results_table',fieldList)
	# except Exception as e:
	#     pass


########################################################################################
########################################################################################
# START

import urllib

from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(b"""
								<!DOCTYPE html>
								<html lang="en">

								<head>
									<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>

									<meta charset="utf-8">
									<title>test</title>
									<!-- <META http-equiv="refresh" content="1;URL=/?"> -->
								</head>

								<body>
									<input type="text" name="code" id="code" value='{ "first": "Scott", "last": "Reph" }'><br>
									<input type="submit" value="Submit" onclick="python.send()">
								</body>
								<script>

									python = {
										items: [],
										itemID: 0,
										fix: function() {
											var data = JSON.parse($("#code").val());
											$("#code").val(JSON.stringify(data))
											
										}, //==============================================
										send: function() {
											//python.fix();
											$.post(
												"http://127.0.0.1:8000/", {
													'test': $("#code").val()
												},
												function(data) {
													$('body').prepend( '<div id="giftcertificateArea" style=" position: fixed; z-index: 9; background-color: #FFF; width: 300px; height: 190px; left: calc( 50% - 150px ); top: calc( 50% - 95px ); border: whitesmoke; border-style: solid; border-width: 10px; " ><div id="giftcertificateClose" style=" width: 100%; text-align: right; color: crimson; font-weight: bolder; " onclick=" $(this).parent().remove(); " >Close</div><div id="giftcertificate" style=" width: 100%; text-align: left; " ></div></div>' );
													$('#giftcertificate').html(data)
												}
											)
										} // END
									}

								</script>
								</html>

			""")

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)
		self.send_response(200)
		self.end_headers()
		response = BytesIO()
		response.write(b'This is POST request. ')
		response.write(b'Received: ')
		response.write(body)
		submitedData = response.getvalue()
		self.wfile.write( submitedData )
		testDic( submitedData )


def testDic( data ):
	_.pr( type( data ))
	data = str( data )
	_.pr( type( data ))
	_.pr( data )
	_.pr()
	_.pr( 'Got Here' )
	_.pr()
	newData = urllib.parse.unquote( data.split('test=')[1] ).replace( '+', ' ' )[:-1]
	_.pr( newData )
	theDic = True
	try:
		theDic = eval(newData)
	except Exception as e:
		theDic = False
	_.pr()
	_.pr()
	_.pr( type( theDic ))
	_.pr( theDic )

def action():
	httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
	httpd.serve_forever()

if __name__ == '__main__':
	action()






