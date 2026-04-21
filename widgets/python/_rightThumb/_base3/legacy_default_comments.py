

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

# books = _.getText(_v.myTables + _v.slash+'bible_books.csv')
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
