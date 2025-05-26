#!/usr/bin/python3
########################################################################################

# library

## epyi baseIC
## p ic
########################################################################################
# alt+29 ↔ is space
# helpColorScheme

##################################################
import _rightThumb._construct as __
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################
import glob
import sys,os,time,datetime,threading
from operator import itemgetter
from datetime import datetime as dt, timedelta
from datetime import date
##################################################
SHOW_ADS = False
MINI_ADS = False
ADS_CONFIG = False
if ADS_CONFIG:
	adFigFi = _v.myConfig+os.sep+'ads.yml'
	if os.path.isfile(adFigFi):
		adFig = __.getTable(adFigFi,True)
		# print(adFig)
		if 'show' in adFig: SHOW_ADS = adFig['show']
		if 'mini' in adFig: MINI_ADS = adFig['mini']



##################################################
__.showLine_quoteFix=True
##################################################


#                  ¯\_(ツ)_/¯


##################################################

# releaseAcquiredData

##################################################
class Meta_Namespace():
	def __init__( self ): pass
dot=Meta_Namespace


intelligent_code = Meta_Namespace()
intelligent_code.functions = {}
intelligent_code.classes = {}
helpColorScheme = Meta_Namespace()
liaison = Meta_Namespace()

# __.SwitchGroup_Help.SubGroup
# HasSwitchSubGroup
##################################################
# sudo apt install libpython2.7-stdlib
# import json
# 1674156772
##################################################
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



# from os.path import isfile, isdir
# import uuid

# from threading import Timer
# import simplejson as json
# try:
#   import sqlite3
# except Exception as e:
#   pass



from library.frameworks.base.variables.bundle import    _all_colors_, _all_colors_nobk_, _all_colors_nobk_, _all_colors_tact_




def hexColor(*args, **kwargs):
	if not 'hexColor' in intelligent_code.functions:
		from library.tools.code.functions.hexColor import hexColor
		intelligent_code.functions['hexColor'] = hexColor
	return intelligent_code.functions['hexColor'](*args, **kwargs)

def pyColor(*args, **kwargs):
	if not 'pyColor' in intelligent_code.functions:
		from library.tools.code.functions.pyColor import pyColor
		intelligent_code.functions['pyColor'] = pyColor
	return intelligent_code.functions['pyColor'](*args, **kwargs)









def process_pipe_data(data):
	import datetime
	import uuid
	import json
	original_type = type(data)

	if type(data) in (list, tuple, set):
		data = '\n'.join(data)
	elif type(data) == str:
		pass
	else:
		return data
	# Check if the data is likely text or binary
	# Consider it text if more than 95% of characters are printable
	is_text = sum(c.isprintable() or c.isspace() for c in data) / len(data) > 0.95

	if is_text:
		thresh = 5
		# Remove non-printable characters if it's text from the threshold
		if len(data) > thresh:
			data = ''.join(c if c.isprintable() or c.isspace() else '' for c in data[:thresh]) + data[thresh:]
		else:
			data = ''.join(c if c.isprintable() or c.isspace() else '' for c in data)


	# Convert cleaned data back to original type if possible
	if original_type is list:
		return data.split('\n')
		return data.encode('utf-8')
	elif original_type in (list, tuple, set):
		return original_type(data.split('\n'))
	elif original_type is dict:
		return json.loads(data)
	return data






def call(python_file):
	from os import sep
	path = _v.py+sep+python_file
	import importlib
	module = importlib.import_module(path)
	globals().update({name: getattr(module, name) for name in dir(module) if not name.startswith('_')})


def build_documentation_tables(string):
	snip_table = {}
	doc_lines = []
	_code = regImp( __.appReg, '_rightThumb._auditCodeBase' )
	for i, chr in enumerate(string):
		if i in  _code.imp.validator.identity['identity']:
			o = i
			c = _code.imp.validator.identity['location']['open'][o]

			# Assuming the need to capture snippets based on certain characters
			if chr == '(' or chr == '[':
				snip = string[o:c]
				doc_lines.append(snip)

				# Removing the first occurrence of snip from string
				string = string.replace(snip, '', 1)

				snip_table[o] = {
					'open': o,
					'close': c,
					'o': o,
					'c': c,
					'chr': chr,
					'string': string,
					'snip': snip
				}

	return snip_table, doc_lines
'''
__.imp('simplejson').loads(var)
simplejson = __.imp('simplejson')
simplejson.loads(var)
simplejson.dumps(rows, indent=4, sort_keys=False, default=str)
simplejson.dumps(rows, sort_keys=False, default=str)
'''

__.isData_Switches={}

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
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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


def random_color():
	global _all_colors_
	global _all_colors_nobk_
	global _all_colors_tact_
	import random
	return random.choice(_all_colors_tact_)

print_ed_group={}
def print_(*args,p=None,c=None,pad=3,g=None,end=None,pvs=None,pv=None,json=None, dic=None, line=None, rstrip=True, lineMinus=0, lineLen=None, r=None, h=None):
	if type(args) == tuple: args = list(args)
	global prStatus
	if not prStatus: return args
	# if type(args[0]) == str: args[0] = args[0].decode('utf-8')
	if not r is None: end=r
	args=list(args)
	if c == 'r' or c == 'random': c=random_color()

	if p is None: rint=True;
	elif p: rint=True;
	elif not p: rint=False;
	else: rint=True;

	if json:
		try:
			import simplejson
			json = simplejson
		except:
			pass
		try:
			import json
		except ImportError:
			json = simplejson
		args[0]=simplejson.dumps(args[0], indent=4, sort_keys=False, default=str)
		if rint:
			print(args[0])
		return args[0]
	# if pvs: pvs=None; pv=1;

	if dic == 5:
		for i,a in enumerate(args):
			if type(a) == dict: args[i] = str(a).replace('{','').replace('}','').replace("'",'').replace(', | ',' | ')

	if not dic and type(dic) == bool or ( type(dic) == int and dic == 1): printDicFields(args[0]); return None
	try:
		if not end is None and (type(end) == bool or type(end) == int) and end:   end='\r'
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
		if json:
			try:
				import simplejson
				json = simplejson
			except:
				pass
			try:
				import json
			except ImportError:
				json = simplejson
			args[0]=simplejson.dumps(args[0], indent=4, sort_keys=False, default=str)
		if not line is None and line:
			if not lineLen is None:
				args=[linePrint(c=c,p=0,minus=lineMinus,length=lineLen)]
			else:
				args=[linePrint(c=c,p=0,minus=lineMinus)]
		global print_ed; global print_ed_group; items=[]
		pre=''
		# if not g is None:
		# print_ed_group
		for arg in args:
			if type(arg) == list:
				tmp=[]
				for rg in arg: tmp.append(str(rg))
				items.append( ' '.join(tmp) )
			else:
				items.append(str(arg))
		prn=pre+' '.join(items)
		if rstrip: prn=prn.rstrip()
		if not c is None: prn=cp( prn, c, p=0 )
		if not h is None: prn=hexColor( prn, c=h, p=0 )
		if p is None: rint=True
		elif p: rint=True
		elif not p: rint=False
		else: rint=True
		_line__ = ''
		if rint:
			if not end is None:
				if not lineLen is None:
					_line__ = linePrint(txt=' ',p=0,minus=lineMinus)
					print( _line__ , end=end ); print( prn, end=end )
				else:
					_line__ = linePrint(txt=' ',p=0,minus=lineMinus,length=lineLen)
					print( _line__, end=end ); print( prn, end=end )
			# if not end is None: print( '                                                                                        ' , end=end ); print( prn, end=end );
			else: print( prn )
		print_ed.append({'prn':prn, 'line': _line__ })
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
			if not script is None: script(path)
			if not trigger is None: fo_fi2.append(trigger(path))
			else: fo_fi2.append(path)


	if folder is None: folder=os.getcwd()
	global fo_fi2
	if first: fo_fi2=[]
	if not os.path.isdir(folder) and not os.path.isfile(folder): return fo_fi2
	if not os.path.isdir(folder) and os.path.isfile(folder): folder = __.path(folder,pop=True)

	try: files=os.listdir(folder)
	except Exception as ee: return fo_fi2
	for item in files:
		path=folder+os.sep+item; path=__.path(path)

		if not test is None and test(path): _fo_fi_add(path,trigger,script)

		if os.path.isfile(path) or os.path.isdir(path):
			if test is None: _fo_fi_add(path,trigger,script)
			if r and os.path.isdir(path): fo2(path,r,script,trigger,test,first=False)
	return fo_fi2


fo_rel=''
fo_fi=[]
def fo(folder=None,r=False,script=None,first=True,rel=False):
	global fo_rel
	if folder is None:
		# try: os=__.imp('os.getcwd');
		# except Exception as e: pass;
		folder=os.getcwd()
	global fo_fi
	if first:
		fo_rel = folder
		fo_fi=[]
	if not os.path.isdir(folder): return fo_fi
	try:
		files=os.listdir(folder)
	except Exception as e:
		return fo_fi
	for item in files:
		path=folder+os.sep+item
		path=__.path(path)
		relative=path[len(fo_rel)+1:]
		if os.path.isfile(path):
			if rel:
				fo_fi.append(relative)
			else:
				fo_fi.append(path)

		if not script is None: script(path)
		if r and os.path.isdir(path): fo(path,r,script,False,rel)
	return fo_fi

def fos(folder=None,r=False,script=None,first=True,rel=False):
	global fo_rel
	if folder is None:
		# try: os=__.imp('os.getcwd');
		# except Exception as e: pass;
		folder=os.getcwd()
	global fo_fi
	if first:
		fo_rel = folder
		fo_fi=[]
	if not os.path.isdir(folder): return fo_fi
	try:
		files=os.listdir(folder)
	except Exception as e:
		return fo_fi
	for item in files:
		path=folder+os.sep+item
		path=__.path(path)
		relative=path[len(fo_rel)+1:]
		if os.path.isdir(path):
			if not script is None: script(path)
			if rel:
				fo_fi.append(relative)
			else:
				fo_fi.append(path)
			if r: fos(path,r,script,False,rel)
	return fo_fi


def printt( table, cols=None, sort=None, responsive=None, focus=None,    c=None,s=None,r=None, name='default', fn=None, long=False, l=None, triggers=None, t=None  ):
	if not t is None: triggers = t
	if not l is None: long = l
	if not r is None: responsive=r
	if responsive: cols=unixAutoColumns(table,cols,focus,responsive)
	''' ( table, cols=None, sort=None,    c=None,s=None  ) '''
	if not c is None: cols = c
	if not s is None: sort = s
	if not table: return None;
	global switches
	global tables
	if long:
		switches.fieldSet('Long','active',True)
	if not sort is None:
		switches.fieldSet( 'Sort', 'active', True )
		switches.fieldSet( 'Sort', 'value', sort )
		switches.fieldSet( 'Sort', 'values', sort.split(',') )
	tables.register( name, table )
	if not fn is None and 'function' in str(type(fn)):
		# _.tables.fieldProfileSet('default','attached','alignment','right')
		fn()
	if cols is None: cols=','.join(list(table[0].keys()));
	tables.print( name, cols )

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
	"""
	Recursively traverses and processes complex data structures, such as nested lists and dictionaries,
	generating a list of paths to each item or a dictionary containing the items. The function can be
	configured to perform additional tasks, such as filtering output, previewing values, and adjusting
	output based on language-specific syntax.

	Parameters:
	- data: The data structure to traverse, which can be a list or dictionary.
	- par (str): The parent path to prefix to each key or index.
	- skim: A condition to filter the output paths (default: None).
	- mt (bool): A flag indicating whether to include paths in the output data (default: True).
	- lan (str): Specifies the language for path formatting, either 'js' or 'py' (default: 'js').
	- prev (bool): Flag to determine if previews of values should be included in the output (default: False).
	- dump: A list of specific paths to print or process (default: None).
	- dic (bool): If True, returns a dictionary containing the data items (default: False).
	- list0 (bool): If True, paths for list items start at index 0 (default: True).

	Returns:
	- When dic is False, returns a list of strings representing the paths to each item.
	- When dic is True, returns a dictionary with paths as keys and corresponding data as values.
	"""

	if type(dump)==str: dump=[dump]
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
			e('type(key)')
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
	if dic: return tinydic_dic
	return tinydic_data


def tailpop(subject, delim):
	parts = subject.rsplit(delim, 1)
	return parts[0] if len(parts) > 1 else ''


def tab(val,n=None, t='    ', cnt=False, add=None,  s=False):
	'''
		Tabulate a string, adding tabs to the beginning of each line.
		
		Arguments:
			val {str} - The string to tabulate.
			
		Keyword Arguments:
			n {int} - The number of tabs to add. (default: {1})
			t {str} - The tab character to use. (default: {'    '})
			cnt {bool} - Count the number of tabs needed to align the string. (default: {False})
			add {bool} - Add a tab to the beginning of each line. (default: {None})
			s {bool} - Shorten the string by removing unneeded tabs. (default: {False})
		
		Returns:
			str - The tabulated string.
	'''
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

def vindex(*args, **kwargs):
	if not 'vindex' in intelligent_code.functions:
		from library.frameworks.base.functions.vindex import  vindex
		intelligent_code.functions['vindex'] = vindex
	return intelligent_code.functions['vindex'](*args, **kwargs)


##change
class Switches:
	def __new__(cls, *args, **kwargs):
		if not 'Switches' in intelligent_code.classes:
			from library.frameworks.base.classes.Switches import Switches
			intelligent_code.classes['Switches'] = Switches
		return intelligent_code.classes['Switches'](*args, **kwargs)


class Tables:
	def __new__(cls, *args, **kwargs):
		if not 'Tables' in intelligent_code.classes:
			from library.frameworks.base.classes.Tables import Tables
			intelligent_code.classes['Tables'] = Tables
		return intelligent_code.classes['Tables'](*args, **kwargs)



# class TableSystem:
# 	def register(self, *args, **kwargs):
# 		global tables
# 		if not 'Tables' in intelligent_code.classes:
# 			from library.frameworks.base.classes.Tables import Tables
# 			intelligent_code.classes['Tables'] = Tables
# 		self = intelligent_code.classes['Tables']
# 		return tables.register(*args, **kwargs)
	
# 	def print(self, *args, **kwargs):
# 		global tables
# 		if not 'Tables' in intelligent_code.classes:
# 			from library.frameworks.base.classes.Tables import Tables
# 			intelligent_code.classes['Tables'] = Tables
# 		self = intelligent_code.classes['Tables']
# 		return tables.print(*args, **kwargs)
# 	def returnSorted(self, *args, **kwargs):
# 		global tables
# 		if not 'Tables' in intelligent_code.classes:
# 			from library.frameworks.base.classes.Tables import Tables
# 			intelligent_code.classes['Tables'] = Tables
# 		tables = intelligent_code.classes['Tables']
# 		# intelligent_code.classes['Tables'] = Tables
# 		return intelligent_code.classes['Tables'].returnSorted(*args, **kwargs)


try:
	import colorama
	colorama.init()
except Exception as e:
	pass

# from threading import Thread



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
def myFolder(subject):
	if type(subject) == str:
		subjects = [subject]
	elif type(subject) == list:
		subjects = subject
	else:
		print_(type(subject))
		err( 'myFolder', subject )
	results=[]

	for sub in subjects:
		if os.path.isdir(sub):
			results.append(sub)
		else:
			global _bm
			if _bm is None:
				import _rightThumb._bookmarks as _bm
			path = _bm.Bookmarks( sub ).get2()
			# print_(sub,path)
			if path is None:
				cp( 'Error, Bookmark does not exist', 'red' )
				results.append(sub)
			else:
				results.append(path)
	# print(results)
	if type(subject) == str and len(results):
		return results[0]
	elif type(subject) == str and not len(results):
		return subject
	elif type(subject) == list:
		return results
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
			path = _bm.Bookmarks( sub ).get2()
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


__.tableLine = '‽'
__.tableLine = '\t'
v = dot()
vv = dot()
vv.isData = {}
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

def printDicFields( dic,title=None ,t=None ):
	if not t is None: title=t
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

	if title:
		fields.register( 'dic', 'title', str(title) )
		for k in dic: fields.register( 'dic', 'title', fields.value( 'dic', 'field', str(k)+':', right=True )+fields.value( 'dic', 'value', str(dic[k]) ) )
		ti='↓'+fields.value( 'dic', 'title', str(title), center=True )+'↓';  pr(ti,c='Background.blue');
	for k in dic:
		print_( pr(fields.value( 'dic', 'field', str(k)+':', right=True ),c='darkcyan',p=0), pr(fields.value( 'dic', 'value', str(dic[k]) ),c='cyan',p=0) )
	# if title: ti='↑'+fields.value( 'dic', 'title', str(title), center=True )+'↑';  pr(ti,c='Background.blue');
	# if title: ti='↑'+fields.value( 'dic', 'title', ' ', center=True )+'↑';  pr(ti,c='Background.blue');

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
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
	dic=simplejson.loads(txt)
	# print(dic)
	# print((dic))
	if dic['s']==59:
		dic=date_diff_dic(oneA+1,twoA)
		if dic['s']==58:
			dic=date_diff_dic(oneA-1,twoA)
	return dic


def isDate(*args, **kwargs):
	if not 'isDate' in intelligent_code.functions:
		from library.frameworks.base.functions.isDate import isDate
		intelligent_code.functions['isDate'] = isDate
	return intelligent_code.functions['isDate'](*args, **kwargs)


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

##change
# from library.frameworks.base.classes.AGGREGATE import AGGREGATE, aggregate_trigger
# __.aggregate.obj = AGGREGATE()



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
	try:
		if pyperclip is None:
			import pyperclip
		pyperclip.copy( cleanString(stripColor(cleanString(data))) )

	except: pass


def getClip():
	global pyperclip
	# try:except: pass
	try:
		if pyperclip is None:
			import pyperclip
		return cleanString( pyperclip.paste() )
	except: return ''

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
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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


def saveCryptTable(*args, **kwargs):
	if not 'saveCryptTable' in intelligent_code.functions:
		from library.frameworks.base.functions.saveCryptTable import saveCryptTable
		intelligent_code.functions['saveCryptTable'] = saveCryptTable
	return intelligent_code.functions['saveCryptTable'](*args, **kwargs)



def head( path ): return IS(path)
def header(path): return head(path)
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

def linePrint(  label=None, text=None, txt='_', mn=50, add=5, p=2, c='', x=None,pre='',length=None, center=None, minus=0 ):
	color=c
	if not length is None:
		mn=length
	ln = mn
	if text is None and label is None:
		if length is None and __.terminal.width:
			ln = __.terminal.width
			add = 0
	ln-=minus
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


def dic_key_sort2(*args, **kwargs):
	if not 'dic_key_sort2' in intelligent_code.functions:
		from library.frameworks.base.functions.dic_key_sort2 import dic_key_sort2
		intelligent_code.functions['dic_key_sort2'] = dic_key_sort2
	return intelligent_code.functions['dic_key_sort2'](*args, **kwargs)

def dic_key_sort( table, n=False ):
	saveTable( table, '-tmp-dic_key_sort.json', tableTemp=True, printThis=False,  sort_keys=True )
	return getTable( '-tmp-dic_key_sort.json', tableTemp=True )
	# dataDump = json.dumps(table, indent=4, sort_keys=True, default=str)
	# print_(dataDump)
	# sys.exit()
	# return json.load( str(dataDump) )


def isCrypt(path):
	if IS(path,'41 45 53 02 00 00 1B'): return True
	else:
		if has_crypt_header(path):
			return True
		else:
			return False

def isGz(path):
	if IS(path,'1F 8B 08 08'): return True
	else: return False

def isBz2(path):
	if IS(path,'42 5A 68'): return True
	else: return False


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


def zeros3(n,total,z='0'):
	''' calculating length of output '''
	c=len(str(total))

	result = ''
	a = len(str(n))
	while not len(result)+a == c:
		result += z
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



def percentageDiffIntAuto(smaller, bigger, isFloat=False):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	if not isFloat:
		return percentageDiffInt(s, b)
	else:
		result = round(float(s / b * 100), 1)
		r = str(result)
		if '.0' in r:
			result = int(result)
		return result
def percentageDiffAuto(smaller, bigger, isFloat=False, rnd=1):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	return _.percentageDiffCalc(s, b, isFloat, rnd)
def percentageDiffSmaller(smaller, bigger, isFloat=False, rnd=1):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	a = _.percentageDiffCalc(s, b, isFloat, rnd)
	b = _.percentageDiffCalc(b, s, isFloat, rnd)
	if a < b:
		return a
	else:
		return b
def percentageDiffCalc(smaller, bigger, isFloat=False, rnd=1):
	try:
		if not isFloat:
			return int(round(abs(abs(smaller - bigger) / smaller) * 100, 0))
		else:
			r = round(abs(abs(smaller - bigger) / smaller) * 100, rnd)
			if str(r) == '0.0':
				return 0
			return r
	except Exception as e:
		return 0
		smaller += 1
		bigger += 1
		if not isFloat:
			return int(round(abs(abs(smaller - bigger) / smaller) * 100, 0))
		else:
			r = round(abs(abs(smaller - bigger) / smaller) * 100, rnd)
			if str(r) == '0.0':
				return 0
			return r

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

#     print(vv.isData)
#     print(data)
#     return data
FilesFiles = []
def isData( data=None, focus=None, pipeClean=False, required=False,     r=None, c=None, noclean=None, p=False ):
	global FilesFiles
	FilesFiles = myFileLocation_Files
	__.FilesFiles = myFileLocation_Files
	global switches
	global appData
	if type(appData[__.appReg]['pipe']) == list:
		if p: 
			return appData[__.appReg]['pipe']
		pipeCleaner(0)
	try:
		if appData[__.appReg]['pipe']: return appData[__.appReg]['pipe']
		for sw in __.isData_Switches:
			if not sw == 'Files': return switches.values(sw)
		if data is None and switches.isActive('Paste-isData-json'):
			try:
				import simplejson
				json = simplejson
			except:
				pass
			try:
				import json
			except ImportError:
				json = simplejson
			d=getClip().strip()
			return simplejson.loads(d)
		elif data is None and switches.isActive('Paste-isData'): return getClip().split('\n')


		def _isData_(tst):
			global myFileLocation_Files
			# if not tst and pipe_surfing(): tst = pipe_surfing()
			if not tst: return myFileLocation_Files;
			# print(tst,myFileLocation_Files)

			for name in vv.isData:
				if len(switches.values(name)):
					if 'data' in vv.isData[name]: return tst

			if myFileLocation_Files and os.path.isfile(myFileLocation_Files[0]): return myFileLocation_Files
			return tst
		def isData_path_list(stuff,dAta=[]):
			for f in stuff:
				f = __.path(f)
				if os.path.isfile(f):
					dAta.append(f)
			return dAta

		if not noclean is None: pipeClean=noclean
		if not c is None: pipeClean=c;
		if not r is None: required = r;
		# pr('here',data,c='gray')

		if data is None:
			if pipeClean:
				pipeCleaner(0)
			if focus is None:
				focus = __.appReg
			data = pipe_surfing()


		if type(data) ==list and  len(data)==1 and data[0]=='': data=[]
		if not data:
			data=[]
			# global switches
			isClean=False
			
			for name in vv.isData:
				if len(switches.values(name)):
					for isD in vv.isData[name].split(','):
						if isD == 'clean' and noclean is None:
							isClean=True
						elif isD == 'name':
							for n in switches.values(name):
								data.append(n)
						elif isD == 'glob' and 'data' in vv.isData[name]:
							for n in switches.values(name):
								for f in isData_path_list( glob.glob( n ) ):
									__.FilesFiles.append(f)
									for xXx in getText2( f ).split('\n'):
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
								__.FilesFiles.append(n)
								tData.append(getText2(n))
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
	except: e('Data src missing','possibly: -f')

def payloadCache( data, file=None, theFocus=None ):
	# _.payloadCache( saveFile, __file__, focus() )

	if theFocus is None:
		theFocus = __.appReg
	if file is None:
		appDBA = __.thisApp( __.postLoadFile )
	else:
		appDBA = __.thisApp( file )
	__.appInfoAcquiredData = { 'app': appDBA, 'focus': theFocus, 'data': data }
	__.appInfoAcquiredData['app'] = appDBA
	__.appInfoAcquiredData['focus'] = theFocus
	__.appInfoAcquiredData['data'] = data
	# releaseAcquiredData( appDBA, theFocus, data )

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


def help(justAppNotFullHelp=True):
	global switches
	switches.help(justAppNotFullHelp)

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

def unixAutoColumns( asset, columns, focus=None, threshold=10 ):
	if not isinstance(threshold, int): threshold=10
	import _rightThumb._md5 as _md5
	label=_md5.string(str(asset))
	if not asset or not len(asset):
		return columns
	asset = asset.copy()

	if columns is None:
		columns=','.join(list(asset[0].keys()))

	if not __.terminal.width:
		return columns

	cols = __.terminal.width
	cols-=threshold
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
	fields.asset( label, asset )
	lengths = fields.lengths( label )

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
	if not len(importance):
		e(
			'columns registration missing',
			[
				'in _.appInfo[focus()] = {',
				'order them most important fields on top',
				'to least on bottom',
			])
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

responsiveColumns = unixAutoColumns
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
			try:
				folderProfileAttribute( folder, info )
			except: pass
			return None

		try:
			if record[what] == {}:
				record[what][app] = {}
				record[what][app][epoch] = info
				saveTable2( record, saveTo )
		except: pass

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


def percentageDiff(smaller, bigger, isFloat=False):
	try:
		if not isFloat:
			return abs(smaller / bigger) * 100
		else:
			r = abs(smaller / bigger) * 100
			if str(r) == '0.0':
				return 0
			return r
	except Exception as e:
		return 0
		smaller += 1
		bigger += 1
		if not isFloat:
			return abs(smaller / bigger) * 100
		else:
			r = abs(smaller / bigger) * 100
			if str(r) == '0.0':
				return 0
			return r
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
	# dicf_()
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
	return myFolder(data)
	if 'myFolderLocations' in __.setting('omit-functions', d=[]):
		return data
	if type(data) == list:
		for i,d in enumerate(data):
			data[i] = myFolderLocations(d)
		return data
	return aliasesFo(data)
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
	subject = subject.replace('*','')
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



def saveCSV(data, filename):
	"""
	Save a list of dictionaries as a CSV file.

	Arguments:
		data: A list of dictionaries containing the data to be saved.
		filename: The name of the file to be saved.
	"""
	import csv
	with open(filename, 'w', newline='') as csvfile:
		fieldnames = data[0].keys()
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for row in data:
			writer.writerow(row)


def saveCSV2( data, file, printThis=True,here=False,                p=None, me=0,h=None ):
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

class AllColor:
	magenta = '\033[1;35;40m'
	red = '\033[1;31;40m'
	green = '\033[92m'
	cyan = '\033[0;36;47m'
	white = '\033[1;37;40m'
	bold = '\033[1m'
	yellow = '\033[1;37;43m'
	blue = '\033[1;34;47m'
	blue = '\033[0;34;47m'
	end = '\033[0m'
	red = '\033[91m'
	blue = '\033[1;37;44m'
	cyan = '\033[1;36;40m'
	light_blue = '\033[1;37;46m'
	yellow = '\033[93m'
	brown = '\033[0;33;47m'
	yellow = '\033[1;33;40m'
	red = '\033[0;31;47m'
	brown = '\033[1;33;47m'
	gray = '\033[1;30;40m'
	gray = '\033[1;37;40m'
	magenta = '\033[0;35;47m'
	cyan = '\033[1;36;47m'
	green = '\033[1;37;42m'
	black = '\033[1;30;47m'
	magenta = '\033[1;35;47m'
	red = '\033[1;31;47m'
	green = '\033[0;32;47m'
	underline = '\033[4m'
	blue = '\033[1;34;40m'
	cyan = '\033[96m'
	purple = '\033[95m'
	darkcyan = '\033[36m'
	purple = '\033[1;37;45m'
	red = '\033[1;37;41m'
	black = '\033[1;37;48m'
	black = '\033[0;30;47m'
	green = '\033[1;32;47m'
	gray = '\033[0;37;40m'
	grey = '\033[1;37;47m'
	green = '\033[1;32;40m'
	blue = '\033[94m'

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


def colorizeRowLength( row, tableID=False, prefix='', prefixColor='', haltColorShift=False, pipe_break=True ):
	global colorizeRow_last
	if len(prefix) and len(prefixColor):
		prefix = colorThis( prefix, prefixColor, p=0 )
	global switches
	if switches.isActive( 'NoColor' ):
		return len(row.replace('‽',''))
		return False

	if type(tableID) == bool:
		tableID = __.color_palette
	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		return len(row)
	else:
		if _str.hasVisible(row):
			up =True
		else:
			up =False
		# print_( 'tableID:', tableID, colorID( tableID ) )
		# print_( str(len(row))+colorID( tableID, up ) + row + Background.end )
		if not pipe_break or not __.tableLine in row:
			print_( prefix + colorizeRow_last + row )
		else:
			sep = ' '
			line = prefix + sep
			parts=[]
			for part in row.split(__.tableLine):
				parts.append( colorizeRow_last + part + Background.end )

			line += sep.join(parts) + sep
			return len(line)

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
		printBold( 'Color:: ' + str(color), 'red' )
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




def percentageInt(percent, whole, isFloat=False):
	if not isFloat:
		return int(round(percent * whole / 100.0, 0))
	else:
		return round(percent * whole / 100.0, 1)
def percentageDiffInt(smaller, bigger, isFloat=False, rnd=1):
	try:
		if not isFloat:
			return int(round(abs(smaller / bigger) * 100, 0))
		else:
			r = round(abs(smaller / bigger) * 100, rnd)
			if str(r) == '0.0':
				return 0
			return r
	except Exception as e:
		return 0
		smaller += 1
		bigger += 1
		if not isFloat:
			return int(round(abs(smaller / bigger) * 100, 0))
		else:
			r = round(abs(smaller / bigger) * 100, rnd)
			if str(r) == '0.0':
				return 0
			return r


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

def remove_carriage_returns():
	lines = sys.stdin.readlines()
	return [line.replace('\r', '') for line in lines]

def fromEpoch( epoch ):
	return datetime.datetime.fromtimestamp(epoch).strftime('%c')

def postLoad( file, epoch=0, theFocus=False ):
	try:
		if os.environ['burn_this'] == 'yes': return None;
	except: pass
	__.postLoadFile = file
	global autoLoadData
	global switches
	global appData

	if not sys.stdin.isatty():
		setPipeData( sys.stdin.readlines(), __.appReg, clean=l.conf('clean-pipe' ,d=False) )

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
		__.appInfoAcquiredData['app'] = appDBA
		__.appInfoAcquiredData['focus'] = theFocus
		# __.appInfoAcquiredData['data'] = data
		# __.appInfoAcquiredData = { 'app': appDBA, 'focus': theFocus }
		# reclaimAcquiredData( appDBA, epoch, theFocus )
	else:
		__.appInfoAcquiredData['app'] = appDBA
		__.appInfoAcquiredData['focus'] = theFocus
		# __.appInfoAcquiredData['data'] = data
		# __.appInfoAcquiredData = { 'app': appDBA, 'focus': theFocus }
		# releaseAcquiredData( appDBA, theFocus )

# print(os.environ['burn_this']); sys.exit();

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
	try:
		if os.environ['burn_this'] == 'yes': return None;
	except: pass
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
				'folder': os.getcwd(),
				'app': appDBA,
				'session': _v.session(),
				'rebuiltCommand': password_filter(rebuiltCommand),
				'rebuiltCommandEpoch': password_filter(rebuiltCommandEpoch),
				'files': [],
				'switches': mask_password(switches.getTable()),
				'errors': [],
				'printed': print_ed,
	}
	# print(print_ed)
	# global switches
	if switches.isActive('SavePrint'):
		printed = []
		for rec in print_ed:
			printed.append( rec['prn'].rstrip() )
		saveText(printed,switches.value('SavePrint'))

	if switches.isActive('CopyPrint'):
		printed = []
		for rec in print_ed:
			printed.append( rec['prn'].rstrip() )
		_copy = regImp( __.appReg, '-copy' )
		_copy.imp.copy( '\n'.join(printed), p=0 )
		


	# pv(info); sys.exit();
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
		secureFiles = _secure_files_()
		if len( myFileLocation_Files ):
			for i,file in enumerate(myFileLocation_Files):
				if os.path.isfile(file):
					if not __.path(file) in secureFiles:
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




		try: saveTable2( info, log )
		except:
			if raq_err: pr('d8f4',c='red')
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
	# __.payloadCache = None
	if 'payload' in info:
		__.store.set('payloadCache', info['payload'])
		# __.payloadCache = info['payload']


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

def addComma2(data):
	try:
		# Convert the data to a float
		data = float(data)
	except ValueError:
		# If conversion fails, return the original data
		return data
	
	# Check if there's a decimal part
	if '.' in str(data):
		# Round to 2 decimal places if there are decimals
		data = round(data, 2)
	
	# Convert the number to string and split into integer and decimal parts
	integer_part, *decimal_part = str(data).split('.')
	
	# Reverse the integer part and insert commas every three digits
	reversed_integer = integer_part[::-1]
	grouped_reversed_integer = ','.join(reversed_integer[i:i + 3] for i in range(0, len(reversed_integer), 3))
	
	# Reverse it back to the original order
	formatted_integer = grouped_reversed_integer[::-1]
	
	# Join the integer part with the decimal part if it exists
	if decimal_part:
		return f"{formatted_integer}.{decimal_part[0]}"
	else:
		return formatted_integer


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
def setPipeData( data, theFocus=False, clean=False ):

	# data = process_pipe_data( data )
	# if type(data) == str: data=data.replace('\r','')
	# if type(data) == list: data='\n'.join(data).replace('\r','').split('\n')
	global appData
	if type( theFocus ) == bool:
		theFocus = __.appReg
	if not appData[theFocus]['pipe'] and len(data) > 0:
		# if not clean:
		#   setPipeDataRan = True
		#   appData[theFocus]['pipe']=data
		#   return data
		appData[theFocus]['pipe'] = []
		for pd in data:
			if clean:
				pd = pd.replace('\n','')
				pd = pd.replace('\r','')
				if not pd == '':
					appData[theFocus]['pipe'].append(pd)
			else:
				appData[theFocus]['pipe'].append(pd.rstrip())
		setPipeDataRan = True



def pipeCleaner(clean=0):
	if 'clean-pipe' in l.v.cnf.data and not l.conf('clean-pipe'): return
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
			if len(appData[__.appReg]['pipe'][0]):
				if not appData[__.appReg]['pipe'][0][0] in _str.safe:
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
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
	# saveTable2( data, _v.json_temp )
	# txt = getText( _v.json_temp, raw=True )

	return simplejson.dumps(data, indent=4, sort_keys=sort_keys, default=str)

def printVar1( data ):
	print_( d2json( data ) )


def printVar( data, sort_keys=False, isDic=None ):
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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

def printVarSimple( data, sort_keys=False, isDic=None, prefix=None, remove=None, d=None, p=True, r=None, min=False ):
	#n)--> r, stands for just return and not print
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
	if min:
		dump=simplejson.dumps(data, sort_keys=sort_keys, default=str)
		print(dump)
		return dump
	else:
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


def printVarSimpleFake3( data ):
	for line in data.split('\n'):
		try:
			printVarColor(line)
		except Exception as e:
			print(line)
def printVarSimpleFake2(*args, **kwargs):
	if not 'printVarSimpleFake2' in intelligent_code.functions:
		from library.frameworks.base.functions.printVarSimpleFake2 import printVarSimpleFake2
		intelligent_code.functions['printVarSimpleFake2'] = printVarSimpleFake2
	return intelligent_code.functions['printVarSimpleFake2'](*args, **kwargs)

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
	# myFileLocationsABC( file, silent=silent, currentBaseVersion=currentBaseVersion )
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
	file = aliases_file_open(path)
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

file_open_aliases=None
def aliases_file_open(file):
	if not os.path.exists(file):
		global file_open_aliases
		if file_open_aliases is None: file_open_aliases = getTable('file-open-aliases.hash')
		if 'aliases' in file_open_aliases and file in file_open_aliases['aliases']:
			a=file
			file = file_open_aliases['aliases'][file]
			# print(a,file)
	return file

def url2file(path):
	url=path
	if path.startswith('http:'): path=path.replace('http:','https:')
	if path.startswith('https:') or path.startswith('http:'):
		url=url.replace('https://www.','https://')
		url=url.replace('http://www.','http://')
		if '?' in url: url=url.split('?')[0]
		sites=getTable('site-locations.list')
		for mPath in sites:
			if os.path.isfile(mPath):
				p = __.path(mPath,pop=True)
				if getText( mPath, raw=True ).strip().startswith('{'): meta = getTable2( mPath )
				else: meta = getYML( mPath )
				if 'url' in meta:
					u = meta['url'].replace('https://www.','https://')
					u = meta['url'].replace('http://www.','http://')
					if url.startswith(u):
						x=url[len(u):].replace('/',os.sep)
						# print(x);sys.exit()
						# print(x);sys.exit();
						y=p+os.sep+x
						# if not os.path.isdir(y): print('missing folder')
						if os.path.isdir(y):
							test='index.php index.htm index.html'.split(' ')
							for t in test:
								yt=str(y+os.sep+t).replace(os.sep+os.sep,os.sep)
								if os.path.isfile(yt):
									y=yt
						y=y.replace(os.sep+os.sep,os.sep)
						if os.path.isfile(y):
							path=y
	return path

isFirst=True
def myFileLocations( file, silent=False, currentBaseVersion=3 ):
	if True:
		valid = True
		for test in [
			'unclaimed_tickets_history',
		]:
			if test in file:
				valid = False
		if valid:
			recs = getTable('myFileLocations.index')
			if not recs: recs = {}
			if type(file) == str:
				files = [file]
			for path in files:
				path = __.path(path)
				try:
					recs[path] = {'epoch': time.time(), 'session': os.environ['Session_ID']}
				except:
					recs[path] = {'epoch': time.time(), 'session': time.time()}
			saveTable(recs,'myFileLocations.index',printThis=False)

	file=url2file(file)
	file = aliases_file_open(file)
	if isWin and type(file) == str and '/' in file: file=file.replace('/',os.sep)
	if isWin and type(file) == str and file.startswith('~'): file=_v.home+file[1:]
	if __.isRequired_Pipe_or_File:
		return file
	# return file
	global appData
	global isFirst
	if '*' in file:
		__.trigger_isPipe = 'glob'
	if os.path.exists(file):
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
							try:
								appData[__.appReg]['pipe'].append( thisFile )
							except: pass
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

	if os.path.exists( file ):
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

def friendlyDate3( theDate ):
	theDate = autoDate(theDate)
	return str(datetime.datetime.fromtimestamp(float(theDate)).strftime('%Y-%m-%d %H:%M:%S'))
	return str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(theDate)))


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

def md5UUID(string,brackets=False):
	import hashlib
	md5_hash = hashlib.md5(string.encode('utf-8')).hexdigest()
	if brackets:
		uuid_format = f"{{{md5_hash[:8]}-{md5_hash[8:12]}-{md5_hash[12:16]}-{md5_hash[16:20]}-{md5_hash[20:]}}}"
	else:
		uuid_format = f"{md5_hash[:8]}-{md5_hash[8:12]}-{md5_hash[12:16]}-{md5_hash[16:20]}-{md5_hash[20:]}"
	return uuid_format

def regMD5( data, project='', label='' ):
	myMD5 = md5UUID(data)
	if len(project):
		resolve = getTable('idResolution.json')
		if len(label):
			resolve.append({'id': myMD5, 'name': project+' - '+label})
		else:
			resolve.append({'id': myMD5, 'name': project})
		saveTable(resolve,'idResolution.json',printThis=False)
	return myMD5

def regMD5Mini( data, project='', label='' ):
	myMD5 = md5UUID(data).split('-')[-1]
	if len(project):
		resolve = getTable('idResolution.json')
		if len(label):
			resolve.append({'id': myMD5, 'name': project+' - '+label})
		else:
			resolve.append({'id': myMD5, 'name': project})
		saveTable(resolve,'idResolution.json',printThis=False)
	return myMD5

def regID( data, project='', label='' ):
	data = str(data)
	if not len(project): return data
	if len(project):
		resolve = getTable('idResolution.json')
		if len(label):
			resolve.append({'id': data, 'name': project+' - '+label})
		else:
			resolve.append({'id': data, 'name': project})
		saveTable(resolve,'idResolution.json',printThis=False)
	return data

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

	try: uuid = __.imp('uuid')
	except: import uuid

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
	if len(project):
		resolve = getTable('idResolution.json')
		if len(label):
			resolve.append({'id': string, 'name': project+' - '+label})
		else:
			resolve.append({'id': string, 'name': project})
		saveTable(resolve,'idResolution.json',printThis=False)
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

def tinyUUID(length=8):
	import random
	import string
	characters = string.ascii_lowercase + string.digits
	return ''.join(random.choice(characters) for _ in range(length))


def UUID_Epoch2(vVv=None,dec=2,epoch=None):
	myuuid = UUID_Epoch(vVv,dec,epoch)
	return myuuid[1:-1]
def UUID_Epoch(vVv=None,dec=2,epoch=None):

	if vVv is None:
		vVv = genUUID()

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





## UUID ## END ############################################################################################################################


__.fn.saveText = False
def saveText( rows, theFile, errors=True, me=0, test=None, lock=False ):
	if lock:
		FileLocker.check(theFile)
		FileLocker.lock(theFile)
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
				encoding_list = [ 'utf-8', "ascii", "big5", "big5hkscs", "cp037", "cp273", "cp424", "cp437", "cp500", "cp720", "cp737", "cp775", "cp850", "cp852", "cp855", "cp856", "cp857", "cp858", "cp860", "cp861", "cp862", "cp863", "cp864", "cp865", "cp866", "cp869", "cp874", "cp875", "cp932", "cp949", "cp950", "cp1006", "cp1026", "cp1125", "cp1140", "cp1250", "cp1251", "cp1252", "cp1253", "cp1254", "cp1255", "cp1256", "cp1257", "cp1258", "cp65001", "euc_jp", "euc_jis_2004", "euc_jisx0213", "euc_kr", "gb2312", "gbk", "gb18030", "hz", "iso2022_jp", "iso2022_jp_1", "iso2022_jp_2", "iso2022_jp_2004", "iso2022_jp_3", "iso2022_jp_ext", "iso2022_kr", "latin_1", "iso8859_2", "iso8859_3", "iso8859_4", "iso8859_5", "iso8859_6", "iso8859_7", "iso8859_8", "iso8859_9", "iso8859_10", "iso8859_11", "iso8859_13", "iso8859_14", "iso8859_15", "iso8859_16", "johab", "koi8_r", "koi8_t", "koi8_u", "kz1048", "mac_cyrillic", "mac_greek", "mac_iceland", "mac_latin2", "mac_roman", "mac_turkish", "ptcp154", "shift_jis", "shift_jis_2004", "shift_jisx0213", "utf_32", "utf_32_be", "utf_32_le", "utf_16", "utf_16_be", "utf_16_le", "utf_7", "utf_8", "utf_8_sig"]

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
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] )
	if lock:
		FileLocker.unlock(theFile)
def getText2(theFile,what='text',t=None,l=None):
	if not t is None and t: what='text'
	if not l is None and l: what='list'

	# Extended list of encodings
	encodings = ['utf-8', 'latin-1', 'ascii', 'iso-8859-1', 'windows-1252', 'utf-16', None]  # None for system default
	for encoding in encodings:
		try:
			with open(theFile, 'r', encoding=encoding) as f:
				if what.lower().startswith('l'):
					return f.readlines() # list
				else:
					return f.read() # text
		except Exception as e:
			pass
			# print(f"Failed to open the file with {encoding} encoding. Error: {e}")
	raise Exception(f"Failed to read the file {theFile} with any of the provided encodings.")


def getText( theFile, raw=False, clean=False,  e=0, c=0 ):
	if type(theFile) == list: theFile = theFile[0]
	if os.path.isfile(theFile):
		vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	HD.chmod(theFile)
	lines = None
	if os.path.isfile(theFile):
		if raw:   what = 'text'
		else:     what = 'list'
		lines = getText2( theFile, 'list' )
		# try:
		# 	f = open(theFile, 'r', encoding='utf-8')
		# 	lines = f.readlines()
		# 	f.close()
		# except Exception as e:
		# 	try:
		# 		f = open(theFile, 'r', encoding='latin-1')
		# 		lines = f.readlines()
		# 		f.close()
		# 	except Exception as e:
		# 		f = open(theFile, 'r')
		# 		lines = f.readlines()
		# 		f.close()
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

hasPlus=None
def showLine( string, plus = '', minus = '',plusOr = False, end=None,isSub=False, OR=None, code=False, itIs=False ):

	# <2024-04-02>
	string = str(string)
	string = string.strip()
	# </2024-04-02>


	'''showLine( string, plus = '', minus = '',plusOr = False, end=None,isSub=False, OR=None, code=False )'''
	global switches
	global hasPlus
	if hasPlus is None:
		hasPlus = switches.isActive('Plus')
	if not hasPlus:
		if not string or not string.strip(): return True
	# print_(plus)
	# print_(string)
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
		result = minusResults(string,minus,itIs)
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



def positive_results_code(string, plus='', plus_or=False, end=None, OR=None):
	# Preliminary adjustments and setup
	global switches
	plus_or = OR if OR is not None else (plus_or or switches.isActive('PlusOr'))

	plus_input = _prepare_plus_input(plus)

	# Handle case sensitivity
	strict_case = switches.isActive('StrictCase')
	if not strict_case:
		string = string.lower()
		plus_input = [item.lower() for item in plus_input]

	# Add 'end' to 'plusInput' if provided
	if end is not None:
		plus_input = [item + end for item in plus_input]

	# Check if 'plusInput' exists in the string
	count_found = sum(1 for item in plus_input if _is_substring_present(item, string))

	return count_found == len(plus_input) or (plus_or and count_found > 0)


def _prepare_plus_input(plus):
	"""Prepare the 'plus' input parameter"""
	global switches
	if not plus:
		return switches.values('Plus').copy()
	elif isinstance(plus, str):
		return [plus]
	return plus


def _is_substring_present(sub, main_string):
	"""Check if a substring is present based on various conditions."""
	if '=' in __.sw.PlusCode:
		return main_string == sub
	if '*x' in __.sw.PlusCode:
		return main_string.endswith(sub)
	if 'x*' in __.sw.PlusCode:
		return main_string.startswith(sub)

	no_break_chars = '[]()_01`23456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"' + "'" + sub
	cleaned_main_string = ''.join(char if char in no_break_chars else ' ' for char in main_string)
	return f' {sub} ' in cleaned_main_string





def positiveResultsCode(string,plus='',plusOr=False,end=None,OR=None):
	# __.sw.PlusCode

	string = string.replace("'",' ').replace('"',' ')
	global switches
	if switches.isActive('PlusCode') and 'n' in switches.value('PlusCode'):
		return positive_results_code(string,plus,plusOr,end,OR)
	if plusOr or switches.isActive('PlusOr'):
		plusOr = True

	if not OR is None:
		plusOr=OR
	if not plus == '':
		if type(plus) == str:
			plusInput = [plus]
		else:
			plusInput = plus
	else:
		plusInput = switches.values('Plus').copy()




	if type( plusInput ) == list:
		for i,yh in enumerate(plusInput):
			plusInput[i]= ci(plusInput[i])
	# -->   #end> this was added 2022-07-20

	if __.showLine_quoteFix and type(plusInput)==list:
		new=[]
		for i,x in enumerate(plusInput):
			if "'" in x:
				# new.append(x.replace("'",'"'))
				if not i and switches.isActive('Plus-single'):
					x=x.replace("'",'"')
			new.append(x)
		plusInput=new
	if not end is None:
		if type( plusInput ) == str:
			plusInput += end
		else:
			for i,yh in enumerate(plusInput):
				plusInput[i] += end
	StrictCase=switches.isActive('StrictCase')
	if not StrictCase:
		string=string.lower()
	pi = []
	for x in plusInput:
		if not StrictCase:
			pi.append( ci(x).lower() )
		else:
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
	if __.showLine_quoteFix and type(plusInput)==list:
		new=[]
		for i,x in enumerate(plusInput):
			if "'" in x:
				# new.append(x.replace("'",'"'))
				if not i and switches.isActive('Plus-single'):
					x=x.replace("'",'"')
			new.append(x)
		plusInput=new
	# print(plusInput);sys.exit();
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
		elif not plusOr:
			return False
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

def minusResults(string,minus='',itIs=False):
	result = True

	global switches
	if type(minus) == list:
		minusInput = minus
		# print('minus'); sys.exit()
	else:
		if not switches.isActive('StrictCase'):
			string = string.lower()
		result = True
		if not minus == '':
			minusInput = minus
		else:
			minusInput = switches.values('Minus')

	if itIs:
		for i,row in enumerate(minusInput):
			if not switches.isActive('StrictCase'):
				minusInput[i] = minusInput[i].lower()
			if string == minusInput[i]:
				return False
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
		#   if not switches.isActive('StrictCase'):
		#       _yh=ci(yh).lower()
		#   else:
		#       _yh=ci(yh)
		#   _minusInput.append( _yh )
		#   # minusInput[i]= ci(minusInput[i])
		# minusInput=_minusInput.copy()
		# del _minusInput
		#e)--> slow

		for i,yh in enumerate(minusInput):
			if not switches.isActive('StrictCase'):
				minusInput[i]= ci(minusInput[i]).lower()
			else:
				minusInput[i]= ci(minusInput[i])
	# -->   #end> this was added 2022-07-20
		if __.showLine_quoteFix and  type(minusInput)==list:
			new=[]
			for i,x in enumerate(minusInput):
				if "'" in x:
					# new.append(x.replace("'",'"'))
					if not i and switches.isActive('Minus-single'):
						x=x.replace("'",'"')
				new.append(x)
			minusInput=new
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
					return False
					result = False
					break
			elif len(s) > 1 and s[0] == '*':
				s = s.replace('*','')
				if string.endswith(s):
					return False
					result = False
					break
			elif len(s) > 1 and s[-1] == '*':
				s = s.replace('*','')
				if string.startswith(s):
					return False
					result = False
					break
			if not string.find(ci(s)) == -1 or s in string:
				return False
				result = False
				break
	except Exception as e:
		pass
	return result


def saveLog( logname, rows=[], focus=True, printThis=True ):
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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

def saveTable( rows, theFile, tableTemp=False, printThis=True, indentCode=True, sort_keys=False, archive=False,                k=0,s=0,tmp=None,here=None,h=None,    p=1, me=0, lock=False   ):
	if theFile == _v.tt+os.sep+'fileBackup.json': lock = True
	if theFile == _v.tt+os.sep+'fileBackupSchedule.json': lock = True
	HD.chmod(theFile)
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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
	if lock:
		FileLocker.check(file0)
		FileLocker.lock(file0)
	

	if __.print_path:
		print_(file0)
	try:
		if indentCode:
			dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
		else:
			dataDump = simplejson.dumps(rows, sort_keys=False, default=str)
	except Exception as e:
		try:
			if indentCode:
				dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
			else:
				dataDump = json.dumps(rows, sort_keys=False, default=str)
		except Exception as ee:
			pr('save json error',c='red')
			sys.exit()
			err('Unable to save json file',ee)
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
	if lock:
		FileLocker.unlock(file0)
	return file0

def getTable(theFile, tableTemp=False, isDic=None, isList=None, tmp=None):
	# print(theFile)
	if os.path.isfile(theFile):
		vv.opened_file_me[theFile] = os.path.getmtime(theFile)


	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson

	# Determine the file path
	file0 = _v.myTables + _v.slash + theFile
	if not isinstance(tableTemp, bool):
		if tableTemp == 'split':
			file0 = _v.myTables + _v.slash + 'tablesets' + _v.slash + theFile
	elif tableTemp:
		file0 = _v.stmp + _v.slash + theFile
	else:
		file0 = _v.myTables + _v.slash + theFile

	if not os.path.isfile(file0):
		file0 = theFile

	# Check if the file is empty
	if os.path.isfile(file0) and os.path.getsize(file0) > 0:
		try:
			with open(file0, 'r', encoding='utf-8') as json_file:
				try:
					json_data = simplejson.load(json_file)
				except Exception as e:
					json_data = json.load(json_file)
				return json_data
		except Exception as e:
			print('Error loading JSON file:', e)
			sys.exit()

	else:
		# print(f"File {file0} not found or is empty.")
		return __.data_default(file=theFile, default=[]).default()



def getTableOld( theFile, tableTemp=False,      isDic=None, isList=None,      tmp=None ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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
			try:
				json_data = simplejson.load(json_file)
			except Exception as ee:
				try:
					json_data = json.load(json_file)
				except Exception as eee:
					pr('get json error',c='red')
					sys.exit()
					err('Unable to load json',eee)
		return json_data
		# with open( file0, 'rb' ) as f:
			# json_data = bigjson.load(f)
			# json_data = bigjson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
	else:
		return __.data_default(file=theFile,default=[]).default()

def getTable3(theFile):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
	if os.path.isfile(theFile) == True:
		with open(theFile,'r') as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	return __.data_default(file=theFile,default=[]).default()


def getTable2(theFile, isDic=None, isList=None):
	if os.path.isfile(theFile):
		vv.opened_file_me[theFile] = os.path.getmtime(theFile)

	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson

	# Adjust for specific file extensions
	if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
		isDic = True

	# Check if the file exists and is not empty
	if os.path.isfile(theFile) and os.path.getsize(theFile) > 0:
		try:
			with open(theFile, 'r', encoding='utf-8') as json_file:
				try:
					json_data = simplejson.load(json_file)
				except Exception as e:
					json_data = json.load(json_file)
				return json_data
		except Exception as e:
			print('Error loading JSON file:', e)
			sys.exit()
	else:
		# print(f"File {theFile} not found or is empty.")
		return __.data_default(file=theFile, default=[]).default()



def getTable2Old( theFile,     isDic=None, isList=None ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
	if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
		isDic = True
	if os.path.isfile(theFile):
		with open(theFile,'r', encoding="latin-1") as json_file:
			try:
				json_data = simplejson.load(json_file)
			except Exception as e:
				try:
					json_data = json.load(json_file)
				except Exception as e:
					pr('get2 json error',c='red')
					sys.exit()
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()

def getTableBIG( theFile,     isDic=None, isList=None ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
	theFile = _v.dbTables + _v.slash + theFile
	# print(theFile)
	if os.path.isfile(theFile):
		if isTar.bz2(theFile) or isTar.gz(theFile):
			global _tar
			if _tar is None:
				import _rightThumb._tar as _tar
				_tar.unzip( theFile )


		with open(theFile,'r', encoding="utf-8") as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()


def getTableProject( project, theFile,     isDic=None, isList=None, path=False ):
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson

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
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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
	_v.mkdir(theFile,f=1)
	try:
		f = open(theFile,'w')
		f.write(str(dataDump))
		f.close()
		saved=True
	except Exception as e:
		saved=False
		# print_(e,c='red')
		# print_(theFile,c='red')
		# print_(type(rows),rows,c='purple')

	if os.path.isfile(theFile): HD.chmod(theFile)
	if printThis:
		if saved:
			print_('Saved: ' + theFile)
		else:
			print_('Not Saved: ' + theFile)
	if me and theFile in vv.opened_file_me: changeM( theFile, vv.opened_file_me[theFile] );

def saveTable3( rows, theFile, printThis=False, me=0 ):
	HD.chmod(theFile)
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		json = simplejson
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

		import uuid
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

printAutoAbbreviations_scheduled = False

##change
# from library.frameworks.base.classes.Switches import Switches
# from library.frameworks.base.classes.Tables import Tables


###########################################################################################


def md5Str(text: str) -> str:
	import hashlib
	return hashlib.md5(text.encode()).hexdigest()

def md5(fname):
	import hashlib
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()
	return hash_md5.hexdigest()

from library.frameworks.base.functions.formatSize import formatSize, unFormatSize, unFormatSize2, to_bytes

def count_bytes(fo, recursive=True):
	total_files = 0
	total_bytes = 0
	try:
		for entry in os.scandir(fo):
			if entry.is_file():
				total_files += 1
				total_bytes += entry.stat().st_size
			elif entry.is_dir() and recursive:
				sub_total_files, sub_total_bytes = count_bytes(entry.path)
				total_files += sub_total_files
				total_bytes += sub_total_bytes

	except Exception as e:
		pr(e,c='red')
	return total_files, total_bytes

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
		if not do.startswith('-') or not do.startswith('+'):
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
	if type(string) == float or type(string) == int: return True
	if not type(string) == str: return False
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



###########################################################################################

def Databases(*args, **kwargs):
	if not 'Database' in intelligent_code.functions:
		from library.frameworks.base.classes.Database import Databases
		intelligent_code.functions['Databases'] = Databases
	return intelligent_code.functions['Databases'](*args, **kwargs)

def Database(*args, **kwargs):
	if not 'Database' in intelligent_code.functions:
		from library.frameworks.base.classes.Database import Database
		intelligent_code.functions['Database'] = Database
	return intelligent_code.functions['Database'](*args, **kwargs)

def Database2(*args, **kwargs):
	if not 'Database2' in intelligent_code.functions:
		from library.frameworks.base.classes.Database2 import Database2
		intelligent_code.functions['Database2'] = Database2
	return intelligent_code.functions['Database2'](*args, **kwargs)

###########################################################################################




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
		[ ';sp',        ' '       ],
		[ '_;192A;_',   ','       ],
		[ '_;192B;_',   ':'       ],
		[ ';;',         ','       ],
		[ ';c',         ','       ],
		[ ';_',         '-'       ],
		[ ';-',         '-'       ],
		[ ';p;',        '%'       ],
		[ ';p',         '%'       ],
		[ ';.',         ':'       ],
		[ ";;'",        _v.slash+'"' ],
		[ _v.slash+'n', '\n'      ],
		[ ';n',         '\n'      ],
		[ ';return',    '\n'      ],
		[ ';t',         '\t'      ],
		[ ";'",         '"'       ],
		[ ';q;',        '"'       ],
		[ '"\'"',       "'"       ],
		[ ';sq',        "'"       ],
		[ 'null00',     '"",'     ],
		[ '"\'", "\'"', "','"      ],
		[ '[gg]',       '>>'       ],
		[ '[star]',     '*'       ],
		[ '[a]',        '*'       ],
		[ '[s]',        '$'       ],
		[ '[eq]',       '='       ],
		[ ';opar;',     '['       ],
		[ ';bkt0;',     '['       ],
		[ ';bkt1;',     ']'       ],
		[ '[pipe]',     '|'       ],
		[ '[p]',        '|'       ],
		[ '[htmlopen]', '<'       ],
		[ '[htmlclose]','>'       ],
		[ '[gtr]',      '>'       ],
		[ '[lss]',      '<'       ],
		[ ';6',         '^'       ],
		[ ';+',         '+'       ],
		[ '+--+c',      '--c'     ],
		[ '[semi]',     ';'       ],
		[ ';bs',        '/'       ],
		[ ';fs',        '\\'      ],
		[';d;',         __.theDelim ],
		[';delim;',     __.theDelim ],
		[';thedelim;',  __.theDelim ],
		[';theDelim;',  __.theDelim ],
		[';p',          '%'       ],
		[';js',         '//'      ],
		[';bs',         '/'       ],
		[';fs',         '\\'      ],
		[';t',          '\t'      ],
		['↔',           ' '       ],
		['--',          '-'       ],
		['[oo]',          '>>'       ],
		[';bk',         _v.myBackup ],
		[ '[caret]',    '^'       ],
		[ '[and]',      '&'       ],


 )
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
		#   columns = 'a:' + columns[2:]
		# if ',a.' in columns:
		#   columns = columns.replace( ',a.', ',a:' )

		# if columns.startswith('d.'):
		#   columns = 'd:' + columns[2:]
		# if ',d.' in columns:
		#   columns = columns.replace( ',d.', ',d:' )


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

def aliasesFo(fo):
	if 'aliasesFo' in __.setting('omit-functions', d=[]):
		return fo
	if os.path.isdir(fo): return fo
	import _rightThumb._bookmarks as _bm # type: ignore
	try:
		return _bm.Bookmarks( fo ).get()
	except: pass

	return fo

def aliasesFi(fi):
	if os.path.isfile(fi): return fi
	aliases=getTable('file-open-aliases.hash')
	if not 'aliases' in aliases: aliases['aliases']={}
	if not 'files' in aliases: aliases['files']={}
	if fi in aliases['aliases']:
		fi = aliases['aliases'][fi]
	return fi

def defaultScriptTriggers_do():
	global defaultScriptTriggers_run
	global default_switch_trigger_index
	for name in default_switch_trigger_index:
		switches.trigger(name,default_switch_trigger_index[name])

	if defaultScriptTriggers_run:
		if len(appInfo[__.appReg_bk]['columns']) > 0:
			if not 'Column' in __.setting('omit-switch-triggers',d=[]):
				switches.trigger('Column',formatColumns)
			if not 'Sort' in __.setting('omit-switch-triggers',d=[]):
				switches.trigger('Sort',formatColumnsSort)
			if not 'GroupBy' in __.setting('omit-switch-triggers',d=[]):
				switches.trigger('GroupBy',formatColumns)
			if not 'GroupTotals' in __.setting('omit-switch-triggers',d=[]):
				switches.trigger('GroupTotals',formatColumns)
		if not 'PlusClose' in __.setting('omit-switch-triggers',d=[]):
			switches.trigger('PlusClose',plusCloseClean)
		if not 'Ago' in __.setting('omit-switch-triggers',d=[]):
			switches.trigger('Ago',timeAgo)
		if not 'PrintEpoch' in __.setting('omit-switch-triggers',d=[]):
			switches.trigger('PrintEpoch',print_epoch_trigger)
		# switches.trigger('Aggregate',aggregate_trigger)
		##change
		# switches.postScripts.append( aggregate_trigger )



def autoAbbreviations():
	global printAutoAbbreviations_scheduled
	# return False
	global myFileLocation_File
	if not type( myFileLocation_File ) == bool:
		if not len( appInfo[__.appReg]['columns'] ) and myFileLocation_File.lower().endswith('.json'):

			printAutoAbbreviations_scheduled = True
			data = []
			groups = {}
			try:
				myFileLocation_File_Data = getTable2( myFileLocation_File )
			except:
				return None
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

def Threads(*args, **kwargs):
	if not 'Threads' in intelligent_code.functions:
		from library.frameworks.base.classes.Threads import Threads
		intelligent_code.functions['Threads'] = Threads
	return intelligent_code.functions['Threads'](*args, **kwargs)

def Queue(*args, **kwargs):
	if not 'Queue' in intelligent_code.functions:
		from library.frameworks.base.classes.Queue import Queue
		intelligent_code.functions['Queue'] = Queue
	return intelligent_code.functions['Queue'](*args, **kwargs)
#########################################################################################################################################################

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

def isNum( data, c=False ):
	if type( data ) == int:
		return True
	else:
		if not c: return False
		try:
			data=int(data)
			return True
		except: return False

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
class Fields:
	def __new__(cls, *args, **kwargs):
		if not 'Fields' in intelligent_code.classes:
			from library.frameworks.base.classes.Fields import Fields as live
			intelligent_code.classes['Fields'] = live
		return intelligent_code.classes['Fields'](*args, **kwargs)

# _.fields.register( 'project', 'name', script=_.resolveEpochTest )
# _.fields.asset( 'project', {} )
# _.fields.asset( 'project', [{}] )
# _.fields.register( 'project', 'name', value, appReg=focus() )
# _.fields.register( 'project', 'name', value )
# _.fields.value( 'project', 'name', value )
# fields=Fields()
###################################################################################################################





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
		if not __.setting('default-switches'): return None
	# if True
	
	##change
	global switches
	if switches is None:
		# from library.frameworks.base.classes.Switches import Switches
		switches = Switches()


	global switchDefault

	# global tables

	# switches.trigger('Column',formatColumns)

	switchDefault = switches.length()
	swGrp = 0
	swGrp += 1
	switches.register('Help', '?,??,/?,/??,-?,-??,--??,/h,/help,-help,--help', '(?? Print Table Help Without Global Switches) copy  OR ids  OR  12  OR  ?? x ', default=True, group=[swGrp,'Help'] )
	
	swGrp += 1
	switches.register('Plus', '+','all unless -or', default=True, group=[swGrp,'Search'] )
	switches.register('Minus', '-', default=True, group=[swGrp,'Search'] )
	switches.register('Plus-single', '+1', default=True, group=[swGrp,'Search'] )
	switches.register('Minus-single', '-1', default=True, group=[swGrp,'Search'] )
	switches.register('Plus-Sub', '++','any', default=True, group=[swGrp,'Search'] )
	switches.register('PlusOr', '-or', default=True, group=[swGrp,'Search'] )
	switches.register('PlusClose', '+close', '90%', default=True, group=[swGrp,'Search'] )
	switches.register('PlusCode', '+code','=  OR  *x  OR  x*  AND/OR color AND/OR n/new' , default=True, group=[swGrp,'Search'] )
	switches.register('PlusDuplicate', '+dup,+duplicate', '90%', default=True, group=[swGrp,'Search'] )
	switches.register('StrictCase', '-case,-strictcase,-strict', default=True, group=[swGrp,'Search'] )
	
	swGrp += 1
	switches.register('Column', '-c,-column', 'size, name', default=True, group=[swGrp,'Tables'] )
	switches.register('Sort','-s,-sort', 'a.type, d.ext', default=True, group=[swGrp,'Tables'] )
	switches.register('PrintAutoAbbreviations', '-printa,-aprint', default=True, group=[swGrp,'Tables Help'] )
	switches.register('TablePlus','t+,+t,-ts+,-st+,-tablesearch', 'Search_Sting', default=True, group=[swGrp,'Tables Seach'] )
	switches.register('TableMinus','t-,-t,-ts-,st-,-tableminus', 'Search_Sting', default=True, group=[swGrp,'Tables Seach'] )
	switches.register('GroupBy', '-g,-group,-groupby', 'ext, month', default=True, group=[swGrp,'Tables Reports'] )
	switches.register('GroupTotals', '-gt,-grouptotal,-gtotal,-gtotals', 'mem_usage', default=True, group=[swGrp,'Tables Reports'] )
	switches.register('Aggregate', '-aggregate', '" eof-field-len= add(len(version),len(backup)); config(var,eof,isFirst); "', default=True, group=[swGrp,'Tables Reports'] )
	switches.register('GroupSpaces', '-gs,-space,-groupspaces', default=True, group=[swGrp,'Tables Reports'] )
	switches.register('WrapTable', '-wrap', 'n p  OR  2  OR  path', default=True, group=[swGrp,'Tables Format'] )
	switches.register('NoWrapTable', '-nowrap', default=True, group=[swGrp,'Tables Format'] )
	switches.register('TableProfile', '-tp,-table',' *;c *;l  h;l header;left  size;l,gs', default=True, group=[swGrp,'Tables Format'] )
	switches.register('Long', '-long', default=True, group=[swGrp,'Tables Format'] )
	switches.register('Short', '-sc,-short', default=True, group=[swGrp,'Tables Format'] )
	switches.register('Length', '-length','x3', default=True, group=[swGrp,'Tables Format'] )
	# switches.register('ShortenColumn', '-sc,-shortencolumn', default=True, group=[swGrp,'Tables'] )
	# switches.register('SkipColumnTriggers', '-skiptriggers', default=True, group=[swGrp,'Tables'] )
	swGrp += 1
	switches.register('Debug', '-debug', default=True, group=[swGrp,'Debug'] )
	switches.register('DumpSwitches', '-dump', 'all', default=True, group=[swGrp,'Debug'] )
	switches.register('Errors', '-Error,-Errors', '8,11 OR hide:8,11', default=True, group=[swGrp,'Debug'] )
	switches.register('Timeout', '-t,-Timeout', default=True, group=[swGrp,'Debug'] )
	switches.register('chmod', '-chmod,-777', default=True, group=[swGrp,'Debug'] )
	swGrp += 1
	# switches.register('NoTableLines', '-nolines', default=True, group=[swGrp,'A_Group'] )
	switches.register('YesTableLines', '-yl,-yeslines', default=True, group=[swGrp,'Output'] )
	switches.register('TableJSON', '-tjson,-tablejson', default=True, group=[swGrp,'Output'] )
	switches.register('FieldTotal', '-fieldtotal', 'mem_usage', default=True, group=[swGrp,'Output'] )
	switches.register('NoColor', '-nocolor', space=True, default=True, group=[swGrp,'Output'] )
	switches.register('NoTitleChange', '-ntc,-notitlechange', default=True, group=[swGrp,'Output'] )
	switches.register( 'Paste-isData', '--pa,--paste,-ppa,-ppaste,-ispa,-idpa' , default=True, group=[swGrp,'Output'] )
	switches.register( 'Paste-isData-json', '--json,-pjson,-jsonp' , default=True, group=[swGrp,'Output'] )
	switches.register( 'Markdown-Table', '--md' , default=True, group=[swGrp,'Output'] )
	# switches.register('Report', '-report', default=True, group=[swGrp,'Output'] )
	swGrp += 1
	switches.register( 'SavePrint', '--savePrint' , default=True, group=[swGrp,'Script Helper'] )
	switches.register( 'CopyPrint', '--copyPrint' , default=True, group=[swGrp,'Script Helper'] )


	swGrp += 1
	switches.register('LoadEpoch', '-loadepoch', default=True, group=[swGrp,'Rebuild From Logs'] )
	switches.register('PrintEpoch', '-printepoch', default=True, group=[swGrp,'Rebuild From Logs'] )

	defaultScriptTriggers_do()




##############################
regImps = {}
def regImp(*args, **kwargs):
	if not 'regImp' in intelligent_code.functions:
		from library.frameworks.base.classes.regImp import regImp
		intelligent_code.functions['regImp'] = regImp
	return intelligent_code.functions['regImp'](*args, **kwargs)
impReg=regImp
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


def err( msg='STOP' , e=None, note=None, kill=True, bulletDash=False, dash=None):
	if not dash is None:
		bulletDash = dash

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
		add='  \t    '
		if type(e) == str:
			cp( [add,e], 'cyan' )
		else:
			add+='- '
			for x in e:
				cp( [add,x], 'cyan' )
	# if not note is None and type(note) == str:

	if not note is None and type(note) == list:
		for n in note:
			if bulletDash:
				cp( ['  \t\t   -',n], 'cyan' )
			else:
				cp( ['  \t\t   ',n], 'cyan' )

	elif not note is None and type(note) == str:
		if bulletDash:
			cp( ['  \t\t   -',note], 'cyan' )
		else:
			cp( ['  \t\t   ',note], 'cyan' )

	# if not note is None:
		# cp( ['  \t\t\t',note], 'cyan' )

	# cp( '**********************************************************************', 'red', isError=True )
	# linePrint()
	cp( linePrint(txt='*',p=0), 'red' )
	if kill:
		sys.exit()
	# △ ▽


def key( subject ):
	try:
		table = getTableDB( 'secureStrings.hash' )
		return table[subject]
	except Exception as ee:
		err( 'secureString', ee )



def historyPrint( code, pre='' ):
	##change
	global switches
	if switches is None:
		# from library.frameworks.base.classes.Switches import Switches
		switches = Switches()
	i=0
	while not i >= 4:
		i+=1
		# code = _str.cleanBE(code, '\n')
		# code = _str.cleanBE(code, ' ')
		# code = _str.cleanBE(code, '\t')

	if switches.isActive('DoNotColorize'):
		return code
	result = ''

	colors = {
				'cmd': 'blue',
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
		if ( x.startswith('=') and len(x) > 1 ) or x.startswith('`') or x.startswith('||') or x.lower() == 'p' or x.lower() == 'p' or x.lower() == '%py%' or x.lower() == 'pp' or x.lower() == 'python' or x.lower() == 'python.exe' or x.lower().endswith('python.exe'):
			lastP = True
			
			if x.startswith('`') and x.endswith('`'):
				x = x.replace('`','')
				result += '`'+colorThis( x, colors['cmd'], p=0 )+'`'
			elif x.startswith('`'):
				x = x.replace('`','')
				result += '`'+colorThis( x, colors['cmd'], p=0 )
			elif x.startswith('||'):
				x = x.replace('||','')
				result += colorThis( x, colors['cmd'], p=0 )
			elif x.startswith('='):
				x = x.replace('=','')
				result += colorThis( x, colors['cmd'], p=0 )
			else:
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


dict_generator_separator='print'
dict_generator_spent=[]
dict_generator_index={}
def dict_generator(indict, pre=None, fields=[] ):
	global dict_generator_spent
	global dict_generator_index
	global dict_generator_separator
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
							if dict_generator_separator == 'print':
								print_()
							else:
								linePrint()
							# print_()
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
	import random
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
	import requests
	url='https://eyeformeta.com/apps/ids/?subject=live-'+subject
	page = requests.get(url).content.decode("utf-8").replace('\\n','\n').replace('\n','').replace('\r','').replace(' ','').replace('\t','')
	return page


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
	import random
	ads=fo(_v.life+'apps')
	ri = random.randrange(len(ads))
	cho=ads[ri]
	ic=list('🧻🧪💀🦆🦉🥓🦄🦀🖕🍣🍤🍥🍡🥃🥞🐕👾🐉🐓🐋🐌🐢👽👿🥑🐡🐗💐🏹🎨🐔🐛🎯🌯📷🛶🥕🍸🍳🐲🎣🐟🦅👀🐸🤞💪💾👻🐊🍔🌭🍀🕓🦊🍟🥝🐒🥞🐼📎🐧💩🍕🍍🦏🍗🌈🐳🦑🚀🙈🙊🙉🌮🐅🐯🍉🚽🍅👅🎩🍷')
	for x in ic:
		print(x)


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
	if not __.isRequired_or_List:
		__.isRequired_or_List = __.setting('require-list')
def l_registerSwitches( trig=None, sw=None ):
	global appInfo
	global argvProcess
	global myFileLocation_Print
	global autoBackupData
	# __.appInfoAcquiredData = { 'app': __.appReg, 'focus': theFocus, 'data': data }
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
			setPipeData( sys.stdin.readlines(), __.appReg, clean=l.conf('clean-pipe' ,d=True) )
	postLoad( l.conf('__file__') )
	myFileLocation_Print=l.conf('myFileLocation_Print',d=False)
	if appInfo[__.appReg]['file'] == 'thisApp.py':
		appInfo[__.appReg]['file'] =appInfo[__.appReg]['liveAppName']
l=dot()
l.v=dot()
l.sw=dot()
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
	if not os.path.isdir(_v.ads): return None
	global SHOW_ADS
	if not SHOW_ADS: return None
	global MINI_ADS
	global ads
	ads = []

	def add_ad_fo(ad_fo):
		global ads
		for a2 in fo(_v.ads+ad_fo): ads.append(a2);

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
		import random
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

# def URL(url):
# 	requests=dots('requests.get')
# 	return requests.get(url).content.decode("utf-8").replace('\\n','\n')
def URL(url, data={}):
	import requests
	response = requests.post(url, data=data)
	return response.content.decode("utf-8").replace('\\n', '\n')

def getConfig(path):
	def _cl_(string): return _str.do('be',   _str.do('be',string,'\n')   ,' ');
	def _val_(string):
		if string.startswith('"'): string=string[1:]; string=string[:-1]; return _cl_(string);
		if string.startswith("'"): string=string[1:]; string=string[:-1]; return _cl_(string);
		if string.startswith('[') or string.startswith('{'):
			try:
				import simplejson
				json = simplejson
			except:
				pass
			try:
				import json
			except ImportError:
				json = simplejson
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
			try:
				import simplejson
				json = simplejson
			except:
				pass
			try:
				import json
			except ImportError:
				json = simplejson
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
	appDBA = __.appInfoAcquiredData['app']
	theFocus = __.appInfoAcquiredData['focus']
	data = __.appInfoAcquiredData['data']
	releaseAcquiredData( appDBA, theFocus, data )
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


def pipe_surfing(data=None):
	global appData
	for app in appData:
		if 'pipe'  in appData[app] and appData[app]['pipe']:
			if not data is None: appData[app]['pipe']=data
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

def fromYML(text): return __.fromYML(text)
def toYML(dic,path=None): return __.toYML(dic,path)

def getYML(path,here=False,h=None,auto=True,a=None,t=False):
	if not a is None: auto=a
	if not h is None: here=h
	if here: auto = False
	if not auto: here=True
	loaded=False
	import yaml
	os = __.imp('os.path.isfile')
	if t: path=_v.tt+os.sep+path
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
	import yaml
	os = __.imp('os.sep')
	y=yaml.dump( data, sort_keys=False )
	if not here and not os.sep in path:
		path = _v.myTables + _v.slash + path
	saveText(y,path)

def saveYML2(data,path): return saveYML(data,path,here=True)
def getYML2(path): return getYML(path,here=True)

# class auditor:
#   def __init__(self, label='default'):
#       time=__.imp('time.time')
#       self.label = label
#       self.epoch=time.time()
#   def stamp( location='default', line=None,    l=None ):
#       if not l is None: line=l





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

def pipepipe():
	return [line.strip() for line in sys.stdin]
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
#       off='b9e086cad1834395a9aae81d869fd17b'
#       off='b9e086cad1834395'
#       off='b9e086ca'
#       # string1=off+string1
#       # string2=off+string2
#       def _chr_(n):
#               r=''; i=0;
#               while not i==n: i+=1; r+='*';
#               return r
#       def pattern_length_offset(off,xstring1,xstring2):
#               def pldiff(str1,str2):
#                       l1=len(str1)
#                       l2=len(str2)
#                       ll1=l1
#                       ll2=l2
#                       if l2 < l1:
#                               ll1=l2
#                               ll2=l1
#                       plen=round(percentageDiff(ll1,ll2),3)
#                       diff=ll2-ll1
#                       return diff,plen
#               d,p=pldiff(xstring1,xstring2)
#               # print(d,p)
#               d,p=pldiff(off,off+_chr_(d))
#               # print(d,p)
#               return p


#       def function_name(_string1_,_string2_):
#               y={}
#               y['s1']=patternz(_string1_)
#               y['s2']=patternz(_string2_)

#               common = list(set(y['s1']) & set(y['s2']))

#               plen=percentageDiffInt(len(_string1_),len(_string2_))


#               p1=percentageDiff(len(common),len(y['s1']))
#               p2=percentageDiff(len(common),len(y['s2']))
#               p0=p1
#               if p2 < p1: p0=p2

#               y['1s']=_string1_
#               y['2s']=_string2_
#               y['ptn1']=str(y['s1'])
#               y['ptn2']=str(y['s2'])
#               y['ptn_len1']=len(y['s1'])
#               y['ptn_len2']=len(y['s2'])
#               y['tcommon']=len(common)
#               y['common']=str(common)


#               len1=len(_string1_)
#               len2=len(_string2_)
#               len0=len1
#               if len2 < len1: len0=len2
#               y['len1']=len1
#               y['len2']=len2
#               y['len0']=len0

#               y['%len']=plen
#               # y['weight']=
#               # y['offsetted']=
#               y['%1']=round(p1,3)
#               y['%2']=round(p2,3)
#               y['%0']=round(p0,3)
#               return y

#       def sequential(s1,s2):
#           # print('s1,s2',s1,s2)
#           seq={}
#           _range=6
#           mx=-10
#           for i,p in enumerate( s2 ):
#               found=False
#               for j in range(-2,_range):
#                   if i+j >mx:
#                       try:
#                           if not found and s2[i]==s1[i+j]:
#                               mx=i+j
#                           # print(s2[i],s1[i+j])
#                           # if s2[i]==s1[i+j]:
#                               # print(99)
#                               if not j in seq:
#                                   if j==0: default=False
#                                   else: default=False
#                                   seq[j]={'cnt':0,'last': default}
#                               if seq[j]['last']:
#                                   seq[j]['cnt']+=1

#                                   try:
#                                       if not s2[i+1]==s1[i+j+1]:
#                                           # print(i,j,s2[i],'1-here')
#                                           seq[j]['cnt']+=1
#                                   except:
#                                       # print(i,j,s2[i+1],'2-here',8)
#                                       # print(i,j,'2-here',8)
#                                       seq[j]['cnt']+=1
#                               seq[j]['last']=True
#                               # print(j)

#                           # else:
#                           #   if j in seq: seq[j]['last']=False
#                       except:
#                           pass
#                           # if j in seq: seq[j]['last']=False
#           seq['max']=0
#           for j in range(-2,_range):
#           #   if j in seq and seq[j]['last']: seq[j]['cnt']+=1
#               if j in seq:
#                   seq['max']+=seq[j]['cnt']

#           if s1[0] == s2[0] and not s1[1] == s2[1]: seq['max']+=1
#           # pv(seq)
#           # pr(s1,s2,c='Background.red')
#           # pr(seq['max'],c='red')
#           # sys.exit()
#           fx=[len(s1),len(s2)]
#           fx.sort()
#           # if fx[0]<seq['max']: seq['max']=fx[0]
#           return seq['max']



#       d = function_name(string1,string2)

#       _min=8
#       d['%lenoff']=pattern_length_offset( _chr_(_min) ,string1,string2)
#       if d['%lenoff'] > d['%len']:
#               d['offset'] = round(d['%lenoff']-d['%len'],3)
#       else:
#               d['offset']=0

#       d['%off']=d['%0']+d['offset']


#       # ↓ THERE ARE 2 WAYS OF DOING THIS ↓

#       # ↓ by charecter ↓
#       # _seq1=sequential(string1,string2)
#       # _seq2=sequential(string2,string1)

#       # ↓ by pattern ↓
#       _seq1=sequential(d['s1'],d['s2'])
#       _seq2=sequential(d['s2'],d['s1'])

#       # ↑ THERE ARE 2 WAYS OF DOING THIS ↑

#       _seqL=[_seq1,_seq2]
#       _seqL.sort()
#       # print('_seqL:',_seqL)
#       d['seq']=_seqL[-1]
#       if d['seq'] > d['len0']: d['seq'] = _seqL[0]
#       d['seq_weight']=round(percentageDiff(d['seq'],d['len0']),3)
#       # pr(d['seq'],d['len0'],c='purple')
#       seq=d['seq']

#       # pv(d)

#       weighted = {}
#       # weighted['vVv']=d['vVv']
#       weighted['1s']=d['1s']
#       weighted['2s']=d['2s']
#       weighted['%0']=d['%0']
#       weighted['offset']=d['offset']
#       weighted['%off']=d['%off']
#       weighted['len0']=d['len0']
#       weighted['seq']=d['seq']
#       weighted['seq_weight']=d['seq_weight']
#       weighted['seq_offset']=round(percentageDiff(d['seq']+3,d['len0']+3)-d['seq_weight'],3)
#       weighted['seq_weight_offsetted']=round(weighted['seq_weight']+weighted['seq_offset'],2)
#       # return weighted



#       if weighted['seq_weight_offsetted'] > 99 and not string1 == string2: weighted['seq_weight_offsetted']=99
#       if weighted['seq_weight'] > 99 and not string1 == string2: weighted['seq_weight']=99

#       if w: return weighted['seq_weight_offsetted']
#       return weighted['seq_weight']




def pattern_probability(string1,string2,w=False):
		if string1==string2: return 100
		off='b9e086cad1834395a9aae81d869fd17b'
		off='b9e086cad1834395'
		off='b9e086ca'
		# string1=off+string1
		# string2=off+string2

		def _chr_(n):
				r=''; i=0;
				while not i==n: i+=1; r+='*';
				return r

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
							#   if j in seq: seq[j]['last']=False
						except:
							pass
							# if j in seq: seq[j]['last']=False
			seq['max']=0
			for j in range(-2,_range):
			#   if j in seq and seq[j]['last']: seq[j]['cnt']+=1
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
		weighted['len']=d['len0']
		weighted['seq']=d['seq']
		weighted['seq_weight']=d['seq_weight']
		weighted['seq_offset']=round(percentageDiff(d['seq']+3,d['len0']+3)-d['seq_weight'],3)
		weighted['seq_weight_offsetted']=round(weighted['seq_weight']+weighted['seq_offset'],2)
		# return weighted



		if weighted['seq_weight_offsetted'] > 99 and not string1 == string2: weighted['seq_weight_offsetted']=99
		if weighted['seq_weight'] > 99 and not string1 == string2: weighted['seq_weight']=99

		if w: return weighted['seq_weight_offsetted']
		return weighted['seq_weight']





def pattern_probability_list_best(_str,_list,clean=None,omit=[],i=0):
	# a.playlist playlist.txt Metallica
	#   type %1 | call p youtubeSearch -official -song -band %2 | p youtube
	#   type %1 | p prefix-file-number-by-patterns -f *.mp3 -omit %2

	_i_=i
	_str_=_str
	_str=_str.replace('’',"'")
	_str=_str.lower()
	def _sp_(txt):
		while '  ' in txt: txt=txt.replace('  ',' ')
		txt=txt.strip()
		return txt
	def _omit_(txt):
		for o in omit:
			o=o.lower()
			if o in txt.lower():
				i=txt.lower().index(o)
				txt=txt[0:i]+txt[i+len(o)+1:]
		txt=_sp_(txt)
		return txt


	def _clean_(li,clean):
		def _cl2_(xt):
			tx=''
			for c in xt:
				if c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'+"'":
					tx+=c
				else:
					tx+=' '
			return _sp_(tx)
		li=_omit_(li)
		if clean is None: return li
		if type(clean) == str and 'file' in clean:
			if '.' in li and len(li.split('.')[-1]) < 6:
				cli=li.split('.')
				cli.pop(-1)
				li='.'.join(cli)
		sub='()'
		while sub[0] in li and sub[1] in li: li = li[0:li.index(sub[0])]+li[li.index(sub[1])+1:]
		sub='[]'
		while sub[0] in li and sub[1] in li: li = li[0:li.index(sub[0])]+li[li.index(sub[1])+1:]
		# li=_sp_(li)
		li=_cl2_(li)
		return li
	_str=_clean_(_str,clean)
	results=[]
	for li in _list:
		li=li.replace('’',"'")
		li=li.lower()
		lic=_clean_(li,clean)
		probability=pattern_probability(_str,lic)
		probability=pattern_probability(_str,lic)
		w_probability=pattern_probability(_str,li.lower(),w=True)
		results.append({'i': _i_, 'p':probability, 'wp': w_probability, 'str':_str_, 'lic':lic, 'li':li })
		# print(probability,w_probability)
	results = tables.returnSorted( 'data', 'd.p', results )
	# pt(results)
	# sys.exit()
	return results[0]
	return results[0]['li'],results[0]['p'],results[0]['lic']

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


def afile(line,path,first=None,   f=None):
	if not f is None: first=f
	ifile=os.path.isfile(path)
	f = open(path, "a")
	if not first is None and not ifile: f.write(str(first)+'\n')
	f.write(str(line)+'\n')
	f.close()

def replace_line_in_file(file_path, search_string, replace_string):
	# https://chat.openai.com/chat
	with open(file_path, 'r') as file:
		lines = file.readlines()

	with open(file_path, 'w') as file:
		for line in lines:
			if search_string in line:
				line = replace_string + '\n'
			file.write(line)

def replace_lines_in_file(file_path, lst):
	# https://chat.openai.com/chat
	with open(file_path, 'r') as file:
		lines = file.readlines()

	with open(file_path, 'w') as file:
		for line in lines:
			for item in lst:
				search_string  = item[0]
				replace_string = item[1]
				if search_string in line:
					line = replace_string + '\n'
			file.write(line)

def appAPI(app='_admin_',api=None):
	if not api is None:
		APIs = getTable('app-APIs.index')
		APIs[app]=api
		saveTable(APIs,'app-APIs.index',p=0)
		# print(api)
		return api
	api='2728aff2b84de76828b1db566850722a40dcee4e'
	APIs = getTable('app-APIs.index')
	if app in APIs: api = APIs[app]
	# print(api)
	return api

def secureURL(url,app='_admin_',data={},headers={},showError=True,inject=False):
	test=True
	test=False
	requests=__.imp('requests.post')
	_data=data
	_headers=headers

	machine = {
				'app': app,
				'machine': _v.getMachineID(),
				'node': _v.computername,
				'user': _v.user,
	}
	if inject:
		for k in machine: data[k]=machine[k]

	if not 'User-Agent' in headers: headers['User-Agent'] = 'Mozilla/5.0'
	if not 'API' in headers and not 'APP-API-KEY' in headers:
		headers['API'] = appAPI(app)
		headers['APP-API-KEY'] = appAPI(app)
	elif not 'API' in headers:
		headers['API'] = headers['APP-API-KEY']
	elif not 'APP-API-KEY' in headers:
		headers['APP-API-KEY'] = headers['API']


	if not 'APP' in headers: headers['APP'] = app
	# pv(headers)
	# pv(data)
	page=str(requests.post(url, headers=headers, data = data ).content,'iso-8859-1')
	if test: print('page:',page)

	if not '!!REQUEST!!' in page: return page
	# if not 'ACCESS EXPIRED' in page: e(app,page)

	headers = {
		'User-Agent': 'Mozilla/5.0',
		# 'API': '789d6ecbfe23e2c29d64ca0912ea1d2552820b84',
	}

	phone = input('Phone: ')
	_scan = regImp( __.appReg, 'record-cleaner' )
	scan=_scan.imp.app.scan.process( phone, 'A02F28B2' )
	if 'phone' in scan: phone=scan['phone'][0]
	# print('phone:',phone)
	data=machine
	data['phone']=phone


	page=str(requests.post(url, headers=headers, data = data ).content,'iso-8859-1')
	if test:
		pv(headers)
		pv(data)
		print('page:',page)

	if page.startswith('??') and page.endswith('??'):
		uuid=page[2:-2]
		pin = input('pin?: ')
		page=str(requests.post(url, headers=headers, data = {
				'pin': pin,
				'id': uuid,
			} ).content,'iso-8859-1')
		if test: print('page:',page)
		if len(page) == 40:
			appAPI(app,page)
			_headers['APP-API-KEY'] = page
			_headers['API'] = page
			return secureURL(url,app,_data,_headers)
		if showError:
			e('pin',page)
		return None
	else:
		if showError:
			e('pre-pin',page)
		return None

##################################################
def _secure_files_():
	def _VIEW_(table):
		# global dirs
		# global good
		# global errors
		dirs=[]
		good=[]
		errors=[]
		for i,path in enumerate( table ):
			if os.path.isdir(path): dirs.append(path)
			if os.path.isfile(path): good.append(path)
			else:  errors.append(path)
		return good
	a=_VIEW_(  getTable('crypt-docs.list')  )
	b=_VIEW_(  getTable('secure-crypt-local.meta')  )
	return a + b
def sort(table,s=None):
	if not len(table): return table
	if type(table[0]) == dict and not s is None: return tables.returnSorted( 'algorithm', s, table )
	if type(table[0]) == dict:
		s=list(table[0].keys())[0]
		return tables.returnSorted( 'algorithm', s, table )
	table.sort()
	return table

##################################################
def columnAbbreviations(data,appReg=None):
	global appInfo
	if appReg is None: appReg = __.appReg
	if data:
		abbrev=[]
		abbr={}
		for k in data[0]:
			ks=k.strip()
			kk=ks.replace(' ','_')
			kl=kk.lower()
			if '_' in kk:
				aa=''
				for i,w in enumerate(kl.split('_')): aa+=w[0]

				if aa in abbrev:
					aa=''
					for i,w in enumerate(kl.split('_')):
						if w:
							if i == 0:
								aa+=w[0]+w[1]
							else:
								aa+=w[0]
					if aa in abbrev:
						aa=''
						for i,w in enumerate(kl.split('_')):
							if w:
								aa+=w[0]+w[1]
						if aa in abbrev:
							aa=''
							for i,w in enumerate(kl.split('_')):
								aa+=w[0]+w[1]+w[2]
				if not aa in abbrev and aa:
					abbrev.append(aa)
					if not k in abbr: abbr[k]=[]
					abbr[k].append(aa)
			else:
				aa=kl[0]
				if aa in abbrev:
					aa=''
					for c in kl:
						if aa in abbrev:
							aa+=c
						else: break




				if not aa in abbrev and aa:
					abbrev.append(aa)
					if not k in abbr: abbr[k]=[]
					abbr[k].append(aa)
		for k in data[0]:
			ks=k.strip()
			kl=ks.lower()
			if not kl[0] in abbrev and kl[0]:
				abbrev.append(kl[0])
				if not k in abbr: abbr[k]=[]
				abbr[k].append(kl[0])
			# if not k in abbr: _.e(k,abbr)
			if k in abbr:
				appInfo[appReg]['columns'].append({'name': k, 'abbreviation': ','.join(abbr[k])})
##################################################
# path=_.zZip(path);   _.cleanUnzip()

def IS(path,check=1):
	if not os.path.isfile(path): return False
	global isHeaders
	if check in isHeaders.keys():
		check = isHeaders[check]
	header=" ".join(['{:02X}'.format(byte) for byte in     open( path, 'rb' ).read(32)    ])
	if check == 1: return header
	if type(check) == str:
		if header.startswith(check): return True
	elif type(check) == list:
		for c in check:
			if header.startswith(c): return True

	return False


def isZip(path):
	if not os.path.isfile(path): return False
	if path.endswith('.docx'): return False
	if IS(path,'50 4B 03 04'): return True
	if IS(path,'50 4B 05 06'): return True
	else: return False

def ZIP( a, b=None, d=None, p=1 ):
	if isZip(a): unzip_file(a,b)
	else: return zip_file(a,b,d,p)

def zip_file(input_file, output_zip=None, d=None, p=1):
	import zipfile
	if output_zip is None or not output_zip: output_zip = input_file+'.zip'
	zip9(input_file,output_zip)
	if not d is None and d:
		if not input_file == output_zip:
			os.unlink(input_file)
			if p: pr('Deleted',c='red')
	return output_zip


def unzip_file(zip_file, output_file=None):
	if not isZip(zip_file): return zip_file
	zip_file=__.path(zip_file)
	extracted_file_path = None
	output_folder=None
	import zipfile
	with zipfile.ZipFile(zip_file, 'r') as zipf:
		if len(zipf.namelist()) == 1:
			file_to_extract = zipf.namelist()[0]
			if output_folder is None:
				output_folder = os.path.dirname(zip_file)
			extracted_file_path = os.path.join(output_folder, file_to_extract)
			if os.path.isfile(extracted_file_path): toTMP(extracted_file_path)
			zipf.extract(file_to_extract, output_folder)
		else:
			return unzip_files(zip_file, output_file=output_file)

	return extracted_file_path



def unzip_files(zip_file, output_file=None):
	if not isZip(zip_file): return zip_file
	import zipfile
	if output_file is None:
		if zip_file.endswith('.zip'):
			output_file = zip_file[:-len('.zip')]
		else:
			output_file = zip_file+'.unzip'
	if os.path.isfile(output_file): toTMP(output_file)
	with zipfile.ZipFile(zip_file, 'r') as zipf:
		zipf.extractall(output_file)
	return output_file
foundZip=[]
def zZip(path):
	if '.' in path and path.lower().split('.')[-1] in ['xls','xlsx','doc','docx']: return path
	# maybe a zip
	if isZip(path):
		global foundZip
		path0=path
		path=unzip_file(path)
		if not path0 == path:
			foundZip.append(path)
	return path

def cleanUnzip():
	# after maybe a zip
	global foundZip
	if foundZip:
		time.sleep(.5)
		for path in foundZip: toTMP(path)

def toTMP(path):
	import shutil
	import _rightThumb._dir as _dir
	zFo=_v.stmp+os.sep+'unzipped'+os.sep
	_v.mkdir(zFo)
	tmp=zFo+os.sep+str(mod(path))+'___'+_dir.info(path,k='name')
	shutil.move(path, tmp )
	# pr(tmp,c='red')

# path=_.zZip(path);   _.cleanUnzip()
##################################################
def encrypt(path,ext=True): enFi(path,ext=True)
def decrypt(path,ext=True): deFi(path,ext=True)



##################################################
def enFi(path,ext=True):
	# print('enFi',isCrypt(path))
	if os.path.isfile(path) and not isCrypt(path):
		# print('enFi')
		_cryptFile = regImp( __.appReg, 'cryptFile' )
		_cryptFile.switch( 'Decrypt', delete=True )
		if ext: _cryptFile.switch( 'NoExt',delete=True )
		else:   _cryptFile.switch( 'NoExt' )
		_cryptFile.switch( 'Clean' )
		_cryptFile.switch( 'Encrypt' )
		_cryptFile.switch( 'Files', path )
		_cryptFile.do( 'action' )
def deFi(path,ext=True):
	# print('deFi',isCrypt(path))
	if os.path.isfile(path) and isCrypt(path):
		# print('deFi')
		_cryptFile = regImp( __.appReg, 'cryptFile' )
		_cryptFile.switch( 'Decrypt' )
		if ext: _cryptFile.switch( 'NoExt',delete=True )
		else:   _cryptFile.switch( 'NoExt' )
		_cryptFile.switch( 'Clean' )
		_cryptFile.switch( 'Encrypt', delete=True )
		_cryptFile.switch( 'Files', path )
		_cryptFile.do( 'action' )
##################################################
crypt_header = b'AES_ENCRYPTED_4a2e'
def has_crypt_header(file_path):
	global crypt_header
	with open(file_path, 'rb') as file:
		file_header = file.read(len(crypt_header))
	return file_header == crypt_header
##################################################
def password_filter( cmd ):
	scan = '-password -pass -pw -en -de -key -crypt -p'.split(' ')
	for test in scan:
		if test in cmd.lower():
			parts = cmd.split(' ')
			isNext = False
			newCMD = []
			for part in parts:
				if isNext: part = '*****'
				if part in scan: isNext = True
				newCMD.append( part )
				if isNext and part == '*****': isNext = False
			cmd = ' '.join( newCMD )
	return cmd
def mask_password(data):
	for item in data:
		if isinstance(item, dict) and item.get("name") == "Password":
			item["value"] = '******'
			item["values"] = ['******']
	return data
##################################################
def getTextFirst(file_path):
	try:
		with open(file_path, 'r') as file:
			first_char = file.read(1)  # Read the first character
			return first_char
	except FileNotFoundError:
		print(f"File '{file_path}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")
##################################################
def query(db_path, query, params=()):
	"""
	Query an SQLite database and return the results.

	Args:
		db_path: Path to the SQLite database file.
		query: SQL query to execute.
		params: Parameters to use in the SQL query (optional).

	Returns:
		List of tuples representing the query results.
	"""
	import sqlite3
	# Connect to the SQLite database
	conn = sqlite3.connect(db_path)

	# Create a cursor object to execute queries
	cursor = conn.cursor()

	# Execute the query
	cursor.execute(query, params)

	# Fetch all the results
	results = cursor.fetchall()

	# Close the cursor and connection
	cursor.close()
	conn.close()

	return results

# conn = sqlite3.connect("example.db")
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 35))
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
# conn.commit()
# cursor.close()
# conn.close()

# data = _.query("example.db", "SELECT * FROM users WHERE age > ?", (27,))

##################################################
def sortFo(file_paths):
	return sorted(file_paths, key=lambda path: (path.count('/'), path.count(os.sep), path.count('/' + os.sep)))
def sortFo2(file_paths):
	return sorted(file_paths, key=lambda path: tuple(int(s) if s.isdigit() else s for s in path.split(os.sep)))

##################################################
fields = Fields()
##change
switches = None
# switches = Switches()
# tables = Tables()
# tables = TableSystem()
# __.onExit(tables.eof)
# databases = Databases()
# __.databases = Databases()

##################################################
errors = []
appInfo = {}
appData = {}
argvProcess = True
##################################################

server_proxy = []
server_proxy.append( '' )
server_proxy.append( 'http://www.rightthumb.com/projects/widget/proxy.php?p=' )
server_proxy.append( 'http://rephrecruiting.com/proxy.php?p=' )
server_proxy.append( 'http://www.pillerbeauty.com/proxy.php?p=' )
server_proxy.append( 'http://signaturemassageandfacialspa.com/p.php?p=' )
server_proxy.append( 'https://signaturemassagetampa.com/payroll/p.php?p=' )

##################################################
nsfw=True

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

hp = historyPrint
ph = historyPrint
e=err
colorPrint=colorThis
cp=colorThis
pv=printVarSimple
vp=printVarSimple
pvs=printVarSimple
ppv=printVarColor
ppvv=printVarColor
pvv=printVarColor
pvpv=printVarColor

aib=aiBullet
ail=aiLine
bu=aiBullet
bull=aiBullet
lbu=aiLine
nw=n2w
prLine=linePrint
pr=print_
prDic=printDicFields
prStatus = True
ct=colorThis
cr=colorizeRow
c=colorizeRow
prt=printt
pt=printt
getYAML2=getYML2
getYAML=getYML
saveYAML=saveYML
saveYAML2=saveYML2
imp=regImp
ago=timeAgo
toBytes=to_bytes
yt=toYML
yf=fromYML
##################################################
def isTextFi(path, num_chars=20):
	with open(path, 'rb') as file:
		content = file.read(num_chars)
		try:
			content.decode('utf-8')
			return True
		except UnicodeDecodeError:
			return False
def isTextFiGet(path, num_chars=20):
	with open(path, 'rb') as file:
		content = file.read(num_chars)
		try:
			return content.decode('utf-8')
		except UnicodeDecodeError:
			return ''
##################################################
def searchColor(row,search,c='green',p=1):
	for sub in caseUnspecificCode(row,search):row=row.replace(sub,pr(sub,c,p=0))
	if p: print(row)
	return row
##################################################
def pp(fi=False):
	try:
		if not isData(r=0):
			try:
				_paste = regImp( __.appReg, '-paste' )
				data=_paste.imp.paste().split('\n')
			except: pass

			if fi:
				d=data.copy()
				data=[]
				for x in d:
					x=x.strip()
					if os.path.isfile(x): data.append(x)
		else: data=isData()
		return data
	except: return isData(r=0)
myData=pp
##################################################
def zip9(folder_path, zip_path):
	zipfile=__.imp('zipfile')
	with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_BZIP2) as zipf:
		for root, dirs, files in os.walk(folder_path):
			for file in files:
				file_path = os.path.join(root, file)
				relative_path = os.path.relpath(file_path, folder_path)
				zipf.write(file_path, arcname=relative_path)
	return zip_path
##################################################

def an(string): import re; return re.sub(r'\W+', '', string); # removes all non-alphanumeric characters including spaces
def ansp(string): import re; return re.sub(r' +', ' ', re.sub(r'[^\w\s]', '', string)) # removes all non-alphanumeric characters accept single spaces
##################################################
def sp1(string): import re; return re.sub(' +', ' ', string); # removes double spaces
def lis(has,string):
	''' # LIST IN STRING '''
	if type(has) == str: has = sp1(has).strip().split(' ')
	return all(item in string for item in has )
def lisa(has,string):
	''' # LIST IN STRING HAS ALL'''
	if type(has) == str: has = sp1(has).strip().split(' ')
	return all(string.count(item) == has.count(item) for item in set(has))

def dicSort(d): return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
sortDic=dicSort
##################################################
def dict_to_markdown_table(dict_list):
	# print(dict_list); sys.exit();
	# Check if dict_list is a callable method rather than a list
	if callable(dict_list):
		return "Invalid input: expected a list, received a method"

	# Check if the list is empty
	if not dict_list or not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
		return "Invalid input: expected a list of dictionaries"

	# Extract headers (keys) from the first dictionary
	headers = dict_list[0].keys()
	header_row = '| ' + ' | '.join(headers) + ' |'

	# Create the separator row
	separator_row = '| ' + ' | '.join(['---'] * len(headers)) + ' |'

	# Create rows for each dictionary in the list
	rows = [header_row, separator_row]
	for d in dict_list:
		row = '| ' + ' | '.join(str(d.get(h, '')) for h in headers) + ' |'
		rows.append(row)

	# Join all rows into a single string
	results = '\n'.join(rows)
	results=results.replace('| --','|---')
	results=results.replace('-- |','---|')
	return results

# def dict_to_markdown_table(dict_list):
# 	if not dict_list:
# 		return "No data available"

# 	# Extract headers (keys) from the first dictionary
# 	headers = dict_list[0].keys()
# 	header_row = '| ' + ' | '.join(headers) + ' |'

# 	# Create the separator row
# 	separator_row = '| ' + ' | '.join(['---'] * len(headers)) + ' |'

# 	# Create rows for each dictionary in the list
# 	rows = [header_row, separator_row]
# 	for d in dict_list:
# 		row = '| ' + ' | '.join(str(d[h]) for h in headers) + ' |'
# 		rows.append(row)

# 	# Join all rows into a single string
# 	return '\n'.join(rows)

##################################################
## micro helpers
def _default_triggers_():
	global switches
	if not 'Files' in __.setting('omit-switch-triggers',d=[]):
		switches.trigger( 'Files', myFileLocations, vs=True )
	if not 'Ago' in __.setting('omit-switch-triggers',d=[]):
		switches.trigger( 'Ago', timeAgo )
	if not 'Folder' in __.setting('omit-switch-triggers',d=[]):
		switches.trigger( 'Folder', myFolderLocations )
	if not 'Folders' in __.setting('omit-switch-triggers',d=[]):
		switches.trigger( 'Folders', myFolderLocations )
	if not 'URL' in __.setting('omit-switch-triggers',d=[]):
		switches.trigger( 'URL', urlTrigger )
	if not 'Duration' in __.setting('omit-switch-triggers',d=[]):
		switches.trigger( 'Duration', timeFuture )
def _default_settings_():
	__.setting('receipt-log',True)
	__.setting('receipt-file',True)
	__.setting('myFileLocations-skip-validation',False)
	__.setting('require-pipe',False)
	__.setting('require-pipe||file',False)
	__.setting('pre-error',False)
	__.setting('switch-raw',[])
	__.setting('default-switches',True)
def appInfoContinuity(app,info={}):
	if not 'file' in info: info['file'] = __.thisApp( __file__ )
	if not 'liveAppName' in info: info['liveAppName'] = __.thisApp( __file__ )
	if not 'description' in info: info['description'] = 'Changes the world'
	keys = '''
categories
usage
relatedapps
prerequisite
examples
columns
aliases
notes
	'''
	keys=keys.strip()
	keys=keys.split('\n')
	for k in keys:
		if not k in info: info[k]=[]
	return info
def appDataContinuity(info={}):
	if not info:
		info = {
			'start': __.startTime,
			'uuid': '',
			'audit': [],
			'pipe': False,
			'data': {
						'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
						'table': {'sent': [], 'received': [] },
			},
		}
		return info
	if not 'start' in info: info['start'] = __.startTime
	if not 'uuid' in info: info['uuid'] = ''
	if not 'audit' in info: info['audit'] = []
	if not 'pipe' in info: info['pipe'] = False
	if not 'data' in info: info['data'] = {
		'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
		'table': {'sent': [], 'received': [] },
		}
def injectLines(data, lines, start, end):
	# Convert inputs to lists of lines if they're strings
	if isinstance(data, str):
		data = data.replace('\r', '').split('\n')
	if isinstance(lines, str):
		lines = lines.replace('\r', '').split('\n')

	# Initialize variables
	modified_data = []
	in_range = False

	# Iterate through each line of the original data
	for line in data:
		# Check for the start marker
		if start in line:
			in_range = True
			modified_data.append(line)
			continue  # Move to the next iteration to avoid appending the start line twice

		# Check for the end marker
		if end in line and in_range:
			# Append the lines to be injected
			modified_data.extend(lines)
			in_range = False

		# Append current line if not in the range to skip
		if not in_range or line == end:
			modified_data.append(line)

	# Return the modified data as a single string
	return '\n'.join(modified_data)

def injectLinesTest():
	data = '''
aaa
bbb
ccc
123
xxx
yyy
zzz
456
ddd
eee
fff
'''

	lines = '''
this
is
a
test
'''
	print(injectLines(data, lines, '123', '456'))




##################################################
isHeaders = {
	# IS(path, 'gz')
	'gzip': '1F 8B 08 08',
	'docx': [
		'50 4B 03 04',
		'50 4B 05 06',
	],
	'isCrypt': '41 45 53 02 00 00 1B',
	'gz': '1F 8B 08 08',
	'bz2': '42 5A 68',
}
##################################################



def compress2(original_file_path, compressed_file_path):
	import gzip
	import shutil
	try:
		if IS(original_file_path,'gzip'):
			shutil.copyfile(original_file_path, compressed_file_path)
			return 'Skipped'
		with open(original_file_path, 'rb') as original_file:
			with gzip.open(compressed_file_path, 'wb') as compressed_file:
				shutil.copyfileobj(original_file, compressed_file)
		print(f"Compressed gzip {original_file_path}")
	except:
		return 'Error'

def decompress2(compressed_file_path, decompressed_file_path):
	import gzip
	import shutil
	try:
		if not IS(compressed_file_path,'gzip'):
			shutil.copyfile(compressed_file_path, decompressed_file_path)
			return 'Skipped'
		with gzip.open(compressed_file_path, 'rb') as compressed_file:
			with open(decompressed_file_path, 'wb') as decompressed_file:
				shutil.copyfileobj(compressed_file, decompressed_file)
		print(f"Decompressed gzip {decompressed_file_path}")
	except:
		return 'Error'

def compress(path):
	import gzip
	import shutil
	if IS(path,'gzip'): return False
	path = __.path(path)
	compressed_file_path = path
	original_file_path = path+'_temp'
	os.rename(path, original_file_path)
	with open(original_file_path, 'rb') as original_file:
		with gzip.open(compressed_file_path, 'wb') as compressed_file:
			shutil.copyfileobj(original_file, compressed_file)
	print(f"Compressed gzip {compressed_file_path}")
	os.unlink(original_file_path)

def decompress(path):
	import gzip
	import shutil
	if not IS(path,'gzip'): return False
	path = __.path(path)
	decompressed_file_path = path
	compressed_file_path = path+'_temp'
	os.rename(path, compressed_file_path)
	with gzip.open(compressed_file_path, 'rb') as compressed_file:
		with open(decompressed_file_path, 'wb') as decompressed_file:
			shutil.copyfileobj(compressed_file, decompressed_file)
	print(f"Decompressed gzip {decompressed_file_path}")
	os.unlink(compressed_file_path)
def BYTES(path): os.stat(  path  ).st_size
MOD=mod
def fileMeta(path,include='',individual=False):
	# print(path)
	# print(include)
	path = __.path(path)
	meta = {}
	if 'md5' == include and not 'md5' in meta:
		import _rightThumb._md5 as _md5
		meta['md5'] = _md5.md5File(path)
		if individual: return meta['md5']
		return meta
	if 'sha1' == include and not 'sha1' in meta:
		import _rightThumb._md5 as _md5
		meta['sha1'] = _md5.string(path,'sha1')
		if individual: return meta['sha1']
		return meta
	if 'sha256' == include and not 'sha256' in meta:
		import _rightThumb._md5 as _md5
		meta['sha256'] = _md5.string(path,'sha256')
		if individual: return meta['sha256']
		return meta
	if 'sha512' == include and not 'sha512' in meta:
		import _rightThumb._md5 as _md5
		meta['sha512'] =_md5.string(path,'sha512')
		if individual: return meta['sha512']
		return meta
	if not include:
	# if True:
		meta['path']     = path
		meta['file']     = __.path(path,file=True)
		meta['folder']   = path[:-len(meta['file'])-1]
		meta['bytes']    = os.stat(path).st_size
		meta['size']     = formatSize(meta['bytes'])
		meta['modified'] = os.path.getmtime(path)
		meta['created']  = os.path.getctime(path)
		meta['accessed'] = os.path.getatime(path)
		meta['me'] = meta['modified']
		meta['ce'] = meta['created']
		meta['ae'] = meta['accessed']
	else:
		import _rightThumb._dir as _dir
		meta = _dir.individual(path,include,True)
	if individual:
		if len(meta.keys()) == 1:
			return meta[ list(meta.keys())[0] ]
	return meta
##################################################
def prWC(text,colorize,color='green'):
	# wc = word color
	if type(colorize) == str:
		for subject in caseUnspecificCode( text, colorize ):
			text = text.replace( subject, colorThis( subject, color, p=0 ) )
	else:
		for clr in colorize:
			for subject in caseUnspecificCode( text, clr ):
				text = text.replace( subject, colorThis( subject, color, p=0 ) )
	return text
def prWC2(text, colorize, color='green', color2='cyan'):
	# Function to colorize parts of the text based on the keywords in colorize
	if type(colorize) == str:
		new = []
		subjects = caseUnspecificCode(text, colorize)
		last_end = 0
		for subject in subjects:
			start = text.find(subject, last_end)
			new.append(colorThis(text[last_end:start], color2, p=0))
			new.append(colorThis(subject, color, p=0))
			last_end = start + len(subject)
		new.append(colorThis(text[last_end:], color2, p=0))
		text = ''.join(new)
	else:
		import re
		subjects = []
		for clr in colorize:
			subjects.extend(caseUnspecificCode(text, clr))
		subjects = list(set(subjects))  # Remove duplicates
		pattern = "|".join(map(re.escape, subjects))
		parts = []
		last_end = 0
		for match in re.finditer(pattern, text):
			parts.append(colorThis(text[last_end:match.start()], color2, p=0))
			parts.append(colorThis(match.group(0), color, p=0))
			last_end = match.end()
		parts.append(colorThis(text[last_end:], color2, p=0))
		text = ''.join(parts)
	return text
##################################################
def Form(form,p=False):
	__.FormPrint = p
	from _rightThumb._forms import genForm
	results = genForm(form)
	return results
##################################################
def isGui():
	import platform
	if platform.system() == "Windows":
		return True
	else:
		display_var = os.getenv('DISPLAY')
		if display_var:
			return True
	return False
##################################################
def ptr(data, theColumns, id=None):
	if id is None:
		id = genUUID()
	tables.print( id, unixAutoColumns( data, theColumns, __.appReg ) )
##################################################


# if not dic and not autoDic: return mdFigSimp(md=md, title=title, wrap=wrap, file=file, t=t, w=w, f=f)




def mdFig(md='', title='###', wrap=True, file=None, t=None, w=None, f=None, dic=False, autoDic=True, context=False):
	if not t is None:
		title = t
	title = title.strip() + ' '
	if not w is None:
		wrap = w
	if not f is None:
		file = f

	if isinstance(md, str):
		md = md.split('\n')

	comments = {
		"multi": [
			{"lan": "html", "code": "<!--{contents}-->",},
			{"lan": "js", "code": "/*{contents}*/"},
			{"lan": "php", "code": "/*{contents}*/"},
			{"lan": "py", "code": '"""{contents}"""'},
			{"lan": "py", "code": "'''{contents}'''"},
			{"lan": "java", "code": "/*{contents}*/"},
			{"lan": "c", "code": "/*{contents}*/"},
			{"lan": "ruby", "code": "=begin\n{contents}\n=end"},
			{"lan": "sql", "code": "/*{contents}*/"},
			{"lan": "swift", "code": "/*{contents}*/"},
		],
		"single": [
			{"lan": "js", "code": "//"},
			{"lan": "php", "code": "//"},
			{"lan": "py", "code": "#"},
			{"lan": "java", "code": "//"},
			{"lan": "c", "code": "//"},
			{"lan": "ruby", "code": "#"},
			{"lan": "swift", "code": "//"},
		]
	}

	code = {}
	current_section = None
	current_snippet = []
	is_snippet = False
	snippet_language = None

	def initialize_comment_settings(line_containing_language):
		commentSettings = {}
		commentSettings['hasMulti'] = False
		commentSettings['hasSingle'] = False
		commentSettings['lan'] = line_containing_language.split('~~~')[-1].lower()
		for rec in comments['multi']:
			if rec['lan'] == commentSettings['lan']:
				commentSettings['hasMulti'] = True
				commentSettings['multiOpen'] = rec['code'].split('{contents}')[0]
				commentSettings['multiClose'] = rec['code'].split('{contents}')[1]
		for rec in comments['single']:
			if rec['lan'] == commentSettings['lan']:
				commentSettings['hasSingle'] = True
				commentSettings['single'] = rec['code']
		return commentSettings

	def parse_iter_markers(lines):
		"""Extract and replace iter markers dynamically."""
		result_lines = []
		iter_items = []
		current_iter_code = []
		subject = None
		inside_iter = False

		for line in lines:
			stripped = line.strip()
			if "iter:Start:" in stripped:
				inside_iter = True
				subject = stripped.split(":")[-1].strip(" -->")
				iter_marker = f"<!-- iter:{subject}:{len(iter_items) + 1}  -->"
				result_lines.append(iter_marker)
			elif "iter:End:" in stripped and inside_iter:
				inside_iter = False
				iter_items.append({
					"Subject": subject,
					"Replace": iter_marker,
					"Code": '\n'.join(current_iter_code).strip()
				})
				current_iter_code = []
			elif inside_iter:
				current_iter_code.append(line)
			else:
				result_lines.append(line)

		return result_lines, iter_items


	def remove_comments_and_parse_metadata(snippet_value, comment_settings):
		"""Remove comments and parse metadata based on the comment settings."""
		import yaml
		snippet_metadata = {}
		lines = snippet_value.split('\n')
		language = comment_settings['lan']

		# Handle multi-line comments
		if comment_settings['hasMulti']:
			if lines[0].strip().startswith(comment_settings['multiOpen']):
				yaml_lines = []
				for line in lines[1:]:  # Start after the opening tag
					if line.strip().startswith(comment_settings['multiClose']):
						break
					yaml_lines.append(line.strip())
				yaml_content = '\n'.join(yaml_lines).strip()
				
				# Parse the metadata from YAML-like structure
				try:
					parsed_metadata = yaml.safe_load(yaml_content)
					if isinstance(parsed_metadata, dict):
						# Preserve the original keys without modification
						snippet_metadata = parsed_metadata
				except yaml.YAMLError:
					snippet_metadata = {}
				
				# Remove the metadata lines from snippet_value
				snippet_value = '\n'.join(lines[len(yaml_lines) + 2:]).strip()  # Skip opening/closing tags

		# Handle single-line comments
		elif comment_settings['hasSingle']:
			single_line_comment = comment_settings['single']
			yaml_lines = []
			remaining_lines = []
			for line in lines:
				if line.strip().startswith(single_line_comment):
					yaml_lines.append(line[len(single_line_comment):].strip())
				else:
					remaining_lines.append(line)
			try:
				parsed_metadata = yaml.safe_load('\n'.join(yaml_lines))
				if isinstance(parsed_metadata, dict):
					snippet_metadata = parsed_metadata
			except yaml.YAMLError:
				snippet_metadata = {}
			snippet_value = '\n'.join(remaining_lines).strip()

		return snippet_value, snippet_metadata




	for line in md:
		stripped_line = line.strip()

		# Detect sections
		if stripped_line.startswith(title):
			current_section = stripped_line[len(title):].strip()
			continue

		# Start or end a code snippet
		if stripped_line.startswith('~~~'):
			if is_snippet:
				# End of the snippet
				if current_section:
					snippet_key = current_section
					snippet_value = '\n'.join(current_snippet)

					# Initialize comment settings
					comment_settings = initialize_comment_settings(snippet_language)

					# Remove comments and parse metadata if context=True
					snippet_metadata = {}
					if context:
						snippet_value, snippet_metadata = remove_comments_and_parse_metadata(snippet_value, comment_settings)

					# Process iter markers
					result_lines, iter_items = parse_iter_markers(snippet_value.split('\n'))

					if dic or autoDic:
						# Store as dict with metadata
						code[snippet_key] = {
							"original": snippet_value,
							"code": '\n'.join(result_lines).strip(),
							"iter": iter_items,
						}
						if context or dic:
							code[snippet_key]["metadata"] = snippet_metadata
					else:
						# Store unmodified snippet as string
						code[snippet_key] = snippet_value

				# Reset snippet tracking
				current_snippet = []
				is_snippet = False
				snippet_language = None
			else:
				# Start of the snippet
				is_snippet = True
				snippet_language = stripped_line[3:].lower() if len(stripped_line) > 3 else None
		elif is_snippet:
			# Accumulate snippet lines
			current_snippet.append(line)

	# Return the full dictionary of snippets
	return code






def mdFigSimp(md='', title='###', wrap=True, file=None, t=None, w=None, f=None):
	if not t is None: title=t
	if not w is None: wrap=w
	if not f is None: file=f
	if not file is None:
		if os.path.isfile(file):
			md = open(file, 'r').read()
		elif os.path.isfile(_v.mdFig+os.sep+file):
			md = open(_v.mdFig+os.sep+file, 'r').read()
		elif os.path.isfile(_v.ttt+os.sep+file):
			md = open(_v.ttt+os.sep+file, 'r').read()
	if type(md) == str: md = md.split('\n')
	isOpen=False
	current = []
	fig = {}
	code = {}
	defaultSection = '5e85ba2c-4476-4910-81ab-917152328c05'
	section = defaultSection
	mdFile = '\n'.join(md).replace('\r','')
	if not '\n### ' in mdFile and '\n## ' in mdFile:
		title = '##'
	for line in md:
		lineRaw=line
		line=line.strip()
		if line.startswith('```') and not line.startswith('````'):
			line = line.replace('```','~~~')
		if line.startswith(title): section = line.split(title+' ')[1]
		if isOpen and line.startswith('~~~'):
			if wrap:
				code[section] = '\n'+'\n'.join(current)+'\n'
			else:
				code[section] = '\n'.join(current)
			isOpen = False
			current = []
		elif not isOpen and line.startswith('~~~'):
			isOpen = True
		elif isOpen:
			current.append(lineRaw)
	if defaultSection in code: del code[defaultSection]
	return code
##################################################
def code( script, addString=None, lan = 'javascript' ):
	global _code
	try:
		__.code
	except Exception as e:
		_code = regImp( __.appReg, '_rightThumb._auditCodeBase' )
	_code.imp.validator.register( script, lan )
	return __.code.process( script, addString=addString )
def code2( script, addString=None, lan = 'javascript' ):
	li = code( script, addString, lan )
	index = {}
	for rec in li:
		# print(rec)
		index[rec['o']] = rec['c']
		# try:
		# except: pass
	return index

def codex(data):
	dirty = code( data )
	index = {}
	for rec in dirty:
		index[rec['o']] = rec['c']
	return {
		'index': index,
		'records': dirty
	}

def acb(data): return codex( data )['index']
import re

def codex2(text, phrases=None, language=None):
	"""
	Finds open-close pairs for various delimiters and custom phrases in a string.
	
	Args:
		text (str): The text to analyze.
		phrases (list): A list of phrases to find and pair.
		language (str): The language or context (e.g., "SQL", "HTML", "Python").
						Defaults to common programming and markup languages.
		
	Returns:
		dict: A dictionary mapping open index positions to close index positions.
	"""
	# Define open-close pairs for common programming and markup languages
	common_pairs = {
		'}': '{', ')': '(', ']': '[', '>': '<',
		'"': '"', "'": "'", '`': '`', '|': '|', '‖': '‖',
		'⌋': '⌊', '⌉': '⌈',
	}

	# Multicharacter open-close pairs
	common_multi_pairs = {
		'"""': '"""', "'''": "'''", '{{': '}}', '${': '}',
	}

	# Language-specific extensions
	language_pairs = {}
	if language == "HTML" or language == "XML":
		language_pairs = {
			'</': '<',  # For HTML/XML tags
		}
	elif language == "SQL":
		language_pairs = {
			'BEGIN': 'END',  # SQL blocks
		}
	elif language == "Python":
		language_pairs = {}  # No additional pairs for Python
	
	# Merge language-specific pairs into common pairs
	pairs = {**common_pairs, **language_pairs}
	multi_pairs = {**common_multi_pairs}
	
	# Initialize stack and result
	stack = []
	result = {}
	
	# Add custom phrases to be searched
	if phrases:
		phrase_locs = {}
		for phrase in phrases:
			for match in re.finditer(re.escape(phrase), text):
				start = match.start()
				phrase_locs[start] = start + len(phrase)  # Store phrase ends
		result.update(phrase_locs)

	# Scan through the text
	i = 0
	while i < len(text):
		# Check for multicharacter open-close pairs
		for open_token, close_token in multi_pairs.items():
			if text.startswith(open_token, i):
				stack.append((open_token, i))
				i += len(open_token) - 1  # Skip the token length
				break
			if text.startswith(close_token, i):
				if stack and stack[-1][0] == open_token:
					_, start_idx = stack.pop()
					result[start_idx] = i + len(close_token) - 1
				else:
					raise ValueError(f"Unmatched closing token '{close_token}' at index {i}")
				i += len(close_token) - 1
				break

		# Check for single-character open-close pairs
		char = text[i]
		if char in pairs.values():  # Opening character
			stack.append((char, i))
		elif char in pairs.keys():  # Closing character
			if stack and stack[-1][0] == pairs[char]:  # Matches the last opening
				_, start_idx = stack.pop()
				result[start_idx] = i
			else:
				raise ValueError(f"Unmatched closing character '{char}' at index {i}")
		i += 1

	# Error if unmatched open tokens remain
	if stack:
		unmatched = [f"{char} at index {idx}" for char, idx in stack]
		raise ValueError(f"Unmatched opening characters: {', '.join(unmatched)}")

	return result

##################################################
# def simpleIndex(text):
#     open_close_pairs = {
#         '{': '}', '[': ']', '(': ')', '<': '>', '"': '"', "'": "'"
#     }
#     stack = []  # Stack to keep track of open positions
#     index = {}  # Dictionary to store open-close pairs
#     in_quote = None  # Tracks if we're inside a quote
#     escape_next = False  # Flags the next character as escaped

#     for i, char in enumerate(text):
#         # If the character is escaped, skip processing this loop iteration
#         if escape_next:
#             escape_next = False
#             continue

#         # Check if we're entering an escape sequence
#         if char == '\\' and not escape_next:
#             escape_next = True
#             continue

#         # Manage quoted text
#         if in_quote:
#             if char == in_quote:  # End of quoted section
#                 start_index = stack.pop()
#                 index[start_index] = i
#                 in_quote = None
#             continue

#         # If char starts a quote and we're not already inside one
#         if char in {'"', "'"} and not in_quote:
#             in_quote = char
#             stack.append(i)
#             continue

#         # Handle open brackets if not inside a quote
#         if char in open_close_pairs and not in_quote:
#             stack.append(i)

#         # Handle close brackets if not inside a quote
#         elif char in open_close_pairs.values() and not in_quote:
#             if stack:
#                 start_index = stack.pop()
#                 open_char = text[start_index]
#                 if open_char in open_close_pairs and open_close_pairs[open_char] == char:
#                     index[start_index] = i

#     return index




# class deX:

# 	def __init__( self, data ):
# 		self.o(data)
# 		self.c(data)
# 	def o(self, text): # simpleIndex open close
# 		open_close_pairs = {'{': '}', '[': ']', '(': ')', '<': '>', '"': '"', "'": "'", '`': '`'}
# 		stack = []  # Stack to keep track of open positions
# 		index = {}  # Dictionary to store open-close pairs
# 		in_quote = None  # Tracks if we're inside a quote
# 		escape_next = False  # Flags the next character as escaped

# 		# This loop will handle each character and identify quotes, escaped characters, and bracket pairs
# 		for i, char in enumerate(text):
# 			# If the character is escaped, skip processing this loop iteration
# 			if escape_next:
# 				escape_next = False
# 				continue

# 			# Check if we're entering an escape sequence
# 			if char == '\\' and not escape_next:
# 				escape_next = True
# 				continue

# 			# If we're inside a quote, handle closing it
# 			if in_quote:
# 				if char == in_quote:  # End of quoted section
# 					start_index = stack.pop()
# 					index[start_index] = i
# 					in_quote = None
# 				continue

# 			# Handle the start of a quoted section
# 			if char in {'"', "'"} and not in_quote:
# 				in_quote = char
# 				stack.append(i)
# 				continue

# 			# Handle open brackets if not inside a quote
# 			if char in open_close_pairs and not in_quote:
# 				stack.append((i, char))

# 			# Handle close brackets if not inside a quote
# 			elif char in open_close_pairs.values() and not in_quote:
# 				if stack:
# 					start_index, open_char = stack.pop()
# 					if open_close_pairs[open_char] == char:
# 						index[start_index] = i  # Record the open-close pair
# 		self.oi = index
# 		return self.oi

# 	def p(self, text, phrases): # phraseIndex
# 		import re
# 		# Initialize dictionaries for index and definitions
# 		index = {}
# 		definition = {}
# 		phDex = {}
# 		# Loop through each phrase and search for occurrences in text
# 		for phrase in phrases:
# 			if not phrase in reverse:
# 				phDex[phrase] = []
# 			matches = [match.start() for match in re.finditer(re.escape(phrase), text)]
# 			for start in matches:
# 				end = start + len(phrase)
# 				index[start] = end
# 				definition[start] = phrase
# 				phDex[phrase].append(start)
		
# 		# Return a multidimensional dictionary
# 		self.pi = {
# 			"index": index,
# 			"def": definition,
# 			"ph": phDex
# 		}
# 		return self.pi

# 	def c(self, text): # index_newlines / carriage return
# 		"""
# 		Indexes all newline characters in the text.
# 		Returns a list of character indices where each newline is found.
# 		"""
# 		self.ci = [index for index, char in enumerate(text) if char == '\n']
# 		return self.ci

# 	def l(self, index): # find_line
# 		"""
# 		Given a character index and a list of newline indices, 
# 		returns the line number (1-based) for the character index.
# 		"""
# 		# Find the line by counting how many newlines are before the given index
# 		line = 1
# 		for newline_index in self.ci:
# 			if index < newline_index:
# 				break
# 			line += 1
# 		return line





class deX:

	# def __init__( self ): pass

	def o(text): # simpleIndex open close
		open_close_pairs = {'{': '}', '[': ']', '(': ')', '<': '>', '"': '"', "'": "'", '`': '`'}
		stack = []  # Stack to keep track of open positions
		index = {}  # Dictionary to store open-close pairs
		in_quote = None  # Tracks if we're inside a quote
		escape_next = False  # Flags the next character as escaped

		# This loop will handle each character and identify quotes, escaped characters, and bracket pairs
		for i, char in enumerate(text):
			# If the character is escaped, skip processing this loop iteration
			if escape_next:
				escape_next = False
				continue

			# Check if we're entering an escape sequence
			if char == '\\' and not escape_next:
				escape_next = True
				continue

			# If we're inside a quote, handle closing it
			if in_quote:
				if char == in_quote:  # End of quoted section
					start_index = stack.pop()
					index[start_index] = i
					in_quote = None
				continue

			# Handle the start of a quoted section
			if char in {'"', "'"} and not in_quote:
				in_quote = char
				stack.append(i)
				continue

			# Handle open brackets if not inside a quote
			if char in open_close_pairs and not in_quote:
				stack.append((i, char))

			# Handle close brackets if not inside a quote
			elif char in open_close_pairs.values() and not in_quote:
				if stack:
					start_index, open_char = stack.pop()
					if open_close_pairs[open_char] == char:
						index[start_index] = i  # Record the open-close pair

		return index

	def p(text, phrases): # phraseIndex
		import re
		# Initialize dictionaries for index and definitions
		index = {}
		definition = {}
		phDex = {}
		# Loop through each phrase and search for occurrences in text
		for phrase in phrases:
			if not phrase in phDex:
				phDex[phrase] = []
			matches = [match.start() for match in re.finditer(re.escape(phrase), text)]
			for start in matches:
				end = start + len(phrase)
				index[start] = end
				definition[start] = phrase
				phDex[phrase].append(start)
		
		# Return a multidimensional dictionary
		result = {
			"index": index,
			"def": definition,
			"ph": phDex
		}
		return result

	def c(text): # index_newlines / carriage return
		"""
		Indexes all newline characters in the text.
		Returns a list of character indices where each newline is found.
		"""
		return [index for index, char in enumerate(text) if char == '\n']

	def l(index, newline_indices): # find_line
		"""
		Given a character index and a list of newline indices, 
		returns the line number (1-based) for the character index.
		"""
		# Find the line by counting how many newlines are before the given index
		line = 1
		for newline_index in newline_indices:
			if index < newline_index:
				break
			line += 1
		return line
	def i(data): # auditCodeBase but indexed
		return codex( data )['index']
	def x(data,phrases,language): codex2(data,phrases,language)
oIndex = deX.o
simpleIndex = deX.o
pIndex = deX.p
phraseIndex = deX.p
cIndex = deX.c
carriageIndex = deX.c
cLine = deX.l
find_line = deX.l
##################################################

def formatSizeUp(size_in_bytes):
	size = formatSizeUpMath(size_in_bytes)
	value, unit = size.split(' ')
	value = int(value)
	
	# If the value is a single digit, do nothing
	if len(str(value)) == 1:
		return size

	# Determine target size based on real-world drive sizes
	target_value = next_real_world_drive_size(value, unit)
	while value < target_value:
		increment = increments[unit]  # Increment by the appropriate unit
		size_in_bytes += increment
		size = formatSizeUpMath(size_in_bytes)
		value, unit = size.split(' ')
		value = int(value)
	
	return size

def next_real_world_drive_size(value, unit):
	"""Get the next real-world drive size based on the unit."""
	if unit == "GB":
		# Common USB and SSD sizes in GB
		common_sizes = [8, 16, 32, 64, 128, 256, 512, 750, 1000]  # 750 GB for transitional HDDs
		for size in common_sizes:
			if value <= size:
				return size
		return value + 250  # Default increment if above known sizes

	elif unit == "TB":
		# Common HDD sizes in TB
		common_sizes = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
		for size in common_sizes:
			if value <= size:
				return size
		return value + 2  # Default increment for larger drives

	return value  # If no match, return the value as is

def formatSizeUpMath(size_in_bytes):
	import math
	units = [
		(1 << 60, "EB"),  # Exabyte
		(1 << 50, "PB"),  # Petabyte
		(1 << 40, "TB"),  # Terabyte
		(1 << 30, "GB"),  # Gigabyte
		(1 << 20, "MB"),  # Megabyte
		(1 << 10, "KB"),  # Kilobyte
		(1, "B")          # Byte
	]
	
	for factor, suffix in units:
		if size_in_bytes >= factor:
			value = math.ceil(size_in_bytes / factor)
			return f"{value} {suffix}"
	
	return "0 B"

# Define increments for each unit
increments = {
	"B": 1,
	"KB": 1 << 10,  # 1024 bytes
	"MB": 1 << 20,  # 1024^2 bytes
	"GB": 1 << 30,  # 1024^3 bytes
	"TB": 1 << 40,  # 1024^4 bytes
	"PB": 1 << 50,  # 1024^5 bytes
	"EB": 1 << 60   # 1024^6 bytes
}





##################################################
'''
AesEverywhere
git clone https://github.com/mervick/aes-everywhere
cd aes-everywhere/python
pip install --upgrade pip setuptools wheel build
python -m build
pip install dist/aes_everywhere-1.2.9-py3-none-any.whl
pip install -e .
python -m pip show aes-everywhere
'''
class aesEverywhere:
	def __init__(self,password=None):
		if password is None and 'aes' in _v.fig:
			password = _v.fig['aes']
		try:
			from AesEverywhere import aes256
		except: pass
		self.aes256 = aes256
		self.password = password

	def binEncrypt(self, data, key=None ):
		if key is None: key = self.password
		return self.aes256.encrypt(data,key)
	def binDecrypt(self, data, key=None ):
		if key is None: key = self.password
		return self.aes256.decrypt(data,key)
	
	def encrypt(self, data, key=None ):
		if key is None: key = self.password
		return self.aes256.encrypt(data,key).decode('utf-8')
	def decrypt(self, data, key ):
		if key is None: key = self.password
		try:
			return self.aes256.decrypt(data,key).decode('utf-8')
		except:
			e('Decryption Failure','Possibly bad password.')

	## SHORTCUTS

	def bEn(self, data, key=None ):
		return self.binEncrypt(data,key)
	def bDe(self, data, key=None ):
		return self.binDecrypt(data,key)
	def be(self, data, key=None ):
		return self.binEncrypt(data,key)
	def bd(self, data, key=None ):
		return self.binDecrypt(data,key)

	def e(self, data, key=None ):
		return self.encrypt(data,key)
	def d(self, data, key=None ):
		return self.decrypt(data,key)
	def en(self, data, key=None ):
		return self.encrypt(data,key)
	def de(self, data, key=None ):
		return self.decrypt(data,key)

# _base3.aesEverywhere
##################################################

# __.switch_raw
##################################################
# class regImp:
# positiveResultsCode
# __.sw.PlusCode
# def caseUnspecific
# caseISspecific
# releaseAcquiredData
##################################################
# globals()['var']
##################################################
# alt+29 ↔ is space
##################################################

def rImp(app):
	import importlib.util
	module_name = app
	file_path = os.path.join(_v.py, app + ".py")

	# Load the module spec
	spec = importlib.util.spec_from_file_location(module_name, file_path)
	if spec is None:
		raise ImportError(f"Cannot find module at path: {file_path}")

	# Create the module
	module = importlib.util.module_from_spec(spec)

	# Add it to sys.modules
	sys.modules[module_name] = module

	# Execute the module
	spec.loader.exec_module(module)

	return module


##################################################




def create_backup_filename(*args, **kwargs):
	if not 'create_backup_filename' in intelligent_code.functions:
		from library.tools.os.file.create_backup_filename import create_backup_filename
		intelligent_code.functions['create_backup_filename'] = create_backup_filename
	return intelligent_code.functions['create_backup_filename'](*args, **kwargs)




fibk=create_backup_filename
backupName=create_backup_filename
##################################################
pr0c='yellow'
def pr0(*args,c=None):
	global pr0c
	if c is None: c=pr0c
	return pr(*args,c=c,p=0)
##################################################

def isLink(path):
	if os.path.islink(path): return True
	try: return os.stat(path).st_nlink > 1
	except: return False

##################################################
def logLine(*items, log=None):
	if log is None:
		e("missing log='file.log'")
		return
	
	try:
		asterisks = '*' * len(items)
		tab_delimited_items = '\t'.join(map(str, items))
		with open(log, 'a') as log_file:
			log_file.write(f'{asterisks}\n')
			log_file.write(f'{tab_delimited_items}\n')
		pr('Saved',c='green')
		return True
	except Exception as e:
		e(f"Error appending to log file: {e}")
		return False
##################################################
# self.value('Help')
# 'DumpSwitches'
# __.switch_skimmer.active
# 11780
# if switches.isActive('Plus-single'): break
# dict_to_markdown_table
# sys.stdin.readlines()
########################################################################################
import time

def bkExpire(*args, **kwargs):
	if not 'bkExpire' in intelligent_code.functions:
		from library.tools.os.file.bkExpire import bkExpire
		intelligent_code.functions['bkExpire'] = bkExpire
	return intelligent_code.functions['bkExpire'](*args, **kwargs)




########################################################################################
import re

class FileLocker:
	@staticmethod
	def lockName(path):
		"""Strip non-filename safe characters."""
		return re.sub(r'[^\w\-_\. ]', '_', path)

	@staticmethod
	def lockPath(path):
		"""Get the lock file path, ensuring the directory exists."""
		folder_path = _v.fileLocks  # Assumes `_v.fileLocks` is defined in your framework
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)
		return os.path.join(folder_path, FileLocker.lockName(path))

	@staticmethod
	def lock(path):
		"""Rename the file to create a lock."""
		lock_path = FileLocker.lockPath(path)
		lock_file = lock_path + ".lock"
		start_time = time.time()
		while True:
			try:
				# Try renaming the file to acquire the lock
				os.rename(lock_path, lock_file)
				return  # Lock acquired
			except FileNotFoundError:
				# If the original file doesn't exist, create a dummy lock
				with open(lock_file, "w") as f:
					f.write("")  # Create an empty lock file
				return
			except OSError:
				# Another process holds the lock; wait and retry
				if time.time() - start_time > 10:  # Optional timeout of 10 seconds
					raise TimeoutError("Timeout waiting for lock")
				time.sleep(0.1)  # Retry after a short delay

	@staticmethod
	def unlock(path):
		"""Rename the lock file back to its original name."""
		lock_path = FileLocker.lockPath(path)
		lock_file = lock_path + ".lock"
		try:
			os.rename(lock_file, lock_path)  # Release the lock
		except FileNotFoundError:
			pass  # Lock already released or doesn't exist

	@staticmethod
	def check(path):
		"""Wait until the lock file does not exist."""
		lock_path = FileLocker.lockPath(path)
		lock_file = lock_path + ".lock"
		while os.path.exists(lock_file):
			time.sleep(0.1)
			# if time.time() - md(path) > 15:
			# 	pr('File Lock Override in 15 Seconds',c='red')

			if time.time() - md(path) > 30:
				pr('Lock Override',c='red')
				FileLocker.unlock(path)


# FileLocker.check(path)
# FileLocker.lock(path)
# FileLocker.unlock(path)
# folderProfileAttribute <-- errors

########################################################################################
def md(path): return os.path.getmtime(path)
########################################################################################


###################################
'''
class index
# indexes on init
	myVar = _.index(code)


## post init index


### .index: additional index changes nothing in the class
	myVar.index(code,settings)

### .fn: auto lang, js fn NS || py fn || php fn (no ns for php)
	myVar.fn()

### .line: line text by char pos
	myVar.line(i)

### .inDex: check if pos in range [o]=c
	myVar.inDex(index, pos, i=False)
		index is {} or 'oc' (myVar.db name)
		pos is char pos
		if i is False    <-------------------------------- bool
			returns bool unless
		if i is True     <-------------------------------- pos
			returns pos of open


			
### .nextDex: next o pos in  [o]=c
	myVar.nextDex(index, pos)
		index is {} or 'oc' (myVar.db name)

### .prevDex: previous o pos in  [o]=c
	myVar.prevDex(pos, index=None)
		index defaults to .db[oc]
		index is {} or 'quotes' (myVar.db name)

### .prevChar(i, search, code=None)
### .prevChar(i, 'a')
### .prevChar(i, 'an')
### .prevChar(i, 'n')
### .prevChar(i, 'an_.')
### .justDex(only=['{}','[]'],index=None, code=None)

### .justDex(only, index=None, code=None)
### .endOfLine(i, text=None)
### .startOfLine(i, text=None)




### additional line tools
	myVar.lineNumber(i)
	myVar.lineStart(i)

'''


class index:
	def __new__(cls, *args, **kwargs):
		if not 'index' in intelligent_code.classes:
			from library.tools.code.classes.index import  index as live
			intelligent_code.classes['index'] = live
		return intelligent_code.classes['index'](*args, **kwargs)


########################################################################################
def sort2(table, fields):
	"""Sorts a list of dictionaries based on multiple fields with ascending (.a) and descending (.d) support."""
	
	# Process sorting fields
	sorting_criteria = []
	reverse_flags = []

	for field in fields.replace(' ', '').split(','):
		if '.a' in field:
			sorting_criteria.append(field.replace('.a', ''))
			reverse_flags.append(False)  # Ascending
		elif '.d' in field:
			sorting_criteria.append(field.replace('.d', ''))
			reverse_flags.append(True)   # Descending
		else:
			sorting_criteria.append(field)
			reverse_flags.append(False)  # Default to ascending

	# Pre-process: Ensure all fields exist in each record
	for record in table:
		for field in sorting_criteria:
			if field not in record:
				# Determine default value (int -> 0, string -> "")
				record[field] = 0 if any(isinstance(r.get(field, ""), int) for r in table) else ""

	# Perform sorting
	table = sorted(
		table,
		key=lambda x: tuple(x[field] for field in sorting_criteria),
		reverse=False  # Always sort ascending first, then adjust descending fields
	)

	# Apply descending order where needed
	for field, reverse in reversed(list(zip(sorting_criteria, reverse_flags))):
		table = sorted(table, key=lambda x: x[field], reverse=reverse)

	return table

########################################################################################
WidgetsFW = {
	'_rightThumb._construct': '__',

	'_rightThumb._auditCodeBase': '_code',
	'_rightThumb._asynchronous': '_async',
	'_rightThumb._backupLog': '_bkLog',
	'_rightThumb._banners': '_banners',
	'_rightThumb._base3': '_',
	'_rightThumb._base': '_',
	'_rightThumb._base1': '_',
	'_rightThumb._base2': '_',
	'_rightThumb._base3b': '_',
	'_rightThumb._base3c': '_',
	'_rightThumb._base4': '___',
	'_rightThumb._base5': '_',
	'_rightThumb._beep': '_beep',
	'_rightThumb._beep': '_beeper',
	'_rightThumb._bookmarks': '_bm',
	'_rightThumb._cloud': '_cloud',
	'_rightThumb._copy': '_copy',
	'_rightThumb._date': '_date',
	'_rightThumb._dir': '_dir',
	'_rightThumb._drive': '_drive',
	'_rightThumb._encryptFile': '_bl',
	'_rightThumb._encryptFile': '_blowfish',
	'_rightThumb._encryptFile': '_crypt',
	'_rightThumb._encryptString': '_',
	'_rightThumb._encryptString': '_blowfish',
	'_rightThumb._getPipe': '_getPipe',
	'_rightThumb._imdb': '_imdb',
	'_rightThumb._logs': '_logs',
	'_rightThumb._Bible': '_B',
	'_rightThumb._matrix': '_matrix',
	'_rightThumb._md5': '_hash',
	'_rightThumb._md5': '_md5',
	'_rightThumb._mimetype': '_mime',
	'_rightThumb._nID': '_nID',
	'_rightThumb._pID': '_pID',
	'_rightThumb._profileVariables': '_',
	'_rightThumb._profileVariables': '_profile',
	'_rightThumb._servers': '_srv',
	'_rightThumb._sessions': '_sessions',
	'_rightThumb._simpleThreads': '_threads',
	'_rightThumb._stardate': '_sd',
	'_rightThumb._string': '_str',
	'_rightThumb._tar': '_tar',
	'_rightThumb._toolsScrapeFrontEnd': '_browser',
	'_rightThumb._tz': '_tz',
	'_rightThumb._vars': '_v',
	'_rightThumb._vault': '_vault',
	'_rightThumb._zipper': '_zipper',
}
WidgetsFW_Clean = {
	'_rightThumb._construct': '__',
	'_rightThumb._base3': '_',
	'_rightThumb._vars': '_v',
	'_rightThumb._string': '_str',
	'_rightThumb._dir': '_dir',
	'_rightThumb._md5': '_hash',
	'_rightThumb._vault': '_vault',
	'_rightThumb._encryptString': '_crypt',
	'_rightThumb._encryptFile': '_crypt',
	'_rightThumb._bookmarks': '_bm',
	'_rightThumb._beep': '_beep',
	'_rightThumb._copy': '_copy',
	'_rightThumb._date': '_date',
	'_rightThumb._mimetype': '_mime',

	'_rightThumb._backupLog': '_bkLog',
	'_rightThumb._banners': '_banners',
	'_rightThumb._getPipe': '_getPipe',
	'_rightThumb._logs': '_logs',
	'_rightThumb._matrix': '_matrix',
	
	
	'_rightThumb._nID': '_nID',
	'_rightThumb._pID': '_pID',
	'_rightThumb._profileVariables': '_profile',
	'_rightThumb._servers': '_srv',
	'_rightThumb._sessions': '_sessions',
	'_rightThumb._simpleThreads': '_threads',
	'_rightThumb._stardate': '_sd',

	'_rightThumb._tar': '_tar',
	'_rightThumb._toolsScrapeFrontEnd': '_browser',
	'_rightThumb._tz': '_tz',
	
	'_rightThumb._zipper': '_zipper',
}
WidgetsPY = [
	"_rightThumb._toolsScrapeFrontEnd2",
	"py3to2",
	"imdb",
	"inDic",
	"inFunc",
	"USB_python_modules_synchronized",
	"md",
	"_rightThumb._toolsScrapeFrontEnd",
	"vps-srv-7facG-twilio-send",
	"omitTable",
	"cryptFile",
	"file",
	"secure-delete-file",
	"\"fileBackup;_bk.switch('Silent;_bk.switch('isRunOnce;_bk.switch('Flag',appReg);_bk.switch('DoNotSchedule",
	"ticketTimeline",
	"_rightThumb._auditCodeBase",
	"_rightThumb._franchise",
	"fileNameDate",
	"_rightThumb._MoveDelete",
	"-paste",
	"vps-srv-7facG-twilio-retrieve",
	"tag",
	"steg",
	"greeting",
	"_rightThumb._backupLog",
	"foPath",
	"tmi",
	"netblock",
	"databank",
	"vps-call",
	"fi-len",
	"file-open",
	"listen",
	"keychain",
	"faAuto",
	"fileBackup",
	"fileHeader",
	"file_folder",
	"projectTimer",
	"record-cleaner",
	"_rightThumb._sms_listener",
	"gatekeeper",
	"fileRecover",
	"decrypt-docs",
	"vps-hoth-form-fields",
	"words",
	"secureFiles",
	"lock-files",
	"bookmarks",
	"filePathPatterns",
	"_rightThumb._asynchronous",
	"hotkeys",
	"_rightThumb._toolsScrapeDirect",
	"_rightThumb._vault",
	"auditJavascript",
	"dirList",
	"logout",
	"updateQuickIndex",
	"vps-text-key",
	"_rightThumb._sms_listener.group_auto_reply",
	"-copy"
]
########################################################################################
# bkExpire(_v.tt+os.sep+'fileBackup.json',_v.tt+os.sep+'fileBackup-bk.json',age='3h',cp=_v.tt+os.sep+'bk'+os.sep+'fileBackup')
# bkExpire(_v.tt+os.sep+'fileBackup.json',_v.tt+os.sep+'fileBackup-bk.json',age='3h',cp=_v.tt+os.sep+'bk'+os.sep+'fileBackup',force=True)
########################################################################################
# EOF