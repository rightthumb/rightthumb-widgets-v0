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
	_.switches.register( 'Files', '-f,-fi,-file,-files' )
	_.switches.register( 'Clip', '-clip' )
	_.switches.register( 'exiftool', '-exif,-exiftool' )
	# _.switches.register( 'MP3', '-mp3' )
	# _.switches.register( 'Save', '-save', isRequired=True )
	pass

# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('require-list',[])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'ffmpeg-clip.py',
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


########################################################################################
# START

def cf(string):
	if len(string)==1:
		return '0'+string
	return string

def timex3(string):
	# 00:00:24.57
	t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
	ab=string.split('-')
	a=timexEa1(ab[0])
	b=timexEa1(ab[1])
	diff=b['rt']-a['rt']
	t.a=str(a['r2'])
	t.b=str(b['r2'])
	return t
	# t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
	# p=string.split('-')
	# if p[0].count(':') == 1:
	#     tas=p[0].split(':')[1]
	#     t.a='00:'+cf(p[0].split(':')[0])+':'+cf(tas)
	# elif p[0].count(':') == 2:
	#     tas1=cf(p[0].split(':')[0])
	#     tas2=cf(p[0].split(':')[1])
	#     tas3=cf(p[0].split(':')[2])
	#     # t.a=str( tas1+tas2+tas3  )
	#     t.a='tas1:tas2:tas3'.replace('tas1',tas1).replace('tas2',tas2).replace('tas3',tas3)
	# if p[1].count(':') == 1:
	#     tbs=p[1].split(':')[1]
	#     t.b='00:'+cf(p[1].split(':')[0])+':'+cf(tbs)
	# elif p[1].count(':') == 2:
	#     tas1=cf(p[1].split(':')[0])
	#     tas2=cf(p[1].split(':')[1])
	#     tas3=cf(p[1].split(':')[2])
	#     t.b='tas1:tas2:tas3'.replace('tas1',tas1).replace('tas2',tas2).replace('tas3',tas3)
	# return t

def timex2(string):
	t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
	ab=string.split('-')
	a=timexEa1(ab[0])
	b=timexEa1(ab[1])
	diff=b['rt']-a['rt']
	t.a=str(a['r3'])
	t.b=str(b['r3'])
	return t
	# # 00:00:24.57
	# t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
	# p=string.split('-')
	# if p[0].count(':') == 1:
	#     tas=p[0].split(':')[1]
	#     t.a='00:00:'+cf(p[0].split(':')[0])+'.'+tas
	# elif p[0].count(':') == 2:
	#     tas1=cf(p[0].split(':')[0])
	#     tas2=cf(p[0].split(':')[1])
	#     tas3=cf(p[0].split(':')[2])
	#     # t.a=str( tas1+tas2+tas3  )
	#     t.a='00:tas1:tas2.tas3'.replace('tas1',tas1).replace('tas2',tas2).replace('tas3',tas3)
	# if p[1].count(':') == 1:
	#     tbs=p[1].split(':')[1]
	#     t.b='00:00:'+cf(p[1].split(':')[0])+'.'+tbs
	# elif p[1].count(':') == 2:
	#     tas1=cf(p[1].split(':')[0])
	#     tas2=cf(p[1].split(':')[1])
	#     tas3=cf(p[1].split(':')[2])
	#     t.b='00:tas1:tas2.tas3'.replace('tas1',tas1).replace('tas2',tas2).replace('tas3',tas3)
	# return t



def timex(string):
	t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
	ab=string.split('-')
	a=timexEa1(ab[0])
	b=timexEa1(ab[1])
	diff=b['rt']-a['rt']
	t.a=str(a['ra'])
	t.b=str(b['ra'])
	return t
	# t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
	# p=string.split('-')
	# if p[0].count(':') == 1:
	#     tas=p[0].split(':')[1]
	#     t.a=str(  (int(p[0].split(':')[0])*60)+int(tas) )
	# elif p[0].count(':') == 2:
	#     tas1=(int(p[0].split(':')[0])*60)*60
	#     tas2=(int(p[0].split(':')[1])*60)
	#     tas3=int(p[0].split(':')[2])
	#     t.a=str( tas1+tas2+tas3  )
	# if p[0].count(':') == 1:
	#     tbs=p[1].split(':')[1]
	#     t.b=str(  (int(p[1].split(':')[0])*60)+int(tbs) )
	# elif p[1].count(':') == 2:
	#     tas1=(int(p[1].split(':')[0])*60)*60
	#     tas2=(int(p[1].split(':')[1])*60)
	#     tas3=int(p[1].split(':')[2])
	#     t.b=str( tas1+tas2+tas3  )
	# return t

def timex99(string):
	t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
	p=string.split('-')
	if p[0].count(':') == 1:
		tas=p[0].split(':')[1]
		t.a=str(  (int(p[0].split(':')[0])*60)+int(tas) )
	elif p[0].count(':') == 2:
		tas1=(int(p[0].split(':')[0])*60)*60
		tas2=(int(p[0].split(':')[1])*60)
		tas3=int(p[0].split(':')[2])
		t.a=str( tas1+tas2+tas3  )
	if p[0].count(':') == 1:
		tbs=p[1].split(':')[1]
		t.b=str(  (int(p[1].split(':')[0])*60)+int(tbs) )
	elif p[1].count(':') == 2:
		tas1=(int(p[1].split(':')[0])*60)*60
		tas2=(int(p[1].split(':')[1])*60)
		tas3=int(p[1].split(':')[2])
		t.b=str( tas1+tas2+tas3  )
	return t.a,t.b

def timexINT(string):
	t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
	ab=string.split('-')
	a=timexEa1(ab[0])
	b=timexEa1(ab[1])
	diff=b['rt']-a['rt']
	t.a=str(a['rt'])
	t.b=str(b['rt'])
	return t


	# p=string.split('-')
	# if p[0].count(':') == 1:
	#     tas=p[0].split(':')[1]
	#     t.a=str(  (int(p[0].split(':')[0])*60)+int(tas) )
	#     return 0,int(p[0].split(':')[0]),int(tas)
	# elif p[0].count(':') == 2:
	#     tas1=int(p[0].split(':')[0])
	#     tas2=int(p[0].split(':')[1])
	#     tas3=int(p[0].split(':')[2])
	#     return tas1,tas2,tas3
	#     t.a=str( tas1+tas2+tas3  )
	# if p[0].count(':') == 1:
	#     tbs=p[1].split(':')[1]
	#     t.b=str(  (int(p[1].split(':')[0])*60)+int(tbs) )
	#     return 0,int(p[1].split(':')[0]),int(tbs)
	# elif p[1].count(':') == 2:
	#     tas1=int(p[1].split(':')[0])
	#     tas2=int(p[1].split(':')[1])
	#     tas3=int(p[1].split(':')[2])
	#     return tas1,tas2,tas3
	#     t.b=str( tas1+tas2+tas3  )
	# return t

def timexEa1(text):
	def t1b(nu):
		if nu < 10:
			return '0'+str(nu)
		else:
			return str(nu)
	tt={}
	tt['d']=0
	tt['h']=0
	tt['m']=0
	tt['s']=0
	tt['r3']=''
	tt['r2']=''
	tt['ra']=''
	tt['rt']=0
	p=[]
	seg=text.split(':')
	seg.reverse()
	for i,se in enumerate(seg):
		if i==0: tt['s']=int(se)
		if i==1: tt['m']=int(se)
		if i==2: tt['h']=int(se)
		if i==3: tt['d']=int(se)
	tti={
			'r3': [],
			'r2': [],
			'ra': [],
			'rt': 0,
	}
	if tt['d']: tti['r3'].append(t1b(tt['d']));    tti['r2'].append(t1b(tt['d']));    tti['ra'].append(t1b(tt['d']));    tti['rt'] += ((tt['d']*60)*60)*60;
	if tt['h']: tti['r3'].append(t1b(tt['h']));    tti['r2'].append(t1b(tt['h']));    tti['ra'].append(t1b(tt['h']));    tti['rt'] += (tt['h']*60)*60
	else: tti['r3'].append('00');
	if tt['m']: tti['r3'].append(t1b(tt['m']));    tti['r2'].append(t1b(tt['m']));    tti['ra'].append(t1b(tt['m']));    tti['rt'] += tt['m']*60
	else: tti['r3'].append('00');       tti['r2'].append('00');
	if tt['s']: tti['r3'].append(t1b(tt['s']));    tti['r2'].append(t1b(tt['s']));    tti['ra'].append(t1b(tt['s']));    tti['rt'] += tt['s']
	# if tt['s']:
	#     tti['r3'].append(t1b(tt['s']))
	#     tti['r2'].append(t1b(tt['s']))
	#     tti['ra'].append(t1b(tt['s']))
	#     print(tti['rt'])
	#     print(tt['s'])
	#     tti['rt'] += tt['s']
	else: tti['r3'].append('00');       tti['r2'].append('00');

	tt['r3'] = ':'.join(tti['r3'])
	tt['r2'] = ':'.join(tti['r2'])
	tt['ra'] = ':'.join(tti['ra'])
	tt['rt'] = tti['rt']
	tt['rts'] = str(tti['rt'])

		
	# print(tt)
	# sys.exit()
	return tt

def _time_(string,ff='ra',l=False):
	t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
	rt=_time2_(string,ff,l)
	t.a=str(rt[0])
	t.b=str(rt[1])
	return t

def _time2_(string,ff='ra',l=False):
	ab=string.split('-')
	a=timexEa1(ab[0])
	b=timexEa1(ab[1])
	aa=str(a[ff])
	bb=str(b[ff])
	diff=b['rt']-a['rt']
	if l:
		ab=str(datetime.timedelta(seconds=diff)).split(':')
		ba=[]
		for tm in ab:
			if len(tm) == 1: ba.append( '0'+tm )
			else: ba.append( tm )
		bb=':'.join(ba)

	return aa,bb

def clean(text):
	text=_str.do('+x',text)
	text=_str.do('be',text,' ')
	text=_str.do('be',text,'\n')
	text=_str.do('be',text,' ')
	return text
def clean2(text):
	text=clean(text)
	text=_str.do('dup',text,'\n')
	return text

def exif_process(path):
	if not os.path.isfile(path):
		_.e('no file: '+path)
	_.pr('path:\n',path,c='cyan')

	exif_file=_.getText(path,raw=True)
	exif_file=clean2(exif_file)
	first=1
	fields={}
	records=[]
	for line in exif_file.split('\n'):
		if line.startswith('ExifTool Version Number'):
			if not first: records.append(fields);
			fields={}
			first=0
		else:
			if ':' in line:
				f = line[0:line.index(':')]
				b = line[len(f)+1:len(line)]
				f = clean(f)
				b = clean(b)
				fields[f]=b
				# print(fields);sys.exit();
	# records
	# _.pv(records)
	records2=[]
	for rec in records:
		# pars=rec['File Name'].replace('.mp4','').split('__')[1].split('-')
		ab=rec['File Name'].replace('.mp4','').split('__')[1].replace('.',':').split('-')
		a=timexEa1(ab[0])
		b=timexEa1(ab[1])
		diff=b['rt']-a['rt']
		_.linePrint()
		print(ab)
		print(a)
		print(b)
		print(diff)

		# pre=rec['File Name'].replace('.mp4','').split('__')[1].replace('.',':')
		# pars=timex99(pre)
		# # print(pre,pars)
		# # length = int(pars[1]) - int(pars[0])
		# # print(length)
		# # print(length,pars,pre)
		# # print()
		# print()
		# print()





def action():
	if _.switches.isActive('exiftool'): exif_process(_.switches.value('exiftool')); return None;
	global  c3po
	#--> min, architecture {:strict:}
	# s=_.switches.values('Save')[0]
	# tt=
	# _.pr(tt)
	clips=_.switches.values('Clip')
	if ' ' in clips[0]:
		clips=clips[0].split(' ')
	for t2 in clips:
		# print(t2)
		# t=timex(t2)
		# t=timex2(t2)
		# t=timex3(t2)
		t=_time_(t2,'ra',l=True)
		for i, path in enumerate( _.switches.values('Files') ):
			if os.path.isfile(path):
				info=_dir.info(path)
				fx='ffmpeg -i ff1 -ss aaa -t bbb -acodec copy -vcodec copy ff2'.replace('aaa',t.a).replace('bbb',t.b).replace('ff1',info['name']).replace('ff2','clip-'+str(_.HID('ffmpeg-clip'))+'-'+info['name'].replace('.'+info['ext'].lower(),'').replace('.'+info['ext'].upper(),'').replace('.'+info['ext'],'')+t.c+'.'+info['ext'])
				# fx='ffmpeg -i ff1 -ss aaa -to bbb -c copy ff2'.replace('ff1',info['name']).replace('ff2','clip-'+str(_.HID('ffmpeg-clip'))+'-'+info['name'].replace('.'+info['ext'].lower(),'').replace('.'+info['ext'].upper(),'').replace('.'+info['ext'],'')+t.c+'.'+info['ext']).replace('aaa',t.a).replace('bbb',t.b)
				# fx='ffmpeg -nostdin -ss "aaa" -i "ff1" -to "bbb" -c copy -map 0 "ff2"'.replace('ff1',info['name']).replace('ff2','clip-'+str(_.HID('ffmpeg-clip'))+'-'+info['name'].replace('.'+info['ext'].lower(),'').replace('.'+info['ext'].upper(),'').replace('.'+info['ext'],'')+t.c+'.'+info['ext']).replace('aaa',t.a).replace('bbb',t.b)
				# fx='mencoder -ss aaa -endpos bbb -oac pcm -ovc copy ff1 -o ff2'.replace('ff1',info['name']).replace('ff2','clip-'+str(_.HID('ffmpeg-clip'))+'-'+info['name'].replace('.'+info['ext'].lower(),'').replace('.'+info['ext'].upper(),'').replace('.'+info['ext'],'')+t.c+'.'+info['ext']).replace('aaa',t.a).replace('bbb',t.b)
				_.pr(fx)
				# if _.switches.isActive('MP3'):
				#     fx='ffmpeg -i ff2 ff2.mp3'.replace('aaa',t.a).replace('bbb',t.b).replace('ff1',info['name']).replace('ff2','clip-'+str(_.HID('ffmpeg-clip'))+'-'+info['name'].replace('.'+info['ext'].lower(),'').replace('.'+info['ext'].upper(),'').replace('.'+info['ext'],'')+t.c+'.'+info['ext'])
				#     _.pr(fx)
		del t
def load():
	global  c3po

# os=__.imp('os.sep')
import os
import _rightThumb._dir as _dir
"""
p ffmpeg-clip -f piller-10-2.mp4 -clip "0:38-7:03" | p execute
p ffmpeg-clip -f piller-01.mp4 -clip "4:38-7:24 11:26-13:35 17:54-19:30" | p execute
p ffmpeg-clip -f piller-02.mp4 -clip "0:04-2:20 9:53-12:28 27:37-30:06 32:27-32:55" | p execute
p ffmpeg-clip -f piller-03.mp4 -clip "24:57-27:02 44:12-45:33" | p execute
p ffmpeg-clip -f piller-04.mp4 -clip "4:00-6:20 10:38-13:25 26:10-29:28" | p execute
p ffmpeg-clip -f piller-05.mp4 -clip "29:07-32:16 45:40-47:05 48:10-48:20" | p execute
p ffmpeg-clip -f piller-07-1.mp4 -clip "57:03-1:01:02" | p execute
p ffmpeg-clip -f piller-07-2.mp4 -clip "13:51-16:20 28:19-30:47 40:45-43:58" | p execute
p ffmpeg-clip -f piller-09.mp4 -clip "28:46-32:08 44:51-45:26" | p execute
p ffmpeg-clip -f piller-10-1.mp4 -clip "1:45-4:53" | p execute
p ffmpeg-clip -f piller-10-2.mp4 -clip "1:13-6:29 33:20-37:15 50:52-54:55 1:02:39-1:03:47" | p execute

p ffmpeg-clip -f piller-11.mp4 -clip "28:46-31:57 43:25-45:22" | p execute
p ffmpeg-clip -f piller-12-1.mp4 -clip "18:05-20:31 55:01-57:57" | p execute
p ffmpeg-clip -f piller-12-2.mp4 -clip "9:21-12:31 26:24-28:56 43:29-46:28" | p execute
p ffmpeg-clip -f piller-13.mp4 -clip "28:50-32:10 43:58-45:26 49:51-53:33" | p execute

p ffmpeg-clip -f piller-14-1.mp4 -clip "10:42-13:40" | p execute
p ffmpeg-clip -f piller-14-2.mp4 -clip "4:55-8:11 23:55-27:06 29:54-32:39" | p execute

p ffmpeg-clip -f piller-15.mp4 -clip "5:52-6:34 53:32-54:50" | p execute
p ffmpeg-clip -f piller-16.mp4 -clip "59:37-1:02:30 1:24:45-1:27:59" | p execute
p ffmpeg-clip -f piller-17.mp4 -clip "1:23:33-1:26:56 1:31:50-1:32:55" | p execute
"""

import datetime
# str(datetime.timedelta(seconds=666))
# '0:11:06'


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




