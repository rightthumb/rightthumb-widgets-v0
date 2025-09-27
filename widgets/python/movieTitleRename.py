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
	_.switches.register( 'Test', '-test' )
	_.switches.register( 'Size', '-size' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='name', description='Files' )


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
	'file': 'movieTitleRename.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'generate code to rename movies',
	'categories': [
						'rename',
						'file',
						'folder',
						'entertainment',
						'ent',
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
						'p folder --c | p movieTitleRename',
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
# START



def removeStuff( line ):
	add = ''
	if '2160' in line:
		add = '(2160p)'
	elif '1080i' in line or '1080I' in line:
		add = '(1080i)'
	elif '1080p' in line or '1080P' in line or '1080' in line:
		add = '(1080p)'
	elif '720i' in line or '720I' in line:
		add = '(720i)'
	elif '720p' in line or '720P' in line or '720' in line:
		add = '(720p)'
	elif 'x264' in line.lower():
		add = '(x264)'
	elif 'bluray' in line.lower():
		add = '(BluRay)'
	elif 'dvd' in line.lower():
		add = '(dvd)'
	elif 'hd' in line.lower():
		add = '(HD)'
	if not _.switches.isActive('Size'):
		add = ''



	stuff = [

				'[',
				']',
				')',
				'(',
				'. .',
				'WEBRip',
				'AAC',
				'5.1',
				'YTS.MX',
				'YTS.LT',
				'512Kb',
				'2160p',
				'2160P',
				' MULTI ',
				' HDTV',
				'_track',
				'BluRay',
				'BluRay',
				'HDCLUB',
				'HDRip',
				'720p',
				'1080p',
				'1080P',
				'x264',
				'HD-TS',

				'WwW SeeHD PL',
				'WwW SeeHD',
				'NEW',
				'new',
				'New',
				'WEB-DL',
				'WEB-DLRip',
				'46Gb',
				'Rip 1  Line MegaPeer',
				'P TS',
				'E:\\MOVIES'+_v.slash,
				'dvdrip',
				'xvid',
				'kinokopilka',
				' www ',
				' dvdrip ',
				' Hmark ',
				' Dvdrip ',
				'Xvid',
				'Bgaudio',
				'Siso',
				'-',
				'"',
				'Dvdrip',
				'Brrip',
				'BrRip',
				'YIFY',
				'1400MB',
				' DD ',
				'GalaxyRG',
				'TGx',
				'BRrip',
			]
	for s in stuff:
		line = line.replace(s,' ')
		line = line.replace(s.replace( ' ','' ),' ')
		line = line.replace(s.upper(),' ')
		line = line.replace(s.lower(),' ')
		line = line.replace(s.title(),' ')
	line = _str.cleanBE(line,' ')
	line = line.replace( '.20', ' 20' )
	line = line.replace( '.19', ' 19' )
	line = line.replace( '_', ' ' )
	line = _str.replaceDuplicate( line, ' ' )
	line = line.replace( '. .', '' )
	line = line.replace( ' .', '.' )
	line = _str.cleanBE(line,' ')
	global extensionList
	# _.pr( extensionList )
	# sys.exit()
	hasExt = ''
	# _.pr( extensionList )
	for xt in extensionList:
		if xt.upper() in line:
			hasExt = xt
		if xt in line:
			hasExt = xt
		line = line.replace( xt.upper(), xt )
		line = line.replace( ' '+xt, xt )
		if add:
			line = line.replace( xt, ' '+add+''+xt )
	line = line.replace( hasExt, '' )
	line = line.replace( '.', ' ' )
	line = _str.cleanBE(line,' ')
	line = line + '.'+hasExt
	line = line.replace( '..', '.' )
	if add and not hasExt:
		line = line + ' '+add
	line = _str.replaceDuplicate( line, ' ' )
	# line = line.replace( '  ', ' ' )
	line = _str.cleanBE(line,' ')
	return line

def extt(fi):

	if not '.' in fi: return fi,''
	par=fi.split('.')
	par.reverse()
	ex='.'+par[0]
	ffi = fi[0: len(fi)-len(ex) ]
	# print(ex)
	# print(ffi)
	# sys.exit()
	return ffi, ex

def action():
	extensionsDatabank()
	global extensionList

	# print(_.isData(r=1))
	# print( _.switches.values('Files') )
	# sys.exit()
	# _copy = _.regImp( __.appReg, '-copy' )
	# _copy.imp.copy(  )

	# _movieTitle = _.regImp( __.appReg, 'movieTitle' )
	# _movieTitle.switch( 'JustVar' )
	# import movieTitle

	if _.switches.isActive('Files'):
		data = _.switches.values('Files')
	else:
		data = _.isData(r=1)

	for i,row in enumerate( data ):
		row = _str.cleanBE(row,' ')
		row = row.replace('"','')
		# _movieTitle.imp.pipeData = []
		# _movieTitle.imp.pipeData.append(row)
		# _movieTitle.action()
		# m = movieTitle.theTitle
		# sys.exit()
		xy = extt(row)
		m  = xy[0]
		ex = xy[1]
		m = removeStuff(m)
		m = removeStuff(m)
		m=m+ex; m=m.replace('..','.').replace(' .','.');
		if m.endswith('.'): m=m[:-1]
		if m.endswith(' '): m=m[:-1]
		if _.switches.isActive('Test'):
			_.pr()
			_.pr(row)
			_.pr(m)
			_.pr()
		else:
			if _.isWin:
				_.pr( 'rename '+ '"'+row+'"'  +'   '+ '"'+m+'"' )
			else:
				_.pr( 'mv '+ '"'+row+'"'  +'   '+ '"'+m+'"' )



def extensionsDatabank():
	global extensionList
	extensionList = []
	extensionList.append('.srt')
	_db = _.regImp( __.appReg, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )

	for index in ['video']:
		_db.switch( 'Plus', [index] )
		for i,x in enumerate(_db.do( 'action' )):
			x = x.replace('.','')
			if not x.startswith('.'):
				x = '.'+x
			if not x in extensionList:
				extensionList.append( x.lower() )
	# print(extensionList)



########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()