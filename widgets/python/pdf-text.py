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
	_.switches.register( 'D100', '-d100' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.pdf', isData='name', description='Files', isRequired=False )

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
	'file': 'thisApp.py',
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

from PyPDF2 import PdfReader

def isInt(line,i=1):
	if not len(line) > i: return False
	if line[i] in '0123456789': return True
	else: return False


	return False
def process(data):
	data = data.replace('\t',' ')
	data = data.replace('\r','\n')
	data = data.strip()

	# print(data)

	lines=[]
	n=1
	first=False
	aline=[]
	for i,line in enumerate(data.split('\n')):
		line=line.strip()
		# print(line)
		if line:
			shouldProcess=True
			if not i:
				listname=line
				shouldProcess=False

			# if not line == listname and not line == 'd100 Description': shouldProcess=False
			linel=line.lower()
			if linel.startswith('d') and linel.endswith('description')  and linel.count(' ') < 2:
				if isInt(linel): shouldProcess=False

			if shouldProcess:
				if line == str(n) or line.split(' ')[0] == str(n):
					pass
				elif line.startswith(str(n)):
					line = str(n)+' '+line[len(str(n)):len(line)]
				if line == str(n) or line.split(' ')[0] == str(n):
					n+=1
					if aline: lines.append( ' '.join( aline ).replace('  ',' ').replace('  ',' ') )
					aline=[]
				# print(line)
				aline.append(line)
	if aline: lines.append( ' '.join( aline ).replace('  ',' ').replace('  ',' ') )
	flines=[]
	for line in lines:
		if line.endswith('Description'):
			fa=_.find_all(line,'Description')
			# print(fa,line)
			fad=_.find_all(line,'d')
			# print(fad)
			diff=fa[-1]-fad[-1]

			if diff == 4 or diff == 3 and isInt(line,fad[-1]+1):
				line=line[0:fad[-1]]

			# print(diff,line)
			# sys.exit()
		flines.append(line)
	y = '\n'.join(flines)
	
	return listname,y



import os
def action():
	json={}
	for path in _.isData():
		# print(path)
		# creating a pdf reader object
		reader = PdfReader(path)
		
		# printing number of pages in pdf file
		# print(len(reader.pages))
		
		# getting a specific page from the pdf file
		text=''
		pages=[]
		for i,apage in enumerate(reader.pages):
			page = reader.pages[i]
		
			# extracting text from page
			pages.append(page.extract_text())
		
		text='\n'.join(pages)
		# print(text)
		if _.switches.isActive('D100'):
			listname, text = process(text)
			listname=path
			if os.sep in path: listname=path.split(os.sep)[-1]
			listname=listname.replace(' ','_')
			listname=listname.replace('.pdf','')
			listname=listname.replace(',','')
			listname=listname.replace('…','')
			listname=listname.replace('’',"'")
			listname=listname.replace('”',"'")
			listname=listname.replace('“',"'")
			us=_.find_all(listname,'_')
			listname=listname[us[0]+1:len(listname)]
			json[listname.replace('_',' ')]=text.split('\n')

			# print(text)
			save='C:\\Users\\Scott\\.rt\\profile\\documents\\dnd\\etsy\\D100 Roll Chart Mega-Pack  DM Tools  PDF  DnD Dungeons and Dragons (5e)  Tabletop RPG\\d100-text\\'+listname+'.txt'
			_.saveText(text,save)
			print(listname.replace(' ','_')+'.txt')

	# save = save='C:\\Users\\Scott\\.rt\\profile\\documents\\dnd\\etsy\\D100 Roll Chart Mega-Pack  DM Tools  PDF  DnD Dungeons and Dragons (5e)  Tabletop RPG\\d100.json'
	# _.saveTable2(json,save)
	# print(save)



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
