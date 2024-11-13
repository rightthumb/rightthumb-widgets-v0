#usr/bin/python3
import os,sys,time,importlib,simplejson
if sys.platform[0] == 'w': figpath=os.getenv('USERPROFILE') +os.sep+'.rt'+os.sep+ '.config.hash'
else: figpath=os.getenv('HOME') +os.sep+'.rt'+os.sep+ '.config.hash'
def getTable( file ):
		json_data={}
		if os.path.isfile(file):
			with open(file,'r', encoding="latin-1") as json_file: json_data = simplejson.load(json_file)
		return json_data
fig=getTable(figpath)
sys.path.append( fig['w']+'/widgets/python'.replace('/',os.sep) )

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
import _rightThumb._vault as _vault
import _rightThumb._encryptString as _blowfish
##################################################


def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Save', '-save', 'secure.db' )
	_.switches.register( 'Password', '-password' )
	_.switches.register( 'Encrypt', '-en,-encrypt' )
	_.switches.register( 'Decrypt', '-de,-decrypt' )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
__.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'efm_crypt.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'proud of this little encryption algorithm',
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
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )

def _local_(do): exec(do)

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
		# globals()['var']
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

def scramble(vVv,y=2):
	y=int(y)
	if y==1: y=2
	if y==0: return vVv[::-1]
	seg=[]
	xXx=''
	for i in range(len(vVv)):
		seg.append(i)
		if (i % y) == 0 and  i:
			seg.reverse()
			for x in seg:
				xXx+=vVv[x]
			seg=[]
	if seg:
		seg.reverse()
		# print(seg)
		for x in seg:
			xXx+=vVv[x]
	return xXx


def scrambler(vVv,pw):
	pw=list(str(pw))
	for p in pw: vVv=scramble(vVv,p)
	return vVv



def passClean(pw):
	def nnuu(p,n):
		if not p: return str(n)
		else:
			if not int(p[-1]) == n: return str(n)
			elif not p[-1] == '9': return str(n+1)
			else: return '0'
	p=''
	for c in pw:
		if not c in '0123456789':
			p+=str(ord(c))
		else: p+=c
	pw=p
	pw=pw.replace('1','2')
	if not pw[0] == '2': pw='2'+pw
	p=''
	l=-1
	for n in pw:
		n=int(n)
		if not n == l: p+=str(n)
		else:
			p+=nnuu(p,n)
		l=n
	return p


		# if _.switches.isActive('Save'):

def encrypt(string, password):
	shift_amount = sum(ord(c) for c in password) % len(string)
	new_string = string[shift_amount:] + string[:shift_amount]
	return new_string

def decrypt(string, password):
	shift_amount = sum(ord(c) for c in password) % len(string)
	new_string = string[-shift_amount:] + string[:-shift_amount]
	return new_string


def action():

	if _.switches.isActive('Files'):
		Files=True
		with open(_.switches.values('Files')[0], mode='rb') as file:
			data = file.read()
	else:
		Files=False
		data = '\n'.join(_.appData[__.appReg]['pipe'])

	if _.switches.isActive('Password'):
		password=_.switches.values('Password')[0]
	else:
		password='8136901260'
	pw=passClean(password)
	# print(pw)
	if _.switches.isActive('Encrypt'):
		if Files:
			data=base64.b64encode(data)
		else:
			data=base64.b64encode(data.encode('utf-8'))



		vVv=encrypt(data.decode('ascii'),pw)
		if _.switches.isActive('Save'):
			_.saveText(vVv,_.switches.values('Save')[0])
		# print(vVv)

	if _.switches.isActive('Decrypt'):
		data=data.strip()
		# pw=pw[::-1]
		data=decrypt(data,pw)
		vVv=base64.b64decode(data.encode('utf-8'))
		# print(vVv.decode('ascii'))
		if _.switches.isActive('Save'):
			with open(_.switches.values('Save')[0], 'wb')  as outfile:
				outfile.write(vVv)



import base64


##################################################

# 78afd660-8cfe-4d7f-b2b9-64354c37fc95 
#    check backups for this code with dashes removed

##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	# action()
	start=time.time()
	action()
	# i=0
	# while i < 10000:
	#     i+=1
	diff=time.time()-start
	print(diff)
	_.isExit(__file__)

