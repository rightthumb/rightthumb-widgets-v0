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
##################################################
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
	_.switches.register( 'Test', '-t,-test' )
	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	### EXAMPLE: END

#   finds the file in probable locations
#   and 
#       if  _.autoBackupData = True
#       and __.releaseAcquiredData = True
#           GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#       you can run apps on usb at a clients office
#           when you get home run: p app -loadepoch epoch 
#               backed up
#                   pipe
#                   files
#                   tables
_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	# 'app': '7facG-jo0Cxk',
	'file': 'pipe-dic.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'attempts to convert cmd to table',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						'dir | p pipe-dic | p json-pipe-table',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('dir | p pipe-dic | p json-pipe-table'),
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
	### EXAMPLE: START
	# _.default_switch_trigger('Plus', trigger_plus)
	# _.switches.trigger( 'Files',_.inRelevantFolder )  
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
#   os.path.abspath(path)
#                                                   if platform.system() == 'Windows':
########################################################################################
# START


def indexer():
	global index
	global tabs
	if index: return tabs;
	xam=0

	l=len( _.isData() )
	quotient = 1 / 1.1
	percent = quotient * l
	for ii,row in enumerate( _.isData(r=1) ):
		for i, ch in enumerate(list(row)):
			if i > xam:
				xam=i
			if ch == ' ':
				if not i in index:
					index[i]=0
				index[i]+=1

	i=0
	ii=0
	text=''
	while not ii == xam:
		ii+=1
		i+=1
		if i == 10:
			i=0
		t=str(i)
		# if ii in index:
		#   t='a'
		if ii in index and index[ii] > percent:
			tabs.append(ii)
			# t=_.cp(t,'red',p=0)
		text+=t
	# _.pr(text)
	global fields
	for ii,line in enumerate( _.isData(r=1) ):
		tes=ltest(line)
		if tes > fields:
			fields=tes

	return tabs

def test():
	global index
	indexer()

	pass
	l=len( _.isData() )
	quotient = 1 / 1.1
	percent = quotient * l
	# _.pr(percent)
	# sys.exit()
	# percent = quotient * 100
	pass



	# i=0
	# ii=0
	# text=''
	# while not ii == xam:
	#   ii+=1
	#   i+=1
	#   if i == 10:
	#       i=0
	#   if i == 0:
	#       text+=str(  _.cp(i,'red',p=0)  )
	#   elif i == 5:
	#       text+=str(  _.cp(i,'green',p=0)  )
	#   else:
	#       text+=str(i)
	# _.pr(text)



	i=0
	ii=0
	text=''
	while not ii == xam:
		ii+=1
		i+=1
		if i == 10:
			i=0
		t=str(i)
		# if ii in index:
		#   t='a'
		if ii in index and index[ii] > percent:
			t=_.cp(t,'red',p=0)
		text+=t
	_.pr(text)


	i=0
	ii=0
	text=''
	tens=0
	while not ii == xam:
		ii+=1
		i+=1
		if i == 10:
			tens+=1
			# text+=str(  _.cp(tens,'red',p=0)  )
			text+=str(  tens  )
			i=0
		else:
			text+=' '
	_.pr(text)

def ltest(line):
	tabs=indexer()
	fields=0
	for i,c in enumerate(line):
		if c == ' ' and i in tabs:
			fields+=1
	return fields

def fieldsa(line):
	tabs=indexer()
	fields=0
	lastspace=False
	text=''
	fie=[]
	for i,c in enumerate(line):

		
		# if not c == ' ' and lastspace:
		# if not c == ' ':

		if c == ' ' and not i in tabs and lastspace:
			lastspace=False
			if not text:
				fie.append('')

		if c == ' ' and i in tabs and not lastspace:
			lastspace=True
			fie.append(text)
			text=''

		if not c == ' ' or not i in tabs:
			text+=c

		if not c == ' ': lastspace=False;
		if c == ' ' and i in tabs: lastspace=True;
	if len(text):
		fie.append(text)
	return fie

label_dex={}
def labeler(stri):
	stri=_str.do('be',stri,' ')
	def la(label):
		global label_dex
		if label in label_dex:
			label_dex[label]+=1
			return label+'-'+str(label_dex[label]);

		elif not label in label_dex: label_dex[label]=1; return label;

	global label_dex

	isFile=False
	isFolder=False
	# _.pr(stri)
	try:
		if os.path.isfile(stri):
			isFile=True
	except Exception as e:
		pass

	try:
		if os.path.isdir(stri):
			isFolder=True
	except Exception as e:
		pass
	if isFile: return la('file');
	elif isFolder: return la('folder');
	elif stri.count('/') == 2 or stri.count('-') == 2: return la('date');
	elif stri.count(':'): return la('time');
	elif stri.upper() == 'AM' or stri.upper() == 'PM': return la('xM');

	if not stri: return '-';

	isNumb=True
	for c in stri:
		if not c in '0123456789.,': isNumb=False;

	if isNumb: return la('num');

	return la('na');


def labelee(fie):
	global field_list
	l=labeler(fie)
	if not l in field_list:
		field_list.append(l)
	return l


def dicer(line):
	global label_dex
	global field_list
	label_dex={}
	dic={}
	for fie in fieldsa(line):
		# _.pr(fie)
		l=labelee(fie)
		if not l == '-':
			dic[l]=_str.do('be',fie,' ')
	
	for k in field_list:
		if not k in dic and not k == '-':
			dic[k]=''
	if 'date' in dic and 'time' in dic and 'xM' in dic:
		epoch=_.isDate( _.isDate(dic['date'],f='date') +' '+ dic['time'] +' '+ dic['xM'], f='epoch' )
		del dic['time']
		del dic['xM']
		dic['date']=_.isDate(epoch,f='text-datetime')
		dic['epoch']=int(epoch)
	elif 'date' in dic and 'time' in dic and 'xM' in dic:
		epoch=_.isDate( _.isDate(dic['date'],'date') +' '+ dic['time'] , f='epoch' )
		del dic['time']
		dic['date']=_.isDate(epoch,f='text-datetime')
		dic['epoch']=int(epoch)

	if 'file' in dic:
		if dic['file']:
			if _.switches.isActive('Column'):
				import _rightThumb._dir as _dir
				info=_dir.info(dic['file'])
				for c in _.switches.values('Column'):
					found=False
					for k in info:
						if c == k:
							found=True
							dic[k]=info[k]
							if not k in field_list: field_list.append(k);
					if not found:
						for k in info:
							if k.startswith(c):
								found=True
								dic[k]=info[k]
								if not k in field_list: field_list.append(k);
		dic['path']=os.path.abspath(dic['file'])
		dic['name']=dic['file']
		del dic['file']


	if 'folder' in dic:
		if dic['folder']:
			dic['name']=dic['folder']
			dic['path']=os.path.abspath(dic['folder'])+os.sep
		del dic['folder']
	return dic



def process():
	global fields
	tabs=indexer()
	for ii,line in enumerate( _.isData(r=1) ):
		te=ltest(line)
		if te == fields:
			fi=dicer(line)
	records = []
	for ii,line in enumerate( _.isData(r=1) ):
		te=ltest(line)
		if te == fields:
			fi=dicer(line)
			records.append(fi)
			# _.pv(fi)
				# _.pr('fie',fie)
	return records



def action():
	#--> min, architecture {:strict:}
	if _.switches.isActive('Test'): test(); return None;

	records=process()

	_.pv(records)
	# _.tables.register( 'data', records )
	# _.tables.print( 'data', ','.join(records[0]) )


	# _.pv(index)


index={}
tabs=[]
fields=0
field_list=[]



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()