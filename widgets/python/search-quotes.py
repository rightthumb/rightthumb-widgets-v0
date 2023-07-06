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
	_.switches.register( 'Search-In-Comments-Too', '-ic,-comment' )



__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])


_.appInfo[focus()] = {
	
	'file': 'search-quotes.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Search only text that is in quotation marks or the inverse',
		
		
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
						_.hp('p search-quotes -f nsfw.py + nsfw '),
						_.hp('p search-quotes -f nsfw.py + nsfw -i '),
						_.hp('p search-quotes -f nsfw.py + nsfw -i -comment'),
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

	path = _.switches.values('Files')[0]
	#n)--> single line comment
	remove_comments=False
	if path.endswith('.py'): SLC='#';remove_comments=True;
	if path.endswith('.js'): SLC='//';remove_comments=True;
	file = _.getText(path,raw=True)
	if remove_comments:
		comments={}
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


	# test = re.match(r'\'.*?\'|".*?"|\(.*?\)|\[.*?\]|\{.*?\}', file)
	# print(test)

	# sys.exit()
	subject='javascript'
	if path.endswith('.py'): subject='python'
	
	validator._err_ = False
	index = validator.createIndex( file, 'javascript', skipLoad=True, simple=False, A=None, B=True, C=None )
	if not _.switches.isActive('Invert'):


		cleaner={}
		for k in validator.identity['location']['open']:
			x = validator.assetSnipetClean(k,validator.identity['location']['open'][k])
			if x.startswith('"') or x.startswith("'"):
				uuuid = _.genUUID()
				cleaner[uuuid]=x
				file=file.replace(x,uuuid)



		for i,line in enumerate(file.split('\n')):
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
					_.pr(_.pr(i,c='yellow',p=0),line)


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
						_.pr(_.pr(i,c='yellow',p=0),line)
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
					_.pr(_.pr(i,c='yellow',p=0),line)

def color(line):
	subjects=[]
	for xXx in _.switches.values('Plus'):
		for subject in _.caseUnspecific( line, xXx ):
			subjects.append(subject)
	for subject in subjects:
		line = line.replace( subject, _.cp( subject, 'green', p=0 ) )
	return line


if __name__ == '__main__':
	action()
	__.isExit()