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
	_.switches.register( 'Dump-Types', '-dump' )
	_.switches.register( 'Type', '-t,-type' )
	_.switches.register( 'Clip', '-clip' )
	_.switches.register( 'Form-id', '-f.id' )
	_.switches.register( 'Form-label', '-f.label' )
	_.switches.register( 'Form-class', '-f.class' )
	_.switches.register( 'Form-name', '-f.name' )
	_.switches.register( 'Form-iter', '-f.iter' )
	_.switches.register( 'Form-iter.n', '-f.iter.n' )
	_.switches.register( 'Form-iter.v', '-f.iter.v' )
	pass

#       finds the file in probable locations
#       and 
#               if  _.autoBackupData = True
#               and __.releaseAcquiredData = True
#                       GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#               you can run apps on usb at a clients office
#                       when you get home run: p app -loadepoch epoch 
#                               backed up
#                                       pipe
#                                       files
#                                       tables
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
	'file': 'html-form.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'generate html form',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'form',
						'fields',
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
						_.hp('p html-form '),
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
	# _.switches.trigger( 'Files',_.inRelevantFolder )      
	
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
#       if os.path.isdir( row ):
#       if os.path.isfile( row ):
#       os.path.abspath(path)
#                                                                                                       if platform.system() == 'Windows':
########################################################################################
# START


def lements(_type):
	global elements
	if _type is None:
		return None

	for k in elements:
		if _type in elements[k]:
			return elements[k][_type]

	return None


# def process(_type=None, _name=None, _label=None, _id=None,_class=None,_iter=None,_iter_dic=None):
def process(dic):


	_type=''
	_name=''
	_label=''
	_class=''
	_iter=None
	_iter_dic=None
	if 'name' in dic: _name=dic['name'];
	_id=id_pre()+'-'+_name

	if 'type' in dic: _type=dic['type'];
	if 'label' in dic: _label=dic['label'];
	if 'id' in dic: _id=_id+'-'+dic['id'];
	if 'class' in dic: _class=dic['class'];
	if 'itter' in dic: _iter=dic['itter'];
	if 'itter-dic' in dic: _iter_dic=dic['itter-dic'];



	field = lements(_type)
	if field is None:
		_.e('bad type')
	pass
	if '_iter_n_' in field and _iter_dic:
		d=_iter_dic
		new=[]
		for line in field.split('\n'):
			if not '_iter_n_' in line:
				new.append(line)
			else:
				for k in d:
					l=line.replace('_iter_n_',k)
					l=l.replace('_iter_v_',d[k])
					new.append(l)
	if '_iter_' in field and _iter:
		d=_iter
		new=[]
		for line in field.split('\n'):
			if not '_iter_' in line:
				new.append(line)
			else:
				for k in d:
					l=line.replace('_iter_',k)
					new.append(l)
					
		field='\n'.join(new)


	field = field.replace( '_id_', _id )
	field = field.replace( '_class_', _class )
	field = field.replace( '_type_', _type )
	field = field.replace( '_name_', _name )
	field = field.replace( '_label_', _label )
	return field
	# _.pr(field)
					


def id_pre():
	a = random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	b = random.choice(list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	c = random.choice(list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	d = random.choice(list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	return a+b+c+d

html='''<!DOCTYPE html>
<html lang="en-US">

<head>
		<title>title</title>
		<meta charset="utf-8">
		<!-- <META http-equiv="refresh" content="1;URL=/?"> -->

		<link rel="stylesheet" href="https://eyeformeta.com/assets/forms/fields/default.css">
		
</head>

<body>
<form>
HERE
</form>
		<!-- -->
</body>

</html>'''

def action():
	global html
	load()
	fields = []
	if _.switches.isActive('Dump-Types'):
		dumpTypes()
		return None


	if _.isData():
		if _.isData()[0].replace(' ','').replace('\t','').replace('\r','').replace('\n','').startswith('{'):
			for item in _.isData():
				pro=process(  simplejson.loads(item)  )
				fields.append(pro)

			_.pr( html.replace('HERE', '\n'.join(fields) ) )
			return None



	_type=None
	_name=None
	_label=None
	_id=None
	_class=None
	_iter=None
	_iter_dic=None
	# if _.switches.isActive('Type'):

	_type='text'
	_name='tester'
	_label='my field'
	_id='2F-'+_name
	_class=_name

	_iter=None
	_iter_dic=None



	dic = {
				'type': _type,
				'name': _name,
				'label': _label,
				'id': _id,
				'class': _class,
				# 'itter': [],
				# 'itter-dic': {},
	}

	# _.pr( simplejson.dumps(dic) )

	process(dic)
	# process(_type=_type,_name=_name,_label=_label,_id=_id,_class=_class,_iter=_iter,_iter_dic=_iter_dic)


	

def dumpTypes():
	global elements

	for k in elements:
		_.pr()
		for _type in elements[k]:
			_.pr( _type )


def load():
	global elements
	url='https://eyeformeta.com/assets/forms/fields/dic.php'
	page=str(requests.post(url, data = {'test':'sample'}).content,'iso-8859-1')
	elements = simplejson.loads(page)
	# _.pv(elements)
	# _.e(9)
# assets
# binary
# checkbox
# date
# radio
# range
# select


requests = __.imp('requests')
simplejson = __.imp('simplejson')
random = __.imp('random')


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()