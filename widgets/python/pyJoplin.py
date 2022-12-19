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
import sys, time
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
	#b)--> examples
	_.switches.register( 'Notes', '-n,-note,-notes' )
	_.switches.register( 'Download', '-dl,-download' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'pyJoplin.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
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
						_.hp('p thisApp -file file.txt'),
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
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--#
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();

	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

def jpage(p): global config; global _type_; return config[_type_].url.replace('[page]',str(p))


def all_data(t='notes'):
	global config
	global index
	global _type_
	_type_ = t
	# _.saveYML(index,'pyJoplin.yml')
	if not _type_ in index:
		index[_type_] = {} 
		index[_type_]['parents'] = {}
		index[_type_]['ids'] = {}
		index[_type_]['rev'] = {}
		RECORDS = []
		while not config[_type_].current == config[_type_].max:

			config[_type_].current+=1
			print(_type_, 'page:',config[_type_].current)
			# print(jpage(config[_type_].current))
			page = _.URL( jpage(config[_type_].current) )
			if page == '{"items":[],"has_more":false}':
				config[_type_].max=config[_type_].current
				# _.pr(page,c='red')
			else:
				data = simplejson.loads(page)
				# try:
				# index.table = index.table + data
				for rec in data['items']:
					RECORDS.append(rec)
		
		# for rec in _.tables.returnSorted( 'RECORDS', 'd.epoch', RECORDS ):
		for rec in _.tables.returnSorted( 'RECORDS', 'title', RECORDS ):
			# print(rec)
			# print(rec['title'])
			if rec['parent_id']:
				if not rec['parent_id'] in index[_type_]['parents']: index[_type_]['parents'][rec['parent_id']] = []
				index[_type_]['parents'][rec['parent_id']].append(rec['id'])
				index[_type_]['ids'][rec['id']] = rec
			else:
				index[_type_]['ids'][rec['id']] = rec
				index['top'].append(rec['id'])
				print('parent:',rec['id'])
		_.saveYML(index,'pyJoplin.yml')
				# except:
				#     pass
				#     print('error')






spent={}

def varDepth(paths):
	var = "['xXx']"
	return var.replace('xXx',"']['".join(paths))

base=''
def _hierarchy(paths):
	global index
	def _hier_(pa):
		global hierarchy
		global base
		xXx = _archy_(pa)
		ex = 'if not "'+xXx[0]+'" in hierarchy'+xXx[1]+': hierarchy'+varDepth(pa)+'={};'
		# print(ex)
		exec(ex)
		# hierarchy
		# print(xXx)
	def _archy_(pa):
		p=pa.copy()
		global hierarchy
		global base
		vd = varDepth(pa)
		ix=p[-1]
		p.pop()
		if not p:
			vx=base
			if not pa[0] in hierarchy:
				# print(base)
				hierarchy[pa[0]]={}
		else:
			vx=varDepth(p)
			# ix=p[-1]
		return ix, vx

	global hierarchy
	# print('bof')
	# print(paths)
	for i,ID in enumerate(paths):
		_.v.IDs[ID]=1
		if _.v.print: _.pr('_.v.IDs[ID]=1',ID,index['folders']['ids'][ID]['title'].strip())
		p=[]
		for ii,iD in enumerate(paths):
			p.append(iD)
			if i==ii: break
		_hier_(p)
	# _hier_(paths)




		# print(vx, ix)
	# print('eof')


def reverse(ID,r=0):
	global index
	if not r: _.v.path=[]
	_.v.path = [ID] + _.v.path
	# .append(ID)
	if ID in index['folders']['ids']:
		rec = index['folders']['ids'][ID]
		if rec['parent_id']:
			return reverse(rec['parent_id'],r=1)
	_hierarchy(_.v.path)
	return _.v.path.copy()

def tabs(cnt):
	cnt-=1
	c=0
	result = ''
	while not c == cnt:
		c+=1
		result += '    '
	return result



def buildChildren(ID):
	global index
	if ID in spent: return None
	spent[ID]=1
	if ID in index['folders']['ids']:
		rec = index['folders']['ids'][ID]
		if not rec['parent_id']: level = 0
		# print( index['folders']['ids'] )
		# print( ID, p, rec['title'] )
		paths = reverse(ID)
		level = len(paths)
		if 0 and ID == '88903608dadf4da2991c1adb9ed3a8e4':
			print(level,paths)
			# paths.reverse()
			for i in paths:
				print( tabs(len(reverse(i))), index['folders']['ids'][i]['title'] )

		# print( ID, level, rec['title'], rec['parent_id'] )
		if False:
			try:
				print(tabs(level),rec['title'].strip(),          ' - ',index['folders']['ids'][rec['parent_id']]['title'].strip(), ID  )
			except Exception as e:
				print(tabs(level),rec['title'].strip()  )
		if ID in index['folders']['parents']:
			for iD in index['folders']['parents']:
				if not iD == ID:
					buildChildren(iD)



hierarchy = {}
_.v.IDs={}
def traverse(dic):
	global index
	for k in dic:
		l=len(reverse(k))
		if k in _.v.IDs:
			_.pr( l, tabs(l), index['folders']['ids'][k]['title'].strip(), c='cyan' )
			if _.switches.isActive('Notes'):
				if k in index['notes']['parents']:
					for c in index['notes']['parents'][k]:
						# if _.showLine(index['notes']['ids'][c]['title']):
						if c in _.v.IDs or not _.switches.isActive('Plus'):
							_.pr( l+1, tabs(l+1), index['notes']['ids'][c]['title'].strip(), c='darkcyan' )
		traverse(dic[k])
_.v.print=False
def traverseSearch(dic,r=0):
	global index
	global hierarchy
	if not r: hierarchy={};_.v.IDs={1:1};
	_.v.print=False
	for k in dic:
		if _.showLine(index['folders']['ids'][k]['title']):
			l=len(reverse(k))
			# _.pr( l, tabs(l), index['folders']['ids'][k]['title'].strip(), c='cyan' )
		if _.switches.isActive('Notes'):
			if k in index['notes']['parents']:
				for c in index['notes']['parents'][k]:
					# if c in index['notes']['ids']:
					if _.showLine(index['notes']['ids'][c]['title']):
						_.v.IDs[c]=1
						reverse(k)
						# _.pr( l+1, tabs(l+1), index['notes']['ids'][c]['title'].strip(), c='darkcyan' )
		traverseSearch(dic[k],r=1)


def theCORN():
	global hierarchy
	h=hierarchy.copy()
	hierarchy={};_.v.IDs={1:1};
	if _.switches.isActive('Plus'):
		traverseSearch(h.copy())
	traverse(hierarchy)
	# print(_.toYML(hierarchy))

def action():
	load()
	all_data('folders')
	all_data('notes')
	global index

	# for k in index: print(k)

	for i in index['folders']['ids']: reverse(i)

	# for ID in index['top']: buildChildren(ID)
	theCORN()

	# _.pv(data)

def load():
	global config
	global index
	if not _.switches.isActive('Download'): index = _.getYML('pyJoplin.yml')
	token = _keychain.imp.key('joplin-token')
	# config['notes'].url = 'http://localhost:41184/notes/?token=[joplin-token]'.replace('[joplin-token]',token)
	
	config['folders'] = _.dot()
	config['folders'].url = 'http://localhost:41184/folders/?token=[joplin-token]'.replace('[joplin-token]',token)
	config['folders'].current = 0
	config['folders'].max = 2
	config['folders'].max = 13
	config['folders'].direction = 'ASC'
	config['folders'].direction = 'DESC'
	config['folders'].url = config['folders'].url+'&order_by=updated_time&order_dir='+config['folders'].direction+'&limit=100&page=[page]'
	config['notes'] = _.dot()
	config['notes'].url = 'http://localhost:41184/notes/?token=[joplin-token]'.replace('[joplin-token]',token)
	config['notes'].current = 0
	config['notes'].max = 2
	config['notes'].max = 100000
	config['notes'].direction = 'ASC'
	config['notes'].direction = 'DESC'
	config['notes'].url = config['notes'].url+'&order_by=updated_time&order_dir='+config['notes'].direction+'&limit=100&page=[page]'
index = {}
index['top'] = []
config = {}
data = _.dot()
_keychain = _.regImp( __.appReg, 'keychain' )
simplejson = __.imp('simplejson')

##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()

	#e)--> examples
	action()
	_.isExit(__file__)


