#!/usr/bin/python3
# alt+29 ↔ is space
 

# 1674156772

MINI_ADS = False
MINI_ADS = True

# ¯\_(ツ)_/¯

# sudo apt install libpython2.7-stdlib
# import json

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

#--> min, architecture {:strict:}
#--> trigger/callback  <w#
#--> todo#> meta to scan for

#--> start#> i dont remember what this is but it looks important
# for i, line, bi in _.numerate( _.isData(r=0) ):
#     #--> _.nindex(bi,h,n)  =  line.index(n)
#     _.pr(line)
# _.pr('ready',c='green')
#-->   end#> i dont remember what this is but it looks important


import glob
import sys,os,time,datetime,threading
# from os.path import isfile, isdir
# import uuid
from operator import itemgetter
from datetime import datetime as dt, timedelta
from datetime import date
# from threading import Timer
# import simplejson as json
# try:
#   import sqlite3
# except Exception as e:
#   pass

'''
simplejson = __.imp('simplejson')
simplejson.loads(var)
simplejson.dumps(rows, indent=4, sort_keys=False, default=str)
simplejson.dumps(rows, sort_keys=False, default=str)
'''

def cross_multiplication(dic):
	try:
		n=0
		if type(dic['a']) == int or type(dic['a']) == float: n=n+1
		if type(dic['b']) == int or type(dic['b']) == float: n=n+1
		if type(dic['c']) == int or type(dic['c']) == float: n=n+1
		if type(dic['d']) == int or type(dic['d']) == float: n=n+1
		if not n == 3:
			raise ValueError("bad fields")
	except Exception as ee:
		e('cross_multiplication: (structural error) missing-dic: a/b  c/d',ee)
	which='error'
	w='a'
	if not type(dic[w]) == int and not type(dic[w]) == float: which='a'
	w='b'
	if not type(dic[w]) == int and not type(dic[w]) == float: which='b'
	w='c'
	if not type(dic[w]) == int and not type(dic[w]) == float: which='c'
	w='d'
	if not type(dic[w]) == int and not type(dic[w]) == float: which='d'
	try:
		w='a'
		if not type(dic[w]) == int and not type(dic[w]) == float: return (float(dic['b'])*float(dic['c']))/float(dic['d'])
		w='b'
		if not type(dic[w]) == int and not type(dic[w]) == float: return (float(dic['a'])*float(dic['d']))/float(dic['c'])
		w='c'
		if not type(dic[w]) == int and not type(dic[w]) == float: return (float(dic['a'])*float(dic['d']))/float(dic['b'])
		w='d'
		if not type(dic[w]) == int and not type(dic[w]) == float: return (float(dic['b'])*float(dic['c']))/float(dic['a'])
	except Exception as ee:
		pr(dic,pvs=1)
		pr(which)
		pr(type(dic['a']))
		pr(type(dic['b']))
		pr(type(dic['c']))
		pr(type(dic['d']))
		e('cross_multiplication: bad dic',ee)

def numerate(asset,label='one'):
	row=0
	i=-2
	new=[]
	# print( len('\n'.join(asset)) )
	# print( '\n'.join(asset).index('23') )
	for ii,ass in enumerate(asset):
		# print(len(ass))
		i+=1
		if ii:
			b=i
		else:
			b=i+1
		e=i+len(ass)
		i=e
		new.append( ( ii,ass,b ) )
	return new

def nindex(b,haystack,needle):
	if not needle in haystack: return -1
	if b == 0: return haystack.index(needle);
	else: return haystack.index(needle)+1+b;



def chScan(i,needle,label='one'):
	global numerate_data
	numerate_data[label]={}


def fometa(path,end=''):
	meta = {}
	if os.path.isdir(path):
		folder = __.path(path)
	elif os.path.isfile(path):
		folder = __.path(path,pop=True)
	else:
		folder = __.path(path)

	i=0

	while not os.path.isfile( folder+os.sep+'.folder.meta'+end ):
		i+=1
		if i > 100:
			break
		#     e('missing folder meta')
		try:
			folder = __.path(folder,pop=True)
		except Exception as ee:
			break
	if os.path.isfile(folder+os.sep+'.folder.meta'+end):
		mPath = folder+os.sep+'.folder.meta'+end
		if getText( mPath, raw=True ).strip().startswith('{'): meta = getTable2( mPath )
		else: meta = getYML( mPath )
		meta['folder']=folder
		return meta
	return {}


def json_(data,simp=False,s=None):
	if not s is None: simp=s;
	simplejson = __.imp('simplejson')
	if type(data) == str:
		return simplejson.loads(data)
	if not simp:
		return simplejson.dumps(data, indent=4, sort_keys=False, default=str)
	return simplejson.dumps(data, sort_keys=False, default=str)


def print_pr(text):
	if not '_rightThum'+'b._base3 ' in text:
		return text
	text=text.replace('\r','')
	lines=[]
	for line in text.split('\n'):
		replace=False
		if line.startswith('print('):
			replace=True
		elif '.print(' in line:
			replace=False
		elif line.startswith('def ') or '\t def ' in line or ' def ' in line:
			replace=False
		else:
			replace=True

		
		if replace:
			line=line.replace('print(','_.pr(')
		line=line.replace('def _.pr(', 'def print(')
		line=line.replace('def  _.pr(', 'def print(')
		line=line.replace('def   _.pr(', 'def print(')
		lines.append(line)
	return '\n'.join(lines)

try: print_ed;
except Exception as e: print_ed=[];

_all_colors_='''ColorBold.gray
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
_all_colors_nobk_='''ColorBold.gray
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
Color.bold'''.split('\n')
_all_colors_nobk_='''ColorBold.gray
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
Color.bold'''.split('\n')
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

def random_color():
	global _all_colors_
	global _all_colors_nobk_
	global _all_colors_tact_
	import random
	return random.choice(_all_colors_tact_)

print_ed_group={}
def print_(*args,p=None,c=None,pad=3,g=None,end=None,pvs=None,pv=None,json=None, dic=None, line=None, rstrip=True):
	args=list(args)
	if c == 'r' or c == 'random': c=random_color()

	if p is None: rint=True;
	elif p: rint=True;
	elif not p: rint=False;
	else: rint=True;

	if json:
		simplejson=__.imp('simplejson'); args[0]=simplejson.dumps(args[0], indent=4, sort_keys=False, default=str);
		if rint:
			print(args[0])
		return args[0]
	# if pvs: pvs=None; pv=1;

	if dic == 5:
		for i,a in enumerate(args):
			if type(a) == dict: args[i] = str(a).replace('{','').replace('}','').replace("'",'').replace(', | ',' | ')

	if not dic and type(dic) == bool or ( type(dic) == int and dic == 1): printDicFields(args[0]); return None
	try:
		if not end is None and (type(end) == bool or type(end) == int) and end:   end='\r';
		else:
			if not end is None and not end == '\r':   end=None
		if pvs and not p: return printVarColor_OLD(args[0])
		
		if pvs:
			if type(args[0]) == str:
				return printVarSimpleFake(args[0])
				
			try:
				if type(args[0]) == dict or type(args[0]) == list: return printVarSimple(args[0])

			except: return printVarSimpleFake(args[0])

		if pv: return printVar(args[0])
		if json: simplejson=__.imp('simplejson'); args[0]=simplejson.dumps(args[0], indent=4, sort_keys=False, default=str);
		if not line is None and line:
			args=[linePrint(c=c,p=0)]
		global print_ed; global print_ed_group; items=[];
		pre=''
		# if not g is None:
		# print_ed_group
		for arg in args:
			if type(arg) == list:
				tmp=[]
				for rg in arg: tmp.append(str(rg));
				items.append( ' '.join(tmp) )
			else:
				items.append(str(arg))
		prn=pre+' '.join(items)
		if rstrip: prn=prn.rstrip()
		if not c is None: prn=cp( prn, c, p=0 );
		if p is None: rint=True;
		elif p: rint=True;
		elif not p: rint=False;
		else: rint=True;
		if rint:
			if not end is None: print( linePrint(txt=' ',p=0) , end=end ); print( prn, end=end );
			# if not end is None: print( '                                                                                        ' , end=end ); print( prn, end=end );
			else: print( prn );
		print_ed.append(prn)
		return prn
	except Exception as e:
		return ''

fo_fi2=[]
def fo2( folder=None, r=False, script=None, trigger=None, test=None, first=True ):
	'''
	#n)--> fo 

	#n)--> trigger: fo_fi2.append(trigger(path))
	#n)-->    test: if test(path): _add_
	#n)-->    script: script(path);
	'''

	def _fo_fi_add(path,trigger,script):
			if not script is None: script(path);
			if not trigger is None: fo_fi2.append(trigger(path))
			else: fo_fi2.append(path)


	if folder is None: folder=os.getcwd()
	global fo_fi2
	if first: fo_fi2=[];
	if not os.path.isdir(folder) and not os.path.isfile(folder): return fo_fi2;
	if not os.path.isdir(folder) and os.path.isfile(folder): folder = __.path(folder,pop=True)
	
	try: files=os.listdir(folder)
	except Exception as ee: return fo_fi2
	for item in files:
		path=folder+os.sep+item; path=__.path(path);

		if not test is None and test(path): _fo_fi_add(path,trigger,script)
			
		if os.path.isfile(path) or os.path.isdir(path):
			if test is None: _fo_fi_add(path,trigger,script)
			if r and os.path.isdir(path): fo2(path,r,script,trigger,test,first=False);
	return fo_fi2



fo_fi=[]
def fo(folder=None,r=False,script=None,first=True):
	if folder is None:
		# try: os=__.imp('os.getcwd');
		# except Exception as e: pass;
		folder=os.getcwd()
	global fo_fi
	if first: fo_fi=[];
	if not os.path.isdir(folder): return fo_fi;
	try:
		files=os.listdir(folder)
	except Exception as e:
		return fo_fi
	for item in files:
		path=folder+os.sep+item
		path=__.path(path)
		if os.path.isfile(path):
			fo_fi.append(path)
			if not script is None: script(path);
		if r and os.path.isdir(path): fo(path,r,script,False);
	return fo_fi

def fos(folder=None,r=False,script=None,first=True):
	if folder is None:
		# try: os=__.imp('os.getcwd');
		# except Exception as e: pass;
		folder=os.getcwd()
	global fo_fi
	if first: fo_fi=[];
	if not os.path.isdir(folder): return fo_fi;
	try:
		files=os.listdir(folder)
	except Exception as e:
		return fo_fi
	for item in files:
		path=folder+os.sep+item
		path=__.path(path)
		if os.path.isdir(path):
			if not script is None: script(path);
			fo_fi.append(path)
			if r: fos(path,r,script,False);
	return fo_fi


def printt( table, cols=None, sort=None,    c=None,s=None  ):
	''' ( table, cols=None, sort=None,    c=None,s=None  ) '''
	if not c is None: cols = c
	if not s is None: sort = s
	if not table: return None;
	global switches
	global tables
	if not sort is None:
		switches.fieldSet( 'Sort', 'active', True )
		switches.fieldSet( 'Sort', 'value', sort )
		switches.fieldSet( 'Sort', 'values', sort.split(',') )
	tables.register( 'ea3dfa23ae6d', table )
	if cols is None: cols=','.join(list(table[0].keys()));
	tables.print( 'ea3dfa23ae6d', cols )

def pa(fi=None,fo=None,dot='',mkdir=True):
	if os.path.isdir(fi): fi=None; fo=fi;
	def _pacl(sub,dot):
		sub=sub.replace('\\',os.sep).replace('/',os.sep)
		sub=_str.do('dup',sub,os.sep)
		if dot: sub=sub.replace(dot,os.sep);
		return sub

	if type(fo) == str: fo=_pacl(fo,dot);
	if type(fi) == str:
		if '/' in fi or '\\' in fi: fo=__.path(_pacl(fi,0),pop=True); fi=__.path(_pacl(fi,0),file=True); fo=_pacl(fo,dot);
	if dot: fo=fo.replace('.',os.sep);


	if not fo is None and not fi is None:
		path=fo+os.sep+fi
	elif not fo is None:
		path=fo
		fi=''
	if mkdir:
		if not os.path.isdir(fo):
			_v.mkdir(fo)
	return path

def string_preview(string,l=30):
	string=str(string)
	if not string:
		return string
	new=''
	broke=False
	for i,x in enumerate(string):
		if i+1 <= l:
			if x == '\t':
				x='\\t'
			if x == '\n':
				x='\\n'
			new+=x
		else:
			broke=True
			new+='... ('+addComma(len(string))+')'
			break
	return new


tinydic_data = []
tinydic_last = {}
tinydic_dic = {}
def tinydic(data,par='',skim=None, mt=True, lan='js', prev=False, dump=None, dic=False, list0=True):
	if type(dump)==str: dump=[dump];
	global tinydic_data
	global tinydic_last
	global tinydic_dic
	def rents(lan,p,k,islist=False,list0=True):
		p2=None
		if islist and list0:
			k='0'
			p2=p+"[{k}]".replace('{k}',k)
		elif type(k)==int:
			k=str(k)
			p2=p+"[{k}]".replace('{k}',k)
		elif lan == 'py':
			p2=p+"['{k}']".replace('{k}',k)
		elif lan == 'js':
			p2=p+".{k}".replace('{k}',k)
		else:
			_.e('type(key)')
		return p2
	if not par:
		# if mt: print_('mt');
		tinydic_data=[]
	if type(data) == list:
		for key, value in enumerate(data):
			par2=rents(lan,par,key,islist=True,list0=list0)
			if dump is None and not prev and skim is None and mt and not par2 in tinydic_data:
				tinydic_data.append(par2)
			if skim is None and not dump is None and (   par2 in dump   ):
				print_(str(key)+':',value)
			tinydic(value,par2,skim,mt,lan,prev,dump,dic,list0)
		if dic: return tinydic_dic;
		return tinydic_data

	if 'items' in dir(data) and 'builtin_function_or_method' in str(type(data.items)):
		child=True
	else:
		tinydic_dic[par] = data
		child=False
		if dump is None and prev and skim is None:
			tinydic_data.append(par+' = '+string_preview(data))
		elif dump is None and not prev and skim is None and not par in tinydic_data:
			tinydic_data.append(par)
		if not skim is None:
			if showLine(str(data)):
				if not dump is None:
					for du in dump:
						if du  in tinydic_last:
							ump=du+': '+ tinydic_last[du]
							if not ump in tinydic_data:
								tinydic_data.append('')
								tinydic_data.append(ump)
				if not par in tinydic_data:
					if prev:
						tinydic_data.append(par+' = '+string_preview(data))
					else:
						tinydic_data.append(par)
				tinydic_last={}

	if child:
		for key, value in data.items():
			par2=rents(lan,par,key)
			if not skim is None and not dump is None and key in dump:
				for du in dump:
					if key == du:
						tinydic_last[du]=value
			if skim is None and not dump is None and (   key in dump   or   par2 in dump   ):
				print_(str(key)+':',value)
			if dump is None and not prev and skim is None and mt and not par2 in tinydic_data:
				tinydic_data.append(par2)
			tinydic(value,par2,skim,mt,lan,prev,dump,dic,list0)
	if dic: return tinydic_dic;
	return tinydic_data


def tailpop(subject,delim):
	parts=subject.split(delim)
	parts.reverse()
	e=parts.pop(0)
	parts.reverse()
	return delim.join(parts)

def tab(val,n=None, t='    ', cnt=False, add=None,  s=False):

	if n is None and add is None and not s and not cnt:
		n=1

	def shortest(lines):
		p=None
		for i,line in enumerate(lines):
			l=_str.do('be',line, ' ')
			a=len(line)
			b=len(l)
			d=a-b
			if p is None:
				p=d
			elif b and d < p:
				p=d
		return p
	def shorten(lines):
		p=shortest(lines)
		for i,line in enumerate(lines):
			l=_str.do('be',line, ' ')
			if len(l):
				lines[i] = line[p:]
			else:
				lines[i] = ''
		return lines



	val = val.replace('\t',t)
	val = val.replace('\r','')
	val = _str.do('be',val, '\n')
	# val = _str.do('all',val, ' \n')
	lines = val.split('\n')

	if cnt:
		p=shortest(lines)
		



	if s:
		lines=shorten(lines)

	if not add is None and add:
		for i,line in enumerate(lines):
			l=_str.do('be',line, ' ')
			if len(l):
				lines[i] = t + line
			else:
				lines[i] = ''
	if not n is None and n:
		i=0
		pre=''
		while not i == n:
			i+=1
			pre+=t
		print_('n',n,'|'+pre+'|')
		for i,line in enumerate(lines):
			l=_str.do('be',line, ' ')
			if len(l):
				lines[i] = pre+line
			else:
				lines[i] = ''
	return '\n'.join(lines)

def ll(subject,d=' '): return subject.split(d);

def rev(string):
	a=list(string)
	a.reverse()
	a=''.join(a)
	return a

def n2w(n,c=None):
	d=None
	s=str(n)
	if '.' in s:
		n=int(s.split('.')[0])
		# d=int(s.split('.')[1])
	try:
		import num2word
	except Exception as ee:
		e(ee)

	r = num2word.word(n)
	if not d is None:
		r += ' and '+n2w(d).replace('Hundred','Hundredth').replace('Thousand','Thousandth').replace('Million','Millionth').replace('Billion','Billionth').replace('Trillion','Trillionth')
		if not c is None:
			result = colorThis( r, c )
	return r

def aiBullet(string,depth=None,d=None):
	if type(string) == int:
		s=depth
		d=string
		string=s
		depth=d
	if not d is None:
		depth=d
	if depth is None:
		return '\n                  - '+string
	code='\n                  '
	i=0
	while not i==depth:
		i+=1
		code+='  '
	return code+'- '+string

def aiLine(string,lines=2):

	if type(string) == int:
		s=lines; l=string;
		string=s; lines=l;

	if lines==2:
		return '\n\n                '+string
	else:
		return '\n                '+string

def over(txt,note='',r=None,l=None):
	end=False
	if r: end=True;
	# print_('note',note)
	ss=txt
	if len(note):
		if end:
			ss=rev(ss)
			note=rev(note)

		s=''
		i=0
		nd=len(note)-1
		for ch in ss:
			if i > nd:
				s+=ch
			elif ch in '{-}':
				s+=ch
			else:
				s+=note[i]
			
			if not ch in '{-}':
				i+=1
		ss=s
		if end:
			ss=rev(ss)
			note=rev(note)
	return ss



def ddelim( txt=None, what='szYZhw', d=None, indices=None, f=1, r=-1 ):
	if what.lower() in ll('uuid guid'):
		what = 'uuid'
	def uu(p,r,u):
		if p:
			cp(['in section',u,r], 'Background.red')
		return u
	p=0
	u=0
	ec='yellow'
	ec='Background.light_blue'
	def eeof(u,p,ec,d,r,what,txt,note=None):
		if p:
			if note is None:
				cp([{'r':r, 'u':u, 'p':p, 'd':d,'what':what}],'yellow')
			else:
				cp([{'*':note, 'r':r, 'u':u, 'p':p, 'd':d,'what':what}],'yellow')
			cp(['e',txt],ec)
		return txt
	if txt is None:
		_.cp('ddelim( txt=None, indices=[8, 12, 16, 20], d='-' )','yellow')
		sys.exit()

	specified=1
	
	if d is None:
		specified=0
		# d='-'
	if indices is None:
		specified=0
		# indices=[8, 12, 16, 20]
	if p:
		print_(1,txt)
	if f:
		txt=_str.stripNonAlphaNumaric(txt,'.').replace(' ','')
	if p:
		cp(['~',what,len(txt)],'cyan')
		cp( [specified,txt,what,d], 'white' )
	
	if specified:
		pass
	elif what in '{} [] () <>'.split(' '):
		u=uu(p,r,1)
		new_string=what[0]+txt+what[1]
		return eeof(u,p,ec,d,r,what,new_string)

	elif what == 'uuid2':
		u=uu(p,r,2)
		d='-'; indices=[8, 12, 16, 20];
		txt=ddelim( txt, d=d, indices=indices, f=0, r=u )
		txt=ddelim( txt, what='{}', f=0, r=u )
		return eeof(u,p,ec,d,r,what,txt).replace('{','').replace('}','')
	elif what == 'uuid':
		u=uu(p,r,2)
		d='-'; indices=[8, 12, 16, 20];
		txt=ddelim( txt, d=d, indices=indices, f=0, r=u )
		txt=ddelim( txt, what='{}', f=0, r=u )
		return eeof(u,p,ec,d,r,what,txt)
	elif what == 'time':
		u=uu(p,r,3)
		if len(txt) == 6:
			d=':'; indices=[2, 4];
		elif len(txt) == 4:
			d=':'; indices=[2];
		return eeof(u,p,ec,d,r,what,ddelim( txt, d=d, indices=indices, f=0, r=u ))

	elif what == 'date':
		u=uu(p,r,4)
		d='-'; indices=[4, 6];
		return eeof(u,p,ec,d,r,what,ddelim( txt, d=d, indices=indices, f=0, r=u ))
	elif what in 'dt ts timestamp date-time stamp'.split(' '):
		u=uu(p,r,5)
		txtt=ddelim( txt, d=' ', indices=[8], f=0, r=u )
		if p:
			cp(['txtt',txtt],'darkcyan')
		# sys.exit()
		a=ddelim( txtt.split(' ')[0], what='date', f=0, r=u )
		b=ddelim( txtt.split(' ')[1], what='time', f=0, r=u )
		txt=a+' '+b
		return eeof(u,p,ec,d,r,what,txt)
	elif indices is None:
		cp('ELSE','red')
		print_('-----------',what,txt)
		eeof(u,p,ec,d,r,what,txt,note='WTF')
		e('ELSE')

	# print_(2,txt)

	original = txt
	delimiter = d


	if p and d == ' ':
		cp(['**',txt,what,d,indices],'red')

	new_string = ''
	for i,ch in enumerate(txt):
		new_string += ch
		if i+1 in indices:
			new_string += d
	return eeof(u,p,ec,d,r,what,new_string)
	return eeof(u,p,ec,d,r,what,new_string)



	prev = 0
	for index in indices:
		if p:
			print_('ind',what,(prev,index),original[prev:index])
		new_string += original[prev:index] + delimiter
		prev = index
	new_string += original[prev:]
	return eeof(u,p,ec,d,r,what,new_string)
delimiter=ddelim

def clear():
	global isWin
	if isWin:
		os.system('cls')
	else:
		os.system('clear')

def rstr(code,o,c):
	i=o-1
	txt=''
	while not i == c:
		i+=1
		txt+=code[i]
	return txt

def get_supporting_line(data,i,b=';',rev={}):
	if type(data) == list:
		data = ''.join(data)
	eol=vindex(data,i,n='\n')
	# print_('eol',eol)
	if eol == {}:
		eol=len(data)
	if eol > len(data)-1:
		eol=len(data)-2
	line = data[ i: eol+1 ].replace('\n','')
	ii=i-1
	ip=i-1
	pre=''
	# for c in line:
	#   ip+=1
	#   cc=data[ip]
	#   if cc in '({[':
	#       break
	#   else:
	#       if cc in ')}]':
	#           print_('rev',rev)
	#           print_('xxxxxxxxxxxxxxxxx',cc,ip)
	#           print_( ip in rev )
	#           print_( ip+1 in rev )
	#           print_( ip-1 in rev )
	#           print_( ip+2 in rev )
	#           print_( ip-2 in rev )
	#           if ip in rev:
	#               print_('here here here here here here here here here here here ')
	#               ipx=vindex(data,rev[ip],n='\n',r=True)
	#               pre=data[ ipx: ip ]
	#               print_( 'pre pre', pre )
	#               break
	#           sys.exit()
	#       pre+=cc
	# print_('pre',pre)
	while True:
		ii+=1
		if ii>=len(data): break;
		c=data[ii]
		if c == '\n' or ( len(b) and c == b ): break;
		if c in '({[':
			y=vindex(data,ii)
			if ii in y:
				ii=y[ii]
			else:
				iii=ii
				while not iii in y:
					iii+=1
					if iii in y:
						ii=y[iii]
						if iii >= len(data):
							ii=len(data)
				# print_(ii,c,y)
				# sys.exit()
		
	return pre+data[i:ii]

def idlen(_len):
	if type(_len)==str: _len=len(_len)
	if not _len: return ''
	result=''
	while not len(result) > _len:
		result+=genUUID3()
	return result[0:_len]

def strip_comments(data,comment='#'):
	dex=qindex(data)
	inde={}
	for o in dex:
		c=dex[o]+1
		if not data[o:c] in inde:
			inde[data[o:c]]=idlen(len(data[o:c]))
		data = data[0:o] + inde[data[o:c]] + data[c: ]
	datal=data.split('\n')
	for i,line in enumerate(datal):
		if comment in line:
			par=line.split(comment)
			line=par[0]
			par.pop(0)
			datal[i]=line.split(comment)[0]
	data='\n'.join(datal)

	for quo in inde:
		data=data.replace(inde[quo],quo)

	return data

def ephemeral_strip(data,comment='#',script=None):
	comments={}

	dex=qindex(data)
	inde={}
	for o in dex:
		c=dex[o]+1
		if not data[o:c] in inde:
			inde[data[o:c]]=idlen(len(data[o:c]))
		data = data[0:o] + inde[data[o:c]] + data[c: ]
	datal=data.split('\n')
	for i,line in enumerate(datal):
		if comment in line:
			par=line.split(comment)
			line=par[0]
			par.pop(0)
			comments[i]=comment+comment.join(par)
			datal[i]=line.split(comment)[0]
	data='\n'.join(datal)
	data=_str.do('sh',data)
	#n)--> stuff stripped out

	try: data=script(data)
	except Exception as e: pass

	datal=data.split('\n')
	#n)--> adding stuff back in
	for i,line in enumerate(datal):
		if i in comments: datal[i]+=comments[i]

	for quo in inde:
		data=data.replace(inde[quo],quo)

	return data

def qindex( data, comment='#' ):
	''' find ids of all quotes including triplet avoiding comments 

	def print_all_quotes():
		data = '\n'.join(_.isData())
		dex=_.qindex(data)
		print(dex)
		for o in dex:
			c=dex[o]+1
			_.pr( data[o:c] )
	'''
	dex={}
	def qtest(data,i):
		try: data[i]; return True;
		except: return False
		return False
	i=0
	while qtest(data,i):
		c=data[i]
		if c == comment:
			eof=False
			while not data[i] == '\n':
				i+=1; exec("try:data[i]\nexcept:eof=True");
				if eof: i-=1; break;
		if c in '`"'+"'":
			vi=vindex(data,i,comment=comment)
			if i in vi:
				dex[i]=vi[i]
				i=vi[i]+1
			else: i+=1
		else: i+=1
	return dex


def vindex(  code, i=0, esc='\\', n='', v=True,r=False,both=True, sort=True, isArg=False, comment='//' ):
	ari=i
	if isArg: a_='-+'
	else: a_=''
	def _sort(sort,dic):
		if not sort: return dic;
		ks=list(dic.keys()); ks.sort(); new={};
		for k in ks: new[k]=dic[k];
		return new

	if type(code)==list:
		code=''.join(code)
	at=i
		
	table={}
	
	table['brackets'] = {}
	table['brackets']['i']=0
	table['brackets']['open'] = {}

	table['braces'] = {}
	table['braces']['i']=0
	table['braces']['open'] = {}

	table['par'] = {}
	table['par']['i']=0
	table['par']['open'] = {}
	index={}

	i-=1
	while True:
		i+=1
		if i >= len(code):
			break
		c=code[i]
		try:
			c2=c+code[i+1]
		except Exception as e:
			c2=''
		try:
			c3=c2+code[i+2]
		except Exception as e:
			c3=''
		try:
			c4=c3+code[i+3]
		except Exception as e:
			c4=''
		try:
			c5=c4+code[i+4]
		except Exception as e:
			c5=''
		if len(esc) == 1 and c==esc:
			i+=1
		else:
			if len(esc) == 1 and c==esc:
				i+=1
			if n=='\n' and r:
				ii=i
				c=code[i]
				while not ii == 0 and c == '\n':
					ii-=1
					c=code[ii]
					if ii == 0:
						return 0
					elif c == '\n':
						return ii

			elif len(n) == 1 and c==n:
				return i
			elif len(n) == 2 and c2==n:
				return i+1
			elif len(n) == 3 and c3==n:
				return i+2
			elif len(n):
				pass
			else:
				if not n and c in '0123456789.':
					cx = c
					ii=i-1
					while cx in '0123456789.':
						ii+=1
						try:
							cx=code[ii]
						except Exception as e:
							ii-=1
							index[i] = ii
							if both:
								index[ii] = i
							break
					index[i] = ii
					if both:
						index[ii] = i
					i=ii
				elif not n and c in a_+'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
					cx = c
					ii=i-1
					while cx in a_+'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._':
						ii+=1
						try:
							cx=code[ii]
						except Exception as e:
							ii-=1
							index[i] = ii
							if both:
								index[ii] = i
							break

					index[i] = ii
					if both:
						index[ii] = i
					i=ii
				elif not n and c3 == '"""':
					ss=vindex(code,i+3,esc,n='"""',v=0,isArg=isArg,comment=comment)
					if type(ss)==int or i in ss:
						if type(ss)==int: s=ss
						else: s=ss[i]
						index[i] = s
						if both:
							index[s] = i
						i=s+2
				elif not n and c3 == "'''":
					ss=vindex(code,i+3,esc,n="'''",v=0,isArg=isArg,comment=comment)
					# if i in ss: s=ss[i]
					if type(ss)==int or i in ss:
						if type(ss)==int: s=ss
						else: s=ss[i]
						index[i] = s
						if both:
							index[s] = i
						i=s+2
				elif not n and c == "'":
					ss=vindex(code,i+1,esc,n="'",v=0,isArg=isArg,comment=comment)
					if type(ss)==int or i in ss:
						if type(ss)==int: s=ss
						else: s=ss[i]
						index[i] = s
						if both:
							# print(index,s,i,type(index),c)
							index[s] = i
						i=s
					# else: pr('err',i,ss,c='yellow')
				elif not n and c == '"':
					ss=vindex(code,i+1,esc,n='"',v=0,isArg=isArg,comment=comment)
					if type(ss)==int or i in ss:
						if type(ss)==int: s=ss
						else: s=ss[i]
						index[i] = s
						if both:
							index[s] = i
						i = s
				elif not n and c2 == '/*':
					i = vindex(code,i+2,esc,n='*/',v=0,isArg=isArg,comment=comment)
				elif not n and len(comment)==1 and c == comment and not code[ari] in '`"'+"'":
					i = vindex(code,i+1,esc,n='\n',v=0,isArg=isArg,comment=comment)+1
				elif not n and len(comment)==2 and c2 == comment and not code[ari] in '`"'+"'":
					i = vindex(code,i+2,esc,n='\n',v=0,isArg=isArg,comment=comment)+1


				elif not n and c == '{':
					table['brackets']['i']+=1
					table['brackets']['open'][table['brackets']['i']]=i
				elif not n and c == '}':
					try:
						s=table['brackets']['open'][table['brackets']['i']]
					except Exception as e:
						return _sort(sort,index)
					index[ s ]=i
					if both:
						index[ i ]=s
					table['brackets']['i']-=1
					if s==at:
						return _sort(sort,index)
				elif not n and c == '[':
					table['braces']['i']+=1
					table['braces']['open'][table['braces']['i']]=i
				elif not n and c == ']':
					try:
						s=table['braces']['open'][table['braces']['i']]
					except Exception as e:
						return _sort(sort,index)
					index[ s ]=i
					if both:
						index[ i ]=s
					table['braces']['i']-=1
					if s==at:
						return _sort(sort,index)
				elif not n and c == '(':
					table['par']['i']+=1
					table['par']['open'][table['par']['i']]=i
				elif not n and c == ')':
					try:
						s=table['par']['open'][table['par']['i']]
					except Exception as e:
						return _sort(sort,index)
					index[ s ]=i
					if both:
						index[ i ]=s
					table['par']['i']-=1
					if s==at:
						return _sort(sort,index)
	return _sort(sort,index)








try:
	import colorama
	colorama.init()
except Exception as e:
	pass

# from threading import Thread


import _rightThumb._construct as __
import _rightThumb._vars as _v
import _rightThumb._string as _str

__.sw=__.dot()
__.sw.PlusCode=[]


__.print_path = False
######################################################

if os.path.isfile( _v.py+_v.slash+'thread.py' ):
	print_( 'rm thread' )
	os.unlink( _v.py+_v.slash+'thread.py' )

######################################################

def find_all(a_str, sub):
	return list(find_all_do(a_str, sub))

def find_all_do(a_str, sub):
	start = 0
	while True:
		start = a_str.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub)

# def substring_range( text, o, c ):
	

######################################################

_bm=None
def bAlias(subject):
	# print_(type(subject))
	if type(subject) == str:
		subjects = [subject]
	elif type(subject) == list:
		subjects = subject
	else:
		print_(type(subject))
		err( 'bAlias', subject )

	results=[]


	for sub in subjects:
		if os.path.isdir(sub):
			results.append(sub)
		else:
			global _bm
			if _bm is None:
				import _rightThumb._bookmarks as _bm
			
			made={}
			if 'wprofile' in _v.config_hash:
				made['h'] = 1
				h  = _v.config_hash['wprofile']
			if 'ww' in _v.config_hash:
				made['ww'] = 1
				ww = _v.config_hash['ww']
			# print_('made',made)
			if 'ww' in made  and 'h' in made:
				a = ww+os.sep+'databank'+os.sep+'tables'+os.sep+'bookmarks.index'
				b = h+os.sep+'tables'+os.sep+'bookmarks.index'
				# print_(os.path.isfile(b))
				try:
					if not os.path.isfile(b) and os.path.isfile(a):
						from shutil import copyfile
						copyfile(a,b)
				except Exception as e:
					pass
			path = _bm.Bookmarks( sub ).get()
			# print_(sub,path)
			if path is None:
				cp( 'Error, Bookmark does not exist', 'red' )
				results.append(sub)
			elif os.path.isdir(path):
				if path.count(':'):
					parts = path.split(':')
					parts.reverse()
					path = path[0]+':'+parts[0]
				results.append(path)
				# return path
			else:
				cp( 'Error, Bookmark no longer exists', 'red' )
				results.append(sub)
	if type(subject) == str and len(results):
		return results[0]
	elif type(subject) == str and not len(results):
		return subject
	elif type(subject) == list:
		return results

######################################################

def reFormatSize( start ):
	start = start.replace( ' ', '' )
	start = start.replace( ',', '' )
	start = start.replace( '?', '' )
	b = unFormatSize( start )
	end = formatSize( b )
	return end

######################################################

class Meta_Namespace():
	def __init__( self ):
		pass
dot=Meta_Namespace
__.tableLine = '‽'
v = dot()
vv = dot()
v.isData = {}
vv.opened_file_me = {}
__.switch_skimmer = dot()
__.switch_skimmer.scan = [ '??','-??','--??','/??' ]
__.switch_skimmer.active = []

__.aggregate = dot()
__.aggregate.eof = dot()
__.aggregate.eof.storage = {}
__.aggregate.obj = None
__.aggregate.prefixes = {
							'eot?':  1,
							'eof?':  1,
							'eog?':  1,
							'bog?':  1,
							'eoga?': 1,
							'run?':  1,
						}

__.aggregate.group_prefixes = {
							'eog?':  1,
							'bog?':  3,
							'eoga?': 1,
							'run?':  2,
						}
__.aggregate.fn = dot()
# '?date' '?comma' '?size' '?bytes'
__.aggregate.fn.format = {
							'add': '?comma',
							'isDate': '?date',
						}
__.aggregate.fn.order = {
							'isDate': 1
						}

# if self.groupID_KEY in item and item[self.groupID_KEY].endswith('-B'):


__.terminal = dot()
try:
	# cols, rows
	__.terminal.width, __.terminal.height = list( os.get_terminal_size() )
except Exception as e:
	# try:
	#   __.terminal.height, __.terminal.width = os.popen('stty size', 'r').read().split()
	# except Exception as e:
	__.terminal.width = 0
	__.terminal.height = 0

# print_(__.terminal.width)

__.terminal.cols = __.terminal.width


######################################################

def path_sep(subject):
	if type(subject) == list:
		s = []
		for x in subject:
			s.append( path_fix(x) )
		subject = s
	if type(subject) == str:
		subject = subject.replace( os.sep+os.sep, os.sep )
		subject = subject.replace( os.sep+os.sep, os.sep )
	return subject

######################################################
_bm = None


def stripColor(text):
	if '0m' in text and '[' in text:
		pass
	else:
		return text
	import re
	ansi_escape = re.compile(r'''
		\x1B  # ESC
		(?:   # 7-bit C1 Fe (except CSI)
			[@-Z\\-_]
		|     # or [ for CSI, followed by a control sequence
			\[
			[0-?]*  # Parameter bytes
			[ -/]*  # Intermediate bytes
			[@-~]   # Final byte
		)
	''', re.VERBOSE)
	return ansi_escape.sub('', text)



def ordinal(n):
	suf = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))
	return suf(n)


def back():
	global _bm
	if _bm is None:
		import _rightThumb._bookmarks as _bm
	return _bm.Bookmarks( 'back' ).get()
files_all=[]
def files( folder, r=0, first=True ):
	global files_all
	if first:
		files_all = []
	if os.path.isdir(folder):
		dirList = os.listdir(folder)
		for item in dirList:
			path = __.path(folder +_v.slash+ item)
			try:
				if os.path.isfile(path):
					files_all.append(item)
				if r and os.path.isdir(path):
					files(path,r=1,first=False)
			except Exception as ee:
				print_(path,ee)
	return files_all

def f( search=None, path=False,       p=None, s=None, r=False ):
	if not p is None:
		path = p
	if not s is None:
		search = s
	if r:
		path = r
	records = []
	result = None
	for file in files( back() ):
		if search is None:
			if path:
				if r:
					return __.path(back()+_v.slash+file)
				records.append(__.path(back()+_v.slash+file))
				result = __.path(back()+_v.slash+file)
			else:
				records.append(file)
				result = file
		elif search.lower() in file.lower():
			if path:
				if r:
					return __.path(back()+_v.slash+file)
				records.append(__.path(back()+_v.slash+file))
				result = __.path(back()+_v.slash+file)
			else:
				records.append(file)
				result = file
	if not path:
		cp( ' '.join(records), 'darkcyan' )
	elif path == 1:
		for record in records:
			cp( record, 'darkcyan' )
	return result

def chmod(path):
	global switches
	if not __.isWin and os.path.isfile(path) and switches.isActive('chmod'):
		try:
			os.chmod( path, 0o777 )
		except Exception as e:
			pass

class HD:

	def chmod(path):
		global switches
		if not __.isWin and os.path.isfile(path) and switches.isActive('chmod'):
			try:
				os.chmod( path, 0o777 )
			except Exception as e:
				pass

def printDicFields( dic ):
	for k in dic:
		dic[k] = str(dic[k])
	global switches
	if switches.isActive('TableJSON'):
		if len(switches.value('TableJSON')):
			saveTable2( dic, switches.values('TableJSON')[0] )
			cp( [ 'saved:', switches.values('TableJSON')[0] ], 'green' )
		else:
			# printVarSimple(self.asset)
			print_( d2json(dic) )
		return None

	for k in dic:
		fields.register( 'dic', 'field', str(k)+':' )
		fields.register( 'dic', 'value', str(dic[k]) )

	for k in dic:
		print_( fields.value( 'dic', 'field', str(k)+':', right=True ), fields.value( 'dic', 'value', str(dic[k]) ) )

arrow = None
_tz = None
pandas = None
_sd = None

def date_diff_dic(one,two=time.time()):
	
	def date_diff_in_seconds(dt2, dt1):
	  timedelta = dt2 - dt1
	  return timedelta.days * 24 * 3600 + timedelta.seconds

	def dhms_from_seconds(seconds):
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		days, hours = divmod(hours, 24)
		return (days, hours, minutes, seconds)
	def dt_mf(foo):
		foo=float(foo)
		return foo
	one=dt_mf(autoDate(one))
	two=dt_mf(autoDate(two))
	# print(one,type(one))
	# print(two,type(two))
	oneA=one
	twoA=two
	if two > one:
		one=datetime.datetime.fromtimestamp(one)
		two=datetime.datetime.fromtimestamp(two)
	else:
		a=one
		b=two
		two=datetime.datetime.fromtimestamp(a)
		# print('mf',two,type(two))
		one=datetime.datetime.fromtimestamp(b)
		# print(one)
	xXx=dhms_from_seconds(date_diff_in_seconds(two, one))
	# print(xXx)
	# print("\n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_in_seconds(two, one)))
	txt='{ "d": %d, "h": %d, "m": %d,  "s": %d }' % dhms_from_seconds(date_diff_in_seconds(two, one))
	# dic=dict("{ 'd': %d, 'h': %d, 'm': %d,  's': %d }" % dhms_from_seconds(date_diff_in_seconds(two, one)))
	simplejson=__.imp('simplejson')
	dic=simplejson.loads(txt)
	# print(dic)
	# print((dic))
	if dic['s']==59:
		dic=date_diff_dic(oneA+1,twoA)
		if dic['s']==58:
			dic=date_diff_dic(oneA-1,twoA)
	return dic

def isDate( theDate=None, record={}, tz=None, q=True, f=None,w=None,what=None ):
	if type(record) == str: e('expected: f='+record)
	# record={}
	if (type(theDate) == int or type(theDate) == float) and theDate < 1:
		return 0
	# if (type(theDate) == int or type(theDate) == float): return theDate
	if theDate is None: theDate=time.time();
	if not w is None: f=w;
	if not what is None: f=what;

	# theDate = autoDate(theDate)

	# print_(theDate)
	# sys.exit()

	global _dir
	if _dir is None:
		import _rightThumb._dir as _dir

	s = time.time()
	# slow from loading pandas
	if not tz is None and not len(tz):
		tz = None



	local_tz = str(time.strftime("%z")).replace(':','')


	hasTZ = False
	if type(theDate) == str and len(theDate) > 11:
		if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
			hasTZ = theDate[-6:].replace(':','')

	if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
		if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
			hasTZ = theDate[-5:].replace(':','')
	epoch = autoDate(theDate)



	_dow_ = {
				'Sunday': 'sun',
				'Monday': 'mon',
				'Tuesday': 'tue',
				'Wednesday': 'wed',
				'Thursday': 'thu',
				'Friday': 'fri',
				'Saturday': 'sat',
	}


	def fitem(f):
		if f=='ago': return _dir.dateDiffText(epoch);
		if f=='ago-dic':
			ad=_2dates(epoch,dic=1); del ad['txt'];
			return ad;
		if f=='ago-txt': return _2dates(epoch)
		if f=='friendly': return friendlyDate( epoch );
		if f=='friendly': return friendlyDate( epoch );
		if f=='iso': return friendlyDate( epoch ).replace( ' ', 'T' ) + local_tz;
		if f=='woy': return _dir.getWeekAndYear( epoch );
		if f=='month': return _dir.getMonthFromEpoch( epoch );
		if f=='epoch': return epoch;
		if f=='ordinal': return datetime.datetime.fromtimestamp( epoch ).toordinal();
		if f=='text-date': return datetime.datetime.fromtimestamp( epoch ).strftime('%b, %d %Y');
		if f=='text-time': return datetime.datetime.fromtimestamp( epoch ).strftime('%I:%M %p');
		if f=='text-datetime': return datetime.datetime.fromtimestamp( epoch ).strftime('%b, %d %Y @ %I:%M %p');
		if f=='sdate': return friendlyDate2( epoch );
		if f=='strip': return onlyNumbers_strip(friendlyDate( epoch ).split(' ')[0]);
		if f=='strip': return onlyNumbers_strip(friendlyDate( epoch ).split(' ')[0]);
		if f=='stript': return onlyNumbers_strip(friendlyDate( epoch ));
		if f=='stripa': return onlyNumbers_strip(friendlyDate( epoch ))[:-2];
		if f=='date': return friendlyDate( epoch ).split(' ')[0];
		if f=='time': return friendlyDate2( epoch ).split(' ')[1];
		if f=='fdate': return friendlyDate( epoch );
		if f=='fdatea': return friendlyDate( epoch )[:-3];
		if f=='cmd': return friendlyDate( epoch )[:-3].replace(' ',' @ ').replace('-','.').replace(':','.');
		if f=='month': return _dir.getMonthFromEpoch( epoch );
		if f=='year': return friendlyDate( epoch ).split('-')[0]
		if f=='year2': return _dir.getYearFromEpoch( epoch ); # prioritizes week over actual year (if jan 01 and week 52 of last year)
		if f=='woy': return _dir.getWeekAndYear( epoch );
		if f=='woy2': return _dir.getWeekAndYear( epoch ).replace(str(_dir.getYearFromEpoch( epoch ))+'.','');
		if f=='ago': return _dir.dateDiffText( epoch );
		if f=='days': return daysDiff(  epoch, time.time()  );
		if f=='dow': return _dir.getDOWromEpochText( epoch );
		if f=='dow2': return _dow_[_dir.getDOWromEpochText( epoch )];
		if f=='tz': return local_tz;
		if f=='fo': return day(epoch);
		if f in 'crypt-date crypt-time crypt-epoch appID app crypt-pass'.split(' '):
			try:
				import _rightThumb._nID as _nID
				try:
					# _keychain = regImp( __.appReg, 'keychain' )
					# nID_password = _keychain.imp.key('nID')
					# _nID.mini.password( nID_password )
					_nID.mini.password( appID_nID_password() )
					isPass = 'secure'
				except Exception as e:
					_nID.mini.password( '1970' )
					isPass = 'unsecure'
				eee = ''
				try:
					ee = str(record['epoch'])
					for c in ee:
						if '.' == c:
							break
						eee+=c
				except Exception as e:
					eee=theDate
					# print_(f,1,'err:', e)
				pass

				if f=='crypt-date': return _nID.mini.gen( record['strip'] );
				if f=='crypt-time': return _nID.mini.gen( record['stript'] );
				try:
					if f=='crypt-epoch': return _nID.mini.gen( int(eee) );
					if f=='appID' or f=='app': return _nID.mini.gen( int(eee) );
				except Exception as ee:
					print_(f,2,'err:', ee)
					sys.exit()
				if f=='crypt-pass': return isPass;
			except Exception as ee:
				print_(f,3,'err:',ee)
				pass
		if f=='stardate':
			try:
				import _rightThumb._stardate as _sd
				return _sd.gen(  epoch  )
			except Exception as e:
				return None
		if f=='quarter':
			dt = friendlyDate( epoch ).split(' ')[0].split('-')
			try:
				return str(record['year']) +'.'+ str(pandas.Timestamp(datetime.date( int(dt[0]) , int(dt[1]), int(dt[2]))).quarter)
			except Exception as e:
				return None
		if f=='true': return True;
		if f=='dow':
			dow=_dir.getDOWromEpochText( epoch ).lower()
			dci = {
					'monday': 'mon',
					'tuesday': 'tue',
					'wednesday': 'wed',
					'thursday': 'thu',
					'friday': 'fri',
					'saturday': 'sat',
					'sunday': 'sun',
			}
			if dow in dci:
				return dci[dow]
			return dow
		return None



	#########################################################
	pass
	if f:
		if type(f)==list:
			f=' '.join(f)
		f=f.replace(',',' ')
		if not ' ' in f:
			return fitem(f)
		else:
			j={}
			for q in f.split(' '):
				j[q] = fitem(q)
			return j








	#########################################################

	# pv(_v.config_hash)
	if 'noarrow' in _v.config_hash:
		local_tz = ''
	else:
		global _tz
		if _tz is None:
			import _rightThumb._tz as _tz
		
		if not type(hasTZ) == bool:
			if not hasTZ == local_tz:
				epoch = _tz.convert( epoch, hasTZ, local_tz )
		if not tz is None and not local_tz == tz:
			epoch = _tz.convert( epoch, local_tz, tz )
			local_tz = tz

			if '/' in tz:
				global arrow
				if arrow is None:
					import arrow
				utc = arrow.utcnow()
				theDate = str(utc.to(tz))
				hasTZ = False
				if type(theDate) == str and len(theDate) > 11:
					if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
						hasTZ = theDate[-6:].replace(':','')

				if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
					if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
						hasTZ = theDate[-5:].replace(':','')
				local_tz = hasTZ

	

	if not epoch:
		return record

	global pandas
	if pandas is None:
		if q:
			try:
				#  pandas  takes .5 seconds to load 
				import pandas
			except Exception as e:
				pass

	ss = time.time()



	if type(epoch) == str:
		epoch = autoDate(epoch.replace('z',''))

	todo='ago ago-dic ago-txt epoch ordinal text-date text-time text-datetime sdate strip stript stripa date time fdate fdatea cmd month year woy woy2 dow dow2 days tz iso fo'

	for k in todo.split(' '):
		record[k]=isDate(epoch,f=k)

	# record['ago'] = _dir.dateDiffText(epoch)
	# record['epoch'] = epoch
	# # print_( epoch )
	# record['ordinal'] = datetime.datetime.fromtimestamp( epoch ).toordinal()
	# # sys.exit()
	# record['text-date'] = datetime.datetime.fromtimestamp( epoch ).strftime('%b, %d %Y')
	# record['text-time'] = datetime.datetime.fromtimestamp( epoch ).strftime('%I:%M %p')
	# record['text-datetime'] = datetime.datetime.fromtimestamp( epoch ).strftime('%b, %d %Y @ %I:%M %p')
	# record['sdate'] = friendlyDate2( epoch )
	# record['strip'] = onlyNumbers_strip(friendlyDate( epoch ).split(' ')[0])
	# record['stript'] = onlyNumbers_strip(friendlyDate( epoch ))
	# record['date'] = friendlyDate( epoch ).split(' ')[0]
	# record['time'] = friendlyDate2( epoch ).split(' ')[1]
	# record['fdate'] = friendlyDate( epoch )
	# record['month'] = _dir.getMonthFromEpoch( epoch )
	# record['year'] = _dir.getYearFromEpoch( epoch )
	# record['woy'] = _dir.getWeekAndYear( epoch )
	# record['woy2'] = _dir.getWeekAndYear( epoch ).replace(str(_dir.getYearFromEpoch( epoch ))+'.','')
	# record['dow'] = _dir.getDOWromEpochText( epoch )
	# # record['ago'] = _dir.dateDiffText( epoch )
	# record['days'] = daysDiff(  epoch, time.time()  )
	# record['tz'] = local_tz
	# # record['iso'] = datetime.datetime.fromtimestamp( epoch ).isoformat()
	# # record['iso'] = datetime.datetime.fromtimestamp( epoch ).replace(microsecond=0).astimezone().isoformat()
	# record['iso'] = record['fdate'].replace( ' ', 'T' ) + record['tz']
	# --------------------------------------------------
	# __.isPass=None
	# def _en_(subject):
	#         try:
	#             import _rightThumb._nID as _nID
	#             if __.isPass is None:
	#                 try:
	#                     # _keychain = regImp( __.appReg, 'keychain' )
	#                     # nID_password = _keychain.imp.key('nID')
	#                     # _nID.mini.password( nID_password )
	#                     _nID.mini.password( appID_nID_password() )
	#                     __.isPass = 'secure'
	#                 except Exception as e:
	#                     _nID.mini.password( '1970' )
	#                     __.isPass = 'unsecure'
	#             eee = ''
	#             ee = str(record['epoch'])
	#             for c in ee:
	#                 if '.' == c:
	#                     break
	#                 eee+=c
	#             # record['crypt-password'] = nID_password
	#             return _nID.mini.gen( subject )
	#         except Exception as e:
	#             return None
	# # iso 24
	# # pv(_v.config_hash)
	# global isWin
	# if isWin:
	#     if 'nocrypt' in _v.config_hash:
	#         pass
	#     else:
	#         sub='strip';val=_en_(record[sub]);
	#         if val: record[sub] = val
	#         sub='crypt-date';val=_en_(record[sub]);
	#         if val: record[sub] = val
	#         sub='crypt-time';val=_en_(record[sub]);
	#         if val: record[sub] = val
	#         sub='crypt-pass';val=_en_(record[sub]);
	#         if val: record[sub] = val
	#         sub='appID';val=_en_(record[sub]);
	#         if val: record[sub] = val

	#         sub='crypt-epoch';val=_en_(int(eee));
	#         if val: record[sub] = val

	#         sub='';val=_en_(record[sub]);
	#         if val: record[sub] = sub

	#         # sub=_en_(record['strip'])
	#         # if sub: record['crypt-date'] = sub
	#         # record['crypt-time'] = _nID.mini.gen( record['stript'] )
	#         # record['crypt-epoch'] = _nID.mini.gen(  )
	#         # record['appID'] = _nID.mini.gen( int(eee) )
	#         # record['crypt-pass'] = __.isPass
	#         del __.isPass
	# --------------------------------------------------

	global isWin
	if isWin:
		if 'nocrypt' in _v.config_hash:
			pass
		else:
			try:
				import _rightThumb._nID as _nID
				try:
					# _keychain = regImp( __.appReg, 'keychain' )
					# nID_password = _keychain.imp.key('nID')
					# _nID.mini.password( nID_password )
					_nID.mini.password( appID_nID_password() )
					isPass = 'secure'
				except Exception as e:
					_nID.mini.password( '1970' )
					isPass = 'unsecure'
				eee = ''
				ee = str(record['epoch'])
				for c in ee:
					if '.' == c:
						break
					eee+=c
				# record['crypt-password'] = nID_password
				record['crypt-date'] = _nID.mini.gen( record['strip'] )
				record['crypt-time'] = _nID.mini.gen( record['stript'] )
				record['crypt-epoch'] = _nID.mini.gen( int(eee) )
				record['appID'] = _nID.mini.gen( int(eee) )
				record['crypt-pass'] = isPass
			except Exception as e:
				pass

		try:
			import _rightThumb._stardate as _sd
			record['stardate'] = _sd.gen(  epoch  )
		except Exception as e:
			pass

		dt = record['fdate'].split(' ')[0].split('-')
		try:
			record['quarter'] = str(record['year']) +'.'+ str(pandas.Timestamp(datetime.date( int(dt[0]) , int(dt[1]), int(dt[2]))).quarter)
		except Exception as e:
			pass

	e = time.time()
	# print_( e-s )
	# print_( e-ss )
	return record


def onlyNumbers_strip(n):
	n = str(n)
	t = ''
	for c in n:
		if c in '0123456789':
			t+=c
	return t



def tfc(c):
	return c.lower().replace(' ','_')


__.table_prefix_padding = 0


# loopPrint(__.table_prefix_padding)
changeC_rc_path = False
changeDate_Table = None
touch_meta = None
_dir = None
# woy_hash_table = None
# def woyTrigger( data ):
#   wks=10000
#   global _dir
#   if _dir is None:
#       import _rightThumb._dir as _dir
#   return _dir.woyTrigger(data)
line_length_hash_table = {}

_vault = None
_blowfish = None
pyAesCrypt = None
shutil = None
_md5 = None
readline = None

win32clipboard = None
__.raw_table = None
class RawTableLength:
	def __init__( self ):
		self.table = []
		self.last = 0
	def table( asset ):
		self.last = len(asset)
		self.table.append(self.last)
	def length( self ):
		return self.last
# def e( asset ):
#   if __.raw_table is None:
#       __.raw_table = RawTableLength()
#   __.raw_table.table( asset )
#   return enumerate(asset)
# def t( asset ):
#   if __.raw_table is None:
#       __.raw_table = RawTableLength()
#   __.raw_table.table( asset )
#   return asset

# def txtTable( txt ):
#   table = []
#   for x in range(0,len(txt)):
#       table.append(txt[x])
#   return table

# def txtTableE( txt ):
#   table = []
#   for x in range(0,len(txt)):
#       table.append(txt[x])
#   return enumerate(table)

def code( script, addString=None ):
	global _code
	try:
		__.code
	except Exception as e:
		_code = regImp( __.appReg, '_rightThumb._auditCodeBase' )

	return __.code.process( script, addString=addString )

aggregate_trigger_ran = False
def aggregate_trigger():
	global aggregate_trigger_ran
	if aggregate_trigger_ran:
		return None
	global switches
	if not switches.isActive('Aggregate'):
		return None
	script = ' '.join( switches.values('Aggregate') )
	__.aggregate.obj.code( script, isSwitch=True )
	



class AGGREGATE:
	def __init__( self ):

		self.records = {}
		self.index = {}
		self.columns = dot()

		self.columns.table = {}
		self.columns.group = {}
		self.columns.eof = {}

		self.columns.eot = {}
		self.columns.otherQ = {}
		self.columns.other = {}

		self.switch = dot()
		self.switch.label = '--sw--c3p0-r2d2-4life--sw--'
		self.switch.processed = False
		# eof eot eog bog eogA

		self.functions = dot()
		self.functions.index = {}
		self.other = dot()
		self.other.index = {}
		self.counter = -1
		self.formating = {}

		self.cache = dot()
		self.cache.records = {}
		self.cache.formating = {}
		self.last = '{D346F128-1468-481C-A0C8-FF8C6083EE64}'
		self.lasting = []
	def code( self, script, label=None, isSwitch=False, addSwitch=False, addAll=False ):
		if script is None:
			return None
		# print_()
		# print_( script )
		# sys.exit()
		self.counter += 1
		if isSwitch:
			label = self.switch.label
			if self.switch.processed:
				return self.records[label]
			self.switch.processed = True
		else:
			if label is None:
				label = 'simple-' + str(self.counter)

		self.records[label] = []
		records = code( script=script, addString=[['alphaParam','?']]  )

		# print_(  )
		# print_( records )
		# print_(  )
		# sys.exit()
		# return None

		indexes = dot()
		indexes.functions = {}
		indexes.table = []
		indexes.group = []
		indexes.eot = []
		indexes.eof = []
		indexes.otherVar = []
		indexes.otherVarQ = []
		indexes.other = []

		for fXn in __.aggregate.fn.order:
			indexes.functions[fXn] = []
		indexes.functions['other'] = []
		for rec in records:
			# print_(rec)
			if rec['status'] and 'function' in rec['l']:
				if rec['txt'] in __.aggregate.fn.order:
					indexes.functions[rec['txt']].append(rec)
				else:
					indexes.functions['other'].append(rec)
				
			elif rec['status'] and 'variable' in rec['l']:
				if not '?' in rec['txt'] or ( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					indexes.table.append( rec )

				elif rec['txt'].startswith('eot?'):
					indexes.eot.append( rec )

				elif rec['txt'].startswith('eof?'):
					indexes.eof.append( rec )

				elif rec['txt'].startswith('eog?'):
					indexes.group.append( rec )

				elif rec['txt'].startswith('bog?'):
					indexes.group.append( rec )

				elif rec['txt'].lower().startswith('eoga?'):
					indexes.group.append( rec )

				elif '?' in rec['txt']:
					indexes.otherVarQ.append( rec )

				else:
					indexes.otherVar.append( rec )
			else:
				indexes.other.append( rec )
		
		tmp_records = []
		for fXn in __.aggregate.fn.order:
			for rec in indexes.functions[ fXn ]:
				tmp_records.append(rec)

		for rec in indexes.functions['other']:
			tmp_records.append(rec)

		for rec in indexes.table:
			tmp_records.append(rec)
		
		for rec in indexes.otherVarQ:
			tmp_records.append(rec)

		for rec in indexes.otherVar:
			tmp_records.append(rec)

		for rec in indexes.group:
			tmp_records.append(rec)

		for rec in indexes.eot:
			tmp_records.append(rec)

		for rec in indexes.eof:
			tmp_records.append(rec)


		for rec in indexes.other:
			tmp_records.append(rec)

		# for rec in tmp_records:
		#   print_(rec)

		# sys.exit()

		for rec in tmp_records:
			self.records[label].append(rec)


		table = {}
		for i,rec in enumerate( self.records[label] ):
			# print_( rec )
			table[ str(rec['i']) ] = str(self.counter) +'-'+ str(i)
			# print_( i, rec )
		# sys.exit()
		for i,rec in enumerate( self.records[label] ):
			self.records[label][i]['i'] = str(self.counter) +'-'+ str(i)
			# print_( rec['i'], i )
		# sys.exit()

		for i,rec in enumerate( self.records[label] ):
			if str( rec['rent'] ) in table:
				self.records[label][i]['rent'] = table[ str( rec['rent'] ) ]
			if 'args' in rec:
				args = []
				for ar in rec['args']:
					if str(ar) in table:
						args.append( table[str(ar)] )
				self.records[label][i]['args'] = args
			if 'p' in rec:
				self.records[label][i]['p'] = table[ str(rec['p']) ]
			if 'val' in rec:
				self.records[label][i]['val'] = table[ str(rec['val']) ]


		for i,rec in enumerate(self.records[label]):
			self.index[rec['i']] = rec

			if rec['status'] and 'function' in rec['l']:
				self.functions.index[rec['i']] = rec 
				
			elif rec['status'] and 'variable' in rec['l']:
				if not '?' in rec['txt'] or ( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					self.columns.table[rec['i']] = rec



				elif rec['txt'].startswith('eot?'):
					self.columns.eot[rec['i']] = rec

				elif rec['txt'].startswith('eof?'):
					self.columns.eof[rec['i']] = rec

				elif rec['txt'].startswith('eog?'):
					self.columns.group[rec['i']] = rec

				elif rec['txt'].startswith('bog?'):
					self.columns.group[rec['i']] = rec

				elif rec['txt'].lower().startswith('eoga?'):
					self.columns.group[rec['i']] = rec

				elif '?' in rec['txt']:
					self.columns.otherQ[rec['i']] = rec

				else:
					self.columns.other[rec['i']] = rec
			else:
				self.other.index[rec['i']] = rec


		# for rec in self.records[label]:
		#   print_( rec )

		# sys.exit()


		self.cache.records[label] = self.records[label]
		self.last = label
		self.lasting = [label]
		# addSwitch addAll
		if addSwitch or addAll:
			return self.build( label=label, addSwitch=addSwitch, addAll=addAll )

		return self.records[label]


	def build( self, label=None, addSwitch=None, addAll=None, s=None ):
		if not s is None:
			addSwitch = s
		if label is None:
			addAll = True
		
		records = []
		toProcess = []
		if addAll:
			for k in self.records:
				toProcess.append(k)

		elif addSwitch:
			if self.switch.label in self.records:
				toProcess.append(self.switch.label)

			if label in self.records:
				toProcess.append(label)
					# print_(rec)
		self.last = '<?>'.join(toProcess)
		self.lasting = toProcess
		if self.last in self.cache.records:
			return self.cache.records[self.last]


		for lab in toProcess:
			for rec in self.records[lab]:
				records.append(rec)



		# else:
		#   cp( 'Error: AGGREGATE.build() ', 'red' )
		#   return []

		indexes = dot()
		indexes.functions = {}
		indexes.table = []
		indexes.group = []
		indexes.eot = []
		indexes.eof = []
		indexes.otherVar = []
		indexes.otherVarQ = []
		indexes.other = []

		for fXn in __.aggregate.fn.order:
			indexes.functions[fXn] = []
		indexes.functions['other'] = []
		for rec in records:
			# print_(rec)
			if rec['status'] and 'function' in rec['l']:
				if rec['txt'] in __.aggregate.fn.order:
					indexes.functions[rec['txt']].append(rec)
				else:
					indexes.functions['other'].append(rec)
				
			elif rec['status'] and 'variable' in rec['l']:
				if not '?' in rec['txt'] or ( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					indexes.table.append( rec )

				elif rec['txt'].startswith('eot?'):
					indexes.eot.append( rec )

				elif rec['txt'].startswith('eof?'):
					indexes.eof.append( rec )

				elif rec['txt'].startswith('eog?'):
					indexes.group.append( rec )

				elif rec['txt'].startswith('bog?'):
					indexes.group.append( rec )

				elif rec['txt'].lower().startswith('eoga?'):
					indexes.group.append( rec )

				elif '?' in rec['txt']:
					indexes.otherVarQ.append( rec )

				else:
					indexes.otherVar.append( rec )
			else:
				indexes.other.append( rec )
		
		tmp_records = []

		for fXn in __.aggregate.fn.order:
			for rec in indexes.functions[ fXn ]:
				tmp_records.append(rec)

		for rec in indexes.functions['other']:
			tmp_records.append(rec)

		for rec in indexes.table:
			tmp_records.append(rec)
		
		for rec in indexes.otherVarQ:
			tmp_records.append(rec)

		for rec in indexes.otherVar:
			tmp_records.append(rec)

		for rec in indexes.group:
			tmp_records.append(rec)

		for rec in indexes.eot:
			tmp_records.append(rec)

		for rec in indexes.eof:
			tmp_records.append(rec)


		for rec in indexes.other:
			tmp_records.append(rec)
		combine_records = []
		for rec in tmp_records:
			combine_records.append(rec)
		
		# print_()
		# # print_( combine_records )
		# print_()

		# for rec in combine_records:
		#   print_(rec)


		# print_( '   self.last:', self.last )
		# print_( 'self.lasting:', self.lasting )
		# sys.exit()
		self.cache.records[self.last] = combine_records
		
		return combine_records


	def formatGen( self, label=None, addSwitch=None, addAll=None, s=None ):
		records = self.build( label=label, addSwitch=addSwitch, addAll=addAll, s=s )

		if self.last in self.cache.formating:
			return self.cache.formating[self.last]


		results = []
		for i,rec in enumerate(records):
			if rec['status'] and 'function' in rec['l'] and 'format' == rec['txt']:
				rXy = []
				for arg in rec['args']:
					rXy.append( self.index[arg]['txt'] )
				results.append( rXy )

			if rec['status'] and 'function' in rec['l'] and rec['txt'] in __.aggregate.fn.format:
				rXy = []
				for arg in rec['args']:
					rXy.append( self.index[arg]['txt'] )

				rXy.append( __.aggregate.fn.format[rec['txt']] )
				results.append( rXy )

			if rec['status'] and 'variable' in rec['l']:
				child = self.index[rec['val']]
				if 'function' in child['l'] and child['txt'] in __.aggregate.fn.format:
					# print_( 'here' )
					rXy = []
					if '?' in rec['txt'] and rec['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
						gc = rec['txt'].split('?')[2]
						rXy.append( gc )
					else:
						rXy.append( rec['txt'] )

					rXy.append( __.aggregate.fn.format[child['txt']] )
					results.append( rXy )

		formating = {}
		for rXy in results:
			fields = []
			cmds = {}

			for res in rXy:
				if not res.startswith('?'):
					fields.append( tfc(res) )
				elif res.startswith('?') and not res.startswith('??') and not res.startswith('???'):
					last = res
					if not res in cmds:
						cmds[res] = {}
				elif res.startswith('???'):
					cmds[last][last2][res] = {}
				elif res.startswith('??'):
					last2 = res
					cmds[last][res] = {}

			
			for f in fields:
				if not f in formating:
					formating[f] = {}
				for c in cmds:
					if not c in formating[f]:
						formating[f][c] = {}
					for p in cmds[c]:
						if not p in formating[f][c]:
							formating[f][c][p] = {}
						for pp in cmds[c]:
							if not pp in formating[f][c][p]:
								formating[f][c][p][pp] = {}
		# printVarSimple( formating )
		# sys.exit()
		self.cache.formating[self.last] = formating
		pass
		return formating

	def format( self, fields, data, label=None, addSwitch=None, addAll=None, s=None ):
		formating = self.formatGen( label=label, addSwitch=addSwitch, addAll=addAll, s=s )
		if not type(fields) is list:
			fields = [fields]
		
		try:
			




			for field in fields:
				f = tfc(field)
				# print_( formating[f] )
				if f in formating:
					if '?date1' in formating[f]:
						return friendlyDate( data )
					if '?date' in formating[f]:
						return friendlyDate2( data )
					if '?size' in formating[f]:
						data = str(data).replace( ',', '' ).replace( ' ', '' )
						# print_('here                                               xx')
						if formating[f]['?size']:
							fm = list(formating[f]['?size'].keys())[0]
							return reFormatSize( str(data)+fm )
						
						# print_( formatSize( int(data) ) )
						return formatSize( int(data) )
					if '?bytes' in formating[f]:
						return unFormatSize( data )
		
					if '?comma' in formating[f]:
						return addComma( data )



		except Exception as e:
			return data
					

		

		return data


__.aggregate.obj = AGGREGATE()

def autoWrapText( text, length=None, txt=False, prefix='', breakOn=None, pre_skip_0=False ):
	if type(prefix) == int:
		n = ''
		i=0
		while i < prefix:
			n += ' '
			i+=1
		prefix=n
	if length is None:
		length = __.terminal.cols-5
	# -copy
	if not pre_skip_0:
		length = length - len(prefix)
	text = str(text)
	if len(text) <= length:
		if not pre_skip_0:
			return prefix+text
		else:
			return text
	if breakOn is None:
		breakAfter = ' ,;(+)\\/.?*&@!_{-}:=`"<~>\'| !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
	else:
		breakAfter = breakOn
	broken = []
	parts = []
	flag = None
	i = 0
	last = -1
	ii = 0
	while i <= len(text)-1:
		ii+=1
		if text[i] in breakAfter:
			flag = i
		if ii > length:
			if not flag is None:
				prt = text[ last+1 : flag+1 ]
				i = flag
				last = flag
			else:
				prt = text[ last+1 : i ]
				last = i-1
			if pre_skip_0 and not parts:
				parts.append(prt)
			else:
				parts.append(prefix+prt)
			flag = None
			ii=0
		i+=1
	if not last == i:
		prt = text[ last+1 : i ]
		if pre_skip_0 and not parts:
			parts.append(prt)
		else:
			parts.append(prefix+prt)

	if txt:
		return '\n'.join(parts)

	return parts

def which(file):
	for path in os.environ["PATH"].split(os.pathsep):
		if os.path.exists(os.path.join(path, file)):
				return os.path.join(path, file)

	return None


pyperclip = None
def setClip(data):
	global pyperclip
	if pyperclip is None:
		import pyperclip
	pyperclip.copy( stripColor(cleanString(data)) )
def getClip():
	global pyperclip
	if pyperclip is None:
		import pyperclip
	return cleanString( pyperclip.paste() )

def cleanString(data):
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	return data

def cleanStringA(data):
	data = _str.cleanBE(data,'\r')
	data = _str.cleanBE(data,'\n')
	data = _str.cleanBE(data,'\r')
	data = _str.cleanBE(data,'\t')
	data = _str.cleanBE(data,' ')
	return data


def path2url(path):
	import pathlib
	return pathlib.Path(os.path.abspath(path)).as_uri()

def autoComplete( table, prompt='> ' ):
	tableX = []
	for x in table:
		x = x.replace( ' ', '_' )
		x = x.replace( '@', '-AT-' )
		tableX.append(x)



	global readline
	if readline is None:
		import readline

	# addrs = ['angela_domain.com', 'angela_gmail.com', 'michael@domain.com', 'david@test.com']

	def completer(text, state):
		options = [x for x in tableX if x.startswith(text)]
		try:
			return options[state]
		except IndexError:
			return None

	readline.set_completer(completer)
	readline.parse_and_bind("tab: complete")
	result = input( prompt )

	found = []
	for x in result.split(' '):
		if x in tableX:
			found.append( table[tableX.index(x)] )
		else:
			found.append( x )

	return found




def getCryptTable( theFile, db=False, bank=False, index=False, temp=False, free=False, password=None ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	global _vault
	global shutil
	global _md5
	global pyAesCrypt
	if _md5 is None:
		import _rightThumb._md5 as _md5
	if shutil is None:
		import shutil
	if pyAesCrypt is None:
		import pyAesCrypt
	if password is None:
		if _vault is None:
			import _rightThumb._vault as _vault
		password =  _md5.md5( _vault.key() )

	the_temp_file = _v.stmp +_v.slash+ '_-cryptTable-'+genUUID()

	# defaults to myTables

	if free:
		file0 = theFile
	elif temp:
		file0 = _v.stmp + _v.slash + theFile
	elif db or bank:
		file0 = _v.dbTables + _v.slash + theFile
	elif index:
		file0 = _v.myIndexes + _v.slash + theFile
	else:
		file0 = _v.myTables + _v.slash + theFile


	if not os.path.isfile(file0):
		file0 = theFile
	if os.path.isfile(file0):
		bufferSize = 64 * 1024
		encFileSize = os.stat(  file0  ).st_size
		with open(  file0, 'rb'  ) as fIn:
			try:
				with open(  the_temp_file , 'wb'  ) as fOut:
					# decrypt file stream
					pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
			except ValueError:
				print_('Err:', 0)
				if os.path.isfile( the_temp_file ):
					print_('Err:', 1)
					os.remove( the_temp_file )
					time.sleep(.2)


		# print_( 'theFile', theFile )
		# print_( 'file0', file0 )
		# import bigjson
		with open(the_temp_file,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
		
		shutil.copyfile( file0, the_temp_file )
		os.unlink(the_temp_file)
		
		return json_data



		# with open( file0, 'rb' ) as f:
			# json_data = bigjson.load(f)
			# json_data = bigjson.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
	else:
		return __.data_default(file=theFile,default=[]).default()



def saveCryptTable( rows, theFile, db=False, bank=False, index=False, temp=False, free=False, indentCode=True, sort_keys=False, archive=False, p=1, password=None, me=0 ):
	HD.chmod(theFile)

	simplejson = __.imp('simplejson')
	global _vault
	global shutil
	global _md5
	global pyAesCrypt
	if _md5 is None:
		import _rightThumb._md5 as _md5
	if shutil is None:
		import shutil
	if pyAesCrypt is None:
		import pyAesCrypt
	if password is None:
		if _vault is None:
			import _rightThumb._vault as _vault
		password =  _md5.md5( _vault.key() )

	the_temp_file = _v.stmp +_v.slash+ '_-cryptTable-'+genUUID()



	# defaults to myTables
	px = ''
	if theFile.startswith('temp'+_v.slash):
		theFile = theFile.replace( 'temp'+_v.slash, '' )
		file0 = _v.stmp + _v.slash + theFile
		px = file0
	elif db or bank:
		theFile = _v.dbTables + _v.slash + theFile
		px = theFile
	elif index:
		theFile = _v.myIndexes + _v.slash + theFile
		px = theFile
	elif free:
			file0 = theFile
			px = theFile
	else:
		if not temp:
			file0 = _v.myTables + _v.slash + theFile
			px = theFile
		else:
			file0 = _v.stmp + _v.slash + theFile
			px = file0

	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
	else:
		dataDump = simplejson.dumps(rows, sort_keys=False, default=str)
	
	if archive:
		import _rightThumb._md5 as _md5

		theFileLabel = theFile
		if _v.slash in theFileLabel:
			global appInfo
			tfl = theFileLabel.split(_v.slash)
			tfl.reverse()
			theFileLabel = str(appInfo[__.appReg]['liveAppName']) + '__' + tfl[0]
		theFileLabel = theFileLabel.replace( '.json', '' )
		theFileLabel = theFileLabel.replace( '.JSON', '' )

		lastMD5 = None
		if os.path.isfile( file0 ):
			lastMD5 = _md5.md5File( file0 )

			backupFile = _v.stmp + _v.slash+'__archive_temp__' + theFileLabel + '__' + genUUID() + '.json'
			





	f = open(the_temp_file,'w')
	f.write( str(dataDump) )
	f.close()
	HD.chmod(theFile)
	bufferSize = 64 * 1024
	# encFileSize = os.stat(  file0  ).st_size
	with open( the_temp_file, 'rb' ) as fIn:
		with open( file0 , 'wb' ) as fOut:
			pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
	
	shutil.copyfile( file0, the_temp_file )
	os.unlink(the_temp_file)

	if archive:
		shouldDocument = False

		if os.path.isfile( file0 ):
			thisMD5 = _md5.md5File( file0 )
		if lastMD5 is None:
			shouldDocument = True
		else:
			if not lastMD5 == thisMD5:
				shouldDocument = True

		if not shouldDocument:
			if os.path.isfile( backupFile ):
				os.remove( backupFile )
		
		if shouldDocument:
			md5Table = getTable( 'table_archive_log.json' )
			found = False
			for i,record in enumerate(md5Table):
				if theFileLabel == record['name']:
					found = True

			theFileLabel
			theFile
			fileDate( theData )


	if p:
		printBold('Saved: ' + px, 'blue')
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );
	return file0



def hex2ascii( hx ):
	if type(hx) == str:
		hx = hx.replace(' ','')
		return ''.join([chr(int(''.join(c), 16)) for c in zip(hx[0::2],hx[1::2])])

	elif not type(hx) == str:
		print_('hex2ascii error')
		sys.exit()



def loopPrint(  length=5, txt=' ', p=0 ):
	if not length:
		return ''
	i=0
	result = ''
	while not i == length:
		result += txt
		i+=1
	if p:
		print_(result)
	return result

lp = loopPrint

def linePrint(  label=None, text=None, txt='_', mn=50, add=5, p=2, c='', x=None,pre='',length=None, center=None ):
	color=c
	if not length is None:
		mn=length
	ln = mn
	if text is None and label is None:
		if length is None and __.terminal.width:
			ln = __.terminal.width
			add = 0

	if not x is None:
		ln=int(ln*x)
	if not label is None:
		global line_length_hash_table
		if not label in line_length_hash_table:
			line_length_hash_table[label] = ln
		else:
			ln = line_length_hash_table[label]
		if not text is None:
			if not p == True and not p == 1:
				p = 0
			if type(text) == str:
				t = len( str(text) )
				if t > ln:
					ln = t
					line_length_hash_table[label] = ln
			elif type(text) == list:
				for texty in text:
					t = len( str(texty) )
					if t > ln:
						ln = t
						line_length_hash_table[label] = ln

	if not center is None:
		if not ln % 2==0:
			ln-=1
		ln=ln/2

	if text is None and ln > 0:
		i = 0
		result = ''
		if add:
			add+=1
		ln += add
		# while not i == ln:
		#     result += txt
		#     i+=1


		r=[]
		# while not i == ln:
		while len(result) < ln:
			result += txt
			r.append(txt)
			i+=1
		if len(result) > ln:
			r.pop(0)
			result=''.join(r)
		res=''
		for i,r in enumerate(result):
			try:
				res+=pre[i]
			except Exception as e:
				res+=result[i]
		result=res


		if not center is None:
			result = result+' '+center+' '+result




		if p:
			if color:
				cp( result, color )
			else:
				print_( result )
		if color:
			result=cp( result, color, p=0 )
		return result



def dic_key_sort( table, n=False ):
	saveTable( table, '-tmp-dic_key_sort.json', tableTemp=True, printThis=False,  sort_keys=True )
	return getTable( '-tmp-dic_key_sort.json', tableTemp=True )
	# dataDump = json.dumps(table, indent=4, sort_keys=True, default=str)
	# print_(dataDump)
	# sys.exit()
	# return json.load( str(dataDump) )



def dic_key_sort2( table, n=False, ip=False, r=False ):


	keys = list( table.keys() )
	dic = {}
	theData = []
	if ip:
		fields.register( 'cnt-ip', 'val', 7, m=3 )
		for x in keys:

			if not x.count('.') == 3:
				theData.append( x )
			else:
				zZz = []

				for y in x.split('.'):
					xXx = fields.padZeros( 'cnt-ip', 'val', int(y) )
					# print_(xXx)

					zZz.append( xXx )
				theData.append( '.'.join(zZz) )
		theData.sort()
		if r:
			theData.reverse()
		for x in theData:
			y = ''
			zZz = []
			if not x.count('.') == 3:
				y = x
			elif x.count('.') == 3:
				for y in x.split('.'):
					# print_(y)
					zZz.append( str(int(y)) )
				y = '.'.join(zZz)
				# print_(y)
			if y in table:
				dic[y] = table[y]
		# print_(theData)
		# printVarSimple(dic)
		# print_()
		return dic



	if not n:
		keys.sort()
		if r:
			keys.reverse()

		for x in keys:
			dic[x] = table[x]
		return dic
	else:
		nKeys = []
		fields.register( 'cnt-n', 'val', 7, m=40 )
		for k in keys:
			nKeys.append(  fields.padZeros( 'cnt-n', 'val', int(k) )  )
		nKeys.sort()
		if r:
			nKeys.reverse()

		for x in nKeys:
			dic[  str(int(x))  ] = table[str(int(x))]
		return dic
def isCrypt(filepath):
	if " ".join(['{:02X}'.format(byte) for byte in     open( filepath, 'rb' ).read(32)    ]).startswith( '41 45 53 02 00 00 1B' ):
		return True
	else:
		return False

def isGz(filepath):
	if " ".join(['{:02X}'.format(byte) for byte in     open( filepath, 'rb' ).read(32)    ]).startswith( '1F 8B 08 08' ):
		return True
	else:
		return False

def isBz2(filepath):
	if " ".join(['{:02X}'.format(byte) for byte in     open( filepath, 'rb' ).read(32)    ]).startswith( '42 5A 68' ):
		return True
	else:
		return False


isTar = dot()
isTar.gz = isGz
isTar.bz2 = isBz2

def sdFile(f):
	return secureDeleteFile(f)

def secureDeleteFile(f):
	result = -1
	if os.path.isfile(f):
		result = 0
		try:
			saveText( zeros(f), f )
			result = 1
		except Exception as e:
			pass

		try:
			os.remove(f)
			result = 2
		except Exception as e:
			pass
	if not result == 2:
		colorThis( [ 'Error: secureDeleteFile', result ], 'red' )

	return result


def zeros3(n,total):
	''' calculating length of output '''
	c=len(str(total))

	result = ''
	a = len(str(n))
	while not len(result)+a == c:
		result += '0'
	result += str(n)
	return result

def zeros2(n,c):
	result = ''
	a = len(str(n))
	while not len(result)+a == c:
		result += '0'
	result += str(n)
	return result

def zeros(n,z='0'):
	if os.path.isfile(fIn):
		n = os.stat(  f  ).st_size

	if not type(n) == int:
		colorThis( "zeros(n,z='0')", 'red' )
		sys.exit()
	x=''
	x+=z
	x+=z
	if n == 0:
		return x
	while not len(x) == n:
		x+=z
	x+=z
	x+=z
	return x

def replaceFile( fIn, fOut ):
	if _v.slash in fOut:
		return fOut

	if fIn == fOut:
		return fOut

	if os.path.isfile(fIn):
		fIn = os.path.abspath( fIn )

	if not _v.slash in fIn:
		return fOut

	parts = fIn.split(_v.slash)
	parts.reverse()
	parts.pop(0)
	parts.reverse()
	return _v.slash.join( parts )+_v.slash+fOut

def patternDiff(a,b):
	# print_('here')
	# a = 'gensslkey'
	# b = 'gensslkey'
	# b = 'gensslkeyz'
	# b = 'ssl_socket_bridge_client_user_administrator_logs_b'
	a = a.lower()
	b = b.lower()
	testing = 0

	if testing:
		print_()
		print_()
		print_('________________________________________________________')
		print_()
		print_()
		print_( a,b )
	x = patternMatch( a, b )
	d = get_change( len(a),len(b) )
	e = get_change( x, d )
	# e = get_change( d, x )
	if testing:
		print_('x',x)
		print_( 'd',d )
		print_( 'e,f',e )
	f = int(100-e)
	f =e
	# print_( 'f',f )
	if f == 0:
		f = 100
	# dd = d
	dd = int(100-d)
	if dd == 0:
		dd = 100
	if testing:
		print_( 'dd',dd )
	# if d <= f:
	if d >= f:
		aa = dd
		bb = f
	else:
		aa = f
		bb = dd
	alphaTest = 'b'
	if alphaTest == 'a':
		kAA = {}
		kAB = {}
		kBA = {}
		kBB = {}
		for ch0 in a:
			if not ch0 in kAA:
				kAA[ch0] = 0
				kAB[ch0] = 0
			if ch0 in b:
				kAA[ch0] += 1
				for ch1 in b:
					kAB[ch0] += 1

		for ch0 in b:
			if not ch0 in kBA:
				kBA[ch0] = 0
				kBB[ch0] = 0
			if ch0 in a:
				kBA[ch0] += 1
				for ch1 in a:
					kBB[ch0] += 1


		theSetA = []
		theSetB = []
		for kk in kAA:
			theSetA.append( percentageDiffIntAuto( kAA[kk], kAB[kk] ) )
		for kk in kAA:
			try:
				theSetB.append( percentageDiffIntAuto( kBA[kk], kBB[kk] ) )
			except Exception as e:
				print_()
				sys.exit()

		# pp = av(theSet)
		pA = av(theSetA)
		pB = av(theSetB)

	elif alphaTest == 'b':
		tA = 0
		tB = 0
		for ch0 in a:
			if ch0 in b:
				tA += 1

		for ch0 in b:
			if ch0 in a:
				tB += 1
		pA = percentageDiffIntAuto( tA, len(a) )
		pB = percentageDiffIntAuto( tB, len(b) )

	if testing:
		print_( 'pA', pA )
		print_( 'pB', pB )

	zz = xMultiply(  [aa,100], [bb,0]  )
	if zz > 100:
		zz = xMultiply(  [bb,100], [aa,0]  )

	if testing:
		print_([aa,100], [bb,0])
		print_(  'diff', zz )
		print_( [aa,bb, pA,pB] )
		print_(  'av', av([aa,bb, pA,pB])  )
	ww = av([aa,bb, pA,pB])
	# if pA > pB:
	#   if pA < ww
	# print_( int(ww), [aa,bb, pA,pB], a, b,  )
	return ww

def av( ds ):
	total = 0
	for x in ds:
		total+=x
	return total / len(ds)

def xMultiply( a, b ):
	fail = False
	if not type(a) == list or not type(b) == list or not len(a) == 2 or not len(b) == 2:
		fail=True

	if not b[1]:
		z = (a[1] * b[0]) / a[0]
	elif not b[0]:
		z = (a[0] * b[1]) / a[1]
	elif not a[1]:
		z = (a[0] * b[1]) / a[0]
	elif not a[0]:
		z = (a[1] * b[0]) / a[1]
	else:
		fail=True
	if fail:
		colorThis( 'Error: xMultiply' )
		colorThis( '\texpected:', 'yellow' )
		colorThis( ['\t\t', str([960,540]), str([480,0])], 'yellow' )
		colorThis( '\t\t         or' )
		colorThis( ['\t\t', str([960,540]), str([0,270])], 'yellow' )
		colorThis( '\t\t         or' )
		colorThis( ['\t\t', str([480,270]), str([960,0])], 'yellow' )
		colorThis( '\t\t         or' )
		colorThis( ['\t\t', str([480,270]), str([0,540])], 'yellow' )
		colorThis( 'fail' )
		sys.exit()
	if str(z).endswith('.0'):
		return int(z)
	else:
		return z


def get_change(current, previous):

	if current == previous:
		return 100.0

	if current < previous:
		c = current
		p = previous
	else:
		p = current
		c = previous     

	try:
		return (abs(c - p) / p) * 100.0
	except ZeroDivisionError:
		return 0


def days_math( epoch, days=1, do='+'):
	if do == '+':
		now = autoDate( friendlyDate( autoDate(epoch) ).split(' ')[0] ) + (  86400*days  )
	elif do == '-':
		now = autoDate( friendlyDate( autoDate(epoch) ).split(' ')[0] ) - (  86400*days  )
	else:
		print_('Error: ', "days_math( epoch, days=1, do='+')")
		sys.exit()
	tdy0 = autoDate(friendlyDate( now ).split(' ')[0])
	return tdy0


def time_ago(epoch):
	return dateDiffText( epoch )
	global _dir
	if _dir is None:
		import _rightThumb._dir as _dir
	return _dir.time_diff(autoDate(epoch))

def time_diff(epoch):
	return dateDiffText( epoch )
	global _dir
	if _dir is None:
		import _rightThumb._dir as _dir
	return _dir.time_diff(autoDate(epoch))

def printText(text,p=1):
	result = str([text])[2:][:-2]
	if p:
		print_( result )
	return result



def changeM( path, stampM, stampA=None, meta=False, p=0 ):
	if p:
		mn = ''
		if time_diff(stampM) == 'today':
			mn = ', '+str(int((time.time() - stampM) /60)) + ' min'
			if mn == '0 min':
				mn = ', just now'
		print_( friendlyDate(stampM), colorThis( [time_diff(stampM)+ mn], 'yellow', p=0 ), path )
	if stampA is None:
		stampA = stampM
	# print_(stampM)
	# print_(stampA)
	global changeDate_Table
	global _dir
	global touch_meta



	if _dir is None:
		import _rightThumb._dir as _dir

	if meta:
		touch_meta = getTable( 'touch.meta' )
		if not path in touch_meta:
			touch_meta[path] = {}
		if not 'epoch' in touch_meta[path]:
			touch_meta[path]['epoch'] = {}
		touch_meta[path]['epoch']['me'] = stampM
		touch_meta[path]['epoch']['ae'] = stampA
		saveTable( touch_meta, 'touch.meta', p=0 )

	if not meta:
		if changeDate_Table is None:
			changeDate_Table = getTable( 'touch.index' )
		try:
			path = os.path.abspath(path)
		except Exception as e:
			pass
		if os.path.isfile(path):
			if not path in changeDate_Table:
				changeDate_Table[path] = _dir.info(path)
				saveTable( changeDate_Table, 'touch.index', p=0 )
			try:
				os.utime(path,(stampA, stampM))
			except Exception as e:
				pass
def changeC( path, stampC, meta=False, p=0 ):
	if p:
		mn = ''
		if time_diff(stampC) == 'today':
			mn = str(int((time.time() - stampC) /60)) + ' min'
		print_( friendlyDate(stampC), colorThis( [time_diff(stampC), mn], 'yellow', p=0 ), path )
	global changeC_rc_path
	global changeDate_Table
	global _dir
	global touch_meta

	if _dir is None:
		import _rightThumb._dir as _dir



	if meta:
		touch_meta = getTable( 'touch.meta' )
		if not path in touch_meta:
			touch_meta[path] = {}
		if not 'epoch' in touch_meta[path]:
			touch_meta[path]['epoch'] = {}
		touch_meta[path]['epoch']['ce'] = stampC
		saveTable( touch_meta, 'touch.meta', p=0 )




	if not meta:
		if changeDate_Table is None:
			changeDate_Table = getTable( 'touch.index' )

		if not changeC_rc_path:
			PowerShell_bashrc_name_break()
		# return None
		try:
			path = os.path.abspath(path)
		except Exception as e:
			pass
		if os.path.isfile(path):
			import subprocess
			if not path in changeDate_Table:
				changeDate_Table[path] = _dir.info(path)
				saveTable( changeDate_Table, 'touch.index', p=0 )
			# if __.isWin:
			#   do = ['powershell.exe', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stampC)+'")']
			#   print_(do)
			#   # p = subprocess.Popen([do], stdout=sys.stdout)
			#   p = subprocess.Popen(['powershell.exe', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stampC)+'")'], stdout=sys.stdout)
			try:

				if __.isWin:
					if os.path.isdir( 'C:\\Windows\\System32\\WindowsPowerShell' ):
						# do = ['powershell.exe', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stampC)+'")']
						# print_( do )
						# p = subprocess.Popen([do], stdout=sys.stdout)
						p = subprocess.Popen(['powershell.exe', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stampC)+'")'], stdout=sys.stdout)
				else:
					return None
					if os.path.isfile('/snap/bin/pwsh'):
						p = subprocess.Popen(['/snap/bin/pwsh', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stampC)+'")'], stdout=sys.stdout)
					elif os.path.isfile('/usr/bin/pwsh'):
						p = subprocess.Popen(['/usr/bin/pwsh', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stampC)+'")'], stdout=sys.stdout)
					elif os.path.isfile('/opt/pwsh'):
						p = subprocess.Popen(['/opt/pwsh', '$(Get-Item "'+path+'").CreationTime=("'+modify_timestamp(stampC)+'")'], stdout=sys.stdout)
			except Exception as e:
				colorThis( path, 'red' )
				time.sleep(.5)
				pass

def modify_timestamp( stamp ):
	d = friendlyDate(stamp).replace('-','/')
	parts = d.split(' ')
	day = parts[0]
	tip = parts[1].split(':')
	
	if int(tip[0]) > 12:
		tip[0] = int(tip[0]) - 12
		ap = 'PM'
	else:
		ap = 'AM'
	if not len(tip)> 2:
		f = day + ' ' + str(tip[0])+':'+str(tip[1])+ ' '+ ap
	else:
		f = day + ' ' + str(tip[0])+':'+str(tip[1])+':'+str(tip[2])+ ' '+ ap
	return f
	
def changeC_END():
	PowerShell_bashrc_name_break_fix()
def changeC_START():
	PowerShell_bashrc_name_break()

######################################################

def PowerShell_bashrc_name_break():
	global changeC_rc_path

	changeC_rc_path = True
	psA = _v.home + _v.slash + _v.slash.join( ['Documents','WindowsPowerShell','Microsoft.PowerShell_profile.ps1'] )
	psB = _v.home + _v.slash + _v.slash.join( ['Documents','WindowsPowerShell','00000_Microsoft.PowerShell_profile.ps1'] )
	if os.path.isfile(psA):
		os.rename( psA , psB )
		time.sleep(.2)
		# print_(psA)
		# print_(psB)

def PowerShell_bashrc_name_break_fix():
	global changeC_rc_path
	changeC_rc_path = False
	time.sleep(.2)
	psA = _v.home + _v.slash + _v.slash.join( ['Documents','WindowsPowerShell','Microsoft.PowerShell_profile.ps1'] )
	psB = _v.home + _v.slash + _v.slash.join( ['Documents','WindowsPowerShell','00000_Microsoft.PowerShell_profile.ps1'] )
	if os.path.isfile(psB):
		os.rename( psB , psA )
######################################################

def year(theDate):
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[0]

def woy(theDate):
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[1]

def getDOWromEpoch(theDate):
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[2]

def dow(theDate):
	return dowConvert(getDOWromEpoch(theDate))
	
def dowConvert(dow):
	result = ''
	if dow == 1:
		result = 'Monday'
	if dow == 2:
		result = 'Tuesday'
	if dow == 3:
		result = 'Wednesday'
	if dow == 4:
		result = 'Thursday'
	if dow == 5:
		result = 'Friday'
	if dow == 6:
		result = 'Saturday'
	if dow == 7:
		result = 'Sunday'
	return resultz


__.nc_histrory = []
class NC:

	def build( self, x, y=None ):
		__.nc_histrory.append(x)
		if not y == None:
			exec( 'self.' +x+ ' = y' )
		else:
			exec( 'self.' +x+ ' = NC()' )

	def child( self, xx, y=None ):
		xx = xx.replace( ' ', '' )
		for x in xx.split(','):
			if '.' in x:
				z = x.split('.')
				b = ''
				for w in z:
					b += '.'+w
					b = _str.cleanBE(b,'.')
					if not b in __.nc_histrory:
						# print_(b)
						self.build(b)


			self.build(x,y)


nc = NC()
"""
pp nx_test
	_.nc.child( 'tables' )
	_.nc.tables.a = 'a.index'
	_.nc.tables.b = 'a.hash'
	_.nc.tables.c = 'c.json'

	_.nc.child( 'a.b.c , a.s.d.f' )
	_.nc.a.s.d.f = 42

	_.nc.child( 'x.y.z', 123 )

"""


######################################################


# for x in sys.modules:
#     print_(x)

import _rightThumb._profileVariables as _profile
colorama_loaded = False
_dir = None
_code = None

isWin = __.isWin
thisOS = __.thisOS



def dicString( var, path ):
	return var + "['" + "']['".join( path.split('.') )+"']"

# def file_language(file):
	

# import inspect
# x = inspect.getargspec(SSHTunnelForwarder)


def check_field_match( actual, search ):
	if actual.lower() == search.lower() or actual.lower() == tfc(search):
		return True
	return False




def fileLabel(path):
	print_(path)
	global _dir
	if _dir is None:
		import _rightThumb._dir as _dir
	f = _dir.info( path )
	label = f['name_'].replace( '.'+f['ext'], '' )
	print_( label )
	return label

def getTablesProject( project ):
	folder = _v.projectData(project)
	# color( [project, folder], 'yellow' )
	files = []
	for file in os.listdir(folder):
		path = folder + _v.slash + file
		files.append( path )
	return files


def color( strings='', c='?', b=None, shouldPrint=True, attr=None,       p=None ):
	global switches
	if switches.isActive( 'NoColor' ):
		if shouldPrint:

			print_(str(strings).replace('‽',''))
			return strings
		else:
			return strings
	result = ''
	# https://pypi.org/project/colorama/
	# https://pypi.org/project/termcolor/

	if not p is None:
		shouldPrint=False


	if c == '?':
		print_("""

	Text colors:
		grey
		red
		green
		yellow
		blue
		magenta
		cyan
		white


	Text highlights:
		on_grey
		on_red
		on_green
		on_yellow
		on_blue
		on_magenta
		on_cyan
		on_white


	Attributes:
		bold
		dark
		underline
		blink
		reverse
		concealed

		""")
		sys.exit()
	background = None
	if b is None:
		cx = c.split(',')
		if len(cx) > 1:
			background = cx[1]
			if not background.startswith('on_'):
				background = 'on_'+background

		forground = cx[0]
	elif not b is None:
		forground = c
		background = b
		if not background.startswith('on_'):
			background = 'on_'+background

	global colorama_loaded
	global colored
	if not colorama_loaded:
		colorama_loaded = True
		from termcolor import colored

	if type(strings) == list:


		for i,x in enumerate(strings):

			strings[i] = str( x )

		string = ' '.join( strings )
	else:
		string = str(strings)

	if not background is None:
		if not attr is None:
			result = colored( string , forground, background, attrs=attr.split(',') )
		else:
			result = colored( string , forground, background)
	elif background is None:
		if not attr is None:
			result = colored( string , forground, attrs=attr.split(',') )
		else:
			result = colored( string , forground )

	if shouldPrint:
		try:
			print_( result )
		except Exception as e:

			try:
				result = str(result,'utf-8')
			except Exception as e:
				try:
					result = str(result,'iso-8859-1')
				except Exception as e:
					result = result.encode('utf-8')
			result = str(result,'iso-8859-1')

	return result
	

def factor( data, f=None, threshold=51, count=1 ):
	records = flattenInt(data,r=1,end='cnt')
	single = {}
	factors = {}
	for x in records:
		# print_( x, records[x] )
		if not x in single:
			single[x] = {
							'len': x,
							'count': len(records[x]),
							'first': None,
							'last': None,
							'diff_fl': None,
							'threshold': threshold,
							'drop_val': 100,
							'drop_id': None,
							'relevant': [],
							# 'records': records[x],

			}
		
		
		single[x]['last'] = percentageDiffAuto( records[x][0]['value'], records[x][  len(records[x])-1  ]['value'], isFloat=True, rnd=2 )
		# print_( "single[x]['last']", single[x]['last'] )
		# sys.exit()
		relevant = []
		# single[x]['relevant'].append({ 'drop': 0, 'id': 0, 'diff': 0, 'diff_0': 0, 'diff_0p': 0 })
		single[x]['relevant'].append({ 'drop': 0, 'id': 0, 'diff': 0, 'diff_0': 0, 'diff_0p': 0 })
		drop = 1
		last = records[x][0]['value']
		for i,y in enumerate(records[x]):

			if i:
				drop = percentageDiffAuto( records[x][i]['value'], last, isFloat=True, rnd=2 )
				# asdf = last-records[x][i]['value']
				# dLast = percentageDiffSmaller( last, asdf , isFloat=True, rnd=2 )
				# print_( dLast, '\t', last, '\t', asdf )
				# print_( records[x][i] )
				if drop <= single[x]['drop_val'] and drop <= threshold:
					single[x]['drop_val'] = drop
					single[x]['drop_id'] = i
					if records[x][i]['value'] >= count:
						single[x]['relevant'].append({ 'drop': drop, 'id': i, 'diff': last-records[x][i]['value'], 'diff_0': records[x][0]['value']- records[x][i]['value'] ,'diff_0p': percentageDiffAuto( records[x][0]['value'], records[x][i]['value'], isFloat=True, rnd=2 ) })
					# else:
					#     print_( records[x][i]['value'], count )
				if i==1:
					single[x]['first'] = percentageDiffAuto( records[x][0]['value'], records[x][i]['value'], isFloat=True, rnd=2 )
					single[x]['diff_fl'] = percentageDiffAuto( single[x]['first'], records[x][i]['value'], isFloat=True, rnd=2 )
					# print_( "single[x]['first']", single[x]['first'] )
					# print_( "single[x]['diff_fl']", single[x]['diff_fl'] )
				
				last = records[x][i]['value']
			# lastD = drop
			# print_(y)
		# single[x]['relevant'] = sort( single[x]['relevant'], 'drop' )
		# printVar( single[x] )
	factors['single'] = single
	if f is None:
		return { 'factors': factors, 'records': records }

	elif not factors is None:
		pass


def flattenInt( data, end=False, reverse=False, r=0, delineator='.' ):

	if r:
		reverse = True
	xyz = traverse(data, config={'delineator':delineator})
	# colorThis(  len( list( xyz['type']['int'].keys() ) ), 'red'  )
	if not end:
		records = []
		del records
		records = []

		for x in xyz['type']['int']:
			y = "['"+"']['".join( x.split(delineator) )+"']"
			records.append({ 'path': x, 'build': y, 'value': eval( 'data'+y ) })
		result = sort( records, 'value' )
		if reverse:
			result.reverse()
	elif end:
		# sys.exit()
		records = {}
		del records
		records = {}
		for x in xyz['type']['int']:
			if x.endswith(delineator+''+end):
				ln = x.count(delineator)
				c = x.split(delineator)
				y = "['"+"']['".join( c )+"']"
				if not ln in records:
					records[ln] = []
				c.pop()
				yy = "['"+"']['".join( c )+"']"
				records[ln].append({ 'path': x, 'buildA': y, 'buildB': yy, 'value': eval( 'data'+y ) })
		result = {}
		for ln in records:
			result[ln] = sort( records[ln], 'value' )
			if reverse:
				result[ln].reverse()


	return result

# _.colorThis( [ '\t', part_profile  ], 'yellow', simpleDic=True, colorProfile=[ { 't': 'i/dict', 'color': 'red', 'field': 'match'  } ] )

# {7DB6A001-0637-4F13-B328-2B17A481CF35}

# traverse_dic traverse_dic_research theFields
# pp multi_dic_test

class dt:
	def __init__( self, d ):
		self.d = d
		self.load()
	def load( self, d=None ):
		if d is None:
			d = self.d
		self.epoch = autoDate(d)
		self.friendly = friendlyDate(self.epoch)
		self.text = self.friendly
		self.print = self.friendly
		self.stamp = self.friendly
		self.timestamp = self.friendly
		self.date = self.friendly.split(' ')[0]
		self.time = self.friendly.split(' ')[1]
		self.object = datetime.datetime.fromtimestamp(self.epoch)


	def add( self, duration, months=False, years=False ):
		if months:
			return self.addMonths(duration)
		if years:
			return self.addYears(duration)
		result = str( dateAdd( self.date, '-', duration ) )
		self.load( result+'@'+self.time )
		return self
	
	def subtract( self, duration, months=False, years=False ):
		if months:
			return self.subtractMonths(duration)
		if years:
			return self.subtractYears(duration)
		result = str( dateSub( self.date, '-', duration ) )
		self.load( result+'@'+self.time )
		return self
		# dateAdd dateSub
		# theDate,delim,addDays

	def addMonths( self, months ):
		sp = self.date.split('-')
		y = int(sp[0])
		m = int(sp[1])
		i=0
		while not i==months:
			i+=1
			if m+1 > 12:
				m = 1
				y+=1
			else:
				m+=1
		mm = str(m)
		if len(mm) == 1:
			mm = '0'+mm
		result = str(y)+'-'+mm+'-'+sp[2]
		self.load( result+'@'+self.time )
		return self

	def subtractMonths( self, months ):
		sp = self.date.split('-')
		y = int(sp[0])
		m = int(sp[1])
		i=0
		while not i==months:
			i+=1
			if m-1 < 1:
				m = 12
				y-=1
			else:
				m-=1
		mm = str(m)
		if len(mm) == 1:
			mm = '0'+mm
		result = str(y)+'-'+mm+'-'+sp[2]
		try:
			pass
			self.load( result+'@'+self.time )
		except Exception as e:
			print_('result',result)
			sys.exit()
			# raise e
		return self

	def addYears( self, years ):
		sp = self.date.split('-')
		y = int(sp[0])+years
		result = str(y)+'-'+sp[1]+'-'+sp[2]
		self.load( result+'@'+self.time )
		return self

	def subtractYears( self, years ):
		sp = self.date.split('-')
		y = int(sp[0])-years
		result = str(y)+'-'+sp[1]+'-'+sp[2]
		self.load( result+'@'+self.time )
		return self


# def isData3( data=None, focus=None, pipeClean=True, required=False,     r=None, c=None ):
#     data = isData2( data, focus, pipeClean, required, r, c )
#     if data == ['Files']:
#         global switches
#         data = switches.values('Files')
#         if len(data) and type(data[0]) == list: data = data[0]

#     print(v.isData)
#     print(data)
#     return data
def isData( data=None, focus=None, pipeClean=True, required=False,     r=None, c=None, noclean=None ):
	global switches
	if data is None and switches.isActive('Paste-isData-json'):
		simplejson=__.imp('simplejson')
		d=getClip().strip()
		return simplejson.loads(d)
	elif data is None and switches.isActive('Paste-isData'): return getClip().split('\n')
	
	
	if not noclean is None: pipeClean=noclean
	def _isData_(tst):
		global myFileLocation_Files
		# if not tst and pipe_surfing(): tst = pipe_surfing()

		if not tst: return myFileLocation_Files;
		return tst

	def isData_path_list(stuff,dAta=[]):
		for f in stuff:
			f = __.path(f)
			if os.path.isfile(f):
				dAta.append(f)
		return dAta
	if not c is None: pipeClean=c;
	if not r is None: required = r;
	# pr('here',data,c='gray')
	if data is None:
		if pipeClean:
			pipeCleaner(0)
		global appData
		if focus is None:
			focus = __.appReg
		data = pipe_surfing()

	if type(data) ==list and  len(data)==1 and data[0]=='': data=[]
	if not data:
		data=[]
		# global switches
		isClean=False

		for name in v.isData:
			if len(switches.values(name)):
				for isD in v.isData[name].split(','):
					if isD == 'clean' and noclean is None:
						isClean=True
					elif isD == 'name':
						for n in switches.values(name):
							data.append(n)
					elif isD == 'glob' and 'data' in v.isData[name]:
						for n in switches.values(name):
							for f in isData_path_list( glob.glob( n ) ):
								for xXx in getText( f, raw=True ).split('\n'):
									data.append(xXx)
					elif isD == 'glob':
						for n in switches.values(name):
							if type(n) == list:
								stuff = n
							if type(n) == str:
								stuff = glob.glob( n )
							if not stuff is None:
								data=isData_path_list(stuff,data)
					elif isD == 'data':
						tData=[]
						for n in switches.values(name):
							tData.append(getText(n,raw=True))
						data = '\n'.join(tData)

		if data:
			if False and not isClean:
				return _isData_(data)
			elif type(data)==str:
				newData=''
				# data = data.replace('\r','')
				data = _str.do('sh',data)
				return _isData_(data.split('\n'))
			elif type(data)==list:
				if len(data) and type(data[0]) == list: data = data[0]
				_data='\n'.join(data)
				_data=_str.do('sh',_data)
				data=_data.split('\n')
				newData=[]
				for row in data:
					row = _str.replaceDuplicate( row, ' ' )
					newData.append(row)
				return _isData_(newData)






			
	if r:
		if type(data) == bool:
			help()
			return _isData_(None)
		if not data:
			help()
			return _isData_(None)
	else:
		if type(data) == bool:
			return _isData_([])
		if not data:
			return _isData_([])
	
	return _isData_(data)

def payloadCache( data, file=None, theFocus=None ):
	# _.payloadCache( saveFile, __file__, focus() )
	
	if theFocus is None:
		theFocus = __.appReg
	if file is None:
		appDBA = __.thisApp( __.postLoadFile )
	else:
		appDBA = __.thisApp( file )
	releaseAcquiredData( appDBA, theFocus, data )

__.appInfoScan = None

domainIndex = None

def json_clean(obj):
	if hasattr(obj, '__class__') and '.'  in str(obj.__class__):
		obj = dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('__'))
		obj = prep4JSON(obj)
	return obj


def prep4JSON(d, to_delete=None):
	# remove keys from multidimensional dicts and lists
	def autoFindKeys(d):
		# removes functions and methods
		global autoFindKeys_temp
		if isinstance(d, dict):
			for k in d.keys():
				t = type( d[k] )
				if 'function' in str(t):
					autoFindKeys_temp.append( k )
				elif 'method' in str(t):
					autoFindKeys_temp.append( k )
				
			for k, v in d.items():
				autoFindKeys(v)
		elif isinstance(d, list):
			for i in d:
				autoFindKeys(i)
		return d

	if to_delete is None:
		global autoFindKeys_temp
		autoFindKeys_temp = []
		autoFindKeys(d)
		return prep4JSON(d, to_delete=autoFindKeys_temp)

	if isinstance(to_delete, str):
		to_delete = [to_delete]
	if isinstance(d, dict):
		for single_to_delete in set(to_delete):
			if single_to_delete in d:
				d[single_to_delete] = ' ** removed ** '
		for k, v in d.items():
			prep4JSON(v, to_delete)
	elif isinstance(d, list):
		for i in d:
			prep4JSON(i, to_delete)
	return d

def delete_keys_from_dict(d, to_delete=None):
	# remove keys from multidimensional dicts and lists
	def autoFindKeys(d):
		# removes functions and methods
		global autoFindKeys_temp
		if isinstance(d, dict):
			for k in d.keys():
				t = type( d[k] )
				if 'function' in str(t):
					autoFindKeys_temp.append( k )
				elif 'method' in str(t):
					autoFindKeys_temp.append( k )
				
			for k, v in d.items():
				autoFindKeys(v)
		elif isinstance(d, list):
			for i in d:
				autoFindKeys(i)
		return d

	if to_delete is None:
		global autoFindKeys_temp
		autoFindKeys_temp = []
		autoFindKeys(d)
		return delete_keys_from_dict(d, to_delete=autoFindKeys_temp)

	if isinstance(to_delete, str):
		to_delete = [to_delete]
	if isinstance(d, dict):
		for single_to_delete in set(to_delete):
			if single_to_delete in d:
				del d[single_to_delete]
		for k, v in d.items():
			delete_keys_from_dict(v, to_delete)
	elif isinstance(d, list):
		for i in d:
			delete_keys_from_dict(i, to_delete)
	return d


def help():
	global switches
	switches.help()

def internet_domains(text):
	global domainIndex
	if domainIndex is None:
		domainIndex = getTableDB( 'domains.index' )
	results = []
	for domain in domainIndex.keys():
		minus = 'www'+domain
		# minus = []
		# minus.append( 'www'+domain )
		# for x in _str.alphanumeric:
		#     minus.append( domain+x )

		for thisDomain in caseUnspecific( text, domain, isPlus=False, minus=minus ):
			results.append( thisDomain )
	return results

def fileFolder( path, slash = _v.slash, py=False ):
	if not slash in path:
		try:
			path = os.path.abspath(path)
		except Exception as e:
			return path

	p = path.split(slash)
	file = p.pop()
	if py and ( file == '__init__.py' or file == '__init__.pyc' ):
		file = p.pop()
		
	return { 'file': file, 'folder': slash.join(p) }


def stringType( string, mini=True ):
	if not type(string) == str:
		if mini:
			return None
		else:
			return str( type(string) ).split("'")[1]
			return type(string)

	upperC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lowerC = 'abcdefghijklmnopqrstuvwxyz'
	numberC = '0123456789'

	if mini:
		total = 't'
		upper = 'u'
		lower = 'l'
		number = 'n'
		special = 's'
		count = 'c'
		percentage = 'p'
	elif not mini:
		total = 'total'
		upper = 'upper'
		lower = 'lower'
		number = 'number'
		special = 'special'
		count = 'count'
		percentage = 'percentage'

	result = {
				total: 0,
				upper: { count: 0, percentage: 0 },
				lower: { count: 0, percentage: 0 },
				number: { count: 0, percentage: 0 },
				special: { count: 0, percentage: 0 },
	}
	for c in string:
		result[total] += 1
		if c in upperC:
			result[upper][count] += 1
		elif c in lowerC:
			result[lower][count] += 1
		elif c in numberC:
			result[number][count] += 1
		else:
			result[special][count] += 1
	
	result[upper][percentage] = percentageDiffIntAuto( result[upper][count], result[total] )
	result[lower][percentage] = percentageDiffIntAuto( result[lower][count], result[total] )
	result[number][percentage] = percentageDiffIntAuto( result[number][count], result[total] )
	result[special][percentage] = percentageDiffIntAuto( result[special][count], result[total] )


	return result

def unixAutoColumns( asset, columns, focus=None ):
	if not len(asset):
		return asset
		# return columns
	asset = asset.copy()
	# if __.thisOS == 'Windows':

	if not __.terminal.width:
		return columns

	cols = __.terminal.width
	if focus is None:
		focus = __.appReg
	global appInfo
	rec = {}
	for k in asset[0].keys():
		rec[k]=k
	asset.append( rec )
		# cols = 102
	reg = appInfo[focus]['columns'].copy()
	reg.reverse()
	importance = []
	for x in reg:
		importance.append(x['name'])
	# importance = [
	#               'date_accessed',
	#               'week_of_year',
	#               'date_created',
	#               'date_modified',
	#               'ext',
	#               'size',
	# ]
	fields.asset( 'asset', asset )
	lengths = fields.lengths( 'asset' )

	# printVarSimple( lengths )

	total = 3
	for col in columns.split(','):
		total+=3
		for key in lengths:
			if col.lower() == key.lower():
				total += lengths[key]
	# print_( total, columns )
	# print_( cols, type(cols) )
	nextDel = 0
	done = False
	newList = []
	while total > cols and not done:
		total = 3
		newCols = []
		for col in columns.split(','):
			if col == importance[nextDel]:
				if not col in newList:
					newList.append(col)
			if not col == importance[nextDel]:
				newCols.append(col)
				total+=3
				for key in lengths:
					if col.lower() == key.lower():
						total += lengths[key]
			columns = ','.join(newCols)
		nextDel += 1
		if not len(newCols):
			done=True
	pass
	if not len(columns):
		columns = newList[ len(newList)-1 ]
	# print_( total, columns )


	# print_( 'total:', total )

	# sys.exit()
	return columns


def callers( i=1 ):
	callersX = []
	error=False

	while not error:
		try:
			try:
				x = sys._getframe(i).f_back.f_code
			except Exception as e:
				x = None
			try:
				xxx = str(sys._getframe(i).f_code.co_name)
			except Exception as e:
				xxx = '_bootstrap'
			# print_(x)
			# print_(xxx)
			if '_bootstrap' in xxx or '<module>' in xxx:
				error=True
			else:
				if not x is None:
					# print_(x)
					callersX.append(x)
				else:
					error=True
		except Exception as e:
			error=True

		i+=1
	# print_(callersX)
	return callersX

def epochDiff( a, b, isInt=None, isText=None, isFloat=None, isHR=None, isDays=None,      isD=None, isH=None, isI=None, isT=None, isF=None, txt=None ):
	# epochDiff( a, b, isH=1, isF=1 )
	if not isI is None:
		isInt = isI
	if not isT is None:
		isText = isT
	if not isF is None:
		isFloat = isF
	if not isH is None:
		isHR = isH
	if not isD is None:
		isDays = isD


	if txt is None:
		if isDays:
			txt = ' day'
		else:
			txt = ' hr'
	elif not txt is None:
		isText = True
		if 'h' in txt.lower():
			isHR = True
		else:
			isDays = True

		txt = txt.replace( ' ', '' )
		txt = txt.replace( 's', '' )
		txt = ' '+txt

	if isHR is None and isDays is None:
		isDays = True
	if isHR is isInt and isText is None and isFloat is None:
		isInt = True


	if a>b:
		start = b
		end = a
	else:
		start = a
		end = b
	diff = end - start
	result = round(  (diff/60)/60, 2  )

	if isHR:
		if result > 1:
			theTXT = txt+'s'
		else:
			theTXT = txt
		if isFloat and not isText:
			return result
		elif isFloat and isText:
			return str(result)+theTXT

		elif isInt and not isText:
			return int( str(result).split('.')[0] )
		elif isInt and isText:
			return str(result).split('.')[0]+theTXT
	elif isDays:
		result = round(  result/24, 2  )
		if result > 1:
			theTXT = txt+'s'
		else:
			theTXT = txt
		if isFloat and not isText:
			return result
		elif isFloat and isText:
			return str(result)+theTXT

		elif isInt and not isText:
			return int( str(result).split('.')[0] )
		elif isInt and isText:
			return str(result).split('.')[0]+theTXT
	return None




def getDriveID( drive, fail_isLetter=False ):
	drive = drive.upper()
	# print_(drive)

	def getDriveID_clean( driveID ):
		
		driveID = driveID.replace(' ','')
		driveID = driveID.replace('\n','')
		driveID = driveID.replace('\r','')
		return driveID

	driveID = None
	if not fail_isLetter:
		driveID = None
	else:
		driveID = drive
	if __.isWin:
		if os.path.isdir(drive+':'+_v.slash):
			idFile = drive + ':'+_v.slash+'drive.id.sys'
			if os.path.isfile(idFile):
				# os._exit(0)
				initiated = os.path.getctime(idFile)
				driveID = open( idFile, 'r' ).read()
				driveID = getDriveID_clean(driveID)

	elif not __.isWin:
		idFileA = drive+'/.drive-id'
		idFileB = drive+'/opt/tech/.drive-id'
		if os.path.isfile(idFileA):
			initiated = os.path.getctime(idFileA)
			driveID = open( idFileA, 'r' ).read()
			driveID = getDriveID_clean(driveID)
		if os.path.isfile(idFileB):
			initiated = os.path.getctime(idFileB)
			driveID = open( idFileB, 'r' ).read()
			driveID = getDriveID_clean(driveID)
		# else:
			# print_('Error')
			# os._exit(0)
	return driveID

def folderProfileAttribute( folder, info ):

	epoch = time.time()

	driveID = getDriveID( folder[0], fail_isLetter=True )
	# print_(driveID)
	# sys.exit()
	# file_drives = 'indexTable_drives-' + _v.getMachineID() + '.json'
	folders = folder[3:].replace( _v.slash, '((-f-))' )
	fld = _v.databank+_v.slash+'profiles'+_v.slash+'folders'+_v.slash+driveID
	saveTo = fld + _v.slash + folders+'.json'
	if not os.path.isdir( fld ):
		os.mkdir(fld)


	app = info['app']

	if info['recursive']:
		what = 'recursive'
	elif not info['recursive']:
		what = 'self'



	if not os.path.isfile( saveTo ):
		record = {
					'self': {},
					'recursive': {},
		}
		record[what][app] = {}
		record[what][app][epoch] = info
		saveTable2( record, saveTo )
	elif os.path.isfile( saveTo ):
		# print_(saveTo)
		try:
			record = getTable2( saveTo )
		except Exception as e:
			if os.path.isfile(saveTo):
				os.unlink(saveTo)
			folderProfileAttribute( folder, info )
			return None
			

		if record[what] == {}:
			record[what][app] = {}
			record[what][app][epoch] = info
			saveTable2( record, saveTo )

		if not app in record[what].keys():
			record[what][app] = {}
			record[what][app][epoch] = info
			saveTable2( record, saveTo )
			
		else:
			for key in list( record[what][app].keys() ):
				same = False
				failed = False
				for fKey in list( info.keys() ):
					if not fKey == 'factors':
						if fKey in record[what][app][key] and info[fKey]  ==  record[what][app][key][fKey]:
							
							same = True
						else:
							# print_( 'failed', fKey )
							failed = True


						if not fKey in record[what][app][key]:
							failed = True
							# print_( 'missing', fKey )
				if same and not failed:
					same = False
					failed = False
					for fKey in list( info['factors'].keys() ):
						if fKey in record[what][app][key]['factors'] and info['factors'][fKey]  ==  record[what][app][key]['factors'][fKey]:
							same = True
							# print_( 'Same' )
						else:
							# print_( 'failed', fKey )
							failed = True


						if not fKey in record[what][app][key]['factors'] :
							failed = True
							# print_( 'missing', fKey )
				# print_()
				# print_( 'same', same )
				# print_( 'failed', failed )
				if same and not failed:
					pass
				else:
					record[what][app][epoch] = info
					saveTable2( record, saveTo )




	pass
"""
{
	'factors': {
					
					'Text': False,
					'Binary': False,
					'Extensions': False,
					'Type': [],


					'PlusOr': False,
					'PlusClose': False,
					'Plus': False,
					'Minus': False,
					
					'Pluses': [],
					'Minuses': [],
	},
	'percentage': _.pDiff( len(files), i, use='less' ),
	'type': _.switches.value('Extensions'),
	'count': len(files),
	'files': i ,
	recursive': False,

}
"""


def getBin( file ):
	theFile=file
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	f = open( file, 'rb' )
	data = f.read()
	f.close()
	return data

def getBin_list( file ):
	f = open( file, 'rb' )
	data = list( f.read() )
	f.close()
	return data

def saveBin( data, file, me=0 ):
	theFile=file
	HD.chmod(file)
	def splitNumber (num):
		lst = []
		while num > 0:
			lst.append(num & 0xFF)
			num >>= 8
		return lst[::-1]
	try:
		f=open( file, 'wb' )
		f.write(data)
		f.close()
	except Exception as e:
		try:
			with open(file, 'br+') as f:
				f.write(data)
		except Exception as e:
			try:
				with open(file, 'br+') as f:
					for number in data:
						f.write(bytes(splitNumber(number)))
			except Exception as e:
				colorThis( 'Error: bin save', 'red' )
	HD.chmod(file)
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );

def pDiff( one, two, use=None,r=None ):
	if not use is None:
		use = use.lower()
	if not r is None:
		
		a = percentageDiffInt(one,two,rnd=r,isFloat=True)
		b = percentageDiffInt(two, one,rnd=r,isFloat=True)
	else:
		a = percentageDiffInt(one,two)
		b = percentageDiffInt(two, one)
	if use == None:
		return str(a)+'%, '+str(b)+'%'
	if a > b:
		g = a
		l = b
	else:
		l = a
		g = b

	if 'g' in use:
		return g
	elif 'l' in use:
		return l
	elif '1' in use or 'f' in use or 'a' in use or 'one' in use:
		return a
	elif '3' in use or 's' in use or 'b' in use or 'two' in use:
		return b


def pDiff2( one, two, use=None,r=None ):
	if not use is None:
		use = use.lower()
	if not r is None:
		
		a = percentageDiff(one,two,rnd=r,isFloat=True)
		b = percentageDiff(two, one,rnd=r,isFloat=True)
	else:
		a = percentageDiff(one,two)
		b = percentageDiff(two, one)
	if use == None:
		return str(a)+'%, '+str(b)+'%'
	if a > b:
		g = a
		l = b
	else:
		l = a
		g = b

	if 'g' in use:
		return g
	elif 'l' in use:
		return l
	elif '1' in use or 'f' in use or 'a' in use or 'one' in use:
		return a
	elif '3' in use or 's' in use or 'b' in use or 'two' in use:
		return b

	
def clean_dic( dic, omit ):
	global traverse_dic_research
	if not type(omit) == list:
		omit = [omit]
	traverse_dic_research['key_has'] = []
	traverse_dic( dic, config={ 'key_has': omit } )
	
	print_( 'key_has len:', len(traverse_dic_research['key_has']) )
	for x in traverse_dic_research['key_has']:
		print_(x)
	if not len(traverse_dic_research['key_has']):
		fields = ''
		for x in traverse_dic_research['all']:
			fields += x['field'] + '; '
			# print_(x)
		print_(fields)
	sys.exit()
traverse_dic_research = {}

def traverse( data=None, config={} ):
	global traverse_dic_research
	del traverse_dic_research
	traverse_dic( data, config )
	return traverse_dic_research
def traverse_dic( data=None, config={} ):
	global traverse_dic_research
	# if hasattr(data, '__class__'):
		# data = dict((name, getattr(data, name)) for name in dir(data) if not name.startswith('__'))
	# del traverse_dic_research
	traverse_dic_research = {  'return': None, 'index': {}, 'fields': [], 'spent': [], 'type': {}  }
	
	if 'inDic' in config:
		traverse_dic_research['inDic'] = []

		config['inDic'] = config['inDic'].lower()
	if 'inDicI' in config:
		traverse_dic_research['inDicI'] = []
		config['inDicI'] = config['inDicI'].lower()

	if data is None:
		print_('traverse_dic_research', traverse_dic_research)
		sys.exit()
	if not 'i_default' in config.keys():
		config['i_default'] = '-i-'
	traverse_obj( data, config )
	return traverse_dic_research

def traverse_obj( data=None, config={}, parents=[], parentsI=[],  ):
	global traverse_dic_research
	if not traverse_dic_research['return'] is None:
		return traverse_dic_research['return']
	if hasattr(data, '__class__') and '.'  in str(data.__class__):
		data = dict((name, getattr(data, name)) for name in dir(data) if not name.startswith('__'))



	if type(data) == list:
	# if hasattr(data, '__iter__') and not isinstance(data, (str, bytes, bytearray)):
		for i,row in enumerate(data):
			if 'i_label' in config.keys():
				np = parents + [ config['i_label'].replace('ID',str(i)) ]


			else:
				np = parents + [config['i_default']]
			npi = parentsI + [str(i)]




			
			traverse_obj( row, config, np, npi )
	elif type(data) == dict:
		for key in data.keys():
			shouldAdd = True
			if key not in traverse_dic_research['index'].keys():
				traverse_dic_research['index'][key] = []
			else:
				if parents in traverse_dic_research['index'][key]:
					shouldAdd = False

			if shouldAdd:
				traverse_dic_research['index'][key].append( parents )
				traverse_dic_research['fields'].append({ 'type': str(type(data[key])).split("'")[1] , 'field': key, 'parents': parents })
				typeX = str(type(data[key])).split("'")[1]
				if not 'delineator' in config:
					TeMP = '.'.join( parents+[key] )
				else:
					TeMP = config['delineator'].join( parents+[key] )
				if not typeX in traverse_dic_research['type']:
					traverse_dic_research['type'][typeX] = {}
				if not TeMP in traverse_dic_research['type'][typeX]:
					traverse_dic_research['type'][typeX][TeMP] = {}
			np = parents + [key]
			npi = parentsI + [key]
			


			if 'inDicI' in config.keys() and  type(data[key]) == str and config['inDicI'] in data[key].lower():
				traverse_dic_research['inDicI'].append( parentsI + [key] )

			if 'inDicI' in config.keys() and  type(data[key]) == list and len(data[key]) and type(data[key][0]) == str:
				for x in data[key]:
					if showLine( x, config['inDicI'].lower() ):
						traverse_dic_research['inDicI'].append( parentsI + [key] )


			if 'inDic' in config.keys() and  type(data[key]) == str and config['inDic'] in data[key].lower():
				
				if not str(np) in traverse_dic_research['inDic_spent']:
					traverse_dic_research['inDic_spent'].append(str(np))
					traverse_dic_research['inDic'].append( parents + [key] )
					print_(key)


			if 'returnField' in config.keys() and  config['returnField'] == np:
				traverse_dic_research['returnField'].append({  'data':  data[key], 'parents': np, 'parentsI': npi,  })
			elif 'returnFields' in config.keys() and  key in config['returnFields'].keys():
				# print_('here')
				for parent in config['returnFields'][key]:
					if parent == np:
						traverse_dic_research['returnFields'].append({  'data':  data[key], 'parents': np, 'parentsI': npi,  })
				

			if 'find_field' in config.keys() and  config['find_field'] == key:
				traverse_dic_research['return'] = data[key]
				return traverse_dic_research['return']

			if 'find_fields' in config.keys() and  config['find_fields'] == key:
				if not 'find_fields' in traverse_dic_research:
					traverse_dic_research['find_fields'] = []
				traverse_dic_research['find_fields'].append({ 'path': parents + [key], 'data': data[key] })

			if 'find_path' in config.keys():
				thePath = '.'.join(np).replace( '-i-', 'i' )
				if config['find_path'] == thePath:
					if not 'find_path' in traverse_dic_research:
						traverse_dic_research['find_path'] = []
					traverse_dic_research['find_path'].append( data[key] )
				

			if 'find_parents' in config.keys() and  config['find_parents'] == key:
				traverse_dic_research[ config['requests'] ] = np
				return np
				break
			
			if 'key_has' in config.keys():
				found = False
				if not type(config['key_has']) == list:
					config['key_has'] = list(config['key_has'])
				for x in config['key_has']:
					if x.lower() in key.lower():
						found = True
				if found:
					if 'requests' in config.keys():

						try:
							traverse_dic_research[ config['requests'] ].append(np)
						except Exception as e:
							traverse_dic_research[ config['requests'] ] = []
							traverse_dic_research[ config['requests'] ].append(np)
					else:
						try:
							traverse_dic_research[ 'key_has' ].append(np)
						except Exception as e:
							traverse_dic_research[ 'key_has' ] = []
							traverse_dic_research[ 'key_has' ].append(np)



		
			traverse_obj( data[key], config, np, npi )
	# pass

	# elif hasattr(data, '__dict__'):
	#     np = parents + ['__dict__']
	#     npi = parentsI + ['__dict__']
	#     traverse_obj( data.__dict__, config, np, npi )
	else:
		pass
		try:
			field = parents.pop()
		except Exception as e:
			field = ''
		if type(field) == int:
			traverse_dic_research['fields'].append({ 'type': str(type(data)).split("'")[1], 'field': field, 'parents': parents })



		if 'find_path' in config.keys():
			thePath = '.'.join(parents).replace( '-i-', 'i' )
			# print_(config['find_path'],thePath)
			if config['find_path'].lower() == thePath.lower():
				# print_(thePath)
				if not 'find_path' in traverse_dic_research:
					traverse_dic_research['find_path'] = []
				traverse_dic_research['find_path'].append( data )

		if 'inDicI' in config.keys() and  type(data) == str and config['inDicI'] in data.lower():
			traverse_dic_research['inDicI'].append( parentsI )

def clean_dic_keys( dic, omit ):
	index = { 'A':{}, 'B':{} }
	for k in dic.keys():
		u = genUUID()
		index['A'][k] = u
		index['B'][u] = k
		dic[u] = dic[k]
		del dic[k]
	for k in dic.keys():
		n = index['B'][k]
		for o in omit:
			n = n.replace(o,'')

		dic[n] = dic[k]
		del dic[k]



def justTime(theDate):
	clock = friendlyDate( theDate ).split(' ')[1]
	clock_parts = clock.split(':')
	am_pm = ' AM'
	if int(clock_parts[0]) > 12:
		am_pm = ' PM'
		clock_parts[0] = str(  int(clock_parts[0])-12  )
	else:
		clock_parts[0] = str(  int(clock_parts[0])  )
	clock_parts.pop(2)
	clock = ':'.join(clock_parts)
	return clock+am_pm
	


def wrapText( data, length=150, pre_space='    ', scan=[], bold='yellow', s=' ', p=True ):
	currentLength = len(pre_space)
	theText = ''
	data = pre_space + data
	dice_scan = [  ]
	for word in data.split(s):
		if len(scan):
			for sn in scan:
				if sn.lower() in word.lower():
					word = colorThis( word, bold, p=0 )

		if '\n' in word:
			word = word.replace( '\n', '\n'+pre_space )

		if currentLength + len(word) > length:
			theText += '\n'+pre_space
			currentLength = len(pre_space)

		currentLength += len(word)
		theText += word + s
		if '\n' in word or currentLength > length:
			currentLength = len(pre_space)
	if not theText is None:
		if theText[-2:] == s+s and not data[-2:] == s+s and data[-1:] == s:
			theText = theText[:-1]
		elif theText[-1:] == s and not data[-1:] == s:
			theText = theText[:-1]
		data = ''
		pre_space = ''
		if p:
			print_( theText )
		else:
			# print_( '\n\ntheText:', theText, '\n\n' )
			return theText


def simpleDic( dic ):
	txt = str(dic)
	txt = txt.replace( '{', '' )
	txt = txt.replace( '}', '' )
	txt = txt.replace( '"', '' )
	txt = txt.replace( "'", '' )
	txt = txt.replace( '_', ' ' )
	txt = txt.title()
	return txt
def simpleDic2( dic ):
	txt = str(dic)
	# print_( txt )
	txt = txt.replace( ", '", ",\n'" )
	txt = txt.replace( '{', '' )
	txt = txt.replace( '}', '' )
	txt = txt.replace( '"', '' )
	txt = txt.replace( "'", '' )
	txt = txt.replace( '_', ' ' )
	txt = txt.title()
	return txt

def lastBackup( file, backup=0 ):
	backupLog = tables.returnSorted( 'backupLog', 'd.timestamp', getTable('fileBackup.json') )
	path = os.path.abspath(file)
	# print_( 'path:', path )
	if backup == '?':

		i = 0
		for record in backupLog:
			if record['file'] == path:
				i+=1
		part = path.split( _v.slash )
		part.reverse()
		label = part[0]
		colorThis( [ '\n\ttotol of', i , 'backups for ', label ], 'yellow' )
		sys.exit()

	else:
		i = 0
		for record in backupLog:
			if record['file'] == path:
				# printTest( record )
				# print_( friendlyDate(record['timestamp']) )
				if i == backup:
					return record['backup']
				i+=1


		i = 0
		for record in backupLog:
			if record['file'] == path:
				i+=1
		part = path.split( _v.slash )
		part.reverse()
		label = part[0]
		colorThis( [ '\n\ttotol of', i , 'backups for ', label ], 'yellow' )
		sys.exit()

		# id timestamp file backup status version flag


	return None

def textClean( txt ):
	clean = 2
	
	if clean:
		txt = _str.replaceDuplicate( txt, '\n' )
		txt = _str.cleanBE( txt, '\n' )
	if clean == 2:
		txt = txt.replace( '\t', ' ' )
		txt = _str.replaceDuplicate( txt, ' ' )
		while '\n \n' in txt:
			txt = txt.replace( '\n \n', '\n' )
		txt = _str.replaceDuplicate( txt, '\n' )
		txt = _str.cleanBE( txt, '\n' )
	return txt

def dicf(obj, seen=None, f=None):
	'Recursively scan for dic fields'
	global dicf_payload
	dicf_payload=[]
	dicf_()
	return dicf_payload

def dicf_(obj, seen=None, f=None):
	'Recursively scan for dic fields'
	global dicf_payload
	if f is None: e('dicf_',"expected: _.indic(obj,f='field')")


	# return 0
	if obj is None:
		return 0
	
	# function source documentation:
	#   searched for: python how much memory usage of list of dict
	#   https://goshippo.com/blog/measure-real-size-any-python-object/

	size = sys.getsizeof(obj)
	if seen is None:
		seen = set()
	obj_id = id(obj)
	if obj_id in seen:
		return 0
	# Important mark as seen *before* entering recursion to gracefully handle
	# self-referential objects
	seen.add(obj_id)
	if isinstance(obj, dict):
		if type(f) == str:
			for ii,k in enumerate(obj.keys()):
				if k.lower() == f.lower():
					v=list(obj.values())[ii]
					dicf_payload.append(v)
					# if not v in dicf_payload: dicf_payload.append(v)
		elif type(f) == list:
			for ii,k in enumerate(obj.keys()):
				for ff in f:
					if k.lower() == ff.lower():
						v=list(obj.values())[ii]
						dicf_payload.append(v)
						# if not v in dicf_payload: dicf_payload.append(v)

		size += sum([dicf_(v, seen, f) for v in obj.values()])
		size += sum([dicf_(k, seen, f) for k in obj.keys()])
	elif hasattr(obj, '__dict__'):
		size += dicf_(obj.__dict__, seen, f)
	elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
		size += sum([dicf_(i, seen, f) for i in obj])
	return size

def get_size(obj, seen=None):
	'Recursively finds size of objects'
	# return 0
	if obj is None:
		return 0
	
	# function source documentation:
	#   searched for: python how much memory usage of list of dict
	#   https://goshippo.com/blog/measure-real-size-any-python-object/

	size = sys.getsizeof(obj)
	if seen is None:
		seen = set()
	obj_id = id(obj)
	if obj_id in seen:
		return 0
	# Important mark as seen *before* entering recursion to gracefully handle
	# self-referential objects
	seen.add(obj_id)
	if isinstance(obj, dict):
		size += sum([get_size(v, seen) for v in obj.values()])
		size += sum([get_size(k, seen) for k in obj.keys()])
	elif hasattr(obj, '__dict__'):
		size += get_size(obj.__dict__, seen)
	elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
		size += sum([get_size(i, seen) for i in obj])
	return size


bmIndex = []
""" {7DB6A001-0637-4F13-B328-2B17A481CF35}
processWordStem = None
def wordStem(word):
	global processWordStem
	if processWordStem is None:
		import nltk
		from nltk.stem import PorterStemmer
		from nltk.tokenize import word_tokenize
		processWordStem = PorterStemmer()
	return processWordStem.stem(word)
"""



class CacheManager:
# get_size()

	def __init__( self ):
		pass

	def load( self, config ):
		return None

	def save( self, data, config ):
		return data

	# def 



# __.app = CacheManager()

def genSerial( subject ):
	serial_no = getText( _v.myVars + _v.slash+'sequence-'+subject+'.serial', clean=2, raw=1 )
	if serial_no is None:
		serial_no = 12345
	else:
		serial_no = int(serial_no)+1
	saveText( str(serial_no), _v.myVars + _v.slash+'sequence-'+subject+'.serial' )
	return serial_no


def extTrigger__File_TYPE__( data ):
	data = data.lower()
	archive = [
				'*.7z',
				'*.s7z',
				'*.ace',
				'*.afa',
				'*.alz',
				'*.apk',
				'*.arc',
				'*.ark',
				'*.cdx',
				'*.arj',
				'*.b1',
				'*.b6z',
				'*.ba',
				'*.bh',
				'*.cab',
				'*.car',
				'*.cfs',
				'*.cpt',
				'*.dar',
				'*.dd',
				'*.dgc',
				'*.dmg',
				'*.ear',
				'*.gca',
				'*.ha',
				'*.hki',
				'*.ice',
				'*.jar',
				'*.kgb',
				'*.lzh',
				'*.lha',
				'*.lzx',
				'*.pak',
				'*.partimg',
				'*.paq6',
				'*.paq7',
				'*.paq8',
				'*.pea',
				'*.pim',
				'*.pit',
				'*.qda',
				'*.rar',
				'*.rk',
				'*.sda',
				'*.sea',
				'*.sen',
				'*.sfx',
				'*.shk',
				'*.sit',
				'*.sitx',
				'*.sqx',
				'*.tar',
				'*.tar.gz',
				'*.tgz',
				'*.tar.Z',
				'*.tar.bz2',
				'*.tbz2',
				'*.tar.lzma',
				'*.tlz.',
				'*.tar.xz',
				'*.txz',
				'*.uc',
				'*.uc0',
				'*.uc2',
				'*.ucn',
				'*.ur2',
				'*.ue2',
				'*.uca',
				'*.uha',
				'*.war',
				'*.wim',
				'*.xar',
				'*.xp3',
				'*.yz1',
				'*.zip',
				'*.zipx',
				'*.zoo',
				'*.zpaq',
				'*.zz'
			]

	office = [
				'*.doc',
				'*.dot',
				'*.wbk',
				'*.docx',
				'*.docm',
				'*.dotx',
				'*.dotm',
				'*.docb',
				'*.xls',
				'*.xlt',
				'*.xlm',
				'*.xlsx',
				'*.xlsm',
				'*.xltx',
				'*.xltm',
				'*.xlsb',
				'*.xla',
				'*.xlam',
				'*.xll',
				'*.xlw',
				'*.ppt',
				'*.pot',
				'*.pps',
				'*.pptx',
				'*.pptm',
				'*.potx',
				'*.potm',
				'*.ppam',
				'*.ppsx',
				'*.ppsm',
				'*.sldx',
				'*.sldm',
				'*.pub',
				'*.xps'
			]
	pass
	# archive
	# office
	


def urlTrigger(url):
	if not '.' in url:
		url = 'http://' + url + '.com'
	elif not url.startswith('http'):
		url = 'http://' + url
	return url

def myFolderLocations( data ):
	return data
	# print_(data)
	if type(data) == list:
		for i,d in enumerate(data):
			data[i] = myFolderLocations(d)
		return data

	if os.path.isdir(data):
		return os.path.abspath(data)
	

	global bmIndex
	
	if not len(bmIndex):
		bmIndex = getTable( 'bookmarks.index' )

	# print_( bmIndex )
	if data in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data])
	if data.lower() in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data.lower()])
	if data.upper() in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data.upper()])
	if data.title() in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data.title()])


	return data

def mod(path):
	return os.path.getmtime(path)



def colorPlus( data, color='green' ):
	for search in switches.values('Plus'):
		for subject in caseUnspecific( data, search, isPlus=True ):

			if type( subject ) == str:
				data = data.replace( subject, colorThis( subject, color, p=0 ) )
			else:
				if subject['pos'] == 'first':
					data = nth_repl(data, subject['data'], colorThis( subject['data'], color, p=0 ), 1)
				else:
					cx = data.count( subject['data'] )
					data = nth_repl(data, subject['data'], colorThis( subject['data'], color, p=0 ), cx)
	return data

def plusColor( row, color='green' ):
	# row = thePrintLine

	if switches.isActive('Plus'):
		thePrintLine = row
		for plusSearchX in switches.values('Plus'):
			plusSearchX = ci( plusSearchX )

			for subject in caseUnspecific( row, plusSearchX ):
				row = thePrintLine.replace( subject, colorThis( subject, color , p=0 ) )

	return row

def caseUnspecificCode( data, subject, isPlus=False, minus=None ):
	global switches

	if __.sw.PlusCode or switches.isActive('StrictCase'):   return caseISspecific(data, subject, isPlus, minus)
	else:                return caseUnspecific(data, subject, isPlus, minus)



def caseUnspecific( data, subject, isPlus=False, minus=None, code=False ):

	if __.sw.PlusCode and 'color' in __.sw.PlusCode: code = True
	if switches.isActive('StrictCase'): code = True

	if code: return caseUnspecificCode(data, subject, isPlus, minus)


	if not minus is None:
		if type(minus) == list:
			for remove in minus:
				for deleteThis in caseUnspecific( data, remove.lower(), isPlus=False ):
					data = data.replace( deleteThis, '' )
		elif type(minus) == str:
			for deleteThis in caseUnspecific( data, minus.lower(), isPlus=False ):
				data = data.replace( deleteThis, '' )

	results = []
	subject = subject.lower()
	if isPlus:
		if '*' in subject and len(subject) > 1:
			if subject.startswith('*'):
				subject = subject.replace( '*', '' )
				subject = ci(subject)
				if data.lower().endswith( subject ):
					return [{ 'data': data[-len(subject):], 'pos': 'last' }]
				return []
			if subject.endswith('*'):
				subject = subject.replace( '*', '' )
				subject = ci(subject)
				if data.lower().startswith( subject ):
					return [{ 'data': data[:len(subject)], 'pos': 'first' }]
				return []
		subject = ci(subject)
			

	while data.lower().find( subject ) > -1:
		scanning = data.lower().find( subject )
		subjectY = ''
		scanComplete = False
		while not scanComplete:
			if len(subjectY) == len(subject):
				scanComplete = True
			elif scanning > len(data)-1:
				scanComplete = True
			else:
				subjectY += data[ scanning ]
			scanning += 1
		if not subjectY in results:
			results.append( subjectY )
		data = data.replace( subjectY, '' )
	return results


def caseISspecific( data, subject, isPlus=False, minus=None ):

	if not minus is None:
		if type(minus) == list:
			for remove in minus:
				for deleteThis in caseISspecific( data, remove, isPlus=False ):
					data = data.replace( deleteThis, '' )
		elif type(minus) == str:
			for deleteThis in caseISspecific( data, minus, isPlus=False ):
				data = data.replace( deleteThis, '' )

	results = []
	subject = subject
	if isPlus:
		if '*' in subject and len(subject) > 1:
			if subject.startswith('*'):
				subject = subject.replace( '*', '' )
				subject = ci(subject)
				if data.endswith( subject ):
					return [{ 'data': data[-len(subject):], 'pos': 'last' }]
				return []
			if subject.endswith('*'):
				subject = subject.replace( '*', '' )
				subject = ci(subject)
				if data.startswith( subject ):
					return [{ 'data': data[:len(subject)], 'pos': 'first' }]
				return []
		subject = ci(subject)
			

	while data.find( subject ) > -1:
		scanning = data.find( subject )
		subjectY = ''
		scanComplete = False
		while not scanComplete:
			if len(subjectY) == len(subject):
				scanComplete = True
			elif scanning > len(data)-1:
				scanComplete = True
			else:
				subjectY += data[ scanning ]
			scanning += 1
		if not subjectY in results:
			results.append( subjectY )
		data = data.replace( subjectY, '' )
	return results


def nth_repl(s, sub, repl, nth):

	# first and only thing a got online

	find = s.find(sub)
	# if find is not p1 we have found at least one match for the substring
	i = find != -1
	# loop util we find the nth or we find no match
	while find != -1 and i != nth:
		# find + 1 means we start at the last match start index + 1
		find = s.find(sub, find + 1)
		i += 1
	# if i  is equal to nth we found nth matches so replace
	if i == nth:
		return s[:find]+repl+s[find + len(sub):]
	return s


def shuffle( myList ):
	result = []
	data = []
	for x in myList:
		data.append({ 'data': x, 'sortBy': genUUID() })

	for record in tables.returnSorted( genUUID(), 'd.sortBy', data ):
		result.append( record['data'] )
	return result



# oc = list(filter(lambda data: data['open'] == pos, record['oc']))
__.loadingVar = {
					'hasLoaded': False,
					'hasCleared': False,
					'isRunning': False,
					'done': False,
}


__.loadingVar['hasLoaded'] = False
__.loadingVar['hasCleared'] = False
__.loadingVar['isRunning'] = False

def listColor( text, rows, color='green' ):
	return text
	r = text

	# print_( 'HERE', r )
	txtCNT = text.lower()
	for row in rows:

		loc = txtCNT.find( row )
		if row in txtCNT:
			print_( 'loc:', loc )
			if loc:
				r = ''
				for i,char in enumerate(text):
					if i >= loc and i <= len(row)-1:
						print_( char )
						r += colorThis( char, color, p=0 )
					else:
						r+=char
	return r



def LoadingDone(done=None):
	if not done is None:
		__.loadingVar['done'] = done
	__.loadingVar['hasLoaded'] = True
	
	global threads
	while not __.loadingVar['hasCleared']:
		time.sleep( .2 )
	time.sleep( .7 )
	print_( '                                                        ', end='\r' )
	time.sleep( 2 )
	__.loadingVar['hasCleared'] = False
	__.loadingVar['hasLoaded'] = False
	__.loadingVar['isRunning'] = False
	del threads
	threads = Queue()

def loadingAnimation(loading='Searching',done='Found' ):
	__.loadingVar['done'] = done
	if not __.loadingVar['isRunning']:
		__.loadingVar['isRunning'] = True
		global threads
		theID = 'loadingAnimation_'+loading+'_' + genUUID()
		threads.add( theID ) # kwargs 
		threads.maxThreadsSafe = 225
		threads.autoLoadedAfter = .1
		threads.scheduleLoop = .01
		threads.auditLoop = .1
		threads.projectDataMaxLen = 500
		threads.report = False
		threads.auditPrint = False
		threads.add( theID, loadingGif, [loading] )


def loadingGif(loading, qID=False):
	
	gif = [
			'       *',
			'      **',
			'     ***',
			'    *** ',
			'   ***  ',
			'  ***   ',
			' ***    ',
			'***     ',
			'**      ',
			'*       ',
			'**      ',
			'***     ',
			' ***    ',
			'  ***   ',
			'   ***  ',
			'    *** ',
			'     ***',
			'      **',
	]
	while not __.loadingVar['hasLoaded']:
		print_( '                                                                                                   ', end='\r' )
		for x in gif:
			animate = colorThis( x, 'red', p=0 )
			print_( '\t\t{' + animate + '} '+loading+'...', end='\r' )
			time.sleep( .4 )
		print_( '                                                                                                   ', end='\r' )
	print_( '                                                                                                   ', end='\r' )
	print_( '\t\t'+colorThis( __.loadingVar['done'], 'green', p=0 ), end='\r' )
	if not type(qID) == bool:
		global threads
		threads.spent( qID, sys.getsizeof( 'obj') )
	__.loadingVar['hasCleared'] = True

		
def loadingGifX(loading):
	
	gif = [
			'       *',
			'      **',
			'     ***',
			'    *** ',
			'   ***  ',
			'  ***   ',
			' ***    ',
			'***     ',
			'**      ',
			'*       ',
			'**      ',
			'***     ',
			' ***    ',
			'  ***   ',
			'   ***  ',
			'    *** ',
			'     ***',
			'      **',
	]
	while not __.loadingVar['hasLoaded']:
		print_( '                                                                                                   ', end='\r' )
		for x in gif:
			animate = colorThis( x, 'red', p=0 )
			print_( '\t\t{' + animate + '} '+loading+'...', end='\r' )
			time.sleep( .4 )
		print_( '                                                                                                   ', end='\r' )
	print_( '                                                                                                   ', end='\r' )
	print_( '\t\t'+colorThis( __.loadingVar['done'], 'green', p=0 ), end='\r' )

	__.loadingVar['hasLoaded'] = False



server_proxy = []
server_proxy.append( '' )
server_proxy.append( 'http://www.rightthumb.com/projects/widget/proxy.php?p=' )
server_proxy.append( 'http://rephrecruiting.com/proxy.php?p=' )
server_proxy.append( 'http://www.pillerbeauty.com/proxy.php?p=' )
server_proxy.append( 'http://signaturemassageandfacialspa.com/p.php?p=' )
server_proxy.append( 'https://signaturemassagetampa.com/payroll/p.php?p=' )

appProxy = 'appProxy.json'

ipsum = None
def ipsumSentence():
	global ipsum
	if ipsum is None:
		ipsum = getText( _v.ipsum, raw=True, clean=2 )
	ipsum = ipsum.replace( '\n', ' ' )
	sentences = []
	for sentence in ipsum.split('.'):
		sentence = _str.replaceDuplicate( sentence, ' ' )
		sentence = _str.cleanBE( sentence, ' ' )
		sentence = sentence + '.'
		sentences.append({ 'sentence': sentence, 'sortBy': genUUID() })

	randomized = tables.returnSorted( 'data', 'd.sortBy', sentences )
	return randomized[0]['sentence']

def ipsumParagraph( count=1, shouldPrint=False, returnList=False, lorem=True ):
	global ipsum
	if ipsum is None:
		ipsum = getText( _v.ipsum, raw=True, clean=2 )
	paragraphs = []
	for item in ipsum.split('\n'):
		item = _str.replaceDuplicate( item, ' ' )
		item = _str.cleanBE( item, ' ' )
		item = item + '.'
		item = _str.replaceDuplicate( item, '.' )
		paragraphs.append({ 'paragraph': item, 'sortBy': genUUID() })

	randomized = tables.returnSorted( 'data', 'd.sortBy', paragraphs )

	result = []

	i=0
	while not i == count:
		result.append( randomized[i]['paragraph'] )
		i+=1

	if lorem:
		result[0] = 'Lorem ipsum ' + result[0][0].lower() + result[0][1:]

	

	if shouldPrint:
		data = '\n\n'.join( result )
		print_( data )

	if returnList:
		return result
	else:
		return '\n\n'.join( result )

def saveCSV( data, file, printThis=True,here=False,                p=None, me=0,h=None ):
	if not h is None: here=h
	theFile=file
	HD.chmod(file)
	if not p is None:
		printThis = p


	import csv
	px = ''
	if file.startswith('temp'+_v.slash):
		file = file.replace( 'temp'+_v.slash, '' )
		theFile = _v.stmp + _v.slash + file
		px = theFile
	elif _v.slash in file:
		theFile = file
		px = theFile
	else:
		theFile = _v.myTables + _v.slash + file
		px = file
	if here: theFile=file

	with open( theFile , mode='w') as csv_file:
		fields = list(data[0].keys())
		writer = csv.DictWriter(csv_file, fieldnames=fields)

		writer.writeheader()
		for record in data:
			writer.writerow( record )
	cleanFile = getText( theFile, raw=True )
	lines = []
	for line in cleanFile.split('\n'):
		line = line.strip()
		if line: lines.append(line)

	saveText( lines, theFile )
	if printThis:
		printBold('Saved: ' + px, 'blue')
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );

def getCSV( file, save=False, json_file='', printThis=True ):
	theFile=file
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	if file.startswith('temp'+_v.slash):
		file = file.replace( 'temp'+_v.slash, '' )
		theFile = _v.stmp + _v.slash + file
	elif _v.slash in file:
		theFile = file
	else:
		theFile = _v.myTables + _v.slash + file

	return csv( file=theFile, save=save, json_file=json_file, printThis=printThis )

def csvTXT( data ):
	import csv
	csv_rows = []
	reader = csv.DictReader(data)
	title = reader.fieldnames
	for row in reader:
		csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
	return csv_rows
def csv( file, save=False, json_file='',printThis=True ):
	import csv
	if type(save) == str:
		json_file = save
		save = True

	elif len(json_file):
		save = True
	elif save and json_file == '':
		json_file = changeExtension( row, 'json' )
	csv_rows = []
	# with open(file, 'r', encoding='utf-8') as csvfile:
	# with open(file, 'r', encoding='utf-8', errors="surrogateescape") as csvfile:
	# with open(file, 'r', encoding='ascii', errors="replace") as csvfile:
	with open( file, 'r', encoding='ascii', errors='ignore' ) as csvfile:
	# with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		title = reader.fieldnames
		# print_( title )
		# for t in title:
		#   print_( t )
		for row in reader:
			csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
		csv_rows = convertTimestamp( csv_rows )
		if save:
			saveTable2(csv_rows,json_file)
			if printThis:
				printBold( json_file, 'green' )
		fixField = False
		
		# if False:
		if True:
			try:
				for field in csv_rows[0].keys():
					if '"' in field:
						fixField = True
			except Exception as e:
				pass
			if fixField:
				for record in csv_rows:
					for field in record.keys():
						if '"' in field:
							tmpF = field.split('"')
							record[ tmpF[1] ] = record[field]
							del record[field]
		return csv_rows
	return False

def csv2( data, file, printThis=True, p=None ):
	if not p is None:
		printThis = p
	saveText(csvText( data ),file)
	if printThis:
		printBold( file, 'green' )

def csvText( data ):
	if not type(data) == list:
		cp( 'Error: csvText, expected list', 'red' )
	if not len(data):
		return ''

	alphanumeric = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\'()*+-./:;<=>?@[\\]^_`{|}~'


	records = []
	line = []
	keys = []
	for field in data[0].keys():
		keys.append(field)
		subject = field
		isAlpha = True
		for s in subject:
			if not s in alphanumeric:
				isAlpha = False
		if not isAlpha:
			subject = '"'+str( [field] )[2:-2]+'"'
		line.append( subject )
		
	records.append( ','.join(line) )

	for record in data:
		line = []
		for f in keys:
			subject = record[f]
			isAlpha = True
			for s in subject:
				if not s in alphanumeric:
					isAlpha = False
			if not isAlpha:
				subject = '"'+str( [subject] )[2:-2]+'"'
			line.append( subject )
		records.append( ','.join(line) )


	return '\n'.join( records )
	# return records

	# sys.exit()


def convertTimestamp( data ):
	if not len( data ):
		return data
	if not 'timestamp' in data[0].keys():
		return data
	if 'datetime' in data[0].keys():
		hasDateTime = True
	else:
		hasDateTime = False
	for i,record in enumerate(data):
		try:
			if len( record['timestamp'] ):
				if isFloat( str(record['timestamp']) ):
					if not hasDateTime:
						data[i]['datetime'] = resolveEpoch( data[i]['timestamp'] )
					else:
						return data
				else:
					data[i]['timestamp'] = autoDate( record['timestamp'] )
					if not hasDateTime:
						data[i]['datetime'] = resolveEpoch( data[i]['timestamp'] )
		except Exception as e:
			return data
	return data

def changeExtension( file, ext ):
	f = removeExtension( file )
	if not '.' in ext:
		return f + '.' + ext
	else:
		return f + ext

def getExtension(string):

	ext0 = string.split('.')
	extId = len(ext0) - 1
	if extId > 0:
		ext = ext0[extId]
	else:
		ext = ''
	return ext
def removeExtension(string):
	if not '.' in string:
		return string
	ext = getExtension(string)
	sl = len(string)
	el = len(ext)
	dl = (sl - el) - 1
	file = ''
	for i,n in enumerate(string):
		if i < dl:
			file += n

	return file


def registerSpent( app, spentID ):
	global appProxy
	data = getTable( appProxy )
	for i,record in enumerate(data):
		if record['app'] == app:
			pass
	saveTable( appProxy )

# colorizeRow
# printBold

__.color_palette = 0

# from timeout import timeout
plusClose = 70
autoBackupData = False
autoLoadData = False

idResolution = []

theExtensionsList = []
relevantFolders = []
setPipeDataRan = False

__.columnAbbreviations = 1

# print_( 'make pattern algorithm for pattern IDs' )

# def testPatterns( two, one ):

def saveData( rows, theFile, printThis=True ):
	HD.chmod(theFile)
	if theFile.lower().endswith( '.json' ):
		if _v.slash in theFile:
			saveTable2( rows, theFile, printThis )
			if printThis:
				print_( 'Saved: ', theFile )
		else:
			saveTable( rows, theFile, printThis )
		return True

	if theFile.lower().endswith( '.txt' ):
		if _v.slash in theFile:
			saveText( rows, theFile )
			if printThis:
				print_( 'Saved: ', theFile )
		else:
			if os.path.isfile( _v.myTables + _v.slash + theFile ):
				saveText( rows, _v.myTables + _v.slash + theFile )
			else:
				saveText( rows, _v.myTables + _v.slash + theFile )
			if printThis:
				print_( 'Saved: ', _v.myTables + _v.slash + theFile )
		return True

	location = theFile
	if os.path.isfile( theFile ):
		found = True
	
	if not os.path.isfile( theFile ):
		found = False
		if not _v.slash in theFile:
			if not '.' in theFile:
				if os.path.isfile( _v.myTables + _v.slash + theFile + '.json' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.json'
				elif os.path.isfile( _v.myTables + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.txt'
				elif os.path.isfile( _v.myTables + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.txt'
			else:
				if os.path.isfile( _v.myTables + _v.slash + theFile ):
					found = True
					location = _v.myTables + _v.slash + theFile
				elif os.path.isfile( _v.myTables + _v.slash + theFile ):
					found = True
					location = _v.myTables + _v.slash + theFile


	if found:
		if location.lower().endswith( '.json' ):
			saveTable2( rows, location, printThis )
			if printThis:
				print_( 'Saved: ', location )
			return True

		if location.lower().endswith( '.txt' ):
			saveText( rows, location )
			if printThis:
				print_( 'Saved: ', location )
			return True


	t = type( rows )
	if t == str:
		location = _v.myTables + _v.slash + theFile + '.txt'
		saveText( rows, location )
		if printThis:
			print_( 'Saved: ', location )
		return True

	if t == dict:
		saveTable( rows, theFile+'.json', printThis )
		return True
	if t == list:
		if len(rows) == 0:
			print_( 'Error: no data to save' )
			return False

		t = type( rows[0] )
		if t == dict:
			saveTable( rows, theFile+'.json', printThis )
			return True
		pass
		if t == str:
			location = _v.myTables + _v.slash + theFile + '.txt'
			saveText( rows, location )
			if printThis:
				print_( 'Saved: ', location )
			return True

	print_( 'Error: unable to save file' )
	return False



def getData( theFile, exitOnError=False ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	location = theFile
	if os.path.isfile( theFile ):
		found = True
	
	if not os.path.isfile( theFile ):
		found = False
		if not _v.slash in theFile:
			if not '.' in theFile:
				if os.path.isfile( _v.myTables + _v.slash + theFile + '.json' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.json'
				elif os.path.isfile( _v.myTXT + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTXT + _v.slash + theFile + '.txt'
				elif os.path.isfile( _v.myTables + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.txt'
			else:
				if os.path.isfile( _v.myTables + _v.slash + theFile ):
					found = True
					location = _v.myTables + _v.slash + theFile
				elif os.path.isfile( _v.myTXT + _v.slash + theFile ):
					found = True
					location = _v.myTXT + _v.slash + theFile

		if not found:
			print_( 'Error: unable to locate file' )
			if exitOnError:
				sys.exit()
			return []



	if not os.path.isfile( theFile ):
		if location.lower().endswith( '.json' ):
			return getTable2( location )



	file = getText( location, raw=True, clean=1 )
	textList = file.split('\n')
	if '[' in textList or '{' in textList:
		data = eval( file )
	else:
		data = textList
	return data



class ColorBold:
	gray = '\033[1;30;40m'
	red = '\033[1;31;40m'
	green = '\033[1;32;40m'
	yellow = '\033[1;33;40m'
	blue = '\033[1;34;40m'
	magenta = '\033[1;35;40m'
	cyan = '\033[1;36;40m'
	white = '\033[1;37;40m'
	underline = '\033[4m'
	end = '\033[0m'


class Color:
	purple = '\033[95m'
	cyan = '\033[96m'
	darkcyan = '\033[36m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	end = '\033[0m'


class Background:
	red = '\033[1;37;41m'
	green = '\033[1;37;42m'
	yellow = '\033[1;37;43m'
	blue = '\033[1;37;44m'
	purple = '\033[1;37;45m'
	light_blue = '\033[1;37;46m'
	grey = '\033[1;37;47m'
	black = '\033[1;37;48m'
	end = '\033[0m'

class BackgroundGrey:
	black = '\033[0;30;47m'
	red = '\033[0;31;47m'
	green = '\033[0;32;47m'
	brown = '\033[0;33;47m'
	blue = '\033[0;34;47m'
	magenta = '\033[0;35;47m'
	cyan = '\033[0;36;47m'
	gray = '\033[0;37;40m'
	end = '\033[0m'
	
class BackgroundGreyBold:
	black = '\033[1;30;47m'
	red = '\033[1;31;47m'
	green = '\033[1;32;47m'
	brown = '\033[1;33;47m'
	blue = '\033[1;34;47m'
	magenta = '\033[1;35;47m'
	cyan = '\033[1;36;47m'
	gray = '\033[1;37;40m'
	end = '\033[0m'
	


row_colors = []

row_colors.append([ 0, Background.blue ])
row_colors.append([ 0, Background.light_blue ])
row_colors.append([ 0, Background.purple ])

row_colors.append([ 1, BackgroundGrey.red ])
row_colors.append([ 1, BackgroundGrey.brown ])
row_colors.append([ 1, BackgroundGrey.blue ])

row_colors.append([ 2, Color.cyan ])
row_colors.append([ 2, Color.green ])

row_colors_ID = 0

colorHelp_colorList = [
	"ColorBold.gray",
	"ColorBold.red",
	"ColorBold.green",
	"ColorBold.yellow",
	"ColorBold.blue",
	"ColorBold.magenta",
	"ColorBold.cyan",
	"ColorBold.white",

	"",

	"Color.purple",
	"Color.cyan",
	"Color.darkcyan",
	"Color.blue",
	"Color.green",
	"Color.yellow",
	"Color.red",
	"Color.bold",
	
	"",

	"Background.red",
	"Background.green",
	"Background.yellow",
	"Background.blue",
	"Background.purple",
	"Background.light_blue",
	"Background.grey",
	"Background.black",

	"",

	"BackgroundGrey.black",
	"BackgroundGrey.red",
	"BackgroundGrey.green",
	"BackgroundGrey.brown",
	"BackgroundGrey.blue",
	"BackgroundGrey.magenta",
	"BackgroundGrey.cyan",
	"BackgroundGrey.gray",

	"",

	"BackgroundGreyBold.black",
	"BackgroundGreyBold.red",
	"BackgroundGreyBold.green",
	"BackgroundGreyBold.blue",
	"BackgroundGreyBold.magenta",
	"BackgroundGreyBold.cyan",
	"BackgroundGreyBold.gray"
]

def colorHelp( ipsum=False ):
	global colorHelp_colorList
	for sample in colorHelp_colorList:
		if not len( sample ):
			print_()
		else:
			result = eval( sample + '+ "THE_TEXT" + Color.end' )
			if ipsum:
				result = result.replace( 'THE_TEXT', ipsumSentence() )
			else:
				result = result.replace( 'THE_TEXT', sample )
			
			print_( result )
	sys.exit()


def buldColorTable( tableID ):
	global row_colors
	newColorTable = []
	for row in row_colors:
		if row[0] == tableID:
			newColorTable.append( row[1] )
	return newColorTable

def colorNext( tableID ):
	row_colors = buldColorTable( tableID )
	global row_colors_ID
	row_colors_ID += 1
	# if row_colors_ID == len(row_colors):
	if row_colors_ID % len(row_colors) == 0:
		row_colors_ID = 0

def colorID( tableID, up=True ):
	row_colors = buldColorTable( tableID )
	global row_colors_ID
	result = row_colors[row_colors_ID]
	if up:
		colorNext( tableID )
	return result

colorizeRow_last = None
def colorizeRow( row, tableID=False, prefix='', prefixColor='', haltColorShift=False, pipe_break=True ):
	global colorizeRow_last
	if len(prefix) and len(prefixColor):
		prefix = colorThis( prefix, prefixColor, p=0 )
	global switches
	if switches.isActive( 'NoColor' ):
		print_( row.replace('‽','') )
		return False

	if type(tableID) == bool:
		tableID = __.color_palette
	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		print_( row )
	else:
		if _str.hasVisible(row):
			up =True
		else:
			up =False
		# print_( 'tableID:', tableID, colorID( tableID ) )
		# print_( str(len(row))+colorID( tableID, up ) + row + Background.end )
		if colorizeRow_last is None or not haltColorShift:
			colorizeRow_last = colorID( tableID, up )
		if not pipe_break or not __.tableLine in row:
			print_( prefix + colorizeRow_last + row + Background.end )
		else:
			sep = colorThis( ' ', 'red', p=0 )
			line = prefix + sep
			parts=[]
			for part in row.split(__.tableLine):
				parts.append( colorizeRow_last + part + Background.end )
				
			line += sep.join(parts) + sep
			print_(line)




app_full_color_index = None
def generateColorIndex():
	global app_full_color_index
	if not app_full_color_index is None:
		return app_full_color_index
	colorClasses = 'ColorBold Color Background BackgroundGrey BackgroundGreyBold'
	list_of_colors = []
	test = 0
	if test == 0:
		for cc in colorClasses.split(' '):
			for x in dir(  eval(  '_.'+cc  )  ):
				if not x.startswith('_'):
					
					subject = x
					subject = subject.lower()
					if not subject in list_of_colors:
						list_of_colors.append( subject )

					subject = cc+'.'+x
					subject = subject.lower()
					if not subject in list_of_colors:
						list_of_colors.append( subject )


	test = 1
	if test == 1:
		for x in _.colorHelp_colorList:
			if '.' in x:
				p = x.split('.')
				a = p[0]+'.'
				aa = a.lower()
				b = p[1]
				bb = b.lower()

				subject = bb
				if not subject in list_of_colors:
					list_of_colors.append( subject )

				subject = x.lower()
				if not subject in list_of_colors:
					list_of_colors.append( subject )


	app_full_color_index = []

	for x in list_of_colors:
		if not '.' in x:
			app_full_color_index.append( x )

	for x in list_of_colors:
		if '.' in x:
			app_full_color_index.append( x )

	return app_full_color_index



# _.colorThis( [ '\t', part_profile  ], 'yellow', simpleDic=True, colorProfile=[  ] )

# simpleDic=True, simpleDicColor=[ [ 'match', 'red' ] ]
def colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False, simpleDic=False, colorProfile=None,      p=None, c=None, sd=None, isError=False ):

	if isError:
		color = 'red'

	if not c is None:
		color = c
	if not sd is None:
		simpleDic = sd

	if not p is None:
		shouldPrint = p

	if simpleDic and type(strings) == dict:
		newString = ''
		for k in strings.keys():
			newString += ' ' + k + ': ' + str(strings[k]) + ' '
		strings = newString

	if simpleDic and type(strings) == list:
		for i,thisItem in enumerate(strings):
			if type(thisItem) == dict:
				newString = ''
				for k in thisItem.keys():
					newString += ' ' + k + ': ' + str(thisItem[k]) + ' '
				strings[i] = newString

# [ { 'color': 'red', 'field': 'match', 'i': 0  } ]
# [ { 'color': 'red', 'field': 'match' } ]
# [ { 'color': 'red', 'i': 0  } ]
# { 'color': 'red', 'i': 0  }
# ['red',1]
# [2,'red']
# ['name','yellow']
# 'red,green'
# 'red,green:*'
# '*red,green'
# 'green,red,green:*'
# 'green:2,red:*,green'

# topic_index
#   'float,2'


# ColorBold Color Background BackgroundGrey BackgroundGreyBold

	
	# color_index = generateColorIndex()
	# colorProfileTmp = []
	# index = {
	#             'i': [],
	#             'keys': [],
	#             'data': {},
	# }
	# if not colorProfile is None:
	#     if type(colorProfile) == str:
	#         if type(strings) == list and ',' in colorProfile:
	#             if colorProfile.count('*') > 1:
	#                 print_( ' only 1 * ' )
	#             new_CP = []
	#             cp = colorProfile.split(',')
	#             end = len(strings)-1
	#             leftC = len(cp)-1
	#             leftL = end


	#             for i,xx in enumerate(strings):



	#     if type(colorProfile) == list:
	#         for i,record in enumerate(colorProfile):
	#             if type(record) == dict:
	#                 record['id'] = i
	#                 if 'c' in record.keys():
	#                     record['color'] = record['c']
	#                     del record['c']

	#                 if 'f' in record.keys():
	#                     record['field'] = record['f']
	#                     del record['f']

	#                 if 'column' in record.keys():
	#                     record['field'] = record['column']
	#                     del record['column']


	#                 if 'i' in record.keys():
	#                     index['i'].append( record['i'] )
	#                     index['data'][i] = record
					
	#                 if 'field' in record.keys():
	#                     if ',' in record['field']:
	#                         for ef in record['field'].split(','):
	#                             index['keys'].append( ef )
	#                             index['data'][ ef ] = record
	#                     else:
	#                         index['keys'].append( record['field'] )
	#                         index['data'][record['field']] = record
	#                 colorProfileTmp.append( record )
					
	#             if type(record) == list:
	#                 if len(record) == 2:
	#                     newRecord = { 'id': i }


	#                     if type( record[0] ) == int:
	#                         newRecord['i'] = record[0]
	#                         newRecord['color'] = record[1]

	#                     elif type( record[1] ) == int:
	#                         newRecord['i'] = record[1]
	#                         newRecord['color'] = record[0]
	#                     else:
	#                         if record[0].lower() in color_index:
	#                             newRecord['field'] = record[0]
	#                             newRecord['color'] = record[1]
	#                         if record[1].lower() in color_index:
	#                             newRecord['field'] = record[1]
	#                             newRecord['color'] = record[0]

	#                     if 'color' in newnewRecord.keys():

	#                         if 'i' in newRecord.keys():
	#                             index['i'].append( newRecord['i'] )
	#                             index['data'][i] = newRecord
							
	#                         if 'field' in newRecord.keys():
	#                             if ',' in newRecord['field']:
	#                                 for ef in newRecord['field'].split(','):
	#                                     index['keys'].append( ef )
	#                                     index['data'][ ef ] = newRecord
	#                             else:
	#                                 index['keys'].append( newRecord['field'] )
	#                                 index['data'][newRecord['field']] = newRecord
	#                         colorProfileTmp.append( newRecord )



	#     if type(colorProfile) == dict:
	#         record = colorProfile
	#         if 'c' in record.keys():
	#             colorProfile[i]['color'] = record['c']
	#             record['color'] = record['c']
	#         if 'f' in record.keys():
	#             colorProfile[i]['field'] = record['f']
	#             record['field'] = record['f']
	#         if 'column' in record.keys():
	#             colorProfile[i]['field'] = record['column']
	#             record['field'] = record['column']


	#         if 'i' in record.keys():
	#             index['i'].append( record['i'] )
			
	#         if 'field' in record.keys():
	#             index['keys'].append( record['field'] )
	#         colorProfile = [record]




	if type(strings) == list:

		for i,x in enumerate(strings):

			strings[i] = str( x )

		string = ' '.join( strings )
	else:
		string = str(strings)

	global switches
	if switches.isActive( 'NoColor' ):
		if shouldPrint:
			print_(string.replace('‽',''))
			return string
		else:
			return string

	if ipsum:
		string = ipsumSentence()

	found = False

	if color == 'help':
		print_()
		print_()
		print_( "_.colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False )" )
		print_()
		print_()
		colorHelp( ipsum )


	pass 
	aaPre=''
	ws=ws_sep(string)
	aaPre=ws[0]
	string=ws[1]
	result=''


	if '.' in color:

		try:
			result = eval( color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True

	else:
		color = color.lower()


	if not found and notBold:
		try:
			result = eval( 'Color.' + color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'ColorBold.' + color + '+ string + ColorBold.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'Color.' + color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'Background.' + color + '+ string + Background.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'BackgroundGrey.' + color + '+ string + BackgroundGrey.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'BackgroundGreyBold.' + color + '+ string + BackgroundGreyBold.end')
		except Exception as e:
			pass
		else:
			found = True

	result = aaPre+result
	
	if not found:
		printBold( 'Error: _.colorThis: color not found ' + str(color), 'red' )
		print_()
		print_( strings )
		print_()
		colorHelp( ipsum )

		sys.exit()



	if shouldPrint:
		try:
			print_( result )
		except Exception as e:

			try:
				result = str(result,'utf-8')
			except Exception as e:
				try:
					result = str(result,'iso-8859-1')
				except Exception as e:
					result = result.encode('utf-8')
			result = str(result,'iso-8859-1')
		if isError:
			sys.exit()
		return None



	return result

def ws_sep(string):
	a=''
	b=''
	done=False
	for ch in string:
		if done:
			b+=ch
		elif ch in ' \t':
			a+=ch
		else:
			b+=ch
			done=True
	return a,b


def inlineColor( string, color='red' ):

	global switches
	if switches.isActive( 'NoColor' ):
		return string.replace('‽','')

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'red':
		return Color.red + string + Color.end
	elif color == 'cyan':
		return Color.cyan + string + Color.end
	elif color == 'darkcyan' or color == 'grey':
		return Color.darkcyan + string + Color.end
	elif color == 'blue':
		return Color.blue + string + Color.end
	elif color == 'green':
		return Color.green + string + Color.end
	elif color == 'yellow':
		return Color.yellow + string + Color.end
	elif color == 'underline':
		return Color.underline + string + Color.end


def printColor( string, color='red' ):

	global switches
	if switches.isActive( 'NoColor' ):
		print_( string.replace('‽','') )
		return False

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'red':
		print_( Color.red + string + Color.end )
	elif color == 'cyan':
		print_( Color.cyan + string + Color.end )
	elif color == 'darkcyan' or color == 'grey':
		print_( Color.darkcyan + string + Color.end )
	elif color == 'blue':
		print_( Color.blue + string + Color.end )
	elif color == 'green':
		print_( Color.green + string + Color.end )
	elif color == 'yellow':
		print_( Color.yellow + string + Color.end )
	elif color == 'underline':
		print_( Color.underline + string + Color.end )

# def formatData( result ):
#     try:
#         result = str(result,'utf-8')
#     except Exception as e:
#         try:
#             result = str(result,'iso-8859-1')
#         except Exception as e:
#             result = result.encode('utf-8')
#     return result

def printBold( string, color='white', prefix='' ):
	
	if '\n' in string:
		string = string.replace( '\n', '\n'+prefix )
	else:
		string = prefix + string
	
	global switches
	if switches.isActive( 'NoColor' ):
		print_( string.replace('‽','') )
		return False

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		print_( ColorBold.white + string + ColorBold.end )
	elif color == 'red':
		print_( ColorBold.red + string + ColorBold.end )
	elif color == 'gray' or color == 'grey':
		print_( ColorBold.gray + string + ColorBold.end )
	elif color == 'green':
		print_( ColorBold.green + string + ColorBold.end )
	elif color == 'yellow':
		print_( ColorBold.yellow + string + ColorBold.end )
	elif color == 'blue':
		print_( ColorBold.blue + string + ColorBold.end )
	elif color == 'magenta':
		print_( ColorBold.magenta + string + ColorBold.end )
	elif color == 'cyan':
		print_( ColorBold.cyan + string + ColorBold.end )


def inlineColorGroup( row, tableID=False ):

	global switches
	if switches.isActive( 'NoColor' ):
		return row

	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		tableID = __.color_palette
	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		print_( row )
	else:
		if _str.hasVisible(row):
			up =True
		else:
			up =False
		# print_( 'tableID:', tableID, colorID( tableID ) )
		return colorID( tableID, up ) + row + Background.end


def inlineBold( string, color='white' ):
	global switches
	if switches.isActive( 'NoColor' ):
		return string.replace('‽','')
	
	string = str(string)
	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		return ColorBold.white + string + ColorBold.end 
	elif color == 'red':
		return ColorBold.red + string + ColorBold.end 
	elif color == 'gray' or color == 'grey':
		return ColorBold.gray + string + ColorBold.end 
	elif color == 'green':
		return ColorBold.green + string + ColorBold.end 
	elif color == 'yellow':
		return ColorBold.yellow + string + ColorBold.end 
	elif color == 'blue':
		return ColorBold.blue + string + ColorBold.end 
	elif color == 'magenta':
		return ColorBold.magenta + string + ColorBold.end 
	elif color == 'cyan':
		return ColorBold.cyan + string + ColorBold.end
	elif color == 'underline':
		return ColorBold.underline + string + ColorBold.end

def patternMatch( one, two, best=True, simple=True, both=False, unsorted=False ):
	# simple=True
	result = []
	result.append( testPatterns( one, two, simple ) )
	result.append( testPatterns( two, one, simple ) )
	if type(both) == int and both == 2:
		return result
	if not both:
		if best:
			return max(result)
		else:
			return min(result)
	else:
		if unsorted:
			return result

		if not simple:
			if result[0][0] > result[1][0]:
				return result[0],result[1]
			else:
				return result[1],result[0]
		else:
			if result[0] > result[1]:
				return result[0],result[1]
			else:
				return result[1],result[0]

def testPatterns( one, two, simple=True ):
	if one == two: return 100

	test = False
	spent = []
	patterns = []
	matches = []
	def tempDataset( datasetX ):
		newDataset = []
		for dat in datasetX:
			newDataset.append( dat )
		return newDataset
	def genChars( datasetY, x=False ):
		chars = []
		for d in datasetY:
			chars.append( one[d] )
			if x:
				print_( one[d], d )
		return ''.join( chars )
	def addSpent( datasetY ):
		for d in datasetY:
			spent.append( d )

	def addMatch( datasetY ):
		for d in datasetY:
			if not d in matches:
				matches.append( d )

	def testSpent( datasetX ):
		for d in datasetX:
			if d in spent:
				return False
		return True

	def expandTest( datasetX ):
		if testSpent( datasetX ):
			first = datasetX[0]
			last = datasetX[len(datasetX)-1]
			theLast = len(datasetX)-1
			theMax = len(one)-1

			datasetY = tempDataset( datasetX )
			if not datasetX[0] == 0:
				nextFirst = int(first)
				for x in range(1,100000):
					nextFirst = first - 1
					if nextFirst >= 0:
						datasetY.append( nextFirst )
						datasetY.sort()
						if not genChars( datasetY ) in two:
							datasetY.pop(0)
							break
					else:
						break
			if not datasetY[len(datasetY)-1] == theMax:
				nextLast = int(datasetY[len(datasetY)-1])
				# print_()
				# print_( 'nextLast:', nextLast )
				for x in range(1,100000):
					# print_()
					# print_( nextLast, x, nextLast + x )
					nextLast = nextLast + 1
					if nextLast <= theMax:
						datasetY.append( nextLast )
						datasetY.sort()
						if not genChars( datasetY, x=False ) in two:
							datasetY.reverse()
							datasetY.pop(0)
							datasetY.reverse()
							addSpent( datasetY )
							addMatch( datasetY )
							patterns.append( genChars( datasetY ) )
							# print_( '\t1' )
							break
					else:
						addSpent( datasetY )
						addMatch( datasetY )
						patterns.append( genChars( datasetY ) )
						# print_( '\t2' )
						break
			else:
				addSpent( datasetY )
				addMatch( datasetY )
				patterns.append( genChars( datasetY ) )
				# print_( '\t3' )

	def runTest( patternLength ):
		data = generatePatterns2( one, 2 )
		# data = generatePatterns( one, 2 )
		# print_( len(data) )
		i = 0
		ii = 0
		for dataset in data:
			x = genChars( dataset )
			if x in two:
				addMatch( dataset )
				expandTest( dataset )
				# print_( x )
				if test:
					print_( x )
				i += 1
			else:
				ii += 1

		result = percentageDiffInt( i, len(data) )
		return result
	resultX = []

	for x in range(2,10):
		if len( one ) > x:
			resultX.append( runTest( x ) )


	newResult = percentageDiffInt( len(matches), len(one) )
	# print_( patterns )
	# print_( newResult )
	if simple:
		return newResult
	else:
		return newResult, tuple(patterns)

def testPatterns22( one, two, simple=True ):
	if one == two: return 100

	test = False
	spent = []
	patterns = []
	matches = []
	def tempDataset( datasetX ):
		newDataset = []
		for dat in datasetX:
			newDataset.append( dat )
		return newDataset
	def genChars( datasetY, x=False ):
		chars = []
		for d in datasetY:
			chars.append( one[d] )
			if x:
				print_( one[d], d )
		return ''.join( chars )
	def addSpent( datasetY ):
		for d in datasetY:
			spent.append( d )

	def addMatch( datasetY ):
		for d in datasetY:
			if not d in matches:
				matches.append( d )

	def testSpent( datasetX ):
		for d in datasetX:
			if d in spent:
				return False
		return True

	def expandTest( datasetX ):
		if testSpent( datasetX ):
			first = datasetX[0]
			last = datasetX[len(datasetX)-1]
			theLast = len(datasetX)-1
			theMax = len(one)-1

			datasetY = tempDataset( datasetX )
			if not datasetX[0] == 0:
				nextFirst = int(first)
				for x in range(1,100000):
					nextFirst = first - 1
					if nextFirst >= 0:
						datasetY.append( nextFirst )
						datasetY.sort()
						if not genChars( datasetY ) in two:
							datasetY.pop(0)
							break
					else:
						break
			if not datasetY[len(datasetY)-1] == theMax:
				nextLast = int(datasetY[len(datasetY)-1])
				# print_()
				# print_( 'nextLast:', nextLast )
				for x in range(1,100000):
					# print_()
					# print_( nextLast, x, nextLast + x )
					nextLast = nextLast + 1
					if nextLast <= theMax:
						datasetY.append( nextLast )
						datasetY.sort()
						if not genChars( datasetY, x=False ) in two:
							datasetY.reverse()
							datasetY.pop(0)
							datasetY.reverse()
							addSpent( datasetY )
							addMatch( datasetY )
							patterns.append( genChars( datasetY ) )
							# print_( '\t1' )
							break
					else:
						addSpent( datasetY )
						addMatch( datasetY )
						patterns.append( genChars( datasetY ) )
						# print_( '\t2' )
						break
			else:
				addSpent( datasetY )
				addMatch( datasetY )
				patterns.append( genChars( datasetY ) )
				# print_( '\t3' )

	def runTest( patternLength ):
		data = generatePatterns( one, 2 )
		# data = generatePatterns( one, 2 )
		# print_( len(data) )
		i = 0
		ii = 0
		for dataset in data:
			x = genChars( dataset )
			if x in two:
				addMatch( dataset )
				expandTest( dataset )
				# print_( x )
				if test:
					print_( x )
				i += 1
			else:
				ii += 1

		result = percentageDiffInt( i, len(data) )
		return result
	resultX = []

	for x in range(2,10):
		if len( one ) > x:
			resultX.append( runTest( x ) )


	newResult = percentageDiffInt( len(matches), len(one) )
	# print_( patterns )
	# print_( newResult )
	if simple:
		return newResult
	else:
		return newResult, tuple(patterns)

def generatePatterns( string, patternLength=2 ):

	def genP( by ):
		
		offset = 0
		dataset = []
		for offset in range(0,by):
			# print_( offset )
			ix = False
			for i,char in enumerate(string):
				if i >= offset:
					ix = ( i + offset )
					
				if not type(ix) == bool:
					# dataset.append( char )
					dataset.append( i )
					if len(dataset) % by == 0:
						if len( dataset ):
							dataset.sort()
							data.append( dataset )
							# print_( ''.join( dataset ) )
						dataset = []


	l = len( string )
	data = []
	genP( patternLength )
	return data

def generatePatterns2( data, patternLength=2 ):
	records = []
	m = len(data)
	for n in range(0,len(data)):
		# a = n-1
		good = True
		pl = 0
		rec = []
		new = n
		while not pl == patternLength:
			if not new < m:
				good = False
			rec.append( new )
			new+=1
			pl+=1
		b = n
		c = n+1
		# if a > -1:
		#   records.append([ a,b ])
		# if c < m:
		if good:
			records.append( rec )
	return records

def patternz(string):
	pat = generatePatterns2( string )
	ptz=[]
	for x in pat:
		z=[]
		for y in x:
			z.append(string[y])
		ptz.append(''.join(z))
	return ptz






def stringDiff( one, two ):
	one = one.lower()
	two = two.lower()
	appropriate = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

	if len(one) > len(two):
		a = len(one)
		b = len(two)
	else:
		b = len(one)
		a = len(two)
	d = a - b
	# if d > 2:
	#   return False
	setA = 0
	theTotal_one = 0
	theTotal_two = 0
	for x in appropriate:
		if x in two:
			theTotal_two += 1
		if x in one:
			theTotal_one += 1
		if x in one and x in two:
			setA += 1

	resultX = []
	resultX.append(percentageDiffInt( setA, theTotal_one ))
	resultX.append(percentageDiffInt( theTotal_one, theTotal_two ))
	resultX.append(percentageDiffInt( theTotal_one, theTotal_two ))
	resultX.append( testPatterns( one, two ) )
	result = max(resultX)
	
	# resultY = []
	# resultY.append(min(resultX))
	# resultY.append(patternMatch( one, two ))
	# result = max(resultY)
	# print_()
	# print_( setA, theTotal_one )
	# print_( resultX, one, two )

	return result



def fromEpoch( epoch ):
	return datetime.datetime.fromtimestamp(epoch).strftime('%c')

def postLoad( file, epoch=0, theFocus=False ):
	__.postLoadFile = file
	global autoLoadData
	global switches
	global appData
	


	try:
		__.appInfoScan
	except Exception as e:
		pass
	if not type( theFocus ) == bool:
		theFocus = theFocus
	else:
		theFocus = __.appReg

		# print_( 'theFocus:', theFocus )
		# printVar( appData )
		if  theFocus in appData:
			if type( appData[theFocus]['pipe'] ) == bool:
				hasPipeData = False
			else:
				hasPipeData = True
		else:
			hasPipeData = False



		# print_( type( appData[theFocus]['pipe'] ) )


		# print_( appData[theFocus]['pipe'] )


		if type( myFileLocation_File ) == bool:
			hasFile = False
		else:
			hasFile = True
		
		# if __.isRequired_Pipe_or_File and not hasFile and not hasPipeData:
		#     if __.pre_error:
		#         print_(  )
		#         print_( inlineBold('Error:','red')+inlineBold(' Pipe')+' data or '+inlineBold('File')+' is required' )
		#         print_(  )
		#         sys.exit()

		# if __.isRequired_Pipe and not hasPipeData:
		#     if __.pre_error:
		#         print_(  )
		#         print_( 'Error: Pipe data is required' )
		#         print_(  )
		#         sys.exit()

		on = switches.records( formating='dic_on-off-v', appReg=theFocus )['on']
		# printVarSimple(on)
		metCriteria = True
		if __.isRequired_or_List is None:
			if __.isRequired_Pipe:
				__.isRequired_or_List = ['Pipe']
			if __.isRequired_Pipe_or_File:
				__.isRequired_or_List = ['Pipe','Files']


		if not __.isRequired_or_List is None:
			if __.pre_error:
				fnd = False
				if not metCriteria:
					if not hasPipeData and 'Pipe' in __.isRequired_or_List:
						metCriteria = False
				if not metCriteria:
					for x in __.isRequired_or_List:
						if not x == 'Pipe':
							if x in on:
								fnd = True
					if not fnd:
						metCriteria = False
				
				if not metCriteria:
					help()
		if metCriteria:
			if len( __.isRequired_index[theFocus] ):
				fnd = False
				for x in __.isRequired_index[theFocus]:
					if not x == 'Pipe':
						if x in on:
							fnd = True
				if not fnd:
					metCriteria = False
			
			if not metCriteria:
				help()

		# if metCriteria:


		# if not type( __.isRequired_or_List ) == bool and __.registeredApps[0] == __.appReg:
		#     meetsRequirements = False


		#     if 'Pipe' in __.isRequired_or_List:
		#         if hasPipeData:
		#             meetsRequirements = True
		#         if not hasFile and not hasPipeData:
		#             pass
		#         else:
		#             meetsRequirements = True
		#     if not meetsRequirements:
		#         for check in __.isRequired_or_List:
		#             if switches.isActive(check):
		#                 meetsRequirements = True
		#         if not meetsRequirements:
		#             if __.pre_error:
		#                 print_(  )
		#                 print_( inlineBold( 'Error:', 'red' ) + ' One of the following is required:', ', '.join( __.isRequired_or_List ) )
		#                 print_(  )

		#                 # print_( __.registeredApps )

		#                 sys.exit()


	appDBA = __.thisApp( file )

	if switches.isActive( 'LoadEpoch' ):
		if '.' in switches.value( 'LoadEpoch' ):
			autoLoadData = True
			epoch = float( switches.value( 'LoadEpoch' ) )
	if autoLoadData and epoch == 0:
		if type( autoLoadData ) == str:
			if '.' in autoLoadData:
				epoch = float( autoLoadData )
		if type( autoLoadData ) == float:
			epoch = autoLoadData

		if epoch == 0:
			autoLoadData = False


	if autoLoadData:
		reclaimAcquiredData( appDBA, epoch, theFocus )
	else:
		releaseAcquiredData( appDBA, theFocus )


raq_err=True
def releaseAcquiredData( appDBA, theFocus, payload=None ):
	global raq_err
	l_registerSwitches_vars()
	if appDBA == '__init__':
		return None
	if not __.releaseAcquiredData:
		return None
	if not os.name == 'nt':
		return None
	global autoBackupData
	global switches
	global appData
	global myFileLocation_Files
	global switches
	global print_ed


	log = _v.appLogs()+_v.slash+day(time.time())+'execution_receipt-' + appDBA + '-' + str( __.startTime ) + '.json'
	rebuiltCommandRaw = theCommand( appDBA, printThis=False, separate=True )
	if len( rebuiltCommandRaw[1] ):
		rebuiltCommand = rebuiltCommandRaw[0] + ' ' + rebuiltCommandRaw[1]
		rebuiltCommandEpoch = rebuiltCommandRaw[0] + ' -loadEpoch ' + str( __.startTime ) + ' ' + rebuiltCommandRaw[1]
	else:
		rebuiltCommand = rebuiltCommandRaw[0]
		rebuiltCommandEpoch = rebuiltCommandRaw[0] + ' -loadEpoch ' + str( __.startTime ) 
	# print_( log )
	# print_( rebuiltCommandRaw )


	# autoBackupData = True



	info = {
				'epoch': __.startTime,
				'app': appDBA,
				'session': _v.session(),
				'rebuiltCommand': rebuiltCommand,
				'rebuiltCommandEpoch': rebuiltCommandEpoch,
				'files': [],
				'switches': switches.getTable(),
				'errors': [],
				'printed': print_ed,
	}
	if not payload is None:
		info['payload'] = payload

	# if not autoBackupData:
	# _v.mkdir( __.path(log,pop=True) )
	_v.mkdir( log, isFile=True )
	try: saveTable2( info, log )
	except:
		if raq_err: pr('d8f3',c='red')
	# print(log)
	# print(info)
	# print(log)

	if autoBackupData:
		if len( myFileLocation_Files ):
			for i,file in enumerate(myFileLocation_Files):
				if os.path.isfile(file):
					thisName = 'files-' + appDBA + '-' + str( __.startTime ) + '_file' + str(i) + '.cache'
					import _rightThumb._dir as _dir
					dirRecord = _dir.info( file, mime=True )
					info['errors'] = []
					fileError = 'Error: File is ' + dirRecord['mime'] + ' and ' + dirRecord['size']
					try:
						if dirRecord['mime'] == 'Text' and dirRecord['bytes'] < 5242880:
							tmpData = getText( file )
							saveText( tmpData, _v.myAppLogs + _v.slash + thisName )
							info['files'].append( thisName )
						else:
							info['errors'].append({ 'error': fileError, 'file': _v.myAppLogs + _v.slash + thisName })
							saveText( fileError, _v.myAppLogs + _v.slash + thisName )
							

					except Exception as e:
						info['errors'].append({ 'error': fileError, 'file': _v.myAppLogs + _v.slash + thisName })

		# print_( theFocus, type( appData[theFocus]['pipe'] ) )
		# print_('theFocus',theFocus)
		if not type( appData[theFocus]['pipe'] ) == bool:
			thisName = 'files-' + appDBA + '-' + str( __.startTime ) + '_pipe' + '.cache'
			saveText( appData[theFocus]['pipe'], _v.myAppLogs + _v.slash + thisName )
			# print_(info)
			info['files'].append( thisName )
			
		

		saveTable2( info, log )

		# print_()
		# print_()
		# printVar( info )

	# 
# _.theCommand( __file__ )
# file0 = _v.myTables + _v.slash+'applogs'+_v.slash + log

def reclaimAcquiredData( appDBA, epoch, theFocus=False ):
	print_( 'reclaimAcquiredData' )
	global switches
	if not type( theFocus ) == bool:
		appReg = theFocus
	else:
		appReg = __.appReg

	log = _v.appLogs()+_v.slash+day(time.time()) + _v.slash+'execution_receipt-' + appDBA + '-' + str( epoch ) + '.json'
	print_(  os.path.isfile(log), log )
	if not os.path.isfile(log):
		cp( 'Error: please select a valid backup', 'error' )
		sys.exit()
	info = getTable2( log )
	__.payloadCache = None
	if 'payload' in info:
		__.payloadCache = info['payload']


	# print_( log )
	# print_( info )
	# printVar( info )

	def pipeFile():
		for file in info['files']:
			if 'pipe' in file:
				return _v.myAppLogs + _v.slash + file
		return False

	def theFiles():
		theFiles = []
		for file in info['files']:
			if not 'pipe' in file:
				theFiles.append( _v.myAppLogs + _v.slash + file )
		return theFiles

	def rebuildSwitches( switchData ):
		# printVar( switchData )
		for i,switch in enumerate(switchData):
			if switch['name'] == 'File' or switch['name'] == 'Files':
				switchData[i]['values'] = []
				for file in info['files']:
					if not 'pipe' in file:
						switchData[i]['values'].append( _v.myAppLogs + _v.slash + file )
				switchData[i]['value'] = ','.join( switchData[i]['values'] )
		return switchData

	def rebuildFiles( switchData ):
		data = []
		for i,switch in enumerate(switchData):
			if switch['name'] == 'File' or switch['name'] == 'Files':
				switchData[i]['values'] = []
				for file in info['files']:
					if not 'pipe' in file:
						switchData[i]['values'].append( _v.myAppLogs + _v.slash + file )
				switchData[i]['value'] = ','.join( switchData[i]['values'] )
				data.append( switchData[i] )
		return data
	def rebuildFiles( switchData ):
		for i,switch in enumerate(switchData):
			if switch['name'] == 'File' or switch['name'] == 'Files':
				switchData[i]['values'] = []
				for file in info['files']:
					if not 'pipe' in file:
						switchData[i]['values'].append( _v.myAppLogs + _v.slash + file )
				switchData[i]['value'] = ','.join( switchData[i]['values'] )
				data.append( switchData[i] )
		return data

	pass
	if 'printed' in info:
		# cp( '' )
		for line in info['printed']:
			print(line)

	else:

		if switches.onlyLoadEpoch( theFocus=appReg ):
			switchData = rebuildSwitches( info['switches'] )
		else:
			switchData = rebuildFiles( info['switches'] )
		# printVar( switchData )
		switches.loadTable( switchData, theFocus=appReg )
		# print_( 'theFocus:', theFocus )

		if not type( pipeFile() ) == bool:
			appData[appReg]['pipe'] = getText( pipeFile() )



def theCommand( file='', theFocus=False, printThis=True, justSwitches=False, separate=False ):
	global switches
	# _.theCommand( __file__, theFocus=False, printThis=True, justSwitches=False  )
	
	if not type( theFocus ) == bool:
		appReg = theFocus
	else:
		appReg = __.appReg
	if len( file ):
		if _v.slash in file or '.py' in file.lower():
			appDBA = __.thisApp( file )
		else:
			appDBA = file
	else:
		appDBA = ''
	theSwitchInfo = switches.rebuild()
	if justSwitches:
		result = theSwitchInfo
	else:
		result = 'p ' + appDBA + ' ' + theSwitchInfo
	if printThis:
		print_( result )
	if separate:
		return [ 'p ' + appDBA, theSwitchInfo ]

	return result

def triggerSpace( data ):
	data = data.replace( ',', ' ' )
	return data

def longDashAdd( data ):
	data = _str.clean_latin1( data )
	data = data.replace( ' :', ':' )
	data = data.replace( '-', '—' )
	return data

def longDashRemove( data ):
	data = data.replace( '—', '-' )
	return data


def inRelevantFolder( file ):
	# if __.myFileLocations_SKIP_VALIDATION:
	#   return file
	found = inRelevantFolderSearch( file )
	if type( found ) == bool:
		return file
	if os.path.isfile( found ):
		myFileLocation_Files.append( found )
	return found
def inRelevantFolderSearch( file ):
	# if __.myFileLocations_SKIP_VALIDATION:
	#   return file
	if os.path.isfile( file ):
		return os.getcwd() +_v.slash+ file

	probableLocations = [
		"_v.py + _v.slash+''+_v.slash + '*THEFILENAME*' + '.py'",
		"_v.py + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myTables + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'batch'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'batch'+_v.slash + '*THEFILENAME*' + '.bat'",
		"_v.myDatabases + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'Downloads'+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'exe'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'php'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'php'+_v.slash + '*THEFILENAME*' + '.php'",
		"_v.myApps + _v.slash+'powershell'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'vbs'+_v.slash + '*THEFILENAME*'",
	]

	for test in probableLocations:
		f = test.replace( '*THEFILENAME*', file )
		if os.path.isfile( f ):
			return f



	global relevantFolders
	if not len( relevantFolders ):
		rf = getText( _v.relevant_folders, raw=True, clean=2 )
		relevantFolders = rf.split('\n')
	# 

	for folder in relevantFolders:
		f = folder +_v.slash+ file
		if os.path.isfile( f ):
			return f
	return False


def hasExtion( data, wild=False, free=False ):
	global theExtensionsList
	if not len( theExtensionsList ):
		if not wild and not free:
			ext = getText( _v.myTables + _v.slash+'extensions.txt', raw=True, clean=2 )
		elif free:
			ext = getText( _v.myTables + _v.slash+'extensions_free.txt', raw=True, clean=2 )
		else:
			ext = getText( _v.myTables + _v.slash+'extensions_wild.txt', raw=True, clean=2 )
		theExtensionsList = ext.split('\n')
	if not free:
		if '.' in data:
			end0 = data[(-4):]
			end1 = data[(-5):]
			if '.' == end0[0] or '.' == end1[0]:
				testX = data.split('.')
				test = testX[len(testX)-1].lower()
				if test in theExtensionsList:
					return True
	else:
		for ext in theExtensionsList:
			if data.lower().endswith( '.'+ext ):
				return True

	return False



def popDelim( data, delim, pop=1 ):
	data = str( data )
	dataX = data.split( delim )
	i = 0
	while not i == pop:
		dataX.pop()
		i+=1
	return delim.join( dataX )


def addComma( data ):
	test = 0
	try:
		int(data)
		test+=1
	except Exception as e:
		pass
	try:
		float(data)
		test+=1
	except Exception as e:
		pass
	
	if not test:
		return data

	txt = str( data )
	if '.' in txt:
		txt = txt.split( '.' )[0]
	n = []
	for x in txt:
		n.append( x )
	n.reverse()
	y = []
	for i,x in enumerate(n):
		y.append( x )
		if ((i+1)%3==0):
			y.append( ',' )
	y.reverse()
	result = ''.join( y )
	result = _str.cleanBE( result, ',' )
	return result



def genAppName( file ):
	if file.lower().endswith( '.py' ):
		x = file.split( '.' )
		x.pop( len(x)-1 )
		result = '.'.join( x )
	else:
		result = file
	return result

def printFields( data, depth=1 ):
	if depth == 1:
		print_()
	def tabLoop( depth ):
		result = ''
		i=0
		while not i == depth:
			i+=1
			result += '\t'
		return result
	if type( data ) == list:

		if len(data) and type(data[0]) == dict:
			for row in data[0].keys():
				print_( tabLoop( depth ), row )
				printFields( data[0][row], depth+1 )
	elif type( data ) == dict:
		for row in data.keys():
			print_( tabLoop( depth ), row )
			printFields( data[row], depth+1 )

def removeReturn( data ):
	for i,row in enumerate(data):
		data[i] = data[i].replace( '\n', '' )
	return data

def flattenList( data ):
	result = ''
	for row in data:
		row = row.replace( '\n', '' )
		result += row + '\n'
	result = _str.cleanBE( result, '\n' )
	return result

def resolveIDs( data ):
	global idResolution
	data = str(data)
	# if len( idResolution ) == 0:
	if not len( idResolution ):
		idResolution = getTable('idResolution.json')
	# idResolution = getTable('idResolution.json')
	for idx in idResolution:
		if data in idx['id']:
			return ' ** ' + idx['name'] + ' ** '
	return data

def printSafe( data ):
	data = str( data )
	result = ''
	for ch in data:
		if ch in _v.safeChar:
			result += ch
	return result

def setUmlData( data, openUML=True ):
	saveTable2( data, _v.umlJson )

	with open(_v.umlJson, 'r+') as f:
		content = f.read()
		f.seek(0, 0)
		f.write("theData=" + content)

	# f=open(_v.umlJson,'a')
	# f.seek(0,0)
	# f.write("theData=")
	# f.close()

	if openUML:
		import webbrowser
		webbrowser.open( _v.umlHtml, new=2)
def setPipeData( data, theFocus=False, clean=True ):
	# pr('setPipeData',c='gray')
	# pr(data)
	# pr('setPipeData',c='gray')
	global appData
	if type( theFocus ) == bool:
		theFocus = __.appReg
	# _.appData[__.appReg]['pipe'] = list(data)
	if not appData[theFocus]['pipe'] and len(data) > 0:
		appData[theFocus]['pipe'] = []
		# if not clean:
		# 	appData[theFocus]['pipe'].append('')
		for pd in data:
			if clean:
				pd = pd.replace('\n','')
				pd = pd.replace('\r','')
				if not pd == '':
					appData[theFocus]['pipe'].append(pd)
			else:
				appData[theFocus]['pipe'].append(pd)
		setPipeDataRan = True



def pipeCleaner(clean=0):
	def pipeCleanerDeep(p):
		while p.startswith(' '):
			p = p[1:]

		while p.endswith(' '):
			p = p[:-1]



		while p.startswith('\r'):
			p = p[1:]

		while p.endswith('\r'):
			p = p[:-1]



		while p.startswith('\n'):
			p = p[1:]

		while p.endswith('\n'):
			p = p[:-1]



		while p.startswith('\t'):
			p = p[1:]

		while p.endswith('\t'):
			p = p[:-1]
		return p


	global appData
	try:
		if not appData[__.appReg]['pipe'][0][0] in _str.safeChar:
			appData[__.appReg]['pipe'][0] = appData[__.appReg]['pipe'][0][1:]
	except Exception as e:
		pass
	try:
		for i,pipeData in enumerate(appData[__.appReg]['pipe']):
			p = appData[__.appReg]['pipe'][i].replace('\n','')
			if clean:
				while p.startswith(' '):
					p = p[1:]

				while p.endswith(' '):
					p = p[:-1]
			if type(clean) == int and clean > 1:
				p = pipeCleanerDeep(p)
				p = pipeCleanerDeep(p)
				p = pipeCleanerDeep(p)


			appData[__.appReg]['pipe'][i] = p
	except Exception as e:
		pass
	return appData[__.appReg]['pipe']

""" {7DB6A001-0637-4F13-B328-2B17A481CF35}
def copyVar( data ):
	import pyperclip
	return pyperclip.copy( str(data) )
"""
""" {7DB6A001-0637-4F13-B328-2B17A481CF35}
def openURL( data ):
	import webbrowser
	webbrowser.open( data, new=2 )

def copyDicAsJSON( data, openUML=False ):
	txt = copyVar( d2json( data ) )
	if openUML:
		import webbrowser
		webbrowser.open('https://vanya.jp.net/vtree/', new=2)
	return txt
"""

def cleanDic( data ):
	nowJSON_TXT = d2json( data )
	nowDic = json2d( nowJSON_TXT, True )

def d2json( data, sort_keys=False ):
	simplejson = __.imp('simplejson')
	# saveTable2( data, _v.json_temp )
	# txt = getText( _v.json_temp, raw=True )

	return simplejson.dumps(data, indent=4, sort_keys=sort_keys, default=str)

def printVar1( data ):
	print_( d2json( data ) )


def printVar( data, sort_keys=False, isDic=None ):
	simplejson = __.imp('simplejson')
	result = simplejson.dumps(data, indent=4, sort_keys=False, default=str)
	printVarColor( result )
	print_(  )
	return result
	data = json_clean(data)
	if not isDic is None and isDic and type(data) == str:
		saveText( data, _v.myTemp + _v.slash+'printVar.json' )
		data = getTable2( _v.myTemp + _v.slash+'printVar.json' )
		result = d2json( data, sort_keys )
	else:
		result = data
	# saveTable2( data, _v.json_temp )
	# result = getText( _v.json_temp, raw=True )
	# result = type( result )
	result = printVarColor( result )
	print_(  )

def printTest( data, color='white', line=None, isPrint=1, shouldExit=1, validate=1, raw=0, profile=False, sort_keys=False, pause=None,    r=0, v=1, val=1, l=None, x=1, s=False, sk=False, p=None ):

	data = json_clean(data)

	if not p is None:
		pause = p

	if s or sk:
		sort_keys = True

	if not x:
		shouldExit = 0


	if r:
		raw = True
	if not l is None:
		line = l
	if not v or not val:
		validate = False
	if raw:
		validate = False
	isCode = False

	if p is None:
		pause = p

	shouldPause = False
	if not pause is None:
		shouldPause = True
		shouldExit = 0

	if not line is None:
		colorThis( [ 'Line:', line ], 'green' )
	if type( data ) == dict:
		isCode = True
	elif type( data ) == list and len(data) and type( data[0] ) == dict:
		isCode = True
	elif type( data ) == list and not isPrint:
		isCode = True
	elif type( data ) == list and isPrint:
		isCode = False
	else:
		isCode = False

	if not validate:
		isCode = False

	if profile:
		import _rightThumb._profileVariables as _profile
		profile = _profile.records.audit( 'printTest_profile', data )
		data = profile
		isCode = True
	


	if isCode:
		if validate:
			printVar( data, sort_keys )
		else:
			printVarSimple( data, sort_keys )
	else:
		if raw:
			colorThis( str(data), color )
		else:
			colorThis( data, color )

	if shouldPause:
		print_('pause doesnt work')
		sys.exit()

		pause=input(' - ')
	elif shouldExit:
		# print_('shouldExit')
		sys.exit()


def printVar2( data, sort_keys=False ):
	printVarOld( data, sort_keys )
	
def printVarSimple( data, sort_keys=False, isDic=None, prefix=None, remove=None, d=None, p=True, r=None ):
	#n)--> r, stands for just return and not print
	simplejson = __.imp('simplejson')
	dump=simplejson.dumps(data, indent=4, sort_keys=sort_keys, default=str)
	if d:
		if p:
			print_(dump)
		return dump 
	data = json_clean(data)
	if not isDic is None and isDic and type(data) == str:
		# saveText( data, _v.myTemp + _v.slash+'printVarSimple.json' )
		# data = getTable2( _v.myTemp + _v.slash+'printVarSimple.json' )
		data = dump
	printVarOld( data, sort_keys, prefix=prefix, remove=remove )

def printVarSimple2( data, sort_keys=False, isDic=None ):

	result = d2json( data, sort_keys )
	result = result.replace( '"', '' )
	result = result.replace( ',', '' )
	result = printVarColor_OLD( result )
	print_( result )


def printVarSimpleFake( data ):
	result = printVarColor_OLD( data )
	print_( result )
def printVarOld( data, sort_keys=False, prefix=None, remove=None ):
	result = d2json( data, sort_keys )
	# result = type( result )
	result = printVarColor_OLD( result )
	if not remove is None:
		for x in remove:
			result = result.replace(x,'')
	if prefix is None:
		print_( result )
	else:
		for x in result.split('\n'):
			print_( prefix+x )

def printVarSimplePostReplace( data, string, newString, sort_keys=False ):
	result = d2json( data, sort_keys )
	# result = type( result )
	result = printVarColor_OLD( result )
	result = result.replace( string, newString )
	print_( result )


def printVar2( data, sort_keys=False ):
	result = d2json( data, sort_keys )
	result = printVarColor_OLD( result )
	print_( result )


def printVarColor( data ):
	_code = regImp( __.appReg, '_rightThumb._auditCodeBase' )
	validator = _code.imp.Validator()

	# index = validator.createIndex( data, 'javascript' )
	# validator.colorPrint_old()
	# print_(data)
	index = validator.createIndex( data, 'javascript', skipLoad=True, simple=False, A=None, B=True, C=None )
	# printVarSimple(validator.identity)
	# index = validator.createIndex( data, 'javascript', simple=False, B=True )
	validator.colorPrint()
	
def printVarSimpleSTR(data):
	print_( printVarColor_OLD( data ) )

def hashtag_(code,i):
	tx=''
	for ii in range(2000):
		if not c == '\n' and i <= len(code):
			c=code[i]
			tx+=c
			res += c
			i+=1
		else:
			e()
			return {
						'i': i,
						'txt': pr(tx,c='white',p=0),
			}


def printVarColor_OLD( code ):
	result = ''
	i=-1
	for nothing in code:
		i+=1
		if i == len(code):
			return result;
		c=code[i]
		# if 0:
		if c == '#':
			dic=hashtag_(code,i)
			i=dic['i']
			result += dic['txt']
		elif c == "'":
			ii = vindex(code,i+1,n="'",v=0)
			txt=''
			txt+=Color.darkcyan+"'"+Color.end
			# txt+=inlineBold( '"', 'darkcyan' )
			txt+=inlineBold( code[i+1:ii], 'cyan' )
			txt+=Color.darkcyan+"'"+Color.end
			# print_(ii,c,)
			result += txt
			i = ii
		elif c == '"':
			ii = vindex(code,i+1,n='"',v=0)
			txt=''
			txt+=Color.darkcyan+'"'+Color.end
			# txt+=inlineBold( '"', 'darkcyan' )
			txt+=inlineBold( code[i+1:ii], 'cyan' )
			txt+=Color.darkcyan+'"'+Color.end
			# print_(ii,c,)
			result += txt
			i = ii
		else:
			result += printVarColorChar( c )

	return result


	# Gray = '\033[1;30;40m'
	# Red = '\033[1;31;40m'
	# Green = '\033[1;32;40m'
	# Yellow = '\033[1;33;40m'
	# Blue = '\033[1;34;40m'
	# Magenta = '\033[1;35;40m'
	# Cyan = '\033[1;36;40m'
	# White = '\033[1;37;40m'
	# END = '\033[0m'


# def inlineColor( string, color='RED' ):
#   color = color.upper()
#   if not type(string) == str:
#       string = str(string)
#   if color == 'RED':
#       return Color.RED + string + Color.END
#   elif color == 'CYAN':
#       return Color.CYAN + string + Color.END
#   elif color == 'DARKCYAN' or color == 'grey':
#       return Color.DARKCYAN + string + Color.END
#   elif color == 'BLUE':
#       return Color.BLUE + string + Color.END
#   elif color == 'GREEN':
#       return Color.GREEN + string + Color.END
#   elif color == 'YELLOW':
#       return Color.YELLOW + string + Color.END
#   elif color == 'UNDERLINE':
#       return Color.UNDERLINE + string + Color.END


def printVarColorChar( data ):


	what = '('
	color = 'Background.red'
	if data == what:
		return data.replace( what, colorThis( what, color, shouldPrint=False ) )

	what = ')'
	color = 'Background.red'
	if data == what:
		return data.replace( what, colorThis( what, color, shouldPrint=False ) )


	what = '{'
	color = 'green'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )
	
	what = '}'
	color = 'green'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )
	
	what = '['
	color = 'YELLOW'
	if data == what:
		return data.replace( what, inlineColor( what, color ) )

	what = ']'
	color = 'YELLOW'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = '"'
	color = 'white'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = "'"
	color = 'white'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = ':'
	color = 'red'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = ','
	color = 'Magenta'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = '='
	color = 'red'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	return data



def class2Dic( data ):
	saveTable2( data, _v.json_temp )
	txt = getTable2( _v.json_temp )
	return txt

""" {7DB6A001-0637-4F13-B328-2B17A481CF35}
def json2d( data, formatOnline=False ):
	saveText( data, _v.json_temp )
	dic = getTable2( _v.json_temp )
	if formatOnline:
		copyVar( dic )
		
		import webbrowser
		webbrowser.open('https://beautifier.io/', new=2)
	return dic
"""

myFileLocation_Print = True
myFileLocation_File = False
myFileLocation_Files = []
myFileLocation_Pipe = []
backup_subject_files = True

def myFileLocationsXYZ( file, silent=False, currentBaseVersion=3 ):
	global appData
	global myFileLocation_Files
	global myFileLocation_Pipe
	myFileLocationsABC( file, silent=silent, currentBaseVersion=currentBaseVersion )
	if not __.myFileLocations_SKIP_VALIDATION:
		if type(appData[__.appReg]['pipe']) == list:
			for i,f in enumerate(appData[__.appReg]['pipe']):
				appData[__.appReg]['pipe'][i] = __.path(f)
	for i,f in enumerate(myFileLocation_Files):
		myFileLocation_Files[i] = __.path(f)
	for i,f in enumerate(myFileLocation_Pipe):
		myFileLocation_Pipe[i] = __.path(f)
	if type(appData[__.appReg]['pipe']) == list and len(appData[__.appReg]['pipe']):
		# print_('here a')
		return appData[__.appReg]['pipe']
	else:
		# print_('here b')
		# print_(type(myFileLocation_Files[0]))
		if len(myFileLocation_Files):
			return myFileLocation_Files[0]
		else:
			return myFileLocation_Files

def myFileLocations_add_file(path):
	global appData
	global myFileLocation_Files
	if __.myFileLocations_SKIP_VALIDATION:
		if type( appData[__.appReg]['pipe'] ) == bool:
			appData[__.appReg]['pipe'] = []
		if isFirst:
			isFirst=False
		else:
			appData[__.appReg]['pipe'].append( path )
	if  not path in myFileLocation_Files:
		myFileLocation_Files.append( path )

def _mfl(file):
	if type(file) == str: file=file.replace(os.sep+os.sep,os.sep);
	if type(file) == list and len(file) and type(file[0]) == str:
		for i,f in enumerate(file):
			if type(f) == str: file[i]=file[i].replace(os.sep+os.sep,os.sep);
	return file

isFirst=True
def myFileLocations( file, silent=False, currentBaseVersion=3 ):
	if isWin and type(file) == str and '/' in file: file=file.replace('/',os.sep)
	if isWin and type(file) == str and file.startswith('~'): file=_v.home+file[1:]
	if __.isRequired_Pipe_or_File:
		return file
	# return file
	global appData
	global isFirst
	if '*' in file:
		__.trigger_isPipe = 'glob'
	if os.path.isfile(file):
		myFileLocations_add_file(file)

	# print_('here')
	try:
		__.myFileLocations_processed
	except Exception as e:
		__.myFileLocations_processed = False
	# print_('__.trigger_isPipe',__.trigger_isPipe)
	# print_(__.trigger_isPipe)
	# if 'glob' in __.trigger_isPipe:
	#     import glob
	#     g = glob.glob(file)
	#     print_('g',g,__.myFileLocations_processed)
	#     return g

	if not __.myFileLocations_processed and not type( __.trigger_isPipe ) == bool:
		__.myFileLocations_processed = True
		if 'glob' in __.trigger_isPipe:
			# cp('__.trigger_isPipe=glob','purple')
			appData[__.appReg]['pipe'] = ''
			# __.trigger_isPipe = False
			# glob = __.imp('glob')
			import glob
			g = glob.glob(file)
			for f in g:
				# f = __.path(f)
				# FX = getText( f, raw=True )
				# print_('_____________________')
				# print_(f,FX)
				# print_('_____________________')
				# sys.exit()
				# appData[__.appReg]['pipe'] += FX + '\n'
				myFileLocations( f, silent, currentBaseVersion )
			file = g
			# print_(g)
			# return g
			# appData[__.appReg]['pipe'] = appData[__.appReg]['pipe'].split('\n')
			# print_("appData[__.appReg]['pipe']",appData[__.appReg]['pipe'])
			return _mfl(file)
			try:
				return _mfl(f)
			except Exception as e:
				return _mfl(file)

	# print_(__.myFileLocations_SKIP_VALIDATION)
	# print_(os.path.isdir(file))
	# print_(file)
	# sys.exit()

	# print_( 'HERE HERE HERE HERE ', file )
	if '*' in file:
		import glob
		if not type(appData[__.appReg]['pipe']) == list: appData[__.appReg]['pipe']=[];
		for path in glob.glob(file):
			appData[__.appReg]['pipe'].append(path)
		return _mfl(appData[__.appReg]['pipe'])



	global myFileLocation_File
	global backup_subject_files
	if type(__.myFileLocations_SKIP_VALIDATION) == bool and __.myFileLocations_SKIP_VALIDATION:
		# print_('here')
		# sys.exit()
		if not type(appData[__.appReg]['pipe']) == list:
			appData[__.appReg]['pipe']=[]
			return _mfl(None)
		if isFirst:
			isFirst=False
		else:
			appData[__.appReg]['pipe'].append( file )
		return _mfl(None)
	# if ',' in file and not os.path.isfile( file ):
	#   nFiles = []
	#   for f in file.split(','):
	#       nFiles.append( myFileLocations2( f, silent, currentBaseVersion ) )
	#   file = ','.join( nFiles )
		
	# else:
	#   myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )

	myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )
	if  not myFileLocation_File in myFileLocation_Files:
		myFileLocation_Files.append( myFileLocation_File )
	try:
		autoAbbreviations()
	except Exception as e:
		pass
	if len( myFileLocation_Files ):
		# print_('xxx')
	# if len( myFileLocation_Files ) and type( appData[__.appReg]['pipe'] ) == bool:
		if not type( __.trigger_isPipe ) == bool:
			# print_( 'HERE', myFileLocation_Files )
			__.appRegPipe = __.appReg

			if 'name' in __.trigger_isPipe:
				justNames = True
			else:
				justNames = False

			tmpFiles = []
			hasFiles = False
			if justNames:
				# print_( 'HERE' )
				# setPipeData( myFileLocation_Files, __.appReg )

				if type( appData[__.appReg]['pipe'] ) == bool:
					appData[__.appReg]['pipe'] = []
				for thisFile in myFileLocation_Files:
					# if os.path.isfile( thisFile ):
					if not thisFile in myFileLocation_Pipe:
						myFileLocation_Pipe.append( thisFile )
						if isFirst:
							isFirst=False
						else:
							appData[__.appReg]['pipe'].append( thisFile )
			else:
				for thisFile in myFileLocation_Files:
					if os.path.isfile( thisFile ):
						hasFiles = True
						if not thisFile in myFileLocation_Pipe:
							myFileLocation_Pipe.append( thisFile )
							if type( appData[__.appReg]['pipe'] ) == bool:
								appData[__.appReg]['pipe'] = []
							if 'clean' in __.trigger_isPipe:
								for row in getText( thisFile, raw=True, clean=True ).split('\n'):
									if isFirst:
										isFirst=False
									else:
										appData[__.appReg]['pipe'].append( row )
									# tmpFiles.append( row )
							else:
								for row in getText( thisFile, raw=True ).split('\n'):
									if isFirst:
										isFirst=False
									else:
										if type(appData[__.appReg]['pipe']) == list:
											appData[__.appReg]['pipe'].append( row )
									# tmpFiles.append( row )
			# if hasFiles:
			#   if 'clean' in __.trigger_isPipe:
			#       setPipeData( tmpFiles, __.appReg, clean=True )
			#   else:
			#       setPipeData( tmpFiles, __.appReg, clean=False )
			if not hasFiles:
				if type( appData[__.appReg]['pipe'] ) == bool:
					appData[__.appReg]['pipe'] = []
					for row in myFileLocation_Files:
						if isFirst:
							isFirst=False
						else:
							appData[__.appReg]['pipe'].append( row )



	return _mfl(myFileLocation_File)
def myFileLocations2( file, silent=False, currentBaseVersion=3 ):
	if __.myFileLocations_SKIP_VALIDATION:
		return _mfl(file)
	# global myFileLocation_Print
	# silentSetTo = myFileLocation_Print
	silentSetTo = l.conf('myFileLocation_Print',d=False)
	if silent:
		silentSetTo = silent

	if os.path.isfile( file ):
		return _mfl(file)

	if 'tmpf' in file.lower():
		fx = file.lower()
		if 'tmpf' == fx:
			return _mfl(_v.tmpf)
		elif 'tmpf0' == fx:
			return _mfl(_v.tmpf0)
		elif 'tmpf1' == fx:
			return _mfl(_v.tmpf1)
		elif 'tmpf2' == fx:
			return _mfl(_v.tmpf2)
		elif 'tmpf3' == fx:
			return _mfl(_v.tmpf3)
		elif 'tmpf4' == fx:
			return _mfl(_v.tmpf4)
		elif 'tmpf5' == fx:
			return _mfl(_v.tmpf5)
		elif 'tmpf6' == fx:
			return _mfl(_v.tmpf6)
		elif 'tmpf7' == fx:
			return _mfl(_v.tmpf7)
		elif 'tmpf8' == fx:
			return _mfl(_v.tmpf8)
		elif 'tmpf9' == fx:
			return _mfl(_v.tmpf9)
		return _mfl(file)

	probableLocations = [
		"_v.py + _v.slash+'_rightThumb'+_v.slash + '_' + '*THEFILENAME*' + _v.slash+'__init__.py'",
		"_v.py + _v.slash+''+_v.slash + '*THEFILENAME*' + '.py'",
		"_v.py + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myTables + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'batch'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'batch'+_v.slash + '*THEFILENAME*' + '.bat'",
		"_v.myDatabases + _v.slash+''+_v.slash + '*THEFILENAME*'",

		"os.environ['USERPROFILE'] + _v.slash+'Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'Downloads'+_v.slash + '*THEFILENAME*'",

		"os.environ['HOME'] + _v.slash+'Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['HOME'] + _v.slash+'Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['HOME'] + _v.slash+'Downloads'+_v.slash + '*THEFILENAME*'",
		
		"_v.myTXT + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'exe'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'php'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'php'+_v.slash + '*THEFILENAME*' + '.php'",
		"_v.myApps + _v.slash+'powershell'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'vbs'+_v.slash + '*THEFILENAME*'",
	]

	if file == 'base':
		file = 'base' + str( currentBaseVersion )

	if True:
		for testThis in probableLocations:
			try:
				theTest = eval( testThis )
				# print_()
				# print_(theTest)
				theTest = theTest.replace( '*THEFILENAME*', file )
				# print_(os.path.isfile( theTest ),theTest)
				if os.path.isfile( theTest ):
					if silentSetTo:
						
						print_()
						print_( 'File not here but in:', theTest )
						print_()
					# print(theTest)
					# return theTest
					return _mfl(theTest)

			except Exception as e:
				pass
	
	if not os.path.isfile( _v.relevant_folders ) and __.isWin:
		print_( 'generateRelevantFolders' )
		import generateRelevantFolders
		generateRelevantFolders.action()

	if os.path.isfile( _v.relevant_folders ):
		for fld in getText( _v.relevant_folders, raw=True, clean=1 ).split('\n'):
			if os.path.isfile( fld  +_v.slash+  file ):
				return _mfl(fld  +_v.slash+  file)
			if 'ext' in __.specifications:
				if os.path.isfile( fld  +_v.slash+  file+ __.specifications['ext'] ):
					return _mfl(fld  +_v.slash+  file)
			# print_(fld)

	return _mfl(file)



def cleanList( data ):
	for i,d in enumerate(data):
		data[i] = data[i].replace( '\n', '' )
	return data

adminStatus = ''
def isAdmin():
	global adminStatus
	if type(adminStatus) == str:
		tempFile = _v.stmp + _v.slash + genUUID()
		do = 'echo %isAdmin%>'+tempFile
		test = os.system('"' + do + '"')
		isAdmin0 = getText(tempFile)
		isAdmin1 = isAdmin0[0].replace('\n','')
		os.remove(tempFile)
		if 'True' in isAdmin1:
			adminStatus = True
		else:
			adminStatus = False
	return adminStatus

def isN(data):
	if not type(data) == int: return data
	if type(data) == str:
		data=_str.do('trim',data)
	standard='.1234567890'
	if type(data) == int: return data
	if type(data) == float: return data
	if not type(data) == str: return None
	r=False
	for d in data:
		if not d in standard: return None
	if '.' in data: return float(data)
	return int(data)

def autoDate( theDate ):
	n=isN(theDate)
	if n: theDate=n

	if not theDate: return None
	# if type(theDate) == float or type(theDate) == int:
	#   return theDate
	import _rightThumb._date as _date
	return _date.autoDate( theDate )

def friendlyDate2( theDate ):
	fd = friendlyDate( theDate )
	if type(fd) == str and len(fd):
		fd = fd[:-3][2:]
		# if fd.startswith('21-'):
		#   fd = fd[3:]
	return fd

def friendlyDate( theDate ):
	import _rightThumb._date as _date
	return _date.friendlyDate( theDate )
def friendlyDateTouch( theDate ):
	import _rightThumb._date as _date
	return _date.friendlyDateTouch( theDate )

def resolveEpoch( theDate, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	return resolveEpochTest( theDate, test, showPrint, showPrintTry, onlyEpoch, delim, falseBlank )

def resolveEpochTest( theDate, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	import _rightThumb._date as _date
	return _date.resolveEpoch( theDate, test, showPrint, showPrintTry, onlyEpoch, delim, falseBlank )

def fileDate( theDate ):
	friendly = friendlyDate( theDate )
	friendly = friendly.replace( ' ', '_' )
	friendly = friendly.replace( ':', '-' )
	return friendly

def dateAdd2( theDate, addDays, delim='-' ):
	
	theDate = str( theDate )

	if not delim in theDate:
		try:
			float( theDate )
			theDate = resolveEpochTest( theDate, onlyEpoch='day', delim=delim )
			if type(theDate) == bool:
				print_( 'Error:', theDate )
				sys.exit()
		except Exception as e:
			printBold( 'Error: '+ theDate, 'red' )
			sys.exit()

	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 + datetime.timedelta(days=addDays)

def dateMathEpoch( epoch, theDays, do='+' ):
	# print_(epoch, theDays)
	epoch = autoDate(epoch)
	# if do == '+':
	#   return epoch + ( theDays*86400 )
	# elif do == '-':
	#   return epoch - ( theDays*86400 )


	date0 = datetime.datetime.fromtimestamp((epoch))
	if do == '+':
		date1 = date0 + datetime.timedelta(days=theDays)
	elif do == '-':
		date1 = date0 - datetime.timedelta(days=theDays)
	else:
		print_( "dateMathEpoch( epoch, theDays, do='+' )" )
		sys.exit()
	# print_(date1.timestamp())
	return autoDate((date1.timestamp()))


def txt2Date(text):
	# _.switches.trigger('Watched', _.txt2Date)

	try:
		if not type(text) == str:
			text = ''
	except Exception as e:
		text = ''

	if text == '':
		theDate = datetime.date.today()
		result = str( theDate ).split()[0]
	elif '-' in text:
		if text.count('-') == 2:
			try:
				textSplit = text.split('-')
				# print_(textSplit)
				theDate = datetime.datetime( int(textSplit[0]), int(textSplit[1]), int(textSplit[2]), 0, 0 )
				result = str( theDate ).split()[0]
			except Exception as e:
				printBold('Date error: using today\'s date','red')
				theDate = datetime.date.today()
				result = str( theDate ).split()[0]
		else:
			print_('Date error: using today\'s date')
			theDate = datetime.date.today()
			result = str( theDate ).split()[0]
	else:
		fnd = 'ymwd'
		do = text.lower().replace(' ','')
		nmb = do
		for t in fnd:
			nmb = nmb.replace(t,'')
		if len(nmb) == 0:
			nmb = 1
		try:
			nmb = int(nmb)
		except Exception as e:
			nmb = 1
		if 'y' in do:
			theDate = datetime.date.today() + datetime.timedelta(-365 * nmb)
		if 'm' in do:
			theDate = datetime.date.today() + datetime.timedelta(-30 * nmb)
		if 'w' in do:
			theDate = datetime.date.today() + datetime.timedelta(-7 * nmb)
		if 'd' in do:
			theDate = datetime.date.today() + datetime.timedelta(-1 * nmb)
		result = str( theDate ).split()[0]
	return result



## UUID ## START ############################################################################################################################


def uuidEpoc( uuid, f='iso' ):
	uuid = _str.do('an',uuid)
	if 'epoc' in uuid:
		d=int(uuid.split('epoc')[1][:10])
		return _.isDate( d, f=f)
	return None

def genUUID3(): return genUUID()[1:-1].replace('-','')
def genUUID2(): return genUUID()[1:-1]

def genUUID( project='', label='', uniqueTimestamp=False, note=None, r=None, e=None, n=None, c=False, epoch=None,    small=None, t=None, tiny=None, focus=None, save=None ):
	if focus is None: focus=__.appReg
	if not tiny is None: small=tiny;    #KEEP 1ST
	if not t is None: small=t;          #KEEP 2ND
	if small: return miniUUID();        #KEEP 3RD
	if not e is None: epoch=e;
	if not n is None:  note=n;
	if not r is None: small=None; end=r;

	if epoch:
		dec=2
		if type(epoch) == int and not epoch==1:
			dec=epoch

		ee=time.time()
		ea=str(ee).split('.')[0]
		eb=str(ee).split('.')[1]
		ec=str(ee).replace('.','d')
		ad=ea
		i=0
		while not i == dec:
			ad += eb[i]
			i+=1
		end=True
		note='epoc'+ad




	global appData
	global appInfo
	def rev(string):
		l=list(string)
		l.reverse()
		return ''.join(l)
	uuid = __.imp('uuid')
	string = uuid.uuid4()
	string = str(string)
	# return string
	ss=string
	if note:
		if end:
			r=1
		else:
			r=0
		ss=over(ss,note,r=r)
	if c:
		string = ss
	else:
		string = '{' + ss + '}'
	try:
		type(appData[focus]['uuid'])
		good = True
	except Exception as e:
		good = False
	if good:

		try:
			timestamp = appData[focus]['start']
		except Exception as e:
			timestamp = time.time()

		if not project == '' and not label == '':
			rec={}
			rec['app'] = appInfo[focus]['file']
			rec['uuid'] = string
			rec['timestamp'] = timestamp
			rec['project'] = ''
			rec['label'] = ''
			if uniqueTimestamp:
				rec['timestamp'] = time.time()

			if not project == '':
				rec['project'] = project

			if not label == '':
				rec['label'] = label
				
			uuidLog = getTable('uuid_log.json')
			uuidLog.append(rec)
			saveTable(uuidLog,'uuid_log.json',printThis=False)
			if not save is None and type(save) is str:
				index=_.getTable(save)
				index[string] = rec
				_.saveTable(index,save)


		if not project == '' or not label == '':

			if type(appData[focus]['uuid']) == str:
				# print_()
				# print_( 'focus', focus )
				# print_()
				# print_(d2json( appData ))
				# print_()
				appData[focus]['uuid'] = {}
				# print_(appInfo[focus]['file'])
				# sys.exit()
				appData[focus]['uuid']['app'] = appInfo[focus]['file']

			if not type(appData[focus]['uuid']) == str:
				
				appData[focus]['uuid']['uuid'] = string
				appData[focus]['uuid']['timestamp'] = timestamp
				appData[focus]['uuid']['project'] = ''
				appData[focus]['uuid']['label'] = ''

				if uniqueTimestamp:
					appData[focus]['uuid']['timestamp'] = time.time()

				if not project == '':
					appData[focus]['uuid']['project'] = project

				if not label == '':
					appData[focus]['uuid']['label'] = label
					
				uuidLog = getTable('uuid_log.json')
				uuidLog.append(appData[focus]['uuid'])
				saveTable(uuidLog,'uuid_log.json',printThis=False)
			# appData[focus]['uuid'] = { 'uuid': theID, 'timestamp': time.time(), 'project': theProject, 'app': 'guid' }
	return string


def miniUUID(epoch=None):
	u = genUUID()
	u = u.replace( '{','' ).replace( '-','' )
	result = '{' + u[:12] + '}'
	if epoch is None:
		return result
	else:
		return UUID_Epoch(result)


def UUID_Epoch(vVv,dec=2,epoch=None):

	if '{' in vVv:
		hasBr=True
	else:
		hasBr=False


	vVv=vVv.replace('{','').replace('}','')
	i=0
	indices=[]
	for c in vVv:
		if c == '-':
			indices.append(i)
		if not c == '-':
			i+=1
	vVv = _str.do('an',vVv)
	if epoch is None:
		e=time.time()
	else:
		e=epoch
	ea=str(e).split('.')[0]
	eb=str(e).split('.')[1]
	if len(eb) == 1:
		eb+='0'
	ec=str(e).replace('.','d')
	ad=ea
	if not dec is None:
		dec=int(dec)
	else:
		dec=2
	pre='epoc'
	if len(vVv) == 12 or len(vVv) == 14:
		from random import randrange
		dec=0
		pre=str(randrange(10))+'e'
	i=0
	while not i == dec:
		ad += eb[i]
		i+=1

	# vVv = _.over(vVv,   ea+'e'  )
	vVv = over(vVv,   pre+ad , r=1   )
	if indices:
		vVv = ddelim(vVv,d='-',indices=indices)
	if hasBr and not '{' in vVv:
		vVv = '{'+vVv+'}'

	return vVv



UUID=genUUID
guid=genUUID

UUIDm=miniUUID
UUIDM=miniUUID
MUUID=miniUUID
mUUID=miniUUID

UUIDE=UUID_Epoch
guidE=UUID_Epoch
uuidE=UUID_Epoch

UUIDe=uuidEpoc
uuide=uuidEpoc

## UUID ## END ############################################################################################################################


__.fn.saveText = False
def saveText( rows, theFile, errors=True, me=0, test=None ):
	# print_(rows)
	ty9=type(rows)
	if not test is None:
		__.fn.saveText = test
	test=0
	if __.fn.saveText:
		cp( [ 'saveText', __.appReg, type(rows), theFile ], 'cyan' )
	HD.chmod(theFile)
	# print_(type(rows))
	try:
		if type(rows) == bytes:
			rows = str(rows,'utf-8')
		f = open(theFile,'w', encoding='utf-8')
		# if type(rows) == str:

		# print_(type(rows))
		# f.write(str(rows))
		# rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
		# f.write(rows)
		# f.write(rows.encode("iso-8859-1", "replace"))

		# print_(type(rows))
		if type(rows) == str:
			# print_(rows)
			f.write(rows)
			if __.fn.saveText:
				print_(1111111,0)
		else:
			if __.fn.saveText:
				print_(1111111,1)
			# if ty9 == str:
			#     f.write(str(rows))
			# elif ty9 == list:
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						f.write(str(row) + '\n')
				else:
					f.write(str(row) + '\n')
		f.close()
		
			
	except Exception as e:
		if type(rows) == list:
			result = ''
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						result += str(row) + '\n'
				else:
					result += str(row) + '\n'

			rows = result
		try:
			open(theFile, 'wb').write(rows)
			if __.fn.saveText:
				print_(2222222)
		except Exception as e:
			try:
				open(theFile, 'w').write(rows)
				if __.fn.saveText:
					print_(3333333)
			except Exception as e:
				new_text = ''
				for x in rows:
					if x in _str.printable:
						new_text+=x
				

				# --> start#> encoding fix
				# -->  date#>  2022-07-21
				# --> url#> https://stackoverflow.com/questions/1728376/get-a-list-of-all-the-encodings-python-can-encode-to
				encoding_list = ["ascii", "big5", "big5hkscs", "cp037", "cp273", "cp424", "cp437", "cp500", "cp720", "cp737", "cp775", "cp850", "cp852", "cp855", "cp856", "cp857", "cp858", "cp860", "cp861", "cp862", "cp863", "cp864", "cp865", "cp866", "cp869", "cp874", "cp875", "cp932", "cp949", "cp950", "cp1006", "cp1026", "cp1125", "cp1140", "cp1250", "cp1251", "cp1252", "cp1253", "cp1254", "cp1255", "cp1256", "cp1257", "cp1258", "cp65001", "euc_jp", "euc_jis_2004", "euc_jisx0213", "euc_kr", "gb2312", "gbk", "gb18030", "hz", "iso2022_jp", "iso2022_jp_1", "iso2022_jp_2", "iso2022_jp_2004", "iso2022_jp_3", "iso2022_jp_ext", "iso2022_kr", "latin_1", "iso8859_2", "iso8859_3", "iso8859_4", "iso8859_5", "iso8859_6", "iso8859_7", "iso8859_8", "iso8859_9", "iso8859_10", "iso8859_11", "iso8859_13", "iso8859_14", "iso8859_15", "iso8859_16", "johab", "koi8_r", "koi8_t", "koi8_u", "kz1048", "mac_cyrillic", "mac_greek", "mac_iceland", "mac_latin2", "mac_roman", "mac_turkish", "ptcp154", "shift_jis", "shift_jis_2004", "shift_jisx0213", "utf_32", "utf_32_be", "utf_32_le", "utf_16", "utf_16_be", "utf_16_le", "utf_7", "utf_8", "utf_8_sig"]

				try:
					open(theFile, 'w', encoding='utf-8').write(new_text)
				except Exception as e:
					for i_enc in encoding_list:
						try:
							open(theFile, 'w', encoding=i_enc).write(new_text)
						except Exception as e: pass
				# -->   end#> encoding fix
				
				if __.fn.saveText:
					print_(4444444)
		HD.chmod(theFile)
		# if errors:
		#   print_( 'Auto correction when saving text' )
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );

def getText( theFile, raw=False, clean=False,  e=0, c=0 ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	HD.chmod(theFile)
	lines = None
	if os.path.isfile(theFile):
		try:
			f = open(theFile, 'r', encoding='utf-8')
			lines = f.readlines()
			f.close()
		except Exception as e:
			try:
				f = open(theFile, 'r', encoding='latin-1')
				lines = f.readlines()
				f.close()
			except Exception as e:
				f = open(theFile, 'r')
				lines = f.readlines()
				f.close()
	else:
		if not e:
			return None
		print_('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( _v.slash+'n', '\n' )

		if clean:
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		return txt
	elif c > 0:
		if c > 1:
			txt = ''.join( lines )
			TXT = ''
			txt = txt.replace( "'\"\"\"'", '' )
			if '"""' in txt:
				for i,item in enumerate(txt.split('"""')):
					if i % 2 == 0:
						TXT+=item
			elif not '"""' in txt:
				TXT = txt
			while '    ' in TXT:
				TXT = TXT.replace( '    ', '\t' )
			while ' (' in TXT:
				TXT = TXT.replace( ' (', '(' )
			while ' =' in TXT:
				TXT = TXT.replace( ' =', '=' )
			while '= ' in TXT:
				TXT = TXT.replace( '= ', '=' )
			while 'def  ' in TXT:
				TXT = TXT.replace( 'def  ', 'def ' )
			while 'class  ' in TXT:
				TXT = TXT.replace( 'class  ', 'class ' )
			lines = TXT.split('\n')

		newLines = []
		for i,row in enumerate(lines):
			# row = row.replace('\n','')
			row = row.replace('\r','')
			
			if not c > 1:
				newLines.append(row)
			else:
				row = row.split('#')[0]
				test = row
				# while test.startswith(' ') or test.startswith('\t'):
				#   test = _str.cleanBE( test, ' ' )
				#   test = _str.cleanBE( test, '\t' )
				if not test.startswith('#') and len(test):
					newLines.append(row)


			


		return newLines

	elif clean:
		# lines = _str.replaceDuplicate( lines, '\n' )
		# lines = _str.cleanBE( lines, '\n' )
		for i,row in enumerate(lines):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			if type(clean) == int:
				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )
			if clean == 3:
				row = ' ' + row + ' '

			# print_( row )
			lines[i] = row
		return lines
	else:
		return lines

def getSize(fileobject):
	try:
		fileobject.seek(0,2) # move the cursor to the end of the file
		size = fileobject.tell()
		return size
	except Exception as e:
		try:
			return get_size( fileobject )
		except Exception as e:
			return None

# def formatSize(size):
#   result = ''
#   if size == None:
#       result = ''
#   elif size < 1024:
#       result = str(size) + ' B'
#   elif size > 1024 and size < 1048576:
#       num = round(size / 1024, 2)
#       result = str(num) + ' KB'
#   elif size > 1048576 and size < 1073741824:
#       num = round(size / 1048576, 2)
#       result = str(num) + ' MB'
#   elif size > 1073741824 and size < 137438953472:
#       num = round(size / 1073741824, 2)
#       result = str(num) + ' GB'
#   # if size < 1:
#   #   result = ''
#   return result

def monthByNumber(month):
	result = ''
	if str(month) == '01':
		result = 'Jan'
	if str(month) == '02':
		result = 'Feb'
	if str(month) == '03':
		result = 'Mar'
	if str(month) == '04':
		result = 'Apr'
	if str(month) == '05':
		result = 'May'
	if str(month) == '06':
		result = 'Jun'
	if str(month) == '07':
		result = 'Jul'
	if str(month) == '08':
		result = 'Aug'
	if str(month) == '09':
		result = 'Sep'
	if str(month) == '10':
		result = 'Oct'
	if str(month) == '11':
		result = 'Nov'
	if str(month) == '12':
		result = 'Dec'
	return result

def weeks_between(start_date, end_date):
	import math
	start_date = datetime.date(int(formatDateYear(start_date)),int(formatDateMonth(start_date)),int(formatDateDay(start_date)))
	start_date_monday = (start_date - datetime.timedelta(days=start_date.weekday()))
	end_date = datetime.date(int(formatDateYear(end_date)),int(formatDateMonth(end_date)),int(formatDateDay(end_date)))
	num_of_weeks = math.ceil((end_date - start_date_monday).days / 7.0)
	return num_of_weeks - 1
def months_between(start_date, end_date):
	# start_date = int(start_date)
	# end_date = int(end_date)
	# st = str(formatDateYear(start_date)) + '-' + str(formatDateMonth(start_date)) + '-' +  str(formatDateDay(start_date)) 
	# en = str(formatDateYear(end_date)) + '-' + str(formatDateMonth(end_date)) + '-' +  str(formatDateDay(end_date))
	start = datetime.date(int(formatDateYear(start_date)), int(formatDateMonth(start_date)), int(formatDateDay(start_date)) )
	end = datetime.date(int(formatDateYear(end_date)), int(formatDateMonth(end_date)), int(formatDateDay(end_date)) )
	months = calculate_monthdelta(start, end)
	return months
""" {7DB6A001-0637-4F13-B328-2B17A481CF35}
def calculate_monthdelta(date1, date2):
	import calendar
	def is_last_day_of_the_month(date):
		days_in_month = calendar.monthrange(date.year, date.month)[1]
		return date.day == days_in_month
	imaginary_day_2 = 31 if is_last_day_of_the_month(date2) else date2.day
	monthdelta = (
		(date2.month - date1.month) +
		(date2.year - date1.year) * 12 +
		(-1 if date1.day > imaginary_day_2 else 0)
		)
	# print monthdelta
	return monthdelta
"""

# def timeout(start,t):

#     # os._exit(0)
#     # print_('loop')
#     global completed
#     global killTime
#     global timeoutKill
#     ts = dt.now()

#     if start == 'start':
#         timeoutKill = False
#         completed = False
#         killTime = ts + timedelta(seconds=int(t))

#     if completed == False and ts < killTime:
#         x = Timer(0.0, timeout, ('loop',t))
#         x.start()
#     elif completed == False:
#         timeoutKill = True
#         completed = True
#         print_('\n*** Timeout ***()')
#         # os._exit(0)

# def processTimeout():
#     global switches
#     global defaultTimeout
#     if switches.isActive('Timeout') == True:
#         try:
#             defaultTimeout = int(switches.value('Timeout'))
#         except Exception as e:
#             errors.append({'id': 18, 'function': 'parent', 'cnt': 1, 'location': "defaultTimeout = int(switches.value('Timeout'))", 'vars': [{'name': 'timeout', 'value': switches.value('Timeout')}], 'error': e})
#             printBold('Error:','red')
#             print_('\tBad timeout value.')
#             os._exit(0)

#     # print_(defaultTimeout)
#     x = Timer(0.0, timeout, ('start',defaultTimeout))
#     x.start()


def showLine( string, plus = '', minus = '',plusOr = False, end=None,isSub=False, OR=None, code=False ):
	'''( string, plus='', minus='', plusOr=False, end=None, isSub=False, OR=None )'''
	# print_(plus)
	# print_(string)
	global switches
	# print_(switches.isActive('Plus'))
	# print_(switches.values('Plus'))
	# sys.exit()
	if plus is None :
		result = True
	else:
		if switches.isActive('Plus') or code or not plus == '':
			# print('asdf',plus);sys.exit();
			if switches.isActive('PlusCode'):
				result = positiveResultsCode(string,plus,plusOr,end,OR=OR)
			else:
				result = positiveResults(string,plus,plusOr,end,OR=OR)
			if not result and switches.isActive('PlusClose'):
				result = closeResults( string )

			if result and not isSub and switches.isActive('Plus-Sub'):
				result = False
				for xXx in switches.values('Plus-Sub'):
					if xXx.lower() in string.lower():
						result = True
						break


		else:
			result = True
	if result == True and  (switches.isActive('Minus') or not minus == ''):
		result = minusResults(string,minus)
	# print_(result)
	return result
def closeResults( string ):
	global switches
	global plusClose
	
	if len( switches.value('PlusClose') ):
		try:
			plusClose = float( switches.value('PlusClose') )
		except Exception as e:
			pass

	test = patternDiff( string, switches.value('Plus') )
	# print_( int(test), string, switches.value('Plus') )
	if test >= plusClose:
		# print_( test, string )
		return True
	else:
		return False




def positiveResultsCode(string,plus='',plusOr=False,end=None,OR=None):

	# __.sw.PlusCode

	global switches
	if plusOr or switches.isActive('PlusOr'):
		plusOr = True
	
	if not OR is None:
		plusOr=OR
	if not plus == '':
		plusInput = plus
	else:
		plusInput = switches.values('Plus').copy()


	if type( plusInput ) == list:
		for i,yh in enumerate(plusInput):
			plusInput[i]= ci(plusInput[i])
	# -->   #end> this was added 2022-07-20
	if not end is None:
		if type( plusInput ) == str:
			plusInput += end
		else:
			for i,yh in enumerate(plusInput):
				plusInput[i] += end
	
	pi = []
	for x in plusInput:
		pi.append( ci(x) )
	plusInput = pi
	del pi
	if type( plusInput ) == str:
		plusList = [plusInput]
	else:
		plusList = plusInput
	length = len(plusList)

	if length == 1 and not plusList[0] in string: return False
	elif length == 2:
		if not plusList[0] in string: return False
		if not plusList[1] in string: return False
	elif length == 3:
		if not plusList[0] in string: return False
		if not plusList[1] in string: return False
		if not plusList[3] in string: return False

	cnt = 0
	result = False
	noBreak='[]()_01`23456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"'+"'" + ''.join(plusList)
	stringN=' '
	xstringx=string
	for vgo in string:
		if vgo in noBreak: stringN+=vgo
		else: stringN+=' '
	stringN+=' '
	# string=stringN


	for s in plusList:
		sN=' '+s+' '
		if '=' in __.sw.PlusCode:
			if string == s:
				cnt += 1
		# elif len(s) > 1 and s[0] == '*':
		elif '*x' in __.sw.PlusCode:
			if string.endswith(s):
				cnt += 1
		# elif len(s) > 1 and s[-1] == '*':
		elif 'x*' in __.sw.PlusCode:
			if string.startswith(s):
				cnt += 1
		else:
			# if s in string: cnt += 1
			if sN in stringN: cnt += 1
		# if 'opus' in string:
		#   print_(cnt, string)
		if length == cnt:
			result = True
			break
		if plusOr:
			if cnt > 0:
				result = True
	# print(cnt)
	return result

















def positiveResults(string,plus='',plusOr=False,end=None,OR=None):
	global switches
	# print('here')
	if plusOr or switches.isActive('PlusOr'):
		plusOr = True
	
	if not OR is None:
		plusOr=OR
	if not plus == '':
		plusInput = plus
	else:
		plusInput = switches.values('Plus').copy()
	# --> #start> this was added 2022-07-20
	if type( plusInput ) == list:
		for i,yh in enumerate(plusInput):
			plusInput[i]= ci(plusInput[i])
	# -->   #end> this was added 2022-07-20
	if not end is None:
		if type( plusInput ) == str:
			plusInput += end
		else:
			for i,yh in enumerate(plusInput):
				plusInput[i] += end
	
	pi = []
	for x in plusInput:
		pi.append( ci(x) )
	plusInput = pi
	del pi
	if type( plusInput ) == str:
		if not switches.isActive('StrictCase'):
			plusInput = plusInput.lower()
		plusList = plusInput.split(',')
	else:
		for i,row in enumerate(plusInput):
			if not switches.isActive('StrictCase'):
				plusInput[i] = plusInput[i].lower()
		plusList = plusInput
	length = len(plusList)
	cnt = 0
	result = False
	if not switches.isActive('StrictCase'):
		string = string.lower()
	# print_( plusList )
	# sys.exit()
	for s in plusList:
		if not switches.isActive('StrictCase'):
			s = s.lower()
		# print(':s:',s)
		
		if len(s) > 1 and s[0] == '!':
			s=s[1:]
			if string == s:
				cnt += 1
		elif len(s) > 1 and s[0] == '*':
			s = s.replace('*','')
			if string.endswith(s):
				cnt += 1
		elif len(s) > 1 and s[-1] == '*':
			s = s.replace('*','')
			if string.startswith(s):
				cnt += 1
		elif not switches.isActive('PlusDuplicate') and (  not string.find(ci(s)) == -1 or s in string  ):
			cnt += 1
		elif switches.isActive('PlusDuplicate') and (  string.count(ci(s)) > 1 or string.count(s) > 1 ):
			cnt += 1
		# if 'opus' in string:
		#   print_(cnt, string)
		if length == cnt:
			result = True
			break
		if plusOr:
			if cnt > 0:
				result = True
	# if result:
	#     print_(string,plus)
	return result

def minusResults(string,minus=''):
	global switches
	if not switches.isActive('StrictCase'):
		string = string.lower()
	result = True
	if not minus == '':
		minusInput = minus
	else:
		minusInput = switches.values('Minus')

	# 23-01-04
	string=string.strip() #:    //*   #* 
	if minusInput and '*' in minusInput[0]:
		mi = minusInput[0].replace('*','')
		if minusInput[0].endswith('*'):
			if string.startswith(mi): return False
		if minusInput[0].startswith('*'):
			if string.endswith(mi): return False


	# --> #start> this was added 2022-07-20
	if type( minusInput ) == list:

		#b)--> slow
		# _minusInput=[]
		# for i,yh in enumerate(minusInput):
		# 	if not switches.isActive('StrictCase'):
		# 		_yh=ci(yh).lower()
		# 	else:
		# 		_yh=ci(yh)
		# 	_minusInput.append( _yh )
		# 	# minusInput[i]= ci(minusInput[i])
		# minusInput=_minusInput.copy()
		# del _minusInput
		#e)--> slow

		for i,yh in enumerate(minusInput):
			if not switches.isActive('StrictCase'):
				minusInput[i]= ci(minusInput[i]).lower()
			else:
				minusInput[i]= ci(minusInput[i])
	# -->   #end> this was added 2022-07-20
	if type( minusInput ) == str:
		if not switches.isActive('StrictCase'):
			minusInput = minusInput.lower()
		else:
			minusInput = minusInput
		minusList = minusInput.split(',')
	else:
		for i,row in enumerate(minusInput):
			if not switches.isActive('StrictCase'):
				minusInput[i] = minusInput[i].lower()

		minusList = minusInput

	try:
		for s in minusList:
			if not switches.isActive('StrictCase'):
				s = s.lower()
			if len(s) > 1 and s[0] == '!':
				s=s[1:]
				if string == s:
					result = False
					break
			elif len(s) > 1 and s[0] == '*':
				s = s.replace('*','')
				if string.endswith(s):
					result = False
					break
			elif len(s) > 1 and s[-1] == '*':
				s = s.replace('*','')
				if string.startswith(s):
					result = False
					break
			if not string.find(ci(s)) == -1 or s in string:
				result = False
				break
	except Exception as e:
		pass
	return result

def saveLog( logname, rows=[], focus=True, printThis=True ):
	simplejson = __.imp('simplejson')
	global appInfo
	global appData
	
	indentCode = True
	log = 'app_audit_log_TIMESTAMP__FILENAME__LOGNAME__INSTANCE.json'

	if type(focus) == bool:
		focus = __.appReg
		
	if not len(rows) and logname == 'threads':
		global threads
		rows = threads.log()
		# print_( rows )
		# sys.exit()
	if not len(rows) and logname == 'audit':
		for ad in __.structure():
			if len(appData[ad]['audit']) > 0:
				rows.append( { 'app': appInfo[ad]['file'], 'focus': ad, 'records': appData[ad]['audit'] } )
	try:
		if len(appInfo[focus]['instance']) > 0:
			log = log.replace('INSTANCE',appInfo[focus]['instance'])
		else:
			log = log.replace('__INSTANCE','')
	except Exception as e:
		log = log.replace('__INSTANCE','')
	
	log = log.replace('TIMESTAMP',str(appData[focus]['start']))
	log = log.replace('FILENAME',appInfo[focus]['file'])
	log = log.replace('LOGNAME',logname)
	
	file0 = _v.myTables + _v.slash+'applogs'+_v.slash + log

	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=True, default=str)
	else:
		dataDump = simplejson.dumps(rows, sort_keys=False, default=str)
	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(file0)
	if printThis:
		print_('Saved: ' + file0)

def saveTable( rows, theFile, tableTemp=False, printThis=True, indentCode=True, sort_keys=False, archive=False,                k=0,s=0,tmp=None,here=None,h=None,    p=1, me=0   ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')
	if not h is None: here = True;
	if not here is None: saveTable2( rows, theFile ); return None;
	if not tmp is None: tableTemp = True;
	if k or s: sort_keys = True;
	if not p: printThis = False;
		

	   


	# defaults to myTables
	px = ''
	if theFile.startswith('temp'+_v.slash):
		theFile = theFile.replace( 'temp'+_v.slash, '' )
		file0 = _v.stmp + _v.slash + theFile
		px = file0
	else:
		if not tableTemp:
			file0 = _v.myTables + _v.slash + theFile
			px = theFile
		else:
			file0 = _v.stmp + _v.slash + theFile
			px = file0

	if __.print_path:
		print_(file0)
	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
	else:
		dataDump = simplejson.dumps(rows, sort_keys=False, default=str)
	
	if archive:
		import _rightThumb._md5 as _md5

		theFileLabel = theFile
		if _v.slash in theFileLabel:
			global appInfo
			tfl = theFileLabel.split(_v.slash)
			tfl.reverse()
			theFileLabel = str(appInfo[__.appReg]['liveAppName']) + '__' + tfl[0]
		theFileLabel = theFileLabel.replace( '.json', '' )
		theFileLabel = theFileLabel.replace( '.JSON', '' )

		lastMD5 = None
		if os.path.isfile( file0 ):
			lastMD5 = _md5.md5File( file0 )

			backupFile = _v.stmp + _v.slash+'__archive_temp__' + theFileLabel + '__' + genUUID() + '.json'
			

	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(theFile)

	if archive:
		shouldDocument = False

		if os.path.isfile( file0 ):
			thisMD5 = _md5.md5File( file0 )
		if lastMD5 is None:
			shouldDocument = True
		else:
			if not lastMD5 == thisMD5:
				shouldDocument = True

		if not shouldDocument:
			if os.path.isfile( backupFile ):
				os.remove( backupFile )
		
		if shouldDocument:
			md5Table = getTable( 'table_archive_log.json' )
			found = False
			for i,record in enumerate(md5Table):
				if theFileLabel == record['name']:
					found = True

			theFileLabel
			theFile
			fileDate( theData )


	if printThis:
		printBold('Saved: ' + px, 'blue')
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );
	return file0


def getTable( theFile, tableTemp=False,      isDic=None, isList=None,      tmp=None ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	# defaults to myTables
	if not type( tableTemp ) == bool:
		if tableTemp == 'split':
			file0 = _v.myTables + _v.slash+'tablesets'+_v.slash + theFile
	else:
		if tableTemp == True:
			file0 = _v.stmp + _v.slash + theFile
		else:
			file0 = _v.myTables + _v.slash + theFile


	if not os.path.isfile(file0):
		file0 = theFile
	if os.path.isfile(file0):
		# print_( 'theFile', theFile )
		# print_( 'file0', file0 )
		# import bigjson
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
		return json_data
		# with open( file0, 'rb' ) as f:
			# json_data = bigjson.load(f)
			# json_data = bigjson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
	else:
		return __.data_default(file=theFile,default=[]).default()

def getTable3(theFile):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	if os.path.isfile(theFile) == True:
		with open(theFile,'r') as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	return __.data_default(file=theFile,default=[]).default()

def getTable2( theFile,     isDic=None, isList=None ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
		isDic = True
	if os.path.isfile(theFile):
		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()

def getTableBIG( theFile,     isDic=None, isList=None ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	import pandas as pd
	if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
		isDic = True
	if os.path.isfile(theFile):
		# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
		df = pd.read_json(theFile)
		try:
			json_data = df.to_dict('series')
		except Exception as e:
			try:
				json_data = df.to_dict('records')
			except Exception as ee:
				raise ee

		# with open(theFile) as f:
		#   json_data = pd.DataFrame(simplejson.loads(line) for line in f)

		# with open(theFile,'r', encoding="latin-1") as json_file:
		#   json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()

_tar = None
def getTableDB( theFile,     isDic=None, isList=None ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	theFile = _v.dbTables + _v.slash + theFile
	# print(theFile)
	if os.path.isfile(theFile):
		if isTar.bz2(theFile) or isTar.gz(theFile):
			global _tar
			if _tar is None:
				import _rightThumb._tar as _tar
				_tar.unzip( theFile )


		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()


def getTableProject( project, theFile,     isDic=None, isList=None, path=False ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	theFile = _v.projectData(project) + theFile
	if path:
		print_(theFile)
		return None
	# print_(theFile)
	# print_(theFile)
	# print_(theFile)
	# print_(theFile)
	if os.path.isfile(theFile) == True:
		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()


def saveTableProject( project, rows=[], theFile='', printThis=False, sort_keys=False, indentCode=True,  p=None, me=0, path=False ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')
	# print_('*******************',theFile)
	theFile = _v.projectData(project) + theFile
	if __.print_path:
		print_(theFile)
	if path:
		print_(theFile)
		return None
	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
	else:
		dataDump = simplejson.dumps(rows, sort_keys=False, default=str)

	# dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(theFile)
	if printThis:
		print_('Saved: ' + theFile)
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );

def saveTableDB( rows, theFile, printThis=False, sort_keys=False, indentCode=True,  p=None, me=0 ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')

	# print_('*******************',theFile)
	theFile = _v.dbTables + _v.slash + theFile
	if __.print_path:
		print_(theFile)
	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
	else:
		dataDump = simplejson.dumps(rows, sort_keys=False, default=str)

	# dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(theFile)
	if printThis:
		print_('Saved: ' + theFile)
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );


def saveTable2( rows, theFile, printThis=False, sort_keys=False, indentCode=True, p=None, me=0 ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')
	if not p is None:
		printThis = p
	# print_('*******************',theFile)
	if theFile.startswith('temp'+_v.slash):
		theFile = theFile.replace( 'temp'+_v.slash, '' )
		theFile = _v.stmp + _v.slash + theFile

	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
	else:
		dataDump = simplejson.dumps(rows, sort_keys=False, default=str)

	# dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(theFile)
	if printThis:
		print_('Saved: ' + theFile)
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );

def saveTable3( rows, theFile, printThis=False, me=0 ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')
	# print_('*******************',theFile)
	dataDump = simplejson.dumps(rows, sort_keys=False, default=str)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(theFile)
	if printThis:
		print_('Saved: ' + theFile)
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );


def tempFile(rows,theFile):
	file0 = _v.stmp + _v.slash + theFile
	file = open(file0,'w')
	for r in rows:
		if not '\n' in r:
			file.write(r+'\n')
		else:
			file.write(r)
	file.close()

def stamp2Date(ts):
	# print_(ts)
	# print_(datetime.datetime.fromtimestamp(int(ts) / 1e3))
	return datetime.datetime.fromtimestamp(int(ts) / 1e3)
def float2Date(ts):
	import _rightThumb._date as _date
	auto = _date.autoDate( ts )
	if type(ts) == str:
		ts = ts.replace('_','.')
		if '.' in ts:
			ts = float(ts)
		else:
			ts = int(ts)
		# print_(type(ts))
		# print_( stamp2Date(ts) )
	return stamp2Date(ts)
def float2Date2(ts):
	if type(ts) == str:
		ts = ts.replace('_','.')
		if '.' in ts:
			ts = float(ts)
		else:
			ts = int(ts)
		# print_(type(ts))
	return str(datetime.datetime.fromtimestamp(ts)).split('.')[0]
	# return str(datetime.datetime.fromtimestamp(ts / 1e3))
	# return str(ts)
	# return str(datetime.datetime.fromtimestamp(ts)).split('.')[0] + '\t' + str(ts)
	# return str(ts).split('.')[0] + '\t' + str(datetime.datetime.fromtimestamp(ts)).split('.')[0]
def float2Date3(ts):
	return str(datetime.datetime.fromtimestamp(float(ts)).strftime('%Y-%m-%d %H:%M:%S'))
def float2Date3B(ts,isJson = True):
	stmp = float2Date3(ts)
	dtx = stmp.split(' ')[0]
	preResult = {'year': dtx.split('-')[0],'month': dtx.split('-')[1],'day': dtx.split('-')[2]}
	if isJson:
		result = preResult
	else:
		result = str(preResult['year']) + '-' + str(preResult['month']) + '-' + str(preResult['day'])

	return result

def expireCheck(theDate,delim):
	now = datetime.datetime.now()
	today = now.strftime("%Y-%m-%d")
	fdtl = theDate.split(delim)
	foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	td = str(today).split('-')
	tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
	diff = tdd - foundDate
	return int(diff.days)

def dateDiff( theDate0, theDate1, delim='-' ):
	theDate0 = str(theDate0)
	theDate1 = str(theDate1)


	if not delim in theDate0:
		try:
			theDate0 = resolveEpochTest( theDate0, onlyEpoch='day', delim=delim )
			if type(theDate0) == bool:
				printBold( 'Error: _.dateDiff '+ str(theDate0), 'red' )
				sys.exit()
		except Exception as e:
			printBold( 'Error: _.dateDiff '+ str(theDate0), 'red' )
			sys.exit()


	if not delim in theDate1:
		try:
			theDate1 = resolveEpochTest( theDate1, onlyEpoch='day', delim=delim )
			if type(theDate1) == bool:
				printBold( 'Error: _.dateDiff '+ str(theDate1), 'red' )
				sys.exit()
		except Exception as e:
			printBold( 'Error: _.dateDiff '+ str(theDate1), 'red' )
			sys.exit()

	# print_(theDate0,theDate1,delim)
	# sys.exit()
	fdtl0 = theDate0.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))

	fdtl1 = theDate1.split(delim)
	date1 = datetime.date(int(fdtl1[0]), int(fdtl1[1]), int(fdtl1[2]))

	diff = date1 - date0
	return (int(diff.days))
	
def dateDiffX( theDate0, theDate1, delim='-' ):
	theDate0 = str(theDate0)
	theDate1 = str(theDate1)


	if not delim in theDate0:
		theDate0 = resolveEpochTest( theDate0, onlyEpoch='day', delim=delim )



	if not delim in theDate1:
		theDate1 = resolveEpochTest( theDate1, onlyEpoch='day', delim=delim )



	# print_(theDate0,theDate1,delim)
	# sys.exit()
	fdtl0 = theDate0.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))

	fdtl1 = theDate1.split(delim)
	date1 = datetime.date(int(fdtl1[0]), int(fdtl1[1]), int(fdtl1[2]))

	diff = date1 - date0
	return (int(diff.days))

def dateAdd(theDate,delim,addDays):
	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 + datetime.timedelta(days=addDays)

def dateSub(theDate,delim,addDays):
	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 - datetime.timedelta(days=addDays)

def listAverage(theList):
	total = 0
	for item in theList:
		total += item
	try:
		result =  total / len(theList)
	except Exception as e:
		result = 0
	return result 
def date2epoch(theDate,delim='-'):
	theDate = str(theDate)
	if len( theDate ) == 0:
		return ''
	theDate = theDate.replace(delim,'-')
	fdtl = theDate.split(' ')[0].split('-')
	if ':' in theDate:
		theDate = theDate.replace('.',':')
		if theDate.count(':') == 2:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M:%S')
		elif theDate.count(':') == 1:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M')
		elif theDate.count(':') == 3:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M:%S:%f')
		else:
			print_('Error: date2epoch')
			sys.exit()

	else:
		stmp = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	# stmp = datetime.datetime.strptime(theDate, '%Y-%m-%d')
	return float(time.mktime(stmp.timetuple()))

def validateEmail(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip(data)
	good = True
	# if not '@' in data:
	if not data.count('@') == 1:
		good = False
	if good:
		if not '.' in data.split('@')[1]:
			good = False
	# if data.count('@') == 1:
	if not good and len(data) > 0:
		data = ' ___________ * BAD * ___________'
	return data

def figureOutDate(theDate, theFormat):
	theFormat = str(theFormat)
	theFormat = _str.replaceDuplicate(theFormat,' ')
	theFormat = _str.cleanBE(theFormat,' ')
	theFormat = theFormat.lower()

	theFormatExp = 'dmy'
	if not len(theFormat) == 3:
		print_('format error, expected: dmy, ymd')
		sys.exit()
	if theFormat[0] in theFormatExp and theFormat[1] in theFormatExp and theFormat[2] in theFormatExp:
		pass
	else:
		print_('format error, expected: dmy, ymd')
		sys.exit()
	# theFormat = 'dmy'
	theDate = str(theDate)
	theDate = _str.replaceDuplicate(theDate,' ')
	theDate = _str.cleanBE(theDate,' ')

	
	n = '0123456789'
	a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
	autoDelim = ''
	for d in theDate:
		if d in n:
			pass
		elif d in a:
			pass
		else:
			autoDelim = d
			break

	theDateDe = theDate.split(autoDelim)
	info = {}

	info[theFormat[0]] = theDateDe[0]
	info[theFormat[1]] = theDateDe[1]
	info[theFormat[2]] = theDateDe[2]
	if info['m'][0] in a:
		m = info['m']
		m = m.lower()
		found = False
		for monththeDate in getMonthData():
			# print_(monththeDate)
			# sys.exit()
			full = monththeDate['month']
			abbrev = monththeDate['abbrev']
			mNumber = monththeDate['number']
			full = full.lower()
			abbrev = abbrev.lower()
			if m == full or m == abbrev:
				found = True
				info['m'] = mNumber
		if not found:
			ans = input('What Month? ')
			if len(ans) == 0:
				print_('Month error')
				sys.exit()
			try:
				int(ans)
			except Exception as e:
				printBold('Month error','red')
				sys.exit()
			if len(ans) == 1:
				 info['m'] = 0 + ans
			elif len(ans) == 2:
				 info['m'] = ans
			else:
				printBold('Month error','red')
				sys.exit()

	ifoy = info['y']
	ifom = info['m']
	ifod = info['d']
	pResult = info['y'] + '-' + info['m'] + '-' + info['d']
	hasDup = False
	if pResult.count(ifoy) > 1:
		hasDup = True
	if pResult.count(ifom) > 1:
		hasDup = True
	if pResult.count(ifod) > 1:
		hasDup = True


	changed = []
	def test(l):
		result = ''
		if int(l) > 1000:
			result = 'y'
		elif int(l) > 12:
			result = 'd'
		return result
	fList = ''
	if test(ifom) == 'y':
		fList += 'y'
		info['y'] = ifom
		# info['m'] = ifoy
	if test(ifod) == 'y':
		fList += 'y'
		info['y'] = ifod
		# info['d'] = ifoy
	if test(ifod) == 'd':
		fList += 'd'
	if test(ifoy) == 'd':
		fList += 'd'
		info['d'] = ifoy
	if test(ifom) == 'd':
		fList += 'd'
		info['d'] = ifom
	if test(ifoy) == '' and 'd' in fList:
		fList += 'm'
		info['m'] = ifoy
	if test(ifoy) == '' and 'd' in fList:
		fList += 'm'
		info['m'] = ifoy
	if test(ifoy) == 'd':
		fList += 'd'
		info['d'] = ifoy
	if test(ifod) == '' and 'd' in fList:
		info['m'] = ifod
	# print_(test(ifoy))
	# print_(fList)

	result = info['y'] + '-' + info['m'] + '-' + info['d']
	# print_(result)
	if not hasDup:
		hasDup = False
		if result.count(ifoy) > 1:
			hasDup = True
		if result.count(ifom) > 1:
			hasDup = True
		if result.count(ifod) > 1:
			hasDup = True
		if hasDup:
			print_('Error please specify format: ymd')
			sys.exit()
	else:
		if result.count(info['y']) > 1:
			print_('Error please specify format: ymd')
			sys.exit()

	print_(result)
	sys.exit()
	return result



def getMonthData():
	monthData = getText(_v.myTables + _v.slash+'month.txt')
	monthList = []
	for md in monthData:
		md = md.replace('\n','')
		mds = md.split(',')
		monthList.append({'month': mds[0], 'abbrev': mds[1], 'number': mds[2]})
	return monthList



def formatPhone00(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)
	data = _str.cleanBE(data,'.')
	return data

def formatPhone0(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = '(' + data[0] + data[1] + data[2] + ') ' + data[3] + data[4] + data[5] + '-' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

def formatPhone1(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = data[0] + data[1] + data[2] + '-' + data[3] + data[4] + data[5] + '-' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

def formatPhone2(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = data[0] + data[1] + data[2] + '.' + data[3] + data[4] + data[5] + '.' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

updateLine_disable = False


def updateLine( string, clear=True, color=None, sleep=None ):
	if not sleep is None: time.sleep(sleep)
	return print_(string,c=color,end='\r')


	
	global updateLine_disable
	if updateLine_disable:
		clear = False
	if type(string) == list:
		for i,s in enumerate(string):
			string[i]=str(s)
		string = ' '.join(string)
	a=None
	b=None
	c=None
	if type(clear) == str:
		b = clear
	if type(color) == bool:
		a = color
	if type(clear) == int or type(clear) == float:
		c = clear
	if type(color) == int or type(color) == float:
		c = color

	if not a is None:
		clear = a
	if not b is None:
		color = b
	if not c is None:
		sleep = c


	if type(color) == str:
		string = cp( string, color, p=0 )

	if clear:
		txt = linePrint(txt=' ',p=0)
		updateLine(txt,clear=False)


	if updateLine_disable:
		print_(string)
	else:
		print_('{}\r'.format(string), end="")


	if not sleep is None:
		time.sleep(sleep)




def getLastTableSplit(theFile,tableTemp = 'split'):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	if tableTemp == 'split':
		basePath = _v.myTables + _v.slash+'tablesets'
	else:
		basePath = _v.stmp
	# print_(basePath)
	dirList = os.listdir(basePath)
	fileList = []
	for d in dirList:
		if d.startswith(theFile):
			fileList.append(d)
	# print_(fileList)
	fileList.sort()
	# print_(fileList)
	# print_()
	# print_(fileList[len(fileList)-1])
	# print_(fileList)
	# file0 = basePath + _v.slash + fileList[len(fileList)-1]
	# print_(file0)
	return getTable(fileList[len(fileList)-1],tableTemp)

def saveTableSplitNew( rows,theFile,tableTemp = True,printThis = True, project=False, me=0 ):
	HD.chmod(theFile)
	# defaults to myTables
	print_( 'save size:', len(rows))
	if tableTemp:
		file0 = _v.myTables + _v.slash+'tablesets' + _v.slash + theFile
	elif project:
		file0 = _v.myTables + _v.slash+'projects' + _v.slash + theFile

	else:
		file0 = _v.stmp + _v.slash + theFile

	def count(cnt):
		char = 6
		cnt = str(cnt)
		lencnt = len(cnt)
		if lencnt == 1:
			cnt = '00000' + cnt
		if lencnt == 2:
			cnt = '0000' + cnt
		if lencnt == 3:
			cnt = '000' + cnt
		if lencnt == 4:
			cnt = '00' + cnt
		if lencnt == 5:
			cnt = '0' + cnt
		cnt = '_' + cnt
		return cnt

	suffix = '.json'
	cnt = 0
	path = file0 + count(cnt) + suffix
	while os.path.isfile(path) == True:
		cnt += 1
		path = file0 + count(cnt) + suffix
	simplejson = __.imp('simplejson')
	dataDump = simplejson.dumps(rows, indent=4, sort_keys=True, default=str)
	f = open(path,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(path)
	if printThis:
		print_('Saved: ' + path)
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );

def sort(rows, name):
	global errors
	tempFields = []
	sortBy = {}
	name = name.replace('.',':')
	sortList = name.split(',')
	sortList.reverse()

	### Check for bad sort input
	for item in sortList:
		item = item
		try:
			if item.count(':') > 0:
				sb = item.split(':')[1]
			else:
				sb = item
		except Exception as e:
			errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})


	# itemgetter = __.imp('operator.itemgetter')
	for item in sortList:
		try:
			direction = item.split(':')[0]
			sb = item.split(':')[1]
			if direction == 'asc':
			# if direction.find('a') == 0:
				rows = sorted(rows, key=itemgetter(sb))
			else:
				rows = sorted(rows, key=itemgetter(sb), reverse=True)
		except Exception as e:
			try:
				pass
				rows = sorted(rows, key=itemgetter(item))
			except Exception as e:
				errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			
		uuid = __.imp('uuid')
		sortBy[item] = str(uuid.uuid4())
		tempFields.append( sortBy[item] )
		i = 0
		for row in rows:
			rows[i][sortBy[item]] = i
			i += 1

	# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

	sortCode = 'rows = sorted(rows, key=lambda d: ('
	for item in sortList:
		sortCode += "d['" + str(sortBy[item]) + "'],"
	sortCode = sortCode[:-1]
	sortCode += '))'
	exec(sortCode)
	if len( tempFields ):
		# print_( tempFields )
		for ix,r in enumerate(rows):
			for tmp in tempFields:
				try:
					del rows[ix][tmp]
				except Exception as e:
					pass

	return rows

def blank_script_trigger(data):
	return data

class Switch:

	def __init__(self, name, switch, expected_input_example, description, space):
		self.appReg = __.appReg
		self.name = name
		self.switch = switch
		self.pos = 0
		self.active = False
		self.value = None
		self.values = []
		self.expected_input_example = expected_input_example
		self.documentation = { 'description': description, 'examples': [], 'required': [], 'related': [] }
		self.space = space
		self.vs = False
		self.script_trigger_alt = None
		self.script=blank_script_trigger
		
	def trigger(self,script,vs=False,alt=None):
		if not alt is None:
			self.script_trigger_alt = alt
			vs = True
		self.vs = vs
		self.script_trigger = script
		self.script = script



class Switches:

	def __init__(self):
		self.switches = []
		self.index = {}
		self.appRegDefault = None
		self.appReg = __.appReg
		self.hasRequired = []
		self.isRequired = {}
		self.postScripts = []
		self.dex = {}


	def all( self, appReg=None, omit=None, omitDefaults=True,             od=1 ):
		if not od:
			omitDefaults = False
		if omitDefaults:
			omitList = [ 'Help', 'Column', 'Sort', 'Debug', 'Errors', 'Timeout', 'GroupBy', 'ShortenColumn', 'Long', 'Length', 'Report', 'Plus', 'Minus', 'PlusOr', 'PlusClose', 'PrintAutoAbbreviations', 'LoadEpoch', 'NoColor', 'Clean', 'NoCount', 'Count' ]
		else:
			omitList = []

		if not  omit is None:
			if type(omit) == str:
				omit = omit.replace(  ' ', '' )
				omit = omit.split(',')
			for x in omit:
				omitList.append( x )


		# appReg values expected: None, 1, true, 'all'
		if appReg is None:
			appReg = __.appReg

		result = []
		for i,row in enumerate(self.switches):
			if not row.name in omitList:
				if row.active:
					shouldAdd = True
					if type( appReg ) == str:
						if not appReg == 'all':
							if not row.appReg == appReg:
								shouldAdd = False

					if shouldAdd:
						if not row.values:
							for ii,rec in enumerate(self.switches):
								if not i == ii and rec.name == row.name and rec.values: shouldAdd = False
					if shouldAdd:
						result.append({
											'active': row.active,
											'name': row.name,
											'value': row.value,
											'values': row.values,
											'appReg': row.appReg,
						})
		# _result=[]
		# _spent=[]
		# for i, rec in result:
		# 	cnt=0
		# 	for i, rec in result:



		return result




	def records( self, formating=None, appReg=None ):
	# def records( self, formating=None, appReg=None, empty=True, v=None ):
		# if not v is None and v: empty=False
		# elif not v is None and v: empty=True
		if formating is None:
			colorThis( 'formating options:', 'bold' )
			colorThis( [ '\t', 'list' ], 'yellow' )
			colorThis( [ '\t', 'dic_a-v', '\t', "{ 'isActive': {}, 'values': {} }" ], 'yellow' )
			colorThis( [ '\t', 'dic_on-off-v', '\t', "{ 'on': [], 'off': [], 'values': {} }" ], 'yellow' )
			colorThis( [ '\t', 'dump' ], 'yellow' )
			colorThis( [ '\t', 'relevant' ], 'yellow' )
			colorThis( [ '\t', 'dump2' ], 'yellow' )
			sys.exit()

			colorThis(  )
		if appReg is None:
			appReg = __.appReg


		records = {
						'list': [],
						'dic_a-v': { 'active': self.active(), 'isActive': {}, 'values': {} },
						'dic_on-off-v': { 'on': [], 'off': [], 'values': {} },
						'dump': [],
						'dump2': {},
		}


		for i,switch in enumerate(self.switches):

			#b)--> dump2
			if not switch.appReg in records['dump2']: records['dump2'][switch.appReg]={}
			if not 'on' in records['dump2'][switch.appReg]:
				records['dump2'][switch.appReg]['on']={}
				records['dump2'][switch.appReg]['off']={}

			if switch.active:
				if switch.name in records['dump2'][switch.appReg]['on'] and switch.values:
					records['dump2'][switch.appReg]['on'][switch.name] = switch.values
				else:
					records['dump2'][switch.appReg]['on'][switch.name] = switch.values
			else: records['dump2'][switch.appReg]['off'][switch.name] = switch.values
			#e)--> dump2

			
			
			#b)--> duplicate fix
			##### #timestamp)--> 2022-07-26T17:09:11-0400
			shouldAdd = True
			for ii,rec in enumerate(self.switches):
				if not i == ii and rec.name == switch.name and rec.values: shouldAdd = False
			if shouldAdd:
			#e)--> duplicate fix
			
				if self.switches[i].appReg == appReg:
					records['list'].append({ 'name': switch.name, 'values': switch.values })


					records['dic_a-v']['isActive'][switch.name] = switch.active
					records['dic_a-v']['values'][switch.name] = switch.values


					records['dump'] = dict((name, getattr(switch, name)) for name in dir(switch) if not name.startswith('__'))
					records['dic_on-off-v']['values'][switch.name] = switch.values

					
					if switch.active:
						records['dic_on-off-v']['on'].append( switch.name )
					else:
						records['dic_on-off-v']['off'].append( switch.name )
		
		#b)--> relevant
		records['relevant']={}
		for on in records['dic_on-off-v']['on']:
			records['relevant'][on] = records['dic_on-off-v']['values'][on]
		if formating.startswith('r'): formating = 'relevant'
		#e)--> relevant
		return records[ formating ]
	def documentation( self, name, data ):
		result = False
		try:
			for i,row in enumerate(self.switches):
				if row.name == name:
					# print_( 'SET' )
					if self.switches[i].appReg == __.appReg:

						try:
							if len( data['description'] ):
								self.switches[i].documentation['description'] = data['description']
						except Exception as e:
							pass

						try:
							if len( data['examples'] ):
								self.switches[i].documentation['examples'] = data['examples']
						except Exception as e:
							pass

						try:
							if len( data['required'] ):
								self.switches[i].documentation['required'] = []
								self.switches[i].documentation['related'] = []
								for record in data['required']:
									if record == 'Pipe':
										__.isRequired_Pipe = True
									else:
										self.switches[i].documentation['required'].append( record )
										self.switches[i].documentation['related'].append( record )
										if not name in self.hasRequired:
											self.hasRequired.append( name )
								

						except Exception as e:
							pass

						try:
							if len( data['related'] ):
								for record in data['related']:
									self.switches[i].documentation['related'].append( record )
						except Exception as e:
							pass

						try:
							if type( data['isRequired'] ) == bool:
								if data['isRequired']:
									if not name in self.isRequired[__.appReg]:
										self.isRequired[__.appReg].append( name )
						except Exception as e:
							pass



		except Exception as e:
			result = False
		return result


	def record( self, name ):
		result = False
		try:
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						return i
		except Exception as e:
			result = False
		return result

	def dumpSwitches(self,includeBlank=False):
		self.fieldSet('Long','active',True)
		data = []
		for i,row in enumerate(self.switches):
			# if not row.value is None:
			if includeBlank:
				data.append({ 'name': row.name, 'value': row.value, 'appreg': row.appReg })
			else:
				if not row.value is None or row.active:
					data.append({ 'name': row.name, 'value': row.value, 'appreg': row.appReg })
			# print_(row.name,'\t',row.value,'\t',row.appReg)
		tables.register('data',data)
		tables.print('data','appreg,name,value')

	def register(self, name, switch, expected_input_example = None, isRequired=False, isPipe=None, isData=None, description='', space=False):

		if not isPipe is None:
			__.trigger_isPipe = isPipe

		if not isData is None:
			__.trigger_isPipe = isData
			isPipe=isData
		i=len(self.switches)

		if not __.appReg in self.dex:
			self.dex[__.appReg]={}
		self.dex[__.appReg][name]=i

		self.switches.append(Switch(name, switch, expected_input_example, description, space))

		try:
			if not type(self.isRequired[__.appReg]) == list:
				self.isRequired[__.appReg] = []
		except Exception as e:
			self.isRequired[__.appReg] = []
		
		

		switch = switch.replace( ' ', '' )

		
		if not isPipe is None:
			if type(isPipe) == bool and isPipe:
				isPipe = 'data'
			v.isData[name]=isPipe

			if 'name' in isPipe and ( 'data' in isPipe or 'clean' in isPipe ):
				pass
			elif 'name' in isPipe:
				__.trigger_isPipe = 'name'
			elif 'data' in isPipe or 'clean' in isPipe:
				if 'clean' in isPipe:
					__.trigger_isPipe = 'data,clean'
				else:
					__.trigger_isPipe = 'data'
		elif isPipe:
			__.trigger_isPipe = 'data'

		if isRequired:
			__.isRequired_index[__.appReg].append( name )
			if not name in self.isRequired[__.appReg]:
				self.isRequired[__.appReg].append( name )



	def fieldSet( self, name, column, value, theFocus=False, runTrigger=True ):
		if name == 'Sort':
			if column == 'value':
				if type(value) == str:
					if value.startswith('a.'):
						value = 'a:' + value[2:]
					if ',a.' in value:
						value = value.replace( ',a.', ',a:' )

					if value.startswith('d.'):
						value = 'd:' + value[2:]
					if ',d.' in value:
						value = value.replace( ',d.', ',d:' )
			if column == 'values':
				if type(value) == list:
					for i,asdf in enumerate(value):
						if value[i].startswith('a.'):
							value[i] = 'a:' + value[i][2:]
						if value[i].startswith('d.'):
							value[i] = 'd:' + value[i][2:]


		if type( theFocus ) == bool:
			theFocus = __.appReg

		if column == 'values':
			if type(value) == str:
				value = [value]
			values = []
			valuesV = []
			if not runTrigger:
				for x in value:
					values.append( x )
			elif runTrigger:
				if self.fieldExists( name, 'script_trigger', theFocus ):
					for x in value:
						values.append( self.scriptTrigger( name, x, theFocus  ) )

				elif self.fieldExists( name, 'script_trigger', theFocus ) == True:    
					for x in value:
						script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,x)# script_trigger_external
						values.append( eval(script) )
				else:
					for x in value:
						values.append( x )
			for x in values:
				if type(x) == str:
					valuesV.append( x.replace(',',';;') )
		if column == 'value':
			if runTrigger:
				if self.fieldExists( name, 'script_trigger', theFocus ):
					value = self.scriptTrigger( name, value, theFocus  )
					# self.fieldGet(name,'script_trigger')(value)
				elif self.fieldExists( name, 'script_trigger', theFocus ) == True:
					script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)# script_trigger_external
					value = eval(script)
		# print_( name, column, value )
		# sys.exit()
		for i,row in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				if row.name == name:
					if column == 'active':
						if value == True:
							self.switches[i].active = True
						else:
							self.switches[i].active = False
					elif column == 'value':
						if value == True:
							self.switches[i].value = True
						elif value == False:
							self.switches[i].value = False
						else:
							self.switches[i].value = value
					elif column == 'values':
						self.switches[i].values = values
						self.switches[i].value = ','.join(valuesV)

					else:
						# self.switches[i][column] = value
						exec('self.switches[i].' + column + '= value')
						# value = str(value)
						# try:
						#   exec('self.switches[i].' + column + '=str(\'' + value + '\')')
						# except Exception as e:
						#   exec('self.switches[i].' + column + '=\'' + value + '\'')
			
		return ''



	def fieldExists( self, name, column, theFocus=False ):# doesFieldExist
		result = False
		try:
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						eval('row.' + column)
						result = True
		except Exception as e:
			result = False
		return result
	def scriptTrigger( self, name, value, theFocus=False, cc=False ):# externalScriptTrigger
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					if not cc:
						value = self.switches[i].script_trigger(value)# script_trigger_external
					elif cc:
						if not self.switches[i].vs:
							value = self.switches[i].script_trigger(value)# script_trigger_external
						elif not self.switches[i].script_trigger_alt is None:
							value = self.switches[i].script_trigger_alt(value)# script_trigger_external



		return value

	def fieldGet2(self,name,column):# getSwitchField
		# print_(name,column)
		result = ''
		for i,row in enumerate(self.switches):
			if row.name == name:
				result = eval('row.' + column)
		return result

	def fieldGet( self, name, column, theFocus=False ):# getSwitchField
		# print_(name,column)
		result = ''
		if not column == 'pos':

			if name == 'NoColor' and column == 'active':

				found = False

				for i,row in enumerate(self.switches):
					if row.name == name:
						# print_( row.name, row.active )
						if row.active:
							found = True

				result = found
						
				# print_( 'here', name, found )
				# sys.exit()


			else:


				i = self.searchIndex( name, theFocus )
				if i is None:

					if column == 'active':
						return False

					if column == 'value':
						return ''

					if column == 'values':
						return []

					printBold( 'Error: Nonexistent Switch', 'red' )
					print_( name, column, theFocus )
					printVar( self.index )
					sys.exit()
				row = self.switches[i]
				result = eval('row.' + column)

		else:
			if type( theFocus ) == bool:
				theFocus = __.appReg
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == theFocus:
					if row.name == name:
						result = eval('row.' + column)
		return result

	def isActive2( self, name, theFocus=False ):
			for i,row in enumerate(self.switches):
				if self.switches[i].name == name and self.switches[i].active: return True
			return False


	def isActive( self, name, theFocus=False ):# isSwitchActive
		if not theFocus: theFocus = __.appReg
		if theFocus in self.dex and name in self.dex[theFocus]:
			# print('from index')
			return self.switches[self.dex[theFocus][name]].active
		return self.fieldGet( name, 'active', theFocus )

	def getField( self, name, field, theFocus=False ):
		return self.fieldGet( name, field, theFocus )

	def value( self, name, theFocus=False ):# getSwitchValue
		result = self.fieldGet( name, 'value', theFocus )
		if result is None:
			result = ''
		return result

	def values( self, name, theFocus=False ):# getSwitchValue
		result = self.fieldGet( name, 'values', theFocus )
		if result is None:
			result = []
		return result


	def trigger( self, name, script, vs=False, alt=None ):
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					self.switches[i].trigger(script,vs,alt)
	
	def simpleTrigger( self, name, value ):
		return self.switches[self.dex[__.appReg][name]].script(value)
					

	def value2(self,name):
		# return ','.join( self.value3(name) )
		# return ','.join(  self.value3(name)  )


		switchInput = sys.argv
		for i,a in enumerate(switchInput): switchInput[i]=a.replace('↔',' ')
		# print(switchInput)
		# sys.exit()

		try:
			switchInput[self.fieldGet(name,'pos') + 1]
			result = ''

			i = 0
			for a in switchInput:
				if i > self.fieldGet(name,'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					else:
						if not name in __.switch_raw:
							if switchInput[i] == ':':
								switchInput[i] = switchInput[i].replace(':','_;192B;_')
							if switchInput[i] == ',':
								switchInput[i] = switchInput[i].replace(',','_;192A;_')
						result += str(switchInput[i]) + ','
				i += 1
			result = result[:-1]
			if not name in __.switch_raw:
				result = _str.cleanAll(result,'"','')
				result = _str.cleanAll(result,':,',':')
				result = _str.cleanAll(result,',,',',')

		except Exception as e:
			result = ''
		if not name in __.switch_raw:
			return result
			# return _str.cleanBE( result, ' ' )
		else:
			return result

	def value3(self,name):
		switchInput = sys.argv
		for i,a in enumerate(switchInput): switchInput[i]=a.replace('↔',' ')
		data = []
		try:
			switchInput[self.fieldGet(name,'pos') + 1]
			result = ''

			for i,a in enumerate(switchInput):
				# a=self.simpleTrigger(name,a)
				if i > self.fieldGet(name,'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					else:
						if not a == ' ':
							if not name in __.switch_raw:
								data.append(a)
								# data.append( _str.cleanBE( a, ' ' ) )
							else:
								data.append( a )
						else:
							data.append( a )


		except Exception as e:
			data = []
		return data

	def isSwitch(self,string):# checkIfSwitch
		result = False
		for i,a in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				for b in a.switch.split(','):
					if b == string:
						result = True
					# print_(b,result)
		return result

	def format(self,name):# processSwitchFormatting
		value = self.value2(name)
		if self.fieldExists(name,'script_trigger'):
			value = self.scriptTrigger(name,value,cc=True)
		elif self.fieldExists(name,'script_trigger'):
			script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)
			value = eval(script)
		return value

	def format2( self, name ):
		values = self.value3(name)
		# if name =='Plus':
		#     print_(values)
		if values is None:
			values = []
		else:
			for i,value in enumerate(values):
				if self.fieldExists(name,'script_trigger'):
					values[i] = self.scriptTrigger(name,value)
				elif self.fieldExists(name,'script_trigger'):
					script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)
					values[i] = eval(script)
		return values

	def exists(self,name):# checkSwitchExist
		result = False
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.name == name:
					result = True
		return result
	def help(self):
		if self.value('Help') == 'x' or self.value('Help') == 'cls' or self.value('Help') == 'clear':
			if __.isWin:
				os.system('cls')
			else:
				os.system('clear')
		# print_(__.registeredApps)
		# print_(__.appReg)
		# sys.exit()
		if len(__.registeredApps) > 1:
			# print_(__.appReg)
			if __.appReg == '__init__' or __.appReg == 'cryptFile':
				return None
		if __.appInfoScan:
			return None
		# self.help()
		global appInfo
		global fields
		self.fieldSet('Long','active',True)
		if __.cls_process_switches_help or 'cls' in self.value('Help'):
			os.system('cls')
		# os.system('cls')
		print_()
		print_()
		filename = colorThis(  [ 'Program:  \t' ], 'bold', p=0  )
		try:
			filename += colorThis(  [ appInfo[__.appReg]['liveAppName'] ], 'yellow', p=0  )
		except Exception as e:
			filename += colorThis(  [ appInfo[__.appReg]['file'].replace('.py','') ], 'yellow', p=0  )
		print_()
		print_( filename )
		print_()

		try:
			if type( appInfo[__.appReg]['description'] ) == list:
				print_( inlineBold('Description:   '))
				for x in appInfo[__.appReg]['description']:
					print_( '                 - ', x )
				print_()
			else:
				print_( inlineBold('Description:   '), appInfo[__.appReg]['description'] + '\n')
			configured = True
		except Exception as e:
			configured = False
			
		try:
			# print_( inlineBold('Categories:    '), ', '.join( appInfo[__.appReg]['categories'] ) + '\n')
			print_( inlineBold('Tags:          '), '(',', '.join( appInfo[__.appReg]['categories'] ), ')' + '\n')
			# print_( inlineBold('          Tags:'), ', '.join( appInfo[__.appReg]['categories'] ) + '\n')
			pass
		except Exception as e:
			pass

		try:
			if len(appInfo[__.appReg]['prerequisite']) > 0:
				printBold('Prerequisite:')
				for docItem in appInfo[__.appReg]['prerequisite']:
					if type(docItem) == list:
						colorThis( '\t\t'+docItem[0], docItem[1]  )
					else:
						colorizeRow( '\t\t'+ docItem , 2)
					# colorizeRow('\t' + prereq,2)
				print_('\n')
		except Exception as e:
			pass
		try:
			if len(appInfo[__.appReg]['relatedapps']) > 0:
				printBold('Related Apps:')
				for docItem in appInfo[__.appReg]['relatedapps']:
					if type(docItem) == list:
						colorThis( '\t\t'+docItem[0], docItem[1]  )
					else:
						colorizeRow( '\t\t'+ docItem , 2)
				print_('\n')
		except Exception as e:
			pass
		if configured:
			quit_early = False
			if len(appInfo[__.appReg]['examples']) > 0:
				printBold('Examples:')
				IDs = {}
				ei = 1
				for docItem in appInfo[__.appReg]['examples']:
					if not docItem is None:
						prei = str(ei)
						if len(self.value('Help')) and self.value('Help') == prei:
							prei = '*'
						elif not 'id' in self.value('Help') and not 'c' in self.value('Help') :
							prei = ''
						else:
							quit_early = True
						if type(docItem) == list:
							if not len(docItem[0]):
								prei = ''
							else:
								ei+=1
							if prei == '*':
								setClip(docItem[0])
								quit_early= True
							if len(prei):
								IDs[prei] = docItem[0]
							colorThis( '\t'+prei+'\t'+docItem[0], docItem[1]  )
						else:
							if not len(docItem):
								prei = ''
							else:
								ei+=1

							if len(prei):
								IDs[prei] = docItem
							if prei == '*':
								setClip(docItem)
								quit_early = True
							colorizeRow( '\t'+prei+'\t'+ docItem , 2)
			if 'id' in self.value('Help') or 'c' in self.value('Help') or 'ask' in self.value('Help'):
				askID = input( '?> : ' )
				if askID in IDs:
					setClip(IDs[askID])
					cp(  [ '\n\nCopied:\n\t', IDs[askID], '\n\n' ], 'green'  )
			if quit_early:
				sys.exit()
					# colorizeRow('\t' + ex,2)
				print_('\n')
			if len(appInfo[__.appReg]['columns']) > 0:
				printBold('Columns and abbreviations:')
				result = ''
				if len( appInfo[__.appReg]['columns'] ):
					# fields.register( 'columns', 'name,abbreviation', script=__.triggerTest )
					fields.asset( 'columns', appInfo[__.appReg]['columns'] )
					print_()

				if __.columnAbbreviations == 0:
					for col in appInfo[__.appReg]['columns']:
						if not col['name'] == col['abbreviation']:
							result += col['name'] + '(' + col['abbreviation'] + '), '
					result = result[:-2]
					colorizeRow('\t' + result + '\n',2)

				if __.columnAbbreviations == 1:
					for col in appInfo[__.appReg]['columns']:
						if not col['name'] == col['abbreviation']:
							abbreviation =  fields.value( 'columns', 'abbreviation', col['abbreviation'] )
							name =          fields.value( 'columns', 'name', col['name'] )
							colorizeRow( '\t' + abbreviation + '\t' + name )
						# print_( '\t', col['abbreviation'], '\t', col['name']  )

				if len( appInfo[__.appReg]['columns'] ):
					print_()
					print_()
				# print_('\n')
		pass
		print_()
		print_()
		# def linePrint(  label=None, text=None, txt='_', mn=50, add=5, p=2, c='', half=False, h=None )
		linePrint(txt='+',c='yellow',x=.5)
		# colorThis('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','yellow')
		printBold( 'Requirements:' )
		print_()
		hasRequirements = False
		# if __.isRequired_Pipe_or_File:
		#     hasRequirements = True
		#     colorThis(  [  '  !! Required Pipe or Files'  ]  , 'red' )

		# if len( self.isRequired[__.appReg] ):
		#     for x in self.isRequired[__.appReg]:
		#         hasRequirements = True
		#         colorThis(  [  '  !! Required Switch:', x  ]  , 'red' )

		if __.isRequired_Pipe:
			hasRequirements = True
			colorThis(  [  '  !! Required Pipe data' ]  , 'red' )
		
		if __.isRequired_Pipe_or_File:
			hasRequirements = True
			colorThis(  [  '  !! Required Pipe data or Files switch' ]  , 'red' )

		if len(self.isRequired[__.appReg]):
			hasRequirements = True
			colorThis(  [  '  !! Required ' + ' and '.join(self.isRequired[__.appReg])  ]  , 'red' )


		if not __.isRequired_or_List is None:
			# for x in __.isRequired_or_List:
			hasRequirements = True
			colorThis(  [  '  !! Required ' + ' or '.join(__.isRequired_or_List)  ]  , 'red' )


		for switch in self.switches:
			# print_( dir(switch) )
			# print_( switch.__dict__ )
			if len(switch.documentation['required']) :
				print_()
				print_()
				print_( colorThis( '  !! If using switch:' , 'bold', p=0 ), colorThis( switch.name , 'yellow', p=0 ), colorThis( 'the following is required:' , 'bold', p=0 ) )
				for x in switch.documentation['required']:
					hasRequirements = True
					colorThis(  [ '\t', x  ]  , 'red' )


			if len(switch.documentation['related']) :
				print_()
				print_()
				print_( colorThis( '  If using switch:' , 'bold', p=0 ), colorThis( switch.name , 'yellow', p=0 ), colorThis( 'the following is related:' , 'bold', p=0 ) )
				for x in switch.documentation['related']:
					hasRequirements = True
					colorThis(  [ '\t', x  ]  , 'yellow' )

				# del switch.script_trigger
				# del switch.__dict__.script_trigger
				# print_( dict( str(switch.__dict__) ) )
				# printVar( dict(switch.__dict__) )
			# sys.exit()
		if not hasRequirements:
			colorThis( [ '\t', 'No requirements' ], 'green' )
		print_()
		linePrint(txt='+',c='yellow',x=.5)
		# colorThis('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','yellow')
		print_()
		print_()
		self.print()
		if 'notes' in appInfo[__.appReg]:
			if len( appInfo[__.appReg]['notes'] ):
				print_()
				print_()
				printBold( 'Notes:' )
				for col in appInfo[__.appReg]['notes']:
					print_()
					printVarSimple( col, prefix='                ', remove='"' )
					print_()

		# for x in sys.modules:
		#     print_(x)
		sys.exit()
		raise SystemExit
		os._exit(0)
		sys.exit(1)
		os._exit(os.EX_OK)



			
	def process( self, helpx=False ):
		load()
		global customHelp
		global argvProcess
		global printAutoAbbreviations_scheduled
		for ii,sw in enumerate(self.switches):
			if self.switches[ii].appReg == __.appReg:
				self.switches[ii].pos = None
				self.switches[ii].active = False
				self.switches[ii].value = None
				try:
					__.trigger_isPipe = self.switches[ii].isData
				except Exception as e:
					pass

		switchHelp = []
		isActiveList = []
		hasActiveRequireList = []
		isActiveRequireList = []

		if argvProcess:
			for i,a in enumerate(sys.argv):
				a=a.replace('↔',' ')
				if a in __.switch_skimmer.scan:
					__.switch_skimmer.active.append( a )
				a = a.replace(':','')
				for ii,sw in enumerate(self.switches):
					for s in sw.switch.split(','):
						if s.lower() == a.lower():
							if self.switches[ii].appReg == __.appReg:
								self.switches[ii].pos = i
								self.switches[ii].active = True
								self.switches[ii].value = self.format(self.switches[ii].name)
								self.switches[ii].values = self.format2(self.switches[ii].name)

								isActiveList.append( ii )
								if self.switches[ii].name in self.hasRequired:
									hasActiveRequireList.append( ii )
								if self.switches[ii].name in self.isRequired[__.appReg]:
									isActiveRequireList.append( ii )

								if type( self.switches[ii].value ) == str:
									if '-??' in self.switches[ii].value:
										switchHelp.append(ii)

		if self.exists('_Raw') == True:
			# print_('test')
			self.fieldSet('_Raw','pos',1)
			self.fieldSet('_Raw','active',True)
			self.fieldSet('_Raw','value',self.format('_Raw'))


		for i,record in enumerate(self.switches):
			if self.appRegDefault is None:
				self.appRegDefault = self.switches[i].appReg
			self.index[ self.switches[i].appReg ] = {}
		for i,record in enumerate(self.switches):
			self.index[ self.switches[i].appReg ][self.switches[i].name] = i



		if len( switchHelp ):
			if __.cls_process_switches_help:
				os.system('cls')

			somethingPrinted = False
			for i in switchHelp:
				if len( self.switches[i].documentation['description'] ):
					somethingPrinted = True
					print_()
					print_( inlineBold('Description:\t'), self.switches[i].documentation['description'] )
					print_()
				if len( self.switches[i].documentation['examples'] ):
					printBold( 'Examples:' )
					for example in self.switches[i].documentation['examples']:
						if type(example) == list:
							_.colorThis( '\t\t'+example[0], example[1]  )
						else:
							colorizeRow( '\t\t'+ example , 2)



			if somethingPrinted:
				sys.exit()

		if self.isActive('PlusCode'):
			__.sw.PlusCode.append('0a72b2d27816')
			for xCode in self.values('PlusCode'):
				if len(xCode) > 1:
					if xCode.startswith('*'): __.sw.PlusCode.append('*x')
					elif xCode.endswith('*'): __.sw.PlusCode.append('x*')
				else:
					if xCode == '=': __.sw.PlusCode.append('=')
					elif xCode == '!': __.sw.PlusCode.append('=')


		if self.isActive('Help') or helpx:
			self.help()

		# if self.isActive(''):


		if len( self.isRequired[__.appReg] ):
			allSatisfied = True
			
			for req in self.isRequired[__.appReg]:
				satisfied = False
				for i in isActiveRequireList:
					if self.switches[i].name.lower() == req.lower():
						satisfied = True

				try:
					__.appInfoScan
				except Exception as e:
					if not satisfied:
						allSatisfied = False
						print_()
						print_( colorThis( 'Error:', 'red', p=0 ) + ' missing required switch:', req )
						sys.exit()


		if len( hasActiveRequireList ):
			allSatisfied = True
			for i in hasActiveRequireList:
				satisfied = False
				for r in self.switches[i].documentation['required']:
					for ia in isActiveList:
						if self.switches[i].name.lower() == r.lower():
							satisfied = True
				if not satisfied:
					if not i in switchHelp:
						switchHelp.append( i )
						print_()
						print_( 'Error:\t\t missing required switch' )
					allSatisfied = False



		if self.isActive('DumpSwitches'):
			self.dumpSwitches()
			sys.exit()
		if self.isActive('Debug') == True or self.isActive('Errors') == True:
			# self.print()
			self.printStatus()
			sys.exit()
		
		if printAutoAbbreviations_scheduled:
			printAutoAbbreviations()

		if self.isActive('TableProfile') and len(self.value('TableProfile')):
			global TableProfile_Config

			TableProfile_Config = {}

			values = self.values('TableProfile')
			value  = self.value('TableProfile')

			if not ',' in value and not ';' in value:
				tpv = value


				if tpv == 'gs' or tpv == 'groupspaces' or tpv == 'groupspace':
					try:
						TableProfile_Config['ALLTABLES']['GroupSpaces'] = True
					except Exception as e:
						TableProfile_Config['ALLTABLES'] = {}
						TableProfile_Config['ALLTABLES']['GroupSpaces'] = True
				elif tpv == 'hl':
					try:
						TableProfile_Config['_header_']['alignment'] = 'left'
					except Exception as e:
						TableProfile_Config['_header_'] = {}
						TableProfile_Config['_header_']['alignment'] = 'left'



			else:
				for tpv in value.split(','):
					if not ';' in tpv:



						if tpv == 'gs' or tpv == 'groupspaces' or tpv == 'groupspace':
							try:
								TableProfile_Config['ALLTABLES']['GroupSpaces'] = True
							except Exception as e:
								TableProfile_Config['ALLTABLES'] = {}
								TableProfile_Config['ALLTABLES']['GroupSpaces'] = True
						elif tpv == 'hl':
							try:
								TableProfile_Config['_header_']['alignment'] = 'left'
							except Exception as e:
								TableProfile_Config['_header_'] = {}
								TableProfile_Config['_header_']['alignment'] = 'left'


					elif ';' in tpv and tpv.count(';') == 1:


						tpvX = tpv.split(';')
						if tpvX[1] == 'l' or tpvX[1] == 'left' or tpvX[1] == 'r' or tpvX[1] == 'right' or tpvX[1] == 'c' or tpvX[1] == 'center':
							if tpvX[0] == 'header' or tpvX[0] == 'h':
								tpvX[0] = '_header_'
							if tpvX[1] == 'l': tpvX[1] = 'left';
							if tpvX[1] == 'r': tpvX[1] = 'right';
							if tpvX[1] == 'c': tpvX[1] = 'center';
							try:
								TableProfile_Config[  tpvX[0]  ]['alignment'] = tpvX[1]
							except Exception as e:
								TableProfile_Config[  tpvX[0]  ] = {}
								TableProfile_Config[  tpvX[0]  ]['alignment'] = tpvX[1]

							# printVarSimple( TableProfile_Config )

		# theErrors()
		pass
		pass
		# for i,record in enumerate(self.switches):
		#   self.index[ self.switches[i].name +'._.'+ self.switches[i].appReg ] = i

		if len( self.postScripts ):
			for childScript in self.postScripts:
				if 'function' in str(type(childScript)):
					childScript()
		
		
	def searchIndex( self, name, appReg ):
		if type(appReg) == bool or appReg is None:
			appReg = __.appReg
		try:
			result = self.index[ appReg ][ name ]
			
			# result = self.index[ name +'._.'+ appReg ]
		except Exception as e:
			try:
				result = self.index[ self.appRegDefault ][ name ]
			except Exception as e:
				# print_( name, appReg, self.appRegDefault )
				result = None

		return result


	def print(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				switch.append({'name':sw.name ,'switch':sw.switch,'expected_input_example': sw.expected_input_example})
		# def test(value):
		#   value = value + '_V_'
		#   return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,switch,expected_input_example')
	def printStatus(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.active:
					active = 'True'
				else:
					active = ''
				value = sw.value
				if sw.value == True:
					value = 'True'
				elif sw.value == False:
					value = ''

				switch.append({'name':sw.name ,'active':active,'value': value})
		# def test(value):
		#   value = value + '_V_'
		#   return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,active,value')
	def active(self,theFocus=None):
		if theFocus is None:
			theFocus = __.appReg
		table = []
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				# print_( type(sw.active), sw.active )
				if sw.active:
					table.append(sw.name)
		return table


	def length(self,theFocus=None):
		if theFocus is None:
			theFocus = __.appReg
		ii = 0
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				ii += 1
		return ii

	def rebuild( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		data = []
		for i,row in enumerate(self.switches):
			# if not row.value is None:
			if row.appReg == appReg:
				if row.active:
					sX = row.switch.split(',')
					if row.value is None:
						r = sX[0]
					else:
						r = sX[0] + ' ' + str(row.value)
					data.append( r )
			# print_(row.name,'\t',row.value,'\t',row.appReg)
		return ' '.join( data )
	def getTable( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		data = []
		for i,row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active:

					info = {
								'name': row.name,
								'value': row.value,
								'values': row.values,
					}

					data.append( info )
		return data


	def loadTable( self, data, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		for i,row in enumerate(self.switches):
			for info in data:
				if row.appReg == appReg:
					if row.name == info['name']:

						self.switches[i].value = info['value']
						self.switches[i].values = info['values']
						self.switches[i].active = True

	def onlyLoadEpoch( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		for i,row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active and not row.name == 'LoadEpoch':
					return False


		return True



#   def getSelf(self,name):
#       result = ''
#       for sw in self.switches:
#           if sw.name == name:
#               result = sw
#       return result
# def getSwitchSelf(name):
#   global switches
#   return switches.getSelf(name)


class TableView:

	def __init__(self,name,table,fields,sort):
		self.name = name
		self.fields = fields
		self.sort = sort
		self.table = table
		# print_(self.name)


TableProfile_Config = {}
class Table:

	def __init__( self, name, asset=[], group_space=True, tab='', webtable=None ):
		global switches
		global _dir
		

		self.webtable = webtable
		self.group_space = group_space
		self.name = name
		self.asset = asset
		self.fields = []
		self.views = []
		self.spaces = {}
		self.maxNameLength = 35
		if switches.isActive('Long'):
			try:
				self.maxNameLength = int(switches.value('Long'))
			except Exception as e:
				self.maxNameLength = 35
		self.columnTab = '   '
		self.groupSeparator = '_'
		self.tableProfile = []
		self.tableProfileDefaultAlignment = 'left'
		self.tableProfileDefaultAlignmentHeader = ''
		self.tableProfileDefaultAlignmentChanged = False
		self.tableProfileDefaultAlignment = False
		self.tableProfileDefaultSupersedes = False
		self.views = []
		self.universalSpacing = False

		self.wrapTableKey = 'Da529801Ef674997B9f3382B3eD2b93F'
		self.backup = dot()
		self.backup.asset = asset.copy()
		self.aggregate_processed = False
		self.isWrap = False
		self.hasAggregate = False
		self.hasGroups = False
		self.backup.fields = {}
		self.backup.allfields = {}
		self.backup.NGfields = {}
		self.groupID_KEY = genUUID()
		if len( self.asset ):
			for r in self.asset:
				for k in r:
					if not k in self.backup.fields:
						self.backup.fields[k] = 1
						self.backup.allfields[ tfc(k) ] = k
						self.backup.NGfields[ tfc(k) ] = k


		self.tab_color = ''
		if type(tab) == list:
			self.tab_color = tab[1]
			tab = tab[0]

		tabH = ''
		i=0
		while not i == len(tab):
			i+=1
			tabH+=' '

		self.tab = { 'header': tabH, 'table': tab }

	def registerView(self,name,fields,sort = ''):
		self.views.append(TableView(name,self.name,fields,sort))

	def printView(self,name):
		global switches
		i=0
		for tp in self.views:
			# print_()
			# for x in dir(self.views[i]):
			#   print_(x)

			if self.views[i].name == name:
				# print_('found')
				switches.fieldSet('Sort','active',True)
				switches.fieldSet('Sort','value',str(self.views[i].sort))
				# print_(switches.value('Sort'))
				# try:
					
				# except Exception as e:
				#   pass
				# print_('name:',name)
				self.print(self.views[i].fields)
			i += 1

	# def trigger(self,field,script,includes):
	#   self.views.append({'name': field, 'script_trigger': script , 'includes': includes })


	def nameLength(self,string,suffix):
		result = ''
		toLong = False
		if switches.isActive('Length'):
			result = self.nameLengthFix(string,switches.value('Length'),'')
		else:
			try:
				i = 0
				for L in string:
					if i <= self.maxNameLength:
						result += L
					else:
						toLong = True
					i += 1
				if toLong == True:
					result += '...'
					if len(suffix) > 0:
						result += '  .' + suffix
			except Exception as e:
				result = string
		return result

	def nameLengthFix(self,string,change,suffix):
		result = ''
		toLong = False
		change = change.lower()
		old = self.maxNameLength
		if 'x' in change:
			change = change.replace('x','')
			newLength = self.maxNameLength * int(change)
		else:
			newLength = self.maxNameLength + int(change)
		try:
			i = 0
			for L in string:
				if i <= newLength:
					result += L
				else:
					toLong = True
				i += 1
			if toLong == True:
				result += '...'
				if len(suffix) > 0:
					result += '  .' + suffix
		except Exception as e:
			result = string
		return result

	def tabGetMaxSpace(self,name):
		global errors
		global switches
		rows = self.asset
		spacer = 1
		# print_('*** ' + name)

		# 23-01-09 14:19
		# an attempt to fix    p ls -r    long folder names that include new trigger   _.tables.fieldProfileSet( 'data', 'folder', 'trigger', relative_folder )
			# def fn(field):return field
			# for i,x in enumerate(self.tableProfile):
			# 	if self.tableProfile[i]['name'] == name and '' in self.tableProfile[i] and  'function' in type(self.tableProfile[i]['trigger']):
			# 		fn=self.tableProfile[i]['trigger']
		# did not work

		size = len(name) + spacer
		
		# print_(name,00)
		# rows[0][name]
		for i,rec in enumerate(self.asset):
			if not name in rec: self.asset[i][name]=''
		try:
			pass
			if name in rows[0]:
				rows[0][name]
			else:
				# print_(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
				eval(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
		except Exception as e:
			errors.append({'id': 9, 'function': 'tabGetMaxSpace()', 'cnt': 1, 'location': 'rows[0][name]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			printBold('Error:','red')
			printBold('\tBad column input.')
			print_(9)
			print_(name)
			print_(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
			printVarSimple(rows[0])
			printBold('record sample','red')
			os._exit(0)
		# print_(name)
		for item in rows:
			shorten = True
			if switches.isActive('Long') == True:
				shorten = False
				if switches.isActive('ShortenColumn') == True:
					shortenColumn = switches.value('ShortenColumn')
					for sc in shortenColumn.split(','):
						if sc == name:
							shorten = True
			
			if name in item:
				thisData = item[name]
			elif name.split('.')[0] in item:
				thisData = eval(  'item["' + '"]["'.join(name.split('.')) + '"]'  )


			if shorten == True and not switches.isActive('Length'):
				try:
					text = self.nameLength( str(self.scriptTriggerField(name,thisData)) ,'')
				except Exception as e:
					text = self.nameLength(str(thisData),'')
			else:
				if switches.isActive('Length'):
					# print_('asdf')
					# sys.exit()
					try:
						
						text = self.nameLengthFix(  str(self.scriptTriggerField(name,thisData)) ,switches.value('Length'),'')
					except Exception as e:
						text = self.nameLengthFix(str(thisData),switches.value('Length'),'')
				else:
					# sys.exit()
					# if type(thisData) == int or type(thisData) == float:
					#     text = thisData
					# else:
					try:
						text = self.scriptTriggerField(name,thisData)
					except Exception as e:
						text = thisData
							
			
			itemSize = len(str(text)) + spacer
			if itemSize > size:
				size = itemSize
			# print_(item)
		return size

	def addSpace(self,string,max):
		dif = int(max) - len(string)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def addSpace2(self,max):
		dif = int(max)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def scriptTriggerField(self,field,value):
		i = 0
		for s in self.tableProfile:
			try:
				if self.tableProfile[i]['includes'] == True:
					if ',' in self.tableProfile[i]['name']:
						found = False
						for n in self.tableProfile[i]['name'].split(','):
							if n in field:
								found = True
						if found:
							value = self.tableProfile[i]['script_trigger'](value)
					else:
						if self.tableProfile[i]['name'] in field:
							value = self.tableProfile[i]['script_trigger'](value)
				else:
					if field == self.tableProfile[i]['name']:
						value = self.tableProfile[i]['script_trigger'](value)
			except Exception as e:
				pass
			i += 1
		return value
	def triggerExecute(self,field,value):
		i = 0
		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i]['trigger'](value)
				except Exception as e:
					pass
			else:
				if type(value) == int:
					value = addComma( str(value) )
			i += 1
		return value

	def fieldProfileSet(self,field,propertyName,value):
		field = field.lower()
		if field == '*' and propertyName == 'alignment':
			self.tableProfileDefaultAlignment = value
			self.tableProfileDefaultAlignmentChanged = True
		if field == '_header_' and propertyName == 'alignment':
			self.tableProfileDefaultAlignmentHeader = value
		else:
			if ',' in field:
				for n in field.split(','):
					self.fieldProfileSet(n,propertyName,value)

			found = False
			i = 0
			for s in self.tableProfile:
				if self.tableProfile[i]['name'] == field:
					found = True
					self.tableProfile[i][propertyName] = value
				i += 1

			if not found:
				item = len(self.tableProfile)
				self.tableProfile.append({'name': field, propertyName: value})

	def fieldProfileGet(self,field,propertyName,isHeader = False):
		# print_('ran')
		field = field.lower()
		i = 0
		value = ''
		if isHeader and '_header_' in TableProfile_Config.keys() and propertyName in TableProfile_Config['_header_'].keys():
			return TableProfile_Config['_header_'][propertyName]
		elif not isHeader and field in TableProfile_Config.keys() and propertyName in TableProfile_Config[field].keys():
			return TableProfile_Config[field][propertyName]
		elif '*' in TableProfile_Config.keys() and propertyName in TableProfile_Config['*'].keys():
			return TableProfile_Config['*'][propertyName]

		if propertyName == 'alignment':
			value = self.tableProfileDefaultAlignment

		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i][propertyName]
				except Exception as e:
					pass
			i += 1


		if self.tableProfileDefaultAlignmentChanged and self.tableProfileDefaultSupersedes:
			value = self.tableProfileDefaultAlignment
		if isHeader and len(self.tableProfileDefaultAlignmentHeader) > 0:
			value = self.tableProfileDefaultAlignmentHeader

		elif isHeader:
			value = 'center'
		if propertyName == 'alignment' and value == '':
			value = 'left'
		return value
	def showColumn(self,column,i,columnHeaderLength):
		# print_(column)
		global errors
		global lastGroup
		global switches
		def test(one,two):
			# print_(one,two)
			if (one) == (two):
				return True
			else:
				return False
		groupByList = self.groupByList
		rows = self.asset
		# print_(rows)

		columnList = column
		if column in rows[i]:
			value = str(self.triggerExecute(column,rows[i][column]))
		elif column.split('.')[0] in rows[i]:
			value = str(self.triggerExecute(column,  eval(  'rows[i]["' + '"]["'.join(column.split('.')) + '"]'  )  ) )

		# value = rows[i][column]
		# print_(column,value)
		value = value.replace('\n','')
		# value = self.scriptTriggerField(column,rows[i][column])
		try:
			pass
		except Exception as e:
			pass

		shorten = True
		if switches.isActive('Long') == True:
			shorten = False
			if switches.isActive('ShortenColumn') == True:
				shortenColumn = switches.value('ShortenColumn')
				for sc in shortenColumn.split(','):
					if sc == column:
						shorten = True
		text = str(value)
		if shorten == True:
			text = self.nameLength(str(value),'')
		else:
			text = str(value)


		groupBy = switches.value('GroupBy')
		try:
			tabFix = self.spaces[column]
		except Exception as e:
			# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
			tabFix = self.tabGetMaxSpace(column)
			self.spaces[column] = tabFix

		if switches.isActive('GroupBy') == True:
			for gb in groupBy.split(','):
				gb = str(gb)
				if column == gb:
					# print_('- -',last,text)
					if not test(groupByList[gb],text) == True:
						if groupBy.split(',')[0] == column:
							pass
							if self.group_space:
								print_(self.groupLine(columnList,columnHeaderLength))
							if not self.isExtraRecord:
								for g in groupBy.split(','):
									groupByList[g] = ''
						else:
							pass
							if self.group_space:
								print_('')
						 

						if not self.isExtraRecord:
							groupByList[gb] = text
						else:
							if self.isExtraRecord_000x.split('-')[0] in self.isExtraRecord_0001:
								text = ''

						# else:
						#   print_(text)
					else:
						pass
						 
						if len(self.isExtraRecord_000x):
							self.isExtraRecord_0001[ self.isExtraRecord_000x.split('-')[0] ] = 1
						text = ''
						
		alignment = self.fieldProfileGet(column,'alignment')
		# print_(alignment)
		# if alignment == 'left':
		result = text + self.addSpace(text,tabFix)
		if alignment == 'left':
			result = text + self.addSpace(text,tabFix)
		if alignment == 'right':
			result = self.addSpace(text,tabFix) + text
		if alignment == 'center':
			totalSpace = int(tabFix) - len(text)
			if totalSpace > 0:
				if totalSpace % 2 == 0:
					div2 = totalSpace/2
					theLeft = div2
					theRight = div2
				else:
					divTMP = totalSpace - 1
					div2 = divTMP/2
					theLeft = div2 + 1
					theRight = div2
			else:
				theLeft = 0
				theRight = 0
			result = self.addSpace2(theLeft) + text + self.addSpace2(theRight)
			# print_(column,theLeft,theRight,'0' + result + '0')
			# print_(totalSpace,theLeft,theRight)
		#   result = theLeft + text + theRight
		return result

	def groupLine(self,columnList,columnHeaderLength):
		columnNumber = len(columnList.split(','))
		loop = 0
		result = ''
		while loop < columnHeaderLength + (columnNumber * 4):
			result += self.groupSeparator
			loop += 1
		return result

	def showColumnHeader(self,column):
		# rows = self.asset
		result = ' '
		if type(self.universalSpacing) == dict:
			self.spaces = self.universalSpacing
		for c in column.split(','):
			try:
				tabFix = self.spaces[c]
			except Exception as e:
				# errors.append({'id': 11, 'function': 'showColumn()', 'cnt': 2, 'location': 'tabFix = spaces[c]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}], 'error': e})
				tabFix = self.tabGetMaxSpace(c)
				self.spaces[c] = tabFix
				# print_(tabFix)
			# x
			# alignment = 'center'
			alignment = self.fieldProfileGet(c,'alignment',isHeader=True)
			alignment='left'
			if alignment == '':
				########## Default Alignment ##########
				alignment = 'left'

			if switches.isActive('YesTableLines'):
				result+='|'
			else:
				result+=' '

			if alignment == 'center':
				totalSpace = int(tabFix) - len(c)
				if totalSpace > 0:
					if totalSpace % 2 == 0:
						div2 = totalSpace/2
						theLeft = div2
						theRight = div2
					else:
						divTMP = totalSpace - 1
						div2 = divTMP/2
						theLeft = div2 + 1
						theRight = div2
				else:
					theLeft = 0
					theRight = 0
				result += self.addSpace2(theLeft) + c.replace('_',' ').upper() + self.addSpace2(theRight) + self.columnTab
			if alignment == 'left':
				result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
			if alignment == 'right':
				result += self.addSpace(c,tabFix) + c.replace('_',' ').upper() + self.columnTab
			# else:
				# result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
		
		if switches.isActive('YesTableLines'):
			result += '|'
			if len(switches.value('YesTableLines')):
				newResult = '\n'
				for x in result.replace(' |','| '):
					if x == '|':
						newResult+=x
					else:
						newResult+='-'
				newResult = _str.cleanEnd(newResult,'-')
				result+=newResult

				# for c in column.split(','):
					# result += '|'+self.addSpace(c,tabFix).replace(' ','-') + self.columnTab.replace(' ','-')
					# result += '|'+self.addSpace(c,tabFix).replace(' ','-')


		if switches.isActive('YesTableLines'):
			result = result.replace(' |','| ')
		else:
			result += '\n'
		return '\n'+result

	def findColumName( self, column ):
		for k in self.asset[0].keys():
			if k.lower() == column.lower():
				return k
		for k in self.asset[0].keys():
			if k.lower() == column.split('.')[0].lower():
				return column




	def prefixSize( self ):
		pre = ''
		for x in self.tab['table']+loopPrint(__.table_prefix_padding):
			if x == '\t':
				pre += '    '
			else:
				pre += x
		return len(pre)


	def wrapTable( self, cols=None ):
		# return None

		if not __.terminal.width:
			return None

		cols = __.terminal.width
		cols -= 8
		spaces = []
		theKeys = []
		for c in self.spaces:
			theKeys.append(c)
			spaces.append({ 'c': c, 's': self.spaces[c] })

		spaces = sorted(spaces, key=lambda d: (d['s']))
		spaces.reverse()

		fieldsToShorten = []

		if not len(switches.value('WrapTable')):
			fieldsToShorten.append( spaces[0]['c'] )
			if len( self.spaces.keys() ) > 1:
				diff = percentageDiffIntAuto( spaces[0]['s'], spaces[1]['s'] )
				if diff >= 50:
					fieldsToShorten.append( spaces[1]['c'] )
				# print_( 'diff:', diff )

				if len( self.spaces.keys() ) > 2:
					diff = percentageDiffIntAuto( spaces[0]['s'], spaces[2]['s'] )
					if diff >= 50:
						fieldsToShorten.append( spaces[2]['c'] )
					# print_( 'diff:', diff )
		elif len(switches.value('WrapTable')):
			done = False
			if len(switches.values('WrapTable')) == 1:
				done = False
				wrapBy = switches.value('WrapTable')
				if wrapBy in self.asset[0].keys():
					done = True
				if not done:
					if formatColumns(wrapBy) in self.asset[0].keys():
						wrapBy = formatColumns(wrapBy)
						done = True

				if not done:
					wrapBy = 0
					try:
						wrapBy = int(switches.value('WrapTable'))
					except Exception as e:
						wrapBy = 0
					if wrapBy > 0:
						done = True
			elif len(switches.values('WrapTable')) > 1:
				wrapBy = []
				for xx in switches.values('WrapTable'):
					y = formatColumns(xx)
					if y in self.asset[0].keys():
						wrapBy.append(y)
						done = True

			if done:
				if type(wrapBy) == str:
					fieldsToShorten.append( wrapBy )
				if type(wrapBy) == list:
					for yy in wrapBy:
						fieldsToShorten.append( yy )
				if type(wrapBy) == int:
					for isp, itx in enumerate(spaces):
						fieldsToShorten.append( itx['c'] )
						
						if isp+1 == wrapBy:
							break

				# print_(type(wrapBy))
				# print_(wrapBy)
				# sys.exit()

					


		# print_(fieldsToShorten)
		# sys.exit()

		maxLen = self.maxNameLength
		total = self.prefixSize()
		for c in self.spaces:
			total += self.spaces[c]
			total += len(self.columnTab)
		
		tempSpaces = self.spaces.copy()
		for c in tempSpaces:
			if tempSpaces[c] > maxLen:
				if not c in fieldsToShorten:
					fieldsToShorten.append(c)

		while total > cols:
			hasGrtMax = False

			for fs in fieldsToShorten:
				if tempSpaces[fs] > maxLen:
					hasGrtMax = True
					tempSpaces[fs] -=1
			if not hasGrtMax:
				for fs in fieldsToShorten:
					tempSpaces[fs] -=1

			total = self.prefixSize()
			for c in tempSpaces:
				total += tempSpaces[c]
				total += len(self.columnTab)
		


		# percentageDiffIntAuto
		# printVarSimple( self.spaces )
		# print_( '---------' )
		# printVarSimple( tempSpaces )
		# for x in spaces:
		#   print_(x)

		wrapTableKey = self.wrapTableKey
		
		counter = 0
		global fields
		fields.register( wrapTableKey+'-b', 'val', 4, m=4 )
		fields.register( wrapTableKey, 'val', 7, m=12 )
		test = fields.padZeros( wrapTableKey, 'val', 5 )
		test = fields.padZeros( wrapTableKey+'-b', 'val', 5 )
		letters = {}
		

		# print_(letterSet)
		# sys.exit()
		def letterBoost( i ):
			if not str(i) in letters:
				letters[str(i)] = 'a'
		

		recordsToAdd = []
		for i,record in enumerate(self.asset):
			letters[ str(i) ] = 'a'
			recordKey = 1
			

			this_key = fields.padZeros( wrapTableKey, 'val', i+1 )
			this_key_B = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )

			
			self.asset[i][wrapTableKey+'-sort'] = this_key+'-'+this_key_B
			rec = {}
			rec_last = {}
			for c in tempSpaces:

				if c in record and len( str(record[c]) ) > tempSpaces[c]:
					# rec[c] = {}
					recordKey = 1
					# cs = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
					# # print_(cs)
					# if not cs in rec:
					#   rec[cs] = {}
					# if not c in rec[cs]:
					#   rec[cs][c] = ''
					
					rec_parts = autoWrapText( str(record[c]), length=tempSpaces[c] )

					# print_('_________________________________________')
					# print_()
					# print_(record[c])
					# print_()
					# print_(rec_parts)
					# print_()
					# print_('_________________________________________')
					rp = ''
					last_rp = ''
					for rp in rec_parts:
						if len(rp) and not last_rp == rp:
							last_rp = rp
							cs = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
							recordKey += 1
							if not cs in rec:
								rec[cs] = {}
							if not cs in rec_last:
								rec_last[cs] = {}
							# if not c in rec[cs]:
								# rec[cs][c] = ''
							
							# if c in rec_last[cs]:
							#   if 
							rec[cs][c] = rp
					rp = ''

					# for x in record[c]:
					#   rec[cs][c] += x
					#   if len( rec[cs][c] ) > tempSpaces[c]:
					#       recordKey += 1
					#       cs = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
					#       # print_(cs)
					#       if not cs in rec:
					#           rec[cs] = {}
					#       if not c in rec[cs]:
					#           rec[cs][c] = ''
					# printVarSimple(rec)
					# sys.exit()
			if rec:
				for iii,xXx in enumerate(rec):
					if xXx == '0001':
						for c in rec[xXx]:
							self.asset[i][c] = rec[xXx][c]
					else:
						# print_(xXx)
						rec[xXx][wrapTableKey+'-sort'] = this_key +'-'+ xXx
						recordsToAdd.append(rec[xXx])
					# print_(rec[x])
				# print_(rec)

		for rec in recordsToAdd:
			self.asset.append(rec)
			# print_(rec)
		# sys.exit()
		self.spaces = {}


		groupBy = switches.values('GroupBy')
		last = {}
		for gb in groupBy:
			last[gb] = '{7270D97A-CC1D-4365-9545-87CA34F2F026}'



		for i,record in enumerate(self.asset):
			ks = list(record.keys())
			for k in theKeys:
				if not k in ks:
					self.asset[i][k] = ''
			for k in theKeys:
				if not k in self.spaces:
					self.spaces[k] = 0
				if len(str(record[k])) > self.spaces[k]:
					self.spaces[k] = len(str(record[k]))


		# for i,record in enumerate(self.asset):
		#   for gb in groupBy:
		#       if gb in self.asset[i]:
		#           if self.asset[i][gb] == last[gb]:
		#               self.asset[i][gb] = ''
		#           else:
		#               last[gb] = self.asset[i][gb]
		self.asset = sorted(self.asset, key=lambda d: (d[wrapTableKey+'-sort']))


		# for x in self.asset:
		#   print_()
		#   print_(x)
		#   print_()




		# for i,record in enumerate(self.asset):
		#   print_( record[wrapTableKey+'-sort'] )
		# sys.exit()
		# print_(self.asset)
		# for x in self.asset:
		#   print_()
		#   print_(x)
		#   print_()
		# sys.exit()
		
		self.print(
					column=self.print_backup['column'],
					fieldLengths=self.print_backup['fieldLengths'],
					pc=self.print_backup['pc'],
					printColumns=self.print_backup['printColumns'],
					force=True
		)




	def aggregateRecord( self, i ):
		# print_()
		
		for c in self.aggregates.columns:
			if not c in self.asset[i]:
				self.asset[i][c] = ''

		for seg in self.aggregates.segments:
			if seg['status']:
				record = self.aggregate_record_process( i, seg['i'] )


	def aggregateTop( self, s ):
		ss = str(s)
		if self.aggregates.index[ss]['rent'] >= 0:
			return self.aggregateTop(self.aggregates.index[ss]['rent'])
		else:
			return self.aggregates.index[ss]


	def aggregateItemValue( self, v, f ):
		if not 'params' in v:
			v['params'] = {}
		if not 'fields' in v:
			v['fields'] = {}
		if not 'data' in v:
			v['data'] = []

		# print_( self.aggregate_backtrack )

		if 'data' in f:
			v['data'].append( f['data'] )
		if 'fields' in f:
			if not 'fields' in v:
				v['fields'] = {}
			for k in f['fields']:
				v['fields'][k] = f['fields'][k]
		elif 'params' in f:
			if not 'params' in v:
				v['params'] = {}
			for k in f['params']:
				v['params'][k] = f['params'][k]
		return v

	def aggregate_record_process_group( self, i, s ):
		ss = str(s)
		seg = self.aggregates.index[ss]
		if 'variable' in seg['l']:
			alpha = seg['l']
			if '?' in seg['txt'] and seg['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
				txtParts = seg['txt'].split('?')
				grp = txtParts[0]+'?'
				fld = txtParts[1]
				lbl = txtParts[2]
				if not lbl in self.aggregates.group_storage:
					self.aggregates.group_storage[lbl] = 0


				data = self.aggregate_record_process( i, seg['val'] )
				child = self.aggregates.index[ str(seg['val']) ]
				do = None
				if 'function' in child['l']:
					do = child['txt']
					done = False
					if do == 'max':
						done = True;
						try:
							if data['data'] > self.aggregates.group_storage[lbl]:
								self.aggregates.group_storage[lbl] = data['data']
						except Exception as e: cp('Error: group max variable', 'red');

					if do == 'add':
						done = True;
						try:
							self.aggregates.group_storage[lbl] += data['data']
						except Exception as e: cp('Error: group add variable', 'red');
					
					# if not done:
					#   self.aggregates.group_storage[lbl] = data['data']

				pass


				
				pass

				if i in self.aggregates.groups[fld]['e']:
					if  __.aggregate.group_prefixes[  seg['txt'].lower().split('?')[0]+'?'  ] == 3:
						self.asset[  self.aggregates.groups[fld]['e'][i]  ][lbl] = addComma( self.aggregates.group_storage[lbl] )
					else:
						if tfc(lbl) in self.backup.NGfields:
							if not str(i) in self.aggregates.agroupsADD:
								self.aggregates.agroupsADD[ str(i) ] = {}
							self.aggregates.agroupsADD[ str(i) ][lbl] = self.aggregates.group_storage[lbl]
						else:           
							self.asset[i][lbl] = addComma( self.aggregates.group_storage[lbl] )
					if not __.aggregate.group_prefixes[  seg['txt'].lower().split('?')[0]+'?'  ] == 2:
						self.aggregates.group_storage[lbl] = 0
			


		# if self.aggregates.groups:
		#   printVarSimple(self.aggregates.groups)
		#   print_( list( self.asset[0].keys() ) )
		#   sys.exit()


	def aggregate_record_process( self, i, s ):

		ss = str(s)
		if True:
			seg = self.aggregates.index[ss]
			# print_(seg)
			
			# self.aggregate_backtrack = { 'i': i, 's': s, 'seg': seg }


			if 'alpha' in seg['l'] and 'arg' in seg['l'] :
				simple_keys = {}
				for key in list(self.asset[i].keys()):
					simple_keys[ tfc(key) ] = key
				if tfc(formatColumns( seg['txt'] )) in simple_keys:
					vXv = simple_keys[tfc(formatColumns( seg['txt'] ))]
					return { 'fields': { vXv: self.asset[i][vXv] }, 'data': self.asset[i][vXv] }

				elif formatColumns( seg['txt'] ) in self.asset[i]:
					return { 'fields': { formatColumns( seg['txt'] ): self.asset[i][formatColumns( seg['txt'] )] }, 'data': self.asset[i][formatColumns( seg['txt'] )] }
				return { 'params': { seg['txt']: 1 } }



			if 'variable' in seg['l']:
				alpha = seg['l']
				isOF = False
				data = self.aggregate_record_process( i, seg['val'] )
				if '?' in seg['txt'] and  seg['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes:
					isOF = True
					if '?' in seg['txt'] and seg['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
						return None
					if seg['txt'].startswith('eot?'):
						if not seg['txt'] in self.aggregates.storage:
							self.aggregates.storage[ seg['txt'] ] = {}
						if not alpha in self.aggregates.storage[seg['txt']]:
							self.aggregates.storage[seg['txt']][alpha] = {}
							self.aggregates.storage[seg['txt']][alpha]['data'] = 0
							self.aggregates.storage[seg['txt']][alpha]['settings'] = {}
					if seg['txt'].startswith('eof?'):
						# print_( seg['txt'] ); sys.exit();
						if not seg['txt'] in __.aggregate.eof.storage:
							__.aggregate.eof.storage[ seg['txt'] ] = {}
						if not alpha in __.aggregate.eof.storage[seg['txt']]:
							__.aggregate.eof.storage[seg['txt']][alpha] = {}
							__.aggregate.eof.storage[seg['txt']][alpha]['data'] = 0
							__.aggregate.eof.storage[seg['txt']][alpha]['settings'] = {}
					
					
					# print_(isOF, seg['txt'])

				
					child = self.aggregates.index[ str(seg['val']) ]
					do = None
					if 'function' in child['l']:
						do = child['txt']


					if seg['txt'].startswith('eot?'):
						done = False
						if do == 'max':
							done = True;
							try:
								if data['data'] > self.aggregates.storage[seg['txt']][alpha]['data']:
									self.aggregates.storage[seg['txt']][alpha]['data'] = data['data']
							except Exception as e: cp('Error: max variable', 'red');

						if do == 'add':
							done = True;
							try:
								self.aggregates.storage[seg['txt']][alpha]['data'] += data['data']
							except Exception as e: cp('Error: add variable', 'red');

						
						if not done:
							self.aggregates.storage[seg['txt']][alpha]['data'] = data['data']
							
					elif seg['txt'].startswith('eof?'):
						done = False
						if do == 'max':
							done = True;
							try:
								if data['data'] > __.aggregate.eof.storage[seg['txt']][alpha]['data']:
									__.aggregate.eof.storage[seg['txt']][alpha]['data'] = data['data']
							except Exception as e: cp('Error: max variable', 'red');

						if do == 'add':
							done = True;
							try:
								__.aggregate.eof.storage[seg['txt']][alpha]['data'] += data['data']
							except Exception as e: cp('Error: add variable', 'red');
						
						if not done:
							__.aggregate.eof.storage[seg['txt']][alpha]['data'] = data['data']
				
				else:
					# print_( i, seg['txt'], data['data'] )
					self.asset[i][seg['txt']] = data['data']

					

					return data
				return { 'data': '' }
			if 'function' in seg['l']:
				###########################################################################################################
				if seg['txt'] == 'trigger':
					pass

				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'add':
					result = 0; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								try:
									result += float( d )
								except Exception as e: pass;
						else:
							try:
								result += float( v['data'] )
							except Exception as e: pass;
					if str(result).endswith('.0'):
						result = int(result)
					return { 'data': result }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'int':
					result = 0; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						nX = []
						if type(v['data']) == list:
							for d in v['data']:
								for cn in str(d):
									if cn in '0123456789.':
										nX.append(cn)
						else:
							for cn in str(v['data']):
								if cn in '0123456789.':
									nX.append(cn)
					
					try:
						result = float(''.join(nX))
					except Exception as e:
						nXj=[]
						for x99 in nX:nXj.append(str(x99))
						result = ''.join(nXj)
					if str(result).endswith('.0'):
						result = int(result)
					# print_(result)
					return { 'data': result }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'len':
					result = 0; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								# print_( 'len-d:', d )
								result += len( str( d ) )
						else:
							# print_( 'len-vd:', v['data'] )
							result += len( str( v['data'] ) )
					# print_( 'len-v', v )
					if str(result).endswith('.0'):
						result = int(result)
					return { 'data': result }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'max':
					result = []; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f ); 
					for d in v['data']:
						if '?date' in v['params']:
							try:
								ad = autoDate( d )
							except Exception as e: ad = 0;
							result.append(ad)
						else:
							try:
								ad = float( d )
							except Exception as e: ad = 0;
							result.append(ad)
					result.sort()
					result.reverse()

					return { 'data': result[0] }


				if seg['txt'] == 'config':
					result = []; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f ); 
					for par in v['params']:
						result.append(par)
					suffix = ''
					for par in result:
						suff = "['"+par+"']"
						suffix += suff
						try:
							eval( '__.aggregate.config'+suffix  )
						except Exception as e:
							exec( '__.aggregate.config'+suffix+' = { }'  )
					# printVarSimple(__.aggregate.config)
					# sys.exit()

				pass
				if seg['txt'] == 'format':
					result = []; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f ); 
					for par in v['params']:
						result.append(par)
					suffix = ''
					for par in result:
						suff = "['"+par+"']"
						suffix += suff
						# print_( 'suffix:', suffix )
						try:
							eval( '__.aggregate.format'+suffix  )
						except Exception as e:
							exec( '__.aggregate.format'+suffix+' = { }'  )



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'isDate':
					result = None; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								try:
									result = autoDate( d )
								except Exception as e: pass;
						else:
							try:
								result = autoDate( v['data'] )
							except Exception as e: pass;
					
					if not result is None:
						try:
							global _dir
						except Exception as e:
							pass
						if _dir is None:
							import _rightThumb._dir as _dir
						# print_( result )
						# self.asset[i]['month'] = _dir.getMonthFromEpoch( result )
						# self.asset[i]['year'] = _dir.getYearFromEpoch( result )
						# self.asset[i]['woy'] = _dir.getWeekAndYear( result )
						# self.asset[i]['dow'] = _dir.getDOWromEpochText( result )
						# self.asset[i]['ago'] = _dir.dateDiffText( result )
						self.asset[i] = isDate( result, self.asset[i] )
						
						# month year woy dow ago
						 

						month = _dir.getMonthFromEpoch
						# year = _dir.getYearFromEpoch
						# woy = _dir.getWOYFromEpoch
						# dow = _dir.getDOWromEpochText
						# ago = _dir.dateDiffText
					return { 'data': None }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'file':
					result = ''; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								try:
									result = d
								except Exception as e: pass;
						else:
							try:
								result = v['data']
							except Exception as e: pass;


					# global _dir
					if _dir is None:
						import _rightThumb._dir as _dir
					# info = _dir.info( _str.cleanBE( result, ' ' ).replace( '\t', '' ) )
					# print_( info )
					try:
						info = _dir.info( _str.cleanBE( result, ' ' ).replace( '\t', '' ) )
					except Exception as e:
						info = {
									"path": "",
									"name_": "",
									"name": "",
									"folder": "",
									"bytes": 0,
									"size": "",
									"date_created_raw": 0,
									"date_modified_raw": 0,
									"date_created": "",
									"date_modified": "",
									"type": "File",
									"typesort": 1,
									"ext": "txt",
									"week_of_year": "",
									"week_of_year_": 0,
									"day_of_the_week": "",
									"month": "",
									"friendly_week": "",
									"friendly_month": "",
									"md5": "",
									"year": 2021,
									"accessed_raw": 0,
									"date_accessed": "",
									"ce": 0,
									"me": 0,
									"ae": 0,
									"meta": {},
									"ago": "",
									"header": "",
									"error": 0
								}
					
					for k in info:
						if not k in self.asset[i]:
							self.asset[i][k] = info[k]

					return { 'data': result }




				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				###########################################################################################################



	def aggregateBuild( self ):
		if self.aggregate_processed:
			return None
		
		self.aggregate_processed = True


		a = ' '.join( switches.values('Aggregate') )
		# print_( a )

		
		self.aggregates = dot()

		
		self.aggregates.storage = {}
		self.aggregates.group_storage = {}
		# self.aggregates.segments = __.code.process( a, addString=[['alphaParam','?']] )
		# self.aggregates.segments = __.aggregate.data.records
		self.aggregates.segments = __.aggregate.obj.build( self.name, addSwitch=True )

		self.aggregates.index = {}

		self.aggregates.groups = {}
		self.aggregates.agroups = {}
		self.aggregates.agroupsADD = {}
		self.aggregates.columns = []
		for rec in self.aggregates.segments:
			self.aggregates.index[ str(rec['i']) ] = rec
			if rec['status'] and rec['l'] == 'variable':
				# if not rec['txt'].startswith('eot?'):
				# if not rec['txt'].startswith('eot?') and not rec['txt'].startswith('eof?') and not rec['txt'].startswith('eog?') and  not rec['txt'].startswith('bog?') and  not rec['txt'].lower().startswith('eoga?'):
				if not '?' in rec['txt'] or ( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					self.aggregates.columns.append( rec['txt'] )
					if not rec['txt'] in self.backup.allfields:
						self.backup.allfields[ rec['txt'] ] = rec['txt']
						self.backup.NGfields[ rec['txt'] ] = rec['txt']
		for rec in self.aggregates.segments:
			if rec['status'] and rec['l'] == 'variable':
				if not '?' in rec['txt'] or ( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					pass
				elif '?' in rec['txt'] and rec['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
				# elif 'g?' in rec['txt']:
					self.aggregates.agroups[ rec['i'] ] = rec
					
					try:
						gc = rec['txt'].split('?')[2]

					except Exception as e:
						cp( 'Error: aggregates, group split', 'red' )
						sys.exit()
					else:
						self.aggregates.columns.append( gc )
					if not gc in self.backup.allfields:
						self.backup.allfields[ rec['txt'] ] = gc

		# self.hasGroups

		pass
		# print_( self.aggregates.columns )
		# sys.exit()



		# sys.exit()
		# for x in segments:
		#   if x['status']:
		#       cp( x, 'green' )
		#   else:
		#       cp( x, 'cyan' )
		#       # print_( x )

		for i,record in enumerate(self.asset):
			self.aggregateRecord( i )


		# sys.exit()
		__.aggregate.storage = self.aggregates.storage
		return self.aggregates.columns


	def aggregateRecordGroups( self, i ):
		# print_()

		for seg in self.aggregates.segments:
			if seg['status']:
				# record = self.aggregate_record_process_group( i, seg['i'] )
				try:
					record = self.aggregate_record_process_group( i, seg['i'] )
				except Exception as ee:
					cp( 'Error: aggregate, group error', 'red' )
					cp( '\t expected:', 'yellow' )
					cp( '\t\t eog?level?group-len=add(len)', 'green' )
					print_()
					cp( [ 'Specifically:', ee ], 'red' )
					print_()
					sys.exit()




	def aggregateGroup( self ):
		# NOTE: reprocess after aggregates added        
		for ix in self.aggregates.agroups:
			seg = self.aggregates.agroups[ix]
			q = seg['txt'].split('?')
			subject = q[1]
			# print_( self.asset[0].keys() )
			# print_(subject); sys.exit();
			if subject in self.asset[0] and not subject in self.aggregates.groups:
				self.aggregates.groups[subject] = {}
				self.aggregates.groups[subject]['b'] = {}
				self.aggregates.groups[subject]['e'] = {}
				lastQ = ''
				lastID = -1
				for i,record in enumerate(self.asset):
					# print_(subject)
					if subject in record:
						# print_( record[subject] )
						if not record[subject] == lastQ:
							if not lastID == -1:
								self.aggregates.groups[subject]['b'][lastID] = i
								self.aggregates.groups[subject]['e'][i] = lastID
							lastQ = record[subject]
							lastID = i
				self.aggregates.groups[subject]['b'][lastID] = len(self.asset)-1
				self.aggregates.groups[subject]['e'][len(self.asset)-1] = lastID

		# if self.aggregates.groups:
		#   printVarSimple(self.aggregates.groups)
		#   print_( list( self.asset[0].keys() ) )
		#   sys.exit()

	def aggregate( self, script ):
		self.hasAggregate = True
		__.aggregate.obj.code( script, label=self.name )

	def aggregateBuildGroup( self ):
		self.aggregateGroup()
		for i,record in enumerate(self.asset):
			self.aggregateRecordGroups( i )

		if self.aggregates.agroupsADD:
			

			fields.register( self.groupID_KEY, 'val', 7, m=6 )
			test = fields.padZeros( self.groupID_KEY, 'val', 5 )
			newRecords = []
			for i,record in enumerate(self.asset):
				ii = str(i)
				ix = fields.padZeros( self.groupID_KEY, 'val', i )
				record[ self.groupID_KEY ] = ix + '-A'
				newRecords.append(record)
				if ii in self.aggregates.agroupsADD:
					rec = self.aggregates.agroupsADD[ii]
					rec[ self.groupID_KEY ] = ix + '-B'
					for k in self.backup.allfields:
						if not self.backup.allfields[k] in rec:
							rec[ self.backup.allfields[k] ] = ''
					newRecords.append(rec)
			self.asset = newRecords
	def print( self, column, fieldLengths=False, pc=None, printColumns=True, force=False, l=None, p=None ):
		global switches

		if switches.isActive('TableJSON'):
			if len(switches.value('TableJSON')):
				saveTable2( self.asset, switches.values('TableJSON')[0] )
				cp( [ 'saved:', switches.values('TableJSON')[0] ], 'green' )
			else:
				# printVarSimple(self.asset)
				print_( d2json(self.asset) )
			return None


		if not p is None:
			self.tab['table'] = p

		if not type(self.asset) == list or len(self.asset) == 0:
			print_('Null Set')
			sys.exit()




		if not force:
			if not switches.isActive('Help'):
				if switches.isActive('Column'):
					column = switches.value('Column')
					if column == '*' and self.asset:
						column = ','.join( list( self.asset[0].keys() ) )
			
				if switches.isActive('Sort'):
					self.asset = self.sort()
				elif switches.isActive('GroupBy'):
					
					switches.fieldSet('Sort','active',True)
					switches.fieldSet('Sort','value',switches.value('GroupBy'))
					self.asset = self.sort()

			pass
			__.aggregate.storage = {}
			__.aggregate.config = {}
			__.aggregate.format = {}
			__.aggregate.prefix = self.tab['table']+loopPrint(__.table_prefix_padding)
			if switches.isActive('Aggregate') or self.hasAggregate:
				aggregate_columns = self.aggregateBuild()
				if  type(aggregate_columns) == list:
					columns = column.split(',')
					for ac in aggregate_columns:
						if not ac in columns:
							columns.append(ac)
					column = ','.join(columns)
				__.aggregate.columns = columns

				shouldSortAgain = False
				if switches.isActive('Sort'):
					for sxy in switches.values('Sort'):
						if sxy in aggregate_columns:
							shouldSortAgain = True

					if shouldSortAgain:
						self.asset = self.sort()
				self.aggregateBuildGroup()
				for i,record in enumerate(self.asset):
					for c in record:
						nw = __.aggregate.obj.format( c, record[c] )
						if not nw == record[c]:
							self.asset[i][c] = nw
			pass
			for i,record in enumerate( self.asset ):
				for k in record:
					if record[k] is None:
						self.asset[i][k] = ''



		if self.webtable and switches.isActive('WebTable') and len(switches.value('WebTable')):
			asset = []
			for record in self.asset:
				rec = {}
				for k in column.split(','):
					rec[k] = record[k]
				asset.append(rec)
			saveTable( asset, 'web-tmp-'+switches.values('WebTable')[0]+'.json' )


		self.isExtraRecord = False
		if force:
			self.isWrap = True
		self.print_backup = {
								'column': column,
								'fieldLengths': fieldLengths,
								'pc': pc,
								'printColumns': printColumns,
		}
		self.isExtraRecord_0001 = {}
		self.isExtraRecord_000x = ''
		# print_('here',column)
		if not pc is None:
			printColumns = pc
		self.groupByTrigger()
		if type(fieldLengths) == dict:
			self.universalSpacing = fieldLengths
		# print_(column)
		# print_(self.assets)
		# rows = self.asset
		if not type(self.asset) == list or len(self.asset) == 0:
			print_('Null Set')
			sys.exit()
		global errors
		global switchDefault
		column = column.lower()
		columnSearch = column
		column = ''
		for cs in columnSearch.split(','):
			try:
				column += self.findColumName(cs.split('=')[0]) + ','
			except Exception as e:
				column += cs + ','
				# print_( 'Error: print column', cs )
				# sys.exit()
			# print_(cs.split('=')[0])
		column = _str.cleanBE(column,',')
		# print_(column)
		newData = []
		oldData = []
		if ':' in column or '=' in columnSearch:
			oldData = self.asset
		if ':' in column:
			depth = []
			flat = []
			for c in column.split(','):
				if not ':' in c:
					flat.append(c)
				else:
					try:
						found = False
						i=0
						for dp in depth:
							if depth[i]['parent'] == c.split(':')[0]:
								found = True
								dpID = i
							i+=1
					except Exception as e:
						found = False
					if found:
						depth[dpID]['children'].append(c.split(':')[1])
					else:
						depth.append({'parent': c.split(':')[0],'children': [c.split(':')[1]]})
			
			i = 0
			for data in self.asset:
				r = {}
				for f in flat:
					r[f] = data[f]
				x = []
				hasRecords = False
				for dp in depth:
					if len(data[dp['parent']]) > 0:
						hasRecords = True
						for dpi in data[dp['parent']]:
							y = {}
							hasData = False
							for dpic in dp['children']:
								try:
									if len(str(dpi[dpic])) > 1:
										hasData = True
								except Exception as e:
									pass
								try:
									y[str(dp['parent']) + ':' + str(dpic)] = dpi[dpic]
								except Exception as e:
									pass
							for f in flat:
								y[f] = r[f]
							if hasData:
								newData.append(y)
				if not hasRecords:
					for dpi in data[dp['parent']]:
						for dpic in dp['children']:
							r[str(dp['parent']) + ':' + str(dpic)] = ''
					newData.append(r)
				i+=1
			self.asset = newData
			# print_(newData)
			# print_('dasfdasdfasdfadsf')


		newData = []
		if '=' in columnSearch:
			for data in self.asset:
				rowInclude = True
				for c in columnSearch.split(','):
					if rowInclude:
						if '=' in c:
							cc = c.split('=')
							string = data[cc[0]]
							string = _str.cleanBE(string.lower(),' ')
							cc[1] = _str.cleanBE(cc[1],' ')
							try:
								dataYes = _str.cleanBE(cc[1].split('-')[0],' ')
							except Exception as e:
								dataYes = ''
							try:
								dataNo = _str.cleanBE(cc[1].split('-')[1],' ')
							except Exception as e:
								dataNo = ''
							if len(dataYes) > 0:
								# print_('IS')
								# print_(dataYes)
								length = 0

								for s in dataYes.split(' '):
									if rowInclude:
										rowInclude = False
										if len(s) > 0:
											length += 1
											# print_(string)
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
													rowInclude = True
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													# print_(s,string)
													cnt += 1
													rowInclude = True
											elif s in string:
												cnt += 1
												rowInclude = True
								# print_(length,cnt)
								# if length == cnt:
								# if cnt > 0:
									# rowInclude = True
										# if switches.isActive('PlusOr') == True:
										#   if cnt > 0:
										#       rowInclude = True
							if len(dataNo) > 0 and rowInclude:
								# print_('ISNOT')
								rowInclude = True
								try:
									for s in dataNo.split(' '):
										if len(s) > 0:
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													cnt += 1
											elif not string.find(ci(s)) == -1:
												cnt += 1
											# if not string.find(ci(s)) == -1:
											if cnt > 0:
												rowInclude = False
												break
								except Exception as e:
									pass
				if rowInclude:
					newData.append(data)
			self.asset = newData
			# print_(self.asset)





		# if not len(groupByList):


		# if not column == False:
			# switches.fieldSet('Column','value',column)
			# column = switches.value('Column')

		# print_('-',column)
		columnHeader = self.showColumnHeader(column)
		columnHeaderLength = len(columnHeader)
		# print_(columnHeader)


		self.groupByList = {}
		try:
			for gb in switches.value('GroupBy').split(','):
				self.groupByList[str(gb)] = ''
		except Exception as e:
			pass



		if not force and not switches.isActive('NoWrapTable'):

			if __.terminal.width:
				maxSize = 0
				i=0
				for item in self.asset:
					result = ''
					for c in column.split(','):
						try:
							result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
						except Exception as e:
							pass
					# print_(result)
					maxSize = len(result)+self.prefixSize()
					i+=1


				# print_( maxSize )
				if maxSize > __.terminal.width and not switches.isActive('NoWrapTable'):
					self.wrapTable(__.terminal.width)
					# print_( 'error' )
					# sys.exit()
					return None


		pass
		self.groupByList = {}
		try:
			for gb in switches.value('GroupBy').split(','):
				self.groupByList[str(gb)] = ''
		except Exception as e:
			pass


		if printColumns:
			if switches.isActive('YesTableLines'):
				columnHeader = self.tab['table']+loopPrint(__.table_prefix_padding) + columnHeader
			else:
				columnHeader = self.tab['table']+loopPrint(__.table_prefix_padding) + columnHeader.replace( '\n', '' )
			print_()
			printBold( columnHeader )
			# printBold( columnHeader, prefix=self.tab['header'] )
			if not len(switches.value('YesTableLines')):
				print_()
		i = 0
		# print_(self.asset)
		self.isExtraRecord_0001 = {}
		self.isExtraRecord_000x = ''
		tableLine = __.tableLine
		if switches.isActive('YesTableLines'):
			tableLine = '|'

		if l is None:
			if switches.isActive('NoTableLines'):
				tableLine = ''
		elif not l:
			tableLine = ''

		for item in self.asset:
			# print_(item)
			result = ''
			for c in column.split(','):
				try:
					pass
					# result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					pass
				# print_(result)
				self.isExtraRecord = False
				
				
				# if self.wrapTableKey+'-sort' in item:
					# print_(  item[self.wrapTableKey+'-sort']  )
					# print_(    )

				if self.wrapTableKey+'-sort' in item:
					self.isExtraRecord_000x = item[self.wrapTableKey+'-sort']

				if self.wrapTableKey+'-sort' in item and not item[self.wrapTableKey+'-sort'].endswith('-0001'):
					self.isExtraRecord = True
				try:
					pass
					result += self.showColumn(c,i,columnHeaderLength) + self.columnTab+tableLine
				except Exception as e:
					errors.append({'id': 12, 'function': 'print()', 'cnt': 1, 'location': "result += showColumn(rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': 'folder'}, {'name': 'column', 'value': column}], 'error': e})
					printBold('Error:','red')
					printBold('\tBad column input.')
					print_(12)
					print_(c)
					print_(12)
					os._exit(0)
			# print_(_str.totalStrip5(result)) #TESTING
			
			maxSize = len(result)+self.prefixSize()
			if maxSize > __.terminal.width and not switches.isActive('NoWrapTable'):
				ToDo = " result = ''   "
				ToDo = ' for sult in self.wrapTable2(i):  '
				ToDo = '     result += sult  '
			else:
				ToDo = ' the below if will be under this else '

			if len(result) > 0:
				# print_(result)
				shouldPrint = True
				if self.isExtraRecord_000x.split('-')[0] in self.isExtraRecord_0001:
					testResult = result
					testResult = testResult.replace( ' ', '' ).replace( '\t', '' )
					if not len(testResult):
						shouldPrint = False
				# if self.isExtraRecord:
				#   print_( self.isExtraRecord )

				if shouldPrint:
					if self.groupID_KEY in item and item[self.groupID_KEY].endswith('-B'):
						cp( [ self.tab['table']+loopPrint(__.table_prefix_padding) + result ], 'BackgroundGrey.blue' )
					else:
						colorizeRow( tableLine+result, prefix=self.tab['table']+loopPrint(__.table_prefix_padding), prefixColor=self.tab_color, haltColorShift=self.isExtraRecord )
			i += 1
			if 'expected_input_example' in column and 'switch' in column and  switchDefault == i:
				# if '??' in __.switch_skimmer.active:
				if __.switch_skimmer.active:
					sys.exit()
				pass
				print_('')
		# if len(oldData) > 0:
		#   self.asset = oldData
		self.asset = self.backup.asset.copy()
		self.aggregate_processed = False
		# print_( 'recovered' )


		footer = {}
		aSettings = {}
		for k in __.aggregate.storage:
			if k.startswith('eot?'):
				f = k[len('eot?'):]
				for y in __.aggregate.storage[k]:
					for sv in __.aggregate.storage[k][y]['settings']:
						aSettings[sv] = __.aggregate.storage[k][y]['settings'][sv]

					if '?date' in __.aggregate.storage[k][y]['settings']:
						__.aggregate.storage[k][y]['data'] = friendlyDate( __.aggregate.storage[k][y]['data'] )
					theKey = f 
					special = {}

					kk = k
					var = 'var'
					if 'var' in __.aggregate.config:
						var = 'var'
					if '?var' in __.aggregate.config:
						var = '?var'
					if 'var?' in __.aggregate.config:
						var = 'var?'

					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
					kk = '?all'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'all?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'eot?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
						

					if '?fl' in special:
						theKey = f + ' '+ y
					if '?first' in special:
						theKey = f
					elif '?second' in special:
						theKey = y


					# for fo in __.aggregate.format:
					#   if fo == k or fo == y:
					#       if '?date' in __.aggregate.format[fo]:
					#           __.aggregate.storage[k][y]['data'] = friendlyDate( __.aggregate.storage[k][y]['data'] )
					#       if '?comma' in __.aggregate.format[fo]:
					#           __.aggregate.storage[k][y]['data'] = addComma( __.aggregate.storage[k][y]['data'] )
					# # print_(  )
					# footer[ theKey ] = __.aggregate.storage[k][y]['data']
					footer[ theKey ] = __.aggregate.obj.format( [k,y], __.aggregate.storage[k][y]['data'] )
		if footer:
			print_()
			# print_()
			footer_txt = []
			footer_txt.append( __.aggregate.prefix )

			for k in footer:
				footer_txt.append( k+':' ) 
				footer_txt.append( footer[k] ) 
				footer_txt.append( '  ' )
			cp( footer_txt, 'cyan' ) 
			# print_( __.aggregate.config )
			print_()
					# print_( f, y, __.aggregate.storage[k][y]['data'] )
			# print_( k )
			# sys.exit()

	def sort(self,fields=''):# sortThis  
		rows = self.asset

		if not len(self.asset):
			return None

		if self.wrapTableKey+'-sort' in self.asset[0]:
			return rows
		

		global errors
		global switches
		# self.sort = name
		tempFields = []
		delim = ':'
		if fields == '':
			name = switches.value('Sort')
		else:
			name = fields
		name = name.replace(':',delim)
		# if not name:
		sortBy = {}
		sortList = name.split(',')
		sortList.reverse()

		### Check for bad sort input
		for item in sortList:
			item = item
			try:
				if item.count(delim) > 0:
					sb = item.split(delim)[1]
				else:
					sb = item
			except Exception as e:
				errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})

		# itemgetter = __.imp('operator.itemgetter')
		for item in sortList:
			try:
				direction = item.split(delim)[0]
				sb = self.findColumName(item.split(delim)[1])
				if 'a' in direction:
				# if direction.find('a') == 0:
					self.asset = sorted(self.asset, key=itemgetter(sb))
				else:
					self.asset = sorted(self.asset, key=itemgetter(sb), reverse=True)
			except Exception as e:
				try:
					pass
					self.asset = sorted(self.asset, key=itemgetter(self.findColumName(item)))
				except Exception as e:
					errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
				
			uuid = __.imp('uuid')
			sortBy[item] = str(uuid.uuid4())
			tempFields.append( sortBy[item] )
			i = 0
			for row in self.asset:
				self.asset[i][sortBy[item]] = i
				i += 1

		# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

		sortCode = 'rows = sorted(rows, key=lambda d: ('
		for item in sortList:
			sortCode += "d['" + str(sortBy[item]) + "'],"
		sortCode = sortCode[:-1]
		sortCode += '))'
		exec(sortCode)
		if len( tempFields ):
			# print_( tempFields )
			for ix,r in enumerate(rows):
				for tmp in tempFields:
					try:
						del rows[ix][tmp]
					except Exception as e:
						pass
		return self.asset

	def countThis(self):
		rows = self.asset
		i = 0
		for x in self.asset:
			i += 1
		return i

	def file(self,file):
		self.file = file

	def save(self,theFile = '',tableTemp = True,printThis = True, me=0):
		HD.chmod(theFile)
		simplejson = __.imp('simplejson')
		if theFile == '':
			theFile = str(self.file)
		self.file = theFile
		# print_(theFile)
	# def saveTable(rows,theFile,tableTemp = True,printThis = True):
		# defaults to myTables
		if tableTemp == True:
			file0 = str(_v.myTables) + str(_v.slash) + str(theFile)
		else:
			file0 = _v.stmp + _v.slash + theFile
		dataDump = simplejson.dumps(self.asset, indent=4, sort_keys=True, default=str)
		f = open(file0,'w')
		f.write(str(dataDump))
		f.close()
		HD.chmod(theFile)
		if printThis:
			print_('Saved: ' + file0)
		if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );
	def get(self,theFile = '',tableTemp = True,printThis = False):
		if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
		simplejson = __.imp('simplejson')
		if theFile == '':
			theFile = self.file
		self.file = theFile
		# defaults to myTables
		if tableTemp == True:
			file0 = _v.myTables + _v.slash + theFile
		else:
			file0 = _v.stmp + _v.slash + theFile
		if printThis:
			print_('Loaded: ' + file0)
		if os.path.isfile(file0) == True:
			with open(file0,'r', encoding="latin-1") as json_file:
				json_data = simplejson.load(json_file)
				# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		else:
			json_data = []
		self.asset = json_data
		return json_data

	def assets(self):
		return self.asset

	def set(self,asset):
		self.asset = asset
		return self.asset

	def groupByTrigger( self ):
		try:
			if switches.isActive('GroupBy') and len(self.asset):
				newValues = []
				keys = []
				for key in self.asset[0].keys():
					keys.append( key )
				for val in switches.value('GroupBy').split( ',' ):
					for key in keys:
						if key.lower() == val.lower():
							newValues.append( key )
				if len(newValues):
					switches.fieldSet( 'GroupBy', 'value', ','.join(newValues) )
		except Exception as e:
			pass



class Tables:

	def __init__(self):
		self.tables = []
		self.index = {}
		self.maxNameLength = 35
		self.columnTab = '\t'
		self.groupSeparator = '_'
		self.group_space = False



	def aggregate( self, name=None, code=None ):
		if code is None:
			return None
		if name is None:
			name = self.tables[ len(self.tables)-1 ].name
		
		self.tables[ self.index[name] ].aggregate( code )


	def rprint( self, asset, columns=None, name=None, n=None, sc=True, printColumns=True, h=None, l=None, p=None ):
		if columns is None:
			columns = ','.join(list(asset[0].keys()))
		

		if not h is None:
			printColumns = h
		if not n is None:
			name = n
		if name is None:
			name = genUUID()
		self.register( name, asset )
		if sc and switches.isActive('Column'):
			columns = switches.value('Column')
		self.print( name, columns, printColumns=printColumns, l=l, p=p )



	def rsort( self, asset, columns, name=None, n=None ):
		if not n is None:
			name = n
		if name is None:
			name = genUUID()
		self.register( name, asset )
		return self.returnSorted( name,columns,asset )
		# return self.sort( name, columns )


	def register( self, name=None, asset = [], group_space=True, tab='',    gs=None, t=None, n=None, w=True ):
		global TableProfile_Config
		if not n is None:
			name = n
		if name is None:
			name = genUUID()
		if not __.table_b_print:
			for i,record in enumerate(asset):
				for field in record.keys():
					if str( record[field] ) == 'b':
						asset[i][field] = ''


		found = False
		thisID = False
		if not gs is None:
			group_space = gs
		elif 'ALLTABLES' in TableProfile_Config.keys() and 'GroupSpaces' in TableProfile_Config['ALLTABLES'].keys():
			group_space = TableProfile_Config['ALLTABLES']['GroupSpaces']
		else:
			group_space = switches.isActive('GroupSpaces')
		if not t is None:
			tab = t
		for i,t in enumerate(self.tables):
			if t.name == name:
				thisID = i
				found = True
				self.tables[i].maxNameLength = self.maxNameLength
				if len(asset) > 0:
					self.tables[i].set(asset)
		if found:
			self.tables.pop( thisID )
			found = False

		if not found:
			self.tables.append(Table( name, asset, group_space, tab, w ))
			self.tables[ len( self.tables )-1 ].maxNameLength = self.maxNameLength
			self.index[name] = len( self.tables )-1
		return name

	def trigger(self,name,field,script,includes = False):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].trigger(field,script,includes)
			i += 1

	def registerView(self,table,name,fields,sort):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].registerView(name,fields,sort)
			i += 1

	def fieldProfileSet(self,table,field,propertyName,value):
		i = 0
		found = False
		for t in self.tables:
			if t.name == table:
				found = True
				self.tables[i].fieldProfileSet(field,propertyName,value)
			i += 1
		if not found:
			self.tables.append(Table(table,[]))
			i = 0
			for t in self.tables:
				if t.name == table:
					self.tables[i].fieldProfileSet(field,propertyName,value)
				i += 1

	def print(self,name,fields,fieldLengths=False, pc=None, printColumns=True, h=None, l=None, p=None ):
		if not h is None:
			printColumns = h
		global switches
		if not ',' in fields:
			pc = False

		xXx = switches.records('dic_on-off-v')
		if 'Sort' in xXx['on']:
			sortBy = xXx['values']['Sort']
			self.sort( name, ','.join( sortBy ) )
			# print_( sortBy )
			# sys.exit()
		if not pc is None:
			printColumns = pc
		# print_(name,fields)
		sI = None
		i = 0
		for t in self.tables:
			if t.name == name:
				if len(self.tables[i].asset) > 0:
					if not ',' in fields:
						printColumns = False
					self.tables[i].print(fields,fieldLengths,printColumns=printColumns, l=l, p=p)
					sI = i
				else:
					print_('Null Set')
			i += 1
		if switches.isActive('FieldTotal'):
			fieldTotals = {}
			for field in switches.values('FieldTotal'):
				fieldTotals[field] = { 'actual': None, 'total': 0 }
				for rec in self.tables[sI].asset:
					for key in rec.keys():
						if check_field_match( key, field ):
							fieldTotals[field]['actual'] = key
							thisFieldA = str(rec[key])
							thisFieldB = []
							for char in thisFieldA:
								if char in '0123456789':
									thisFieldB.append(char)
							thisFieldC = int(''.join(thisFieldB))
							fieldTotals[field]['total'] += thisFieldC
			print_()
			print_()
			for field in fieldTotals:
				print_( addComma(fieldTotals[field]['total']),'\t', fieldTotals[field]['actual'] )




	def sort(self,name,fields):
		fields = fields.replace('.',':')
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
			i += 1

	def returnSorted(self,name,fields,asset = []):
		fields = fields.replace('.',':')
		if len(asset) > 0:
			self.register(name,asset)

		result = []
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
				result = self.tables[i].asset
			i += 1
		return result
	def view(self,table,name):
		i = 0
		for t in self.tables:
			if t.name == table:
				try:
					self.tables[i].printView(name)
				except Exception as e:
					pass
			i += 1

	def save(self,table,theFile = '',tableTemp = True,printThis = True, me=0):
		HD.chmod(theFile)
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].save(theFile,tableTemp,printThis)
			i += 1
		HD.chmod(theFile)
		if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );

	def get(self,table,theFile = '',tableTemp = True,printThis = False):
		if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].get(theFile,tableTemp,printThis)
			i += 1

	def asset(self,table):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].assets()
			i += 1

	def file(self,table,theFile):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].file(theFile)
			i += 1

	def set(self,table,asset):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].set(asset)
			i += 1

	def alignmentMasterSupersedes(self,table,value):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].tableProfileDefaultSupersedes = value
			i += 1
		
	def getLength(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		total = 0
		for r in result.keys():
			total += result[r]
			total += 5
		# print_(result)
		return total

	def getFieldLengths(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		###### How it works:
		# totalColumnWidth = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   spaces = tables.getLength(m['table'],'type,field,max,min,average')
		#   if spaces > totalColumnWidth:
		#       totalColumnWidth = spaces


		# fieldLengths = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#   if not type(fieldLengths) == dict:
		#       fieldLengths = data
		#   for name in fieldLengths.keys():
		#       if data[name] > fieldLengths[name]:
		#           fieldLengths[name] = data[name]



		# for m in self.meta['data']:
		#   genLine(totalColumnWidth,'=')
		#   print_('Table:\t',m['table'])
		#   print_('Parent:\t',m['parent'])
		#   print_('Records:',m['count'])
		#   print_()
		#   tables.register(m['table'],m['fields'])
		#   tables.fieldProfileSet(m['table'],'*','alignment','center')
		#   tables.print(m['table'],'type,field,max,min,average',fieldLengths)

		#   genLine(totalColumnWidth,'=')
		# print_()
		# print_('Records:',self.meta['records'])
		# print_()
		# print_('Errors:')
		# for e in self.meta['errors']:
		#   print_('\t',e)

		return result



	def eof( self ):
		try:
			__.aggregate.eof.storage
		except Exception as e:
			shouldPrint = False
		else:
			shouldPrint = True

		if not __.aggregate.eof.storage:
			shouldPrint = False

		if shouldPrint:
			print_()
			print_()

			linePrint()

			# print_()
			# printVarSimple( __.aggregate.eof.storage )


		footer = {}
		aSettings = {}

		for k in __.aggregate.eof.storage:
			if k.startswith('eof?'):
				f = k[len('eof?'):]
				for y in __.aggregate.eof.storage[k]:
					for sv in __.aggregate.eof.storage[k][y]['settings']:
						aSettings[sv] = __.aggregate.eof.storage[k][y]['settings'][sv]

					if '?date' in __.aggregate.eof.storage[k][y]['settings']:
						__.aggregate.eof.storage[k][y]['data'] = friendlyDate( __.aggregate.eof.storage[k][y]['data'] )
					theKey = f +' '+ y
					special = {}

					kk = k
					var = 'var'
					if 'var' in __.aggregate.config:
						var = 'var'
					if '?var' in __.aggregate.config:
						var = '?var'
					if 'var?' in __.aggregate.config:
						var = 'var?'

					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
					kk = '?all'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'all?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'eof?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
						

					if '?first' in special:
						theKey = f
					elif '?second' in special:
						theKey = y

					# print_( 'format:', __.aggregate.format )
					# print_( 'k y:', k, y  )

					# for fo in __.aggregate.format:
					#   if fo == k or fo == y:
					#       if '?date' in __.aggregate.format[fo]:
					#           __.aggregate.eof.storage[k][y]['data'] = friendlyDate( __.aggregate.eof.storage[k][y]['data'] )
					#       if '?comma' in __.aggregate.format[fo]:
					#           __.aggregate.eof.storage[k][y]['data'] = addComma( __.aggregate.eof.storage[k][y]['data'] )



					# # print_(  )
					# footer[ theKey ] = __.aggregate.eof.storage[k][y]['data']
					footer[ theKey ] = __.aggregate.obj.format( [k,y], __.aggregate.eof.storage[k][y]['data'] )
		if footer:
			print_()
			# print_()
			footer_txt = []
			footer_txt.append( __.aggregate.prefix )

			for k in footer:
				footer_txt.append( k+':' ) 
				footer_txt.append( footer[k] ) 
				footer_txt.append( '  ' )
			cp( footer_txt, 'cyan' ) 
			# print_( __.aggregate.config )
			print_()
					# print_( f, y, __.aggregate.storage[k][y]['data'] )
			# print_( k )






###########################################################################################
def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()
	return hash_md5.hexdigest()


def formatSize(size,what=None):
	try:
		size = int(size)
	except Exception as e:
		size = float(size)
	result = ''
	if what is None:

		if size == None:
			result = ''
		elif size < 1024:
			result = str(size) + ' B'
		elif size >= 1024 and size < 1048576:
			num = round(size / 1024, 2)
			result = str(num) + ' KB'
		elif size >= 1048576 and size < 1073741824:
			num = round(size / 1048576, 2)
			result = str(num) + ' MB'
		elif size >= 1073741824 and size < 1099511627776 :
			num = round(size / 1073741824, 2)
			result = str(num) + ' GB'
		elif size >= 1099511627776 and size < 1125899906842624 :
			num = round(size / 1099511627776, 2)
			result = str(num) + ' TB'
		elif size >= 1125899906842624 and size < 1152921504606847000 :
			num = round(size / 1125899906842624, 2)
			result = str(num) + ' PB'
		elif size >= 1152921504606847000 and size < 1180591620717411303424 :
			num = round(size / 1152921504606847000, 2)
			result = str(num) + ' EB'
		elif size >= 1180591620717411303424 and size < 1208925819614629174706176 :
			num = round(size / 1180591620717411303424, 2)
			result = str(num) + ' ZB'
		else:
			num = round(size / 1208925819614629174706176, 2)
			result = str(num) + ' YB'
	
	elif not what is None:
		what=what.upper()
		if size == None:
			result = ''
		elif what == 'B':
			result = str(size) + ' B'
		elif what == 'KB':
			num = size / 1024
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' KB'
		elif what == 'MB':
			num = size / 1048576
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' MB'
		elif what == 'GB':
			num = size / 1073741824
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' GB'
		elif what == 'TB':
			num = size / 1099511627776
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' TB'
		elif what == 'PB':
			num = size / 1125899906842624
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' PB'
		elif what == 'EB':
			num = size / 1152921504606847000
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)         
			result = str(num) + ' EB'
		elif what == 'ZB':
			num = size/1180591620717411303424
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' ZB'
		elif what == 'YB':
			num = size / 1208925819614629174706176
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' YB'
		else:
			result = str(size) + ' B'
	return result

def unFormatSize(size):
	size = str(size)
	size = size.upper()
	factor = ''
	# 1152921504606846976
	if False:
		pass



	elif 'YB' in size:
		factor = 1208925819614629174706176
	elif 'ZB' in size:
		factor = 1180591620717411303424
	elif 'EB' in size:
		factor = 1152921504606847000
	elif 'PB' in size:
		factor = 1125899906842624
	elif 'TB' in size:
		factor = 1099511627776
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024

	else:
		factor = 1
	size2 = ''
	for c in size:
		if c in '0123456789.':
			size2+=c
	size = size2
	# size = size.replace('X','')
	# size = size.replace('Y','')
	# size = size.replace('Z','')
	# size = size.replace('E','')
	# size = size.replace('P','')
	# size = size.replace('T','')
	# size = size.replace('B','')
	# size = size.replace('M','')
	# size = size.replace('K','')
	# size = size.replace('G','')
	size = float(size)
	if str(size).endswith('.0'):
		size = int(size)

	result = round(size * factor,0)
	# print_( size, factor )
	# result = size * factor
	return result

def unFormatSize2(size):
	size = str(size)
	# size = size.upper()
	factor = ''
	# 1152921504606846976

	bity=False
	if False:
		pass



	elif 'YB' in size or 'yB' in size:
		factor = 1208925819614629174706176
	elif 'ZB' in size or 'zB' in size:
		factor = 1180591620717411303424
	elif 'EB' in size or 'eB' in size:
		factor = 1152921504606847000
	elif 'PB' in size or 'pB' in size:
		factor = 1125899906842624
	elif 'TB' in size or 'tB' in size:
		factor = 1099511627776
	elif 'GB' in size or 'gB' in size:
		factor = 1073741824
	elif 'MB' in size or 'mB' in size:
		factor = 1048576
	elif 'KB' in size or 'kB' in size:
		factor = 1024




	elif 'Yb' in size or 'yb' in size or 'ybit' in size.lower():
		bity=True
		factor = 1000000000000000000000000
	elif 'Zb' in size or 'zb' in size or 'zbit' in size.lower():
		bity=True
		factor = 1000000000000000000000
	elif 'Eb' in size or 'eb' in size or 'ebit' in size.lower():
		bity=True
		factor = 1000000000000000000
	elif 'Pb' in size or 'pb' in size or 'pbit' in size.lower():
		bity=True
		factor = 1000000000000000
	elif 'Tb' in size or 'tb' in size or 'tbit' in size.lower():
		bity=True
		factor = 1000000000000
	elif 'Gb' in size or 'gb' in size or 'gbit' in size.lower():
		bity=True
		factor = 1000000000
	elif 'Mb' in size or 'mb' in size or 'mbit' in size.lower():
		bity=True
		factor = 1000000
	elif 'Kb' in size or 'kb' in size or 'kbit' in size.lower():
		bity=True
		factor = 1000

	else:
		factor = 1
	size2 = ''
	for c in size:
		if c in '0123456789.':
			size2+=c
	size = size2
	# size = size.replace('X','')
	# size = size.replace('Y','')
	# size = size.replace('Z','')
	# size = size.replace('E','')
	# size = size.replace('P','')
	# size = size.replace('T','')
	# size = size.replace('B','')
	# size = size.replace('M','')
	# size = size.replace('K','')
	# size = size.replace('G','')
	size = float(size)
	if str(size).endswith('.0'):
		size = int(size)

	result = round(size * factor,0)
	if 0 and bity:
		result = result /8
	# print_( size, factor )
	# result = size * factor
	rt = str(result)
	if rt.endswith('.0'):
		return int(result)
	return result
isTime = False

timeAgoBase = []
timeAgoBaseCount = 0
def timeAgo( do='', startDate=None,epoch=None, d=None ):
	if do == 'm': do = 'md'
	if do == 'c': do = 'cd'
	if do == 'md' or do == 'cd': return do
	new=timeAgo22( do, startDate,epoch, d )

	return new

def timeAgo22( do='', startDate=None,epoch=None, d=None ):
	if not epoch is None:
		startDate = epoch
	if not d is None:
		startDate = d

	try:
		do = float(do)
		return do
	except Exception as e:
		pass

	global timeAgoBase
	global timeAgoBaseCount
	if not len(timeAgoBase) and timeAgoBaseCount == 0:
		if ',' in do:
			timeAgoBase = do.split(',')
			# print_(do)
			# sys.exit()
	timeAgoBaseCount += 1
	# print_( do, friendlyDate(startDate) )
	if len(do) == 19 and do.count('-') == 2 and do.count(':') == 2:
		return autoDate( do )
	if len(do) == 16 and do.count('-') == 2 and do.count(':') == 1:
		return autoDate( do )
	if len(do) == 21 and do.count('-') == 4:
		result = []
		for x in do.split(','):
			result.append( timeAgo( x, startDate ) )
			# result.append( timeAgo_do( x, startDate ) )
		return result
	if len(do) == 10 and do.count('-') == 2:
		ts = autoDate( do )
	else:
		# ts = timeAgo_do( do, startDate)
		if not do.startswith('+'):
			ts = timeAgo_past(do,startDate)
		elif do.startswith('+'):
			ts = timeFuture(do,startDate)


	if len(timeAgoBase) > 1 and do == timeAgoBase[1]:
		if timeAgoBaseCount == 3 or timeAgoBaseCount == 5 :
			try: ts += 86400-1
			except Exception as ee: pass
	# print_( timeAgoBaseCount, ts )
	return ts

def timeCalc(do, epoch=None):
	global epoch_times_dic
	et=epoch_times_dic
	k=list(et.keys())
	k.reverse()
	for t in et:
		do=do.replace(t,t+',')
		do=_str.do('be',do,',')
	print_(do)
	sys.exit()
	if epoch is None:
		epoch = time.time()


def timeAgo_past(do='', startDate=None):
	if startDate is None:
		startDate  = time.time()
	# start_date = isDate(startDate,f='date')
	# start_date = [time.time()]
	global isTime
	# return do
	if '.' in do:
		dos = do.split('.')
		e = timeAgo( dos[0], startDate )
		# return e
		for di,ds in enumerate(dos):
			if di:
				e = timeAgo( dos[di], e )
		return e
	if do.startswith('-'):
		do = do[1:]
	if do is None:
		colorThis( '\t Error: Ago is Missing parameters', 'red' )
		sys.exit()
	if type(do) == float:
		return do
	if do.lower() == 'r':
		return 'resent'
	if 're' in do.lower():
		return 'resent'
	if 'a' in do.lower():
		return 'a'
	if 'cd' in do:
		return do.lower()
	if 'md' in do:
		return do.lower()
	if 'mod' in do.lower():
		return 'md'
	if 'crea' in do.lower():
		return 'cd'
	if 'o' in do.lower():
		return 'one'

	if len(do) == 0:
		do = switches.value('Ago')
	do = do.lower()

	if 't' in do:
		one = resolveEpochTest( startDate )
		two = autoDate( one.split(' ')[0] )
		return two
	if isTime:
		if 'm' in do:
			each = 60
			units = do
			units = units.replace( 'm', '' )
			units = int( units )
			remove = units * each
			return startDate - remove  
	if 'mm' in do or 'min' in do:
		each = 60
		units = do
		units = units.replace( 'min', '' )
		units = units.replace( 'm', '' )
		units = int( units )
		remove = units * each
		return startDate - remove  

	if 'h' in do:
		each = 3600
		units = do
		units = units.replace( 'h', '' )
		units = int( units )
		remove = units * each
		return startDate - remove  


	fnd = 'ymwd'
	nmb = do
	for t in fnd:
		nmb = nmb.replace(t,'')
	if len(nmb) == 0:
		nmb = 1
	try:
		nmb = int(nmb)
	except Exception as e:
		nmb = 1
	if 'y' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-365 * nmb)
		# start_date = dateMathEpoch( startDate, 365 * nmb, '-' )
		return yearMath( startDate, nmb, do='-' )
	if 'm' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-30 * nmb)
		# start_date = dateMathEpoch( startDate, 30 * nmb, '-' )
		return monthMath( startDate, nmb, do='-' )

		print('asdf',start_date)
	if 'w' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-7 * nmb)
		return dateMathEpoch( startDate, 7 * nmb, '-' )
	if 'd' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-1 * nmb)
		return dateMathEpoch( startDate, nmb, '-' )
	return time.time()
	# dTx = str(start_date)
	# print_(dT)
	# print_(dT)
	# print_(dT)
	# print_(dT)
	# d = dTx.split('-')
	# result = datetime.datetime(int(d[0]),int(d[1]),int(d[2]),0,0).timestamp()

	# print_(start_date)
	# print_(result)]
	# print_(result)
	# return result

def epoch_math(epoch, d=None,w=None,m=None,y=None,    h=None,mm=None,s=None, add=None, sub=None):
	if add is None and sub is None: add=True;
	if sub: add = False;


	def em_years(sourcedate, years, add=None):
		if add: years_to_add = sourcedate.year + years;
		if not add: years_to_add = sourcedate.year - years;
		return sourcedate.replace(year=years_to_add)

	def em_months(sourcedate, months, add=None):
		from dateutil.relativedelta import relativedelta
		if add: return sourcedate + relativedelta(months=months);
		if not add: return sourcedate - relativedelta(months=months);

	orig = datetime.datetime.fromtimestamp(epoch)

	if add:
		if not w is None: orig = orig + datetime.timedelta(days=w*7);
		if not d is None: orig = orig + datetime.timedelta(days=d);
	else:
		if not w is None: orig = orig - datetime.timedelta(days=w*7);
		if not d is None: orig = orig - datetime.timedelta(days=d);

	if not m is None: orig = em_months(orig, m, add);
	if not y is None: orig = em_years(orig, y, add);
	epoch = orig.timestamp()

	if add:
		if not h is None: epoch+=(h*3600);
		if not mm is None: epoch+=(mm*60);
		if not s is None: epoch+=s;
	else:
		if not h is None: epoch-=(h*3600);
		if not mm is None: epoch-=(mm*60);
		if not s is None: epoch-=s;

	return epoch

def timeAgo_do( do, epoch):
	# print_(do)
	def d486(yolo):
		return int(yolo)
		return float(yolo)

	dic={}
	if not do:
		return do
	
	add=False
	builder=''
	i=-1
	while True:
		i+=1
		try:
			c=do[i]
		except Exception as e:
			return epoch
		if c == '+' or c == '-':
			builder=''
			if c == '+':
				add=True
			elif c == '-':
				add=False
		elif c in '0123456789.':
			builder+=c
		elif c == 'm':
			ghost=False
			try:
				if do[i+1] == 'i' and do[i+2] == 'n': ghost=True;
			except Exception as e:
				pass
			if ghost:
				i+=2
				epoch = epoch_math(epoch, mm=d486(builder), add=add)

			else:
				epoch = epoch_math(epoch, m=d486(builder), add=add)
			builder=''
		elif c == 'y': epoch = epoch_math(epoch, y=d486(builder), add=add); builder='';
		elif c == 's': epoch += s; builder='';
	return epoch









def timeFuture(do='', startDate=None):
	if startDate is None:
		startDate = time.time()
	global isTime

	if '.' in do:
		dos = do.split('.')
		e = timeAgo( dos[0], startDate )
		# return e
		for di,ds in enumerate(dos):
			if di:
				e = timeAgo( dos[di], e )
		return e
	if do.startswith('+'):
		do = do[1:]
	if do is None:
		colorThis( '\t Error: Ago is Missing parameters', 'red' )
		sys.exit()
	if type(do) == float:
		return do
	if do.lower() == 'r':
		return 'resent'
	if 're' in do.lower():
		return 'resent'
	if 'a' in do.lower():
		return 'a'
	if 'cd' in do:
		return do.lower()
	if 'md' in do:
		return do.lower()
	if 'mod' in do.lower():
		return 'md'
	if 'crea' in do.lower():
		return 'cd'
	if 'o' in do.lower():
		return 'one'

	if len(do) == 0:
		do = switches.values('Ago')[0]
	do = do.lower()

	if 't' in do:
		one = resolveEpochTest( startDate )
		two = autoDate( one.split(' ')[0] )
		return two
	if 'mm' in do or 'min' in do:
		each = 60
		units = do
		units = units.replace( 'min', '' )
		units = units.replace( 'm', '' )
		units = int( units )
		remove = units * each
		return startDate + remove  
	if isTime:
		if 'm' in do:
			each = 60
			units = do
			units = units.replace( 'm', '' )
			units = int( units )
			remove = units * each
			return startDate + remove  

	if 'h' in do:
		each = 3600
		units = do
		units = units.replace( 'h', '' )
		units = int( units )
		remove = units * each
		return startDate + remove  
	if 's' in do:
		units = do
		units = units.replace( 's', '' )
		units = int( units )
		return startDate + units


	fnd = 'ymwd'
	nmb = do
	for t in fnd:
		nmb = nmb.replace(t,'')
	if len(nmb) == 0:
		nmb = 1
	try:
		nmb = int(nmb)
	except Exception as e:
		nmb = 1

	if 'y' in do:
		# start_date = dateMathEpoch( startDate, 365 * nmb, '+' )
		# start_date = dateMathEpoch( startDate, 365 * nmb, '+' )
		start_date = yearMath( startDate, nmb, do='+' )
	if 'm' in do:
		# start_date = dateMathEpoch( startDate, 30 * nmb, '+' )
		start_date = monthMath( startDate, nmb, do='+' )
	if 'w' in do:
		start_date = dateMathEpoch( startDate, 7 * nmb, '+' )
	if 'd' in do:
		start_date = dateMathEpoch( startDate, nmb, '+' )
	return start_date


def monthsDiff( one, two ):
	one = friendlyDate( autoDate( one ) ).split(' ')[0]
	two = friendlyDate( autoDate( two ) ).split(' ')[0]

	# print_( 'here' )
	# print_( 'one', one )
	# print_( 'two', two )
	oneB = one.split('-')
	twoB = two.split('-')
	# print_( 'here' )

	oneA = float( oneB[0]+'.'+oneB[1] )
	twoA = float( twoB[0]+'.'+twoB[1] )

	if oneA == twoA:
		return 0
	elif oneA < twoA:
		do = '-'
	else:
		do = '+'

	oneB[0] = int(oneB[0])
	oneB[1] = int(oneB[1])

	twoB[0] = int(twoB[0])
	twoB[1] = int(twoB[1])
	i=0
	# print_(  )
	# print_(' i',i, do)
	done = False
	while  not done:
		if oneB[0] == twoB[0] and  oneB[1] == twoB[1]:
			done = True
		if not done:
			i+=1
			if do == '+':
				twoB[1]+=1
				if twoB[1] == 13:
					twoB[1] = 1
					twoB[0] += 1
			elif do == '-':
				twoB[1]-=1
				if twoB[1] == 0:
					twoB[1] = 12
					twoB[0] -= 1
	#   print_('i',i, twoB[0], twoB[1])
	# print_(' i',i, do, oneB[0], oneB[1], '|', twoB[0], twoB[1] )
	return i
cal_days = None
def days_in_month( m, y=None ):
	global cal_days
	if cal_days is None:
		cal_days = getTableDB( 'cal-days.hash' )
	if m == 2:
		if y is None:
			return 28
		elif not y is None:
			if isLeapYear( y ):
				return 29
			else:
				return 28
	return cal_days[str(m)]


def isLeapYear( year ):
	global leap_years_table
	if leap_years_table is None:
		leap_years_table = getTableDB( 'leap-years.list' )

	if year in leap_years_table:
		return True
	return False


def dateDiffDic( one, two ):

	oA = autoDate( friendlyDate( autoDate(one) ).split(' ') )
	tA = autoDate( friendlyDate( autoDate(two) ).split(' ') )
	if oA > tA:
		o = oA
		t = tA
	else:
		o = tA
		t = oA



	md1 = monthsDiff( one, two )
	# md1 = autoDate( friendlyDate( autoDate(md1) ).split(' ') )
	print_( 'md1', md1 )
	md2 = md1
	mx1 = monthMath( t, md1, do='+' )
	print_( 'mx1', friendlyDate(mx1) )
	mx1 = autoDate( friendlyDate( autoDate(mx1) ).split(' ') )
	print_( 'mx1', friendlyDate(mx1) )
	# if mx1 > t:
	if abs(mx1 - o) > 86420:
		print_( 'error a' )
		print_( '-', abs(mx1 - o) )
		print_( friendlyDate(mx1), friendlyDate(o) )
		print_( (mx1), (o) )
		print_( 'error a' )
		md1-=1
		mx1 = monthMath( o, md1-1, do='+' )
	d1 = abs(daysDiff( o, mx1 ))

	# mx2 = monthMath( o, md2, do='+' )
	# mx2 = autoDate( friendlyDate( autoDate(mx2) ).split(' ') )
	# # if mx2 > o:
	# if abs(mx2 - t) > 86420:

	#   print_( 'error b' )
	#   print_( '-', abs(mx2 - t) )
	#   print_( friendlyDate(mx2), friendlyDate(t) )
	#   print_( (mx2), (t) )

	#   print_( 'error b' )
	#   md2-=1
	#   mx2 = monthMath( t, md2, do='+' )
	# d2 = daysDiff( t, mx2 )


	return md1, d1

	# one = friendlyDate( autoDate( one ) ).split(' ')[0]
	# two = friendlyDate( autoDate( two ) ).split(' ')[0]

	# # print_( 'here' )
	# # print_( 'one', one )
	# # print_( 'two', two )
	# oneB = one.split('-')
	# twoB = two.split('-')
	# # print_( 'here' )

	# oneA = float( oneB[0]+'.'+oneB[1] )
	# twoA = float( twoB[0]+'.'+twoB[1] )

	# if oneA == twoA:
	#   return 0
	# elif oneA < twoA:
	#   do = '-'
	# else:
	#   do = '+'

	# oneB[0] = int(oneB[0])
	# oneB[1] = int(oneB[1])
	# oneB[2] = int(oneB[2])

	# twoB[0] = int(twoB[0])
	# twoB[1] = int(twoB[1])
	# twoB[2] = int(twoB[2])

	# cnt = {
	#           'y': 0,
	#           'm': 0,
	#           'd': 0,
	# }
	# # print_(  )
	# # print_(' i',i, do)
	# done = False

	# done = False

	# # print_(  )



	# while  not done:
	#   print_( oneB, twoB )
	#   if oneB[0] == twoB[0] and  oneB[1] == twoB[1]  and  oneB[2] == twoB[2] :
	#       done = True
	#   if not done:
	#       twoB[2]+=1
	#       cnt['d'] += 1
	#       if twoB[2] > days_in_month( twoB[1], twoB[0] ):
	#           twoB[2] = 1
	#           twoB[1] += 1
	#           cnt['d'] = 0
	#           cnt['m'] += 1

	#       if twoB[1] == 13:
				
	#           twoB[1] = 1
	#           twoB[0] += 1
	cnt['y'] = int(str( cnt['m']/12 ).split('.')[0])
	cnt['m'] = cnt['m'] - ( cnt['y']*12 )
	return cnt
# def dateDiffDic( one, two ):
	# one = friendlyDate( autoDate( one ) ).split(' ')[0]
	# two = friendlyDate( autoDate( two ) ).split(' ')[0]

	# # print_( 'here' )
	# # print_( 'one', one )
	# # print_( 'two', two )
	# oneB = one.split('-')
	# twoB = two.split('-')
	# # print_( 'here' )

	# oneA = float( oneB[0]+'.'+oneB[1] )
	# twoA = float( twoB[0]+'.'+twoB[1] )

	# if oneA == twoA:
	#   return 0
	# elif oneA < twoA:
	#   do = '-'
	# else:
	#   do = '+'

	# oneB[0] = int(oneB[0])
	# oneB[1] = int(oneB[1])
	# oneB[2] = int(oneB[2])

	# twoB[0] = int(twoB[0])
	# twoB[1] = int(twoB[1])
	# twoB[2] = int(twoB[2])

	# i=0
	# # print_(  )
	# # print_(' i',i, do)
	# done = False
#   while  not done:
#       if oneB[0] == twoB[0] and  oneB[1] == twoB[1]:
#           done = True
#       if not done:
#           i+=1
#           if do == '+':
#               twoB[1]+=1
#               if twoB[1] == 13:
#                   twoB[1] = 1
#                   twoB[0] += 1
#           elif do == '-':
#               twoB[1]-=1
#               if twoB[1] == 0:
#                   twoB[1] = 12
#                   twoB[0] -= 1
	
#   # md = days_in_month( twoB[1], twoB[0] )
#   # if twoB[2] > md:
#   #   dif = twoB[2] - md
#   #   twoB[2] = dif
#   #   twoB[1] += 1
#   #   i+=1
#   days = oneB[2] - twoB[2]
#   if days < 0:

#       bb = str(twoB[1])
#       cc = str(twoB[2])
#       # print_( '048b' )
#       if twoB[1] < 10:
#           bb = '0'+bb
#       if twoB[2] < 10:
#           cc = '0'+cc
#       text = str(twoB[0])+'-'+bb+'-'+cc
#       result = autoDate(  text  )

#   tMs = int(str(tMsZ).split('.')[0])
#   y = int(str( i/12 ).split('.')[0])
#   i = i - ( y*12 )

#   return { 'y': y, 'm': i }



def woy_from_year_week( y, w ):
	return str(round(w * 0.01,2) + y)

def woy2dates( woy ):
	s = woy2date( woy ) 
	e = days_math( s, 7, '+' )-1
	return [s, e]

def woy2datesFriendly( woy ):
	es = woy2dates( woy )
	return friendlyDate(es[0]), friendlyDate(es[1])

def woy2date( woy ):
	d = "2013-W26"
	d = woy.split('.')[0]
	d += '-'
	d += 'W' + str(int(woy.split('.')[1]))
	return autoDate(str(datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")).split(' ')[0])

def dateDiffText( theDate, epoch=None ):

	y=0
	m=0
	w=0

	theDate = autoDate( theDate )
	if epoch is None:
		epoch = time.time()
	# woy = getWOY( theDate )
	days = abs(daysDiff( theDate, epoch ))
	
	if theDate < epoch:
		end = '<'
	else:
		end = '>'

	msDiff = epoch - theDate

	if msDiff > 0 and msDiff <= 86400:
		return 'today'
	elif msDiff > 0 and msDiff <= 82800:
		return 'today'
	elif msDiff > 0 and msDiff <= 169200:
		return 'yesterday'
	elif msDiff > 0 and msDiff <= 604801:
		return 'this week'



	# print_( theDate, days, theDate < epoch, theDate > epoch, epoch, time.time() )
	if days == 0:
		return 'today'
	elif theDate < epoch:
		if days == 1:
			return 'yesterday'
		elif days < 7:
			return 'this week'
	elif theDate > epoch:
		if days == 1:
			return 'tommorow'
		elif days < 7:
			return 'next week'

	if days >= 365:
		tmp = float(days / 365)
		y = int(str(tmp).split('.')[0])
		days = days - ( y*365 )
	if days >= 30:
		tmp = float(days / 30)
		m = int(str(tmp).split('.')[0])
		days = days - ( m*30 )
	if days >= 7:
		tmp = float(days / 7)
		w = int(str(tmp).split('.')[0])
		days = days - ( w*7 )

	result = []
	if y:
		result.append( str(y)+'y' )
	if m:
		result.append( str(m)+'m' )
	if w:
		result.append( str(w)+'w' )
	result.append( end )
	return ' '.join( result )

def getWOY( theDate ):
	theDate = autoDate( theDate )
	woy = getWOYFromEpoch(theDate)
	year = getYearFromEpoch(theDate)
	weekAndYear = round(woy * 0.01,2) + year
	weekAndYear = str(weekAndYear)
	if len(weekAndYear) == 6:
		weekAndYear += '0' 
	return weekAndYear

def getYearFromEpoch(theDate):
	theDate = autoDate(theDate)
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[0]

def getWOYFromEpoch(theDate):
	# print_('theDate:',theDate)
	theDate = autoDate(theDate)

	try:
		return datetime.datetime.fromtimestamp( theDate ).isocalendar()[1]
	except Exception as e:
		print_( 'Error:', theDate )
		sys.exit()


date_datetime = None
def daysDiff( one, two ):
	global date_datetime
	oneA = autoDate( one )
	twoB = autoDate( two )
	g = 1
	if two > one:
		g = 2

	if one == two:
		return 0
	elif one > two:
		one = friendlyDate( oneA ).split(' ')[0]
		two = friendlyDate( twoB ).split(' ')[0]
	else:
		one = friendlyDate( twoB ).split(' ')[0]
		two = friendlyDate( oneA ).split(' ')[0]


	# print_( '090', one, two )

	oneB = one.split('-')
	twoB = two.split('-')
	if date_datetime is None:
		from datetime import date as date_datetime
	d0 = date_datetime(int(oneB[0]), int(oneB[1]), int(oneB[2]))
	# print_( '080', twoB )
	d1 = date_datetime(int(twoB[0]), int(twoB[1]), int(twoB[2]))
	delta = d1 - d0
	dd = delta.days
	if g == 1:
		dd = abs(dd)
	return dd


def yearMath( thisDate, years, do='+' ):
	theDateParts = friendlyDate( autoDate( thisDate ) ).split(' ')
	theDate = theDateParts[0]
	parts = theDate.split('-')
	parts[0] = int(parts[0])
	i = 0
	while not i == years:
		if do == '+':
			parts[0] += 1
		elif do == '-':
			parts[0] -= 1
		i+=1
				

	return autoDate(  str(parts[0])+'-'+parts[1]+'-'+parts[2] +' '+ theDateParts[1] )


def monthMath( thisDate, months, do='+' ):
	months = abs(months)
	# print_( '040', thisDate, autoDate( thisDate ), friendlyDate(thisDate) )
	theDateParts = friendlyDate( autoDate( thisDate ) ).split(' ')
	theDate = theDateParts[0]
	parts = theDate.split('-')
	parts[0] = int(parts[0])
	parts[1] = int(parts[1])
	parts[2] = int(parts[2])
	i = 0
	while not i == months:
		# print_( months, 1, parts )
		if do == '+':
			parts[1]+=1
			if parts[1] == 13:
				parts[1] = 1
				parts[0] += 1
		elif do == '-':
			parts[1]-=1
			if parts[1] == 0:
				parts[1] = 12
				parts[0] -= 1
		i+=1
	# print_( '048a' )
	bb = str(parts[1])
	cc = str(parts[2])
	# print_( '048b' )
	if parts[1] < 10:
		bb = '0'+bb
	if parts[2] < 10:
		cc = '0'+cc
	# print_( '048c' )
	text = str(parts[0])+'-'+bb+'-'+cc +' '+ theDateParts[1]
	# print_( '049', text )
	result = autoDate(  text  )
	# print_( '050a', text, type( result ) )
	while type( result ) == bool:

		parts[2]-=1

		bb = str(parts[1])
		cc = str(parts[2])
		if parts[1] < 10:
			bb = '0'+bb
		if parts[2] < 10:
			cc = '0'+cc
		text = str(parts[0])+'-'+bb+'-'+cc +' '+ theDateParts[1]
		result = autoDate(  text  )
		# print_( '050b', text, type( result ) )



	# print_( '050c', text )
	# print_( '060', result )
	return result

def epoch(string,end=False):
	string = str(string)
	if '.' in string:
		d = string.split('.')
	elif _v.slash in string:
		d = string.split(_v.slash)
	elif '-' in string:
		d = string.split('-')
	elif len(string) == 6:
		t = string[:4] + '-' + string[-2:]
		d = t.split('-')
	elif len(string) == 8:
		x = string[-4:]
		t = string[:4] + '-' + x[:2] + '-' + x[-2:]
		d = t.split('-')

	if not len(d) == 3:
		day = 1
	else:
		day = d[2]
	# print_(d)
	# sys.exit()
	if end:
		y = int(d[0])
		m = int(d[1])
		if m == 12:
			y += 1
			m = 1
		else:
			m += 1
		start_date = datetime.datetime(y,m,1,0,0) + datetime.timedelta(-1)
		result = start_date.timestamp()
	else:
		result = datetime.datetime(int(d[0]),int(d[1]),int(day),0,0).timestamp()
	# result = d
	return result
def isNu(string):
	result = True
	for s in string:
		try:
			int(s)
		except Exception as e:
			result = False
	return result
def isNu2(string):
	result = True
	string = str(string).replace('.','').replace('-','').replace(_v.slash,'').replace('/','')
	try:
		try:
			int(string)
		except Exception as e:
			float(string)
	except Exception as e:
		result = False
	return result
def number2Words(n):
	global numberWords
	try:
		numberWords
		if len(numberWords) == 0:
			numberWords = getText(_v.myTables + _v.slash+'numberWords.txt')
	except Exception as e:
		numberWords = getText(_v.myTables + _v.slash+'numberWords.txt')
	numberWords = getText(_v.myTables + _v.slash+'numberWords.txt')
	if type(n) == int:
		result = numberWords[n].replace(' ','_').replace('-','_').replace('\n','')
	else:
		result = n.replace(' ','_')
	return result
###########################################################################################
###########################################################################################
def checkKey(dict, key):
	if key in dict.keys():
		return True
	else:
		return False

class Databases:

# FOREIGN KEY (project_id) REFERENCES projects (id)

	def __init__( self ):
		
		self.databases = []


	def register( self, name=False, file=False, table=False, records=False, fields=False, delete=False, description=False, project=False, auto=False, printFileActivity=False ):

		idx = len( self.databases )
		self.databases.append( Database( name=name, file=file, table=table, records=records, fields=fields, delete=delete, description=description, project=project, auto=auto, printFileActivity=printFileActivity ) )


	def search( self, name=False, info=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].search( info )

	def getFields( self, name=False, table=False, exclude=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].getFields( table, exclude )

	def update( self, name=False, info=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].update( info )

	def add( self, name=False, info=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].add( info )

	def insertRecords( self, name, table, records ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].insertRecords( table=table, records=records )
							
	def trigger( self, name, table, field, trigger ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].addTrigger( table, field, trigger )


class Database:
	
	def __init__( self, name=False, file=False, table=False, records=False, fields=False, delete=False, description=False, project=False, auto=False, printFileActivity=False ):
		self.initialized = []
		self.initializedDB = False
		self.tableInfo = []
		self.tables = []
		self.relationships = []

		self.name = name
		self.file = _v.myDatabases + _v.slash + file
		self.delete = delete
		self.printFileActivity = printFileActivity

		self.project = project
		self.description = description
		self.apps = False

		self.table = table
		self.records = records
		
		self.fieldsManual = fields
		self.fields = {}

		if type( table ) == bool:
			auto = True
		if not type( self.records ) == bool:
			for i,r in enumerate(self.records):
				self.records[i]['date_created'] = time.time()
				self.records[i]['date_modified'] = ''
				# print_( self.records[i] )

		if self.delete and os.path.isfile( self.file ):
			os.unlink( self.file )
			if self.printFileActivity:
				print_( ' file deleted ')
		if os.path.isfile( self.file ):
			if self.printFileActivity:
				print_( ' file exists ')

		if auto and os.path.isfile( self.file ):
			self.genInfo( process=True )
		else:
			if not type( table ) == bool:
				if not type( self.records ) == bool:
					self.insertRecords( table )
					


	def generateStructure( self, table ):
		if not table in self.initialized:
			self.initialized.append( table )
			if os.path.isfile( self.file ):
				self.genInfo( process=True )
			else:
				fieldsData = self.processRecords()
				self.create( table, fieldsData )

				self.genInfo( process=True )

			

	def addTrigger( self, table, field, trigger ):
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for ii,fieldX in enumerate(self.tables[i].fields):
					if fieldX.name == field:
						self.tables[i].fields[ii].info['trigger'] = trigger



	def updateFieldInfo( self, table, field, label, data ):
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for ii,fieldX in enumerate(self.tables[i].fields):
					if fieldX.name == field:
						self.tables[i].fields[ii].info['label'] = data
	def updateManualFieldInfo( self ):
		if not type( self.fieldsManual ) == bool:
			for i,f in enumerate(self.fieldsManual):
				for k in f.keys():
					if not k == 'name' and not k == 'type' and not k == 'table':
						self.updateFieldInfo( f['table'], f['name'], k, f[k] )

	def getFields( self, table, exclude=False ):
		result = []
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for field in self.tables[i].fields:
					add = True
					if not type( exclude ) == bool:

						if type( exclude ) == str:
							ex = exclude.split(',')
						else:
							ex = exclude

						for x in ex:
							if len( x ) > 0:
								if x in field.name:
									add = False
					if add:
						result.append( field.name )

		return result

	def getFieldType( self, table, field ):
		result = ''
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for fieldX in self.tables[i].fields:
					if fieldX.name == field:
						result = fieldX.info['type']
		return result

	# def update( self, info ):

	#   sql = "update "+info['table']+" set [x] where " + info['update'] + " "
	#   u = ''
	#   for f in info['record'].keys():
	#       t = self.getFieldType( info['table'], f )
	#       if 'int' in t:
	#           u += f + " = " + str(info['record'][f]) + ","
	#       else:
	#           u += f + " = '" + str(info['record'][f]) + "',"
	#   u = _str.cleanBE( u, ',' )

	#   sql = sql.replace( '[x]', u )

	#   conn = sqlite3.connect( self.file )
	#   cursor = conn.cursor()
	#   tables = []
	#   rows = cursor.execute( sql )

	#   fields = self.getFields( info['table'] )
	#   results = []
	#   for row in (rows):
	#       d = {}
	#       for i,column in enumerate(row):
	#           d[ fields[i] ] = row[i]
	#       results.append( d )
	#   conn.commit()
	#   conn.close()

	def update( self, info ):
		sqlite3 = __.imp('sqlite3')
		sql = "update "+info['table']+" set [x] where " + info['update'] + " "
		u = ''
		for f in info['record'].keys():
			t = self.getFieldType( info['table'], f )
			if 'int' in t:
				u += f + " = " + str(info['record'][f]) + ","
			else:
				u += f + " = '" + str(info['record'][f]) + "',"
		u = _str.cleanBE( u, ',' )

		sql = sql.replace( '[x]', u )

		conn = sqlite3.connect( self.file )
		cursor = conn.cursor()
		tables = []
		rows = cursor.execute( sql )

		fields = self.getFields( info['table'] )
		results = []
		for row in (rows):
			d = {}
			for i,column in enumerate(row):
				d[ fields[i] ] = row[i]
			results.append( d )
		conn.commit()
		conn.close()

	def search( self, info ):
		sqlite3 = __.imp('sqlite3')
		if not self.initializedDB:
			print_( 'no data' )
			sys.exit()

		if not type( info['custom'] ) == bool and not info['force']:
			sql = "select * from "+info['table']+" where "+info['custom']
		elif info['force'] and not type( info['custom'] ) == bool:
			sql = info['custom']
		else:
			if info['type'] == 'text':
				sql = "select * from "+info['table']+" where "+info['field']+" like '"+info['search']+"'"
			else:
				sql = "select * from "+info['table']+" where "+info['field']+" "+info['search']

		conn = sqlite3.connect( self.file )
		cursor = conn.cursor()
		tables = []
		rows = cursor.execute( sql )

		fields = self.getFields( info['table'] )
		results = []
		for row in (rows):
			d = {}
			for i,column in enumerate(row):
				# d[ fields[i] ] = row[i]
				d[ fields[i] ] = self.trigger( info['table'], fields[i], row[i] )
			results.append( d )

		conn.close()

		return results
		# print_( info )
	def trigger( self, table, field, data ):
		result = data
		if field == 'date_created':
			return resolveEpochTest( data )
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for fieldX in self.tables[i].fields:
					if fieldX.name == field:
						if not type( fieldX.info['trigger'] ) == bool:
							result = fieldX.info['trigger']( data )
		return result


	def insertRecords( self, table, records=[] ):
		sqlite3 = __.imp('sqlite3')
		if len( records ) > 0:
			self.records = records
			for i,r in enumerate(self.records):
				self.records[i]['date_created'] = time.time()
				self.records[i]['date_modified'] = ''
		self.generateStructure( table )

		conn = sqlite3.connect(self.file)
		cursor = conn.cursor()
		for record in self.records:
			# self.records[i]['date_created'] = time.time()
			record['date_created'] = time.time()
			record['date_modified'] = ''
			sql = self.genRecordInsert( table, record )
			# n = ''

			# for field in fields:
			#   n += field['name'] + ' ' + field['type'] + ','

			# n = _str.cleanBE( n, ',' )
			# sql = sql.replace( '[n]', n )


			cursor.execute( sql )
			conn.commit()
		conn.close()



	def genRecordInsert( self, table, record ):
		b = "'insert into [table] ( [names] ) values ( [dataDel] )'.format( [data] )"
		n = ''
		dd = ''
		d = ''
		b = b.replace( '[table]', table )
		x = []

		for k in record.keys():
			n += k + ','
			d += "record['"+k+"'],"
			dd += '"{}",'
			x.append( record[k] )
		n = _str.cleanBE( n, ',' )
		dd = _str.cleanBE( dd, ',' )
		d = _str.cleanBE( d, ',' )

		b = b.replace( '[names]', n )
		b = b.replace( '[dataDel]', dd )
		b = b.replace( '[data]', d )
		# print_( b )
		return eval( b )


	def genInfo( self, process=False ):
		sqlite3 = __.imp('sqlite3')
		if os.path.isfile( self.file ) and not self.initializedDB:
			self.initializedDB = True
			self.tableInfo = []
			sql = "select name from sqlite_master where type = 'table'"

			conn = sqlite3.connect( self.file )
			cursor = conn.cursor()
			tables = []
			tablesRaw = cursor.execute( sql )
			for table in tablesRaw:
				for data in table:
					if len( data ) > 1 and not 'sqlite' in data:
						tables.append( data )

			# print_( tables )

			for table in tables:
				sql = 'PRAGMA table_info('+table+')'
				fieldsRaw = cursor.execute( sql )
				fields = []
				for fieldsX in fieldsRaw:

					if not type( self.fieldsManual ) == bool:
						data = list(filter(lambda itemX: itemX['name'] == fieldsX[1], self.fieldsManual))
						if len( data ) > 0:
							data[0][ 'type' ] = fieldsX[2]
							fields.append( data[0] )
						else:
							fields.append({ 'name': fieldsX[1], 'type': fieldsX[2],  })
					else:
						fields.append({ 'name': fieldsX[1], 'type': fieldsX[2],  })

					
				
				self.tableInfo.append({ 'name': table, 'fields': fields })

			conn.close()
			if process:
				self.addGeneratedTables()
			return self.tableInfo

	def addGeneratedTables( self ):
		dataOK = True
		if not type( self.records ) == bool:

			for record in self.processRecords():
				found = False
				for table in self.tableInfo:
					for field in table['fields']:
						if record['name'] == field:
							found = True
				if not found:
					dataOK = False
			
		for table in self.tableInfo:
			self.tables.append( DatabaseTables( table['name'], table['fields'] ) )
			self.updateManualFieldInfo()

	def processRecords( self ):
		autoFieldType = []
		for record in self.records:

			for field in record.keys():
				if len(list(filter(lambda itemX: itemX['name'] == field, autoFieldType))) == 0:
					if isText( record[ field ] ):
						t = 'text'
						if 'date_' in field:
							t = 'date'
						if not type( self.fieldsManual ) == bool:
							data = list(filter(lambda itemX: itemX['name'] == field, self.fieldsManual))
							if len( data ) > 0:
								data[0][ 'type' ] = t
								autoFieldType.append( data[0] )
							else:
								autoFieldType.append({ 'name': field, 'type': t })
						else:
							autoFieldType.append({ 'name': field, 'type': t })
					if isNum( record[ field ] ):
						t = 'integer'
						if 'date_' in field:
							t = 'date'
						if not type( self.fieldsManual ) == bool:
							data = list(filter(lambda itemX: itemX['name'] == field, self.fieldsManual))
							if len( data ) > 0:
								data[0][ 'type' ] = t
								autoFieldType.append( data[0] )
							else:
								autoFieldType.append({ 'name': field, 'type': t })
						else:
							autoFieldType.append({ 'name': field, 'type': t })
					if isFloat( record[ field ] ):
						t = 'real'
						if 'date_' in field:
							t = 'date'
						if not type( self.fieldsManual ) == bool:
							data = list(filter(lambda itemX: itemX['name'] == field, self.fieldsManual))
							if len( data ) > 0:
								data[0][ 'type' ] = t
								autoFieldType.append( data[0] )
							else:
								autoFieldType.append({ 'name': field, 'type': t })
						else:
							autoFieldType.append({ 'name': field, 'type': t })


		return autoFieldType

	def fieldInfo( self, table, field, fType ):
		self.fields[ field ] = fType

	def create( self, table=False, fields=False ):
		sqlite3 = __.imp('sqlite3')
		if os.path.isfile(self.file):
			print_( 'Database exists' )
		else:
			conn = sqlite3.connect(self.file)
			cursor = conn.cursor()
			# sql =  'CREATE TABLE '+table+' ([n])'
			sql =  'CREATE TABLE '+table+' (id integer primary key autoincrement not null, [n])'
			n = ''
			nn = ''
			for field in fields:
				n += field['name'] + ' ' + field['type'] + ','
				if not 'date_modified' == field['name']:
					nn += field['name'] + ','

			n = _str.cleanBE( n, ',' )
			nn = _str.cleanBE( nn, ',' )
			sql = sql.replace( '[n]', n )
			cursor.execute( sql )
			sql =   "CREATE TRIGGER UpdateLastTime UPDATE OF "+nn+" ON "+table+" "\
					" BEGIN"\
					"  UPDATE "+table+" SET date_modified=datetime('now','localtime') WHERE id=old.id;"\
					" END;"
			cursor.execute( sql )

			conn.close()



class DatabaseTables:
	def __init__( self, table=False, fields=False ):
		
		self.fields = []

		self.table = table

		if not type( fields ) == bool:
			for i,field in enumerate(fields):
				idx = len( self.fields )
				self.fields.append( DatabaseFields( field['name'], field['type'] ) )
				for label in field.keys():
					if not label == 'name' and not label == 'type' and not label == 'table':
						self.fields[ idx ].addFieldInfo( label, field[ label ] )

	def setInfo( self, field, label, info ):
		for i,row in enumerate(self.fields):
			if self.fields[i].name == field:
				self.fields[i].info[ label ] = info


	def setFields( self, fields=False ):
		if not type( fields ) == bool:
			for i,field in enumerate(fields):
				idx = len( self.fields )
				self.fields.append( DatabaseFields( field['name'], field['type'] ) )
				for label in field.keys():
					if not label == 'name' and not label == 'type' and not label == 'table':
						self.fields[ idx ].addFieldInfo( label, field[ label ] )

	def updateFieldInfo( self, field, label, data ):
		for i,f in enumerate(self.fields):
			if self.fields[i].name == field:
				self.fields[i].info[ label ] = data


class DatabaseFields:
	def __init__( self, name=False, fieldType='text' ):
		self.name = name

		self.info = {
						'name': name,
						'type': fieldType,
						'trigger': False,
						'default': False,
		}

	def addFieldInfo( self, label, info ):
		self.info[ label ] = info

	def fieldInfo( self, label ):
		if label in list( self.info.keys() ):
			return self.info[ label ]
		else:
			return False



###########################################################################################
###########################################################################################

class Database2:

	def __init__(self, data):

		appDB = '_Generated_App_Database.db'
		appJSON = '_Generated_App_Database_Config.json'
		appPyRaw = '_Gen_App_Database_Data'
		appPy = appPyRaw + '.py'
		self.appPyDefault = _v.myDatabases + _v.slash+'_default.py'


		self.data = {}
		self.tables = []
		self.name = data.replace(appDB,'').replace(appJSON,'').replace(appPy,'').replace('.json','')
		if os.path.isfile(self.name + appDB):
			self.appDB =   self.name + appDB
			self.appJSON = self.name + appJSON
			self.appPy =   self.name + appPy

		else:
			self.appDB = _v.myDatabases + _v.slash + self.name + appDB
			self.appJSON = _v.myDatabases + _v.slash + self.name + appJSON
			self.appPy = _v.myDatabases + _v.slash + self.name + appPy
		self.appPyRaw = self.name + appPyRaw

		self.tableDelim = '_x_'

		self.meta = []

	def registerTable(self, name):
		self.tables.append(TablesDB(name))

	def TableFieldCount(self):
		result = 0
		for i,ci in enumerate(self.tables):
			if ci.name == name:
				result = self.tables[i].getCount()
		return result
# {
#   'table': 'table,name',
#   'fields': [
#       {'names': 'one,two'},
#       {'names': 'three', 'table': 'name', 'as': 'threeish'}
#   ],
#   'action': [
#       { 'type': 'text', 'names': 'field', 'table': 'your_mom', 'search': '*.txt,desktop'},
#       { 'type': 'text', 'names': 'testy', 'and_or': 'or', 'table': 'or_test', 'search': '*.py,*.txt'},
#       { 'type': 'field_type(text)', 'table': 'name', 'names': 'field,names', 'and_or': 'and',  'search': '*.py,tech'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': '1000,2000'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'g,1000'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'l,1000'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(ago(2000))'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(epoch(2018.07))'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(epoch(2018.07)),str(epoch('2018.10',True))'},
#       { 'type': 'field_type(sort)', 'names': 'field', 'order': 'asc'},
#       { 'type': 'field_type(sort)', 'names': 'field', 'order': 'desc'},
#   ]
# } 

	def queryBuilder(self,data): # queryBuilder
		self.data = data
		# print_(data['fields'])
		# sys.exit()
		self.qbFields = []
		tbls = data['table'].split(',')
		if len(tbls) > 1:
			multi_Table = True
		else:
			multi_Table = False
		if multi_Table:
			sql = 'SELECT '
			# print_(data['fields'])
			for field in data['fields']:
				for name in field['names'].split(','):
					thisT = ''
					try:
						thisT = field['table']
					except Exception as e:
						thisT =  tbls[0]
					try:
						asF = field['as']
					except Exception as e:
						asF =  name
					name = "" + thisT + '.' + name + " AS " + asF
					self.qbFields.append(asF)
					sql += name + ', '
			sql = _str.cleanLast(sql,', ')
			sql += ' FROM ' + tbls[0] + ' '
			for iJ,tJ in enumerate(tbls):
				if iJ > 0:
					sql += ' JOIN ' + tJ + ' ON ' + tJ + '.id_parent = ' + tbls[0] + '.id_uuid '
				
			sql += ' WHERE '
		else:
			sql = 'SELECT '
			for field in data['fields']:
				for name in field['names'].split(','):
					thisT = ''
					try:
						thisT = field['table']
					except Exception as e:
						thisT =  tbls[0]
					try:
						asF = field['as']
					except Exception as e:
						asF =  name
					name = "" + thisT + '.' + name + " AS " + asF
					self.qbFields.append(asF)
					sql += name + ', '
			sql = _str.cleanLast(sql,', ')
			sql += ' FROM ' + tbls[0] + ' WHERE '
		# JOIN albums ON albums.albumid = tracks.albumid
		orderBy = False
		for i,action in enumerate(data['action']):
			if action['type'] == 'text':
				sql += '('
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "" + thisT + '.' + name + ""
					try:
						and_or = action['and_or']
					except Exception as e:
						and_or =  'and'
					for tv in action['search'].split(','):
						if tv.startswith('*'):
							tv = tv.replace('*','')
							sql += ' ' + name + " like '%" + tv + "' " + and_or + ' '
						elif tv.endswith('*'):
							tv = tv.replace('*','')
							sql += ' ' + name + " like '" + tv + "%' " + and_or + ' '
						else:
							sql += ' ' + name + " like '%" + tv + "%' " + and_or + ' '
				sql = _str.replaceDuplicate(sql,' ')
				sql = _str.cleanLast(sql,' and ')
				sql = _str.cleanLast(sql,' or ')
				sql += ') and '
			sql = sql.replace('WHERE and ','WHERE ')
			if action['type'] == 'number':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if not len(coin) == 2:
						print_('bad input')
						sys.exit()
					if isNu(coin[0]):
						do = 'b'
					else:
						do = coin[0]
					if do == 'b':
						sql += name + ' > ' + str(coin[0]) + " and " + name + " < " + str(coin[1]) + ' and '
					if do == 'l':
						sql += name + ' < ' + str(coin[1]) + ' and '
					if do == 'g':
						sql += name + ' > ' + str(coin[1]) + ' and '



			if action['type'] == 'date':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if not len(coin) == 2:
						if isNu2(coin[0]):
							sql += name + ' > ' + str(epoch(coin[0])) + ' and '
						else:
							sql += name + ' > ' + str(timeAgo(coin[0])) + ' and '
					else:
						if isNu2(coin[0]):
							do = 'b'
						else:
							do = coin[0]
						if do == 'b':
							sql += name + ' > ' + str(epoch(coin[0])) + " and " + name + " < " + str(epoch(coin[1],True)) + ' and '
						if do == 'l':
							sql += name + ' < ' + str(epoch(coin[1])) + ' and '
						if do == 'g':
							sql += name + ' > ' + str(epoch(coin[1])) + ' and '



			if action['type'] == 'bytes':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if coin[0] == 'l':
						sql += name + ' < ' + str(unFormatSize(coin[1])) + ' and '
					elif coin[0] == 'g':
						sql += name + ' > ' + str(unFormatSize(coin[1])) + ' and '
					else:
						sql += name + ' > ' + str(unFormatSize(coin[0])) + " and " + name + " < " + str(unFormatSize(coin[1])) + ' and '



			if action['type'] == 'sort':
				orderBy = True
		sql = _str.cleanLast(sql,' and ')
		sql = _str.cleanLast(sql,' or ')
		if orderBy:
			sql += ' ORDER BY '
			for i,action in enumerate(data['action']):
				if action['type'] == 'sort':
					try:
						if 'a' in action['order'].lower():
							order = 'ASC'
						else:
							order = 'DESC'
					except Exception as e:
						order = 'ASC'
					for name in action['names'].split(','):
						if multi_Table:
							try:
								thisT =  action['table']
							except Exception as e:
								thisT =  tbls[0]
							name = "'" + thisT + '.' + name + "'"
						sql += name + ' ' + order + ', '

		sql = _str.cleanLast(sql,' and ')
		sql = _str.cleanLast(sql,' or ')
		sql = _str.cleanLast(sql,', ')
		sql = _str.replaceDuplicate(sql,' ')
		sql = _str.cleanLast(sql,' ')
		sql += ';'
		sql = sql.replace('WHERE;',';')
		return sql
	def metaGen(self):
		sqlite3 = __.imp('sqlite3')
		import re
		# import numpy as np
		meta = []
		con = sqlite3.connect(self.appDB)
		for line in con.iterdump():
			if 'CREATE TABLE' in line and not 'INSERT INTO' in line:
				# print_(line)
				one = line.split('CREATE TABLE ')[1]
				two = one.split(' (')
				table = two[0]
				# print_(table)
				fieldRaw = two[1].split(')')[0]
				f = []
				for field in fieldRaw.split(', '):
					# print_('\t',field)
					fd = field.split(' ')
					f.append({'type': fd[1], 'field': fd[0], 'max': 0, 'min': 0, 'average': 0})


				if self.tableDelim in table:
					parent = ''
					mx = len(table.split(self.tableDelim))-1
					for iT,tX in enumerate(table.split(self.tableDelim)):
						if iT < mx:
							parent += tX + self.tableDelim
					parent = _str.cleanLast(parent,self.tableDelim)
				else:
					parent = ''


				meta.append({'table': table, 'parent': parent, 'fields': f})
			elif 'INSERT INTO' in line:
				pass
				# break
		average = {}
		for im,m in enumerate(meta):
			sql = 'SELECT * FROM ' + m['table']
			conn = sqlite3.connect(self.appDB)
			c = conn.cursor()
			c.execute(sql)
			rows = c.fetchall()
			for row in rows:
				# print_(row)
				for fi,field in enumerate(m['fields']):
					# print_(field['field'],row[fi])
					aKey = str(m['table']) + '-' + str(number2Words(field['field']))
					# print_(aKey)
					
					try:
						if not type(average[aKey]['datapoints']) == list:
							average[aKey] = {'max': 0, 'min': 'first', 'average': 0, 'datapoints': [], 'count': 0}

						# print_(type())                     
					except Exception as e:
						average[aKey] = {'max': 0, 'min': 'first', 'average': 0, 'datapoints': [], 'count': 0}
					average[aKey]
					# print_(aKey)
					if field['type'] == 'int':
						if type(row[fi]) == int:
							size = row[fi]
						else:
							string = re.sub('[^0-9]', '', str(row[fi]))
							# print_(type(string),string)
							# print_(string)
							if len(string) == 0:
								size = 0
							else:
								size = int(string)
					if field['type'] == 'str':
						size = len(str(row[fi]))
					# print_()
					# print_(type(average[aKey]['max']),average[aKey]['max'])
					# print_(type(size),size)
					if average[aKey]['max'] < size:
						average[aKey]['max'] = size
					if average[aKey]['min'] == 'first':
						average[aKey]['min'] = size
					elif average[aKey]['min'] > size:
						average[aKey]['min'] = size
					average[aKey]['datapoints'].append(size)

		errors = []
		totalCount = 0
		for im,m in enumerate(meta):

			for row in rows:
				# print_(row)
				for fi,field in enumerate(m['fields']):
					# print_(meta[im]['fields'][fi]['max'])
					aKey = m['table'] + '-' + number2Words(field['field'])
					# print_(aKey)
					try:
						# print_(average[aKey]['max'])
						meta[im]['fields'][fi]['max'] = average[aKey]['max']
						meta[im]['fields'][fi]['min'] = average[aKey]['min']
						# meta[im]['fields'][fi]['average'] = int(np.mean(average[aKey]['datapoints']))
						meta[im]['count'] = len(average[aKey]['datapoints'])
						total = meta[im]['count']
					except Exception as e:
						errors.append(aKey)
				totalCount += total

		self.meta = {'data': meta, 'records': totalCount, 'errors': errors}
		saveTable2(meta,'database_meta.json')

		return meta
	def metaPrint(self):
		if self.meta == []:
			self.metaGen()

		totalColumnWidth = 0
		for m in self.meta['data']:
			tables.register(m['table'],m['fields'])
			spaces = tables.getLength(m['table'],'type,field,max,min,average')
			if spaces > totalColumnWidth:
				totalColumnWidth = spaces



		# fieldLengths = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#   if not type(fieldLengths) == dict:
		#       fieldLengths = data
		#   for name in fieldLengths.keys():
		#       if data[name] > fieldLengths[name]:
		#           fieldLengths[name] = data[name]



		for m in self.meta['data']:
			genLine(totalColumnWidth,'=')
			print_('Table:\t',m['table'])
			print_('Parent:\t',m['parent'])
			print_('Records:',m['count'])
			print_()
			tables.register(m['table'],m['fields'])
			# tables.fieldProfileSet(m['table'],'*','alignment','center')
			# tables.print(m['table'],'type,field,max,min,average',fieldLengths)
			tables.print(m['table'],'type,field,max,min,average')

			genLine(totalColumnWidth,'=')
		print_()
		print_('Records:',self.meta['records'])
		print_()
		print_('Errors:')
		for e in self.meta['errors']:
			print_('\t',e)
		print_()
		print_()
		print_('Example:')
		print_('\t p dba -app',self.name)
		print_()
		print_()
	def findParent(self,table):
		# parent = 'Error'
		# for m in self.meta['data']:
		#   if m['table'] == table:
		#       parent = m['parent']
		#       break
		if self.tableDelim in table:
			parent = ''
			mx = len(table.split(self.tableDelim))-1
			for iT,tX in enumerate(table.split(self.tableDelim)):
				if iT < mx:
					parent += tX + self.tableDelim
			parent = _str.cleanLast(parent,self.tableDelim)
		else:
			parent = ''
		return parent

	def findChildren(self,table):
		if self.meta == []:
			self.metaGen()
		children = []
		for m in self.meta['data']:
			if m['parent'] == table:
				children.append(m['table'])

		return children

	def findType(self,column):
		mainTable = self.data['table'].split(',')[0]
		found = False
		nm = ''
		result = ''

		for action in self.data['fields']:
			for name in action['names'].split(','):
				if name == column:
					try:
						if action['type'] == 'date' or 'byte' in action['type']:
							result = action['type']
					except Exception as e:
						pass

		if len(result) == 0:
			for action in self.data['action']:
				for name in action['names'].split(','):
					if name == column:
						if action['type'] == 'date' or 'byte' in action['type']:
							result = action['type']

		if len(result) == 0:
			for field in self.data['fields']:
				try:
					table = field['table']
				except Exception as e:
					table = mainTable
				if ',' in field['names']:
					for name in field['names'].split(','):
						if name == column:
							nm = name
							found = True
				else:
					try:
						newName = field['as']
					except Exception as e:
						newName = field['names']
					if newName == column:
						nm = newName
						found = True
				# print_(field)
				if found:
					break

			result = self.checkConfig(table,nm)
		# print_(mainTable)
		return result
	def checkConfig(self,tbl,nm):
		self.appJSON
		# print_(self.appJSON)
		# print_(tbl,nm)
		structure = getTable2(self.appJSON)
		result = ''
		if tbl == structure['name']:
			for zs in structure['zstructure']:
				if zs['field'] == nm:
					result = zs['type']
					break
		return result

	def executeSQL(self,sql,group=0):
		sqlite3 = __.imp('sqlite3')
		conn = sqlite3.connect(self.appDB)
		c = conn.cursor()
		c.execute(sql)
		all_rows = c.fetchall()
		records = []
		for f in all_rows:
			row = {}
			for ic,c in enumerate(self.qbFields):
				row[c] = f[ic]

			records.append(row)
		col = ''
		for c in self.qbFields:
			col += c + ','
		col = _str.cleanLast(col,',')
		tables.register('sql',records)
		for ic,c in enumerate(self.qbFields):
			if self.findType(c) == 'date':
				tables.fieldProfileSet('sql',c,'trigger',float2Date2)
			if 'byte' in self.findType(c):
				tables.fieldProfileSet('sql',c,'trigger',formatSize)
			if self.findType(c) == 'bytes':
				tables.fieldProfileSet('sql',c,'trigger',formatSize)
			# print_(self.findType(c))
		tables.print('sql',col)



class TablesDB:

	def __init__(self):
		self.columns = []

	def register(self, name):
		self.columns.append(ColumnsDB(name))
		self.fieldCount = len(self.columns)

	def getCount(self):
		return self.fieldCount


class ColumnsDB:

	def __init__(self, name, kind):
		self.name = name
		self.active = False
		self.kind = kind

	# def trigger(self,script):
	#   self.script_trigger = script

	# def changeStatus(self,newStatus):
	#   self.active = newStatus

	# def print(self):
	#   childItems = []
	#   for ci in self.columns:
	#       childItems.append({'name':ci.name})
	#   tables.register('childClassItems',childItems)
	#   # tables.trigger('switches','switch,name',test,True)
	#   tables.print('childClassItems','name')


	#       childItems.append({'name':ci.name ,'active':active,'value': value})
	#   tables.register('childClassItems',childItems)
	#   tables.print('childClassItems','name,active,value')

	# def status(self,name,newStatus):
	#   for i,ci in enumerate(self.columns):
	#       if ci.name == name:
	#           self.columns[i].changeStatus(newStatus)


###########################################################################################
def get_size2(obj, seen=None):
	# https://medium.com/@alexmaisiura/python-how-to-reduce-memory-consumption-by-half-by-adding-just-one-line-of-code-56be6443d524
	# From https://goshippo.com/blog/measure-real-size-any-python-object/
	# Recursively finds size of objects
	size = sys.getsizeof(obj)
	if seen is None:
		seen = set()
	obj_id = id(obj)
	if obj_id in seen:
		return 0


###########################################################################################
def genLine(count,what, p=1):
	count = int(count)
	what = str(what)
	cnt = 0
	result = ''
	while cnt < count:
		result += what
		cnt += 1
	if p:
		print_(result)
	return result

ciData = (  
			[ ';sp',   ' ' ],
			[ '_;192A;_',   ',' ],
			[ '_;192B;_',   ':' ],
			[ ';;',         ',' ],
			[ ';c',         ',' ],
			
			[ ';_',         '-' ],
			[ ';-',         '-' ],

			[ ';p;',        '%' ],
			[ ';p',         '%' ],
			[ ';.',         ':' ],
			[ ";;'",        _v.slash+'"' ],

			[ _v.slash+'n',        '\n' ],
			[ ';n',         '\n' ],
			[ ';return',    '\n' ],
			[ ';t',         '\t' ],

			[ ";'",         '"' ],
			[ ';q;',        '"' ],
			[ '"\'"',       "'" ],
			[ ';sq',       "'" ],
			[ 'null00',     '"",' ],
			[ '"\'", "\'"', "','" ],

			[ '[star]',     '*' ],
			[ '[a]',        '*' ],
			[ '[s]',        '$' ],
			[ '[eq]',       '=' ],
			[ ';opar;',     '[' ],
			[ ';bkt0;',     '[' ],
			[ ';bkt1;',     ']' ],
			[ '[pipe]',     '|' ],
			[ '[p]',     '|' ],
			[ '[htmlopen]', '<' ],
			[ '[htmlclose]','>' ],
			[ '[gtr]',      '>' ],
			[ '[lss]',      '<' ],
			[ ';6',         '^' ],
			[ ';+',         '+' ],

			[ '+--+c',      '--c' ],

			[ '[semi]',      ';' ],
			[ ';bs',         '/' ],
			[ ';fs',         '\\' ],
			[ ';d;',         __.theDelim ],
			[';delim;',         __.theDelim ],
			[';thedelim;',         __.theDelim ],
			[';theDelim;',         __.theDelim ],
			[';p',                 '%' ],
			[';js',                '//' ],
			[';bs',                '/' ],
			[';fs',                '\\' ],
			[';t',                 '\t' ],
			['↔',                 ' ' ],
			
			[ '[caret]',    '^' ]  )
ci_spent=[]
def ci(string):
	#switchValueClean
	global ciData
	# print_( ciData )
	# sys.exit()
	for cx in ciData:
		if cx[0] in string:
			# print_( 'HERE', cx )
			string = string.replace( cx[0], cx[1] )
	return string

def ci2(string):
	string = ci(string)
	string = _str.replaceAll(string,',',' ')
	return string

# """ {7DB6A001-0637-4F13-B328-2B17A481CF35}
def randomTrueFalse(fix=2):
	import random

	global randomTrueFalseLast
	global randomTrueFalseCount
	global randomTrueFalseSame
	try:
		randomTrueFalseLast
	except Exception as e:
		randomTrueFalseLast = True
		randomTrueFalseSame = 0
		randomTrueFalseCount = 0

	ran = random.randint(1,101)
	result = ran % 2 == 0
	i = 0
	while i < fix:
		i+=1
		if result == randomTrueFalseLast:
			ran = random.randint(1,101)
			result = ran % 2 == 0

	if result == randomTrueFalseLast:
		randomTrueFalseSame += 1
	randomTrueFalseCount += 1
	randomTrueFalseLast = result
	return result
def randomizeCase(string):
	import random

	result = ''
	for ch in string:
		if ch.isalnum():
			try:
				int(ch)
			except Exception as e:
				ran = random.randint(1,101)
				test = ran % 2 == 0
				if randomTrueFalse():
					ch = ch.lower()
				else:
					ch = ch.upper()
		result += ch
	return result
# """


def onlyAlpha(string):
	result = ''
	for ch in string:
		if ch.isalnum():
			try:
				int(ch)
			except Exception as e:
				result += ch
	return result

def onlyNumbers(string):
	result = ''
	for ch in string:
		if ch.isalnum():
			try:
				int(ch)
				result += ch
			except Exception as e:
				pass
	return result
def onlyAlphaNumeric(string):
	result = ''
	for ch in string:
		if ch.isalnum():
			result += ch
	return result
def longID(howMany=2):
	result = ''
	i = 0
	while i < howMany:
		result += genUUID()
		i += 1
	result = result.replace('}{','-')
	return result


# def resolveLocal(file):
#   if os.path.isfile(file):
# %python%\%*.py
# %phpFiles%\%*.php
# %scriptroot%\%*.bat
# %powershell%\%*.ps1
# D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1
# %myPhp%\%*.php
# %myPowershell%\%*.ps1
# %myPython%\%*.py
# %myTables%\%*
# %myTables%\%*.json
# %myDatabases%\%*
# %myWebApp%\%*
# %USERPROFILE%\Desktop\%*

def formatColumns_OLD(columns):
	# print_(__.appReg)
	# print_(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if '.' in c or ':' in c:
				hasPre = True
				c = c.replace(':','.')
				preDataR = c.split('.')
				preData = preDataR[0]
				c = preDataR[1]

			for col in appInfo[__.appReg]['columns']:
				for a in col['abbreviation'].split(','):
					if a.lower() == c.lower():
						c = col['name']
			if hasPre:
				c = preData + '.' + c
			result += c + ','
		result = result[:-1]
	# print_(result)
	return result

def formatColumns(columns):
	# print_(__.appReg)
	# print_(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if c.startswith('d.'): c=c.replace('d.','d:')
			if c.startswith('a.'): c=c.replace('a.','a:')
			if ':' in c:
				hasPre = True
				# c = c.replace(':','.')
				preDataR = c.split(':')
				preData = preDataR[0]
				c = preDataR[1]

			for col in appInfo[__.appReg]['columns']:
				for a in col['abbreviation'].split(','):
					if a.lower() == c.lower():
						# print_(a,c)
						# sys.exit()
						c = col['name']
			if hasPre:
				c = preData + ':' + c
			result += c + ','
		result = result[:-1]
	# print_(result)
	return result


def formatColumnsSort(columns):
	sorting={}
	# Asc:type, Desc:ext
	if type(columns) == str:
		col=[]
		for i,co in enumerate(columns.split(',')):
			if co.lower().startswith('a') or co.lower().startswith('d'):
				if co[1] == '.' or co[1] == ':':
					c=co[2:]
					sorting[i]=co[0]
				elif len(co)>4 and (  co[4] == '.' or co[4] == ':'  ):
					c=co[5:]
					sorting[i]=co[0].lower()
				elif len(co)>3 and (  co[3] == '.' or co[3] == ':'  ):
					c=co[4:]
					sorting[i]=co[0].lower()
				else: c=co
			else: c=co
			col.append(c)
		columns=','.join(col)
		# if columns.startswith('a.'):
		# 	columns = 'a:' + columns[2:]
		# if ',a.' in columns:
		# 	columns = columns.replace( ',a.', ',a:' )

		# if columns.startswith('d.'):
		# 	columns = 'd:' + columns[2:]
		# if ',d.' in columns:
		# 	columns = columns.replace( ',d.', ',d:' )


	# print_(__.appReg)
	# print_(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if ':' in c:
				hasPre = True
				# c = c.replace(':','.')
				preDataR = c.split(':')
				preData = preDataR[1]
				c = preDataR[0]

			for col in appInfo[__.appReg]['columns']:
				if 'sort' in list(col.keys()) and len(col['sort']):
					for a in col['abbreviation'].split(','):
						if a.lower() == c.lower():
							# print_(a,c)
							# sys.exit()
							c = col['sort']
				else:
					for a in col['abbreviation'].split(','):
						if a.lower() == c.lower():
							# print_(a,c)
							# sys.exit()
							c = col['name']
			if hasPre:
				c = preData + ':' + c
				# c = c + '.' + preData

			result += c + ','
		result = result[:-1]
	# print_( result )

	col=[]
	for i,co in enumerate(result.split(',')):
		if i in sorting:
			c = sorting[i] +':'+co
		else: c = co
		col.append(c)
	result=','.join(col)

	# print(result)
	# sys.exit()
	return result


def formatColumnsSortOld(columns):
	# print_(__.appReg)
	# print_(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if '.' in c or ':' in c:
				hasPre = True
				c = c.replace(':','.')
				preDataR = c.split('.')
				preData = preDataR[1]
				c = preDataR[0]

			for col in appInfo[__.appReg]['columns']:
				if 'sort' in list(col.keys()) and len(col['sort']):
					for a in col['abbreviation'].split(','):
						if a.lower() == c.lower():
							c = col['sort']
				else:
					for a in col['abbreviation'].split(','):
						if a.lower() == c.lower():
							c = col['name']
			if hasPre:
				c = preData + '.' + c
				# c = c + '.' + preData

			result += c + ','
		result = result[:-1]
	# print_( result )
	return result

def plusCloseClean(data):
	return data.replace( '%','' )

defaultScriptTriggers_run = False

def defaultScriptTriggers():
	global defaultScriptTriggers_run
	defaultScriptTriggers_run = True
	__.appReg_bk = __.appReg

def print_epoch_trigger(item):
	print_( 'epoch:', __.startTime  )

default_switch_trigger_index={}
def default_switch_trigger(name,script):
	global default_switch_trigger_index
	default_switch_trigger_index[name]=script

def defaultScriptTriggers_do():
	global defaultScriptTriggers_run
	global default_switch_trigger_index
	for name in default_switch_trigger_index:
		switches.trigger(name,default_switch_trigger_index[name])

	if defaultScriptTriggers_run:
		if len(appInfo[__.appReg_bk]['columns']) > 0:

			switches.trigger('Column',formatColumns)
			switches.trigger('Sort',formatColumnsSort)
			switches.trigger('GroupBy',formatColumns)
		switches.trigger('PlusClose',plusCloseClean)
		switches.trigger('Ago',timeAgo)
		switches.trigger('PrintEpoch',print_epoch_trigger)
		# switches.trigger('Aggregate',aggregate_trigger)
		switches.postScripts.append( aggregate_trigger )


printAutoAbbreviations_scheduled = False
def autoAbbreviations():
	global printAutoAbbreviations_scheduled
	# return False
	global myFileLocation_File
	if not type( myFileLocation_File ) == bool:
		if not len( appInfo[__.appReg]['columns'] ) and myFileLocation_File.lower().endswith('.json'):
			
			printAutoAbbreviations_scheduled = True
			data = []
			groups = {}
			myFileLocation_File_Data = getTable2( myFileLocation_File )
			if type( myFileLocation_File_Data ) == dict:
				myFileLocation_File_Data = [myFileLocation_File_Data]
			for i,key in enumerate( myFileLocation_File_Data[0].keys()):
				# print_( key )
				record = {}
				record['id'] = i
				record['key'] = key
				record['first'] = key[:1].lower()
				record['second'] = key[:2].lower()
				record['third'] = key[:3].lower()
				wf = ''
				for w in key.replace( '_', ' ' ).split( ' ' ):
					wf += w[:1].lower()
				record['firstofword'] = wf


				for k in record.keys():
					try:
						if not type(groups[ k ]) == dict:
							groups[ k ] = {}
					except Exception as e:
						groups[ k ] = {}

					try:
						if not type(groups[ k ][ record[k] ]) == dict:
							groups[ k ][ record[k] ] = {}
					except Exception as e:
						groups[ k ][ record[k] ] = {}
						groups[ k ][ record[k] ]['ids'] = []


				for k in record.keys():
					groups[ k ][ record[k] ]['ids'].append( i )
				
				data.append( record )


			approvedAbbreviations= []
			flag = False
			flagged= []

			for k in groups['first'].keys():
				approvedAbbreviations.append({ 'key': data[groups['first'][k]['ids'][0]]['key'], 'abbreviations': k })
				if not len(groups['first'][k]['ids']) == 1:
					flag = True
					for i,idx in enumerate(groups['first'][k]['ids']):
						if not i == 0:
							flagged.append({ 'first': k, 'id': idx, 'assigned': False })

			
			if flag:
				flagsResolved = 0
				for k in groups['firstofword'].keys():
					if len(k) > 1:
						for x in groups['firstofword'][k]['ids']:
							for i,f in enumerate(flagged):
								if not flagged[i]['assigned']:
									if flagged[i]['id'] == x:
										flagsResolved += 1
										flagged[i]['assigned'] = True
										approvedAbbreviations.append({ 'key': data[x]['key'], 'abbreviations': k })

				if not flagsResolved == len(flagged):
					for k in groups['second'].keys():
						for x in groups['second'][k]['ids']:
							for i,f in enumerate(flagged):
								if not flagged[i]['assigned']:
									if flagged[i]['id'] == x:
										flagsResolved += 1
										flagged[i]['assigned'] = True
										approvedAbbreviations.append({ 'key': data[x]['key'], 'abbreviations': k })

				if not flagsResolved == len(flagged):
					for k in groups['third'].keys():
						for x in groups['third'][k]['ids']:
							for i,f in enumerate(flagged):
								if not flagged[i]['assigned']:
									if flagged[i]['id'] == x:
										flagsResolved += 1
										flagged[i]['assigned'] = True
										approvedAbbreviations.append({ 'key': data[x]['key'], 'abbreviations': k })         

				if not flagsResolved == len(flagged):
					for i,f in enumerate(flagged):
						if not flagged[i]['assigned']:
							print_( 'Error: abbreviation', data[flagged[i]['id']]['key'] )


			# printVar( groups )
			# printVar( data )

			for aa in approvedAbbreviations:
				appInfo[__.appReg]['columns'].append({'name': aa['key'], 'abbreviation': aa['abbreviations']})
			if switches.isActive('PrintAutoAbbreviations'):
				print_()
				print_('Columns and abbreviations:')
				result = ''
				for col in appInfo[__.appReg]['columns']:
					result += col['name'] + '(' + col['abbreviation'] + '), '
				result = result[:-2]
				print_('\t' + result + '\n')
				print_()

			defaultScriptTriggers()
			# sys.exit()
			# print_(first)


def printAutoAbbreviations():
	global printAutoAbbreviations_scheduled
	if printAutoAbbreviations_scheduled and switches.isActive('PrintAutoAbbreviations'):
		print_()
		print_('Columns and abbreviations:')
		result = ''
		for col in appInfo[__.appReg]['columns']:
			result += col['name'] + '(' + col['abbreviation'] + '), '
		result = result[:-2]
		print_('\t' + result + '\n')
		print_()



#########################################################################################################################################################


class ThisThread( threading.Thread ):
	
	
	def __init__( self, name, fn=None, a=None, t=None, k=None, timeout=120, start=True, qID=None ):
		threading.Thread.__init__(self)
		self.qID = qID
		self.name = name
		self.fn = fn
		self.arg = a
		self.kwargs = k

		if not t is None:
			timeout = t

		self.killOn = timeout


		self.epoch = 0
		self.endTime = None
		self.duration = None

		self.wasKilled = False

		self.log = {}
		self._stop_event = threading.Event()
		self.target = self.run
		if start:
			# print_( 'pre start' )
			# self.run()
			self.start()
			# print_( 'post start' )



	def run( self ):
		# for x in dir(self):
		#   print_(x)
		# print_('run')
		# print_('xx',self.isAlive())
		self.epoch = time.time()
		completed = False
		error = False
		try:
			if not self.arg is None:
				self.fn(self.arg)
			else:
				if self.kwargs is None:
					self.fn()
				elif type(self.kwargs) == dict:
					self.fn(**self.kwargs)
				elif type(self.kwargs) == list or type(self.kwargs) == tuple:
					self.fn(*self.kwargs)
				elif type(self.kwargs) == str:
					self.fn(self.kwargs)
			completed = True
		except Exception as e:
			error = True
		finally:
			self.endTime = time.time()
			self.duration = self.endTime - self.epoch
			# print_()
			# _.colorThis(  [ self.tID, 'ended' ], 'red'  )
			ended = ''
			if self.wasKilled:
				ended += ' killed '
			if error:
				ended += ' error '
			if completed:
				ended += ' completed '

			self.log = {
								'id': self.getID(),
								'qID': self.qID,
								'name': self.name,
								'start': self.epoch,
								'end': self.endTime,
								'duration': self.duration,
								'ended': ended,
			}

	def getID( self ):

		for id, thread in threading._active.items():
			if thread is self:
				return id
 
	def kill( self ):
		# print_( 'kill started' )
		self.wasKilled = True
		self._stop_event.set()
		# thread_id = self.getID()
		# """ {7DB6A001-0637-4F13-B328-2B17A481CF35} """
		# import ctypes
		# # print_( 'kill id', thread_id )
		# res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
		#     ctypes.py_object(SystemExit))
		# if res > 1:
		#   ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
		# print_( 'kill complete' )
		# raise Exception('My error!')
		



#########################################################################################################################################################

class Threads:
	# Threads.openCnt
	# Threads.closedCnt
	openCnt = 0
	closedCnt = 0
	def __init__( self, name=None, func=None, arg=None, kwargs=None, focus=None, qID=None, addID=None, pID=None, timeout=None ):
		global appInfo
		if name is None:
			name = __.uuid()
		# Threads.openCnt += 1
		self.active = False
		
		self.created = time.time()
		if focus is None:
			focus = __.appReg
		self.app = appInfo[focus]['file']
		self.name = name
		self.func = func
		self.focus = focus
		self.arg = arg
		self.kwargs = kwargs
		self.qID = qID
		self.addID = addID
		self.created = time.time()
		self.status = True
		self.instance = ''
		self.bottom = False
		self.timeout = timeout
		self.hasTimedOut = 0
		self.pID = pID
		self.sstatus = 2



		self.data = False
		# self.trigger = False
		# self.triggerArg = False
		self.executed = False
		self.triggerError = False
		
		self.thisThread = None

		__.threadActivity[self.qID] = {}
		__.threadActivity[self.qID]['error'] = False
		__.threadActivity[self.qID]['activity'] = time.time()
		__.threadActivity[self.qID]['log'] = False

		# try:
		#   self.instance = appInfo[focus]['instance']
		# except Exception as e:
			


		self.log = { 
						'id':       self.qID,
						'parent':   self.pID,
						'app':      self.app,
						'func':     'unknown',
						'arg':      'unknown',
						'instance': self.instance,
						'focus':    self.focus,
						'start':    0,
						'end':      0,
						'runtime':  0,
						'mem':      0,
						'lines':      0,
						'wait':     0,
						'qcount':   0
		}
		try:
			self.log['func'] = self.func.__name__
		except Exception as e:
			pass

		self.log['arg'] = _profile.records.audit(  self.name+' - '+str(self.qID)  , self.arg )
		# if not type(self.arg) == str and not type(self.arg) == list and not type(self.arg) == dict and not type(self.arg) == int and not type(self.arg) == float and not type(self.arg) == tuple:
		#     try:
		#         self.log['arg'] = str(self.arg)
		#     except Exception as e:
		#         pass
		# else:



		try:
			self.argID = self.arg
			self.argID.append( self.qID )
		except Exception as e:
			self.argID = False
		self.open()
	def getLog( self ):
		self.log['error'] = __.threadActivity[self.qID]['error']
		self.log['activity'] = __.threadActivity[self.qID]['activity']
		self.log['errorlog'] = __.threadActivity[self.qID]['log']
		if self.thisThread is None:
			self.log['thisThread'] = None
		else:
			self.log['thisThread'] = self.thisThread.log
		# try:
		# except Exception as e:
		#     pass
		return self.log

		

	def open( self ):
		# print_('open 0')
		self.sstatus = 1
		__.queueLastActivity = time.time()
		self.active = True
		self.log['start'] = time.time()
		self.log['qcount'] = __.queueCount

		if self.kwargs:
			if self.addID:
				data = [{ 'func': self.func, 'args': self.arg[:-1] }]
				data[0]['args'][0]['qID']=self.qID
				self.thisThread = ThisThread(
												qID = self.qID,
												name = self.name+' - '+str(self.qID),
												fn = self.func,
												k = data[0]['args'][0],
												t = self.timeout,
												start = True,
				)
				# threadTimer( .0001, threadKwargs, data, qID=self.qID )
			else:
				data = [[{ 'func': self.func, 'args': self.arg }]]
				self.thisThread = ThisThread(
												qID = self.qID,
												name = self.name+' - '+str(self.qID),
												fn = self.func,
												k = self.arg,
												t = self.timeout,
												start = True,
				)
				# threadTimer( .0001, threadKwargs, data, qID=self.qID )
		else:
			if self.addID:
				self.thisThread = ThisThread(
												qID = self.qID,
												name = self.name+' - '+str(self.qID),
												fn = self.func,
												a = self.qID,
												t = self.timeout,
												start = True,
				)
				# threadTimer( .0001, self.func, self.argID, qID=self.qID )
			else:
				self.thisThread = ThisThread(
												qID = self.qID,
												name = self.name+' - '+str(self.qID),
												fn = self.func,
												a = self.arg,
												t = self.timeout,
												start = True,
				)
				# threadTimer( .0001, self.func, self.arg, qID=self.qID )
		# print_('open 1')

	def close( self, mem=0, data=False, trigger=False, triggerArg=False, kwargs=False, lines=0 ):
		self.sstatus = 0
		__.queueLastActivity = time.time()
		if not type(trigger) == bool:
			try:
				triggerName = trigger.__name__
			except Exception as e:
				triggerName = ''

			try:



				if type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger )
				elif not type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger, data )
				elif type(data) == bool and not type(triggerArg) == bool:
					threadTimer( .0001, trigger, triggerArg )
				elif not type(data) == bool and not type(triggerArg) == bool and kwargs:
					args = [{ 'func': trigger, 'args': triggerArg }]
					args[0]['args'][0]['data'] = data
					threadTimer( .0001, threadKwargs, args )
				elif not type(data) == bool and not type(triggerArg) == bool and not kwargs:
					try:
						triggerArg.append(data)
						threadTimer( .0001, threadKwargs, triggerArg )
					except Exception as e:
						try:
							triggerArg[0].append(data)
							threadTimer( .0001, threadKwargs, triggerArg )
						except Exception as e:
							printBold('close trigger error '+str(self.focus)+' '+ str(self.name) +' '+ str(self.func)+' '+ str(triggerName), 'red' )
							self.triggerError = True


				self.executed = True
				if self.triggerError:
					self.executed = False
			except Exception as e:
				printBold('close trigger error '+str(self.focus)+' '+ str(self.name) +' '+ str(self.func)+' '+ str(triggerName), 'red')
				self.triggerError = True

		

		# Threads.closedCnt += 1
		# print_('Closed:',self.qID,'\tTotal Closed:',Threads.newCounter,'\tScheduler:',__.queueCountScheduleAudit,__.queueCountSchedule,'\tTimers:',__.queueCountTimer)
		self.status = False
		self.log['end'] = time.time()
		self.log['runtime'] = self.log['end'] - self.log['start']
		self.log['mem'] = mem
		self.log['lines'] = lines
		if not type(data) == bool:
			self.data = data
		return self.qID

	def openCnt( self ):
		return Threads.openCnt

	def closedCnt( self ):
		return Threads.closedCnt
#########################################################################################################################################################
class Queue:

	def __init__( self ):

		self.created = time.time()
		self.loadedBy = 0
		self.loadTime = 0
		self.completionTime = 0
		self.lastActivity = 0
		self.lastActivityEach = {}
		
		# self.qID_index = {}

		self.records = {}
		self.nextID = 0
		self.opened = 0
		self.closed = 0
		self.notstarted = 0
		self.maxInQueue = 0
		self.maxThreads = 100
		self.maxThreadsSafe = 100
		self.minThreads = 50
		self.table = {'focus': [], 'name': []}
		self.schedulerInitialized = False


		self.auditPrint = True
		self.maxThreadsAuto = True
		self.auditInitialized = False
		self.auditPercentChangeMax = 30
		self.auditPercentChangeMin = 10
		self.auditPercentReduceBy = 5
		self.auditPercentReduceByDrastic = 15
		self.auditPercentDrasticThreshold = 3
		self.auditWatchMax = 5
		self.auditPercentSample = 10
		self.auditMaxFailuresBeforeAction = 3
		self.auditLogInternal = []
		self.auditLogExternal = []
		self.auditAutoAdjust = False


		##
		self.scheduleLoop = .01
		self.auditLoop = .1
		self.autoLoadedAfter = 5
		self.statusTotal = 0
		self.prefix = False
		##


		self.autoLoaded = True

		self.report = False
		self.reportPrinted = False


		self.timeout = False
		self.timeoutAsk = False


		self.saveLog = True
		self.isLoaded = False

		self.appStructure = __.structure()

		__.totalTask = 0
		__.queueCount = 0
		__.queueCountSchedule = 0
		__.queueCountAudit = 0
		__.queueCountScheduleAudit = 0
		__.queueCountAuditAudit = 0
		__.queueLastActivity = time.time()
		__.queueCountTimer = 0

		__.threadActivity = {}

		self.projectDataMaxLen = 2000
		self.projectDataDetected = False
		__.datadumps = 0
		__.projectData = {}
		__.pdID = {}
		__.saveInitiated = False

		self.listeningFor = False



	def killAll( self ):



		for focus in self.records.keys():
			for i, threads in enumerate( self.records[focus]['threads'] ):
				if not threads.thisThread is None and threads.sstatus == 1:

					name = self.records[focus]['threads'][i].name
					qID = self.records[focus]['threads'][i].qID

					self.records[focus]['threads'][i].hasTimedOut = 1
					self.records[focus]['threads'][i].thisThread.kill()
					self.spent( qID, 0 )

		self.isLoaded = True
		for focus in self.records.keys():
			for name in self.records[focus]['names'].keys():
				self.records[focus]['names'][name]['loaded'] = True
				self.spendFocus( name, focus, 99 )



# func=False, arg=False, kwargs=False, focus=False , addID=True , 
# loaded=False,
# , pID=False


	
	def register( self, name, trigger=None, triggerArg=False, triggerKwargs=False,  timeout=False, database=False, focus=None,      completed=None, onComplete=None,      oc=None, c=None, a=None, k=None, t=None, d=None  ):
		if not completed is None:
			trigger = completed
		if not onComplete is None:
			trigger = onComplete
		if not oc is None:
			trigger = oc
		if not c is None:
			trigger = c

		if not a is None:
			triggerArg = a
		if not k is None:
			triggerKwargs = k
		if not t is None:
			timeout = t
		if not d is None:
			database = d



		loaded = False



		# print_('arg:',arg)
		# print_( name, type( trigger ) )
		# sys.exit()
		nextID = False
		global appInfo
		self.lastActivity = time.time()

		if focus is None:
			focus = __.appReg
		pass

		try:
			self.lastActivityEach[focus][name] = time.time()
		except Exception as e:
			self.lastActivityEach[focus] = {}
			self.lastActivityEach[focus][name] = time.time()



		try:
			__.projectData[focus]
		except Exception as e:
			__.projectData[focus] = {}

		__.projectData[focus][name] = {}
		# if not 'folder' in name:
		#   print_( 'zero' )
		#   sys.exit()

		__.projectData[focus][name][0] = {}
		__.projectData[focus][name][0]['saveInitiated'] = False
		# print_( 'check3:', focus, name, 0 )
		__.projectData[focus][name][0]['data'] = []

		__.projectData[focus][name][1] = {}
		__.projectData[focus][name][1]['saveInitiated'] = False
		# print_( 'check4:', focus, name, 1 )
		__.projectData[focus][name][1]['data'] = []

		try:
			__.pdID[focus]
		except Exception as e:
			__.pdID = {}
			__.pdID[focus] = {}


		__.pdID[focus][name] = 0

		if self.maxThreadsAuto:
			maxThreads = self.maxThreadsSafe
		else:
			maxThreads = self.maxThreads
		if trigger is None:
			trigger = False

		try:
			self.records[focus]['names'][name] = {
													'timeout': timeout,
													'loaded': loaded,
													'trigger': trigger,
													'maxThreads': maxThreads,
													'failure': 0,
													'changes': 0,
													'watch': 0,
													'closed': 0,
													'database': database,
													'executed': False,
													'projectSaveInitiated': False,
												}
		except Exception as e:
			self.records[focus] = {
										'threads': [],
										'open': 0,
										'app': appInfo[focus]['file'],
										'names': {
												name: {
													'timeout': timeout,
													'loaded': loaded,
													'trigger': trigger,
													'maxThreads': maxThreads,
													'failure': 0,
													'changes': 0,
													'watch': 0,
													'closed': 0,
													'database': database,
													'executed': False,
													'projectSaveInitiated': False,
												}
										}
			}



		pass
		self.isLoaded = False
		self.records[focus]['names'][name]['loaded'] = loaded
		if not self.auditAutoAdjust:
			# print_(focus,name)
			if self.maxThreadsAuto:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreadsSafe
			else:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreads


		if not loaded:
			self.records[focus]['names'][name]['loaded'] = False

		if not trigger is None:
			self.records[focus]['names'][name]['trigger'] = trigger
			if not triggerArg is None:
				self.records[focus]['names'][name]['triggerArg'] = triggerArg
			else:
				self.records[focus]['names'][name]['triggerArg'] = False



		if not self.auditInitialized and self.maxThreadsAuto:
			self.auditInitialized = True
			threadTimer( self.auditLoop, threadAudit )
			# Timer( .3, threadAudit ).start()

		return nextID



	def add( self, name, func=False, arg=False, kwargs=False, focus=False , addID=True , trigger=False, triggerArg=False, triggerKwargs=False, loaded=False, timeout=False, database=False, pID=False ):
		# print_('arg:',arg)
		# print_( name, type( trigger ) )
		# sys.exit()
		nextID = False
		global appInfo
		self.lastActivity = time.time()

		if type(focus) == bool:
			focus = __.appReg

		try:
			self.lastActivityEach[focus][name] = time.time()
		except Exception as e:
			self.lastActivityEach[focus] = {}
			self.lastActivityEach[focus][name] = time.time()

		try:
			self.records[focus]['threads']
			self.records[focus]['names'][name]['loaded'] = loaded
		except Exception as e:

			try:
				__.projectData[focus]
			except Exception as e:
				__.projectData[focus] = {}

			__.projectData[focus][name] = {}
			# if not 'folder' in name:
			#   print_( 'zero' )
			#   sys.exit()

			__.projectData[focus][name][0] = {}
			__.projectData[focus][name][0]['saveInitiated'] = False
			# print_( 'check3:', focus, name, 0 )
			__.projectData[focus][name][0]['data'] = []

			__.projectData[focus][name][1] = {}
			__.projectData[focus][name][1]['saveInitiated'] = False
			# print_( 'check4:', focus, name, 1 )
			__.projectData[focus][name][1]['data'] = []

			try:
				__.pdID[focus]
			except Exception as e:
				__.pdID = {}
				__.pdID[focus] = {}


			__.pdID[focus][name] = 0

			if self.maxThreadsAuto:
				maxThreads = self.maxThreadsSafe
			else:
				maxThreads = self.maxThreads
			try:
				self.records[focus]['names'][name] = {
														'timeout': timeout,
														'loaded': loaded,
														'trigger': trigger,
														'maxThreads': maxThreads,
														'failure': 0,
														'changes': 0,
														'watch': 0,
														'closed': 0,
														'database': database,
														'executed': False,
														'projectSaveInitiated': False,
													}
			except Exception as e:
				self.records[focus] = {
											'threads': [],
											'open': 0,
											'app': appInfo[focus]['file'],
											'names': {
													name: {
														'timeout': timeout,
														'loaded': loaded,
														'trigger': trigger,
														'maxThreads': maxThreads,
														'failure': 0,
														'changes': 0,
														'watch': 0,
														'closed': 0,
														'database': database,
														'executed': False,
														'projectSaveInitiated': False,
													}
											}
				}


		if type(timeout) == bool:
			timeout = self.records[focus]['names'][name]['timeout']


		self.isLoaded = False
		self.records[focus]['names'][name]['loaded'] = loaded
		if not self.auditAutoAdjust:
			# print_(focus,name)
			if self.maxThreadsAuto:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreadsSafe
			else:
				self.records[focus]['names'][name]['maxThreads'] = self.maxThreads


		if not loaded:
			self.records[focus]['names'][name]['loaded'] = False

		if not type(trigger) == bool:
			self.records[focus]['names'][name]['trigger'] = trigger
			if not type(triggerArg) == bool:
				self.records[focus]['names'][name]['triggerArg'] = triggerArg
			else:
				self.records[focus]['names'][name]['triggerArg'] = False

		if not type(func) == bool:
			self.table['focus'].append(focus)
			# self.table['name'].append(name)
			nextID = self.nextID
			# self.qID_index[ (qID) ] = { 'focus': focus, 'name': name }
			self.records[focus]['threads'].append( Threads( name, func, arg, kwargs, focus, nextID, addID, pID=pID, timeout=timeout ) )

			shouldOpen = False
			if not self.records[focus]['names'][name]['maxThreads']:
				shouldOpen = True
			elif self.opened > self.records[focus]['names'][name]['maxThreads']:
				shouldOpen = True
			if not shouldOpen:
				self.notstarted += 1
			else:
				pass
				# self.records[focus]['threads'][nextID].open()
				# self.cnt( focus, True )
			self.nextID += 1
			if not self.schedulerInitialized and True:
				self.schedulerInitialized = True
				threadTimer( self.scheduleLoop, threadSchedule )
				# Timer( self.scheduleLoop, threadSchedule ).start()

		if not self.auditInitialized and self.maxThreadsAuto:
			self.auditInitialized = True
			threadTimer( self.auditLoop, threadAudit )
			# Timer( .3, threadAudit ).start()

		return nextID

	def loadedGroup( self, name=False , focus=False ):

		if self.autoLoaded:

			if type(focus) == bool:
				focus = __.appReg


			hasChildren = False
			for rec in self.records[focus]['threads']:
				if rec.focus == focus and rec.name == name:
					# if name == 'processMovies':
					#     colorThis( [ 'processMovies' ], 'red' )
					hasChildren = True


			if hasChildren:
				self.records[focus]['names'][name]['loaded'] = True



	def loaded( self, name=False , focus=False ):


		if self.autoLoaded:

			if type(focus) == bool:
				focus = __.appReg


			hasChildren = False
			for rec in self.records[focus]['threads']:
				if rec.focus == focus and rec.name == name:
					# if name == 'processMovies':
					#     colorThis( [ 'processMovies' ], 'red' )
					hasChildren = True


			if hasChildren:
				# self.isLoaded = True
				if not type(name) == bool:
					self.records[focus]['names'][name]['loaded'] = True
					# name = str(list(self.records[focus]['names'].keys())[0])
				else:
					for f in self.records.keys():
						for n in self.records[f]['names'].keys():
							if not self.records[f]['names'][n]['loaded']:
								self.records[f]['names'][n]['loaded'] = True


		pass
		allComplete = True
		for f in self.records.keys():
			for n in self.records[f]['names'].keys():
				if not self.records[f]['names'][n]['loaded']:
					allComplete = False
		if allComplete:
			self.isLoaded = True


	def spent( self, qID, mem=0, data=False, trigger=False, triggerArg=False, kwargs=False, lines=0 ):
		qID = int(qID)
		focus = False
		result = False
		for i,t in enumerate(self.records[self.table['focus'][qID]]['threads']):
			if self.records[ self.table['focus'][qID] ]['threads'][i].qID == qID:
				result = self.records[self.table['focus'][qID]]['threads'][i].close( mem, data, trigger, triggerArg, kwargs, lines )
				focus = self.table['focus'][qID]
				name = self.records[self.table['focus'][qID]]['threads'][i].name
		if not type(focus) == bool:
			self.cnt( focus, False )

			# if self.isEverythingLoadedEach(  focus,  name  ) and self.notstarted == 0:
			if self.isEverythingLoadedEach(  focus,  name  ) and self.isEverythingClosedEach( focus, name ):
				self.spendFocus( name, focus, 1 )
				self.printReport()
		return result



	def printReport( self ):
		if not self.reportPrinted:
			self.completionTime = time.time() - self.created
			if self.report:
				self.reportPrinted = True
				print_('__________________________________________')
				print_()
				print_('opened:',self.opened)
				# print_('records open:',self.records[focus]['open'])
				print_('isEverythingLoaded:',time.time()-self.loadedBy,time.time()-self.lastActivity)
				print_('spendFocus')
				print_('queueCountSchedule:',__.queueCountSchedule)
				print_('queueCountAudit:',__.queueCountAudit)
				print_('audit:',__.queueCountAudit)
				print_()
				print_('load time:\t', int(self.loadTime))
				print_('time after load:\t', int(time.time()-self.loadedBy))
				print_()
				print_('app time:\t', int(self.completionTime))
				print_()
				print_('maxInQueue:',self.maxInQueue)
				# str((self.completionTime/1000)%60)
				print_()
				print_('timeouts:',self.timeoutCount())
				# print_("Average of the list =", round(average, 2)) 
				print_()
				print_('__________________________________________')
			elif self.statusTotal > 0:
				cTime = round(self.completionTime,2)
				if cTime > 60:
					ncTime = str(round((self.completionTime/60),2)) + ' min'
				else:
					ncTime = str(round(self.completionTime,2)) + ' sec'
				print_('App time: ' + str(ncTime), end='\r', flush=True)
				# sys.stdout.flush()

	def spendFocus( self, name, focus, which ):


		# print_( 'spendFocus which:', which )

		# print_( 'HERE: 0' )
		self.saveData()
		# print_( 'HERE: 1' )

		if not self.records[focus]['names'][name]['executed']:
			if not type( self.records[focus]['names'][name]['trigger'] ) == bool:
				if not type( self.records[focus]['names'][name]['triggerArg'] ) == bool:
					# Timer(.0001, self.records[focus]['names'][name]['trigger'], self.records[focus]['names'][name]['triggerArg']).start()
					# print_( '\trunning 0' )
					self.records[focus]['names'][name]['trigger'](**self.records[focus]['names'][name]['triggerArg'])

				else:
					# print_( '\trunning 1' )
					self.records[focus]['names'][name]['trigger']()
			self.records[focus]['names'][name]['executed'] = True
		# print_( 'HERE: 2' )


	def log( self, name=False, focus=False ):
		if type(focus) == bool:
			focus = __.appReg
		log = []
		if not type(name) == bool:
			for i,t in enumerate(self.records[focus]['threads']):
				if self.records[focus]['threads'][i].name == name:
					log.append(self.records[focus]['threads'][i].getLog())
		else:
			for i,t in enumerate(self.records[focus]['threads']):
				for n in self.records[focus]['names']:
					if self.records[focus]['threads'][i].name == n:
						log.append(self.records[focus]['threads'][i].getLog())

		for f in self.records:
			self.records[f]['threads'] = False
			for n in self.records[f]['names']:
				if not type(self.records[f]['names'][n]['trigger']) == bool:
					self.records[f]['names'][n]['trigger'] = True



		return {
					'session': _v.session(),
					'created': self.created,
					'loadedby': self.loadedBy,
					'loadtime': self.loadTime,
					'lastactivity': self.lastActivity,
					'completiontime': self.completionTime,
					'nextid': self.nextID,
					'maxinqueue': self.maxInQueue,
					'totaltask': __.totalTask,
					'records': self.records,
					'maxthreadssafe': self.maxThreadsSafe,
					'projectdatamaxlen': self.projectDataMaxLen,
					'datadumps': __.datadumps,
					'appstructure': __.structure(),
					'threadlog': log
		}

	def cnt( self, focus, up ):
		# self.maxThreadsSafe
		# self.maxThreads
		if up:
			if self.opened > self.maxInQueue:
				self.maxInQueue = self.opened
			self.lastActivity = time.time()
			self.records[focus]['open'] += 1
			self.opened += 1
			__.queueCount += 1
		else:
			self.closed += 1
			self.records[focus]['open'] -= 1
			self.opened -= 1
			__.queueCount -= 1

	def schedule( self ):
		Timer = __.imp('threading.Timer')
		__.queueCountSchedule += 1
		__.queueCountScheduleAudit -= 1



		if self.opened > self.maxThreads and self.notstarted > 0:
			pass
			time.sleep(.02)
			# Timer( self.scheduleLoop, threadSchedule ).start()
		else:

			i = 0 
			while self.opened < self.maxThreads-10 and i < self.notstarted:
				# time.sleep(.02)
				# print_( 'open:', self.opened, 'max:', self.maxThreads )
				# if self.opened < self.maxThreads-10 and i < self.notstarted:
				chosen = self.nextInQueue()
				if type(chosen) == bool:
						return False
				else:
					try:
						self.records[chosen['focus']]['threads'][chosen['qID']].open()
						self.notstarted -= 1
						self.cnt( chosen['focus'], True )
						i += 1
					except Exception as e:
						time.sleep(.2)
						try:
							self.records[chosen['focus']]['threads'][chosen['qID']].open()
							self.notstarted -= 1
							self.cnt( chosen['focus'], True )
							i += 1
						except Exception as e:
							time.sleep(.2)
							try:
								self.records[chosen['focus']]['threads'][chosen['qID']].open()
								self.notstarted -= 1
								self.cnt( chosen['focus'], True )
								i += 1
							except Exception as e:
								pass


		if self.notstarted > 0:
			try:
				Timer( self.scheduleLoop, threadSchedule ).start()
			except Exception as e:
				time.sleep(.2)
				try:
					Timer( self.scheduleLoop, threadSchedule ).start()
				except Exception as e:
					time.sleep(.2)
					try:
						Timer( self.scheduleLoop, threadSchedule ).start()
					except Exception as e:
						time.sleep(.2)
						try:
							Timer( self.scheduleLoop, threadSchedule ).start()
						except Exception as e:
							pass




	def nextInQueue( self ):
		chosen = False
		try:
			for key in self.records.keys():
				for i,q in enumerate(self.records[key]['threads']):
					if not self.records[key]['threads'][i].active:
						chosen = { 'focus': key, 'qID': self.records[key]['threads'][i].qID }
			if type(chosen) == bool:
				# print_('active:',self.checkActive())
				return False
		except Exception as e:
			chosen = False
		return chosen

	def checkActive( self ):
		active = 0
		for key in self.records.keys():
			for i,q in enumerate(self.records[key]['threads']):
				if not self.records[key]['threads'][i].active:
					active += 1
		return active

	def isEverythingLoaded( self ):
		loaded = True
		shouldRun = True
		if self.loadedBy > 0:
			if self.loadedBy > self.lastActivity:
				shouldRun = False
		
		if shouldRun:
			for f in self.records.keys():
				for n in self.records[f]['names'].keys():
					if not self.records[f]['names'][n]['loaded']:
						loaded = False
			if loaded:
				self.loadedBy = time.time()
				self.loadTime = self.loadedBy - self.created
				# self.isLoaded = True
		return loaded

	def isEverythingClosedEach( self, focus, name ):

		closed = 0
		total = 0
		for key in self.records.keys():
			for i,q in enumerate(self.records[key]['threads']):
				if self.records[key]['threads'][i].name == name and self.records[key]['threads'][i].focus == focus:
					total += 1
					if self.records[key]['threads'][i].sstatus == 0:
						closed += 1
		if total and closed and total == closed:
			return True
		return False

	def isEverythingLoadedEach( self, focus, name ):
		f = focus
		n = name



		hasChildren = False
		for rec in self.records[focus]['threads']:
			if rec.focus == focus and rec.name == name:
				# if name == 'processMovies':
				#     colorThis( [ 'processMovies' ], 'red' )
				hasChildren = True


		if not hasChildren:
			loaded = False
		if hasChildren:



			diff = int(time.time() - self.lastActivityEach[focus][name])
			if diff > self.autoLoadedAfter:
				self.loadedGroup( name=name , focus=focus )


			loaded = True
			shouldRun = True
			# if self.loadedBy > 0:
			#     if self.loadedBy > self.lastActivityEach[focus][name]:
			#         shouldRun = False
			
			if shouldRun:

				if not self.records[f]['names'][n]['loaded']:
					loaded = False

				if loaded:
					self.loadedBy = time.time()
					self.loadTime = self.loadedBy - self.created
					# self.isLoaded = True



			allComplete = True
			for f in self.records.keys():
				for n in self.records[f]['names'].keys():
					if not self.records[f]['names'][n]['loaded']:
						allComplete = False
			if allComplete:
				self.isLoaded = True


		return loaded



	def getRuntimeMemoryFocus( self, focus ):
		runtime = []
		memory = []
		runtimeMemory = []
		for i,q in enumerate(self.records[focus]['threads']):
			if not self.records[key]['threads'][i].status:
				run = self.records[focus]['threads'][i].log['runtime']
				mem = self.records[focus]['threads'][i].log['mem']
				runtime.append( run )
				memory.append( mem )
				runtimeMemory.append({ 'runtime': run, 'mem': mem })

		return { 'runtime': runtime, 'mem': memory, 'runmem': runtimeMemory, 'averagemem': self.calcAverage(memory), 'averageruntime': self.calcAverage(runtime)  }

	def getRuntimeMemoryNameFocus( self, name, focus ):
		runtime = []
		runtimebottom = []
		memory = []
		runtimeMemory = []
		self.numberClosed()
		if self.records[focus]['names'][name]['closed'] < 5:
			return False

		for i,q in enumerate(self.records[focus]['threads']):
			if not self.records[focus]['threads'][i].status and self.records[focus]['threads'][i].name == name:
				run = self.records[focus]['threads'][i].log['runtime']
				mem = self.records[focus]['threads'][i].log['mem']
				runtime.append( run )
				memory.append( mem )
				runtimeMemory.append({ 'runtime': run, 'mem': mem })
			if not self.records[focus]['threads'][i].status and self.records[focus]['threads'][i].name == name and not self.records[focus]['threads'][i].bottom:
				self.records[focus]['threads'][i].bottom = True
				runtimebottom.append( run )

			if len(runtime) == 0 or len(memory) == 0 or len(runtimebottom) == 0 :
				return False

		try:

			data = {
					'runtime': runtime,
					'runtimebottom': runtimebottom,
					'mem': memory,
					'runmem': runtimeMemory,
					'averagemem': self.calcAverage(memory),
					'averageruntime': self.calcAverage(runtime)
		}

		except Exception as e:
			data = False
			# print_(memory)

		return data

	def getRuntimeMemoryReport( self ):
		self.runtime = []
		self.mem = []
		self.runtimeMemory = []
		self.averagemem = 0
		self.averageruntime = 0
		for key in self.records.keys():
			for i,q in enumerate(self.records[key]['threads']):
				if not self.records[key]['threads'][i].status:
					run = self.records[key]['threads'][i].log['runtime']
					mem = self.records[key]['threads'][i].log['mem']

					self.runtime.append( run )
					self.mem.append( mem )
					self.runtimeMemory.append({ 'runtime': runtime, 'mem': mem })

		self.averagemem = self.calcAverage(mem)
		self.averageruntime = self.calcAverage(runtime)
		return { 'runtime': runtime, 'mem': mem, 'runmem': self.runtimeMemory, 'averagemem': self.averagemem, 'averageruntime': self.averageruntime }


	def calcAverage( data ):
		return round(data, 2)

	def saveData( self ):

		sqlite3 = __.imp('sqlite3')
		for focus in __.projectData:
			try:
				del __.projectData[focus][0]
			except Exception as e:
				pass
			for name in __.projectData[focus].keys():
				logName = 'auto_' + self.records[focus]['app'] + '_' + name + '_' + str(self.created)
				for pdID in __.projectData[focus][name].keys():
					if len(__.projectData[focus][name][pdID]['data']):
						__.datadumps += 1
						if type(self.records[focus]['names'][name]['database']) == bool or self.records[focus]['names'][name]['database'] is None:
							if len(__.projectData[focus][name][pdID]['data']) > 0:
								
								saveTableSplitNew( __.projectData[focus][name][pdID]['data'], logName, project=True )
								print_( 'check0:', focus, name, pdID )
								if not 'folder' in name:
									print_( 'zero' )
									sys.exit()
								__.projectData[focus][name][pdID]['data'] = []
						else:
							print_()
							print_('Data saved to:',self.records[focus]['names'][name]['database'])
							print_()


							if len(__.projectData[focus][name][pdID]['data']) > 0:
								try:
									conn = sqlite3.connect(self.records[focus]['names'][name]['database'])
									cursor = conn.cursor()
									errors = []
									for sql in __.projectData[focus][name][pdID]['data']:
										try:
											cursor.execute( sql )
										except Exception as e:
											errors.append( sql )
									conn.commit()
									conn.close()
									if len(errors) > 0:
										saveTableSplitNew( errors, logName+'__ERRORS__', project=True )
								except Exception as e:
									saveTableSplitNew( __.projectData[focus][name][pdID]['data'], logName, project=True )
									print_( 'check1:', focus, name, pdID )
								if not 'folder' in name:
									print_( 'zero' )
									sys.exit()
								__.projectData[focus][name][pdID]['data'] = []



	def manageData( self ):
		sqlite3 = __.imp('sqlite3')
		self.data = {}
		self.data[0] = 0
		self.data[1] = 0
		for focus in __.projectData:
			# print_( 'focus:', focus )
			try:
				del __.projectData[focus][0]
			except Exception as e:
				pass
			for name in __.projectData[focus].keys():
				logName = 'auto_' + self.records[focus]['app'] + '_' + name + '_' + str(self.created)
				for pdID in __.projectData[focus][name].keys():
					if not type(__.projectData[focus][name][pdID]['saveInitiated']) == bool:
						# print_('saveInitiated:',__.projectData[focus][name][pdID]['saveInitiated'])
						# print_()
						# print_(len( __.projectData[focus][name][ __.projectData[focus][name][pdID]['saveInitiated']['pdID'] ]['data'] ), __.projectData[focus][name][pdID]['saveInitiated']['size'] )
						# print_()
						if len( __.projectData[focus][name][ __.projectData[focus][name][pdID]['saveInitiated']['pdID'] ]['data'] ) > __.projectData[focus][name][pdID]['saveInitiated']['size']:
							__.projectData[focus][name][pdID]['saveInitiated']['timeSizeChange'] = time.time()
						else:
							# print_()
							# print_('got here')
							# print_()

							diff = time.time() - __.projectData[focus][name][pdID]['saveInitiated']['timestamp']
							print_()
							# print_()
							# print_('diff:',diff)
							# print_()
							print_( 'diff:', diff )
							print_( __.projectData[focus][name][pdID]['saveInitiated']['size'], len(__.projectData[focus][name][  __.projectData[focus][name][pdID]['saveInitiated']['pdID']  ]['data']))
							if diff > __.projectData[focus][name][pdID]['saveInitiated']['startAfterNoChangeFor']:
								__.datadumps += 1
								if type(self.records[focus]['names'][name]['database']) == bool or self.records[focus]['names'][name]['database'] is None:
									tmpData = __.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data']
									print_( 'save started' )
									saveTableSplitNew( tmpData, __.projectData[focus][name][pdID]['saveInitiated']['logname'], project=True )
									tmpData = []
									print_( 'post split save:', len(__.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data']) )
									__.projectData[__.projectData[focus][name][pdID]['saveInitiated']['focus']][__.projectData[focus][name][pdID]['saveInitiated']['pdID']] = []
									if not 'folder' in name:
										print_( 'zero' )
										sys.exit()
									__.projectData[focus][name][pdID]['saveInitiated'] = False
									threadTimer( .5, enableThreadDataSwap )
							
								else:
									print_()
									print_('Data saved to:',self.records[focus]['names'][name]['database'])
									print_()
									# try:
									conn = sqlite3.connect(self.records[focus]['names'][name]['database'])
									cursor = conn.cursor()
									errors = []
									for sql in __.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data']:
										try:
											cursor.execute( sql )
										except Exception as e:
											errors.append( sql )
									conn.commit()
									conn.close()
									if len(errors) > 0:
										saveTableSplitNew( errors, logName+'__ERRORS__', project=True )
									# except Exception as e:
									#   saveTableSplitNew( __.projectData[focus][name][__.projectData[focus][name][pdID]['saveInitiated']['pdID']]['data'], __.projectData[focus][name][pdID]['saveInitiated']['logname'], project=True )
									


									# __.projectData[focus][name][  __.projectData[focus][name][pdID]['saveInitiated']['pdID']  ]['data'] = []
									if not 'folder' in name:
										print_( 'zero' )
										sys.exit()
									__.projectData[focus][name][pdID]['saveInitiated'] = False
									threadTimer( .5, enableThreadDataSwap )



		tmpData = []

		if not __.saveInitiated:
			for focus in __.projectData:
				try:
					del __.projectData[focus][0]
				except Exception as e:
					pass
				for name in __.projectData[focus].keys():
					for pdID in __.projectData[focus][name].keys():
						# print_('data len:',len(__.projectData[focus][name][pdID]['data']))
						# print_('projectDataMaxLen:',self.projectDataMaxLen)
						if len(__.projectData[focus][name][pdID]['data']):
							self.projectDataDetected = True

							# print_()
							# print_( len(__.projectData[focus][name][pdID]['data']), self.projectDataMaxLen )
							# print_()

							if len(__.projectData[focus][name][pdID]['data']) >= self.projectDataMaxLen:
								
								if __.pdID[focus][name] == 0:
									__.pdID[focus][name] = 1
									print_( 'NOW: 1' )
								else:
									__.pdID[focus][name] = 0
									print_( 'NOW: 0' )
								
								logname = 'auto_' + self.records[focus]['app'] + '_' + str(self.created)
								__.saveInitiated = True

								__.processing = [ focus, name, pdID ]

								__.projectData[focus][name][pdID]['saveInitiated'] = {
															'logname': logname,
															'pdID': pdID,
															'focus': focus,
															'timestamp': time.time(),
															'size': len(__.projectData[focus][name][pdID]['data']),
															'startAfterNoChangeFor': 3,
															'timeSizeChange': 0,

								}


			# self.timeout = False
			# self.timeoutAsk = False
			


	def listen( self, qID, trigger=False, triggerArg=False, kwargs=False, data=False  ):
		try:
			self.listeningFor['active']
		except Exception as e:
			self.listeningFor = []
		self.listeningFor.append( { 'active': True, 'qID': qID, 'trigger': trigger, 'triggerArg': triggerArg, 'kwargs': kwargs, 'data': data } )

	def listener( self ):
		for li,listen in enumerate(self.listeningFor):
			if self.listeningFor[li]['active']:
				for focus in self.records.keys():
					for i,q in enumerate(self.records[focus]['threads']):
						if self.records[focus]['threads'][i].qID == listen['qID'] and not self.records[focus]['threads'][i].status:
							thisData0 = self.records[focus]['threads'][i].data
							thisData1 = self.listeningFor[li]['data']
							thisData = False
							if sys.getsizeof(thisData0) > sys.getsizeof(thisData1):
								thisData = thisData0
							elif sys.getsizeof(thisData0) < sys.getsizeof(thisData1):
								thisData = thisData1
							self.listeningFor[li]['data'] = False
							self.listeningFor[li]['active'] = False
							self.records[focus]['threads'][i].data = False
							self.listenActivated( self.listeningFor[li]['trigger'], self.listeningFor[li]['triggerArg'], self.listeningFor[li]['kwargs'], thisData )


	def listenActivated( self, trigger=False, triggerArg=False, kwargs=False, data=False  ):

		__.queueLastActivity = time.time()
		if not type(trigger) == bool:
			try:
				triggerName = trigger.__name__
			except Exception as e:
				triggerName = ''

			try:

				if type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger )
				elif not type(data) == bool and type(triggerArg) == bool:
					threadTimer( .0001, trigger, [data] )
				elif type(data) == bool and not type(triggerArg) == bool:
					threadTimer( .0001, trigger, triggerArg )
				elif not type(data) == bool and not type(triggerArg) == bool and kwargs:
					args = [{ 'func': trigger, 'args': triggerArg }]
					try:
						args[0]['args'][0]['data'] = data
					except Exception as e:
						args[0]['args']['data'] = data

					
					# print_(args)
					threadTimer( .0001, threadKwargs, args )
				elif not type(data) == bool and not type(triggerArg) == bool and not kwargs:
					try:
						triggerArg.append(data)
						threadTimer( .0001, threadKwargs, triggerArg )
					except Exception as e:
						try:
							triggerArg[0].append(data)
							threadTimer( .0001, threadKwargs, triggerArg )
						except Exception as e:
							print_('listener trigger error')


			except Exception as e:
				print_('listener trigger error')


	def printStatus( self ):
		pDone = str(int(percentageDiffInt(self.closed, self.statusTotal)))
		if not type( self.prefix ) == bool:
			print_(' ' + self.prefix + ':', pDone + '%' , end='\r')
		else:
			print_(' ' + pDone + '%' , end='\r')
		sys.stdout.flush()

	def timeoutCount( self ):
		cnt = 0
		for focus in self.records.keys():
			for i,q in enumerate(self.records[focus]['threads']):

				if self.records[focus]['threads'][i].hasTimedOut:
					cnt += 1
		return cnt

				

	def kill( self, qID ):

		qID = int(qID)
		focus = None
		rID = None
		for i,t in enumerate(self.records[self.table['focus'][qID]]['threads']):
			if self.records[ self.table['focus'][qID] ]['threads'][i].qID == qID:
				focus = self.table['focus'][qID]
				name = self.records[self.table['focus'][qID]]['threads'][i].name
		
				self.spent( qID, 0 )
				self.records[focus]['threads'][i].hasTimedOut = 1
				self.records[focus]['threads'][i].thisThread.kill()



	def checkTimeout( self ):

		for focus in self.records.keys():
			for i, threads in enumerate( self.records[focus]['threads'] ):
				if not threads.thisThread is None:
					if threads.status and threads.timeout:
						dur = time.time() - threads.log['start']
						if dur > threads.timeout:
							# print_( 'time ran out',threads.qID )
							# print_( 'time ran out',threads.qID )
							# print_( 'time ran out',threads.qID )


							# for x in dir(threads.thisThread):
							#     print_(x)

							# sys.exit()


							self.spent( threads.qID, 0 )
							self.records[focus]['threads'][i].hasTimedOut = 1
							self.records[focus]['threads'][i].thisThread.kill()
							# print_( 'stopped' )



		# return None
		# if self.opened:
		#     for focus in self.records.keys():
		#         for i, threads in enumerate( self.records[focus]['threads'] ):
		#             if not threads.thisThread is None:
		#                 if threads.status and threads.timeout:
		#                     print_( 'Has timeout' )
		#                     dur = time.time() - threads.log['start']
		#                     if dur > threads.timeout:
		#                         print_( 'time ran out' )
		#                         self.spent( threads.qID, 0 )
		#                         self.records[focus]['threads'][i].hasTimedOut = 1
		#                         self.records[focus]['threads'][i].thisThread.kill()
		#                         self.records[focus]['threads'][i].thisThread.join()
		#                         print_( 'stopped' )



		# if not type( self.timeout ) == bool:
		#     for focus in self.records.keys():
		#         for i,q in enumerate(self.records[focus]['threads']):
		#             if self.records[focus]['threads'][i].status:
		#                 diff = time.time() - self.records[focus]['threads'][i].created
		#                 if diff > self.timeout:
		#                     self.records[focus]['threads'][i].timeout = True
		#                     __.threadQueue[  self.records[focus]['threads'][i].qID  ]._stop()

		# for focus in self.records.keys():
		#     for name in self.records[focus]['names'].keys():
		#         if not type( self.records[focus]['names'][name]['timeout'] ) == bool:
		#             for i,q in enumerate(self.records[focus]['threads']):
		#                 if name == self.records[focus]['threads'][i].name:
		#                     if self.records[focus]['threads'][i].status:
		#                         diff = time.time() - self.records[focus]['threads'][i].created
		#                         if diff > self.records[focus]['names'][name]['timeout']:
		#                             self.records[focus]['threads'][i].timeout = True
		#                             __.threadQueue[  self.records[focus]['threads'][i].qID  ]._stop()
							

		
	def audit( self ):
		if not type(self.listeningFor) == bool:
			self.listener()
		self.schedule()
		self.checkTimeout()
		self.isEverythingLoaded()
		__.queueCountAudit += 1
		__.queueCountAuditAudit -= 1
		self.numberClosed()
		if not self.isLoaded:
			if self.autoLoaded:

				diff2 = int(time.time() - __.queueLastActivity)
				diff = int(time.time() - self.lastActivity)
				if diff > self.autoLoadedAfter:
					if diff2 > self.autoLoadedAfter:
						if self.auditPrint:
							print_('Auto Loaded:', diff)

						for focus in self.records.keys():
							for name in self.records[focus]['names'].keys():
								self.loaded( name=name, focus=focus )
						
						self.numberClosed()


		self.manageData()



		if self.auditPrint:
			if self.projectDataDetected:

				if False:
					print_()
					print_()
					print_('Opened:',self.opened,'\tClosed:',self.totalClosed,'\tClosed:',self.closed,'\tTotal:',self.nextID,'\tMax in queue:',self.maxInQueue,'\tTotal Task:',__.totalTask,'\tTotal Audit:',__.queueCountScheduleAudit+__.queueCountSchedule )
					print_()
				for focus in __.projectData:
					try:
						del __.projectData[focus][0]
					except Exception as e:
						pass
					for name in __.projectData[focus].keys():
						print_( 'pre:', focus, name, __.projectData[focus].keys() )
						print_( '0:', len(__.projectData[focus][name][0]['data']), focus, name )
						print_( '1:', len(__.projectData[focus][name][1]['data']), focus, name )
						if len(__.projectData[focus][name][0]['data']) or len(__.projectData[focus][name][1]['data']):
							if False:
								print_('Name:',name, '\tProject 0 Length:', len(__.projectData[focus][name][0]['data']), '\tProject 1 Length:', len(__.projectData[focus][name][1]['data']),'\tdb:',self.records[focus]['names'][name]['database'] )
							if True:
								print_('Name:',name, '\tOpened:',self.opened,'\tClosed:',self.closed,'\tTotal:',self.nextID,'\tMax in queue:',self.maxInQueue,'\tTotal Task:',__.totalTask, '\tProject 0 Length:', len(__.projectData[focus][name][0]['data']), '\tProject 1 Length:', len(__.projectData[focus][name][1]['data']),'\tdb:',self.records[focus]['names'][name]['database'] )
			else:
				print_('Opened:',self.opened,'\tClosed:',self.closed,'\tTotal:',self.nextID,'\tMax in queue:',self.maxInQueue,'\tTotal Task:',__.totalTask,'\tTotal Audit:',__.queueCountScheduleAudit+__.queueCountSchedule )
			# print_( self.opened, self.isLoaded, self.notstarted )
			if False:
				print_()
				print_( self.opened, self.isLoaded, self.notstarted )
				print_()

		elif self.statusTotal > 0:
			self.printStatus()

		pass
		# if self.opened == 0:
		for f in self.records.keys():
			for n in self.records[f]['names'].keys():
				if self.isEverythingLoadedEach( name=n, focus=f ) and self.isEverythingClosedEach( name=n, focus=f ):
					self.spendFocus( n, f, 2 )


		if self.opened == 0 and self.isLoaded and self.notstarted <= 0:
			if self.auditPrint:
				print_('audit:',__.queueCountAudit)
			self.printReport()
			self.saveData()
			if self.saveLog:
				threadTimer( 1, saveThreadsLog )

			for f in self.records.keys():
				for n in self.records[f]['names'].keys():
					self.spendFocus( n, f, 2 )


		else:
			diff = self.nextID - self.opened

			if diff < 5:
				threadTimer( self.auditLoop, threadAudit )
				# Timer( .5, threadAudit ).start()
			else:
				for f in self.records.keys():
					for n in self.records[f]['names'].keys():

						data = self.getRuntimeMemoryNameFocusTopBottom( n, f )
						if type(data) == bool:
							threadTimer( self.auditLoop, threadAudit )
							# Timer( .5, threadAudit ).start()
							return False
						else:
							diff = percentageDiffInt(data['top'], data['bottom'])
							diff2 = percentageDiffInt(data['top'], data['freshbottom'])

							if diff < self.auditPercentChangeMax or diff2 < self.auditPercentChangeMax:
								self.records[f]['names'][n]['failure'] = 0
								self.records[f]['names'][n]['changes'] = 0
								self.records[f]['names'][n]['watch'] = 0
								shouldAct = False
							else:
								if not self.records[f]['names'][n]['watch'] >= self.auditWatchMax:
									self.records[f]['names'][n]['watch'] += 1
								else:
									self.records[f]['names'][n]['failure'] += 1
									self.records[f]['names'][n]['changes'] += 1
								shouldAct = True

							if shouldAct:
								
								if self.records[f]['names'][n]['failure'] >= self.auditMaxFailuresBeforeAction:
									lastMax = self.records[f]['names'][n]['maxThreads']
									if self.records[f]['names'][n]['changes'] >= self.auditPercentDrasticThreshold:
										changeBy = self.auditPercentReduceByDrastic
									else:
										changeBy = self.auditPercentReduceBy

									newMax = percentageInt(self.opened, changeBy)

									if newMax < self.minThreads:
										newMax = self.minThreads
									if newMax > self.maxThreadsSafe:
										newMax = self.maxThreadsSafe
									self.auditAutoAdjust = True
									self.records[f]['names'][n]['maxThreads'] = newMax
									print_('_________________________________________')
									print_()
									print_('Changed max threads from:', lastMax,'to:',newMax)

				threadTimer( self.auditLoop, threadAudit )
				# Timer( .5, threadAudit ).start()
	# self.auditWatchMax

# watch

#                           if self.records[f]['names'][n]['maxThreads'] == 0:
#                               newMax = self.opened
#                       percentageInt(percent, whole)
#                       if not self.records[f]['names'][n]['loaded']:
#                           self.records[f]['names'][n]['maxThreads'] = True

#                           self.records[f]['names'][n]['maxThreads'] = 


#       self.auditPercentReduceByOverMax = 15       self.maxThreads = 1000
#       self.auditPercentReduceByOverMaxBy = 30


# self.auditPercentReduceByDrastic
#       self.auditPercentChangeMin = 10
#       self. = 5

#       self.auditPercentChangeMin = 10
#       self.auditPercentReduceBy = 5

# self.records[focus]['names'][name]['maxThreads']
# self.auditPercentChangeMax
#           __.queueCountAudit += 1
#           Timer( .5, threadSchedule ).start()

# threadTimer
# thread = Timer( .0001, threadKwargs, data ).start()
# thread = Timer( .0001, threadKwargs, data ).start()
# thread = Timer( .0001, self.func, self.argID ).start()
# thread = Timer( .0001, self.func, self.arg ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( .3, threadAudit ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( self.scheduleLoop, threadSchedule ).start()
# Timer( .5, threadAudit ).start()
# Timer( .5, threadAudit ).start()
# Timer( .5, threadAudit ).start()


# __.queueCountScheduleAudit = 0
# __.queueCountAuditAudit = 0


	def numberClosed( self ):
		self.isEverythingLoaded()
		totalClosed = 0
		for f in self.records.keys():
			for i,t in enumerate(self.records[f]['threads']):
				for n in self.records[f]['names'].keys():
					if not self.records[f]['threads'][i].name == n:
						self.records[f]['names'][n]['closed'] = 0 


		info = {}
		for f in self.records.keys():
			for i,t in enumerate(self.records[f]['threads']):
				if not self.records[f]['threads'][i].status:
					for n in self.records[f]['names'].keys():
						if self.records[f]['threads'][i].name == n:
							try:
								info[n]['total'] += 1
								info[n]['closed'] += 1
							except Exception as e:
								info[n] = {}
								info[n]['total'] = 0
								info[n]['closed'] = 0
								info[n]['total'] += 1
								info[n]['closed'] += 1
							if not self.records[f]['threads'][i].status:
								self.records[f]['names'][n]['closed'] += 1
								totalClosed += 1
						# if info[n]['total'] == info[n]['closed'] and info[n]['total'] > 0 and self.opened == 0 and self.isEverythingLoaded() and self.notstarted == 0:
							if self.isEverythingLoadedEach( name=n, focus=f ) and self.isEverythingClosedEach( name=n, focus=f ):
								self.spendFocus( n, f, 3 )
								# if not type( self.records[f]['names'][n]['trigger'] ) == bool:
								

		self.totalClosed = totalClosed



	def getRuntimeMemoryNameFocusTopBottom( self, name, focus ):
		topruntime = []
		bottomruntime = []
		bottomruntimeFresh = []
		
		length = len(self.records[focus]['threads'])
		sampleSize = percentageInt( self.auditPercentSample, length )
		bottom = length - sampleSize
		data = self.getRuntimeMemoryNameFocus( name, focus )
		if type(data) == bool:
			return False
		if len(data['runtimebottom']) < 5:
			return False
		else:

			for i,row in enumerate(data['runtime']):
				if i <= sampleSize:
					topruntime.append(row)
				if i >= bottom:
					bottomruntime.append(row)
			for i,row in enumerate(data['runtimebottom']):
					bottomruntimeFresh.append(row)

			topaverageruntime = self.calcAverage(topruntime)
			bottomaverageruntime = self.calcAverage(bottomruntime)
			freshbottomaverageruntime = self.calcAverage(bottomruntimeFresh)

			return { 'top': topaverageruntime, 'bottom': bottomaverageruntime, 'freshbottom': freshbottomaverageruntime }


	def getRuntimeMemoryFocusTopBottom( self, focus ):
		topruntime = []
		bottomruntime = []
		
		length = len(self.records[focus]['threads'])
		sampleSize = percentageInt( self.auditPercentSample, length )
		bottom = length - sampleSize
		data = self.getRuntimeMemoryFocus( focus )

		for i,row in enumerate(data['runtime']):
			if i <= sampleSize:
				topruntime.append(row)
			if i >= bottom:
				bottomruntime.append(row)

		topaverageruntime = self.calcAverage(topruntime)
		bottomaverageruntime = self.calcAverage(bottomruntime)

		return { 'top': topaverageruntime, 'bottom': bottomaverageruntime }



def enableThreadDataSwap():
	print_( 'key test00:', __.projectData[ __.processing[0] ].keys() )
	print_( 'enableThreadDataSwap: initiated' )
	# print_( __.processing )
	print_( 'post process size:', len(__.projectData[ __.processing[0] ][ __.processing[1] ][   __.processing[2]   ]['data']) )
	__.saveInitiated = False
	
	# __.projectData[focus][name][0]['data'] = []
	print_( 'key test0:', __.projectData[ __.processing[0] ].keys() )
	# __.projectData[ __.processing[0] ][ __.processing[1] ][   __.processing[2]   ]['data'] = []
	# __.projectData[ '__main__' ][ 'folder' ][   __.processing[2]   ]['data'] = []
	print_( 'key test1:', __.projectData[ __.processing[0] ].keys() )

# def hasTimedOut():
#   print_( 'hasTimedOut' )

# @timeout( 10, hasTimedOut() )
def threadTimer( tim, func, args=False, qID=False ):
	Timer = __.imp('threading.Timer')
	__.totalTask += 1
	# print_(func.__name__)
	shouldRun = True
	if func.__name__ == 'threadSchedule':
		if __.queueCountScheduleAudit > 4:
			shouldRun = False
		else:
			__.queueCountScheduleAudit += 1

	if func.__name__ == 'threadAudit':
		if __.queueCountAuditAudit > 4:
			shouldRun = False
		else:
			__.queueCountAuditAudit += 1

	if shouldRun:
		if tim < .01:
			tim = .01

		try:
			if type(args) == bool:
				if not type(qID) == bool:
					__.threadQueue[qID] = Timer( tim, func )
					__.threadQueue[qID].start()
				else:
					Timer( tim, func ).start()
			else:
				if not type(qID) == bool:
					__.threadQueue[qID] = Timer( tim, func, args )
					__.threadQueue[qID].start()
				else:
					Timer( tim, func, args ).start()
			__.queueCountTimer += 1
			# https://stackoverflow.com/questions/34562473/most-pythonic-way-to-kill-a-thread-after-some-period-of-time
			# __.threadQueue[qID].join(30)
			# if __.threadQueue[qID].is_alive():
			#   print_( 'Has Timed Out' )
			#   e.set()
			# else:
			#   pass
		except Exception as e:
			print_('Thread Error:',__.queueCountTimer)


def threadAudit():
	global threads
	threads.audit()

def threadSchedule():
	global threads
	threads.schedule()

def threadKwargs( data=False ):
	# print_(data)
	try:
		data['func'](**data['args'][0])
	except Exception as e:
		try:
			data[0]['func'](**data['args'][0])
		except Exception as e:
			print_('Error: kwargs')



def percentageInt( percent, whole, isFloat=False ):
	# return int((percent * whole) / 100.0)
	if not isFloat:
		return int(round( (percent * whole) / 100.0 , 0))
	else:
		return round( (percent * whole) / 100.0 , 1)

def percentageDiffInt( smaller, bigger, isFloat=False, rnd=1 ):
	# fr = force rounding
	# return int((smaller/bigger)*100)
	try:

		if not isFloat:
			return int(round( abs(smaller/bigger)*100, 0))
		else:
			r = round( abs(smaller/bigger)*100, rnd)
			if str(r) == '0.0':
				return 0
			# if str(r).endswtih('.0'):
			#     return int(r)

			return r

	except Exception as e:
		return 0
		smaller+=1
		bigger+=1
		if not isFloat:
			return int(round( abs(smaller/bigger)*100, 0))
		else:
			r = round( abs(smaller/bigger)*100, rnd)
			if str(r) == '0.0':
				return 0
			return r

def percentageDiff( smaller, bigger, isFloat=False ):
	# fr = force rounding
	# return int((smaller/bigger)*100)
	try:

		if not isFloat:
			return abs(smaller/bigger)*100
		else:
			r = abs(smaller/bigger)*100
			if str(r) == '0.0':
				return 0
			# if str(r).endswtih('.0'):
			#     return int(r)

			return r

	except Exception as e:
		return 0
		smaller+=1
		bigger+=1
		if not isFloat:
			return abs(smaller/bigger)*100
		else:
			r = abs(smaller/bigger)*100
			if str(r) == '0.0':
				return 0
			return r


def percentageDiffIntAuto( smaller, bigger, isFloat=False ):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	if not isFloat:
		return percentageDiffInt(s, b)
	else:
		result = round(float((s/b)*100), 1)
		r = str(result)
		if '.0' in r:
			result = int(result)
		return result

def percentageDiffAuto( smaller, bigger, isFloat=False, rnd=1 ):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	return percentageDiffCalc(s, b, isFloat, rnd)

def percentageDiffSmaller( smaller, bigger, isFloat=False, rnd=1 ):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	a = percentageDiffCalc(s, b, isFloat, rnd)
	b = percentageDiffCalc(b, s, isFloat, rnd)
	if a<b:
		return a
	else:
		return b



def percentageDiffCalc( smaller, bigger, isFloat=False, rnd=1 ):
	# x=abs(abs(smaller - bigger)/smaller)*100
	try:

		if not isFloat:
			return int(round( abs(abs(smaller - bigger)/smaller)*100, 0))
		else:
			r = round( abs(abs(smaller - bigger)/smaller)*100, rnd)
			if str(r) == '0.0':
				return 0
			# if str(r).endswtih('.0'):
			#     return int(r)

			return r

	except Exception as e:
		return 0
		smaller+=1
		bigger+=1
		if not isFloat:
			return int(round( abs(abs(smaller - bigger)/smaller)*100, 0))
		else:
			r = round( abs(abs(smaller - bigger)/smaller)*100, rnd)
			if str(r) == '0.0':
				return 0
			return r


	 # = 0.2 = 20%
 # |5 - 6|/5 = 1/5 = 0.2 = 20%


	# return percentageDiffInt(s, b, isFloat, rnd)


###################################################################################################################
""" {7DB6A001-0637-4F13-B328-2B17A481CF35}
	print_('got here 2')

def loadingGraphic():
	# return False
	import tkinter as tk
	from PIL import Image, ImageTk
	from itertools import count, cycle

	global theLoadingGraphic

	class ImageLabel(tk.Label):
		
		#A Label that displays images, and plays them if they are gifs

		#:im: A PIL Image instance or a string filename
		
		def load(self, im):
			if isinstance(im, str):
				im = Image.open(im)
			frames = []

			try:
				for i in count(1):
					frames.append(ImageTk.PhotoImage(im.copy()))
					im.seek(i)
			except EOFError:
				pass
			self.frames = cycle(frames)

			try:
				self.delay = im.info['duration']
			except:
				self.delay = 100

			if len(frames) == 1:
				self.config(image=next(self.frames))
			else:
				self.next_frame()

		def unload(self):
			self.config(image=None)
			self.frames = None

		def next_frame(self):
			if self.frames:
				self.config(image=next(self.frames))
				self.after(self.delay, self.next_frame)

	theLoadingGraphic = tk.Tk()
	theLoadingGraphic.wait_visibility(theLoadingGraphic)
	lbl = ImageLabel(theLoadingGraphic)
	lbl.pack()
	lbl.load( _v.dance )
	theLoadingGraphic.mainloop()

def loadingGraphicEnd():
	# return False
	global theLoadingGraphic
	print_('got here 1')
	# theLoadingGraphic.destroy()
	# theLoadingGraphic.quit()
"""
###################################################################################################################

def isText( data ):
	if type( data ) == str:

		return True
	else:
		return False

def isNum( data ):
	if type( data ) == int:
		return True
	else:
		return False

def isFloat( data ):
	if type( data ) == str:
		t = ''
		for x in data:
			if not x in '.0123456789':
				return False
			else:
				t += x

		try:
			data = float(t)
		except Exception as e:
			return False

	if type( data ) == float:
		return True
	else:
		return False

###################################################################################################################


class Field:

	def __init__( self, project, name, value, appReg, script, maxField ):
		self.appReg = appReg
		self.project = project
		self.name = name
		self.trigger = script
		self.maxField = maxField



		self.registerValue( value )

	def setTrigger( self, script ):
		self.trigger = script

	def addPadding( self, value, extra, right, center ):
		value = self.runTrigger( str(value) )
		oValue = value
		addPadding = (extra + self.maxField) - len( value )
		add = ''
		i=0
		l=''
		r=''
		while not len(value) >= self.maxField+extra:
			i+=1
			if(i%2==0):
				l+=' '
			else:
				r+=' '
			value += ' '
			add += ' '
		# for x in range(1,addPadding+1):
		#   value += ' '
		# return str(self.maxField)+' '+str(len( value ))+value
		if right:
			value = add + oValue
		if center:
			value = l + oValue + r
		return value

	def addPaddingSetSpaces( self, value ):
		value = self.runTrigger( str(value) )
		addPadding = self.maxField - len( value )
		newValue = value
		Zeros = ''
		while not len(newValue) == self.maxField:
			Zeros += ' '
			newValue = Zeros + value
		return newValue

	def addPaddingZeros( self, value ):
		value = self.runTrigger( str(value) )
		addPadding = self.maxField - len( value )
		newValue = value
		Zeros = ''
		while not len(newValue) == self.maxField:
			Zeros += '0'
			newValue = Zeros + value
		return newValue

	def runTrigger( self, value ):
		if type( self.trigger ) == bool:
			return value

		# print_( 'HERE' )
		return self.trigger( value )

	def registerValue( self, value ):
		thisLen = len( self.runTrigger( str(value) ) )

		if thisLen > self.maxField:
			self.maxField = thisLen



class Fields:

	def __init__(self):
		self.fields = {}
		self.extra = 0

	def lengths( self, project ):
		result = {}
		for record in self.fields[project]:
			if record.project == project:
				result[record.name] = record.maxField
			
		return result
		

	def register( self, project='', names='', value='', appReg=False, script=False, maxField=None,        p=None, n=None, v=None, m=None, isRegisterDic=False ):

		# if project in self.fields:
		#   if not isRegisterDic:
		#       del self.fields[ project ]

		if not p is None:
			project = p

		if not n is None:
			names = n

		if not v is None:
			value = v

		maxField = 0

		if not maxField is None:
			maxField = maxField
			
		if not m is None:
			maxField = m


		if type(appReg) == bool:
			appReg = __.appReg
		if not project in self.fields:
			self.fields[project] = []
		for name in names.split(','):

			shouldAdd = True

			for i,s in enumerate(self.fields[project]):
				if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
					shouldAdd = False
			if shouldAdd:
				self.fields[project].append( Field( project, name, value, appReg, script, maxField ) )
				if maxField and type(value) == int:
					return self.fields[project][len(self.fields[project])-1].addPaddingZeros(value)
				elif maxField and type(value) == str:
					return self.fields[project][len(self.fields[project])-1].addPadding(value)
			else:
				self.registerValue( project, name, value, appReg )

	def registerValue( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		
		result = False
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				self.fields[project][i].registerValue( value )
				result = True
		return result


	def padZeros( self, project, name, value, extra=None, appReg=False, space=False ):

		if extra is None:
			extra = self.extra

		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				if space:
					return self.fields[project][i].addPaddingSetSpaces( value )
				else:
					return self.fields[project][i].addPaddingZeros( value )
				result = self.fields[project][i].addPaddingZeros( value )
		return result


	def value( self, project, name, value, extra=None, right=False, appReg=False,    r=None, center=False ):
		result = value
		if not r is None:
			right = r

		if extra is None:
			extra = self.extra

		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				result = self.fields[project][i].addPadding( value, extra, right, center )
		return result
	def valuez( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				result = self.fields[project][i].addPaddingZeros( value )
		return result

	def asset( self, project, asset, appReg=False ):
		self.fields[project] = []
		if type(appReg) == bool:
			appReg = __.appReg

		if type( asset ) == dict:
			self.registerDic( project, asset, appReg )

		if type( asset ) == list:
			for row in asset:
				if type( row ) == dict:
					self.registerDic( project, row, appReg )


	def registerDic( self, project, asset, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg

		for name in asset.keys():
			self.register( project, name, asset[name], appReg, isRegisterDic=True )

# _.fields.register( 'project', 'name', script=_.resolveEpochTest )
# _.fields.asset( 'project', {} )
# _.fields.asset( 'project', [{}] )
# _.fields.register( 'project', 'name', value, appReg=focus() )
# _.fields.register( 'project', 'name', value )
# _.fields.value( 'project', 'name', value )

###################################################################################################################



thisTest = 'hello'



errors = []
appInfo = {}
appData = {}

argvProcess = True

fields = Fields()

threads = Queue()
switches = Switches()
tables = Tables()
databases = Databases()
__.databases = Databases()


def appInfoDump():
	global appInfo
	for k in appInfo.keys():
		print_()
		print_(k,appInfo[k])



def appInfoDump2():
	global appInfo
	for k in appInfo.keys():
		print_()
		print_(k,appInfo[k])



# def appInfoDump2():
#   global appInfo
#   for k in appInfo.keys():
#       print_(k,appInfo[k]['columns'])

switches_loaded = 0
def load():
	global switches_loaded
	switches_loaded += 1
	if switches_loaded > 1:
	# if True
		global switches
		global switchDefault

		# global tables

		# switches.trigger('Column',formatColumns)

		switchDefault = switches.length()
		switches.register('Help', '?,??,/?,/??,-?,-??,--??,/h,/help,-help,--help', 'copy  OR ids  OR  12  OR  ?? x')
		switches.register('Column', '-c,-column', 'size, name')
		switches.register('Sort','-s,-sort', 'a.type, d.ext')
		switches.register('Debug', '-debug')
		switches.register('DumpSwitches', '-dump')
		switches.register('Errors', '-Error,-Errors', '8,11 OR hide:8,11')
		switches.register('Timeout', '-t,-Timeout')
		switches.register('GroupBy', '-g,-group,-groupby', 'ext, month')
		switches.register('WrapTable', '-wrap', 'n p  OR  2  OR  path')
		switches.register('NoWrapTable', '-nowrap')
		# switches.register('NoTableLines', '-nolines')
		switches.register('YesTableLines', '-yl,-yeslines')
		switches.register('TableJSON', ',-tjson,-tablejson')
		switches.register('FieldTotal', '-fieldtotal', 'mem_usage')
		switches.register('Aggregate', '-aggregate', '" eof-field-len= add(len(version),len(backup)); config(var,eof,isFirst); "')
		switches.register('GroupSpaces', '-gs,-space,-groupspaces')
		switches.register('TableProfile', '-tp,-table',' *;c *;l  h;l header;left  size;l,gs')
		# switches.register('ShortenColumn', '-sc,-shortencolumn')
		switches.register('WebTable', '-web')
		switches.register('Long', '-long')
		switches.register('Short', '-sc,-short')
		switches.register('Length', '-length','x3')
		# switches.register('Report', '-report')
		switches.register('Plus', '+','all unless -or')
		switches.register('Minus', '-')
		switches.register('Plus-Sub', '++','any')
		switches.register('PlusOr', '-or')
		switches.register('PlusClose', '+close', '90%')
		switches.register('PlusCode', '+code','=  OR  *x  OR  x*  AND/OR color' )
		switches.register('PlusDuplicate', '+dup,+duplicate', '90%')
		switches.register('StrictCase', '-case,-strictcase')
		switches.register('PrintAutoAbbreviations', ',-printa,-aprint')
		switches.register('NoColor', '-nocolor', space=True)
		switches.register('LoadEpoch', '-loadepoch')
		switches.register('PrintEpoch', '-printepoch')
		switches.register('chmod', '-chmod,-777')
		switches.register( 'Paste-isData', '--pa,--paste,-ppa,-ppaste,-ispa,-idpa' )
		switches.register( 'Paste-isData-json', '--json,-pjson,-jsonp' )
		# switches.register('SkipColumnTriggers', '-skiptriggers')
		defaultScriptTriggers_do()
		



import importlib



regImps = {}



##############################

class regImp:

	def __init__( self, focus=None, app=None, argvProcessForce=False, dirty=False, a=None, i=None ):
		# if app == 'file-open': self.switch('Clean')
		DEFAULTS = {
						'file-open': {'Clean': 1},
		}


		if (not '__' and '.' in focus) or app is None:
			# pr('_.imp should be __.imp, auto corrected', focus, c='r')
			return __.imp(focus)

		if not a is None: app=a
		if not i is None: app=i
		global regImps
		global appInfo
		if app is None:
			err( 'class regImp', 'expected: _.regImp(__.appReg,app)  or _.regImp(focus(),app)' )

		if focus is None: focus = __.appReg

		regImps[focus] = {}

		# self.functions = autoKwargsGetArgsFromApp(app)

		self.app = app
		self.parent = focus
		# print_( 'self.imp = importlib.import_module', app )
		self.imp = importlib.import_module(app)
		# print(app)
		# print(app)
		# print(app)
		# for x in dir(self.imp):
		# 	print(x)
		# sys.exit()
		# self.imp = importlib.util.spec_from_file_location( app, _v.py + _v.slash + app + '.py' )
		# print_( os.path.isfile( _v.py + _v.slash + app + '.py' ) )
		# print_( self.imp )
		# print_( self.imp.test )
		# sys.exit()
		# print_(self.imp.focus())

		self.focus = self.imp.focus( parentApp=focus )
		# print('self.focus:',self.focus)
		self.focusPop = focus
		
		self.saveLog = True

		try:
			self.imp.registerSwitches( argvProcessForce=False)
		except Exception as e:
			self.imp.sw()

		appInfo[self.imp.focus(focus)] = appInfo[self.imp.focus()]
		appData[self.imp.focus(focus)] = appData[self.imp.focus()]
		__.constructRegistration(appInfo[self.imp.focus(focus)]['file'],self.imp.focus(focus))

		regImps[focus] = {}
		regImps[focus][app] = self.imp

		__.appReg = self.focusPop

		if dirty   and   not self.focus == '__init___-___init__':
			self.imp.appDBA = self.focus


		# self.provideImport()

		if app in DEFAULTS:
			for sw in DEFAULTS[app]:
				if type(DEFAULTS[app][sw]) == str:
					self.switch(sw,DEFAULTS[app][sw])
				elif DEFAULTS[app][sw]:
					self.switch(sw)
				else:
					self.switch(sw,delete=True)
		# if app == 'file-open': self.switch('Clean')


	def provideImport( self ):
		return self.imp

	def listFunctions( self ):
		self.functions
		for func in self.functions:
			print_( func['name'], func['args'] )

	def pipe( self, data=[], xfer=False, clear=True, appReg=False ):
		global appData
		if type(data) == bool:
			return appData[self.focus]['pipe']

		if type(appReg) == bool:
			appReg = self.focusPop

		if not len( data ):
			if xfer:
				data = appData[appReg]['pipe']
				if clear:
					appData[appReg]['pipe'] = []

		appData[self.focus]['pipe'] = data

		try:
			appData[self.focus]['data']['table']['received']
			
			profile = _profile.records.audit( 'pipe', data, appReg=[appReg,self.focus] )
			appData[appReg]['data']['table']['sent'].append( profile )
			appData[self.focus]['data']['table']['received'].append( profile )
		except Exception as e:
			pass

	def switch( self, names=[], value=None, appReg=False, dump=False, delete=False,        d=False ):
		global appData
		global switches

		if type(appReg) == bool:
			appReg = self.focusPop

		if dump:
			switches.dumpSwitches()
		else:
			for name in names.split(','):
				vl = value
				if name == 'Password' or name == 'Key':
					vl = '*******'
				if not value is None:
					try:
						appData[self.focus]['data']['field']['received']
						profile = _profile.records.audit( name, vl, appReg=[appReg,self.focus] )
						appData[appReg]['data']['field']['sent'].append( profile )
						appData[self.focus]['data']['field']['received'].append( profile )
					except Exception as e:
						pass


				# print_(self.focus)
				__.appReg = self.focus

				if delete or d:
					switches.fieldSet( name, 'active', False )

				else:

					switches.fieldSet( name, 'active', True )

					# if not type ( value ) == bool:
					if not value is None:
						if type( value ) == list:
							switches.fieldSet( name, 'values', value )
							switches.fieldSet( name, 'value', ','.join(value) )
						else:
							switches.fieldSet( name, 'value', value )
							switches.fieldSet( name, 'values', [value] )


			pass
		__.appReg = self.focusPop

	def deleteSwitch( self, name ):
		global switches
		__.appReg = self.focus

		switches.fieldSet( name, 'active', False )

		__.appReg = self.focusPop

	def action( self, arg='c766f06b', focusPop=True ):
		# focusBK = __.appReg
		__.appReg = self.focus

		self.imp.appDBA = self.focus
		if not arg == 'c766f06b':
			result = self.imp.action(arg)
		else:
			result = self.imp.action()

		if focusPop:
			__.appReg = self.focusPop

		return result


	# def do( self, func, arg=False, focusPop=True ):
	def do(self, *args, **kwargs):
		# focusBK = __.appReg
		focusPop=True

		args=list(args)
		if len(args) == 1 and args[0] == 'action': return self.action()
		func=args.pop(0)
		_kwargs={}
		for k in kwargs:
			if k == 'focusPop': focusPop=kwargs[k]
			else: _kwargs[k]=kwargs[k]

		__.appReg = self.focus

		if type( func ) == str:
			theFunction = eval( 'self.imp.' + func )
		else:
			theFunction = func

		result = 'theFunction'+fak(args,kwargs)


		# if type( arg ) == bool:
		# 	result = theFunction()
		# elif type( arg ) == dict:
		# 	result = theFunction(**arg)
		# elif type( arg ) == list:
		# 	result = theFunction(*arg)
		# else:
		# 	result = theFunction(arg)

		

		if focusPop:
			__.appReg = self.focusPop

		return result

	def execute( self, func, arg=False, nofocus=False ):
		global threads
		theFunc = eval('self.imp.'+func)

		shouldRun = True
		if not nofocus and  type(arg) == bool:
			args = [ self.focus ]
		elif not nofocus and  not type(arg) == bool:
			args = [ arg, self.focus ]

		if nofocus and  type(arg) == bool:
			shouldRun = False
			theID = threads.add( 'execute', theFunc, loaded=True )
		elif nofocus and  not type(arg) == bool:
			args = [ arg ]


		if shouldRun:

			theID = threads.add( 'execute', theFunc, args, loaded=True )

		# if self.saveLog:
		# else:
		#   theID = threads.add( 'execute', theFunc, [ arg, self.focus ], trigger=saveThreadsLog, loaded=True )

		return theID

##############################
# _regImpEXAMPLE = _.regImp( focus(), '_rightThumb._auditCodeBase' )

# _regImpEXAMPLE.do( 'functionTest' )
# _regImpEXAMPLE.do( _codeX.imp.functionTest )
# _regImpEXAMPLE.do( 'functionTestKwargs', ['Scott','Alpha'] )
# _regImpEXAMPLE.do( 'functionTestKwargs', { 'one': 'Scott', 'two': 'Alpha' } )

# _regImpEXAMPLE.switch( 'Long' )
# _regImpEXAMPLE.switch( 'GroupBy', 'appreg' )

# _regImpEXAMPLE.imp.focus( focus() )
# _.switches.dumpSwitches()
# _regImpEXAMPLE.imp.action()
##############################
##############################
# txtBackup = _.regImp( __.appReg, 'txtBackup' )
# txtBackup = _.regImp( focus(), 'txtBackup' )
# txtBackup.switch( 'Silent' )
# txtBackup.switch( 'Input', 'appreg' )

# txtBackup.do( txtBackup.imp.action )
# txtBackup.do( 'action' )
# txtBackup.action()
##############################


def saveThreadsLog():
	global threads
	# log = threads.log('execute')
	saveLog( 'threads', printThis=False )




def autoKwargsGetArgsFromApp(app):
	if not '.py' in app:
		app = app + '.py'
	appText = getText(_v.py + _v.slash + app)
	func = []
	for row in appText:
		if 'def ' in row:
			fr = row.split('def ')[1].replace(' ','')
			name = fr.split('(')[0]
			if name+'():' in fr:
				args = []
			else:
				tmp = fr.replace(name+'(','')
				arg = tmp.split('):')[0]
				args = []
				for x in arg.split(','):
					if '=' in x:
						args.append( { 'arg': x.split('=')[0], 'default': x.split('=')[1] } )
					else:
						args.append( { 'arg': x, 'default': '' } )


			func.append( { 'name': name, 'args': args } )
	return func



###############################################
####### imported into functions as needed
	# math
	# calendar
	# re
	# np
	# random

####### deleted
# glob
# subprocess
# join
# getsize
# splitext
# rrule
# ast
# OrderedDict
###############################################

### NOTES ###
	# types of timestamps:
	#                       1522705321.1137724      file create, modification
	#                       1517338060740           int(round(time.time() * 1000))
	


# _.regImps( focus(), 'app' )
# _.regImps[focus()]['app']

# class Threads
# class Queue
# def add(
# def printReport(
# def checkTimeout(
# def audit

# class regImp:


# 2B-C3P0-AF i: {id} 
# 2B-R2D2-AF
# r: {relatedid}

{ '2B100AF': 0, 'id': 0, 'genfrom': 0,  'created': 1558456773.7885933 }

############################################### ###############################################


leap_years_table = None
###############################################
 



############################################### ###############################################
# testlist = [1, 2, 3, 5, 3, 1, 2, 1, 6]
# test = [i for i,x in enumerate(testlist) if x == 1]



# _.fields.register( 'project', 'name', script=_.resolveEpochTest )
# _.fields.asset( 'project', {} )
# _.fields.asset( 'project', [{}] )
# _.fields.register( 'project', 'name', value, appReg=focus() )
# _.fields.register( 'project', 'name', value )
# _.fields.value( 'project', 'name', value )

# fields = Fields()

# TableProfile TableProfile_Config

# switchDefault = switches.length()

"""

To Do: * aggregate *
	p ls -g folder ext -aggregate sum{bytes} -c folder ext bytes
		self.group_structure[ folder ][ ext ] 
		sum( self.group_structure[ folder ][ ext ][ ' - aggregates (A359) - ' ][ bytes ] )

"""
"""
		fileBackup = _.regImp( focus(), 'fileBackup' )
		fileBackup.switch( 'Silent' )
		fileBackup.switch( 'Flag', 'cloud.del' )
		fileBackup.switch( 'isRunOnce' )
		fileBackup.switch( 'DoNotSchedule' )

		fileBackup.switch( 'Input', path )
		paths['backup'] = fileBackup.do( 'action' )



_cryptFile = _.regImp( __.appReg, 'cryptFile' )
_cryptFile.switch( 'NoExt' )
_cryptFile.imp.appDBA = _cryptFile.focus
focus()

_cryptFile.switch( 'Files', row )
_cryptFile.do( 'action' )

"""



# {0E7253CE-1D9A-423D-9418-E082BF8495E1}

# defaultScriptTriggers()

############################################### ###############################################
# alias

colorPrint=colorThis
cp=colorThis

pv=printVarSimple
vp=printVarSimple
pvs=printVarSimple

ppv=printVarColor
ppvv=printVarColor
pvv=printVarColor
pvpv=printVarColor

def err( msg , e=None, kill=True):
	
	cp( linePrint(txt='*',p=0), 'red' )
	
	cp( '  Error', 'red' )
	if type(msg) == str:
		cp( [ '  \t', msg ], 'yellow' )
	if type(msg) == list:
		nu={}
		# msgN = ['  \t']
		for x in msg:
			if x ==0:
				print_()
			elif type(x)==dict: # { 'l': line, 'c': 'green', 'd': 1, 'n': 'todo' }
				l=x['l']
				if 'c' in x:
					c=x['c']
				else:
					c='yellow'
				if 'd' in x:
					d=x['d']
				else:
					d=0

				if 'n' in x:
					nn=x['n']
					if not nn in nu:
						nu[nn]=0
					n=nu[nn]
				else:
					n=None

				if len(x) == 3:
					c
				w='  \t'
				i=0
				while not i == d:
					i+=1
					w+='\t'
				if n is None:
					cp( [ w, l ], c )
				else:
					nu[nn]+=1
					cp( [ w, str(nu[nn])+')', l ], c )

			else:
				cp( [ '  \t', x ], 'yellow' )

			# msgN.append(x)
		# cp( msgN, 'yellow' )
	if not e is None:
		cp( ['  \t\t',e], 'cyan' )
		
	# cp( '**********************************************************************', 'red', isError=True )
	# linePrint()
	cp( linePrint(txt='*',p=0), 'red' )
	if kill:
		sys.exit()
	# △ ▽
e=err

def key( subject ):
	try:
		table = getTableDB( 'secureStrings.hash' )
		return table[subject]
	except Exception as ee:
		err( 'secureString', ee )



def historyPrint( code, pre='' ):
	i=0
	while not i >= 4:
		i+=1
		code = _str.cleanBE(code, '\n')
		code = _str.cleanBE(code, ' ')
		code = _str.cleanBE(code, '\t')

	if switches.isActive('DoNotColorize'):
		return code
	result = ''
	
	colors = {
				'cmd': 'purple',
				'py': 'yellow',
				'pipe': 'red',
				'switches': 'green',
				'value': 'cyan',
				'quote': 'darkcyan',
	}

		
	lastP=False
	lastSwitch=False
	lastCMD=False
	lastPipe=False
	for i,x in enumerate(code.split(' ')):
		if x.lower() == 'p' or x.lower() == '%py%' or x.lower() == 'pp' or x.lower() == 'python' or x.lower() == 'python.exe' or x.lower().endswith('python.exe'):
			lastP = True
			result += colorThis( x, colors['cmd'], p=0 )
			lastSwitch = False
			lastPipe = False
		elif i == 0 or lastPipe:
			lastPipe = False
			lastCMD = True
			result += colorThis( x, colors['cmd'], p=0 )
		elif lastP:
			lastSwitch = False
			result += colorThis( x, colors['py'], p=0 )
		elif x.startswith('+'):
			lastSwitch = True
			result += colorThis( x, colors['switches'], p=0 )
		elif x.startswith('-') or( x.startswith('/') and not ' -' in code ):
			lastSwitch = True
			result += colorThis( x, colors['switches'], p=0 )


		elif x == '|' or x == '&':
			lastCMD = False
			lastSwitch = False
			lastPipe = True
			result += colorThis( x, colors['pipe'], p=0 )
		elif lastSwitch:
			if '"' in x:
				yx=''
				Yy=''
				for yY in x:
					if not yY == '"':
						Yy+=yY
					else:
						if Yy:
							yx+=colorThis( Yy, colors['value'], p=0 )
							Yy=''
						yx+=colorThis( '"', colors['quote'], p=0 )
				if Yy:
					yx+=colorThis( Yy, colors['value'], p=0 )
					Yy=''

				result += yx
			else:
				result += colorThis( x, colors['value'], p=0 )
		elif lastCMD:
			result += colorThis( x, colors['value'], p=0 )
		else:
			result += x
		result += ' '

		if not x == 'p':
			lastP = False
	return pre+result








class ONLINE:
	def __init__( self ):
		self.onStatus=0
		self.ip='0.0.0.0'
 
		
 

	def page( self, url ):
		# requests = vc.FIG.imp('requests')
		requests = __.imp('requests')
		if requests is None:
			return ''
		try:
			page = requests.get(url)
			page_code = str(page.text)
			self.onStatus=True
		except Exception as e:
			self.onStatus=False
			page_code=''
		page_code = page_code.replace( chr(10), '\n' )
		page_code = page_code.replace( chr(27), '' )
		page_code = page_code.replace( '\r', '' )
		return page_code


	def status( self ):
 
		# loader()
 
		# requests = vc.FIG.imp('requests')
		requests = __.imp('requests')
		if requests is None:
			self.onStatus = None
			return self.onStatus

		url = 'http://tools.rightthumb.com/ip.php'
		if type(self.onStatus) == bool:
			return self.onStatus
		page_code = self.page(url)
		if not self.onStatus:
			return self.onStatus
		page_code = page_code.replace( '\n', '' )
		page_code = page_code.replace( ' ', '' )
		if len(page_code) > 6 and len(page_code) < 16:
			self.ip = page_code
			self.onStatus = True
		else:
			self.onStatus = False
		# print_(self.ip)
		# print_(self.onStatus)
		return self.onStatus



	def download_updates( self ):
		# requests = vc.FIG.imp('requests')
		requests = __.imp('requests')
		# print_('here')
		# vc.FIG.bash_vars(p=0)
		if not os.path.isdir(_v.home +os.sep+ '.rt'):
			os.mkdir(_v.home +os.sep+ '.rt')

		

		if self.status():
			cp( ['status:', self.onStatus], 'green' )
		else:
			cp( ['status:', self.onStatus], 'red' )
		if self.status():

			files = []
			files.append({ 'label': 'tool', 'path': _v.home +os.sep+ '.rt' +os.sep+ 'tool', 'pre-exist': False })
			files.append({ 'label': 'tool.sh', 'path': _v.home +os.sep+ '.rt' +os.sep+ 'tool.sh', 'pre-exist': False })
			files.append({ 'label': 'help.txt', 'path': _v.home +os.sep+ '.rt' +os.sep+ 'help.txt', 'pre-exist': False })
			# rec = { 'label': 'bashrc.py', 'path': v.bash['tech_drive'] + '/tech/programs/python/src/unity/bashrc.py', 'pre-exist': True }
			# rec['path'] = rec['path'].replace( '/', os.sep )
			# files.append(rec)
			rec = { 'label': 'load-vars.sh', 'path': v.bash['tech_drive'] + '/tech/programs/bash/load-vars.sh', 'pre-exist': True }
			rec['path'] = rec['path'].replace( '/', os.sep )
			files.append(rec)


			for rec in files:
				p = rec['path']
				l = rec['label']

				shouldProcess = False
				if not rec['pre-exist']:
					shouldProcess = True
				else:
					if os.path.isfile(rec['path']):
						shouldProcess = True
				if shouldProcess:
					
					if os.path.isfile(p):
						os.unlink(p)
					if not os.path.isfile( p ):
						print_()
						cp( [ 'downloading:', l ], 'yellow' )
						url = 'http://reph.us/tools/'+l
						page = requests.get(url)
						page_code = str(page.text)
						page_code = page_code.replace( chr(10), '\n' )
						page_code = page_code.replace( chr(27), '' )
						page_code = page_code.replace( '\r', '' )
						# vc.HD.saveText( page_code, p )
						saveText( page_code, p )
						cp( [ 'saved:', p ], 'yellow' )
				else:
					print_(rec)

	download = download_updates
imps = {}
def impath(path):
	if path == '?tool':
		path = _v.home +os.sep+ '.rt' +os.sep+ 'tool'
	return path
def import_path(path):
	global imps
	path = impath(path)
	module_name = os.path.basename(path).replace('-', '_')
	spec = importlib.util.spec_from_loader( module_name, importlib.machinery.SourceFileLoader(module_name, path) )
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	sys.modules[module_name] = module
	if not path in imps:
		imps[path] = module
	return imps[path]

size_group_data = [{"l": "1", "s": "500", "x": "kb"}, {"l": "2", "s": "1", "x": "mb"}, {"l": "3", "s": "5", "x": "mb"}, {"l": "4", "s": "10", "x": "mb"}, {"l": "5", "s": "20", "x": "mb"}, {"l": "6", "s": "50", "x": "mb"}, {"l": "7", "s": "200", "x": "mb"}, {"l": "8", "s": "500", "x": "mb"}, {"l": "9", "s": "1", "x": "gb"}, {"l": "10", "s": "5", "x": "gb"}, {"l": "11", "s": "10", "x": "gb"}, {"l": "12", "s": "20", "x": "gb"}, {"l": "13", "s": "50", "x": "gb"}, {"l": "14", "s": "200", "x": "gb"}, {"l": "15", "s": "500", "x": "gb"}, {"l": "16", "s": "1", "x": "tb"}, {"l": "17", "s": "5", "x": "tb"}, {"l": "18", "s": "10", "x": "tb"}, {"l": "19", "s": "20", "x": "tb"}, {"l": "20", "s": "50", "x": "tb"}, {"l": "21", "s": "200", "x": "tb"}, {"l": "22", "s": "500", "x": "tb"}, {"l": "23", "s": "1", "x": "pb"}, {"l": "24", "s": "5", "x": "pb"}, {"l": "25", "s": "10", "x": "pb"}, {"l": "26", "s": "20", "x": "pb"}, {"l": "27", "s": "50", "x": "pb"}, {"l": "28", "s": "200", "x": "pb"}, {"l": "29", "s": "500", "x": "pb"}, {"l": "30", "s": "1", "x": "eb"}, {"l": "31", "s": "5", "x": "eb"}, {"l": "32", "s": "10", "x": "eb"}, {"l": "33", "s": "20", "x": "eb"}, {"l": "34", "s": "50", "x": "eb"}, {"l": "35", "s": "200", "x": "eb"}, {"l": "36", "s": "500", "x": "eb"}, {"l": "37", "s": "1", "x": "zb"}, {"l": "38", "s": "5", "x": "zb"}, {"l": "39", "s": "10", "x": "zb"}, {"l": "40", "s": "20", "x": "zb"}, {"l": "41", "s": "50", "x": "zb"}, {"l": "42", "s": "200", "x": "zb"}, {"l": "43", "s": "500", "x": "zb"}, {"l": "44", "s": "1", "x": "yb"}, {"l": "45", "s": "5", "x": "yb"}, {"l": "46", "s": "10", "x": "yb"}, {"l": "47", "s": "20", "x": "yb"}, {"l": "48", "s": "50", "x": "yb"}, {"l": "49", "s": "200", "x": "yb"}, {"l": "50", "s": "500", "x": "yb"}]
def size_group_print(m=True, l=0):
	global size_group_data
	records = []
	for rec in size_group_data:
		if m:
			if rec['x'] == 'pb':
				break
		records.append({ 'group': rec['l'], 'size': rec['s']+rec['x'] })
	tables.rprint( records , l=l)
def size_group(s):
	global size_group_data
	if type(s) == str:
		s = unFormatSize(s)

	if s == 0:
		return 0
	size_group_data.reverse()
	last = 0

	for rec in size_group_data:
		un = rec['s']+rec['x']
		fo = unFormatSize(un)
		if s >= fo:
			return int(rec['l'])
	return 1

def size_group_size(g,f=1):
	global size_group_data
	if type(g) == str:
		g = int(g)
	for rec in size_group_data:
		if g == int(rec['l']):
			un = rec['s']+rec['x']
			fo = unFormatSize(un)
			if f:
				return formatSize(fo).replace(' ','').replace('.0','')
			return fo



	pass

# try:
#     class ONLINE2:
#         def __init__( self ):
#             self.tool = import_path('?tool')
#             self.page = self.tool.vc.ONLINE = self.tool.ONLINE()
#             self.page = self.tool.vc.ONLINE.page
#             self.status = self.tool.vc.ONLINE.status
#             self.download_updates = self.tool.vc.ONLINE.download_updates
#             self.download = self.tool.vc.ONLINE.download_updates
#     o2 = ONLINE2()
#     ol = o2.status()
#     if ol:
#         cp( 'online', 'green' )
#     else:
#         cp( 'offline', 'red' )
# except Exception as e:
#     cp( 'ol2', 'red' )

# self.columnTab+tableLine

__.onExit(tables.eof)

hp = historyPrint
ph = historyPrint

# class regImp:
# 'WebTable'
# NoTableLines

##########################################################
# index AND line
'''
	i=0
	while True:
		eol=_.vindex(data,i,n='\n')
		if not type(eol) == int: eol=len(data)-1;
		if eol < 1: break;
		line = data[ i: eol+1 ].replace('\n','')
		pass
		pass
		i=eol+1
		if i == len(data): break;
'''
##########################################################
# colorizeRow

# def dict_generator(indict, pre=None):
#     pre = pre[:] if pre else []
#     if isinstance(indict, dict):
#         for key, value in indict.items():
#             if isinstance(value, dict):
#                 for d in dict_generator(value, pre + [key]):
#                     yield d
#             elif isinstance(value, list) or isinstance(value, tuple):
#                 for v in value:
#                     for d in dict_generator(v, pre + [key]):
#                         yield d
#             else:
#                 yield pre + [key, value]
#     else:
#         yield pre + [indict]


def appID_nID_password():
	try:
		from random import randrange
	except Exception as e:
		pass
	tn='8136901260'
	o=randrange(len(tn))
	if not o:
		o+=1
	if str(randrange(1000)/2).endswith('.0'):
		n=tn[o:]
	else:
		n=tn[:o]
	return n


def dict_generator_prefix( cnt, txt='    ' ):
	result=''
	n=0
	while not n == cnt:
		result+=txt
		n+=1
	return result



dict_generator_spent=[]
dict_generator_index={}
def dict_generator(indict, pre=None, fields=[] ):
	global dict_generator_spent
	global dict_generator_index
	pre = pre[:] if pre else []
	if isinstance(indict, dict):
		for key, value in indict.items():
			if isinstance(value, dict):
				for d in dict_generator(value, pre + [key],fields):
					yield d
			elif isinstance(value, list) or isinstance(value, tuple):
				for v in value:
					for d in dict_generator(v, pre + [key],fields):
						yield d
			else:
				# yield pre + [key, value]
				path = pre + [key]
				p = '.'.join(path)
				if not p in dict_generator_index:
					dict_generator_index[p]=1
				else:
					dict_generator_index[p]+=1
				# print_(p)
				found = False

				if key in fields:
					found = True
					pp=key
				elif p in fields:
					pp=p
					found = True
				if found:
					f = fields.index(pp)
					if f == 0:
						if not value in dict_generator_spent:
							dict_generator_spent.append(value)
							cp(value,'green')
							print_()
							print_()
					else:
						xXx = dict_generator_prefix(f) + value
						if f ==1:
							cp(xXx,'yellow')
						elif f == 2:
							cp(xXx,'cyan')
						elif f == 3:
							cp(xXx,'blue')
						elif f == 4:
							cp(xXx,'red')
						elif f == 5:
							cp(xXx,'darkcyan')
						elif f == 6:
							cp(xXx,'purple')
						elif f == 7:
							cp(xXx,'white')
						else:
							print_(xXx)




				yield path
	else:
		if isinstance(indict, list) or isinstance(indict, tuple):
			for v in indict:
				for d in dict_generator(v, pre + ['i'],fields):
					yield d

		# yield pre 

# index = {}
# for x in _.dict_generator(dic):
#   s = '.'.join(x)
#   if not s in index:
#       index[s] = 1
#   else:
#       index[s] += 1

def timeblock(epoch=None,hr=None,ish=None, ):
	if epoch is None and hr is None and ish is None:
		hr=5
	elif not ish is None:
		hr = int( isDate(ish)['time'].split(' ')[1].split(':')[0] )
	elif not epoch is None:
		hr = int( friendlyDate2( epoch ).split(' ')[1].split(':')[0] )
	elif not hr is None:
		hr = int(hr)
	t='err'
	if hr > 22:
		t='late'
	elif hr < 4:
		t='late'
	elif hr < 6:
		t='wee'
	elif hr < 8:
		t='early'
	elif hr < 12:
		t='morning'
	elif hr <= 17:
		t='afternoon'
	else:
		t='evening'
	# wee early morning afternoon evening late
	return t

def rli(LIST,default=''):
	random = __.imp('random')
	if len(LIST) == 0:
		return default
	if len(LIST) == 1:
		return LIST[0]
	# random_list_item
	return LIST[ random.randint(0,len(LIST)-1) ]

tb=timeblock

epoch_times_dic = {
						"y": 31536000,
						"m": 2678400,
						"w": 604800,
						"d": 86400,
						"h": 3600,
						"min": 60
}
et=epoch_times_dic
def epoch_times():
	global epoch_times_dic
	if not epoch_times_dic is None:
		return epoch_times_dic

	dic={}
	a=isDate('2022-03-28',f='epoch')
	b=isDate('2022-03-29',f='epoch')
	day=int(b-a)

	a=isDate('2022-02-25',f='epoch')
	b=isDate('2023-02-25',f='epoch')
	dic['y']=int(b-a)

	a=isDate('2022-01-01',f='epoch')
	b=isDate('2022-02-01',f='epoch')
	dic['m']=int(b-a)

	dic['w']=day*7
	dic['d']=day

	a=isDate('2022-01-01 21:00:00',f='epoch')
	b=isDate('2022-01-01 22:00:00',f='epoch')
	dic['h']=int(b-a)

	a=isDate('2022-01-01 21:15:00',f='epoch')
	b=isDate('2022-01-01 21:16:00',f='epoch')
	dic['min']=int(b-a)


	return dic

# timeCalc

def newid(subject):
	requests = __.imp('requests')
	url='https://eyeformeta.com/apps/ids/?subject=live-'+subject
	page = requests.get(url).content.decode("utf-8").replace('\\n','\n').replace('\n','').replace('\r','').replace(' ','').replace('\t','')
	return page
	
aib=aiBullet
ail=aiLine
bu=aiBullet
bull=aiBullet
lbu=aiLine

nw=n2w

## UUID ##


# print_( 1,2,3,4, c='yellow' ); sys.exit();
pr=print_
prt=printt
pt=printt
_fileBackup=None
def bk(path,flag=None):
	global _fileBackup
	if _fileBackup is None: _fileBackup = regImp( __.appReg, 'fileBackup' );
	_fileBackup.switch( 'Silent' )
	_fileBackup.switch( 'Input', path )
	if type(flag) == str: _fileBackup.switch( 'Flag', flag );
	return _fileBackup.do( 'action' )

def life(subject):
	return _v.life+subject.replace('/',os.sep)





def ico():
	random=__.imp('random')
	ads=fo(_v.life+'apps')
	ri = random.randrange(len(ads))
	cho=ads[ri]
	ic=list('🧻🧪💀🦆🦉🥓🦄🦀🖕🍣🍤🍥🍡🥃🥞🐕👾🐉🐓🐋🐌🐢👽👿🥑🐡🐗💐🏹🎨🐔🐛🎯🌯📷🛶🥕🍸🍳🐲🎣🐟🦅👀🐸🤞💪💾👻🐊🍔🌭🍀🕓🦊🍟🥝🐒🥞🐼📎🐧💩🍕🍍🦏🍗🌈🐳🦑🚀🙈🙊🙉🌮🐅🐯🍉🚽🍅👅🎩🍷')
	for x in ic:
		print(x)

nsfw=True

l=dot()
l.v=dot()
l.sw=dot()


def l_fieldSet( switchName, switchField, switchValue, theFocus=False ):
	global switches
	switches.fieldSet( switchName, switchField, switchValue, theFocus )
def l_registerSwitches_vars():
	autoBackupData = __.setting('receipt-log')
	__.releaseAcquiredData = __.setting('receipt-file') 
	__.myFileLocations_SKIP_VALIDATION = __.setting('myFileLocations-skip-validation')
	__.isRequired_Pipe = __.setting('require-pipe')
	__.isRequired_Pipe_or_File = __.setting('require-pipe||file')
	__.pre_error = __.setting('pre-error')
	__.switch_raw = __.setting('switch-raw')
	__.isRequired_or_List = __.setting('require-list')
def l_registerSwitches( trig=None, sw=None ):
	global appInfo
	global argvProcess
	global myFileLocation_Print
	global autoBackupData
	l_registerSwitches_vars()
	# appInfo=l.conf('info')



	if not l.conf('__name__') == '__main__':
		argvProcess = False
	else:
		argvProcess = True

	if not __.appReg == l.conf('appDBA') and l.conf('appDBA') in __.appReg:



		load()
		appInfo[__.appReg] = appInfo[l.conf('appDBA')]
		appData[__.appReg] = appData[l.conf('appDBA')]
	__.constructRegistration( appInfo[__.appReg]['file'],__.appReg )
	if not sw is None: sw();
	if not trig is None: trig();
	
	defaultScriptTriggers()
	switches.process()
	# pr('l_registerSwitches',c='gray')
	if l.conf('__name__') == '__main__':
		# pr('l_registerSwitches: __main__',c='gray')
		if not sys.stdin.isatty():
			# pr('setPipeData( sys.stdin.readlines',c='gray')
			setPipeData( sys.stdin.readlines(), __.appReg, clean=l.conf('clean-pipe' ,d=True) )
	postLoad( l.conf('__file__') )
	myFileLocation_Print=l.conf('myFileLocation_Print',d=False)
	appInfo[__.appReg]['file']=appInfo[__.appReg]['liveAppName']
l.v.cnf=dot()
l.v.cnf.placeholder='3586006adfdc'
l.v.cnf.default=None
l.v.cnf.data={}
def l_settings(subject,value=l.v.cnf.placeholder,default=l.v.cnf.default,v=None,d=None):
	if not d is None: default=d;
	if not v is None: value=v;

	if not value == l.v.cnf.placeholder:
		l.v.cnf.data[subject]=value

	if subject in l.v.cnf.data: return l.v.cnf.data[subject];
	else: return default;

l.fieldSet=l_fieldSet
l.sw.register=l_registerSwitches
l.cnf=l_settings
l.conf=l_settings
l.config=l_settings
l.fig=l_settings
l.setting=l_settings

def l_vars(fcs,n,f,d):
	__.registeredApps.append( fcs )
	l.conf('__name__',n)
	l.conf('__file__',f)
	l.conf('appDBA',d)
	return l.fieldSet
l.vars=l_vars
oc=vindex


def dots(path):
	def _dots_(pth):
		try: exec(pth); return True;
		except Exception as e: return False;
	rts=path.split('.'); exec('global '+rts[0]);
	if _dots_(path): return eval(rts[0])
	pre=[]; thp=[];
	for i,seg in enumerate(rts):
		pre=thp.copy(); thp.append(seg); npre='.'.join(pre); npath='.'.join(thp)
		if i == len(rts)-1:
			exec('from 1 import 2'.replace('1',npre).replace('2',rts[-1]))
			f='3=2'.replace('1',npre).replace('2',rts[-1]).replace('3',path)
		else: f='1=dot()'.replace('1',npath);

		if not _dots_(npath):
			exec(f)
			if i == len(rts)-1: return eval(rts[0]);
nsfw_=False
def ad(path=None,label='ad'):
	if not os.path.isdir(_v.ads+os.sep+'apps'): return None
	global MINI_ADS
	global ads
	ads = []
	
	def add_ad_fo(ad_fo):
		global ads
		for a2 in fo(_v.ads+os.sep+ad_fo): ads.append(a2);

	# print(_v.life+'apps')
	# sys.exit()
	global nsfw; global nsfw_;
	if not nsfw_:
		should_dl=False
		if not os.path.isfile(_v.rtp+'vars'+os.sep+'nsfw'): should_dl=True
		else:
			diff=time.time()-os.path.getmtime(_v.rtp+'vars'+os.sep+'nsfw')
			if diff > 14415: should_dl=True
		if not should_dl:
			if '1' in getText(_v.rtp+'vars'+os.sep+'nsfw',raw=True): nsfw=True
			else: nsfw=False
		if should_dl:
			try:
				if '1' in URL('https://eyeformeta.com/apps/terminal/status/nsfw'): nsfw=True;
				else: nsfw=False;
			except Exception as ee: nsfw=False;
			if nsfw: saveText('1',_v.rtp+'vars'+os.sep+'nsfw')
			else:    saveText('0',_v.rtp+'vars'+os.sep+'nsfw')

	
	if path:
		cho=__.path(path)
		sub=__.path(cho,file=True)
		sub=sub.replace('.txt','').replace('-',' ').replace('_',' ')
	elif not path:
		nsfw_=True
		random=__.imp('random')
		add_ad_fo('apps')
		add_ad_fo('quotes')
		

		if nsfw:
			add_ad_fo('nsfw')
			
		
		ri = random.randrange(len(ads))
		cho=ads[ri]
		sub=__.path(cho,file=True)
	ad=getText( cho , raw=True )
	ad=ad.replace('\r','')

	if MINI_ADS and '#title)' in ad:
		#title)
		ad2=[];_adGO=False;
		for line in ad.split('\n'):
			if '#title)' in line: _adGO=True
			if _adGO: ad2.append(line)
		ad='\n'.join(ad2)

	def _cl(ad):
		ad=_str.do('be',ad,'\n')
		ad=_str.do('be',ad,' ')
		ad=_str.do('be',ad,'\t')
		return ad
	# ad=_cl(ad); ad=_cl(ad); ad=_cl(ad); ad=_cl(ad);
	# ad=_cl(ad); ad=_cl(ad); ad=_cl(ad); ad=_cl(ad);
	# cp( '<ad>', 'yellow' )
	_width=__.terminal.width - 15 - ( len(label)/2 ) - 1
	linePrint(c='green',center=label, length=_width)
	cp( sub, 'yellow' )
	linePrint('20',c='yellow')
	_the_color_=random_color()

	mx=0
	for liner in ad.split('\n'):
		leg=len(liner)
		if leg > mx:
			mx=leg
	def _ad_space_(line,mx):
		i=0
		while not len(line)==mx:
			line+=' '
		return '|  '+line+'  |'

	for liner in ad.split('\n'):
		pr( pr('#'+label+')  ',c='gray',p=0) +pr(  _ad_space_(liner,mx)  ,c=_the_color_,p=0))
	linePrint(c='green',center=label, length=_width)
	# cp( '</ad>', 'yellow' )
	return ad
# ads=ad

def URL(url):
	requests=dots('requests.get')
	return requests.get(url).content.decode("utf-8").replace('\\n','\n')


def getConfig(path):
	def _cl_(string): return _str.do('be',   _str.do('be',string,'\n')   ,' ');
	def _val_(string):
		if string.startswith('"'): string=string[1:]; string=string[:-1]; return _cl_(string);
		if string.startswith("'"): string=string[1:]; string=string[:-1]; return _cl_(string);
		if string.startswith('[') or string.startswith('{'):
			simplejson = __.imp('simplejson')
			return simplejson.loads(string)
		if string.lower() == 'none': return None;
		if string.lower() == 'null': return None;
		if string.lower() == 'true': return True;
		elif string.lower() == 'false': return False;
		else:
			has=[]
			if '-' in string and not string.startswith('-'): return _cl_(string);
			for s in string:
				if s in '01234567890-' and not 'n' in has: has.append('n');
				if s in '.' and not 'f' in has: has.append('f');
				if s in '\n\tabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}()[]<>' and not 'a' in has: return _cl_(string);
			if 'f' in has and len(has)<3 and len(has)>1: return float(string);
			if 'n' in has and len(has)==1: return int(string);
		return _cl_(string)
	# print(path)
	data=getText(path)
	dic={}
	for item in data:
		item=_str.do('be',item,' ')
		item=_str.do('be',item,'\n')
		item=_str.do('be',item,'\t')
		if item and not item.startswith('#'):
			if '=' in item:
				a=item[0:item.index('=')]
				b=item[item.index('=')+1:len(item)]
				dic[a]=_val_(b)
	return dic

def saveConfig(data,path):
	def _cl_(string): return _str.do('be',   _str.do('be',string,'\n')   ,' ');
	def _val_(string):
		if type(string) == str and not '\n' in string: return _cl_(string);
		elif type(string) == str and '\n' in string: return _cl_(str({'d':string})[7:-2]);
		elif type(string) == int or type(string) == float: return _cl_(str(string));
		elif type(string) == dict or type(string) == list:
			simplejson = __.imp('simplejson')
			return simplejson.dumps(string, sort_keys=False, default=str)

		return _cl_(str(string))

	config=[]
	for k in data:
		config.append(  _cl_(k)+'='+_val_(data[k])  )
	saveText(config,path)
	return config

imp=__.imp
def HID(sub): requests=__.imp('requests'); return int(requests.get('https://eyeformeta.com/assets/widgets/ids/index.php?subject='+sub).content.decode("utf-8").replace('\\n','\n').replace('\n',''));

def cmd(run):
	subprocess=__.imp('subprocess.check_output')
	res = subprocess.check_output(run.split(' '))
	return str(res,'iso-8859-1')

# releaseAcquiredData
dd=date_diff_dic

# def file(path):
#     if not os.path.isfile(path): return 'error, no file'
#     peek=open( path , 'r' ).read(32)
#     peek=_str.do('trim',peek)
#     if peek.startswith('[') or peek.startswith('{'):
#         try: return getTable2(path)
#         except Exception as ee: pass
#     try:
#         return getText(path,raw=True)
#     except Exception as ee:
#         try:
#             return getBin(path)
#         except Exception as ee: e(ee)


# def save(data,path):
#     if type(data) == str: return saveText(data,path)
#     if type(data) == dict: return saveTable2(data,path)
#     if type(data) == list   and len(data) and type(data[0]) == dict: return saveTable2(data,path)
#     if type(data) == list   and len(data) and type(data[0]) == str: return saveText(data,path)

#     try: return saveTable2(data,path)
#     except Exception as ee: pass

#     try: return saveText(data,path)
#     except Exception as ee: pass

#     try: return saveBin(data,path)
#     except Exception as ee: e('_.save')


def waiting(sec,p=True,txt=''):
	if type(txt) == list:
		for i,x in enumerate(txt):
			txt[i]=str(x)
		txt=' | '.join(txt)
	if txt: txt='| '+txt
	if not type(sec) == int: e('waiting expected int')
	
	if not p: time.sleep(sec)
	else:
		
		while not sec==0:
			pr( 'waiting:', sec, txt, end=1 )
			time.sleep(1)
			sec-=1
		pr( '', end=1 )
def day(epoch=None,sep=None,end=None, e=None):
	if end == None and e == None: e=True
	if not end == None: e=end
	if sep is None: sep=os.sep
	if  epoch is None: epoch = time.time()

	year  = isDate(epoch,f='year')
	woy   = isDate(epoch,f='woy').split('.')[1]
	date  = isDate(epoch,f='date')[len('2022-'):]
	today = str(year)+sep+woy+sep+date
	if e: today += sep
	return today

def file_len(filename):
	with open(filename) as f:
		for i, _ in enumerate(f): pass
	return i + 1

def hush():
	global isWin
	if isWin: return ' > nul 2>&1'
	else: return ' > /dev/null 2>&1'

def file_break(path,lines = 4000):
	length = file_len(path)
	lines_per_file = lines
	smallfile = None
	with open(path) as bigfile:
		for lineno, line in enumerate(bigfile):
			if lineno % lines_per_file == 0:
				if smallfile:
					smallfile.close()
				small_filename = path+'__{}_{}'.format(lines,zeros3(lineno + lines_per_file,length))
				smallfile = open(small_filename, "w")
			smallfile.write(line)
		if smallfile:
			smallfile.close()

# https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python


def _2files(sub1,sub2,path=False,p=None,diff=False,d=None):
	if not d is None: diff=d
	if not p is None: path=p
	if path:
		if os.path.isfile(sub1): sub1=getText(sub1,raw=True)
		if os.path.isfile(sub2): sub2=getText(sub2,raw=True)
	if sub1 == sub2 and diff: return ''
	if sub1 == sub2 and not diff: return 100

	return None

def _2lines(line1,line2):

	return None



def _2lists(list1,list2): return list(set(list1).intersection(list2))


def _2dates(d1,d2=None, dic=False):
	if d2 is None: d2=time.time()
	# from datetime import datetime
	from dateutil import relativedelta
	try: d1 = float(d1)
	except Exception as e: pass
	try: d2 = float(d2)
	except Exception as e: pass

	d1=autoDate(d1)
	d2=autoDate(d2)
	if d1 > d2: t2=d1; t1=d2;
	else: t1=d1; t2=d2;
	d1=t1
	d2=t2
	start_date = datetime.datetime.fromtimestamp(int(d1))
	end_date = datetime.datetime.fromtimestamp(int(d2))
	delta = relativedelta.relativedelta(end_date, start_date)
	# for ddd in dir(delta): print(ddd)
	rt = {
				'y': delta.years,
				'mo': delta.months,
				'd': delta.days,
				'h': delta.hours,
				'mi': delta.minutes,
				's': delta.seconds,
	}

	# tt=[]
	# if delta.years: tt.append(str(delta.years)+' y')
	# if delta.months: tt.append(str(delta.months)+' m')
	# if delta.days: tt.append(str(delta.days)+' d')
	# rt['ta1'] = ' '.join(tt)
	# if delta.hours: tt.append(str(delta.hours)+' h')
	# if delta.minutes: tt.append(str(delta.minutes)+' min')
	# rt['ta2'] = ' '.join(tt)
	# if delta.seconds: tt.append(str(delta.seconds)+' sec')
	# rt['ta3'] = ' '.join(tt)

	tt=[]
	if delta.years:
		if delta.years == 1: tt.append(str(delta.years)+' year')
		else: tt.append(str(delta.years)+' years')

	if delta.months:
		if delta.months == 1: tt.append(str(delta.months)+' month')
		else: tt.append(str(delta.months)+' months')

	if delta.days:
		if delta.days == 1: tt.append(str(delta.days)+' day')
		else: tt.append(str(delta.days)+' days')

	# rt['tb1'] = ' '.join(tt)

	if not len(tt) or ( len(tt) == 1 and delta.days == 1 ):

		if delta.hours:
			if delta.hours == 1: tt.append(str(delta.hours)+' hour')
			else: tt.append(str(delta.hours)+' hours')

		if delta.minutes:
			if delta.minutes == 1: tt.append(str(delta.minutes)+' minute')
			else: tt.append(str(delta.minutes)+' minutes')

		if delta.days == 0 and delta.hours == 0:
			if delta.seconds:
				if delta.seconds == 1: tt.append(str(delta.seconds)+' second')
				else: tt.append(str(delta.seconds)+' seconds')

	rt['txt'] = ' '.join(tt)
	if not dic: return rt['txt']
	return rt

def dicKeys(dic,keys=None,omit=None,keep=None):
	if not keep is None and type(keep) == str: keys=keep; keep=1;
	if not omit is None and type(omit) == str: keys=omit; omit=1;
	if not type(keys) == str:
		keys=keys.replace(' ',',')
		keys=keys.split(',')
	if not type(dic) == dict: return dic
	if omit is None and keep is None: omit = True
	new={}
	if omit:
		for k in dic:
			if not k in keys: new[k] = dic[k]
	elif keep:
		for k in dic:
			if k in keys: new[k] = dic[k]
	return new



class Banner:
	""" https://onlineasciitools.com/convert-text-to-ascii-art """
	def __init__( self, banner ):
		self.banner=banner
		self.code=[]



	def gossip( self ):
		pr(line=1,c='yellow')
		pr()
		for go in self.code: pr(go)
		pr()
		pr(line=1,c='yellow')

	def goss( self, code ):
		code=hp(code); self.code.append(code);
		return code

	def pr( self ):
		if self.banner:
			clear()
			# print(__.terminal.width)

			mx=0
			for line in self.banner.split('\n'):
				ln=len(line)
				if ln > mx: mx=ln

			sides = (__.terminal.width/2) - (mx/2)-1
			sides = abs(int(sides))
			# sides = sides/2
			# sides = abs(int(sides))
			# sides = sides/2
			# sides = abs(int(sides))
			sp=_str.sp(sides)
			
			# print('sides',sides)
			brand = _str.es(self.banner,m=sp,be='|')
			pr(line=1,c='green'); pr(line=1,c='green');
			pr(brand,c=random_color())
			pr(line=1,c='green'); pr(line=1,c='green');


def isExit(_file_):
	# print(__.appReg)
	# print('_file_:',_file_)
	__.isExit()
	global appInfo

	def clean_tested(_source,_val='None'):
		if "'tested':"+_val+"," in _source: _source="'tested': "+_val+","
		if "'tested':  "+_val+"," in _source: _source="'tested': "+_val+","
		if "'tested':   "+_val+"," in _source: _source="'tested': "+_val+","
		if "'tested':    "+_val+"," in _source: _source="'tested': "+_val+","
		if "'tested':     "+_val+"," in _source: _source="'tested': "+_val+","
		_val='None'
		if "'tested': "+'0'+"," in _source:
			_source="'tested': "+_val+","
		return _source

	def just_print(i):
		for k in appInfo:
			rec=appInfo[k]
			if 'tested' in rec and not rec['tested']: e('app not tested','_.isExit: '+str(i))

	#n)--> ask will not work if executed after pipe, checking...
		#n)--> yes, i am sure, it is NOT: if not
	if sys.stdin.isatty():
		os=__.imp('os.stat'); sl=os.sep;
		os=__.imp('os.path.getctime'); sl=os.sep;
		_fo=_v.py+sl
		for k in appInfo:
			rec=appInfo[k]
			if not rec: continue
			if 'liveAppName' in rec:
				_fi=rec['liveAppName']+'.py'
				# path=_file_
				path=_fo+_fi
				try:
					ce=str(os.path.getctime(path))
				except Exception as ee: return None
				# print(rec)
				# pr(rec,pvs=1)
				# sys.exit()
				# pr(path,c='cyan')
				if 'tested' in rec and not rec['tested'] and os.path.isfile(path):
					pr( line=1, c='green' )
					pr( 'document tested date of '+_fi+'? ', c='green' )
					# ask=input(' Y / n: ')
					ask=input(' y / N: ')
					if not ask: ask='n'
					if 'y' in ask.lower():
						pr('updating documentation...',c='yellow')
						_source = getText(path,raw=True)
						# _source=clean_tested(_source,'0')
						# _source=clean_tested(_source)
						if "'tested': None," in _source:
							pr('found',c='green')
							# _source = _source.replace( "'created': '0000-00-00',", "'created': '0000-00-00',".replace('0000-00-00',_.isDate(os.path.getctime(path),f='date')) )
							_source = _source.replace( "'tested': None,","'tested': None,".replace('None',ce) )
							if ce in _source:
								saveText(_source,path)
								pr('added testing date to app documentation',c='green')
					

				else: just_print(1)

	elif not sys.stdin.isatty(): just_print(2)


def pipe_surfing():
	global appData
	for app in appData:
		if 'pipe'  in appData[app] and appData[app]['pipe']:
			return appData[app]['pipe']
	return False

	
def fak(*args, **kwargs):
	''' 
		code generator
			eval function args kwargs

				value = eval('function'+_.fak(args,kwargs))
		
					(  args[0], args[1], args[2]  ,  fi=kwargs['fi'],foo=kwargs['foo']  )

	'''
	function=''
	if kwargs:
		kwargs=dict(kwargs).copy()
	iargs=[]
	command=function+'('
	if args:
		for i in range(len(args)):
			iargs.append(str(i))
		_args='args['+'], args['.join(iargs)+']'
		command+='  '+_args
	if args and kwargs:
		command+='  ,  '
	if kwargs:
		kw=[]
		for kwa in kwargs:
			_k=kwa+'='"kwargs['"+kwa+"']"
			kw.append(_k)
		command+=','.join(kw)
	if args or kwargs:
		command+='  '
	command+=')'
	return command

def osvardump():
	varTXT=''
	subprocess=__.imp('subprocess')
	if isWin: varTXT= subprocess.getoutput('set')
	else: varTXT= subprocess.getoutput('printenv')
	return varTXT

def osvar(var=None,val=None):
	if var is None: return osvardump()
	if val is None:
		try: return os.environ[var]
		except: return ''
	try:
		os.environ[var]=val
		return True
	except: return False
		

	# printenv
	# os.environ['USERPROFILE']

def pyApp(path):
	os=__.imp('os.sep')
	path=__.path(path)
	paths=path.split(os.sep)
	file = paths[-1]
	# return file
	# return paths[-3]
	# return os.sep
	# return 'test'

	if len(paths)>1 and paths[-2] == '_rightThumb':
		if file == '__init__.py':
			return '_rightThumb'
		else:
			return '_rightThumb.'+file[:-3]
	elif len(paths)>2 and paths[-3] == '_rightThumb':
		if file == '__init__.py':
			return '_rightThumb.'+paths[-2]
		else:
			return '_rightThumb.'+paths[-2]+'.'+file[:-3]


	else:
		if file == '__init__.py' and len(paths)>1:
			return paths[-2]
		else:
			return file[:-3]

def fromYML(text): return __.imp('yaml').safe_load(text.replace('\t','    '))
def toYML(dic): return __.imp('yaml').dump( dic, sort_keys=False )

def getYML(path,here=False,h=None,auto=True,a=None):
	if not a is None: auto=a
	if not h is None: here=h
	if here: auto = False
	if not auto: here=True
	loaded=False
	yaml = __.imp('yaml')
	os = __.imp('os.path.isfile')
	if os.path.isfile(path):
		data = getText( path, raw=True )
		loaded=True
	elif not here and  os.path.isfile(_v.myTables + _v.slash + path):
		data = getText( _v.myTables + _v.slash + path, raw=True )
		loaded=True
	else: return {}
	data = data.replace('\r','')
	lines=[]
	for line in data.split('\n'):
		if line.strip(): lines.append(  line.rstrip()  )
	data='\n'.join(lines)
	data = data.replace('\t','    ')
	if loaded: data = data.replace('\t','    ')
	if not loaded: return {}
	return yaml.safe_load(data)


def saveYML(data,path,here=False,h=None):
	if not h is None: here = h
	yaml = __.imp('yaml')
	os = __.imp('os.sep')
	y=yaml.dump( data, sort_keys=False )
	if not here and not os.sep in path:
		path = _v.myTables + _v.slash + path
	saveText(y,path)

def saveYML2(data,path): return saveYML(data,path,here=True)
def getYML2(path): return getYML(path,here=True)

# class auditor:
# 	def __init__(self, label='default'):
# 		time=__.imp('time.time')
# 		self.label = label
# 		self.epoch=time.time()
# 	def stamp( location='default', line=None,    l=None ):
# 		if not l is None: line=l



getYAML2=getYML2
getYAML=getYML
saveYAML=saveYML
saveYAML2=saveYML2
imp=regImp
# class regImp:
# positiveResultsCode
# __.sw.PlusCode
# def caseUnspecific
# caseISspecific

def inject( snippet='', data='', header='', b='9a26c2d7f6b0', e='71564a5f3d65', be='## {xXx} ##' ):
	def _clean_(d): return d.replace('\r','')
	snippet=_clean_(snippet);data=_clean_(data);header=_clean_(header);
	bb = be.replace( 'xXx', b ); ee = be.replace( 'xXx', e );
	if not bb in data: data += '\n'+bb+'\n'+ee+'\n'
	active=False; result = [];
	for line in data.split('\n'):
		if bb in line: active=True
		if not active: result.append(line)
		if ee in line:
			result.append(bb)
			for snip in header.split('\n'):  result.append(snip)
			for snip in snippet.split('\n'): result.append(snip)
			result.append('')
			result.append(ee)
			active=False
	if False:
		lines=[]
		for line in result:
			if line.strip(): lines.append(line.rstrip())
		result=lines
	return '\n'.join(result)
# stuff = _.inject('77',stuff); print(stuff);


# def sort(self,fields=''):# sortThis 
# switches.trigger(
# formatColumnsSort


def percentageReduce(n,p): return n*(1-(p/100))
def percentageAdd(n,p): return n*(1+(p/100))

# _.percentageMinus(75000,25)
# _.percentageAdd(56250,25)

def isData2():
	os=__.imp('os.path.isfile')
	d=isData(r=0)
	# print(d)
	if not d: e('no data','_.isData2()')
	if os.path.isfile(d[0]):
		data=getText(d[0],raw=True)
	else:
		data = '\n'.join( d )
	return data
	# isDataR=isData2
	# isDatar=isData2
	# isDatr=isData2

def _thread_(*args, **kwargs):
	# threads=[]
	# import threading
	# t = threading.Thread(target=_thread_, args=(1,2,3), kwargs={'name':'scott','script':test})
	# threads.append(t)
	# t.start()
	for _script in ['_fn_','script']:
		if kwargs and _script in kwargs:
			script=kwargs[_script]
			kw={}
			for k in kwargs:
				if not k == _script:
					kw[k]=kwargs[k]
			ags=[]
			for i,ar in enumerate(args): ags.append('args['+str(i)+']')
			a=','.join(ags)
			kwg=[]
			for k in kw: kwg.append(k+'=kwargs["'+k+'"]')
			k=','.join(kwg)
			ak=[]
			if a: ak.append(a)
			if k: ak.append(k)
			if ak: exec('script('+ ','.join(ak) +')')
			else:exec('script()')
			break


# def pattern_probability(string1,string2,w=False):
# 		off='b9e086cad1834395a9aae81d869fd17b'
# 		off='b9e086cad1834395'
# 		off='b9e086ca'
# 		# string1=off+string1
# 		# string2=off+string2
# 		def _chr_(n):
# 				r=''; i=0;
# 				while not i==n: i+=1; r+='*';
# 				return r
# 		def pattern_length_offset(off,xstring1,xstring2):
# 				def pldiff(str1,str2):
# 						l1=len(str1)
# 						l2=len(str2)
# 						ll1=l1
# 						ll2=l2
# 						if l2 < l1:
# 								ll1=l2
# 								ll2=l1
# 						plen=round(percentageDiff(ll1,ll2),3)
# 						diff=ll2-ll1
# 						return diff,plen
# 				d,p=pldiff(xstring1,xstring2)
# 				# print(d,p)
# 				d,p=pldiff(off,off+_chr_(d))
# 				# print(d,p)
# 				return p


# 		def function_name(_string1_,_string2_):
# 				y={}
# 				y['s1']=patternz(_string1_)
# 				y['s2']=patternz(_string2_)

# 				common = list(set(y['s1']) & set(y['s2']))

# 				plen=percentageDiffInt(len(_string1_),len(_string2_))


# 				p1=percentageDiff(len(common),len(y['s1']))
# 				p2=percentageDiff(len(common),len(y['s2']))
# 				p0=p1
# 				if p2 < p1: p0=p2

# 				y['1s']=_string1_
# 				y['2s']=_string2_
# 				y['ptn1']=str(y['s1'])
# 				y['ptn2']=str(y['s2'])
# 				y['ptn_len1']=len(y['s1'])
# 				y['ptn_len2']=len(y['s2'])
# 				y['tcommon']=len(common)
# 				y['common']=str(common)


# 				len1=len(_string1_)
# 				len2=len(_string2_)
# 				len0=len1
# 				if len2 < len1: len0=len2
# 				y['len1']=len1
# 				y['len2']=len2
# 				y['len0']=len0

# 				y['%len']=plen
# 				# y['weight']=
# 				# y['offsetted']=
# 				y['%1']=round(p1,3)
# 				y['%2']=round(p2,3)
# 				y['%0']=round(p0,3)
# 				return y

# 		def sequential(s1,s2):
# 			# print('s1,s2',s1,s2)
# 			seq={}
# 			_range=6
# 			mx=-10
# 			for i,p in enumerate( s2 ):
# 				found=False
# 				for j in range(-2,_range):
# 					if i+j >mx:
# 						try:
# 							if not found and s2[i]==s1[i+j]:
# 								mx=i+j
# 							# print(s2[i],s1[i+j])
# 							# if s2[i]==s1[i+j]:
# 								# print(99)
# 								if not j in seq:
# 									if j==0: default=False
# 									else: default=False
# 									seq[j]={'cnt':0,'last': default}
# 								if seq[j]['last']:
# 									seq[j]['cnt']+=1

# 									try:
# 										if not s2[i+1]==s1[i+j+1]:
# 											# print(i,j,s2[i],'1-here')
# 											seq[j]['cnt']+=1
# 									except:
# 										# print(i,j,s2[i+1],'2-here',8)
# 										# print(i,j,'2-here',8)
# 										seq[j]['cnt']+=1
# 								seq[j]['last']=True
# 								# print(j)

# 							# else:
# 							# 	if j in seq: seq[j]['last']=False
# 						except:
# 							pass
# 							# if j in seq: seq[j]['last']=False
# 			seq['max']=0
# 			for j in range(-2,_range):
# 			# 	if j in seq and seq[j]['last']: seq[j]['cnt']+=1
# 				if j in seq:
# 					seq['max']+=seq[j]['cnt']

# 			if s1[0] == s2[0] and not s1[1] == s2[1]: seq['max']+=1
# 			# pv(seq)
# 			# pr(s1,s2,c='Background.red')
# 			# pr(seq['max'],c='red')
# 			# sys.exit()
# 			fx=[len(s1),len(s2)]
# 			fx.sort()
# 			# if fx[0]<seq['max']: seq['max']=fx[0]
# 			return seq['max']



# 		d = function_name(string1,string2)

# 		_min=8
# 		d['%lenoff']=pattern_length_offset( _chr_(_min) ,string1,string2)
# 		if d['%lenoff'] > d['%len']:
# 				d['offset'] = round(d['%lenoff']-d['%len'],3)
# 		else:
# 				d['offset']=0

# 		d['%off']=d['%0']+d['offset']


# 		# ↓ THERE ARE 2 WAYS OF DOING THIS ↓ 

# 		# ↓ by charecter ↓
# 		# _seq1=sequential(string1,string2)
# 		# _seq2=sequential(string2,string1)

# 		# ↓ by pattern ↓
# 		_seq1=sequential(d['s1'],d['s2'])
# 		_seq2=sequential(d['s2'],d['s1'])
		
# 		# ↑ THERE ARE 2 WAYS OF DOING THIS ↑

# 		_seqL=[_seq1,_seq2]
# 		_seqL.sort()
# 		# print('_seqL:',_seqL)
# 		d['seq']=_seqL[-1]
# 		if d['seq'] > d['len0']: d['seq'] = _seqL[0]
# 		d['seq_weight']=round(percentageDiff(d['seq'],d['len0']),3)
# 		# pr(d['seq'],d['len0'],c='purple')
# 		seq=d['seq']

# 		# pv(d)

# 		weighted = {}
# 		# weighted['vVv']=d['vVv']
# 		weighted['1s']=d['1s']
# 		weighted['2s']=d['2s']
# 		weighted['%0']=d['%0']
# 		weighted['offset']=d['offset']
# 		weighted['%off']=d['%off']
# 		weighted['len0']=d['len0']
# 		weighted['seq']=d['seq']
# 		weighted['seq_weight']=d['seq_weight']
# 		weighted['seq_offset']=round(percentageDiff(d['seq']+3,d['len0']+3)-d['seq_weight'],3)
# 		weighted['seq_weight_offsetted']=round(weighted['seq_weight']+weighted['seq_offset'],2)
# 		# return weighted



# 		if weighted['seq_weight_offsetted'] > 99 and not string1 == string2: weighted['seq_weight_offsetted']=99
# 		if weighted['seq_weight'] > 99 and not string1 == string2: weighted['seq_weight']=99

# 		if w: return weighted['seq_weight_offsetted']
# 		return weighted['seq_weight']




def pattern_probability(string1,string2,w=False):
		off='b9e086cad1834395a9aae81d869fd17b'
		off='b9e086cad1834395'
		off='b9e086ca'
		# string1=off+string1
		# string2=off+string2
		def _chr_(n):
				r=''; i=0;
				while not i==n: i+=1; r+='*';
				return r
		def pattern_length_offset(off,xstring1,xstring2):
				def pldiff(str1,str2):
						l1=len(str1)
						l2=len(str2)
						ll1=l1
						ll2=l2
						if l2 < l1:
								ll1=l2
								ll2=l1
						plen=round(percentageDiff(ll1,ll2),3)
						diff=ll2-ll1
						return diff,plen
				d,p=pldiff(xstring1,xstring2)
				# print(d,p)
				d,p=pldiff(off,off+_chr_(d))
				# print(d,p)
				return p


		def function_name(_string1_,_string2_):
				y={}
				y['s1']=patternz(_string1_)
				y['s2']=patternz(_string2_)

				common = list(set(y['s1']) & set(y['s2']))

				plen=percentageDiffInt(len(_string1_),len(_string2_))


				p1=percentageDiff(len(common),len(y['s1']))
				p2=percentageDiff(len(common),len(y['s2']))
				p0=p1
				if p2 < p1: p0=p2

				y['1s']=_string1_
				y['2s']=_string2_
				y['ptn1']=str(y['s1'])
				y['ptn2']=str(y['s2'])
				y['ptn_len1']=len(y['s1'])
				y['ptn_len2']=len(y['s2'])
				y['tcommon']=len(common)
				y['common']=str(common)


				len1=len(_string1_)
				len2=len(_string2_)
				len0=len1
				if len2 < len1: len0=len2
				y['len1']=len1
				y['len2']=len2
				y['len0']=len0

				y['%len']=plen
				# y['weight']=
				# y['offsetted']=
				y['%1']=round(p1,3)
				y['%2']=round(p2,3)
				y['%0']=round(p0,3)
				return y

		def sequential(s1,s2):
			# print('s1,s2',s1,s2)
			seq={}
			_range=6
			mx=-10
			for i,p in enumerate( s2 ):
				found=False
				for j in range(-2,_range):
					if i+j >mx:
						try:
							if not found and s2[i]==s1[i+j]:
								mx=i+j
							# print(s2[i],s1[i+j])
							# if s2[i]==s1[i+j]:
								# print(99)
								if not j in seq:
									if j==0: default=False
									else: default=False
									seq[j]={'cnt':0,'last': default}
								if seq[j]['last']:
									seq[j]['cnt']+=1

									try:
										if not s2[i+1]==s1[i+j+1]:
											# print(i,j,s2[i],'1-here')
											seq[j]['cnt']+=1
									except:
										# print(i,j,s2[i+1],'2-here',8)
										# print(i,j,'2-here',8)
										seq[j]['cnt']+=1
								seq[j]['last']=True
								# print(j)

							# else:
							# 	if j in seq: seq[j]['last']=False
						except:
							pass
							# if j in seq: seq[j]['last']=False
			seq['max']=0
			for j in range(-2,_range):
			# 	if j in seq and seq[j]['last']: seq[j]['cnt']+=1
				if j in seq:
					seq['max']+=seq[j]['cnt']

			if s1[0] == s2[0] and not s1[1] == s2[1]: seq['max']+=1
			# pv(seq)
			# pr(s1,s2,c='Background.red')
			# pr(seq['max'],c='red')
			# sys.exit()
			fx=[len(s1),len(s2)]
			fx.sort()
			# if fx[0]<seq['max']: seq['max']=fx[0]
			return seq['max']



		d = function_name(string1,string2)

		_min=8
		d['%lenoff']=pattern_length_offset( _chr_(_min) ,string1,string2)
		if d['%lenoff'] > d['%len']:
				d['offset'] = round(d['%lenoff']-d['%len'],3)
		else:
				d['offset']=0

		d['%off']=d['%0']+d['offset']


		# ↓ THERE ARE 2 WAYS OF DOING THIS ↓ 

		# ↓ by charecter ↓
		# _seq1=sequential(string1,string2)
		# _seq2=sequential(string2,string1)

		# ↓ by pattern ↓
		_seq1=sequential(d['s1'],d['s2'])
		_seq2=sequential(d['s2'],d['s1'])
		
		# ↑ THERE ARE 2 WAYS OF DOING THIS ↑

		_seqL=[_seq1,_seq2]
		_seqL.sort()
		# print('_seqL:',_seqL)
		d['seq']=_seqL[-1]
		if d['seq'] > d['len0']: d['seq'] = _seqL[0]
		d['seq_weight']=round(percentageDiff(d['seq'],d['len0']),3)
		# pr(d['seq'],d['len0'],c='purple')
		seq=d['seq']

		# pv(d)

		weighted = {}
		# weighted['vVv']=d['vVv']
		weighted['1s']=d['1s']
		weighted['2s']=d['2s']
		weighted['%0']=d['%0']
		weighted['offset']=d['offset']
		weighted['%off']=d['%off']
		weighted['len0']=d['len0']
		weighted['seq']=d['seq']
		weighted['seq_weight']=d['seq_weight']
		weighted['seq_offset']=round(percentageDiff(d['seq']+3,d['len0']+3)-d['seq_weight'],3)
		weighted['seq_weight_offsetted']=round(weighted['seq_weight']+weighted['seq_offset'],2)
		# return weighted



		if weighted['seq_weight_offsetted'] > 99 and not string1 == string2: weighted['seq_weight_offsetted']=99
		if weighted['seq_weight'] > 99 and not string1 == string2: weighted['seq_weight']=99

		if w: return weighted['seq_weight_offsetted']
		return weighted['seq_weight']








def pattern_probability_list(_str,_list):
	# pattern_probability(string1,string2,w=False)
	pattern_list=[]
	l_str=len(_str)
	l_list=list(_str)
	for li in _list:
		l_li=len(li)
		lg=l_list
		ll=l_li
		if l_li > l_str:
			lg=l_li
			ll=l_str
		else:
			lg=l_str
			ll=l_li
		diff=lg-ll
		common=list(set(l_list) & set(list(li)))

		p1=percentageDiff(len(common),l_str)
		p2=percentageDiff(len(common),l_li)
		p0=p1
		if p2 < p1: p0=p2

		pattern_list.append({ 'pCommon': p0, 'diff': diff, 'li': li, 'len': l_li, 'common': common })
	# pattern_list = tables.returnSorted( 'data', 'd.diff,d.cnt,d.common', pattern_list )
	pattern_list = tables.returnSorted( 'data', 'd.pCommon', pattern_list )
	top=pattern_list[0]
	probable=[]

	for i,rec in enumerate(pattern_list):
		if rec['pCommon']:
			px=percentageDiff( rec['pCommon'], top['pCommon'] )
			if not px or px > 50:
				if rec['pCommon'] > 50:
				# if i < 10:
					# print()
					# print(px)
					# print(rec)
					probability=pattern_probability(_str,rec['li'])
					w_probability=pattern_probability(_str,rec['li'],w=True)
					if probability and probability >= 50:
						# print(probability)
						rec['probability']=probability
						rec['wprobability']=w_probability
						probable.append(rec)
	# sys.exit()
	if len(probable) > 1: probable = tables.returnSorted( 'data', 'd.probability', probable )
	if not probable: return None
	return probable









# alt+29 ↔ is space
# EOF