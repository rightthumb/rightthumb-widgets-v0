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
# import platform
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
	_.switches.register( 'Index', '-index' )
	_.switches.register( 'Files', '-f,-file,-files' )
	_.switches.register( 'Folders', '-folder,-folders' )
	
	_.switches.register( 'Create', '-add,-create,-ad' )
	_.switches.register( 'Read', '-read' )
	_.switches.register( 'Update', '-update' )
	_.switches.register( 'Delete', '-del,-delete,-remove' )
	
	_.switches.register( 'Edit', '-edit' )
	_.switches.register( 'Test', '-test' )

	_.switches.register( 'Drive', '-drive' )
	
	_.switches.register( 'Selection', '-selection' )
	_.switches.register( 'Select', '-select' )
	_.switches.register( 'Unselect', '-unselect' )

	_.switches.register( 'Library', '-lib,-library' )

	_.switches.register( 'ID', '-id' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'meta.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'manage file and folder meta data',
	'categories': [
						'meta',
						'file',
						'folder',
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
						'p meta -folder -add -test',
						'',
						'p meta -drive e',
						'p meta -drive f',
						'',
						'p meta -folder -add folder.servers.ftp',
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
	_.switches.trigger( 'Folders', _.myFolderLocations )
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

def timeKey():
	time.sleep(.01)
	n = int(str(time.time()).replace('.',''))
	_nID.mini.password( _v.unixIDs[ random.randint(0,9) ] )
	x = _nID.mini.gen( n )
	while len(x) < 10:
		n = int(str(time.time()).replace('.',''))
		x = _nID.mini.gen( n )
	return x

def genKey(path=None):
	if path is None:
		pKey = _v.genUUID('key')
	else:
		pKey = _md5.md5( _v.cloud_path(path) )
	pKey += '-'
	pKey += timeKey()
	key=''

	for i,x in enumerate(pKey):
		if i < 49:
			key+=x
	return key



def build( path, typ=None, ask=False ):
	global subjectConfiguration
	v = _.dicString( 'subjectConfiguration', path )
	if not ask:
		y = []
		try:
			v += ' = {}'
			exec(v)
		except Exception as e:
			for x in path.split('.'):
				y.append(x)
				v = _.dicString( 'subjectConfiguration', '.'.join(y) )
				v += ' = {}'
				# _.pr(v)
				exec(v)


	else:
		# _.colorThis( typ, 'white' )
		if typ == 'list':
			try:

				if len(eval(v)):
					alreadyExists = True
				else:
					alreadyExists = False
			except Exception as e:
				alreadyExists = False
			if not alreadyExists:
				# field = input( typ+'\t'+path+': ' )
				exec( v + ' = []' )
			if 1:
				done = False
				new = []
				while not done:
					_.pr()
					_.pr('List Manager')
					_.pr('___________________________________________')
					_.pr(path)
					_.pr()
					for i,x in enumerate( eval(v) ):
						_.pr( i, x )
					_.pr()
					_.pr( 'Example: del:0,3  OR  edit:0,6  OR  add:item  OR  x' )
					command=''
					command = input( ' ? : ' )
					if 'del:' in command:
						do = 'del'
					elif 'edit:' in command:
						do = 'edit'
					elif 'add' in command:
						do = 'add'
					elif 'x' in command:
						done = True
					if not done:
						if do == 'add':
							new.append( _str.cleanBE( command.split(':')[1], ' ' ) )
						else:
							aL = []
							for u in command.split(':')[1].split(','):
								u = row = _str.cleanBE( u, ' ' )
								if len(u):
									aL.append(int(u))
							newX = []
							for ii,xyz in enumerate(eval(v)):
								if do == 'del' and ii in aL:
									_.pr( 'deleted: ', xyz)
								else:
									if do == 'edit' and ii in aL:
										_.pr(xyz)
										xyz=input( ' edit: ' )
									newX.append( xyz )
								# _.pr('eor')
							new = newX
							# _.pr('eol')
						# _.pr('eoDO')
					# _.pr('eoWHILE')
				
					exec( v +' = new' )
				# _.pr('eoALL')
				_.pr(  )
				_.pr( 'done' )
				_.pr('___________________________________________')


		elif not typ == 'list':
			field = input( typ+' |\t'+path+': ' )
			if typ == 'bool':
				if 'y' in field.lower():
					field = 'True'
				elif 't' in field.lower():
					field = 'True'
				elif '1' in field.lower():
					field = 'True'
				else:
					field = 'False'
			elif typ == 'int':
				pass
			elif typ == 'str':
				if path.endswith('.password'):
					field = _blowfish.encrypt( field, _vault.key() )
				field = '"""'+field+'"""'
			v += ' = ' + field
			exec( v )
	# _.pr( v )


def build_labels( path ):
	global THE_LABELS

	done = False
	while not done:
		if 'LABEL' in path:
			test = path.split('LABEL')[0]
			if test in THE_LABELS:
				path = path.replace('LABEL', THE_LABELS[test], 1)
			elif not test in THE_LABELS:
				# _.pr( test )
				THE_LABELS[test] = input( ' Label: ' )
			

		if not 'LABEL' in path:
			done=True
	return path

def index_dic(metaData, pFix=''):
	# _.pr(metaData,pFix)
	# sys.exit()
	if len(pFix):
		pFix = pFix+'.'
	global subjectConfiguration
	global THE_LABELS
	
	THE_LABELS = {}
	_.traverse( metaData )
	# _.printVarSimple( _.traverse_dic_research )
	fields = []
	dics = []
	for t in _.traverse_dic_research['type']:
		_.colorThis( ['\t',t], 'white' )
		for f in _.traverse_dic_research['type'][t]:
			ff = f.replace( '-i-', 'i' )
			_.colorThis( ['\t\t',pFix+ff], 'cyan' )
			if t == 'dict':
				dics.append( ff )
			else:
				fields.append({ 'type': t, 'path': ff })
	dics.sort()
	# fields.sort()
	_.pr(  )
	for field in dics:
		# yy = field.replace('LABEL', label, 1)
		while True:
			try:
				yy = build_labels( pFix+field )
				break
			except Exception as e:
				_.pr(e)

		# _.colorThis( ['\t',yy], 'yellow' )
		while True:
			try:
				build( yy )
				break
			except Exception as e:
				_.pr(e)

	_.pr(  )
	_.pr(  )
	for field in fields:
		# field['path'] = field['path'].replace('LABEL', label, 1)
		while True:
			try:
				field['path'] = build_labels( pFix+field['path'] )
				break
			except Exception as e:
				_.pr(e)
		while True:
			try:
				build( field['path'], field['type'], True )
				break
			except Exception as e:
				_.pr(e)
		# _.colorThis( ['\t',field], 'cyan' )

	return subjectConfiguration
	
			# traverse_obj( data[key], config, np, npi )
subjectConfiguration = {}
def folder_add(folder):
	global cp
	global category
	global itemID
	pFix = _.switches.values('Create')[0]
	v = _.dicString( '_.nc.meta.meta', pFix )
	subjectMeta = index_dic( eval(v),  pFix)
	_.nc.meta.locations['i'][category][cp] = subjectMeta
	_.saveTableProject(    '_.nc.meta.meta.folder.settings', _.nc.meta.locations['i'][category][cp], itemID   )
	_.printVarSimple( subjectMeta )


def category_action( item, category, do ):
	if category == 'folder' and do == 'create':
		folder_add( item )

def proces_folder( folder, label ):
	metaTablePaths = _.getTable('meta-folder-paths.hash')
	metaTableIDs = _.getTable('meta-folder-ids.hash')
	fL = '.folder-meta'
	if folder.endswith( _v.slash ):
		savePath = folder+fL
	else:
		savePath = folder+_v.slash+fL

	if os.path.isfile( savePath ):
		folderMeta = _.getTable2( savePath )
		folderID = folderMeta['id']
	else:
		folderID = genKey( folder )
		metaTablePaths[folder] = folderID
		metaTableIDs[folderID] = folder
		_.saveTable( metaTablePaths, 'meta-folder-paths.hash' )
		_.saveTable( metaTableIDs, 'meta-folder-ids.hash' )


def proces_drive( drive ):

	fL = '.drive-meta'
	if not drive.endswith( _v.slash ):
		drive += _v.slash


	savePath = drive

	if savePath == '/':
		savePath = '/opt/RightThumb/'


	from _rightThumb._drive import classic as _drive

	if os.path.isfile( savePath + fL ):
		driveMeta = _.getTable2( savePath + fL )
		driveID = driveMeta['id']


	else:
		driveID = genKey( drive )
		if _.isWin:
			driveMeta = _drive.Documentation_Initial( drive[0] )
		else:
			driveMeta = _drive.Documentation_Initial( drive )
		driveMeta.id = driveID
		driveMeta.unixID = _v.unixID
		driveMeta.host = _v.host_alias
		driveMeta.epoch = time.time()
		driveMeta.date = _.friendlyDate( driveMeta.epoch )

		try:
			del driveMeta.descriptorID
		except Exception as e:
			pass

		try:
			del driveMeta.descriptorLoop
		except Exception as e:
			pass

		try:
			del driveMeta.save
		except Exception as e:
			pass

		try:
			del driveMeta.driveSizeLabel
		except Exception as e:
			pass



		_.saveTableProject( 'drive.registration.'+driveID,    driveMeta.__dict__,    'drive.hash' )
		_.saveTable2(  driveMeta.__dict__, savePath + fL  )
		driveMetaIndex = _.getTableDB( 'drives.index' )
		driveMetaIndex[driveMeta.id] = driveMeta.__dict__
		driveMeta = driveMeta.__dict__
		_.saveTableDB( driveMetaIndex, 'drives.index' )
		if _.isWin:
			os.system('attrib +h +s ' + savePath + fL)

	if _.isWin:
		driveMetaUpdate = _drive.volumeSizeInfo( drive[0] )
	else:
		driveMetaUpdate = _drive.volumeSizeInfo( drive )

	_.saveTableProject( 'drive.volume-update.'+driveID,    driveMetaUpdate,    str(time.time())+'.hash' )
	_.saveTableProject( 'drive.last.'+driveID,    driveMetaUpdate,    'volume.hash' )

	# _.pr( driveID )
	# _.pr( driveMeta.__dict__ )
	_.printVarSimple( driveMeta )





def action():
	load()
	global cp
	global itemID
	global category
	global subjectConfiguration
	

	done = False
	# if False:
	if _.switches.isActive('Folders') and _.switches.isActive('ID'):
		done = True
		for folder in _.switches.values('Folders'):
			if _.isWin and len(folder) == 1:
				folder += ':'+_v.slash
			if os.path.isdir( folder ):
				proces_folder( folder )
				# proces_drive( folder )

	if _.switches.isActive('Files') and _.switches.isActive('Library'):
		done = True
		library_label = _.getTableDB( 'library-label.hash' )
		library_path = _.getTableDB( 'library-path.hash' )
		library_id = _.getTableDB( 'library-id.hash' )
		for x in _.switches.values('Library'):
			p = os.path.abspath( _.switches.values('Files')[0] )
			k = genKey(cp)
			library_label[x] =         { 'id': k, 'path': p, 'label': x }
			library_path[p] =         { 'id': k, 'path': p, 'label': x }
			library_id[k] =         { 'id': k, 'path': p, 'label': x }

		_.saveTableDB( library_label, 'library-label.hash' )
		_.saveTableDB( library_path, 'library-path.hash' )
		_.saveTableDB( library_id, 'library-id.hash' )


	elif _.switches.isActive('Selection'):
		done = True
		selection = _.getTable( _.nc.tables.select )
		_.printVarSimple( selection )

	elif _.switches.isActive('Select'):
		done = True
		selection = _.getTable( _.nc.tables.select )
		for x in _.switches.values('Select'):
			path = os.path.abspath( x )
			selection[ path ] = 0
			_.colorThis( path, 'green' )
		_.saveTable( selection, _.nc.tables.select, p=0 )

	elif _.switches.isActive('Unselect'):
		done = True
		selection = _.getTable( _.nc.tables.select )
		for x in _.switches.values('Unselect'):
			path = os.path.abspath( x )
			if path in selection:
				_.colorThis( path, 'green' )
				del selection[path]
			else:
				_.colorThis( path, 'red' )
		_.saveTable( selection, _.nc.tables.select, p=0 )

	elif _.switches.isActive('Drive'):
		done = True
		for drive in _.switches.values('Drive'):
			if _.isWin and len(drive) == 1:
				drive += ':'+_v.slash
			if os.path.isdir( drive ):
				proces_drive( drive )
			

	elif _.switches.isActive('Index'):
		done = True
		_.traverse(_.nc.meta.meta)
		fields = []
		dics = []
		for t in _.traverse_dic_research['type']:
			_.colorThis( ['\t',t], 'white' )
			for f in _.traverse_dic_research['type'][t]:
				ff = f.replace( '-i-', 'i' )
				_.colorThis( ['\t\t',ff], 'cyan' )
	if not done:
		category = 'Error'
		if _.switches.isActive('Files'):
			category = 'file'
			subject = _.switches.values('Files')
		elif _.switches.isActive('Folders'):
			category = 'folder'
			if not len( _.switches.value('Folders') ):
				subject = [os.getcwd()]
			else:
				subject = _.switches.values('Folders')
		_.nc.meta.locations['i']['category'] = _.getTableProject(    'meta.'+category, 'meta.index'    )
		for item in subject:
			cp = _v.cloud_path(item)
			_.nc.meta.locations['i'][cp] = {}
			if cp in _.nc.meta.locations['i'][category]:
				itemID = _.nc.meta.locations['i'][category][cp]
				_.nc.meta.locations['i'][category][cp] = _.getTableProject(    'meta.'+category+'.settings', itemID    )
			else:
				itemID = genKey(cp)
				_.nc.meta.locations['i'][category][cp] = itemID
				_.saveTableProject(    'meta.'+category, _.nc.meta.locations['i'][category], 'meta.index'    )

			subjectConfiguration = _.nc.meta.locations['i'][cp]
			do = 'create'
			if _.switches.isActive('Create'):
				do = 'create'
			elif _.switches.isActive('Read'):
				do = 'read'
			elif _.switches.isActive('Update'):
				do = 'update'
			elif _.switches.isActive('Delete'):
				do = 'delete'

			category_action( item, category, do )    

			if _.switches.isActive('Test'):
				i=0
				while i < 100:
					k = genKey(cp)
					_.pr( k, len(k) )




category = None
cp = None



itemID = None



def load():
	_.nc.child( 'tables , meta' )
	_.nc.tables.select = 'meta-select.hash'
	_.nc.tables.uploaded = 'meta-uploaded.hash'

	_.nc.meta.locations = {
							'i': {},
							'l': {},
						}
	_.nc.meta.documentation = {
									'settings': {
										'server': {
											'omit': {},
											'dependencies': {},
										},
									},
								}
	_.nc.meta.meta = {

							'account': {
								'LABEL': {
									'client':            False,
								},
							},


							'folder': {


								'servers': {
									'cPanel': {
										'account': {
											'LABEL': {
												'client':            False,
												'ssh': {
													'server':        '',
													'user':            '',
													'password':        '',
												},
												'db': {
													'server':        '',
													'user':            '',
													'password':        '',
													'db':            '',
													'prefix':        '',
												},
												'sync': {
													'upload': False,
													'download': False,
													'delay': 120,
												},
												'path':        '',
											},
										},
									},

									'ftp': {
										'account': {
											'LABEL': {
												'server':        '',
												'user':            '',
												'password':        '',
												'path':            '',
												'full-path':            '',
											},
										},

									},




								},


							},



						# possibly add path with label to have default values



							'file': {},


							'groups': [],



						}





	for x in _.nc.meta.meta:
		_.nc.meta.locations['i'][x] = {}


THE_LABELS = {}
import _rightThumb._md5 as _md5
import _rightThumb._nID as _nID
import random
import _rightThumb._vault as _vault
import _rightThumb._encryptString as _blowfish
# _blowfish.encrypt( xxxx, _vault.imp.key() )



"""
TODO
	
	.thumb-meta
	.thumb-meta-id















del D:\tech\programs\databank\tables\drives.index
attrib -h d:\.thumb-meta
attrib -h c:\.thumb-meta
attrib -s d:\.thumb-meta
attrib -s c:\.thumb-meta
del d:\.thumb-meta
del c:\.thumb-meta



n D:\tech\programs\databank\tables\drives.index


p meta -drive c d



I'M TALKING TO YOU!!
??

"""
__.print_path = True

########################################################################################
if __name__ == '__main__':
	action()