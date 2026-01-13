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
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;

def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################

def sw():
	pass
	_.switches.register( 'Keys', '-keys' )
	_.switches.register( 'Key', '-key', 'actions' )
	_.switches.register( 'FormatActions', '-a,-fa,-actions' )
	# _.switches.register( 'ReStructure', '-r,-restructure,-str,-structure' )
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	# _.switches.register( 'Files', '-f,-fi,-file,-files' )
	### EXAMPLE: END
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])

_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'wt.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Search the windows terminal settings config file',
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
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p wt'),
						_.hp('p wt -key actions'),
						_.hp('p wt -key actions + index'),
						_.hp('p wt -key actions + ctrl+shift+'),
						_.hp('p wt -key profiles'),
						_.hp('p wt -key profiles + bat'),
						_.hp('p wt -key profiles + ssh'),
						_.linePrint(label='simple',p=0),
						_.hp('Setup:'),
						_.hp(_v.home+os.sep+'.config.hash'),
						_.hp('add key "wt" and add path to settings.json file'),
						_.linePrint(label='simple',p=0),
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

def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )
_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
### EXAMPLE: START
	#--> make hotkey ad-description soon:  <--<w#
	#-->    - outer most typed first
	#-->    - blank pipe
	#-->    __.setting('hotkey-clip.ad_description-start1',d=False)
	#--> _________________________________
	#--> describe selection area two
	#--> 3 write a note here wrap text
	#--> two dignissim
	#--> 1 inceptos
	#--> _________________________________
	#--> describe selection area two
	#-->              |           |
	#-->              |           | - write a note here
	#-->              |           |   wrap text
	#-->              |           |
	#-->              |           | - dignissim
	#-->              |
	#-->              | - inceptos
	# if _.switches.isActive('Test'): test(); return None;
	# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
	# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
	#--> a=(1 if True else 0) <--# 
	#--> m=[[row[i] for row in matrix] for i in range(4)]
	# requests=__.imp('requests.post')
	# data=str(requests.post(url,data={}).content,'iso-8859-1')
	# for k in globals(): print(k, eval(k) )
### EXAMPLE: END

########################################################################################
# START


import _rightThumb._string as _str

def reorder_keys(data):
	has=False
	if type(data) == list:
		ndata = []
		for item in data:
			if 'command' in item and 'keys' in item:
				has=True
				new = {}
				new['keys'] = item['keys']
				new['command'] = item['command']
				for key in item:
					if not key in 'keys,command'.split(','): new[key] = item[key]
				ndata.append(new)
			else:
				ndata.append(item)
	if has: return ndata
	return data
def wt_implode(text):
	# text = text.replace('\n',', ')
	text = text.replace('\r','')
	text=_str.replaceDuplicate( text, ' ' )
	try:
		if '{ "keys":' in text and '"command":' in text:
			text = text.replace('[','')
			text = text.replace(']','')
			text = text.replace('{ "keys":','\n{ "keys":')
			text = text.replace(' } }, ',' } }')
			lines = text.split('\n')
			lines.sort()
			lines.reverse()
			for i,line in enumerate(lines):
				line=line.strip()
				if i and line:
					lines[i] = line+','
			lines.reverse()
			text = '['
			text += '\n,'.join(lines)
			text += '\n]'
			text = text.replace('\n,','\n')
			text = text.replace(', ,',',')
			text = text.replace(',,',',')
			text = text.replace('}{ "command":','},\n{ "command":')
	except Exception as e:
		_.pr('err',e)
	return text
def implode(text):
	text=_str.replaceDuplicate( text, '\n' )
	text=_str.cleanBE( text, '\n' )
	text=_str.cleanBE( text, '\t' )
	text=_str.cleanBE( text, ' ' )
	text = text.replace('\r','')

	text=_str.cleanBE( text, '\n' )
	text=_str.cleanBE( text, '\t' )
	text=_str.cleanBE( text, ' ' )
	text=_str.cleanBE( text, '\n' )
	text=_str.cleanBE( text, '\t' )
	text=_str.cleanBE( text, ' ' )
	if text.startswith('{') or text.startswith('['):
		try:
			data = simplejson.loads(text)
		except Exception as e:
			try:
				data = eval(text.replace('false','False').replace('true','True'))
			except Exception as e:
				_.pr(e)
		data = reorder_keys(data)
		result = simplejson.dumps(data, sort_keys=False)
		result=result.replace('{','{ ').replace('}',' }')
		return wt_implode(result)

def colorize(lines):
	newLines = []
	for line in lines:
		if _.showLine(line):
			for plusSearchX in _.switches.values('Plus'):
				plusSearchX = _.ci( plusSearchX )
				for subject in _.caseUnspecificCode( line, plusSearchX ):
					line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )
			newLines.append(line)
	return newLines

def action():

	if _.switches.isActive('Keys'):
		from vs import build_key_to_execution
		raw = build_key_to_execution()

		recs = []

		for key in raw:
			if 'sendInput' in str(raw[key]):
				k = raw[key]['keys']
				v = raw[key]['command']['input']
				recs.append( { 'keys': k, 'input': v } )
		_.switches.fieldSet( 'Long', 'active', True )
		_.pt(recs)
		return



	load()
	global c3po
	global r2d2



	if _.switches.isActive('FormatActions'):
		r2d2 = implode(r2d2)
		lines = r2d2.split('\n')
		
		if not _.switches.isActive('Plus'):
			_.printVarSimpleFake( r2d2 )
		else:
			json = simplejson.loads(r2d2)
			recs = []
			for rec in json:
				if _.showLine(str(rec)):
					recs.append( simplejson.dumps(rec) )		
			
			lines = colorize(recs)
			for line in lines:
				print(line)


				
		return r2d2

	#--> min, architecture {:strict:}
	#--> trigger/callback  <w#
	#--> todo#> meta to scan for
	if len(_.switches.all())==0:
		for x in c3po.keys(): print(x)
		return None
	if _.switches.isActive('Key'):
		table=[]
		key = _.switches.value('Key')
		if key == 'actions':
			# for rec in c3po[  key  ]: print(rec)
			for i,rec in enumerate(c3po[  key  ]):

				if 'keys' in rec: reco = { 'i':i, 'keys': rec['keys'], 'command': rec['command'] }
				else:             reco = { 'i':i, 'keys': '', 'command': '' }
				if _.showLine(str(reco)): table.append(reco)
			_.pt(table)
		elif key == 'profiles':
			for i,rec in enumerate(c3po[  key  ]['list']):
				if 'commandline' in rec: reco = { 'i':i, 'name': rec['name'], 'commandline': rec['commandline'] }
				else:                    reco = { 'i':i, 'name': rec['name'], 'commandline': '' }
				if _.showLine(str(reco)): table.append(reco)
			_.pt(table)
		else:
			_.pr(c3po[  key  ], json=True)
			# for rec in c3po[  key  ]: print(rec)

		pass


def load():
	_.switches.fieldSet( 'Long', 'active', True )
	global c3po
	global r2d2
	text = _.getText( _v.config('wt'), raw=True )
	text = _str.do('sh',text)
	se=[]
	for line in text.split('\n'):
		li=line; li=li.replace(' ','').replace('\t','');
		if not li.startswith('//'): se.append(line)

	_.saveText(se, _v.tt+__.os.sep+'wt-settings.json')
	c3po = _.getTable( 'wt-settings.json' )
	r2d2 = simplejson.dumps(c3po['actions'], sort_keys=False)

# def load():
# 	_.switches.fieldSet( 'Long', 'active', True )
# 	global c3po
# 	global r2d2
	
# 	c3po = _.getTable2( 'table' )

# 	text = _.getText( _v.config('wt'), raw=True )
# 	text = _str.do('sh',text)
# 	se=[]
# 	for line in text.split('\n'):

# 		line = line.rstrip()
# 		line = line.split('//')[0]
# 		if line.strip():
# 			se.append(line)
	
# 	print('\n'.join(se)); _.isExit(__file__)
	
# 	c3po = simplejson.loads('\n'.join(se))
# 	r2d2 = '\n'.join(se)

		# li=line; li=li.replace(' ','').replace('\t','');
		# if not li.startswith('//'): se.append(line)

	# _.saveText(se, _v.tt+__.os.sep+'wt-settings.json')
	
	# _.pt(c3po)
import simplejson
########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()
