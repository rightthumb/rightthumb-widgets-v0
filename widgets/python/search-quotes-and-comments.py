import sys, time

import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()

_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=True )
	_.switches.register( 'Invert', '-i,-invert' )
	_.switches.register( 'Search-In-Comments-Too', '-in,-ic,-all,-incomments,-inc', 'if you select this "Invert" is automaticaly activated' )
	_.switches.register( 'Comment', '-comment', '#' )
	_.switches.register( 'Disable-Auto-Language-Comment-Detect', '-no-auto' )
	_.switches.register( 'Dump-Quotes', '-dq,-dumpq,-dumpquotes' )
	_.switches.register( 'Print-Striped-File', '-strip' )



__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])


_.appInfo[focus()] = {
	
	'file': 'search-quotes-and-comments.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Search only text that is in \'quotation\' "marks" or the inverse eveything but quotation marks',
		
		
	'categories': [
						'DEFAULT',
				],
	'usage': [
						
						
						
	],
	'relatedapps': [
						
						
	],
	'prerequisite': [
						
						
	],
	'examples': [
						_.hp('p search-quotes-and-comments -f nsfw.py + nsfw '),
						_.hp('p search-quotes-and-comments -f nsfw.py + nsfw -i '),
						_.hp('p search-quotes-and-comments -f nsfw.py + nsfw -i -all'),
						_.hp('p search-quotes-and-comments -f nsfw.py + nsfw -comment "#" '),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					
					
	],
	'aliases': [
					
					
	],
	'notes': [
					
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, 
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



_code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
validator = _code.imp.Validator()



import sys, re

def action():
	activity=0
	if _.switches.isActive('Search-In-Comments-Too'): _.switches.fieldSet( 'Invert', 'active', True )

	comments={}
	cleaner={}
	#n)--> load file
	path = _.switches.values('Files')[0]
	file = _.getText(path,raw=True)
	xFile=file


	


	if _.switches.isActive('Dump-Quotes'):
		validator._err_ = False
		index = validator.createIndex( file, 'javascript', skipLoad=True, simple=False, A=None, B=True, C=None )
		for k in validator.identity['location']['open']:
			x = validator.assetSnipetClean(k,validator.identity['location']['open'][k])
			if x.startswith('"') or x.startswith("'"):
				if not _.switches.isActive('Print-Striped-File'):
					_.pr(x,c='Background.light_blue')
				# uuuid = _.genUUID()
				# cleaner[uuuid]=x
				# file=file.replace(x,uuuid)

		

	#n)--> manage comment settings
	remove_comments=False
	if path.endswith('.py'): SLC='#';remove_comments=True;
	if path.endswith('.js'): SLC='//';remove_comments=True;
	if _.switches.isActive('Comment'): SLC=_.switches.values('Comment')[0];remove_comments=True;
	if not _.switches.isActive('Disable-Auto-Language-Comment-Detect'):
		common_comments = [
								'//',
								'#',
								'%',
								';',
		]
		tFile = _str.do('sh',file).replace('\t','').replace(' ','')
		possible={}
		for detect in common_comments:
			cnt=tFile.count('\n'+detect)
			if not remove_comments and cnt > 4:
				possible[detect]=cnt
		greatest=0
		for detect in possible:
			if greatest < possible[detect]: greatest=possible[detect]
		if greatest:
			for detect in possible:
				if possible[detect] == greatest:
					SLC=detect;remove_comments=True;
					if not _.switches.isActive('Print-Striped-File'):
						_.pr( 'detected comments:',detect ,c='Background.light_blue' )



	if not remove_comments:
		if not _.switches.isActive('Print-Striped-File'): ask='y'
		elif not _.switches.isActive('Print-Striped-File'):
			_.pr( 'Advanced comment detect ?',c='yellow' )
			ask=input('yN : ')
		if 'y' in ask.lower():
			#n)--> advanced comment detection
			possible={}
			possible2={}
			for line in tFile.split('\n'):
				if line:
					fir=line[0]
					if len(line)>1: fir2=line[1]
					else: fir2==0
					sub=0
					if not fir in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}[]()"':
						if fir == "'" and line.count("'")==1:
							sub="'"
						else:
							sub=fir
					if sub:
						if not sub in possible:
							possible[sub]=line.count(sub)
						else:
							possible[sub]+=line.count(sub)
						if fir2 and not fir2 in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}[]()"'+"'":
							if not sub in possible:
								possible2[sub]=line.count(sub+fir2)
							else:
								possible2[sub]+=line.count(sub+fir2)
						

			greatest=0
			greatest2=0
			for detect in possible:
				if greatest < possible[detect]: greatest=possible[detect]
			for detect in possible2:
				if greatest2 < possible2[detect]: greatest2=possible2[detect]
			po2=0
			for detect in possible:
				if possible[detect] == greatest:
					if greatest > 4:
						po2=detect

			for detect in possible:
				if possible[detect] == greatest:
					if greatest > 4:
						if po2 and (greatest == greatest2 or greatest2 > greatest):
							SLC=po2;remove_comments=True;
							if not _.switches.isActive('Print-Striped-File'):
								_.pr( 'detected comments:',po2 ,c='Background.light_blue' )
						else:
							SLC=detect;remove_comments=True;
							if not _.switches.isActive('Print-Striped-File'):
								_.pr( 'detected comments:',detect ,c='Background.light_blue' )



	if remove_comments or _.switches.isActive('Print-Striped-File'):
		lines=[]
		for i,line in enumerate(file.split('\n')):
			if line.startswith(SLC):
				comments[i]=line
				line=''
			else:
				if SLC in line:
					par=line.split(SLC)
					line=par[0]
					par.pop(0)
					comments[i]=SLC+SLC.join(par)
			lines.append(line)
		pass
		file='\n'.join(lines)
		file=_str.do('sh',file)
		while '\n\n\n' in file: file=file.replace('\n\n\n','\n\n')
		if _.switches.isActive('Print-Striped-File'):
			for line in file.split('\n'):
				print(line)





	#n)-->
	fi_len=len(file.split('\n'))
	subject='javascript'
	if path.endswith('.py'): subject='python'
	
	validator._err_ = False
	index = validator.createIndex( file, 'javascript', skipLoad=True, simple=False, A=None, B=True, C=None )
	if not _.switches.isActive('Invert'):

		
		for k in validator.identity['location']['open']:
			x = validator.assetSnipetClean(k,validator.identity['location']['open'][k])
			if x.startswith('"') or x.startswith("'"):
				uuuid = _.genUUID()
				cleaner[uuuid]=x
				file=file.replace(x,uuuid)



		for i,line in enumerate(file.split('\n')):
			if len(line) > 3:
				x=_str.do('trim',line)
				# if x.startswith('"') or x.startswith("'"): continue

				showLine=False

				for uu in cleaner:
					if uu in line and _.showLine(cleaner[uu]):
						showLine=True
						line = line.replace(uu, color(cleaner[uu]))

				if showLine:
					if line:
						if i in comments: line+=comments[i]
						if not _.switches.isActive('Print-Striped-File'):
							_.pr(_.pr(_.zeros3(i,fi_len),c='yellow',p=0),line)
						activity+=1


		# for k in validator.identity['location']['open']:
		#     x = validator.assetSnipetClean(k,validator.identity['location']['open'][k])
		#     if x.startswith('"') or x.startswith("'"):
		#         if _.showLine(x):
		#             _.pr(x)

	elif _.switches.isActive('Invert'):
		cleaner={}
		for k in validator.identity['location']['open']:
			x = validator.assetSnipetClean(k,validator.identity['location']['open'][k])
			if x.startswith('"') or x.startswith("'"):
				uuuid = _.genUUID()
				cleaner[uuuid]=x
				file=file.replace(x,uuuid)
		pass
		if not _.switches.isActive('Search-In-Comments-Too'):
			# comments={}
			for i,line in enumerate(file.split('\n')):
				x=_str.do('trim',line)
				
				
				if x.startswith('"') or x.startswith("'"): continue
				if _.showLine(line):
					if line:
						line=color(line)
						for uu in cleaner:
							line = line.replace(uu, cleaner[uu])
						if i in comments: line+=comments[i]
						if not _.switches.isActive('Print-Striped-File'):
							_.pr(_.pr(_.zeros3(i,fi_len),c='yellow',p=0),' ',line)
						activity+=1
		elif  _.switches.isActive('Search-In-Comments-Too'):
			# comments={}
			for i,line in enumerate(file.split('\n')):
				x=_str.do('trim',line)
				if i in comments: line+=comments[i]
				
				if x.startswith('"') or x.startswith("'"): continue
				if _.showLine(line):
					line=color(line)
					for uu in cleaner:
						line = line.replace(uu, cleaner[uu])
					if not _.switches.isActive('Print-Striped-File'):
						_.pr(_.pr(_.zeros3(i,fi_len),c='yellow',p=0),' ',_.pr(line,pvs=1,p=0))
					activity+=1
	if not _.switches.isActive('Print-Striped-File'):
		if activity:
			_.pr()
			_.pr(line=1,c='green')
			_.pr(line=1,c='green')
			_.pr()
			_.pr('Found:',_.addComma(activity),'lines out of',_.addComma(fi_len),c='yellow')
			_.pr()
			_.pr(line=1,c='cyan')
			_.pr()
			_.pr( '- enter a line number or space deliminated number(s) and view '+str(_.v.lines)+' lines...', c='darkcyan' )
			_.pr( '    ...above and below the selected line so you figure out what going on in that section', c='darkcyan' )
			_.pr()
			_.pr( '- to change number of lines that print above and below chosen line: L 10', c='darkcyan' )
			_.pr()
			_.pr( '- leave blank and hit enter, to exit', c='darkcyan' )
			_.pr()
			_.pr(line=1,c='cyan')
			while True:
				_.pr(line=1,c='cyan')
				_.pr()
				loop()

def color(line):
	subjects=[]
	for xXx in _.switches.values('Plus'):
		for subject in _.caseUnspecific( line, xXx ):
			subjects.append(subject)
	for subject in subjects:
		line = line.replace( subject, _.cp( subject, 'green', p=0 ) )
	return line


def loop():
	ask=''

	ask=input(' : ')
	if not len(ask.replace(' ','').replace('\r','').replace('\n','').replace('\t','')): _.pr(line=1,c='cyan'); _.pr(); sys.exit();

	_.pr()



_.v.lines=5

_.clear()

if __name__ == '__main__':
	action()
	__.isExit()
