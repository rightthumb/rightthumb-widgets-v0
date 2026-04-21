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
__.registeredApps.append( focus() )


import _rightThumb._base3 as _
_.load()

##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str

# _bm = _.regImp( __.appReg, 'bookmarks' )
	# index = _bm.imp.index()
# _dirList = _.regImp( __.appReg, 'dirList' )
#     _dirList.switch( 'Files' )
#     _dirList.switch( 'Recursion' )
#     _dirList.switch( 'Binary' )
#     _dirList.switch( 'Path','D:\\Apps' )
#     files = _dirList.do( 'action' )

# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword( 'string' )
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
#     _blowfish.encrypt( infilepath, outfilepath, key )
#     _blowfish.decrypt( infilepath, outfilepath, key )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browserX = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )
# _file_folder = _.regImp( __.appReg, 'file_folder' )
#     _file_folder.switch( 'Save,Clean' )
#     _file_folder.switch( 'Compair,Clean' )
#     _file_folder.switch( 'Folder', '' )
# _fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
#     _fileNameDate.imp.newName( filename )
#     _fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )
# _filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	# _filePathPatterns.switch( 'NoPrint' )
	# _filePathPatterns.switch( 'Files', _.switches.value( 'Files' ) )
	# folderReport = _filePathPatterns.action()
# fileBackup = _.regImp( __.appReg, 'fileBackup' )
#     fileBackup.switch( 'Input', filename )
#     fileBackup.switch( 'Flag', 'pre replaceText' )
#     recoveryFile = fileBackup.do( 'action' )
# _folderContent = _.regImp( __.appReg, 'file' )
#     _folderContent.switch( 'Silent' )
#     _folderContent.switch( 'Folder', _v.myAppsBatch )
#     _folderContent.switch( 'NoExtension' )

#     _folderContent.switch( 'Recursive' )

#     _folderContent.switch( 'Text' )
#     _folderContent.switch( 'Binary' )
#     _folderContent.switch( 'Label', 'App: ' )
#     _folderContent.switch( 'Prefix', ';t' )
#     files = _folderContent.do( 'action' )['files']
#     folders = _folderContent.do( 'action' )['folders']
# _tickets = _.regImp( __.appReg, 'ticketTimeline' )
#     _tickets.switch( 'ReturnFiles' )
#     records = _tickets.do( 'records' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )


	_.switches.register('Input', '-i,-f,-file','payroll.sql')
	_.switches.register('App', '-app','signature')
	_.switches.register('Prefix', '-pre,-prefix','_reph_signature_')

	"""
	_.switches.documentation( 'Test', { 
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	"""


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'crud.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Auto gen web app',
	'categories': [
						'app',
						'tool',
						'generate',
						'generate app',
						'auto',
						'auto app',
						'gen',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						'p crudConfig -i sql.json',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p crud -f structure.sql -app share -pre _trt_',
						'',
						'p crud -prefix _reph_signature_ -app signature -file payroll.sql',
						'',
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



# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )



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
	
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	
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
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
# __.appRegPipe
########################################################################################
# START



def clean(string):
	# string = _str.replaceAll(string,'\t',' ')
	string = string.replace('\t',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanBE(string,' ')
	return string

def php_funcname(table):
	prefix = _.switches.value('Prefix')
	# _.pr(prefix)

	# _.pr(table)
	# sys.exit()
	table = table.replace(prefix,'')
	# _.pr(table)
	table = table.replace('_',' ')
	table = table.title()
	table = table.replace(' ','_')
	return table

def php_funcfields(fields,cu):
	f = ''
	for field in fields:
		if actionable(field,',status,del'):
			if cu == 'c':
				if len(field['default']) == 0:
					f += '$' + field['field'] + ', '
			else:
				f += '$' + field['field'] + ', '
	f = _str.cleanBE(f,', ')
	return f

def php_tfields(fields):
	f = ''
	for field in fields:
		if actionable(field,',status,del'):
			# if len(field['default']) == 0:
			f += field['field'] + ', '
	f = _str.cleanBE(f,', ')
	return f

def php_vfields(fields):
	f = ''
	for field in fields:
		if actionable(field,',status,del'):
			# if len(field['default']) == 0:
			if field['type'] == 'int':
				f += ""+'$' + field['field'] + "" + ', '
			else:
				f += "'"+'$' + field['field'] + "'" + ', '
	f = _str.cleanBE(f,', ')
	return f

def php_readfields(table,fields):
	prefix = _.switches.value('Prefix')
	abrev = []
	t = table.replace(prefix,'')
	b = "\n        'FIELD1' => $row['FIELD2'],"
	f = ''
	for field in fields:
		if actionable(field,'del'):
			fx = t + '_' + field['field']
			f += b.replace('FIELD2',field['field']).replace('FIELD1',    (fx))
	f = _str.cleanBE(f,', ')
	return f

def php_labelFix(field):
	if 'label' in field:
		field = 'label'
	return php_deleteFix(field)

def php_deleteFix(field):
	if '_del' in field:
		field = 'action_del'
	return field


def php_updatefields(fields):
	b = "FIELD='$FIELD', "
	bb = "FIELD=$FIELD, "
	f = ''
	for field in fields:
		if actionable(field,''):
			if field['type'] == 'int':
				f += bb.replace('FIELD',field['field'])
			else:
				f += b.replace('FIELD',field['field'])
	f = _str.cleanBE(f,', ')
	return f
def php_toggleArea(crudToggle,fields):
	f = ''
	for field in fields:
		if actionable(field,''):
			if 'toggle' in field['note']:
				f += crudToggle.replace('[funcToggleField]',field['field'].title()).replace('[toggleField]',field['field'])
	return f
def php_joinsArea(crudJoins,thisTable,fields):
	global data
	result = ''
	hasJoins = False
	for field in fields:
		if field['note'] == 'altID':
			hasJoins = True
	if hasJoins:
		
		queryX = 'SELECT [select_fields] \n\n'\
				'FROM [table] AS [abrev] \n\n'\
				'[JOINDATA] \n'\
				'WHERE [abrev].guid=\'$guid\''
		prefix = _.switches.value('Prefix')
		abrev = []
		t = thisTable.replace(prefix,'')

		# _.pr(thisTable)
		buildJoins = ''
		buildfields = ''
		buildfieldsArr = ''
		for field in fields:
			buildfields += thisTable.replace(prefix,'')+'.'+field['field'] + ' as ' + thisTable.replace(prefix,'')+'_'+field['field']+', '

		joinX = 'JOIN [join_table] AS [join_abrev] ON [abrev].[join_field] = [join_abrev].guid \n'
		arrX = "\n        'FIELD' => $row['FIELD'],"
		for field in fields:
			buildfieldsArr += arrX.replace('FIELD',t+'_'+field['field'])
			if field['note'] == 'altID':
				fx = field['field'].replace('_mid','').replace('_id','')
				tx = prefix + fx
				for i,table in enumerate(data['sql']):
					if table['table'] == tx:
						a = tx.replace(prefix,'')
						jn = joinX.replace('[join_table]',tx)
						jn = jn.replace('[join_abrev]',a)
						jn = jn.replace('[join_field]',field['field'])
						buildJoins += jn
						for tfield in table['fields']:
							buildfields += a+'.'+tfield['field'] + ' as ' + a+'_'+tfield['field']+', '
							buildfieldsArr += arrX.replace('FIELD',a+'_'+tfield['field'])


							if tfield['note'] == 'altID':
								yfx = tfield['field'].replace('_mid','').replace('_id','')
								ytx = prefix + yfx
								for i,ytable in enumerate(data['sql']):
									if ytable['table'] == tx:
										ya = ytx.replace(prefix,'')
										jn = joinX.replace('[join_table]',ytx)
										jn = jn.replace('[abrev]',a)
										jn = jn.replace('[join_abrev]',ya)
										jn = jn.replace('[join_field]',tfield['field'])
										buildJoins += jn
										for ytfield in ytable['fields']:
											buildfields += ya+'.'+ytfield['field'] + ' as ' + ya+'_'+ytfield['field']+', '
											buildfieldsArr += arrX.replace('FIELD',a+'_'+ytfield['field'])
		# _.pr()
		buildfields = _str.cleanBE(buildfields,', ')
		queryX = queryX.replace('[JOINDATA]',buildJoins)
		queryX = queryX.replace('[select_fields]',buildfields)
		queryX = queryX.replace('[table]',thisTable)
		queryX = queryX.replace('[abrev]',thisTable.replace(prefix,''))
		result = crudJoins.replace('[readfields]',buildfieldsArr)
		result = result.replace('[theQuery]',queryX)
		# _.pr(result)
	return result

def php_combineTables():
	global data
	app = _.switches.value('App')
	f = ''
	b = ''
	for d in data['sql']:
		if not '_items' in d['table']:
			table = jsAppTable(d['table'])
			f += b.replace('[js_APP]',app).replace('[js_APP_TABLE]',table).replace('TABLELABEL',jsSectionLable(app,d['table']))
	return f

def php_processRecordsFields(table,fields):
	prefix = _.switches.value('Prefix')
	abrev = []
	t = table.replace(prefix,'')
	b = "\n        $FIELD2=$item[FIELD1];"
	f = ''
	for field in fields:
		if actionable(field,''):
			fx = t + '_' + field['field']
			f += b.replace('FIELD2',field['field']).replace('FIELD1',php_labelFix(fx))
	f = _str.cleanBE(f,', ')
	return f

def phpaction(table,fields):
	global phpCrudBase
	global functions
	crud = phpCrudBase['crud']
	crudToggle = phpCrudBase['crud_toggle']
	crudJoins = phpCrudBase['crud_joins']
	crudTables = phpCrudBase['crud_tables']



	funcname0 = '[funcname]'
	funcname1 = php_funcname(table)
	crud = crud.replace(funcname0,funcname1)
	crudToggle = crudToggle.replace(funcname0,funcname1)
	crudJoins = crudJoins.replace(funcname0,funcname1)
	crudTables = crudTables.replace(funcname0,funcname1)

	funcfields0 = '[funcfields_c]'
	funcfields1 = php_funcfields(fields,'c')
	crud = crud.replace(funcfields0,funcfields1)

	funcfields0 = '[funcfields_u]'
	funcfields1 = php_funcfields(fields,'u')
	crud = crud.replace(funcfields0,funcfields1)

	tfields0 = '[tfields]'
	tfields1 = php_tfields(fields)
	crud = crud.replace(tfields0,tfields1)

	vfields0 = '[vfields]'
	vfields1 = php_vfields(fields)
	crud = crud.replace(vfields0,vfields1)

	readfields0 = '[readfields]'
	readfields1 = php_readfields(table,fields)
	crud = crud.replace(readfields0,readfields1)
	crudTables = crudTables.replace(readfields0,readfields1)

	table0 = '[table]'
	table1 = table
	crud = crud.replace(table0,table1)

	updatefields0 = '[updatefields]'
	updatefields1 = php_updatefields(fields)
	crud = crud.replace(updatefields0,updatefields1)


	toggleArea0 = '[toggle]'
	toggleArea1 = php_toggleArea(crudToggle,fields)
	crud = crud.replace(toggleArea0,toggleArea1)

	joinsArea0 = '[joins]'
	joinsArea1 = php_joinsArea(crudJoins,table,fields)
	crud = crud.replace(joinsArea0,joinsArea1)

	joinsArea0 = '[table_data]'
	crud = crud.replace(joinsArea0,crudTables)

	joinsArea0 = '[process_records_fields]'
	crud = crud.replace(joinsArea0,php_processRecordsFields(table,fields))



	# crud += php_combineTables()



	# crudToggle
	# crudJoins
	# crudTables




	# for line in crud.split('\n'):
	#     if 'function ' in line:
	#         function = clean(line.split('function ')[1].split('{')[0])
	#         functions.append(function)
	#         _.pr(function)



	# _.pr(crud)

	return crud

def actionable(row,omit):
	# field,type,length,default,note
	result = True
	for o in omit.split(','):
		if '*' in o:
			if o.replace('*','') in row['field']:
				result = False
		elif row['field'] == o:
			result = False
			
	if row['field'] == 'date_created':
		result = False
	if row['note'] == 'thisID':
		result = False
	# if row['note'] == 'thisID'
	if 'timestamp' in row['default']:
		result = False
	if 'auto' in row['default']:
		result = False
	if 'epoch' in row['note']:
		result = False
	# _.pr(row['note'])
	return result




def jsAppTable(table):
	prefix = _.switches.value('Prefix')
	table = table.replace(prefix,'')
	table = 'x'+table.replace('_',' ')
	table = table.title()
	table = table[1:]
	table = table.replace(' ','')
	table = table.replace('_','')
	return table

def jsFieldVal(app,table,fields,spaces):
	abrev = []
	b = spaces + "try {[js_APP].[js_APP_TABLE].records[i].FIELD1 = $('#[js_APP]_' + i + '_FIELD2').val();} catch (err) { }\n"
	d = spaces + "try { $('#label_' + i + '_FIELD2').text([js_APP].[js_APP_TABLE].records[i].FIELD1); } catch (err) { }\n"
	f = ''
	label = ''
	processedFields = []
	for field in fields:
		if 'label' in field['field']:
			label = field['field']
		if actionable(field,'del'):
			fx = jsFieldName(table,field['field'])
			processedFields.append(fx)
			f += b.replace('FIELD2',field['field'].title()).replace('FIELD1',fx).replace('[js_APP]',app)
			if '_mid' in field['field']:
				pass
			elif '_id' in field['field']:
				pass
			elif 'toggle' in field['note']:
				pass
			else:
				f += d.replace('FIELD2',field['field'].title()).replace('FIELD1',fx).replace('[js_APP]',app)
	# f += b.replace('FIELD2',field['field'].title()).replace('FIELD1',fx).replace('[js_APP]',app)
	x = spaces + 'try {[js_APP].[js_APP_TABLE].records[i].label = '
	if 'label_' in label:
	
		for li in label.replace('label_','').split('_'):
			for pf in processedFields:
				if li in pf and not 'label' in pf:
					x += '[js_APP].[js_APP_TABLE].records[i].' + pf + '+" "+'
		x = _str.cleanBE(x,'+" "+')
	else:
		for pf in processedFields:
			if 'label' in pf:
				x += '[js_APP].[js_APP_TABLE].records[i].' + pf + ''
	x += '; } catch (err) { }\n'
	# _.pr(label,x)
	if len(label) > 0:
		x = x.replace('[js_APP]',app)
		f += x
	# return ''
	return f

def jsFieldValToggle(app,table,fields,spaces):
	abrev = []
	b = spaces + "try {[js_APP].[js_APP_TABLE].records[i].FIELD1 = $('#[js_APP]_' + i + '_FIELD2').val();} catch (err) { }\n"
	b += spaces + "if ([js_APP].[js_APP_TABLE].records[i].FIELD1 === '1') {$('#toggle_' + i + '_FIELD2_on').css('display','inline-block');$('#toggle_' + i + '_FIELD2_off').css('display','none');} else {$('#toggle_' + i + '_FIELD2_on').css('display','none');$('#toggle_' + i + '_FIELD2_off').css('display','inline-block');}\n"
	f = ''
	for field in fields:
		if actionable(field,'del'):
			if 'toggle' in field['note']:
				fx = jsFieldName(table,field['field'])
				f += b.replace('FIELD2',field['field'].title()).replace('FIELD1',fx).replace('[js_APP]',app)
	f = _str.cleanBE(f,', ')
	return f


def jsFieldName(table,field):
	prefix = _.switches.value('Prefix')
	t = table.replace(prefix,'')
	return t + '_' + field
	# return field
	# return '_'+field


def jsValidateSection(app,table,fields,spaces):
	global jsValidate
	# _.pr(jsValidate)
	# sys.exit()
	abrev = []
	f = ''
	for field in fields:
		if actionable(field,'del'):
			if 'email' in field['field']:
				b = jsValidate['email']
			elif field['type'] == 'int':
				b = jsValidate['int']
			else:
				b = jsValidate['text']
			fx = jsFieldName(table,field['field'])
			dn = jsFieldLabel(field['field'])
			f += b.replace('FIELD',field['field'].title()).replace('[js_APP]',app).replace('[spaces]',spaces).replace('DEFAULTLABEL',dn)
	f = _str.cleanBE(f,', ')
	return f

def jsHTMLFields(fields):
	f = ''
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			f += field['field'] + ', '
	f = _str.cleanBE(f,', ')
	return f

def  jsHTMLUndefined(fields,spaces):
	f = ''
	b = "[spaces]if (typeof FIELD === 'undefined') { FIELD = 'DEFAULT'; }\n"
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			f += b.replace('FIELD',field['field']).replace('[spaces]',spaces).replace('DEFAULT',field['default'])
	return f

def  jsHTMLROW(jsCrudBase,app,fields):
	global data

	# jsCrudBase['row_plain']
	# jsCrudBase['row_select']
	# jsCrudBase['row_toggle']

	f = ''
	hasStatus = False
	lastStatus = False
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			tbl = ''
			tblLabel = ''
			if '_mid' in field['field']:
				for d in data['sql']:
					if field['field'].replace('_mid','') in d['table']:
						tbl = jsAppTable(d['table'])
						for fl in d['fields']:
							if 'label' in fl['field']:
								tblLabel = jsFieldName(d['table'],fl['field'])
								# _.pr(d['table'],fl['field'])
								# _.pr(tblLabel)
				code = jsCrudBase['row_select']
			elif '_id' in field['field']:
				code = jsCrudBase['row_hidden']
			elif 'toggle' in field['note']:
				code = jsCrudBase['row_toggle']
			else:
				code = jsCrudBase['row_plain']
			n = jsFieldLabel(field['field'])
			if lastStatus:
				lastStatus = False
				hasStatus = True
				f += jsCrudBase['more_button']

			f += code.replace('FIELD1',field['field']).replace('FIELD2',field['field'].title()).replace('[js_APP]',app).replace('FIELD3',n).replace('[js_APP_TABLE_ALT]',tbl).replace('[js_TABLE_LABEL]',tblLabel)
			if field['field'] == 'status':
				lastStatus = True
	if hasStatus:
		f += jsCrudBase['more_close']
		f += '\n</div>'+_v.slash
	return f

def  jsHTMLNull(app,table,fields,spaces):
	f = ''
	b = "[spaces]if ([js_APP].[js_APP_TABLE].records[i].FIELD === null) { [js_APP].[js_APP_TABLE].records[i].FIELD = 'DEFAULT'; }\n"
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			f += b.replace('FIELD',jsFieldName(table,field['field'])).replace('[spaces]',spaces).replace('[js_APP]',app).replace('DEFAULT',field['default'])
	return f

def  jsHTMLFieldsJSON(app,table,fields):
	f = ''
	b = '[js_APP].[js_APP_TABLE].records[i].FIELD, '
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			f += b.replace('FIELD',jsFieldName(table,field['field'])).replace('[js_APP]',app)
	f = _str.cleanBE(f,', ')
	return f

def jsAdd(app,table,fields):
	f = ''
	b = '"FIELD":"DEFAULT",'
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			if table.endswith('_items') and field['field'].endswith('_id'):
				# _.pr(jsFieldName(table,field['field']))
				f += b.replace('FIELD',jsFieldName(table,field['field'])).replace('"DEFAULT"',app+'.'+jsAppTable(table)+'.parent')
			else:
				f += b.replace('FIELD',jsFieldName(table,field['field'])).replace('DEFAULT',field['default'])
	f = _str.cleanBE(f,', ')
	return f

def  jsHTMLDefault(fields,spaces):
	f = ''
	b = "[spaces]if (FIELD1 === '') { FIELD1 = 'FIELD2'; }\n"
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			n = jsFieldLabel(field['field'])
			f += b.replace('FIELD1',field['field']).replace('[spaces]',spaces).replace('FIELD2',n)
	return f
def  jsFormFocus(app,fields,spaces):
	f = ''
	b = "[spaces]if ('[js_APP]_'+idx+'_FIELD1' === id && $('#'+id).val() === 'FIELD2') { $('#'+id).val('') }\n"
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			n = jsFieldLabel(field['field'])
			f += b.replace('FIELD1',field['field'].title()).replace('[spaces]',spaces).replace('FIELD2',n).replace('[js_APP]',app)
	return f

def  jsFormBlur(app,fields,spaces):
	f = ''
	b = "[spaces]if ( $('#'+[js_APP].v.lastID).hasClass('_FIELD1_') && $('#'+[js_APP].v.lastID).val() === '') { $('#'+[js_APP].v.lastID).val('FIELD2') }\n"
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			n = jsFieldLabel(field['field'])
			f += b.replace('FIELD1',field['field'].title()).replace('[spaces]',spaces).replace('FIELD2',n).replace('[js_APP]',app)
	return f

def jsFieldLabel(field):
	return field.replace('_mid','').replace('_id','').replace('_',' ').replace('dvalue','value').replace('percentage','% or hr').title()

def  jsaField(app,fields):
	f = ''
	b = "'#[js_APP]_' + i + '_FIELD2'"
	found = False
	for field in fields:
		if actionable(field,'del,*json,label_*'):
			if '_mid' in field['field']:
				pass
			elif 'toggle' in field['note']:
				pass
			else:
				if not found:
					found = True
					f = b.replace('FIELD2',field['field'].title()).replace('[js_APP]',app)
	return f

def jsResolveIDs(app):
	global jsCrudBase
	global data
	f = ''
	for d in data['sql']:
		found = False
		for fl in d['fields']:
			if 'label' in fl['field']:
				found = True
		if found:
			table = jsAppTable(d['table'])
			f += jsCrudBase['resolveids'].replace('[js_APP]',app).replace('[js_APP_TABLE]',table)
	return f

def jsAddChildDiv(app,table):
	global data
	global jsCrudBase
	f = ''
	found = False
	for d in data['sql']:
		if d['table'] == (table + '_items') or d['table'] == (table[:-1] + '_items'):
			_.pr(d['table'])
			found = True
		if found:
			# f = '$(\'[js_main_app_id]\').append(\'<div class="thechild"></div>\');'
			f = jsCrudBase['manage_children']
	f = f.replace('[js_APP]',app)
	f = f.replace('[js_APP_TABLE]',jsAppTable(table))
	return f

def jsMainAppId(app,table):
	# if table.endswith('_items'):
	#     f = '.thechild'
	# else:
	#     f = '#manage'
	# return f
	return '#manage'

def jsChildManageFunction(app,table):
	global data
	f = ''
	found = False
	for d in data['sql']:
		if d['table'] == (table + '_items') or d['table'] == (table[:-1] + '_items'):
			f = '[js_APP].[js_APP_TABLE].parent = guid;  [js_APP].[js_APP_TABLE].manage();'
			f = f.replace('[js_APP_TABLE]',jsAppTable(d['table']))
	f = f.replace('[js_APP]',app)
	return f

def jsIsChild(app,table):
	if table.endswith('_items'):
		f = 'true'
	else:
		f = 'false'
	return f


def jsSectionLable(app,table):
	prefix = _.switches.value('Prefix')
	table = table.replace(prefix,'')
	table = table.replace('_',' ')
	table = table.title()
	return table

def jsFieldPrefix(table,fields):
	f = ''
	found = False
	for field in fields:
		if not found:
			x = jsFieldName(table,field['field'])
			f = x.replace(field['field'],'')
			if not x == f:
				found = True
	return f



def jsSelectPageUn(app,table,fields):
	global data
	global jsCrudBase
	prefix = _.switches.value('Prefix')
	f = ''
	found = False
	for field in fields:
		if field['note'] == 'altID':
			fx = field['field'].replace('_mid','').replace('_id','')
			tx = prefix + fx
			for i,tablex in enumerate(data['sql']):
				if tablex['table'] == tx:
					_.pr(table,tx)
					t = jsAppTable(tx)
					g = jsFieldName(table,field['field'])
					found = True


	if found:
		f = jsCrudBase['selectpage_unspecific_has_group']
		f = f.replace('[js_APP_TABLE_GROUP]',t)
		f = f.replace('[js_group_id]',g)
	else:
		f = jsCrudBase['selectpage_unspecific_no_group']
	f = f.replace('[js_APP]',app)
	f = f.replace('[js_APP_TABLE]',jsAppTable(table))
	return f


def jsDataOut(app):
	global data
	f = ''
	b = '        [js_APP].v.tables[\'[js_APP_TABLE]\'] = [js_APP].[js_APP_TABLE].records;\n'
	for i,table in enumerate(data['sql']):
		t = t = jsAppTable(table['table'])
		f += b.replace('[js_APP]',app).replace('[js_APP_TABLE]',t)
	return f

def jsDataIn(app):
	global data
	f = ''
	b = '        [js_APP].[js_APP_TABLE].records = [js_APP].v.tables.[js_APP_TABLE];\n'
	for i,table in enumerate(data['sql']):
		t = t = jsAppTable(table['table'])
		f += b.replace('[js_APP]',app).replace('[js_APP_TABLE]',t)
	return f

def jsProcessPages(table):
	global sendRecordsPages
	return sendRecordsPages.replace('[funcname]',php_funcname(table))













def jsFieldValUpldateList(app,table,fields,spaces):
	abrev = []
	y = spaces + "try {if ([js_APP].[js_APP_TABLE].records[i].FIELD1 !== $('#[js_APP]_' + i + '_FIELD2').val()){[js_APP].[js_APP_TABLE].listAdd(i);} } catch (err) { }\n"
	b = spaces + "try {[js_APP].[js_APP_TABLE].records[i].FIELD1 = $('#[js_APP]_' + i + '_FIELD2').val();} catch (err) { }\n"
	d = spaces + "try { $('#label_' + i + '_FIELD2').text([js_APP].[js_APP_TABLE].records[i].FIELD1); } catch (err) { }\n"
	f = ''
	label = ''
	processedFields = []
	for field in fields:
		if 'label' in field['field']:
			label = field['field']
		if actionable(field,'del'):
			fx = jsFieldName(table,field['field'])
			processedFields.append(fx)
			f += y.replace('FIELD2',field['field'].title()).replace('FIELD1',fx).replace('[js_APP]',app)
			f += b.replace('FIELD2',field['field'].title()).replace('FIELD1',fx).replace('[js_APP]',app)
			if '_mid' in field['field']:
				pass
			elif '_id' in field['field']:
				pass
			elif 'toggle' in field['note']:
				pass
			else:
				f += d.replace('FIELD2',field['field'].title()).replace('FIELD1',fx).replace('[js_APP]',app)
	# f += b.replace('FIELD2',field['field'].title()).replace('FIELD1',fx).replace('[js_APP]',app)
	x = spaces + 'try {[js_APP].[js_APP_TABLE].records[i].label = '
	if 'label_' in label:
	
		for li in label.replace('label_','').split('_'):
			for pf in processedFields:
				if li in pf and not 'label' in pf:
					x += '[js_APP].[js_APP_TABLE].records[i].' + pf + '+" "+'
		x = _str.cleanBE(x,'+" "+')
	else:
		for pf in processedFields:
			if 'label' in pf:
				x += '[js_APP].[js_APP_TABLE].records[i].' + pf + ''
	x += '; } catch (err) { }\n'
	# _.pr(label,x)
	if len(label) > 0:
		x = x.replace('[js_APP]',app)
		f += x
	# return ''
	return f



















def jsaction(table,fields):
	global jsCrudBase
	crud = jsCrudBase['crud']
	# jsCrudBase['row_plain']
	# jsCrudBase['row_select']

	app = _.switches.value('App')


	crud = crud.replace('[js_APP]',app.lower())
	crud = crud.replace('[js_update_json_field_data_0]',jsFieldVal(app,table,fields,'        '))
	crud = crud.replace('[js_update_json_field_data_1]',jsFieldVal(app,table,fields,'                    '))
	crud = crud.replace('[js_update_json_field_data_2]',jsFieldVal(app,table,fields,'                    '))
	crud = crud.replace('[js_update_json_field_data_3]',jsFieldValToggle(app,table,fields,'                    '))
	crud = crud.replace('[js_VALIDATE]',jsValidateSection(app,table,fields,'                        '))
	crud = crud.replace('[JS_HTML_FIELDS]',jsHTMLFields(fields))
	crud = crud.replace('[js_HTML_ROW_undefined]',jsHTMLUndefined(fields,'            '))
	crud = crud.replace('[js_HTML_ROW]'+_v.slash,jsHTMLROW(jsCrudBase,app,fields))
	# crud = crud.replace('[js_HTML_ROW_null]',jsHTMLNull(app,table,fields,'                '))
	crud = crud.replace('[js_HTML_ROW_null]','')
	crud = crud.replace('[js_HTMLFieldsJSON]',jsHTMLFieldsJSON(app,table,fields))
	crud = crud.replace('[js_add]',jsAdd(app,table,fields))
	crud = crud.replace('[js_HTML_ROW_Default]',jsHTMLDefault(fields,'            '))
	crud = crud.replace('[js_form_Focus]',jsFormFocus(app,fields,'        '))
	crud = crud.replace('[js_form_Blur]',jsFormBlur(app,fields,'            '))
	crud = crud.replace('[js_a_Field]',jsaField(app,fields))
	crud = crud.replace('[js_HTML_ROW_Val]',jsFieldValUpldateList(app,table,fields,'                    '))
	crud = crud.replace('[js_resolveids]',jsResolveIDs(app))
	crud = crud.replace('[js_add_child_div]',jsAddChildDiv(app,table))
	crud = crud.replace('[js_main_app_id]',jsMainAppId(app,table))
	crud = crud.replace('[js_child_manage_function]',jsChildManageFunction(app,table))
	crud = crud.replace('[js_is_child]',jsIsChild(app,table))
	crud = crud.replace('[js_section_label]',jsSectionLable(app,table))
	crud = crud.replace('[js_field_prefix]',jsFieldPrefix(table,fields))
	crud = crud.replace('[js_selectpage_unspecific]',jsSelectPageUn(app,table,fields))

	crud = crud.replace('[js_data_out]',jsDataOut(app))
	crud = crud.replace('[js_data_in]',jsDataIn(app))


	# crud = crud.replace('[js_HTML_ROW_Val_DEL]',jsFieldDel(app))




	crud = crud.replace('[js_APP_TABLE]',jsAppTable(table))
	crud = crud.replace('[js_PHP_FILE_SEND]',jsProcessPages(table))

	return crud









def pagesIndexMenu():
	global pageData
	global data
	app = _.switches.value('App')
	b = '              <li><a onclick="[js_APP].[js_APP_TABLE].manage();">Manage TABLELABEL</a></li>\n'
	f = ''
	for d in data['sql']:
		if not '_items' in d['table']:
			table = jsAppTable(d['table'])
			f += b.replace('[js_APP]',app).replace('[js_APP_TABLE]',table).replace('TABLELABEL',jsSectionLable(app,d['table']))
	return f




# def pages():
#     # global pageData
#     app = _.switches.value('App')
#     # pageData['index']
#     return 

def php_allTablesDownload():
	global data
	global phpCrudBase

	app = _.switches.value('App')
	b = '    $tables["[js_APP_TABLE]"] = the_table_[funcname]();\n'
	f = ''
	for d in data['sql']:
		table = jsAppTable(d['table'])
		ft = php_funcname(d['table'])
		f += b.replace('[js_APP]',app).replace('[js_APP_TABLE]',table).replace('[funcname]',ft)
	return f

def php_allTablesUpload():
	global data
	global phpCrudBase

	app = _.switches.value('App')
	b = '    process_records_[funcname](json_encode($data["[js_APP_TABLE]"]));\n'
	f = ''
	for d in data['sql']:
		table = jsAppTable(d['table'])
		ft = php_funcname(d['table'])
		f += b.replace('[js_APP]',app).replace('[js_APP_TABLE]',table).replace('[funcname]',ft)
	return f

def php_generateProcessPages():
	global data
	global sendRecordsPages
	b = '<?PHP\ninclude("_auto_functions.php");\n// echo $_POST["JSON"];\necho process_records_[funcname]($_POST["JSON"]);\n?>'
	for d in data['sql']:
		table = jsAppTable(d['table'])
		ft = php_funcname(d['table'])
		fileContent = b.replace('[js_APP_TABLE]',table).replace('[funcname]',ft)
		fileName = sendRecordsPages.replace('[js_APP_TABLE]',table).replace('[funcname]',ft)
		_.saveText(fileContent,fileName)

def html_loadData():
	app = _.switches.value('App')
	global data
	f = ''
	b = '        [js_APP].[js_APP_TABLE].records = <? echo json_[funcname](); ?>;\n'
	for i,table in enumerate(data['sql']):
		t = t = jsAppTable(table['table'])
		ft = php_funcname(table['table'])
		f += b.replace('[js_APP]',app).replace('[js_APP_TABLE]',t).replace('[funcname]',ft)
	return f

def action():
	global data
	# phpaction()
	sInput = _.switches.value('Input')
	sApp = _.switches.value('App')
	sPrefix = _.switches.value('Prefix')
	import auditSQL
	_.switches.fieldSet('Input','active',True)
	_.switches.fieldSet('Input','value',sInput)

	_.switches.fieldSet('App','active',True)
	_.switches.fieldSet('App','value',sApp)
	
	_.switches.fieldSet('Prefix','active',True)
	_.switches.fieldSet('Prefix','value',sPrefix)
	data = auditSQL.action()
	# _.pr(__.appReg)
	focus()
	# _.pr(__.appReg)
	
	# _.pr(data)
	# _.pr(data['sql'])



	phpcrud = ''
	jscrud = ''
	for i,table in enumerate(data['sql']):
		# if i == 1:
		jscrud += jsaction(table['table'],table['fields'])
		phpcrud += phpaction(table['table'],table['fields'])

	phpcrud += phpCrudBase['crud_tables_all_download'].replace('[php_all_tables_download]',php_allTablesDownload())
	phpcrud += phpCrudBase['crud_tables_all_upload'].replace('[php_all_tables_upload]',php_allTablesUpload())

	_.saveText('<?PHP\ninclude("_functions.php");\n'+phpcrud+'\n?>','_auto_functions.php')
	_.saveText(jscrud,'_auto_functions.js')
	indexPage = pageData['index'].replace('[html_load_data]',html_loadData()).replace('[html_app_name]',sApp)
	_.saveText(indexPage.replace('[html_menu]',pagesIndexMenu()),'_auto_index.php')
	php_generateProcessPages()


	# for i,table in enumerate(data['sql']):
	#     _.pr()
	#     _.pr(table['table'])
	#     for field in table['fields']:
	#         if actionable(field):
	#             pass
	#             _.pr(field['field'])

			# _.pr('\t',field['field'])
		# _.pr(table['fields'])
		# _.tables.register('fields',table['fields'])
		# _.tables.print('fields','field,type,length,default,note')
			# _.pr(field.keys())

def certFix(crud):
	app = _.switches.value('App')
	crud = crud.replace( 'certificates', app )
	crud = crud.replace( 'certificate', app )
	crud = crud.replace( 'cert', app )
	return crud
data = []
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud.php')
fileContent = ''
for i,c in enumerate(theFile):
	if i > 0:
		fileContent += c
phpCrudBase = {}
phpCrudBase['crud'] = fileContent
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_toggle.php')
fileContent = ''
for i,c in enumerate(theFile):
	if i > 0:
		fileContent += c
phpCrudBase['crud_toggle'] = fileContent
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_joins.php')
fileContent = ''
for i,c in enumerate(theFile):
	if i > 0:
		fileContent += c
phpCrudBase['crud_joins'] = fileContent
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_tables.php')
fileContent = ''
for i,c in enumerate(theFile):
	if i > 0:
		fileContent += c
phpCrudBase['crud_tables'] = fileContent
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_tables_all_download.php')
fileContent = ''
for i,c in enumerate(theFile):
	if i > 0:
		fileContent += c
phpCrudBase['crud_tables_all_download'] = fileContent
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_tables_all_upload.php')
fileContent = ''
for i,c in enumerate(theFile):
	if i > 0:
		fileContent += c
phpCrudBase['crud_tables_all_upload'] = fileContent
##########################
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase = {}
jsCrudBase['crud'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_HTML_ROW.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['row_plain'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_HTML_ROW_Pull_Down.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['row_select'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_HTML_ROW_Hidden.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['row_hidden'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_HTML_ROW_Toggle.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['row_toggle'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_HTML_ROW_MORE_.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['more_button'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_HTML_ROW_MORE_CLOSE_.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['more_close'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_manage_children.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['manage_children'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_resolveids.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['resolveids'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_selectpage_unspecific_no_group.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['selectpage_unspecific_no_group'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_selectpage_unspecific_has_group.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsCrudBase['selectpage_unspecific_has_group'] = certFix(fileContent)
##########################
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_validate_email.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsValidate = {}
jsValidate['email'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_validate_text.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsValidate['text'] = certFix(fileContent)
##########################
theFile = _.getText(_v.webapp + _v.slash+'crud_validate_int.js')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
jsValidate['int'] = certFix(fileContent)
##########################
##########################
theFile = _.getText(_v.webapp + _v.slash+'index.php')
fileContent = ''
for i,c in enumerate(theFile):
	fileContent += c
pageData = {}
pageData['index'] = fileContent
##########################
functions = []
sendRecordsPages = 'process[funcname].php'


########################################################################################
if __name__ == '__main__':
	action()