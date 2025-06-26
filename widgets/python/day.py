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
	_.switches.register( 'Fi', '-f,-fi,-file,-files','notes.md' )
	_.switches.register( 'Date', '-d,-date' )
	_.switches.register( 'Epoch', '-e,-epoch' )
	_.switches.register( 'Ago', '-ago' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'Open', '-o,-open' )
	_.switches.register( 'Print', '-p,-print' )
	_.switches.register( 'Change-Dir', '-cd' )
	_.switches.register( 'Cows', '-cow,-cows' )
	_.switches.register( 'mf', '-mf' )
	_.switches.register( 'Color', '-color', 'mf' )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('Crypt-daily/notes.md-Default',False)
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'day.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'daily documentaion system',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'notes',
						'documentaion',
						'today',
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
						_.hp('p day'),
						_.hp(''),
						_.hp('echo. | p day -f notes.md'),
						'|-   ##### #t) 2022-07-21T03:03:49-0400',
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


########################################################################################
# START

# ago = _.switches.value('Ago')
# _.pr(  _.isDate(ago),pvs=1  )
# sys.exti()


def hush():
	global isWin
	if isWin: return ' > nul 2>&1'
	else: return ' > /dev/null 2>&1'

bat = '''@echo off
call m back   > nul 2>&1
echo Background.green linePrint       > %tmpf%-print_color-day
echo yellow last fo: b back          >> %tmpf%-print_color-day
call bb back > %tmpf%-back
SET /p pretty_back=<%tmpf%-back
echo purple %pretty_back%  >> %tmpf%-print_color-day
echo.                                >> %tmpf%-print_color-day
echo darkcyan ago                    >> %tmpf%-print_color-day
echo cyan path                       >> %tmpf%-print_color-day
echo Background.green linePrint      >> %tmpf%-print_color-day
call p print_color -f %tmpf%-print_color-day -tab 2
cd path
'''
sh = '''#!/bin/bash
source $HOME/.bashrc
$m back   > /dev/null 2>&1
echo ''    >> $HOME/.bashrc.once.print
echo last fo: b.back >> $HOME/.bashrc.once.print
$bb back   >> $HOME/.bashrc.once.print
echo ''    >> $HOME/.bashrc.once.print
echo ago   >> $HOME/.bashrc.once.print
echo path  >> $HOME/.bashrc.once.print
echo ''    >> $HOME/.bashrc.once.print
sed -i 's/^/\t\t/' $HOME/.bashrc.once.print
if [ ! -f path/notes.md ] then
	touch path/notes.md
fi
# $cdf path/notes.md
cd path
$SHELL

'''

os = __.imp('os.path.isdir')
os = __.imp('os.system')
os = __.imp('os.chmod')
_docs = _.regImp( __.appReg, 'decrypt-docs' )
focus()
_open = _.regImp( __.appReg, 'file-open' )
_open.switch('Backup')
focus()
_md = _.regImp( __.appReg, 'md' )
focus()
sep=os.sep
# _docs.switch('Files')

def popper(path,cnt=1):
	if path.endswith(os.sep): path = path[:-1]
	c=0
	while not c == cnt:
		c+=1
		pp = path.split(os.sep)
		pp.pop()
		path = os.sep.join(pp)
	return path

def load():
	global fo
	global epoch
	global pesonal_day
	epoch = time.time()
	ep=epoch
	os=__.imp('os.sep')
	sep=os.sep
	if _.switches.isActive('Epoch'): epoch = float(_.switches.value('Epoch'))
	if _.switches.isActive('Ago'): epoch = _.switches.value('Ago'); epoch-=5;
	if _.switches.isActive('Date'): epoch = _.autoDate( _.switches.value('Date') )

	today = _.day(epoch); fo =  _v.rtp+'daily'+os.sep+today;
	# print( today )
	# woy=os.sep+popper(today,1)
	# year=os.sep+popper(today,2)
	# print( ' woy:',woy )
	# print( 'year:',year )
	# sys.exit()
	_v.mkdir(fo)
	var = _v.rtp+'vars'+os.sep
	vbm = _v.rtp+'bookmarks'+os.sep
	if len(_.switches.all())==0:
		brand_day = True
		if os.path.isfile(var+'day.brand'):
			L = _.isDate( float( _.getText(var+'day.brand', raw=True) ) ,f='date')
			N = _.isDate(epoch,f='date')
			if L == N: brand_day = False
		if brand_day:
			pesonal_day = var+'day.'
			if _.isWin: pesonal_day+'bat'
			else:  pesonal_day+'sh'
			today = _.day(epoch); fo =  _v.rtp+'daily'+os.sep+today;
			# print(fo+'notes.md')
			# print(fo+'notes.md')
			# print(fo+'notes.md')
			if not os.path.isfile(fo+'notes.md'):
				path=fo+'notes.md'
				faliases=_.getTable('file-open-aliases.hash')
				if not faliases: faliases={ 'aliases':{}, 'files':{} }
				faliases['aliases']['0']=path
				if not path in faliases['files']: faliases['files'][path]=[]
				faliases['files'][path].append('0')



				_.pr('branding day',c='red')
				_v.mkdir(fo)
				bm = _.getTable('bookmarks.index')
				# _.saveTable(bm,'bookmarks-day.index')
				# print(bm); sys.exit();
				# _wsl = wsl(fo)
				# print('wsl:',_wsl)
				# print('wsl:',_wsl)
				# print('wsl:',_wsl)
				# print('wsl:',_wsl)
				# print('wsl:',_wsl)
				aliases = []
				
				woy=os.sep+popper(today,1)
				year=os.sep+popper(today,2)
				aliases.append('alias woy="cd '+wsl(_v.rtp+'daily'+woy)+'"')
				aliases.append('alias y="cd '+wsl(_v.rtp+'daily'+year)+'"')
				aliases.append('alias yr="cd '+wsl(_v.rtp+'daily'+year)+'"')
				aliases.append('alias year="cd '+wsl(_v.rtp+'daily'+year)+'"')
				aliases.append('alias day="cd '+wsl(_v.rtp+'daily')+'"')
				aliases.append('alias 00="cd '+wsl(_v.rtp+'daily')+'"')
				aliases.append('alias da="cd '+wsl(_v.rtp+'daily')+'"')
				aliases.append('alias daily="cd '+wsl(_v.rtp+'daily')+'"')

				aliases.append('alias 0="cd '+wsl(fo)+'"')
				bm['labels'][str(0)]=fo;  _.saveText(fo,vbm+'BM-0.txt');
				bm['labels']['day']=fo;   _.saveText(fo,vbm+'BM-day.txt');
				bm['labels']['today']=fo; _.saveText(fo,vbm+'BM-today.txt');
				dA=epoch-86400
				dayX = _.day(dA); dX = _v.rtp+'daily'+os.sep+dayX; aliases.append('alias 1="cd '+wsl(dX)+'"');
				we=_.isDate(dA,f='dow2'); bm['labels'][we]=dX;  _.saveText(dX,vbm+'BM-'+we+'.txt');
				bm['labels'][str(1)]=dX;  _.saveText(dX,vbm+'BM-1.txt');
				bm['labels']['yesterday']=dX;  _.saveText(dX,vbm+'BM-yesterday.txt');
				bm['labels']['y']=dX;  _.saveText(dX,vbm+'BM-yy.txt');
				bm['labels']['y']=dX;  _.saveText(dX,vbm+'BM-yy.txt');
				dA=epoch-86400-86400; dayX = _.day(dA); dX = _v.rtp+'daily'+os.sep+dayX; aliases.append('alias 2="cd '+wsl(dX)+'"'); bm['labels'][str(2)]=dX; _.saveText(dX,vbm+'BM-2.txt'); we=_.isDate(dA,f='dow2'); bm['labels'][we]=dX;  _.saveText(dX,vbm+'BM-'+we+'.txt');
				dA=epoch-86400-86400-86400; dayX = _.day(dA); dX = _v.rtp+'daily'+os.sep+dayX; aliases.append('alias 3="cd '+wsl(dX)+'"'); bm['labels'][str(3)]=dX; _.saveText(dX,vbm+'BM-3.txt'); we=_.isDate(dA,f='dow2'); bm['labels'][we]=dX;  _.saveText(dX,vbm+'BM-'+we+'.txt');
				dA=epoch-86400-86400-86400-86400; dayX = _.day(dA); dX = _v.rtp+'daily'+os.sep+dayX; aliases.append('alias 4="cd '+wsl(dX)+'"'); bm['labels'][str(4)]=dX; _.saveText(dX,vbm+'BM-4.txt'); we=_.isDate(dA,f='dow2'); bm['labels'][we]=dX;  _.saveText(dX,vbm+'BM-'+we+'.txt');
				dA=epoch-86400-86400-86400-86400-86400; dayX = _.day(dA); dX = _v.rtp+'daily'+os.sep+dayX; aliases.append('alias 5="cd '+wsl(dX)+'"'); bm['labels'][str(5)]=dX; _.saveText(dX,vbm+'BM-5.txt'); we=_.isDate(dA,f='dow2'); bm['labels'][we]=dX;  _.saveText(dX,vbm+'BM-'+we+'.txt');
				dA=epoch-86400-86400-86400-86400-86400-86400; dayX = _.day(dA); dX = _v.rtp+'daily'+os.sep+dayX; aliases.append('alias 6="cd '+wsl(dX)+'"'); bm['labels'][str(6)]=dX; _.saveText(dX,vbm+'BM-6.txt'); we=_.isDate(dA,f='dow2'); bm['labels'][we]=dX;  _.saveText(dX,vbm+'BM-'+we+'.txt');
				dA=epoch-86400-86400-86400-86400-86400-86400-86400; dayX = _.day(dA); dX = _v.rtp+'daily'+os.sep+dayX; aliases.append('alias 7="cd '+wsl(dX)+'"'); bm['labels'][str(7)]=dX; _.saveText(dX,vbm+'BM-7.txt'); we=_.isDate(dA,f='dow2'); bm['labels'][we]=dX;  _.saveText(dX,vbm+'BM-'+we+'.txt');

				# print(bm['labels'][str(7)]); sys.exit();
				_.saveText(aliases,_v.rtp+'daily'+os.sep+'.seven.sh')
				_.saveText(str(epoch),var+'day.brand')
				# if os.path.isfile(_v.tt+'/tables/bookmarks-day.index'.replace('/',os.sep)): os.unlink(_v.tt+'/tables/bookmarks.index'.replace('/',os.sep))
				_.saveTable(bm,'bookmarks.index')
				
				
				_.saveText(str(epoch),var+'day.brand')
				_.saveText(dX,vbm+'BM-day.txt')
				_.pr('day branded',c='Background.red')

		

				# if not _.switches.isActive('Clean'): _.pr(today)
				_v.mkdir(fo)
				# ago1=_.isDate(epoch,f='ago').replace(' <','').replace('<',''); ago2=str(_.isDate(epoch,f='ago-dic')).replace('"','').replace("'",'').replace('{','').replace('}','').replace('<','').replace('>',''); ago='( '+ago1+' ) '+ago2;
				# if ago1 == 'today': ago=ago1
				ago=_.isDate(float(epoch),f='ago-txt')
				if _.isWin:
					global bat
					# script=_v.ww+sep+'batch'+sep+'.day.bat'
					script=_v.ww+sep+'batch'+sep
					bat = bat.replace('path',fo)
					bat = bat.replace('ago', ago )
					bat = _str.do('sh',bat); _.saveText( bat, script+'.day.bat' ); _.saveText( bat, script+'.d.bat' );
					_.pr( script, c='Background.light_blue' )
	# else:
	#     global sh
	#     script = _v.ww+sep+'bash'+sep+'nav'+sep+'day.sh'
	#     sh = sh.replace('path',fo)
	#     sh = sh.replace('ago', ago)
		
	#     sh = _str.do('sh',sh); _.saveText( sh, script );
	#     os.chmod( script, 0o777 )
	#     _.pr( script, c='Background.light_blue' )

def cryptScan(path):
	'open .md file and scan for "#crypt"'
	if not path.endswith('.md'): return False
	with open(path, 'r') as inF:
		for line in inF:
			if '#crypt' in line: return True
	return False

def files(fi):
	global fo
	path=fo+fi
	color='ColorBold.gray'
	_.pr('files(fi)',c=color)
	# print('_.isData()',_.isData())

	_cryptFi = _.getTable('secure-crypt-local.meta')
	
	if _.isData():
		_.pr('pipe detected',c=color)
		save=True
		if 'e70612b5-9725-4e6f-8d92-c1a9b56910a9' in str(_.isData()):
			txt = ''
		else:
			txt = '\n'.join(_.isData())
		
		if os.path.isfile(path):
			_.pr('append file',c='red')
			# ask=input2(' replace file? : ')
			# if 'n' in ask.lower(): save = False
		if save:
			if os.path.isfile(path):
				_.pr('date generated',c=color)
				t2 = _.getText(path,raw=True)+'\n\n'+'##### #t) '+_.isDate(time.time(),f='iso')+'\n\n'; txt=t2+txt;
			_.saveText( txt, path )
			# _.pr( path, c='cyan' )
		# return None
	if os.path.isfile(path):
		if path.lower().endswith('.md')     and     not path in _cryptFi:
			crypt = False
			_fi_=_.getText(path,raw=True)
			cry=_fi_.count('#crypt')
			if not crypt and '#crypt' in _fi_:
				if not os.path.isfile(path):
					# _.pr('#crypt',c='BackgroundGrey.red')

					_.pr('#crypt found in doc',c='Background.red')
					_.pr('f = full file encryption',c='yellow')
					_.pr('p = partial file encryption',c='yellow')
					_.pr('blank = do NOT encrypt',c='yellow')
					crypt = False; ask = input(' secure doc! f p ?: ');
					if 'y' in ask.lower(): crypt = True



			if crypt: _docs.switch('Files',path); _docs.action();
	_open.switch('Files',path); _open.action();

	# if not os.path.isfile(path):
	#     _.saveText()

def new_file_defaults(fi):
	global fo; global epoch;
	path=fo+fi
	if os.path.isfile(path): return None

	# if fi.endswith('.md'):
		


def action():
	# _.pr( _v.fig, dic=1 ); return None;
	print('Loading...')
	global epoch; global fo; load();
	print('Loaded')

	if _.switches.isActive('Change-Dir'):

		if _.isWin:
			os.system('cd /d  "'+fo+'"')
			# os.chdir(fo)
		else:
			os.system('cd "'+fo+'"; $SHELL;')
		return None

	path = fo
	
	if _.switches.isActive('Fi'):
		for fi in _.switches.values('Fi'):
			files(fi)
			new_file_defaults(fi)
		return None
	no = path+'notes.md'
	# _.pr(no,c='cyan')

	# if not os.path.isfile(no): _.saveText('# '+_.isDate(epoch,f='date')+'\n___\n## today\n- one\n\n~~~\n\n~~~\n___\n',no)
	if not os.path.isfile(no): _.saveText('# '+_.isDate(epoch,f='date')+'\n\n___\n\n## project\n',no)


	# _cryptFi = _.getTable('secure-crypt-local.meta')
	# ef=False
	# for k in _cryptFi.keys():
	#     print(k)
	#     if k.lower() == no.lower():
	#         print('yes')
	#         ef=True
	# print(no)
	# if ef:
	# _.pr('C3P0-pre')
	_.pr("__.setting('Crypt-daily/notes.md-Default') = "+str(__.setting('Crypt-daily/notes.md-Default')),pvs=1)
	# _.pr('C3P0-post')
	if no in _.getTable('secure-crypt-local.meta'):
		_.pr('entire file is encrypted',c='red')
	elif __.setting('Crypt-daily/notes.md-Default'):
		_.pr('file is particularly encrypted',c='red')
		_docs.switch('Files',no); _docs.action();
	
	if _.switches.isActive('Print'): _md.switch('View-Webpage'); _md.switch('Files',no); _md.action();

	if False and not _.isWin:
		os.system( 'nano '+ no )
	else:
		if _.switches.isActive('Open'): _md.switch('Files',no); _md.action();
		else: _open.switch('Files',no); _open.action();


colors='''ColorBold.gray
ColorBold.red
ColorBold.green
ColorBold.yellow
ColorBold.blue
ColorBold.magenta
ColorBold.cyan
ColorBold.white
Color.purple
Color.cyan
Color.darkcyan
Color.blue
Color.green
Color.yellow
Color.red
Color.bold
Background.red
Background.green
Background.yellow
Background.blue
Background.purple
Background.light_blue
Background.grey
Background.black
BackgroundGrey.black
BackgroundGrey.red
BackgroundGrey.green
BackgroundGrey.brown
BackgroundGrey.blue
BackgroundGrey.magenta
BackgroundGrey.cyan
BackgroundGrey.gray
BackgroundGreyBold.black
BackgroundGreyBold.red
BackgroundGreyBold.green
BackgroundGreyBold.blue
BackgroundGreyBold.magenta
BackgroundGreyBold.cyan
BackgroundGreyBold.gray'''.split('\n')
_all_colors_tact_='''ColorBold.gray
ColorBold.red
ColorBold.green
ColorBold.yellow
ColorBold.blue
ColorBold.magenta
ColorBold.cyan
ColorBold.white
Color.purple
Color.cyan
Color.darkcyan
Color.blue
Color.green
Color.yellow
Color.red
Color.bold
Background.red
Background.green
Background.yellow
Background.blue
Background.purple
Background.light_blue'''.split('\n')
def have_a_cow():
	global colors
	global _all_colors_tact_
	# sys.exit()
	os=__.imp('os.path.isdir')
	cfo=_v.rtp+'projects/cows/flock/'.replace('/',os.sep)
	# print(cfo)
	if os.path.isdir(cfo):
		files=[]
		for path in _.fo(cfo):
			files.append(path)
		# _.pr(_.getText(random.choice(files),raw=True),c=random.choice(_all_colors_tact_))
		_.ad(random.choice(files),'cow')

def have_some_cows():
	# _.clear()
	cows=random.choice([1,2,3,4])
	if _.switches.isActive('Cows'):
		if _.switches.values('Cows'):
			cows=int(_.switches.value('Cows'))

	i=0
	while not i==cows:
		i+=1
		have_a_cow()


def wsl(path):
	if not _.isWin: return path
	subject = path
	git_path = subject
	git_path = git_path.replace( _v.slashes['w'], _v.slashes['u'] )
	git_path = git_path.replace( ':', '' )
	git_path = _v.slashes['u'] + git_path
	wsl5 = '/mnt/'+ git_path[1].lower() + git_path[2:]
	wsl5=wsl5.replace(' ','\\ ')
	return wsl5


import _rightThumb._banners as _banners

		


			# print(path)


# C:\\Users\\Scott\\.rt\\profile\\projects\\cows\\flock

	# _.pr(path)

# def input2(txt=''):
#     # p = input(txt)
#     line=''
#     i=0
#     while True:
#         i+=1
#         if i > 1000: break
#         try:
#             line = input(txt)
#         except EOFError:
#             pass
#             clear()
#             # return line

#     return line
os=__.imp('os.system')
os=__.imp('os.chdir')
import random
# p organize-files-by-date
import _rightThumb._dir as _dir
########################################################################################
if __name__ == '__main__':
	# if _.switches.isActive('mf'):
	#     if _.switches.values('mf'):
	#         clear=1
	#     else: clear=0
	#     if _.switches.isActive('Color'):
	#         _banners.mf(clear,c=_.switches.value('Color'))
	#     else:
	#         _banners.mf(clear)

	#     sys.exit()
	if _.switches.isActive('Cows'):
		have_some_cows()
		sys.exit()
	_.pr('##### #t) '+_.isDate(time.time(),f='iso'),c='ColorBold.gray')
	action()
	__.isExit()




