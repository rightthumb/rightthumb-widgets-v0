#!/usr/bin/python3
########################################################################################
# alt+29 ↔ is space
# helpColorScheme
# showLine, validLine


FilesFiles = []
isData_Save = False

AutoClipboardApps = [
	'isData',
	'line',
	'lineline',
	'hasLines',
	'thePath',
	'jsDict',
]
def isDataClip(app=None):
	global AutoClipboardApps

	if not app is None:
		AutoClipboardApps.append(app)
	
	for i,ac in enumerate(AutoClipboardApps):
		if not ac.startswith('__'):
			AutoClipboardApps[i] = '__'+ac+'__'
isDataClip(app=None)

# function_with_args_to_variable = lambda: my_fn("Alice")
# function_with_args_to_variable()




# p lineSnip -f base -start class Switches -stop #Switches-end + "def " -ln



##################################################
import _rightThumb._construct as __ # type: ignore
import _rightThumb._vars as _v # type: ignore
import _rightThumb._string as _str # type: ignore
##################################################
import glob
import sys,os,time,datetime,threading
from operator import itemgetter
from datetime import datetime as dt, timedelta
from datetime import date
##################################################
MINI_ADS = False
SHOW_ADS = False
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

helpColorScheme = dot()

# __.SwitchGroup_Help.SubGroup
# HasSwitchSubGroup
##################################################

## ################################################## ##
def isFile(path,simple=True,s=None):
	if not s is None: simple=s
	if not simple: return myFileLocations(path)
	if os.path.isfile(path): return __.path(path)
	if path.startswith('http:') or path.startswith('https:'):
		path=path.replace('http:','https:')
		path = autoUrl(path)
		return path
	if os.sep in path:
		return path
	return aliases_file_open(path)
## ################################################## ##

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

########################################################################################

########################################################################################



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
linePr=False

# colorPlus

# _.pr( line, plus='cyan' )
# _.pr( line, plus='yellow,cyan', c='cyan' )
# _.pr( line, plus=1, h='chartreuse,cornflower_blue' )
# _.pr( line, plus='cyan',      Plus='list of things to colorize non case specific'.split()      )

def print_(
			*args,
			p=None,
			c=None,
			pad=3,
			g=None,
			end=None,
			pvs=None,
			pv=None,
			json=None,
			dic=None,
			line=None,
			rstrip=True,
			lineMinus=0,
			lineLen=None,
			r=None,
			h=None,
			center=False,
			ShowLine={},
			lineNumber=None,
			flush=False,
			plus=None,
			Plus=None,
		):
	if type(ShowLine) == str:
		ShowLine = { 'line': ShowLine }
	# lineNumber
	if line:
		global linePr
		linePr=True
	if line and type(line) == int and line > 1:
		lineLen = line

	if type(args) == tuple: args = list(args)
	global prStatus
	try:
		prStatus
	except:
		prStatus = True
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
			print(args[0], end=end, flush=flush)
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




		if center:
			if type(center) == int and not center == 1:
				baseLength = center
			else:
				baseLength = __.terminal.width
			length = (baseLength/2)-(len(prn)/2)
			prn = ' '*int(length)+prn
		if rstrip: prn=prn.rstrip()


		if plus:
			# sys.exit()
			plusDone = False
			if not type(plus) == str:
				if h and ',' in h:
					_prn_ = colorList(prn, h=h, v=Plus)
					hh = autoDelim(h)
					h = hh[1]
					plusDone = True
				if not plusDone:
					plus = 'yellow,cyan'
			
			if not plusDone:
				_prn_ = colorList(prn, c=plus, v=Plus)
				plusDone = True
			if not c and not h:
				cc=autoDelim(plus)
				if len(cc) > 1:
					c=cc[1]
			# return _prn_
			# sys.exit()
			
			if prn == _prn_:
				print_(prn, c=c, h=h)
				return prn
			else:
				c=None
			prn = _prn_

		# def showLine( string, plus = '', minus = '',plusOr = False, end=None,isSub=False, OR=None, code=False, itIs=False ):

		if ShowLine:
			if 'line' in ShowLine:
				if not 'plus' in ShowLine: ShowLine['plus'] = ''
				if not 'minus' in ShowLine: ShowLine['minus'] = ''
				if not 'plusOr' in ShowLine: ShowLine['plusOr'] = False
				if not 'end' in ShowLine: ShowLine['end'] = None
				if not 'isSub' in ShowLine: ShowLine['isSub'] = False
				if not 'OR' in ShowLine: ShowLine['OR'] = None
				if not 'code' in ShowLine: ShowLine['code'] = False
				if not 'itIs' in ShowLine: ShowLine['itIs'] = False

				if not showLine( 
						string=ShowLine['line'],
						plus=ShowLine['plus'],
						minus=ShowLine['minus'],
						plusOr=ShowLine['plusOr'],
						end=ShowLine['end'],
						isSub=ShowLine['isSub'],
						OR=ShowLine['OR'],
						code=ShowLine['code'],
						itIs=ShowLine['itIs']
					): return False


		## ShowLine


		## Pre Print End
		if not c is None: prn=cp( prn, c, p=0 )
		if not h is None:
			prn=hexColor( prn, c=h, p=0 )
		if p is None: rint=True
		elif p: rint=True
		elif not p: rint=False
		else: rint=True
		_line__ = ''
		if rint:
			if not end is None:
				if not lineLen is None:
					_line__ = linePrint(txt=' ',p=0,minus=lineMinus)
					print( _line__ , end=end ); print( prn, end=end, flush=flush )
				else:
					_line__ = linePrint(txt=' ',p=0,minus=lineMinus,length=lineLen)
					print( _line__, end=end ); print( prn, end=end, flush=flush )
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
		fo_fi=[];
	if not os.path.isdir(folder): return fo_fi;
	try:
		files=os.listdir(folder)
	except Exception as e:
		return fo_fi
	for item in files:
		path=folder+os.sep+item
		path=__.path(path)
		relative=path[len(fo_rel)+1:]
		__.relative=relative
		if os.path.isfile(path):
			if rel:
				fo_fi.append(relative)
			else:
				fo_fi.append(path)

		if not script is None: script(path);
		if r and os.path.isdir(path): fo(path,r,script,False,rel);
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
		fo_fi=[];
	if not os.path.isdir(folder): return fo_fi;
	try:
		files=os.listdir(folder)
	except Exception as e:
		return fo_fi
	for item in files:
		path=folder+os.sep+item
		path=__.path(path)
		relative=path[len(fo_rel)+1:]
		if os.path.isdir(path):
			if not script is None: script(path);
			if rel:
				fo_fi.append(relative)
			else:
				fo_fi.append(path)
			if r: fos(path,r,script,False,rel);
	return fo_fi


def printt( table, cols=None, sort=None, responsive=None, focus=None,    c=None,s=None,r=None, name='default', fn=None, long=False, l=None, triggers=None, t=None, unique=None, u=None, p=True ):

	if not u is None: unique = u
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
		table = tables.returnSorted( 'backupLog', sort, table )
		# switches.fieldSet( 'Sort', 'active', True )
		# switches.fieldSet( 'Sort', 'value', sort )
		# switches.fieldSet( 'Sort', 'values', sort.split(',') )

	if not cols is None and type(cols) == str:
		new = []
		try:
			if cols.startswith('id,') and not 'id' in table[0]:
				cnt = -1
				for rec in table:
					cnt += 1
					rec['id'] = cnt
					new.append(rec)
				table = new
		except: pass

	def trig(table,triggers):
		new = []
		for rec in table:
			for k in triggers:
				rec[k] = triggers[k](rec[k])
				try:
					pass
				except:
					print('Error:', k, rec)
			new.append(rec)
		return new

	def uniq(table,unique):
		if type(unique) == str:
			while ', ' in unique: unique = unique.replace(', ',',')
			while ' ,' in unique: unique = unique.replace(' ,',',')
			unique = unique.split(',')
		new = []
		spent = {}
		for u in unique:
			spent[u] = []
		for rec in table:
			shouldAdd = True
			for u in unique:
				if rec[u] in spent[u]:
					shouldAdd = False
				spent[u].append(rec[u])
			if shouldAdd:
				new.append(rec)
		return new



	if not unique is None and type(unique) == list: table = uniq(table,unique)

	if not triggers is None and type(triggers) == dict and triggers:
		table = trig(table,triggers)

	if not unique is None and type(unique) == str: table = uniq(table,unique)


	if p:
		tables.register( name, table )
	# for x in dir(tables): print(x)
	# return



	if not fn is None and 'function' in str(type(fn)):
		# _.tables.fieldProfileSet('default','attached','alignment','right')
		fn()
	if cols is None: cols=','.join(list(table[0].keys()))
	if p:
		tables.print( name, cols )
	return table

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


__.tableLine = '‽'
__.tableLine = '\t'
v = dot()
vv = dot()
vv.isData = {}
vv.isDataData = {}
vv.isDataDataRaw = {}
vv.isDataName = {}
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
		if f=='friendly3': return friendlyDate3( epoch );
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

	todo='ago ago-dic ago-txt epoch ordinal text-date text-time text-datetime sdate strip stript stripa date time fdate fdatea cmd month year woy woy2 dow dow2 days tz iso fo friendly friendly3'

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



def saveCryptTable( rows, theFile, db=False, bank=False, index=False, temp=False, free=False, indentCode=True, sort_keys=False, archive=False, p=1, password=None, me=0 ):
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
	if type(stampM) == str:
		stampM = When().parse(stampM)

	# agoThrow

	# if not type(stampM) == int and not type(stampM) == float:
	# 	stampM = ago(stampM)
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
	# agoThrow

	# if not type(stampC) == int and not type(stampC) == float:
	# 	stampC = ago(stampC)
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



def formatIsData( data ):
	global isData_Resolve_Remote
	# os.environ.get('debug', 'no')
	if not isData_Resolve_Remote:
		return data
	if type(data) == str:
			temp = data.split('\n')
			for i,d in enumerate(temp):
				temp[i] = autoUrl(d)
			data = '\n'.join(temp)

	if type(data) == list:
		# print('resolve')
		for i,d in enumerate(data):
			data[i] = autoUrl(d)

	return data
	# autoUrl

def isDataSearch( data=None, focus=None, pipeClean=False, required=False,     r=None, c=None, noclean=None, save=False, resolve=False, R=None ):
	data = isData( data, focus, pipeClean, required, r, c, noclean, save, resolve, R )
	new = []
	for d in data:
		if showLine(d):
			new.append(d)
	return new
def isData_Data(data=None,loc=None):
	global isDataZero
	if data==2:data=[]
	if isDataZero and not data: return []
	# if not loc is None: print_( 'isData_Data', loc )
	# if not loc is None: print_( 'isData_Data, start', loc, data, 'isData_Data, end' )
	if not __.appReg in AutoClipboardApps:
		return formatIsData(data)
	# print('data', data); sys.exit(0)
	# if type(data) != list:data = []
	if not data:
		return formatIsData(getClip().split('\n'))
	return formatIsData(data)

isData_Resolve_Remote = False
isDataZero = False
def isData( data=None, focus=None, pipeClean=False, required=False,     r=None, c=None, noclean=None, save=False, resolve=False, R=None ):
	testingI = False
	global isDataZero
	if data == 0:
		isDataZero = True
		data=2
	
	global isData_Save
	global urlPipeActivated
	global appData
	global isData_Resolve_Remote
	
	if not R is None: resolve = R
	if not resolve is None: isData_Resolve_Remote = resolve

	if testingI: print(11)

	if urlPipeActivated and appData[__.appReg]['pipe']:
		return appData[__.appReg]['pipe']


	if testingI: print(22)

	items_to_check = ['--r']
	if any(item in sys.argv for item in items_to_check):
		isData_Resolve_Remote = True
	if __.PIPE and data == 2:
		return isData_Data(__.PIPE)
	elif data == 2:
		data = None
	if testingI: print(33)
	if save:
		isData_Save = data
		return isData_Data(data,2.111)

	if testingI: print(44)

	if isData_Save:
		return isData_Data(isData_Save,2.222)
	
	global switches
	if switches.isActive('Paste-isData'):
		_paste = regImp( __.appReg, '-paste' )
		return isData_Data(_paste.imp.paste().split('\n'))
	
	if testingI: print(55)
	
	if __.ForcePipe:
		return isData_Data(__.ForcePipe)

	if testingI: print(66)

	if vv.isDataData:
		for name in vv.isDataData:
			return isData_Data(vv.isDataData[name],2.444)
	
	if testingI: print(77)
	
	if vv.isDataName:
		for name in vv.isDataName:
			return isData_Data(vv.isDataName[name],2.333)
	if vv.isDataDataRaw:
		for name in vv.isDataDataRaw:
			return isData_Data(vv.isDataDataRaw[name],2.411)


	
	# if '...' in sys.argv:
	if __.PIPE: appData[__.appReg]['pipe'] = __.PIPE


	global FilesFiles
	FilesFiles = myFileLocation_Files
	__.FilesFiles = myFileLocation_Files
	# global switches
	try:
		if appData[__.appReg]['pipe']: return isData_Data(appData[__.appReg]['pipe'])
		for sw in __.isData_Switches:
			if not sw == 'Files': return isData_Data(switches.values(sw))
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
		elif data is None and switches.isActive('Paste-isData'): return isData_Data(getClip().split('\n'))


		def _isData_(tst):
			global myFileLocation_Files
			# if not tst and pipe_surfing(): tst = pipe_surfing()
			if not tst: return isData_Data(myFileLocation_Files,2.555)
			# print(tst,myFileLocation_Files)


			
			for name in vv.isData:
				if len(switches.values(name)):
					if 'data' in vv.isData[name]: return isData_Data(tst,2.666)

			if myFileLocation_Files and os.path.isfile(myFileLocation_Files[0]): return myFileLocation_Files

			return isData_Data(tst,2.777)
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
									for xXx in getText( f, raw = True ).split('\n'):
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
	except: e('Data src missing','possibly: -f')

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
def resolve(path,isFolder=None):
	if type(path) == list:
		for i,p in enumerate(path):
			path[i] = resolve(p)
		return path

	if not os.path.exists(path):
		path = autoUrl(path)


	if isFolder:
		if not os.path.exists(path): path = aliasesFo(path)
	elif not isFolder:
		if not os.path.exists(path): path = aliasesFi(path)
	# if not os.path.exists(path):
	# 	path = inRelevantFolderSearch(path)
	# if not os.path.exists(path):
	# 	path = inRecentFolders( path )
	return path

remoteFolders_sftp = None

def autoUrl(path):
	if type(path) == list:
		for i,p in enumerate(path):
			path[i] = autoUrl(p)
	
	if type(path) == str:
		if path.startswith('http:') or path.startswith('https:') or path.startswith('/') or path.startswith('\\'):
			test = url2file(path)
			if test and os.path.exists(test):
				return test
	return path
def myFolderLocations( data ):
	data = autoUrl(data)

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



def colorPlus( data, c=None, h=None ):
	color = c
	if color is None and h is None:
		color = 'green'
	if ' ' in color or ',' in color:
		return colorList( data, color=color )
	for search in switches.values('Plus'):
		for subject in caseUnspecific( data, search, isPlus=True ):
			# print('subject:', subject)

			if type( subject ) == str:
				# print('subject:', subject, colorThis( subject, color, p=0 ))
				data = data.replace( subject, pr( subject, c=color, p=0 ) )
			else:
				if subject['pos'] == 'first':
					data = nth_repl(data, subject['data'], pr( subject['data'], c=color, p=0 ), 1)
				else:
					cx = data.count( subject['data'] )
					data = nth_repl(data, subject['data'], pr( subject['data'], c=color, p=0 ), cx)
	return data

def autoDelim(data,d=',', alt=' |'):
	if not type(data) == str:
		return []
	for a in list(alt):
		if a in data:
			data = data.replace(a, d)
	while d+d in data:
		data = data.replace(d+d, d)

	items = data.split(d)
	return items



def ws_edges3(s): # whitespace edges, including text
	import re
	match = re.match(r'^(\s*)(.*?)(\s*)$', s)
	if match:
		return (match.group(1), match.group(2), match.group(3))
	return ('', s, '')

def ws_edges2(s): # whitespace edges
	import re
	match = re.match(r'^(\s*)(.*?)(\s*)$', s)
	if match:
		return (match.group(1), match.group(3))
	return ('', '')

# colorPlus2
def colorList( data, c=None, h=None, v=None, l=None,  delim='3e05a45efd9f' ):
	if not c is None: color = c
	if c:
		colors = autoDelim(c)
		c = colors[0]
	if h:
		colors = autoDelim(h)
		h = colors[0]

	if not l is None: v = l
	
	if not v is None:
		values = v
	else:
		values = switches.values('Plus')

	# if len(colors) == 1: return colorPlus( data, color=color )
	
	for search in values:
		for subject in caseUnspecific( data, search, isPlus=True ):
			# print('subject:', subject)

			if type( subject ) == str:
				# data = data.replace( subject, delim+ pr( subject, c=c, h=h, p=0 )+delim )

				c = delim+ pr( subject, c=c, h=h, p=0 )+delim
				r = data.split( subject )
				data = c.join( r )

			else:
				if subject['pos'] == 'first':
					data = nth_repl(data, subject['data'], delim+ pr( subject['data'], c=c, h=h, p=0 )+delim, 1)
				else:
					cx = data.count( subject['data'] )
					data = nth_repl(data, subject['data'], delim+ pr( subject['data'], c=c, h=h, p=0 )+delim, cx)
	# print('here')
	if len(colors) == 1:
		return data.replace(delim,'')
	elif not delim in data:
		return data
	else:
		# print('here')
		parts = data.split(delim)
		new = ''
		for i, part in enumerate(parts):
			if i % 2 == 0:
				ws = ws_edges3(part)
				part = ws[1]
				if c:
					new += ws[0] + pr( part, c=colors[1], p=0 ) + ws[2]
				elif h:
					new += ws[0] + pr( part, h=colors[1], p=0 ) + ws[2]
			else:
				new += part
				pass
		return new

	return data



def plusColor( row, color='green' ):
	# row = thePrintLine

	if switches.isActive('Plus'):
		thePrintLine = row
		for plusSearchX in switches.values('Plus'):
			plusSearchX = ci( plusSearchX )

			for subject in caseUnspecific( row, plusSearchX ):
				# row = thePrintLine.replace( subject, colorThis( subject, color , p=0 )  )
				c = colorThis( subject, color , p=0 )
				r = row.split( subject )
				row = c.join( r )

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
	print_()
	print_(line=1,c='cyan')
	print_()
	Pallet(cls=False)

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


	# 67f977e5-3680-800a-9527-67a80cbaf38c
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
		reclaimAcquiredData( appDBA, epoch, theFocus )
	else:
		releaseAcquiredData( appDBA, theFocus )

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


def inRecentFolders( item ):
	if os.path.exist(item):
		return item
	log = _v.tt+os.sep+'BookmarksBySession'+os.sep+_v.session()+'.log'
	recent = getText(log,raw=True,clean=2).split('\n')
	for line in recent:
		if os.path.exists(line+os.sep+item):
			pr('Found in recent folder: '+line+os.sep+item,c='Background.green')
			return line+os.sep+item
	return item

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

def HELP(topic):
	"""
	Print the full path to a help file within _base3/help/.

	Example:
		HELP('pipeCleaner')  # -> D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_base3\\help\\pipeCleaner.py
	"""
	base_path = os.path.dirname(__file__)  # points to _base3 directory
	help_path = os.path.join(base_path, 'help', f'{topic}.py')
	print(help_path)
	return help_path


__.setting('pipe-cleaner', {
	'first': True,      # Clean first character if not safe
	'trim': True,       # Strip spaces (left and right)
	'deep': True,       # Strip \r \n \t
	'multi': 3,         # Repeat deep cleaning n times
	'skip': []          # List of indices to skip cleaning
})

def pipeCleaner(clean=0):
	settings = __.setting('pipe-cleaner')

	if isinstance(settings, bool):
		if not settings:
			return None
		settings = {}

	# Ensure all expected keys exist
	settings.setdefault('first', True)
	settings.setdefault('trim', True)
	settings.setdefault('deep', True)
	settings.setdefault('multi', 1)
	settings.setdefault('skip', [])

	if isinstance(clean, bool):
		clean = settings

	if 'clean-pipe' in l.v.cnf.data and not l.conf('clean-pipe'):
		return

	def pipeCleanerDeep(p):
		for _ in range(settings['multi']):
			p = p.strip(' \t\r\n')
		return p

	global appData
	try:
		if settings['first']:
			if appData[__.appReg]['pipe'] and appData[__.appReg]['pipe'][0]:
				first_char = appData[__.appReg]['pipe'][0][0]
				if first_char not in _str.safeChar and first_char not in _str.safe:
					appData[__.appReg]['pipe'][0] = appData[__.appReg]['pipe'][0][1:]
	except Exception as e:
		pass

	try:
		for i, pipeData in enumerate(appData[__.appReg]['pipe']):
			if i in settings['skip']:
				continue

			p = pipeData.replace('\n', '')

			if clean and settings['trim']:
				p = p.strip()

			if clean and settings['deep']:
				p = pipeCleanerDeep(p)

			appData[__.appReg]['pipe'][i] = p
	except Exception as e:
		pass

	return appData[__.appReg]['pipe']



def pipeCleaner_______Original(clean=0):
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
		import simplejson
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
def printVarSimpleFake2( data, noWords=False ):
	# this sucks, new class with centralized database of indices and single run colorization coming soon
	import re
	arguments=[]
	def has_alphanumeric_around_equal(s):
		for i in range(1, len(s) - 1):
			if s[i] == '=' and s[i - 1].isalnum() and s[i + 1].isalnum():
				return True
		return False
	# def colorize_quotes(s, quote_color='darkcyan', content_color='cyan'):
	def show_ansi_codes(s): return s.replace('\033', '\\033')
	def colorize_quotes(s, quote_color='darkcyan', content_color='yellow'):
		# s = re.sub(r'\\033\[\d*\\033\[\d*m', 'm', s)
		# Strip out the broken color codes
		s = re.sub(r'\033\[\d+m', '', s)

		# Colorize the function name
		s = re.sub(r'\b(TABLE_PUT)\b', Color.cyan + r'\1' + Color.end, s)

		# Colorize the quotes and their content
		s = colorize_quotes2(s,quote_color,content_color)

		return s
	def colorize_quotes2(s, quote_color='darkcyan', content_color='yellow'):
		# Pattern to match content inside single or double quotes
		pattern = r"(['\"])(.*?)(?<!\\033)\1"

		# Calculating offsets due to insertion of color codes
		offset = 0

		for match in re.finditer(pattern, s):
			start_quote = match.start(1) + offset
			end_quote = start_quote + len(match.group(1))

			start_content = match.start(2) + offset
			end_content = start_content + len(match.group(2))

			# Colorizing content inside the quote
			s = s[:start_content] + eval(f"Color.{content_color}") + s[start_content:end_content] + Color.end + s[end_content:]
			offset += len(Color.end) + len(eval(f"Color.{content_color}"))

			# Colorizing the starting quote
			s = s[:start_quote] + eval(f"Color.{quote_color}") + s[start_quote:end_quote] + Color.end + s[end_quote:]
			offset += len(Color.end) + len(eval(f"Color.{quote_color}"))

			# Colorizing the ending quote
			end_quote = match.end(2) + offset
			s = s[:end_quote] + eval(f"Color.{quote_color}") + s[end_quote:end_quote + len(match.group(1))] + Color.end + s[end_quote + len(match.group(1)):]
			offset += len(Color.end) + len(eval(f"Color.{quote_color}"))

		return s




	# def colorize_quotes(s, quote_color='darkcyan', content_color='cyan'):
	# 	# Pattern to match content inside single or double quotes
	# 	pattern = r"(['\"])(.*?)\1"

	# 	offset = 0
	# 	for match in re.finditer(pattern, s):
	# 		start_quote = match.start(1) + offset
	# 		end_quote = start_quote + len(match.group(1))

	# 		start_content = match.start(2) + offset
	# 		end_content = start_content + len(match.group(2))

	# 		# Colorizing content inside the quote
	# 		s = s[:start_content] + eval(f"Color.{content_color}") + s[start_content:end_content] + Color.end + s[end_content:]
	# 		offset += len(Color.end) + len(eval(f"Color.{content_color}"))

	# 		# Colorizing the starting quote
	# 		s = s[:start_quote] + eval(f"Color.{quote_color}") + s[start_quote:end_quote] + Color.end + s[end_quote:]
	# 		offset += len(Color.end) + len(eval(f"Color.{quote_color}"))

	# 		# Colorizing the ending quote
	# 		end_quote = match.end(2) + offset
	# 		s = s[:end_quote] + eval(f"Color.{quote_color}") + s[end_quote:end_quote + len(match.group(1))] + Color.end + s[end_quote + len(match.group(1)):]
	# 		offset += len(Color.end) + len(eval(f"Color.{quote_color}"))

	# 	return s
	def find_all_function_names(s):
		pattern = r'\b[A-Za-z]\w*(?=\()'
		matches = [m for m in re.finditer(pattern, s)]

		indices = []
		for match in matches:
			start = match.start()
			end = match.end() - 1
			indices.append((start, end))

		return indices

	def find_arguments(s):
		pattern = r'\(([^)]*)\)'
		matches = list(re.finditer(pattern, s))
		all_indices = []

		for match in matches:
			args_str = match.group(1)
			split_indices = [0] + [m.end() for m in re.finditer(r'(?<!["\']),', args_str)]
			arg_strings = [args_str[i:j] for i, j in zip(split_indices, split_indices[1:] + [None])]

			start_index = match.start(1)
			indices = [(start_index + i, start_index + i + len(arg) - 1) for i, arg in enumerate(arg_strings)]
			all_indices.extend(indices)

		return all_indices
	def find_arguments_words(s):
		pattern = r'\(([^)]*)\)'
		matches = list(re.finditer(pattern, s))
		all_args = []

		for match in matches:
			args_str = match.group(1)
			split_indices = [0] + [m.end() for m in re.finditer(r'(?<!["\']),', args_str)]
			arg_strings = [args_str[i:j].strip() for i, j in zip(split_indices, split_indices[1:] + [None])]

			for arg in arg_strings:
				if not arg.startswith('"') and not arg.startswith("'"):
					all_args.append(arg)

		return all_args

	def colorize_indices(s, indices, color):
		if not indices:
			return s

		if not isinstance(indices, list):
			indices = [indices]

		offset = 0
		for start, end in indices:
			try:
				colored_string = eval('Color.' + color + '+ s[start+offset:end+offset+1] + Color.end')
			except Exception:
				continue

			s = s[:start+offset] + colored_string + s[end+offset+1:]
			offset += len(colored_string) - (end - start + 1)
		return s
	def colorize_chars(result, dic):
		i = 0
		while i < len(result):
			# Detect if current section is an ANSI color code and skip it
			if result[i:i+2] == '\\033':
				color_code_end = result.find('m', i)
				i = color_code_end + 1
				continue

			# Check if the character matches any in the dictionary keys and colorize it
			for k, color in dic.items():
				if result[i] in k:
					result = result[:i] + eval('Color.' + color) + result[i] + Color.end + result[i+1:]
					i += len(eval('Color.' + color)) + len(Color.end) # We have to adjust i to account for the new color sequences added
					break
			i += 1

		return result



	# def colorize_chars(result, dic):
	#   i = 0
	#   output = []
	#   while i < len(result):
	#       # Detect if current section is an ANSI color code and skip it
	#       if result[i:i+2] == '\\033':
	#           color_code_end = result.find('m', i)
	#           output.append(result[i:color_code_end+1])
	#           i = color_code_end + 1
	#           continue

	#       # Check if the character matches any in the dictionary keys and colorize it
	#       colorized = False
	#       for k, color in dic.items():
	#           if result[i] in k:
	#               output.append(eval('Color.' + color) + result[i] + Color.end)
	#               colorized = True
	#               break

	#       # If not colorized, just append the original character
	#       if not colorized:
	#           output.append(result[i])

	#       i += 1

	#   return ''.join(output)
	def colorize_words(result, dic):
		i = 0
		while i < len(result):
			# Detect if current section is an ANSI color code and skip it
			if result[i:i+2] == '\\033':
				color_code_end = result.find('m', i)
				i = color_code_end + 1
				continue

			matched = False
			for word, color in dic.items():
				# If the word is a variable name, ensure that it stands alone by using word boundaries (\b).
				pattern = rf'\b{re.escape(word)}\b' if word.isidentifier() else re.escape(word)
				match = re.search(pattern, result[i:])
				if match:
					matched_text = match.group(0)
					colored_text = eval(f"Color.{color}") + matched_text + Color.end
					result = result[:i + match.start()] + colored_text + result[i + match.end():]
					i += len(colored_text)
					matched = True
					break

			if not matched:
				i += 1

		words = {
			'def': 'cornflower_blue',
			'return': 'chartreuse',
			'while': 'dark_salmon',
			'import': 'light_sea_green',
			'True': 'fuchsia',
			'False': 'fuchsia',
			'None': 'dark_orchid',
		}
		if not noWords:
			for word, color in words.items():
				result = result.replace(word, pr(word,h=color,p=0))
		
		return result

	def find_argument_usage(s, color='CYAN'):
		# Extract arguments from the function description section
		args_match = re.search(r'Usage.*?\(([^)]*)\)', s, re.DOTALL)
		if not args_match:
			return s

		args_str = args_match.group(1)
		arguments = [arg.strip() for arg in re.split(r'(?<!["\']),', args_str)]

		i = 0
		while i < len(s):
			# If current section is an ANSI color code, skip it
			if s[i:i+2] == '\\033':
				color_code_end = s.find('m', i)
				i = color_code_end + 1
				continue

			# Check for standalone word match
			found = False
			for arg in arguments:
				pattern = rf'(?<=[\s(])({re.escape(arg)})(?=[\s,).])'
				match = re.search(pattern, s[i:])
				if match:
					matched_text = match.group(1)
					colored_text = eval(f"Color.{color}") + matched_text + Color.end
					s = s[:match.start()+i] + colored_text + s[match.end()+i:]
					i += len(colored_text)
					found = True
					break

			if not found:
				i += 1

		return s
	variables=[]
	clean=[]
	for line in data.split('\n'):
		if '=' in line and has_alphanumeric_around_equal(line):
			# print(line);sys.exit();
			line=line.replace('=',' = ')
		clean.append(line)
	result = '\n'.join(clean)
	# result=data
	arguments=find_arguments_words(result)
	dic = {
		'[]': 'purple',
	}
	for line in result.split('\n'):
		if ' = ' in line:
			variables.append(line.split(' = ')[0].strip())
	# print(result);sys.exit();
	# result = printVarColor_OLD( result )
	result = colorize_indices(result, find_all_function_names(result), 'cyan')
	result = colorize_indices(result, find_arguments(result), 'darkcyan')
	result = colorize_chars(result,dic)
	# del colorama

	result = colorize_quotes(result)
	result = find_argument_usage(result,'darkcyan')
	dic = {
		'!': 'yellow',
		'(){}': 'purple',
		'-=/': 'red',
	}
	result = colorize_chars(result,dic)
	dic = {
		'RETURN': 'blue',
		'IF': 'purple',
		'THEN': 'purple',
		'ELSE': 'purple',
	}
	spentV=[]
	spentA=[]
	for v in variables:
		v=v.strip()
		if v in spentV: continue
		spentV.append(v)
		if v in arguments:
			dic[' '+v+' ']='darkcyan'
			dic['\n'+v+' ']='darkcyan'
		else:
			dic['\n'+v+' ']='green'
			dic[' '+v+' ']='green'
	for v in arguments:
		if v in spentA: continue
		spentA.append(v)
		dic[' '+v+' ']='darkcyan'
		dic['\n'+v+' ']='darkcyan'
	# print(variables)
	# print(arguments)
	result = colorize_words(result,dic)
	# print(show_ansi_codes(result));sys.exit();
	# print_( re.sub(r'\\033\[0\\033\[36mm', 'm', result) )
	# print_( re.sub(r'\033\[\d+m', '', result) )
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


def printVarColor( data, p=True ):
	_code = regImp( __.appReg, '_rightThumb._auditCodeBase' )
	validator = _code.imp.Validator()

	# index = validator.createIndex( data, 'javascript' )
	# validator.colorPrint_old()
	# print_(data)
	index = validator.createIndex( data, 'javascript', skipLoad=True, simple=False, A=None, B=True, C=None )
	# printVarSimple(validator.identity)
	# index = validator.createIndex( data, 'javascript', simple=False, B=True )
	return validator.colorPrint(p)

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
	file = aliases_file_open(path)
	global appData
	global myFileLocation_Files
	if __.myFileLocations_SKIP_VALIDATION:
		if type( appData[__.appReg]['pipe'] ) == bool:
			appData[__.appReg]['pipe'] = []
		# if isFirst:
		# 	isFirst=False
		# else:
		# 	appData[__.appReg]['pipe'].append( path )
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


def remote2filePathBuild():
	global remoteFolders_sftp
	if not remoteFolders_sftp is None: return remoteFolders_sftp
	remoteFolders_sftp = []
	sites = getTable('site-locations.list')

	for mPath in sites:
		if not os.path.isfile(mPath):
			continue
		raw = getText(mPath, raw=True).strip()
		meta = getTable2(mPath) if raw.startswith('{') else getYML(mPath)

		if 'sftp' in meta and 'path' in meta['sftp']:
			remote_base = meta['sftp']['path'].replace('\\', '/').rstrip('/')
			remoteFolders_sftp.append(remote_base)


def remote2file(path):
	remote_path = path
	remote_path = remote_path.replace('\\', '/')
	if not remote_path.startswith('/'):
		return path
	
	remoteFolders_sftp = remote2filePathBuild()

	if not any(folder in path for folder in remoteFolders_sftp):
		return path
	return 'error'
	sites = getTable('site-locations.list')

	for mPath in sites:
		if not os.path.isfile(mPath):
			continue

		local_base = __.path(mPath, pop=True)
		raw = getText(mPath, raw=True).strip()
		meta = getTable2(mPath) if raw.startswith('{') else getYML(mPath)

		if 'sftp' in meta and 'path' in meta['sftp']:
			remote_base = meta['sftp']['path'].replace('\\', '/').rstrip('/')
			if remote_path.startswith(remote_base):
				relative_path = remote_path[len(remote_base):].lstrip('/')
				local_full = os.path.join(local_base, *relative_path.split('/'))
				test = os.path.normpath(local_full)
				if os.path.exists(test):
					return os.path.normpath(local_full)

	return None


def url2file(path):
	# test = remote2file(path)
	if os.path.exists(path):
		return path
	if path.startswith('/'):
		try:
			test = remote2file(path)
			if os.path.exists(test):
				return test
			else:
				return path
		except:
			return path
		# print('remote2file',test)
		# sys.exit(0)
			
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
						if os.path.exists(y):
							path=y
	return path

# import os

def getExtension(path):
	"""
	Returns the file extension from a full path or filename.
	If there is no extension, returns an empty string.
	"""

	global EXT
	if EXT:
		return EXT

	if type(path) == list:
		for p in path:
			if os.path.isfile(p):
				EXT = os.path.splitext(p)[1].replace('.', '').strip()
				return EXT 
	try:
		EXT = os.path.splitext(path)[1].replace('.', '').strip()
		return EXT
	except:
		return ''

def setLanguage(path):
	global EXT
	EXT = getExtension(path)
	if EXT:
		__.language = EXT
	return EXT
getEXT = getExtension
getExt = getExtension
EXT = None
isFirst=True
def myFileLocations( file, silent=False, currentBaseVersion=3 ):
	# if '*' in file:
	# 	import glob
	# 	file = glob.glob("*.txt")
	if type(file) == str:
		if not os.path.exists(file):
			file = aliasesFi(file)

		if os.path.exists(file):
			file = __.path(file)
	if True:
		# ext = setLanguage(file) # 2025-08-13
		# print(ext)
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

	# file=autoUrl(file)
	# file = aliases_file_open(file)
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
		# if isFirst:
		# 	isFirst=False
		# else:
		# 	appData[__.appReg]['pipe'].append( file )
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
	# try:
	# 	autoAbbreviations()
	# except Exception as e:
	# 	pass
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
						# if isFirst:
						# 	isFirst=False
						# else:
						# 	appData[__.appReg]['pipe'].append( thisFile )
						if not type(appData[__.appReg]['pipe']) == list: appData[__.appReg]['pipe'] = []
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
									# print('isFirst',isFirst)
									# if isFirst:
									# 	isFirst=False
									# else:
									appData[__.appReg]['pipe'].append( row )
									# tmpFiles.append( row )
							else:
								if type(appData[__.appReg]['pipe']) == bool: appData[__.appReg]['pipe'] = []
								for row in getText( thisFile, raw=True ).split('\n'):
									# if isFirst:
									# 	isFirst=False
									# else:
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
						# if isFirst:
						# 	isFirst=False
						# else:
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
	
	# agoThrow
	try:
		if len(theDate) < 4:
			theDate = ago( theDate )
	except:
		pass
	
	return autoDateRun( theDate )

def autoDateRun( theDate ):
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
	if rows is None:
		err('Error: data is None')
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
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
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
			if raw:
				return ''
			elif not raw:
				return []
			# return None
		print_('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( _v.slash+'n', '\n' )

		if clean:
			# print('pre',txt.split('\n')[0])
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
			# print('post',txt.split('\n')[0])
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		# print('final',txt.split('\n')[0])
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







showLine_list = []
showLineC = False
sl = False
hasPlus=None
switch_dict = {}
switch_dict_set=False
LINE = None
showLine2 = False
showLine_Run={}

# _.pr( line, plus='cyan' )
# _.pr( line, plus='yellow,cyan', c='cyan' )
# _.pr( line, plus=1, h='chartreuse,cornflower_blue' )

def ValidLine(string, has=None, omit=None, Any=None, caseStrict=None,        strict=None, Case=None):
	global switches

	if not Case is None: caseStrict = Case
	if not strict is None: caseStrict = strict


	if has is None: has = switches.value('Plus')
	if omit is None: omit = switches.value('Minus')
	if Any is None: Any = switches.value('PlusOr')
	if caseStrict is None: caseStrict = switches.value('StrictCase')


	has = has or []
	omit = omit or []
	
	# Handle case sensitivity
	if not caseStrict:
		string = string.lower()
		has = [h.lower() for h in has]
		omit = [o.lower() for o in omit]
	
	# If omit list contains any matches, fail immediately
	if any(o in string for o in omit):
		return False
	
	# Check for presence based on Any flag
	if Any:
		return any(h in string for h in has) if has else True
	else:
		return all(h in string for h in has) if has else True


def validLine(string, has=None, omit=None, Any=False, caseStrict=False,        strict=None, Case=None):
	if not Case is None: caseStrict = Case
	if not strict is None: caseStrict = strict
	has = has or []
	omit = omit or []
	
	# Handle case sensitivity
	if not caseStrict:
		string = string.lower()
		has = [h.lower() for h in has]
		omit = [o.lower() for o in omit]
	
	# If omit list contains any matches, fail immediately
	if any(o in string for o in omit):
		return False
	
	# Check for presence based on Any flag
	if Any:
		return any(h in string for h in has) if has else True
	else:
		return all(h in string for h in has) if has else True


def showLine(string, plus='', minus='', plusOr=False, end=None, isSub=False, OR=None, code=False, itIs=False, c=False, run=0):
	""" This function wraps the show method in the Line class and dynamically creates the switch_dict. """
	# print(run,string)
	global switches
	global switch_dict
	global switch_dict_set
	global LINE
	global showLine2
	global showLine_Run
	
	defaults = {
		'plus': '',
		'minus': '',
		'plusOr': False,
		'end': None,
		'isSub': False,
		'OR': None,
		'code': False,
		'itIs': False,
		'c': False
	}


	# Create a dictionary of arguments, only including ones that are not their default value
	def createSwitchDict(theArgs):
		global switches
		global switch_dict
		global switch_dict_set
		global LINE
		global showLine2
		global showLine_Run
		valid_args = ['plus', 'minus', 'plusOr', 'end', 'isSub', 'OR', 'code', 'itIs', 'c']
		
		for arg in valid_args:
			# value = locals().get(arg)
			value = theArgs.get(arg, None)
			# if arg == 'minus':
				# print(run,arg, value)
			if value not in ['', None, False]:  # Check if the value is not default
				# print('arg', arg, value	)
				if not type(switch_dict) == dict:
					switch_dict = {}
				# print(arg,value)
				switch_dict[arg] = value
		
		# If all values are default, set switch_dict to None
		if not switch_dict:
			switch_dict = None
		if not LINE is None:
			LINE.register(switch_dict)
		switch_dict_set = True
		showLine_Run[run] = switch_dict

	valid_args = ['plus', 'minus', 'plusOr', 'end', 'isSub', 'OR', 'code', 'itIs', 'c']
	theArgs = {}
	for arg in valid_args:
		value = locals().get(arg)
		theArgs[arg] = value

	if not switch_dict_set or len(plus): createSwitchDict(theArgs)
	if showLine2:
		if run in showLine_Run:
			switch_dict = showLine_Run[run]
		else:
			createSwitchDict(theArgs)


		# Debugging: Check what switch_dict contains
		# print("switch_dict:", switch_dict)
		
		# Call the show method in Line with the dynamically populated switch_dict
	# if LINE is None:
	LINE = __.Line(switches, switch_dict, run)
	# print(string)
	return LINE.show(string)


	ogString = string
	global showLineC
	global showLine_list
	showLineC = False
	# <2024-04-02>
	string = str(string)
	string = string.strip()
	# </2024-04-02>


	'''showLine( string, plus = '', minus = '',plusOr = False, end=None,isSub=False, OR=None, code=False )'''




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


	if result and c:
		# print(showLine_list)
		showLineC = ogString
		for by in showLine_list:
			# print(by)
			showLineC = prWC2(showLineC,by)
			# print(showLineC)
	global sl
	sl = showLineC
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
	string = string.replace('[',' [')
	# __.sw.PlusCode
	global showLine_list

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
	showLine_list = plusInput




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
	global showLine_list
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
	showLine_list = plusInput
	# print('here',showLine_list)
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

	_v.mkdir(file0,f=1)
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
	global switches
	if '--src' in sys.argv: print(1, __.appReg, theFile)
	if switches.isActive('Timeout') and 'table' in switches.value('Timeout'):
		print(theFile)
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
	theFile = file0
	# Check if the file is empty
	if os.path.isfile(theFile) and os.path.getsize(theFile) > 0:
		try:

			text = getText(theFile, raw=True)
			text=text.strip()
			
			if text.startswith('[') or text.startswith('{'):
				try:
					return json.loads(text)
				except:
					try:
						return json.loads(text[:-1])
					except:
						e('Error loading JSON file:', theFile,'jq . broken.json > fixed.json')

			else:
				return fromYML(text)
		except:
			try:
				with open(theFile, 'r', encoding='utf-8') as json_file:
					try:
						json_data = simplejson.load(json_file)
					except Exception as e:
						json_data = json.load(json_file)
					return json_data
			except Exception as e:
				print('Error loading JSON file:', theFile, e)
				sys.exit()
	else:
		# print(f"File {theFile} not found or is empty.")
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
	if '--src' in sys.argv:
		import inspect
		stack = inspect.stack()
		caller_frame = stack[1]  # [0] is current function, [1] is the caller
		print(f"Called from function: {caller_frame.function}")
		print(f"In file: {caller_frame.filename}, line {caller_frame.lineno}")

		print(2, __.appReg, theFile)
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

			text = getText(theFile, raw=True)
			if text.startswith('[') or text.startswith('{'):
				return json.loads(text)
			else:
				return fromYML(text)
		except:
			try:
				with open(theFile, 'r', encoding='utf-8') as json_file:
					try:
						json_data = simplejson.load(json_file)
					except Exception as e:
						json_data = json.load(json_file)
					return json_data
			except Exception as e:
				print('Error loading JSON file:', theFile, e)
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
	# decompress2x(theFile)
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

class Switch:

	def __init__(self, name, switch, example_or_notes, description, space, default, group):
		self.appReg = __.appReg
		self.name = name
		self.switch = switch
		self.default = default
		self.group = group
		self.pos = 0
		self.active = False
		self.value = None
		self.values = []
		self.example_or_notes = example_or_notes
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
		self.resolve = {}


	def dic( self, simple=False ):
		recs = self.all()
		result = {}
		for rec in recs:
			if rec['active']:
				if rec['name'] == 'DumpSwitches': continue
				if rec['values']:
					result[rec['name']] = rec['values']
					if simple and len(rec['values']) <2:
						result[rec['name']] = rec['value']
				elif not rec['values']:
					result[rec['name']] = '_'

		return result


	def all( self, app=True, appReg=None, omit=None, omitDefaults=True,             od=1 ):
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
		# print( 'appReg:', appReg )
		result = []
		for i,row in enumerate(self.switches):
			# pv(row)
			if not row.name in omitList:
				if row.active:
					shouldAdd = True
					if appReg == '__init__':
						appReg = row.appReg
					# print(row.appReg)
					if app:
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
		#   cnt=0
		#   for i, rec in result:



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
		longActive = False
		if self.isActive('Long'):
			longActive = True
		self.fieldSet('Long','active',True)
		data = []
		spent = {}
		for i,row in enumerate(self.switches):
			# if not row.value is None:
			if not row.appReg in spent:
				spent[row.appReg] = []
				if not longActive:
					spent[row.appReg].append( 'Long' )
					spent[row.appReg].append( 'DumpSwitches' )
			if row.name in spent[row.appReg]:
				continue
			if includeBlank:
				data.append({ 'name': row.name, 'value': row.value.replace(',', '\t'), 'appreg': row.appReg })
				spent[row.appReg].append( row.name )
			else:
				if not row.value is None or row.active:
					data.append({ 'name': row.name, 'value': row.value.replace(',', '\t'), 'appreg': row.appReg })
					spent[row.appReg].append( row.name )
			# print_(row.name,'\t',row.value,'\t',row.appReg)
		tables.register('data',data)
		tables.print('data','appreg,name,value')

	def register(self, name, switch, example_or_notes = None, isRequired=False, isPipe=None, isData=None, description='', space=False, default=False, group=None, g=None, resolve=None):
		if type(switch) == str:
			switch = switch.replace( ' ', '' )
		if not g is None:
			group = g

		if not resolve is None:
			if not type(resolve) == str:
				resolve = 'file'
			if 'fo' in resolve.lower():
				self.resolve[name] = 'folder'
			else:
				self.resolve[name] = 'file'

		if not isPipe is None:
			__.trigger_isPipe = isPipe

		if not isData is None:
			__.trigger_isPipe = isData
			isPipe=isData
			if False: pass
			elif 'data' in isData and 'raw' in isData:
				# print('here')
				vv.isDataDataRaw[name] = ''
			elif 'data' in isData and not 'raw' in isData:
				vv.isDataData[name] = []
			elif isData == 'name':
				vv.isDataName[name] = []
		i=len(self.switches)



		if not __.appReg in self.dex:
			self.dex[__.appReg]={}
		self.dex[__.appReg][name]=i

		self.switches.append(Switch(name, switch, example_or_notes, description, space, default, group))

		try:
			if not type(self.isRequired[__.appReg]) == list:
				self.isRequired[__.appReg] = []
		except Exception as e:
			self.isRequired[__.appReg] = []



		switch = switch.replace( ' ', '' )


		if not isPipe is None:
			__.isData_Switches[name]=isPipe
			if type(isPipe) == bool and isPipe:
				isPipe = 'data'
			vv.isData[name]=isPipe
			isPipe=isPipe.replace('raw','name')
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



	def fieldSet2( self, name, column, value, theFocus=False, runTrigger=True ):
		if name in self.resolve:
			if column in 'value values'.split():
				isFolder = True if self.resolve[name] == 'folder' else False
				if type(value) == str:
					value = resolve(value, isFolder)
				if type(value) == list and len(value) > 0 and type(value[0]) == str:
					for i,v in enumerate(value):
						value[i] = resolve(v, isFolder)
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
						self.switches[i].values = [value]
						self.switches[i].value = value
	def field( self, name, column, value, theFocus=False, runTrigger=True ):
		return self.fieldSet( name, column, value, theFocus, runTrigger )


	def Add( self, name, value ):
		for i,row in enumerate(self.switches):
			if row.name == name:
				self.switches[i].active = True
				if not type(self.switches[i].values) == list:
					self.switches[i].values = []
				self.switches[i].values.append( value )
				self.switches[i].value = ','.join(self.switches[i].values)
				



	def set( self, name, column, value, theFocus=False, runTrigger=True ):
		return self.fieldSet( name, column, value, theFocus, runTrigger )

		
	def fieldSet( self, name, column, value, theFocus=False, runTrigger=True ):


		# if name == 'Alias': print(1,'Alias set:', value)

		if name in self.resolve:
			if column in 'value values'.split():
				isFolder = True if self.resolve[name] == 'folder' else False
				if type(value) == str:
					value = resolve(value, isFolder)
				if type(value) == list and len(value) > 0 and type(value[0]) == str:
					for i,v in enumerate(value):
						value[i] = resolve(v, isFolder)


		# if name == 'Alias': print(2,'Alias set:', value)


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
		if type(result) == list and len(result) and type(result[0]) == list:
			return result[0]
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
		if type(result) == list:
			result = ','.join(result)
		return result

	def values2( self, name, theFocus=False ):# getSwitchValue
		for i,row in enumerate(self.switches):
			if self.switches[i].name == name and self.switches[i].active:
				return self.fieldGet( name, 'values', theFocus )
		return []

	def value2( self, name, theFocus=False ):# getSwitchValue
		for i,row in enumerate(self.switches):
			if self.switches[i].name == name and self.switches[i].active:
				return self.fieldGet( name, 'value', theFocus )
		return ''

	def isActive2( self, name, theFocus=False ):
			for i,row in enumerate(self.switches):
				if self.switches[i].name == name and self.switches[i].active: return True
			return False

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
							if switchInput[i] == ':': switchInput[i] = switchInput[i].replace(':','_;192B;_')
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
	def help(self,justAppNotFullHelp=False):
		
		# Help Menu Color Scheme
		## Unused colors commented for navigation
		helpColorScheme.labels = 'ColorBold.white'
		helpColorScheme.tableSwitchGroupsLine = 'blue'
		helpColorScheme.tableSwitchGroupsPostLabel = 'yellow'
		helpColorScheme.file = 'Background.light_blue'
		helpColorScheme.description = 'Background.green'
		helpColorScheme.tags = 'green'
		helpColorScheme.prerequisite = 'ColorBold.blue'
		helpColorScheme.relatedapps = 'ColorBold.blue'
		helpColorScheme.examples = 'purple' # handled differently
		helpColorScheme.ask_example_id = 'yellow'
		helpColorScheme.abbreviations = 'purple' # is colorizeRow
		helpColorScheme.line = 'yellow'
		helpColorScheme.requiredLabel = 'red'
		helpColorScheme.required = 'Background.red'
		helpColorScheme.switchRequredLabel = 'ColorBold.white'
		helpColorScheme.switchRequred = 'yellow'
		helpColorScheme.noRequirements = 'green' # cyan
		helpColorScheme.notes = 'purple' # handled differently
		self.justAppNotFullHelp = justAppNotFullHelp
		if self.value('Help') == 'x' or self.value('Help') == 'cls' or self.value('Help') == 'clear' or 'fn' in self.value('Help'):


			if 'fn' in self.values('Help'):
				info = self.values('Help')
				info.pop(0)
				if not info:
					pr('Usage:',c='yellow')
					for li in ['']: pr('\t- '+li,c='cyan')
					sys.exit()

				import inspect
				fn = info[0]
				info.pop(0)
				pr('Function:',fn,c='yellow')
				if not info or (info[0] == 'arg' or info[0] == 'args'):
					argspec = list(inspect.getfullargspec(eval(fn)))
					pr('\t',argspec[0])
					# for spec in argspec: pr('\t-',spec )

				sys.exit()


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

		filename = colorThis(  [ 'Program:  \t' ], helpColorScheme.labels, p=0  )
		try:
			if not appInfo[__.appReg]['file'] == 'thisApp.py' and appInfo[__.appReg]['liveAppName'] == '__init__':
				filename += colorThis(  [ appInfo[__.appReg]['file'].replace('.py','') ], helpColorScheme.file, p=0  )
				sys.exit()
			else:
				try:
					if not appInfo[__.appReg]['file'] == 'thisApp.py' and not appInfo[__.appReg]['liveAppName'] == '__init__':
						filename += colorThis(  [ appInfo[__.appReg]['liveAppName'] ], helpColorScheme.file, p=0  )
					else:
						filename += colorThis(  [ appInfo[__.appReg]['file'].replace('.py','') ], helpColorScheme.file, p=0  )
				except Exception as e:
					filename += colorThis(  [ appInfo[__.appReg]['file'].replace('.py','') ], helpColorScheme.file, p=0  )
		except: pass

		print_()
		print_( filename )
		print_()

		try:
			if type( appInfo[__.appReg]['description'] ) == list:
				print_( pr('Description:   ',c=helpColorScheme.labels,p=0))
				for x in appInfo[__.appReg]['description']:
					print_( '                 - ', pr(x,c=helpColorScheme.description,p=0) )
				print_()
			else:
				print_( inlineBold('Description:   '), pr(appInfo[__.appReg]['description'],c=helpColorScheme.description,p=0) + '\n')
			configured = True
		except Exception as e:
			configured = False

		try:
			# print_( inlineBold('Categories:    '), ', '.join( appInfo[__.appReg]['categories'] ) + '\n')
			print_( inlineBold('Tags:          '), '(',    pr(', '.join( appInfo[__.appReg]['categories'] ),c=helpColorScheme.tags,p=0)   , ')' + '\n')
			# print_( inlineBold('Tags:          '), '(',    ', '.join( appInfo[__.appReg]['categories'] )   , ')' + '\n')
			# print_( inlineBold('          Tags:'), ', '.join( appInfo[__.appReg]['categories'] ) + '\n')
			pass
		except Exception as e:
			pass

		try:
			if len(appInfo[__.appReg]['prerequisite']) > 0:
				pr('Prerequisite:',c=helpColorScheme.labels)
				for docItem in appInfo[__.appReg]['prerequisite']:
					if type(docItem) == list:
						# colorThis( '\t\t'+docItem[0], docItem[1]  )
						pr('\t\t'+docItem[0],c=helpColorScheme.prerequisite)
					else:
						pr('\t\t'+docItem,c=helpColorScheme.prerequisite)
						# colorizeRow( '\t\t'+ docItem , 2)
					# colorizeRow('\t' + prereq,2)
				print_('\n')
		except Exception as e:
			pass
		try:
			if len(appInfo[__.appReg]['relatedapps']) > 0:
				# printBold('Related Apps:')
				pr('Related Apps:',c=helpColorScheme.labels)
				
				for docItem in appInfo[__.appReg]['relatedapps']:
					if type(docItem) == list:
						pr('\t\t'+docItem[0],c=helpColorScheme.relatedapps)
					else:
						pr('\t\t'+docItem,c=helpColorScheme.relatedapps)
				print_('\n')
		except Exception as e:
			pass
		if configured:
			quit_early = False
			if len(appInfo[__.appReg]['examples']) > 0:
				# printBold('Examples:')
				pr('Examples:',c=helpColorScheme.labels)
				IDs = {}
				ei = 1
				for docItem in appInfo[__.appReg]['examples']:
					if not docItem is None:
						prei = str(ei)
						if len(self.value('Help')) and self.value('Help') == prei:
							prei = '*'
						elif not 'id' in self.value('Help') and not 'c' in self.value('Help') and not 'i' in self.value('Help') :
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
							# colorThis( '\t'+prei+'\t'+docItem[0], docItem[1]  )
							pr('\t'+prei+'\t'+docItem[0],c=helpColorScheme.examples)
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
							# pr('\t'+prei+'\t'+ docItem ,c=helpColorScheme.examples)
			if 'id' in self.value('Help') or 'c' in self.value('Help') or 'ask' in self.value('Help') or 'i' in self.value('Help'):
				askID = input( '?> : ' )
				if askID in IDs:
					setClip(IDs[askID])
					cp(  [ '\n\nCopied:\n\t', IDs[askID], '\n\n' ], helpColorScheme.ask_example_id  )
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
					# helpColorScheme.abbreviations

				if __.columnAbbreviations == 1:
					for col in appInfo[__.appReg]['columns']:
						if not col['name'] == col['abbreviation']:
							abbreviation =  fields.value( 'columns', 'abbreviation', col['abbreviation'] )
							name =          fields.value( 'columns', 'name', col['name'] )
							colorizeRow( '\t' + abbreviation + '\t' + name )
							# helpColorScheme.abbreviations
						# print_( '\t', col['abbreviation'], '\t', col['name']  )

				if len( appInfo[__.appReg]['columns'] ):
					print_()
					print_()
				# print_('\n')
		pass
		print_()
		print_()
		# def linePrint(  label=None, text=None, txt='_', mn=50, add=5, p=2, c='', half=False, h=None )
		linePrint(txt='+',c=helpColorScheme.line,x=.5)
		# colorThis('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','yellow')
		# printBold( 'Requirements:' )
		pr('Requirements:',c=helpColorScheme.labels)
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
			colorThis(  [  '  !! Required Pipe data' ]  , helpColorScheme.requiredLabel )

		if __.isRequired_Pipe_or_File:
			hasRequirements = True
			colorThis(  [  '  !! Required Pipe data or Files switch' ]  , helpColorScheme.requiredLabel )

		if len(self.isRequired[__.appReg]):
			hasRequirements = True
			colorThis(  [  '  !! Required ' + ' and '.join(self.isRequired[__.appReg])  ]  , helpColorScheme.requiredLabel )


		if not __.isRequired_or_List is None:
			# for x in __.isRequired_or_List:
			hasRequirements = True
			isRequired_or_List1 = pr('  !! Required   ',c=helpColorScheme.requiredLabel,p=0)
			isRequired_or_List2 = pr(' or '.join(__.isRequired_or_List),c=helpColorScheme.required,p=0)
			print_(isRequired_or_List1 +':   '+ isRequired_or_List2)
			# colorThis(  [  '  !! Required ' + ' or '.join(__.isRequired_or_List)  ]  , 'red' )

		lastGroup = -1
		for switch in self.switches:
			# print_( dir(switch) )
			# print_( switch.__dict__ )
			if len(switch.documentation['required']) :
				print_()
				print_()
				print_( colorThis( '  !! If using switch:' , helpColorScheme.switchRequredLabel, p=0 ), colorThis( switch.name , helpColorScheme.switchRequred, p=0 ), colorThis( 'the following is required:' , helpColorScheme.switchRequredLabel, p=0 ) )

				for x in switch.documentation['required']:
					hasRequirements = True
					colorThis(  [ '\t', x  ]  , 'red' )


			if len(switch.documentation['related']) :
				print_()
				print_()
				print_( colorThis( '  If using switch:' , helpColorScheme.switchRequredLabel, p=0 ), colorThis( switch.name , helpColorScheme.switchRequred, p=0 ), colorThis( 'the following is related:' , helpColorScheme.switchRequredLabel, p=0 ) )
				for x in switch.documentation['related']:
					hasRequirements = True
					colorThis(  [ '\t', x  ]  , 'yellow' )

				# del switch.script_trigger
				# del switch.__dict__.script_trigger
				# print_( dict( str(switch.__dict__) ) )
				# printVar( dict(switch.__dict__) )
			# sys.exit()
		if not hasRequirements:
			colorThis( [ '\t', 'No requirements' ], helpColorScheme.noRequirements )
		print_()
		linePrint(txt='+',c=helpColorScheme.line,x=.5)
		# colorThis('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','yellow')
		print_()
		print_()
		self.print()
		if 'notes' in appInfo[__.appReg]:
			if len( appInfo[__.appReg]['notes'] ):
				print_()
				print_()
				# printBold( 'Notes:' )
				pr('Notes:',c=helpColorScheme.labels)
				for col in appInfo[__.appReg]['notes']:
					print_()
					printVarSimple( col, prefix='                ', remove='"' )
					# helpColorScheme.notes
					print_()

		# for x in sys.modules:
		#     print_(x)
		sys.exit()
		raise SystemExit
		os._exit(0)
		sys.exit(1)
		os._exit(os.EX_OK)




	def process( self, helpx=False ):
		appRegI = 0
		_appReg_ = __.appReg
		load()
		__.appReg = _appReg_
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
		
		# #DEBUG
		# appRegI+=1;pr(__.appReg,appRegI)

		if argvProcess:
			for i,a in enumerate(sys.argv):
				a=a.replace('↔',' ')
				if a in __.switch_skimmer.scan:
					__.switch_skimmer.active.append( a )
				a = a.replace(':','')
				# print(a)
				# print(__.appReg)
				for ii,sw in enumerate(self.switches):
					for s in sw.switch.split(','):
						# if s.lower() == a.lower():
						# print(s)
						# print(s,a)
						if s == a:
							#taco#
							# print(self.switches[ii].appReg)
							if self.switches[ii].appReg == __.appReg:
								self.switches[ii].pos = i
								self.switches[ii].active = True
								self.switches[ii].value = self.format(self.switches[ii].name)
								self.switches[ii].values = self.format2(self.switches[ii].name)



								if self.switches[ii].name in self.resolve:
									isFolder = True if self.resolve[self.switches[ii].name] == 'folder' else False
									self.switches[ii].value = resolve( self.switches[ii].value, isFolder )
									for i, thisFile in enumerate(self.switches[ii].values):
										self.switches[ii].values[i] = resolve( thisFile, isFolder )


										
									val = self.switches[ii].values
									if type(val) == list and  len(val) > 1 and type(self.switches[ii].value) == str:
										all_strings = all(isinstance(item, str) for item in val)
										if all_strings:
											self.switches[ii].value = ','.join(val)
								# pass
								# self.switches[ii].name
								# λname=self.switches[ii].name
								# λval=self.switches[ii].value
								# λvals=self.switches[ii].values

								# if λname == 'Alias':
								# 	print('Alias set:', λval, '->', λvals)
								# 	sys.exit()
								# print(vv.isDataData)
								if self.switches[ii].name in vv.isDataData:
									# print( 'here here' ); sys.exit()
									for thisFile in self.switches[ii].values:
										# print(thisFile)
										for fileLine in getText(thisFile):
											vv.isDataData[self.switches[ii].name].append( fileLine )
									# print( vv.isDataData ); sys.exit()

								if self.switches[ii].name in vv.isDataName:
									for thisFile in self.switches[ii].values:
										vv.isDataName[self.switches[ii].name].append( thisFile )

								if self.switches[ii].name in vv.isDataDataRaw:
									for thisFile in self.switches[ii].values:
										vv.isDataDataRaw[self.switches[ii].name] += getText(thisFile, raw=True)






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
							colorThis( '\t\t'+example[0], example[1]  )
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

		if not __.appReg in self.isRequired:
			for key in self.isRequired:
				__.appReg = key
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
		global appData
		if __.regApp in appData and __.appReg == '__init__':
			if '--appReg' in sys.argv or os.environ.get('debug', 'no') == 'yes':
				pr('appReg regApp',__.appReg, __.regApp, h='lawn_green')
			__.appReg = __.regApp


		if self.isActive('DumpSwitches'):
			if not self.value('DumpSwitches'):
				self.dumpSwitches()
				sys.exit()
				pv(self.all())

		if 'json' in self.value('DumpSwitches'):
			pv(self.dic())
			sys.exit(0)
		if 'dic' in self.value('DumpSwitches'):
			pv(self.dic(1))
			sys.exit(0)
		# if 'yml' in self.value('DumpSwitches'):
		if any(item in self.values('DumpSwitches') for item in 'yml yaml _ .'.split()):
			print()
			y = toYML( self.dic() )
			if not any(item in self.values('DumpSwitches') for item in 'raw r'.split()):
				# y = y.replace("'",'')
				lines = []
				for i,line in enumerate(y.split('\n')):
					line = line.rstrip()
					if line.startswith("- '"):
						line = line.rstrip("'")
						line = line.replace("- '","- ")
					lines.append(line)
				y = '\n'.join(lines)

			pr( y, h='lawn_green' )
			print()
			sys.exit(0)


		# def process( self )     :: END ::     switches.process()


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
		lastGroup = -1
		swLen = {
			'n':0,
			's':0,
			'e':0,
		}
		sgLe = {}
		lastGroup = -1
		sgLm = 0
		for i,sw in enumerate(self.switches):
			n = len(sw.name)
			s = len(sw.switch)
			try:
				e = len(sw.example_or_notes)
			except: e=0
			if n > swLen['n']: swLen['n'] = n
			if s > swLen['s']: swLen['s'] = s
			if e > swLen['e']: swLen['e'] = e
			if not sw.group is None:
				valid = True
				if type(sw.group) == str:
					swgroupID = sw.group
					swgroupLabel = sw.group
				else:
					if len(sw.group) > 1:
						swgroupID = sw.group[0]
						swgroupLabel = sw.group[1]
					elif len(sw.group) == 1:
						swgroupID = sw.group[0]
						swgroupLabel = sw.group[0]
			# try:
			# 	sw.group[0]
			# 	valid = True
			# except Exception as e:
			# 	valid = False
			# if valid:
			# 	if not lastGroup == sw.group[0]:
			# 		if sgLm > len(sw.group[1]): sgLm = len(sw.group[1])
			# 		sgLe[sw.group[0]] = len(sw.group[1])
			# 	lastGroup = sw.group[0]

		if sgLm > swLen['e']: swLen['e'] = sgLm
		
		
		sgSe = {}
		import math
		for i,L in enumerate(sgLe):
			l = swLen['e'] - sgLe[L]
			sp = math.floor(l / 4)
			sgSe[L] = ''
			for i in range( sp+1 ): sgSe[L] += ' '

		spaces = {
			'n':'',
			's':'',
		}
		sg = len('Switch Group: 1')
		if sg > swLen['n']: swLen['n'] = sg
		# for k in swLen:
		if not swLen['n'] == sg:
			for i in range( math.floor(swLen['n'] / 4) ): spaces['n'] += ' '
		
		for i in range( math.floor(swLen['s'] / 2) ): spaces['s'] += '-'
		# for i in range( swLen['s']-1 ): spaces['s'] += '-'
		spaces['s'] = '  <'+spaces['s']+'>'
		# pv(sgSe)
		try:
			len(__.switchTableSpent)
		except:
			__.switchTableSpent = []
			__.switchTableSpentPrint = []
		def buldSwitchTable(help=False):
			lastGroup = -1
			lastLabel = ''
			switch = []
			# Start: SwitchSubGroup check
			SwitchGroup = False
			SwitchSubGroup = False
			for i,sw in enumerate(self.switches):
				if sw.name in __.switchTableSpent:
					continue
				# __.switchTableSpent.append(sw.name)
				if self.switches[i].appReg == __.appReg:
					valid = False
					if not sw.group is None:
						valid = True
						if type(sw.group) == str:
							swgroupID = sw.group
							swgroupLabel = sw.group
						else:
							if len(sw.group) > 1:
								swgroupID = sw.group[0]
								swgroupLabel = sw.group[1]
							elif len(sw.group) == 1:
								swgroupID = sw.group[0]
								swgroupLabel = sw.group[0]
								
					if valid:
						SwitchGroup = True
						if not lastGroup == swgroupID:
							pass
						elif not swgroupID == swgroupLabel and not lastLabel == swgroupLabel:
							SwitchSubGroup = True
							# sys.exit()

					if __.switch_skimmer.active and not self.switches[i].default:
						pass
					elif not __.switch_skimmer.active:
						pass
					# try:
					# 	lastGroup = swgroupID
					# 	lastLabel = swgroupLabel
					# except: pass 
			# End: SwitchSubGroup check
			
			defaultStarted = False
			spent = []
			for i,sw in enumerate(self.switches):
				
				toAdd = []
				if not help and self.switches[i].default: continue
				if help and not self.switches[i].default: continue
				if self.switches[i].default and self.justAppNotFullHelp: continue
				if sw.name in __.switchTableSpent: continue
				# if sw.name == 'Help':
				# 	print('help here',__.switchTableSpent)
				__.switchTableSpent.append(sw.name)
				# if self.switches[i].default and not defaultStarted:
				# 	continue
				if self.switches[i].default:
					defaultStarted = True
				if self.switches[i].appReg == __.appReg:
					valid = False
					if not sw.group is None:
						valid = True
						if type(sw.group) == str:
							swgroupID = sw.group
							swgroupLabel = sw.group
						else:
							if len(sw.group) > 1:
								swgroupID = sw.group[0]
								swgroupLabel = sw.group[1]
							elif len(sw.group) == 1:
								swgroupID = sw.group[0]
								swgroupLabel = sw.group[0]
								
					if sw.name == '--':
						toAdd.append({'IsSwitchSpacer':'','name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
						continue
					if valid:
						# print('valid',sw.name)
						if False:
							pass
						elif not lastGroup == swgroupID:
							if SwitchSubGroup:
								pass
								toAdd.append({ 'HasSwitchSubGroup': '', 'SwitchGroup': swgroupLabel.strip(), 'name': '','switch': '','example_or_notes': ''})
								
							else:
								pass
								# sys.exit()
								# pr(swgroupLabel,c='BackgroundGreyBold.green')
								if len(sw.group) > 3 and sw.group[2] == 0:
									# switch.append({ 'SwitchGroupPostLabel': sw.group[3].strip(), 'name': '','switch': '','example_or_notes': ''})
									toAdd.append({ 'SwitchGroup': swgroupLabel.strip(), 'SwitchGroupPostLabel': sw.group[3].strip(),'name': '','switch': '','example_or_notes': ''})
								else:
									toAdd.append({ 'SwitchGroup': swgroupLabel.strip(), 'name': '','switch': '','example_or_notes': ''})
							# switch.append({'name':'' ,'switch':'','example_or_notes': '>>'})
						elif not swgroupID == swgroupLabel and not lastLabel == swgroupLabel:
							if len(sw.group) > 2:
								toAdd.append({ 'SwitchGroupDepth': sw.group[2], 'SwitchSubGroup': swgroupLabel.strip(), 'name': '','switch': '','example_or_notes': ''})
							else:
								toAdd.append({ 'SwitchSubGroup': swgroupLabel.strip(), 'name': '','switch': '','example_or_notes': ''})
						# continue
						# SwitchGroup
					if __.switch_skimmer.active and not self.switches[i].default:
						if SwitchGroup:
							if valid:
								key = 'valid'
							else:
								key = 'SwitchGroup'
							if not sw.name in spent:
								spent.append(sw.name)
								switch.extend(toAdd)
								switch.append({key:'','name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
						else:
							if not sw.name in spent:
								spent.append(sw.name)
								switch.extend(toAdd)
								switch.append({'name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
					elif not __.switch_skimmer.active:
						if SwitchGroup:
							if valid:
								key = 'valid'
							else:
								key = 'SwitchGroup'
							if not sw.name in spent:
								spent.append(sw.name)
								switch.extend(toAdd)
								switch.append({key:'','name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
						else:
							if not sw.name in spent:
								spent.append(sw.name)
								switch.extend(toAdd)
								switch.append({'name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
						# switch.append({'name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
					try:
						lastGroup = swgroupID
						lastLabel = swgroupLabel
					except: pass
			return switch
		switch = buldSwitchTable()
		switchHelp = buldSwitchTable(True)
		switch.extend(switchHelp)

		# def test(value):
		#   value = value + '_V_'
		#   return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,switch,example_or_notes')
	def printStatus(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.active:
					active = 'True'
				else:
					active = ''
				v=[]
				for x in sw.values: v.append(str(x))
				value = ' | '.join(v)

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
#Switches-end


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

		self.iGroupFirsts=[]
		self.GroupTotals={}
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
			#   if self.tableProfile[i]['name'] == name and '' in self.tableProfile[i] and  'function' in type(self.tableProfile[i]['trigger']):
			#       fn=self.tableProfile[i]['trigger']
		# did not work

		size = len(name) + spacer

		# print_(name,00)
		# rows[0][name]
		for i,rec in enumerate(self.asset):
			if not name in rec: self.asset[i][name]=''
		Name = name.replace('d.','')
		try:
			pass
			if Name in rows[0]:
				rows[0][Name]
			else:
				# print_(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
				do = 'rows[0]["' + '"]["'.join(Name.split('.')) + '"]'
				print(do)
				eval(  do  )
		except Exception as e:
			errors.append({'id': 9, 'function': 'tabGetMaxSpace()', 'cnt': 1, 'location': 'rows[0][name]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			printBold('Error:','red')
			printBold('\tBad column input.')
			my_dict = {col: [] for col in self.asset[0].keys()}; print('Keys:', ' '.join(my_dict) )
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
	def showColumn(self,column,i,columnHeaderLength,f71=None):
		# print_(column)

		#c3p0

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
		GroupTotals = switches.values('GroupTotals')
		try:
			tabFix = self.spaces[column]
		except Exception as e:
			# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
			tabFix = self.tabGetMaxSpace(column)
			self.spaces[column] = tabFix

		if switches.isActive('GroupBy') == True: #			theLasts
			if column in GroupTotals:
				if not column in self.GroupTotals: self.GroupTotals[column]=0
				if i in self.iGroupFirsts: self.GroupTotals[column]=0

				try:
					self.GroupTotals[column]+=float(self.asset[i][column])
				except: pass
			for gb in groupBy.split(','):
				gb = str(gb)
				if column == gb:
					

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
						text = '' #c3p0
						if not column in self.Groups: self.Groups[column]={'lines':[]}
						self.Groups[column]['lines'].append(i)



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
		#c3p0
		printedLines = 0
		if switches.isActive('GroupBy') and self.asset:




			val=[]
			for k in self.asset[0]:
				for y in switches.values('GroupBy'):
					if k.lower().replace(' ','_') in y.lower().replace(' ','_'): val.append(k)
			switches.fieldSet('GroupBy','value',','.join(val))
			switches.fieldSet('GroupBy','values',val)


			####################################
			group_columns = switches.values('GroupBy')
			first_index = None
			last_key = None
			valTracker = {}
			for i, row in enumerate(self.asset):
				for k in row:
					v = str(row[k])
					if not k in valTracker: valTracker[k] = {}
					if not v in valTracker[k]: valTracker[k][v] = []
					valTracker[k][v].append(i)
					
			for i, row in enumerate(self.asset):
				key = tuple(row[col] for col in group_columns)

				if key != last_key:
					first_index = i
					last_key = key
					valid = True
					vCnt = 0

					for k in group_columns:
						v = str(row[k])
						if i in valTracker[k][v] and len(valTracker[k][v]) == 1:
							vCnt += 1
					if not vCnt == len(group_columns):
						self.iGroupFirsts.append(first_index)
			####################################


		if switches.isActive('GroupTotals') and self.asset:
			val=[]
			for k in self.asset[0]:
				for y in switches.values('GroupTotals'):
					if k.lower().replace(' ','_') in y.lower().replace(' ','_'): val.append(k)
			switches.fieldSet('GroupTotals','value',','.join(val))
			switches.fieldSet('GroupTotals','values',val)

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
			# print_('Null Set')
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

		if switches.isActive('Markdown-Table'):
			pr(dict_to_markdown_table(self.asset))
			sys.exit()
			return self.asset

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
			# print_('Null Set')
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

		self.Groups={}
		for c in switches.values('GroupTotals'):
			self.Groups[c]={
								'lines': [],
			}
		def addField(text,column):

			try:
				tabFix = self.spaces[column]
			except Exception as e:
				# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
				tabFix = self.tabGetMaxSpace(column)
				self.spaces[column] = tabFix
			tabFix+=4
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
			return result




		max_length = 0

		for item in self.asset:
			result = ''
			for c in column.split(','):
				try:
					result += self.showColumn(c, i, columnHeaderLength) + self.columnTab + tableLine
				except Exception:
					pass
			try:
				current_length = colorizeRowLength(tableLine + result)-len('_______________________________________________')
				max_length = max(max_length, current_length)
			except: pass

		last_print_of_uncategorized_switch_preceding_dash = -2
		if len(self.asset) > 5 and 'example_or_notes' in self.asset[1]:
			pass
			_records = []
			_spent = []
			for item in self.asset:
				string = str(item)
				if string in _spent:
					continue
				_spent.append(string)
				_records.append(item)
			self.asset = _records

		for I, item in enumerate(self.asset):
			if I in self.iGroupFirsts:
				print('')
			if 'name' in item:
				if item['name'] in __.switchTableSpentPrint and item['name'] == 'Help':
					break
					
				else:
					__.switchTableSpentPrint.append(item['name'])
			# print_(item)
			result = ''
			# global switches
			for c in column.split(','):
				# if switches.isActive('TablePlus'):
				# 	if not  showLine(str(item),switches.values('TablePlus'),switches.values('TableMinus')): continue
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
				

				
				# result += self.showColumn(c,i,columnHeaderLength,2) + self.columnTab+tableLine

				try:
					pass
					if not switches.isActive('GroupTotals'):
						theLine = self.showColumn(c,i,columnHeaderLength,2) + self.columnTab+tableLine
						result += theLine
						if len(theLine.strip()) > 10: printedLines+=1
					try:
						if switches.isActive('GroupTotals'):
							theLine = self.showColumn(c,i,columnHeaderLength,2) + self.columnTab+tableLine
							result += theLine
							if len(theLine.strip()) > 10: printedLines+=1
						pass
					except:
						pass
						
						# print(result)
						# sys.exit()
						#c3p0
				except Exception as e:
					errors.append({'id': 12, 'function': 'print()', 'cnt': 1, 'location': "result += showColumn(rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': 'folder'}, {'name': 'column', 'value': column}], 'error': e})
					printBold('Error:','red')
					printBold('\tBad column input.')
					my_dict = {col: [] for col in self.asset[0].keys()}; print('Keys:', ' '.join(my_dict) )
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
				theLine = tableLine+result.lstrip()
				__.theRowLength = len(theLine)

				if shouldPrint:


					if 'IsSwitchSpacer' in item:
						print_()
						continue


					hasTotal=False
					_result_=''
					for c in column.split(','):
						if c in self.Groups and not i in self.Groups[c]['lines'] and i-1 in self.Groups[c]['lines']:
							hasTotal=True
					if hasTotal:



						for c in column.split(','):
							total={}
							for gc in self.GroupTotals:
								total[gc]=0
							_g_=switches.values('GroupBy')[0]
							_sub_=self.asset[i-1][_g_]
							for ass in self.asset:
								if _g_ in ass and ass[_g_] == _sub_:
									for gc in self.GroupTotals:
										if not type(ass[gc]) == int: ass[gc] = 0
										total[gc]+=ass[gc]

							if c in self.GroupTotals:
								# _result_+=addField( addComma(self.GroupTotals[c]) ,c)
								_result_+=addField( addComma(total[c]) ,c)
								self.GroupTotals[c]=0
							else:
								_result_+=addField('',c)
						# colorizeRow( tableLine+_result_, prefix=self.tab['table']+loopPrint(__.table_prefix_padding), prefixColor=self.tab_color, haltColorShift=self.isExtraRecord )
						# printedLines
						# str(printedLines)
						
						if printedLines == 1 and str(_result_).strip() == '0':
							pass
						else:
							# print(_result_)
							cp(' '+tableLine+_result_,c='green')
							# cp(str(printedLines)+' '+tableLine+_result_,c='green')




					isSwitchGroup = False
					if self.groupID_KEY in item and item[self.groupID_KEY].endswith('-B'):
						cp( [ self.tab['table']+loopPrint(__.table_prefix_padding) + result ], 'BackgroundGrey.blue' )
					else:
						if result.strip().startswith('Help  '):print_('')

						SwitchGroupPostLabel = ''
						if 'SwitchGroupPostLabel' in item and  'example_or_notes' in item :
							isSwitchGroup = True
							SwitchGroupPostLabel = pr(__.SwitchGroup_Help.PostLabel,item['SwitchGroupPostLabel'],c=helpColorScheme.tableSwitchGroupsPostLabel,p=0)
						# if result.strip().startswith('Switch Group:'): print('')
						if 'SwitchSubGroup' in item and  'example_or_notes' in item :
							isSwitchGroup = True
							if 'SwitchGroupDepth' in item and  'example_or_notes' in item :
								SwitchGroupDepth = item['SwitchGroupDepth']
							else:
								SwitchGroupDepth = 1
							if len(__.SwitchGroup_Help.SubGroup) ==1:
								SwitchGroupDepth +=1
							cnt = str(SwitchGroupDepth-1)
							if cnt == '1':
								cnt=''
							print()
							pr(pr(__.SwitchGroup_Help.SubGroup * (SwitchGroupDepth)+__.SwitchGroup_Help.Delim+' '+__.lastSwitchGroup+f' {__.SwitchGroup_Help.SubGroup} '+item['SwitchSubGroup']+__.SwitchGroup_Help.SubGroup_After.replace(' cnt',' '+cnt),c='ColorBold.white',p=0),SwitchGroupPostLabel)
						if 'SwitchGroup' in item and  'example_or_notes' in item :
							isSwitchGroup = True
							# print()

							if 'HasSwitchSubGroup' in item and  'example_or_notes' in item :
								pr('_' * max_length,c=helpColorScheme.tableSwitchGroupsLine)
								pass
							SwitchGroup = __.SwitchGroup_Help.Group
							END = __.SwitchGroup_Help.Group_After
							if item['SwitchGroup'] == '':
								SwitchGroup = __.SwitchGroup_Help.NoGroup
								END = __.SwitchGroup_Help.NoGroup_After
							else:
								__.lastSwitchGroup = item['SwitchGroup']
								print_()
							if item['SwitchGroup'] == 'Help' and 'Help' in __.switchTableSpentPrint: continue
							if item['SwitchGroup'] == 'Help':
								print('\n\n')
								pr(line=1,c='red',lineLen=__.theRowLength)
								pr('\u25BD\u25BD  :: Default Switches::  \u25BD\u25BD',c='Background.red',center=__.theRowLength)
							if not I-1 == last_print_of_uncategorized_switch_preceding_dash:
								pr(  pr(SwitchGroup+__.SwitchGroup_Help.Delim+' '+item['SwitchGroup']+END,c='ColorBold.white',p=0)  ,  SwitchGroupPostLabel)
								if SwitchGroup == __.SwitchGroup_Help.NoGroup:
									print_()
							last_print_of_uncategorized_switch_preceding_dash = I
						# print(item)
						if isSwitchGroup:
							theLine = tableLine+result.lstrip()
						else:
							theLine = tableLine+result
						shouldPrint = True
						if not theLine.strip() and switches.isActive('GroupBy'):
							shouldPrint = False

						if shouldPrint:
							__.theRowLength = len(theLine)
							colorizeRow( theLine, prefix=self.tab['table']+loopPrint(__.table_prefix_padding), prefixColor=self.tab_color, haltColorShift=self.isExtraRecord )
			i += 1
			if 'example_or_notes' in column and 'switch' in column and  switchDefault == i:

				# if __.switch_skimmer.active: sys.exit()
				pass
				# print_('')
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

			import uuid
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
		try:
			import simplejson
			json = simplejson
		except:
			pass
		try:
			import json
		except ImportError:
			json = simplejson
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
		try:
			import simplejson
			json = simplejson
		except:
			pass
		try:
			import json
		except ImportError:
			json = simplejson
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
#Table-end



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
		global switches

		
		if not h is None:
			printColumns = h
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
					if switches.isActive('GroupBy'):
						keys = list(self.tables[i].asset[0].keys())
						_rec = {}
						for key in keys:
							_rec[key] = ''
						self.tables[i].asset = [ _rec ] + self.tables[i].asset
					if not ',' in fields:
						printColumns = False
					# if switches.isActive('Markdown-Table'):
						# self.tables[i].set(asset)
						# pr(dict_to_markdown_table(self.tables[i].asset)); return True;
					self.tables[i].print(fields,fieldLengths,printColumns=printColumns, l=l, p=p)
					sI = i
				else:
					# print_('Null Set')
					pass

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

#Tables-end




###########################################################################################
def md5(fname):
	import hashlib
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()
	return hash_md5.hexdigest()


def md5_string(text):
	import hashlib
	return hashlib.md5(text.encode('utf-8')).hexdigest()

md5String=md5_string
md5Str=md5_string
str5=md5_string
md5File=md5

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
	return int(result)

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



def to_bytes(size_str):
	if 'Kb' in size_str: size_str = size_str.replace('Kb', 'kbit')
	if 'Mb' in size_str: size_str = size_str.replace('Mb', 'mbit')
	if 'Gb' in size_str: size_str = size_str.replace('Gb', 'gbit')
	if 'Tb' in size_str: size_str = size_str.replace('Tb', 'tbit')
	if 'Pb' in size_str: size_str = size_str.replace('Pb', 'pbyte')
	if 'Eb' in size_str: size_str = size_str.replace('Eb', 'ebyte')
	if 'Zb' in size_str: size_str = size_str.replace('Zb', 'zbyte')
	if 'Yb' in size_str: size_str = size_str.replace('Yb', 'ybyte')

	size_str = size_str.lower()
	unit_map = {
		'b': 1,
		'kb': 1024,
		'mb': 1024**2,
		'gb': 1024**3,
		'tb': 1024**4,
		'pb': 1024**5,
		'eb': 1024**6,
		'zb': 1024**7,
		'yb': 1024**8,
		'byte': 1,
		'kbyte': 1024,
		'mbyte': 1024**2,
		'gbyte': 1024**3,
		'tbyte': 1024**4,
		'pbyte': 1024**5,
		'ebyte': 1024**6,
		'zbyte': 1024**7,
		'ybyte': 1024**8,
		'kbit': 1024/8,
		'mbit': 1024**2/8,
		'gbit': 1024**3/8,
		'tbit': 1024**4/8,
		'pbit': 1024**5/8,
		'ebit': 1024**6/8,
		'zbit': 1024**7/8,
		'ybit': 1024**8/8,
		'bit': 1/8
	}
	try:
		size, unit = size_str.split()
		size = float(size)
		if unit[-1] in ['b', 'e', 't', 'p', 'z', 'y']:
			unit = unit[:-1]
		if unit[-1] == 'k':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'm':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'g':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 't':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'p':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'e':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'z':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'y':
			unit = unit[:-1] + 'byte'
		return int
	except:
		raise ValueError(f'Invalid size string: {size_str}')

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
def timeAgoThrow( do='', startDate=None,epoch=None, d=None ):
	# agoThrow
	if do == 'm': do = 'md'
	if do == 'c': do = 'cd'
	if do == 'md' or do == 'cd': return do
	# test = 'sdwmy'
	# good = False
	# for t in test:
	# 	if t in do:
	# 		good = True
	# if not good:
	# 	raise ValueError("Invalid value provided")
	new=timeAgo22( do, startDate,epoch, d )
	if not type(new) == float:
		raise ValueError("Invalid value provided")


	return new

def Ago( do='', startDate=None,epoch=None, d=None ):
	if type(do) == float: return do
	return timeAgo_past( do, startDate )

def timeAgo( do='', startDate=None,epoch=None, d=None ):
	if type(do) == float: return do

	# translation = str.maketrans('0123456789', '*' * 10)
	# onlyText = do.translate(translation)
	# onlyNumbers = ''.join(c for c in text if c.isdigit())


	if do == 'm': do = 'md'
	if do == 'c': do = 'cd'
	if do == 'md' or do == 'cd': return do
	# test = 'sdwmy'
	# good = False
	# for t in test:
	# 	if t in do:
	# 		good = True
	# if not good:
	# 	raise ValueError("Invalid value provided")
	new=timeAgo22( do, startDate,epoch, d )
	# if not type(new) == float:
	# 	raise ValueError("Invalid value provided")


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
		try:
			one = resolveEpochTest( startDate )
			two = autoDate( one.split(' ')[0] )
		except:
			err('bad second switch',do)
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
#Databases-end

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
		import sqlite3
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
		import sqlite3
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
		import sqlite3
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
		import sqlite3
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
		import sqlite3
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

#Database-end


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
#DatabaseTables-end


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

#DatabaseFields-end

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
		import sqlite3
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
		import sqlite3
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
#Database2-end


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

	# ── Brackets ─────────────────────────────
	[ '[[',            '(',              'bracket' ],
	[ ']]',            ')',              'bracket' ],
	[ ';opar;',        '[',              'bracket' ],
	[ ';bkt0;',        '[',              'bracket' ],
	[ ';bkt1;',        ']',              'bracket' ],

	# ── Quotes ───────────────────────────────
	[ ";'",            '"',              'quote'   ],
	[ ';q;',           '"',              'quote'   ],
	[ '"\'"',          "'",              'quote'   ],
	[ ';sq',           "'",              'quote'   ],
	[ ";;'",           _v.slash+'"',     'quote'   ],

	# ── Whitespace / Control ────────────────
	[ ';sp',           ' ',              'whitespace' ],
	[ _v.slash+'n',    '\n',             'whitespace' ],
	[ ';n',            '\n',             'whitespace' ],
	[ ';return',       '\n',             'whitespace' ],
	[ ';t',            '\t',             'whitespace' ],

	# ── Delimiters ───────────────────────────
	[ ';d;',           __.theDelim,      'delimiter' ],
	[ ';delim;',       __.theDelim,      'delimiter' ],
	[ ';thedelim;',    __.theDelim,      'delimiter' ],
	[ ';theDelim;',    __.theDelim,      'delimiter' ],

	# ── Symbols ──────────────────────────────
	[ '[plus]',        '+',              'symbol' ],
	[ ';+',            '+',              'symbol' ],
	[ '[eq]',          '=',              'symbol' ],
	[ '[star]',        '*',              'symbol' ],
	[ '[a]',           '*',              'symbol' ],
	[ '[s]',           '$',              'symbol' ],
	[ '[caret]',       '^',              'symbol' ],
	[ ';6',            '^',              'symbol' ],
	[ '[pipe]',        '|',              'symbol' ],
	[ '[p]',           '|',              'symbol' ],
	[ '[semi]',        ';',              'symbol' ],
	[ ';.',            ':',              'symbol' ],
	[ '_;192A;_',      ',',              'symbol' ],
	[ '_;192B;_',      ':',              'symbol' ],
	[ ';;',            ',',              'symbol' ],
	[ ';c',            ',',              'symbol' ],
	[ '[and]',         '&',              'symbol' ],
	[ '[u]',           '_',              'symbol' ],
	[ '[q]',           '?',              'symbol' ],

	# ── Dashes / Minuses ─────────────────────
	[ ';_',            '-',              'dash'   ],
	[ ';-',            '-',              'dash'   ],
	[ '[minus]',       '-',              'dash'   ],
	[ '[min]',         '-',              'dash'   ],
	[ '[mn]',          '-',              'dash'   ],
	[ '[m]',           '-',              'dash'   ],
	[ '[m]',           '-',              'dash'   ],
	[ '+--+c',         '--c',            'dash'   ],
	[ '--',            '-',              'dash'   ],

	# ── Redirects / Arrows ───────────────────
	[ '[gg]',          '>>',             'arrow' ],
	[ '[oo]',          '>>',             'arrow' ],

	# ── HTML / Angle Brackets ────────────────
	[ '[htmlopen]',    '<',              'html' ],
	[ '[htmlclose]',   '>',              'html' ],
	[ '[gtr]',         '>',              'html' ],
	[ '[lss]',         '<',              'html' ],

	# ── Slashes / Paths ──────────────────────
	[ ';bs',           '/',              'path' ],
	[ ';fs',           '\\',             'path' ],
	[ ';js',           '//',             'path' ],
	[ ';bk',           _v.myBackup,      'path' ],

	# ── Other / Utility ──────────────────────
	[ '↔',             ' ',              'misc' ],
	[ 'null00',        '"",',            'misc' ],
	[ '"\'", "\'"',    "','" ,           'misc' ],

# ── Brackets ─────────────────────────────
# ── Quotes ───────────────────────────────
# ── Whitespace / Control ────────────────
# ── Delimiters ───────────────────────────
# ── Symbols ──────────────────────────────
# ── Dashes / Minuses ─────────────────────
# ── Redirects / Arrows ───────────────────
# ── HTML / Angle Brackets ────────────────
# ── Slashes / Paths ──────────────────────
# ── Other / Utility ──────────────────────


)

ci_spent=[]
def ci(string):
	# print(string)
	if type(string) == list:
		for i,s in enumerate(string):
			string[i] = ci(s)
		return string
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
		fo =_bm.Bookmarks( fo ).get()
		if fo:
			return fo
	except: pass

	return __.path(fo)
aliasesFiDb=None
def aliasesFi(fi):
	global aliasesFiDb
	if os.sep in fi and os.path.isfile(fi) and isTextFi(fi): return fi
	if not aliasesFiDb:
		aliasesFiDb=getTable('file-open-aliases.hash')
	aliases = aliasesFiDb
	# print(len(aliasesFiDb))
	if not 'aliases' in aliases: aliases['aliases']={}
	if not 'files' in aliases: aliases['files']={}
	if fi in aliases['aliases']:
		fi = aliases['aliases'][fi]
	return fi
__.aliasesFi=aliasesFi
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

#ThisThread-end


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
#Threads-end
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

		import sqlite3
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
		import sqlite3
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
#Queue-end


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

#Field-end

class Fields:

	def __init__(self):
		self.fields = {}
		self.extra = 0

	def lengths( self, project ):
		global switches
		if switches.isActive('Long'):
			minLength=False
		else:
			minLength=True
		result = {}
		for record in self.fields[project]:
			if record.project == project:
				if minLength:
					result[record.name]=43
				else:
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
#Fields-end
# _.fields.register( 'project', 'name', script=_.resolveEpochTest )
# _.fields.asset( 'project', {} )
# _.fields.asset( 'project', [{}] )
# _.fields.register( 'project', 'name', value, appReg=focus() )
# _.fields.register( 'project', 'name', value )
# _.fields.value( 'project', 'name', value )

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
	switches.register('PrintAutoAbbreviations', '-printa,-aprint', default=True, group=[swGrp,'Help'] )
	switches.register('TablePlus','t+,+t,-ts+,-st+,-tablesearch', 'Search_Sting', default=True, group=[swGrp,'Seach'] )
	switches.register('TableMinus','t-,-t,-ts-,st-,-tableminus', 'Search_Sting', default=True, group=[swGrp,'Seach'] )
	switches.register('GroupBy', '-g,-group,-groupby', 'ext, month', default=True, group=[swGrp,'Reports'] )
	switches.register('GroupTotals', '-gt,-grouptotal,-gtotal,-gtotals', 'mem_usage', default=True, group=[swGrp,'Reports'] )
	switches.register('Aggregate', '-aggregate', '" eof-field-len= add(len(version),len(backup)); config(var,eof,isFirst); "', default=True, group=[swGrp,'Reports'] )
	switches.register('GroupSpaces', '-gs,-space,-groupspaces', default=True, group=[swGrp,'Reports'] )
	switches.register('WrapTable', '-wrap', 'n p  OR  2  OR  path', default=True, group=[swGrp,'Format'] )
	switches.register('NoWrapTable', '-nowrap', default=True, group=[swGrp,'Format'] )
	switches.register('TableProfile', '-tp,-table',' *;c *;l  h;l header;left  size;l,gs', default=True, group=[swGrp,'Format'] )
	switches.register('Long', '-long', default=True, group=[swGrp,'Format'] )
	switches.register('Short', '-sc,-short', default=True, group=[swGrp,'Format'] )
	switches.register('Length', '-length','x3', default=True, group=[swGrp,'Format'] )
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
	switches.register( 'Markdown-Table', '--md' , default=True, group=[swGrp,'Output'] )
	switches.register( 'Paste-isData', '--clip,--pa,--paste,-ppa,-ppaste,-ispa,-idpa' , default=True, group=[swGrp,'Input'] )
	switches.register( 'Paste-isData-json', '--json,-pjson,-jsonp' , default=True, group=[swGrp,'Input'] )
	# switches.register('Report', '-report', default=True, group=[swGrp,'Output'] )
	swGrp += 1
	switches.register( 'SavePrint', '--savePrint' , default=True, group=[swGrp,'Script Helper'] )
	switches.register( 'CopyPrint', '--copyPrint' , default=True, group=[swGrp,'Script Helper'] )


	swGrp += 1
	switches.register('LoadEpoch', '-loadepoch', default=True, group=[swGrp,'Rebuild From Logs'] )
	switches.register('PrintEpoch', '-printepoch', default=True, group=[swGrp,'Rebuild From Logs'] )
	swGrp += 1
	switches.register('ExitNotify', '--notify', default=True, group=[swGrp,'--> Notify When App Completes <--'] )

	defaultScriptTriggers_do()






####################### Deleted-On: 25-04-01 
# def load():
# 	global switches_loaded
# 	switches_loaded += 1
# 	if switches_loaded > 1:
# 		if not __.setting('default-switches'): return None
# 	# if True
# 		global switches
# 		global switchDefault

# 		# global tables

# 		# switches.trigger('Column',formatColumns)

# 		switchDefault = switches.length()
# 		switches.register('Help', '?,??,/?,/??,-?,-??,--??,/h,/help,-help,--help', '(?? Print Table Help Without Global Switches) copy  OR ids  OR  12  OR  ?? x ', default=True)
		
# 		switches.register('--', 'd6ec5825d1d5', default=True)
# 		switches.register('Column', '-c,-column', 'size, name', default=True)
# 		switches.register('Sort','-s,-sort', 'a.type, d.ext', default=True)
# 		switches.register('TablePlus','t+,+t,-ts+,-st+,-tablesearch', 'Search_Sting', default=True)
# 		switches.register('TableMinus','t-,-t,-ts-,st-,-tableminus', 'Search_Sting', default=True)
		
# 		switches.register('--', 'd6ec5825d1d5', default=True)
# 		switches.register('Debug', '-debug', default=True)
# 		switches.register('DumpSwitches', '-dump', 'all', default=True)
# 		switches.register('Errors', '-Error,-Errors', '8,11 OR hide:8,11', default=True)
# 		switches.register('Timeout', '-t,-Timeout', default=True)
# 		switches.register('GroupBy', '-g,-group,-groupby', 'ext, month', default=True)
# 		switches.register('GroupTotals', '-gt,-grouptotal,-gtotal,-gtotals', 'mem_usage', default=True)
# 		switches.register('WrapTable', '-wrap', 'n p  OR  2  OR  path', default=True)
# 		switches.register('NoWrapTable', '-nowrap', default=True)
# 		# switches.register('NoTableLines', '-nolines', default=True)
# 		switches.register('YesTableLines', '-yl,-yeslines', default=True)
# 		switches.register('TableJSON', '-tjson,-tablejson', default=True)
# 		switches.register('FieldTotal', '-fieldtotal', 'mem_usage', default=True)
# 		switches.register('Aggregate', '-aggregate', '" eof-field-len= add(len(version),len(backup)); config(var,eof,isFirst); "', default=True)
# 		switches.register('GroupSpaces', '-gs,-space,-groupspaces', default=True)
# 		switches.register('TableProfile', '-tp,-table',' *;c *;l  h;l header;left  size;l,gs', default=True)
# 		# switches.register('ShortenColumn', '-sc,-shortencolumn', default=True)
# 		switches.register('WebTable', '-web', default=True)
# 		switches.register('Long', '-long', default=True)
# 		switches.register('Short', '-sc,-short', default=True)
# 		switches.register('Length', '-length','x3', default=True)
# 		# switches.register('Report', '-report', default=True)
# 		switches.register('Plus', '+','all unless -or', default=True)
# 		switches.register('Minus', '-', default=True)
# 		switches.register('Plus-single', '+1', default=True)
# 		switches.register('Minus-single', '-1', default=True)
# 		switches.register('Plus-Sub', '++','any', default=True)
# 		switches.register('PlusOr', '-or', default=True)
# 		switches.register('PlusClose', '+close', '90%', default=True)
# 		switches.register('PlusCode', '+code','=  OR  *x  OR  x*  AND/OR color AND/OR n/new' , default=True)
# 		switches.register('PlusDuplicate', '+dup,+duplicate', '90%', default=True)
# 		switches.register('StrictCase', '-case,-strictcase,-strict', default=True)
# 		switches.register('PrintAutoAbbreviations', '-printa,-aprint', default=True)
# 		switches.register('NoColor', '-nocolor', space=True, default=True)
# 		switches.register('LoadEpoch', '-loadepoch', default=True)
# 		switches.register('PrintEpoch', '-printepoch', default=True)
# 		switches.register('NoTitleChange', '-ntc,-notitlechange', default=True)
# 		switches.register('chmod', '-chmod,-777', default=True)
# 		switches.register( 'Paste-isData', '--pa,--paste,-ppa,-ppaste,-ispa,-idpa' , default=True)
# 		switches.register( 'Paste-isData-json', '--json,-pjson,-jsonp' , default=True)
# 		switches.register( 'Markdown-Table', '--md' , default=True)
# 		# switches.register('SkipColumnTriggers', '-skiptriggers', default=True)
# 		defaultScriptTriggers_do()

import importlib

regImps = {}

##############################

class regImp:

	def __init__( self, focus=None, app=None, argvProcessForce=False, dirty=False, a=None, i=None ):
		
		
		# __.appReg = __.regApp
		self.regApp = __.appReg
		# __.appReg = self.regApp
		
		
		if focus == 0: focus = None
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
		appReg = __.appReg
		self.imp = importlib.import_module(app)
		# self.imp = importlib.util.spec_from_file_location( app, _v.py + _v.slash + app + '.py' )
		# print(app)
		# print(app)
		# print(app)
		# for x in dir(self.imp):
		#   print(x)
		# sys.exit()
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
		
		__.appReg = self.regApp

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
		__.appReg = self.regApp

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
		__.appReg = self.regApp

	def deleteSwitch( self, name ):
		global switches
		__.appReg = self.focus

		switches.fieldSet( name, 'active', False )

		__.appReg = self.focusPop
		__.appReg = self.regApp


	def kwargs( self, *args, **kwargs ):
		focusPop=True
		if 'focusPop' in kwargs:
			focusPop=kwargs['focusPop']
			del kwargs['focusPop']

		__.appReg = self.focus

		self.imp.appDBA = self.focus
		if args and kwargs:
			result = self.imp.action(*args, **kwargs)
		elif args:
			result = self.imp.action(*args)
		elif kwargs:
			result = self.imp.action(**kwargs)
		else:
			result = self.imp.action()

		if focusPop:
			__.appReg = self.focusPop

		return result
	def action( self, *arg, **kwargs ):
		focusPop=True
		# focusBK = __.appReg
		__.appReg = self.focus

		self.imp.appDBA = self.focus
		result = self.imp.action( *arg, **kwargs )
		# if not arg == 'c766f06b':
		# 	result = self.imp.action(arg)
		# else:
		# 	result = self.imp.action()

		if focusPop:
			__.appReg = self.focusPop

		__.appReg = self.regApp

		return result


	# def do( self, func,

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

		if 'function' in str(type( func )):
			return func()
		elif type( func ) == str:
			theFunction = eval( 'self.imp.' + func )
		else:
			theFunction = func

		result = 'theFunction'+fak(args,kwargs)


		# if type( arg ) == bool:
		#   result = theFunction()
		# elif type( arg ) == dict:
		#   result = theFunction(**arg)
		# elif type( arg ) == list:
		#   result = theFunction(*arg)
		# else:
		#   result = theFunction(arg)



		if focusPop:
			__.appReg = self.focusPop

		__.appReg = self.regApp
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
		__.appReg = self.regApp
		return theID
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


def err( msg='STOP' , e=None, note=None, kill=True, bulletDash=False, dash=None, label='Error'):
	pr()
	primaryColor = 'red'
	if label == 'i': label = 'Information'
	if not label == 'Error':
		primaryColor = 'blue'

	if not dash is None:
		bulletDash = dash

	cp( linePrint(txt='*',p=0), primaryColor )

	cp( '  '+label+'', primaryColor )
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

	# cp( '**********************************************************************', primaryColor, isError=True )
	# linePrint()
	cp( linePrint(txt='*',p=0), primaryColor )
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
	import requests # type: ignore
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
def URL(url, data={}, t=None, txt=None, text=False, headers=None, h=None):
	if not h is None:
		headers = h
	if not t is None:
		text = t
	if not txt is None:
		text = txt

	import requests  # type: ignore
	response = requests.post(url, data=data, headers=headers)

	if text:
		from bs4 import BeautifulSoup # type: ignore
		soup = BeautifulSoup(response.text, 'html.parser')
		return soup.get_text(separator='\n', strip=True)
	else:
		return response.content.decode("utf-8").replace('\\n', '\n')


def URL2(url, data={}):
	import requests # type: ignore
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Language": "en-US,en;q=0.9",
		"Connection": "keep-alive"
	}
	response = requests.post(url, data=data, headers=headers)
	print(f"Fetching data from: {url}")
	return response.text.replace('\\n', '\n')




def URL3(url, post_data=None):
	"""
	Fetch a URL using a Windows 11 Chrome User-Agent.
	If post_data is provided, uses POST, otherwise GET.
	Returns plain text extracted from the HTML.
	"""
	import requests
	from bs4 import BeautifulSoup

	headers = {
		"User-Agent": (
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
			"AppleWebKit/537.36 (KHTML, like Gecko) "
			"Chrome/115.0.0.0 Safari/537.36"
		)
	}

	if post_data:
		resp = requests.post(url, data=post_data, headers=headers)
	else:
		resp = requests.get(url, headers=headers)

	resp.raise_for_status()  # raise an error for HTTP 4xx/5xx

	soup = BeautifulSoup(resp.text, "html.parser")
	return soup.get_text(separator="\n", strip=True)



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
	__.KeyMonActive=False
	global switches
	if switches.isActive('ExitNotify'):
		Notify(Exit='Force')
	else:
		Notify(Exit=True)
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
IS_IS = {
	'gzip': 'gz',
}
##################################################


__.myHeaders = {}

def myHeaders():
	if list(__.myHeaders.keys()):
		return
	hex_headers = getTableDB('hex_headers.json')
	for rec in hex_headers:
		if 'extension' in rec and 'signature' in rec:
			ext = rec['extension'].lower()
			sig = rec['signature']  # No `.lower()`
			if ext not in __.myHeaders:
				__.myHeaders[ext] = []
			__.myHeaders[ext].append(sig)
	if not __.myHeaders: pr('myHeaders Not Loaded',c='red')


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


def Is(path, check):
	check = check.lower()
	if check in IS_IS:
		check = IS_IS[check]

	myHeaders()
	thisHeader = IS(path)
	if not thisHeader:
		return False

	if check in __.myHeaders:
		return any(thisHeader.startswith(sig) for sig in __.myHeaders[check])

	return False

def IsIs(path):
	myHeaders()
	thisHeader = IS(path)
	if not thisHeader:
		return False
	
	thisExt = path.split('.')[-1].lower()
	if Is(path, thisExt):
		ext = thisExt
		sigs = []
		for sig in __.myHeaders[thisExt]:
			if thisHeader.startswith(sig):
				sigs.append(sig)
		length = 99999
		for signature in sigs:
			if len(signature) < length:
				length = len(signature)
				sig = signature
		
		pr(pr(ext, c='yellow',p=0), pr(sig, c='green',p=0))
		return thisExt


	exts = []
	for ext, signatures in __.myHeaders.items():
		for sig in signatures:
			if thisHeader.startswith(sig):
				pr(pr(ext, c='yellow',p=0), pr(sig, c='green',p=0))
				exts.append(ext)
				# return ext

	if not exts:
		return False
	return exts


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
threads = Queue()
switches = Switches()
tables = Tables()
databases = Databases()
__.databases = Databases()

__.onExit(tables.eof)
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

##################################################
def isTextFi___last(path, num_chars=20):
	with open(path, 'rb') as file:
		content = file.read(num_chars)
		try:
			content.decode('utf-8')
			return True
		except UnicodeDecodeError:
			return False
def isTextFi(path, num_chars=1024):
	"""
	First applies a lightweight check (Fi1).
	If inconclusive or negative, double-checks with heuristic (Fi2).
	"""
	if not os.path.isfile(path):
		return False

	result1 = is_likely_utf8_text(path, num_chars)
	if result1:
		return True

	# If first check fails, confirm with deeper heuristic
	return is_heuristic_text_file(path, num_chars)

def is_likely_utf8_text(path, num_chars=1024):
	"""Determine if a file is likely a text file."""
	if not os.path.isfile(path):
		return False

	try:
		with open(path, 'rb') as file:
			content = file.read(num_chars)
			if not content:
				return True  # empty files are considered text

			# Check for null bytes (common in binaries)
			if b'\x00' in content:
				return False

			# Try UTF-8 decode
			try:
				content.decode('utf-8')
				return True
			except UnicodeDecodeError:
				pass

			# Fallback: try Latin-1 or ASCII (more forgiving)
			try:
				content.decode('latin-1')
				return True
			except UnicodeDecodeError:
				return False

	except Exception:
		return False

import os

def is_heuristic_text_file(path, num_chars=1024):
	"""
	Heuristically determines if a file is a text file.
	- Reads the first `num_chars` bytes
	- Tries UTF-8 decoding
	- Falls back to ASCII if needed
	- Checks for non-text control characters
	"""
	if not os.path.isfile(path):
		return False

	try:
		with open(path, 'rb') as file:
			chunk = file.read(num_chars)
			if b'\x00' in chunk:
				return False  # Null byte = almost certainly binary

			try:
				chunk.decode('utf-8')
			except UnicodeDecodeError:
				try:
					chunk.decode('ascii')
				except UnicodeDecodeError:
					return False

			# Check for high ratio of printable characters
			text_chars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)))
			if len(chunk) == 0:
				return False
			nontext_ratio = sum(byte not in text_chars for byte in chunk) / len(chunk)
			return nontext_ratio < 0.30
	except Exception:
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




def compress2(original_file_path, compressed_file_path):
	'''
		.gz
	'''
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
	# if not head(compressed_file_path).strip().startswith('1F 8B 08 08'):
	# 	print(f"File '{compressed_file_path}' is not a gzip file.")
	# 	return 'Not Gzip'
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
decompress2('1748977323.3772092-2025_05_31-12_36_55-.config.hash','.config.hash')
def decompress2x(path):
	if not IS(path,'gzip'):
		return False
	import shutil
	path = path.strip()
	shutil.move(path, path+'.gz')
	decompress2(path+'.gz',path)
	if path:
		os.remove(path+'.gz')
		return True
	else:
		shutil.move(path+'.gz', path)
		return False
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
def code( script, addString=None ):
	global _code
	try:
		__.code
	except Exception as e:
		_code = regImp( __.appReg, '_rightThumb._auditCodeBase' )

	return __.code.process( script, addString=addString )
def code2( script, addString=None ):
	li = code( script, addString=None )
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
##change

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











##################################################
##################################################
##################################################


def create_backup_filename(*args, **kwargs):
	import importlib.util
	if 'create_backup_filename' not in intelligent_code.functions:
		import importlib.util
		path = os.path.normpath(_v.w+'/widgets/python/library/os/file/create_backup_filename.py')
		spec = importlib.util.spec_from_file_location('create_backup_filename', path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		intelligent_code.functions['create_backup_filename'] = module.create_backup_filename
	return intelligent_code.functions['create_backup_filename'](*args, **kwargs)
fibk=create_backup_filename
backupName=create_backup_filename


def hexColor(*args, **kwargs):
	import importlib.util
	if 'hexColor' not in intelligent_code.functions:
		import importlib.util
		path = os.path.normpath(_v.w+'/widgets/python/library/code/functions/hexColor.py')
		spec = importlib.util.spec_from_file_location('hexColor', path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		intelligent_code.functions['hexColor'] = module.hexColor
	return intelligent_code.functions['hexColor'](*args, **kwargs)

def pyColor(*args, **kwargs):
	import importlib.util
	if 'pyColor' not in intelligent_code.functions:
		import importlib.util
		path = os.path.normpath(_v.w+'/widgets/python/library/code/functions/pyColor.py')
		spec = importlib.util.spec_from_file_location('pyColor', path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		intelligent_code.functions['pyColor'] = module.pyColor
	return intelligent_code.functions['pyColor'](*args, **kwargs)

class GPT:
	def __new__(cls, *args, **kwargs):
		import importlib.util
		if 'GPT' not in intelligent_code.classes:
			import importlib.util
			path = os.path.normpath(_v.w + '/widgets/python/library/ai/gpt/__init__.py')
			spec = importlib.util.spec_from_file_location('GPT', path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			intelligent_code.classes['GPT'] = module.GPT
		return intelligent_code.classes['GPT'](*args, **kwargs)


class index:
	def __new__(cls, *args, **kwargs):
		import importlib.util
		if 'index' not in intelligent_code.classes:
			import importlib.util
			path = os.path.normpath(_v.w + '/widgets/python/library/code/classes/index.py')
			spec = importlib.util.spec_from_file_location('index', path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			intelligent_code.classes['index'] = module.index
		return intelligent_code.classes['index'](*args, **kwargs)


class MongoDBMgr:
	def __new__(cls, *args, **kwargs):
		import importlib.util
		if 'MongoDBMgr' not in intelligent_code.classes:
			import importlib.util
			path = os.path.normpath(_v.w + '/widgets/python/library/db/mongoMgr.py')
			spec = importlib.util.spec_from_file_location('MongoDBMgr', path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			intelligent_code.classes['MongoDBMgr'] = module.MongoDBMgr
		return intelligent_code.classes['MongoDBMgr'](*args, **kwargs)


def fetch_advanced(*args, **kwargs):
	import importlib.util
	if 'fetch_advanced' not in intelligent_code.functions:
		import importlib.util
		path = os.path.normpath(_v.w+'/widgets/python/library/url/fetch_advanced.py')
		spec = importlib.util.spec_from_file_location('fetch_advanced', path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		intelligent_code.functions['fetch_advanced'] = module.fetch_advanced
	return intelligent_code.functions['fetch_advanced'](*args, **kwargs)


class CodeColor:
    def __new__(cls, *args, **kwargs):
        import importlib.util
        if 'CodeColor' not in intelligent_code.classes:
            import importlib.util
            path = os.path.normpath(_v.w+'/widgets/python/library/code/classes/CodeColor.py')
            spec = importlib.util.spec_from_file_location('CodeColor', path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            intelligent_code.classes['CodeColor'] = module.CodeColor
        return intelligent_code.classes['CodeColor'](*args, **kwargs)


class When:
	def __new__(cls, *args, **kwargs):
		import importlib.util
		if 'When' not in intelligent_code.classes:
			import importlib.util
			path = os.path.normpath(_v.w+'/widgets/python/library/date/When.py')
			spec = importlib.util.spec_from_file_location('When', path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			intelligent_code.classes['When'] = module.When
		return intelligent_code.classes['When'](*args, **kwargs)


class RuleEngine:
    def __new__(cls, *args, **kwargs):
        import importlib.util
        if 'RuleEngine' not in intelligent_code.classes:
            import importlib.util
            path = os.path.normpath(_v.w+'/widgets/python/library/rules_engines/RulesEngine__JsonDatabase2.py')
            spec = importlib.util.spec_from_file_location('RuleEngine', path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            intelligent_code.classes['RuleEngine'] = module.RuleEngine
        return intelligent_code.classes['RuleEngine'](*args, **kwargs)


class JsonDatabase2:
    def __new__(cls, *args, **kwargs):
        import importlib.util
        if 'JsonDatabase2' not in intelligent_code.classes:
            import importlib.util
            path = os.path.normpath(_v.w+'/widgets/python/library/db/JsonDatabase2.py')
            spec = importlib.util.spec_from_file_location('JsonDatabase2', path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            intelligent_code.classes['JsonDatabase2'] = module.JsonDatabase2
        return intelligent_code.classes['JsonDatabase2'](*args, **kwargs)


##################################################
##################################################
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


def past(value):
	value = str(value)
	import datetime
	value = value.strip()
	today = datetime.date.today()

	# Future date: '+1'
	if value.startswith('+') and value[1:].isdigit():
		return (today + datetime.timedelta(days=int(value[1:]))).strftime('%Y-%m-%d')

	# MM-DD format (e.g., '4-11')
	elif '-' in value and value.count('-') == 1 and all(part.isdigit() for part in value.split('-')):
		month, day = map(int, value.split('-'))
		try:
			target = datetime.date(today.year, month, day)
			if target > today:
				target = datetime.date(today.year - 1, month, day)
			return target.strftime('%Y-%m-%d')
		except:
			raise ValueError("Invalid MM-DD date.")

	# Day of current month: '-11'
	elif value.startswith('-') and value[1:].isdigit():
		day = abs(int(value))
		try:
			return datetime.date(today.year, today.month, day).strftime('%Y-%m-%d')
		except:
			raise ValueError("Invalid day for current month.")

	# Days ago: '0', '1', '10' etc.
	elif value.isdigit():
		return (today - datetime.timedelta(days=int(value))).strftime('%Y-%m-%d')

	raise ValueError("Unsupported input format.")



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
def saveLine(log, *items, p=False):
	if os.path.isfile(log):
		log = __.path(log)
	if not _v.slash in log:
		e('First arg is log path')
	_v.mkdir(log,pop=True)

	try:
		tab_delimited_items = '\t'.join(map(str, items))
		with open(log, 'a') as log_file:
			log_file.write(f'{tab_delimited_items}\n')
		if p:
			pr('Saved', c='green')
		return True
	except Exception as ee:
		e(f"Error appending to log file: {ee}")
		return False

line=saveLine
##################################################
# self.value('Help')
# 'DumpSwitches'
# __.switch_skimmer.active
# 11780
# if switches.isActive('Plus-single'): break
# dict_to_markdown_table
# sys.stdin.readlines()
########################################################################################
import os
import time

def bkExpire(file, backup, age='1d', p=0, pCP=1,ago=None,cp=None,force=False):
	import shutil
	if not ago is None: age=ago
	file_path = file
	backup_path = backup
	age_in_epoch = timeAgo(age)

	if not os.path.exists(file_path):
		if p:
			print(f"Error: File '{file_path}' does not exist.")
		return False
	
	if os.path.isfile(backup_path):
		file_mod_time = os.path.getmtime(backup_path)

	if force or not os.path.isfile(backup_path)   or   file_mod_time < age_in_epoch:
		_v.mkdir(backup_path,pop=True)
		shutil.copy2(file_path, backup_path)
		if p or pCP:
			print(f"Backup created: '{file_path}' -> '{backup_path}'")
		if cp:
			bk = create_backup_filename(file_path,cp)
			_v.mkdir(bk,pop=True)
			shutil.copy2(file_path, bk)
		return True
	else:
		if p:
			print(f"No backup needed. The file '{file_path}' is not older than the specified age.")
		return False




########################################################################################
import os
import re
import time

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
def md(path,change=None):
	if not change is None:
		changeM(path,change)
	return os.path.getmtime(path)
def cd(path): return os.path.getctime(path)
########################################################################################
def tableGet(path):
	"""
	Try loading a JSON file using various parsers, returning immediately on success.
	
	Args:
		path (str): The path to the JSON or HAR file.
	
	Returns:
		dict: Parsed JSON data.
	"""
	parsers = []

	# Try importing each JSON module
	try:
		import orjson
		parsers.append(("orjson", lambda f: orjson.loads(f.read()), "rb"))
	except ImportError:
		pass

	try:
		import ujson
		parsers.append(("ujson", lambda f: ujson.load(f), "r"))
	except ImportError:
		pass

	try:
		import simplejson as json
		parsers.append(("simplejson", lambda f: json.load(f), "r"))
	except ImportError:
		import json
		parsers.append(("json", lambda f: json.load(f), "r"))

	# Try each parser and return immediately on success
	for name, parser, mode in parsers:
		try:
			with open(path, mode, encoding=None if mode == "rb" else "utf-8") as f:
				data = parser(f)
			# print(f"Loaded with {name}")
			return data  # Return immediately on success
		except Exception as e:
			print(f"Failed with {name}: {e}")

	raise RuntimeError("All JSON parsers failed.")

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
##################################################
def isFile2(fileAliasUrl):
	ref = fileAliasUrl
	del fileAliasUrl

	if os.path.isfile(ref): return ref
	if ref.startswith('http:') or ref.startswith('https:'):
		ref = autoUrl(ref)
	aliases=getTable('file-open-aliases.hash')

	if 'aliases' in aliases and not ref in aliases['aliases']:
		return aliases['aliases'][ref]
	
	return ref

def aliasList(ref,p=False,d=None):
	ref = isFile(ref)
	aliases=getTable('file-open-aliases.hash')
	if 'files' in aliases and ref in aliases['files']:
		if p:
			for x in aliases['files']:
				pr(x)
		return aliases['files'][ref]
	else:
		# d = Default Value
		return d
		


##################################################

def spliter(text, delimiters):
	delimiters = delimiters.replace(' |', '|').replace('| ', '|')
	"""
	Splits `text` by multiple substrings provided in `delimiters`, separated by '|'.
	
	Args:
		text (str): The input string to split.
		delimiters (str): A string of delimiters separated by '|', e.g., "123|XYZ|-|Mango".
	
	Returns:
		list: A list of split substrings.
	"""
	pattern = '|'.join(map(re.escape, delimiters.split('|')))  # Escape special characters
	return [s for s in re.split(pattern, text) if s]  # Remove empty strings

# # Example usage
# text = "apple123bananaXYZorange-MangoPineapple"
# delimiters = "123|XYZ|-|Mango"

# result = split_by_multiple(text, delimiters)
# print(result)

##################################################
	# Equivalent windows type command stripping invalid characters


def Type(file_path):
	"""
	Mimics the Windows `type` command:
	- Reads the file as raw text
	- Outputs exactly as-is (no extra encoding issues)
	- Ensures `>` and `|` work correctly
	"""
	if not file_path or not isinstance(file_path, (str, bytes, os.PathLike)):
		sys.stderr.flush()
		return ''

	if not os.path.isfile(file_path):
		sys.stderr.write(f"Error: File '{file_path}' not found.\n")
		sys.stderr.flush()
		return ''

	try:
		with open(file_path, "rb") as file:  # Open in binary mode to prevent encoding issues
			while True:
				chunk = file.read(4096)
				if not chunk:
					break
				sys.stdout.buffer.write(chunk)  # Write raw bytes directly to stdout
				sys.stdout.flush()  # Ensure immediate output
		return ''
	except Exception as e:
		sys.stderr.flush()
		return ''

		


##################################################
class Pressed:
	ctypes = None
	keyboard = None
	pynput_kb = None
	pynput_available = None

	@classmethod
	def __init_once(cls):
		if cls.ctypes is None:
			import ctypes
			cls.ctypes = ctypes
		if cls.keyboard is None:
			try:
				import keyboard  # type: ignore
				cls.keyboard = keyboard
			except ImportError:
				cls.keyboard = None
		if cls.pynput_available is None:
			try:
				from pynput.keyboard import Controller as PynputKeyboard, Key  # type: ignore
				cls.pynput_kb = PynputKeyboard()
				cls.pynput_available = True
			except ImportError:
				cls.pynput_available = False

	@classmethod
	def key(cls, key):
		cls.__init_once()

		vk_codes = {
			'shift': 0x10,
			'left shift': 0xA0,
			'right shift': 0xA1,
			'ctrl': 0x11,
			'left ctrl': 0xA2,
			'right ctrl': 0xA3,
			'alt': 0x12,
			'left alt': 0xA4,
			'right alt': 0xA5,
			'caps lock': 0x14,
			'esc': 0x1B,
			'tab': 0x09,
			'enter': 0x0D,
			'space': 0x20,
			'backspace': 0x08,
			'insert': 0x2D,
			'delete': 0x2E,
			'home': 0x24,
			'end': 0x23,
			'page up': 0x21,
			'page down': 0x22,
			'left': 0x25,
			'up': 0x26,
			'right': 0x27,
			'down': 0x28,
			'win': 0x5B,
			'num lock': 0x90,
			'scroll lock': 0x91,
		}

		key_lower = key.lower()
		vk = vk_codes.get(key_lower)
		win_state = False
		kb_state = False
		pynput_state = False

		# 1. Windows low-level check
		try:
			if vk is not None:
				win_state = cls.ctypes.windll.user32.GetKeyState(vk) & 0x8000 != 0
		except:
			pass

		# 2. Keyboard module check
		if cls.keyboard:
			try:
				kb_state = cls.keyboard.is_pressed(key)
			except:
				kb_state = False

		# 3. Pynput fallback check
		if cls.pynput_available:
			try:
				pynput_state = key in str(cls.pynput_kb.pressed_keys)
			except:
				pynput_state = False

		return win_state or kb_state or pynput_state

##################################################
__.KeyMonActive = True
class KeyMon:
	def __init__(self, listen=None, p=None, kill=['esc','f1'], strict=False):
		import keyboard  # type: ignore
		import threading
		self.threading = threading
		self.keyboard = keyboard

		if type(kill) == str:
			kill = kill.replace(' ','')
			kill = kill.split(',')

		self.kill = kill

		self.strict = strict
		self.strictWait = .01

		self.print = None
		if not listen is None:
			self.listen = listen
			self.print = False
		else:
			self.listen = {}

		if not p is None:
			self.print = p
		elif not self.print is None and not self.print == False:
			self.print = True

		self.pressed_keys = []
		self.shutdown_flag = False
		self.pause = False
		self.start()

	def on_key_press(self, event):
		if self.shutdown_flag: return None
		if self.pause: return None
		if not event.name in self.pressed_keys:
			self.pressed_keys.append(event.name)
		self.listener(event.name)
		if self.print:
			if False:
				if __.keyListener:
					print('Pressed:', ' + '.join(sorted(self.pressed_keys)))
			else:
				print('Pressed:', ' + '.join(sorted(self.pressed_keys)))

	def on_key_release(self, event):
		if self.shutdown_flag: return None
		if self.pause: return None
		# Remove keys that are no longer physically pressed
		self.pressed_keys.remove(event.name)
		self.cleanup()


	def cleanup(self):
		self.pressed_keys = [k for k in self.pressed_keys if Pressed.key(k)]
		def watch_caps():
			cnt = 0
			pre = len(self.pressed_keys)
			while cnt < 3:
				if self.shutdown_flag: return None
				time.sleep(self.strictWait)
				self.pressed_keys = [k for k in self.pressed_keys if Pressed.key(k)]
				time.sleep(self.strictWait)
				self.pressed_keys = [k for k in self.pressed_keys if Pressed.key(k)]
				cnt += 1
			# if not pre == len(self.pressed_keys):
			# 	pr('KeyMon: Cleaned',c='red')
		if self.strict:
			self.threading.Thread(target=watch_caps, daemon=True).start()
		if self.pause:
			# pr('Unpaused',c='green')
			self.pause = False


	def listener(self,key):
		if self.shutdown_flag: return None
		if self.pause: return None
		if self.strict:
			time.sleep(self.strictWait)
			self.pressed_keys = [k for k in self.pressed_keys if Pressed.key(k)]

		completed = False
		
		if len(self.listen.keys()) == 1:
			for k in self.listen:
				if key == k:
					self.pause = True
					try:
						self.listen[k]()
					except:
						pass
				
		if not completed:
			for key_combo, fn in self.listen.items():
				if self.shutdown_flag: return None
				required_keys = [k.strip().lower() for k in key_combo.split(',')]
				cnt = sum(1 for k in required_keys if k in self.pressed_keys)
				if cnt == len(required_keys):
					self.pause = True
					try:
						fn()
					except:
						pass
		self.cleanup()
		if self.pause:
			if key in self.pressed_keys:
				self.pressed_keys.remove(key)
			pr('Unpaused',c='red')
			self.pause = False

	def run(self):
		if self.pause: return None
		if self.shutdown_flag: return None
		self.keyboard.on_press(self.on_key_press)
		self.keyboard.on_release(self.on_key_release)
		try:
			while not self.shutdown_flag:
				if not __.KeyMonActive: self.shutdown_flag = True
				if self.pause: return None
				active = 0
				for key in self.kill:
					if self.keyboard.is_pressed(key):
						active += 1
				if active == len(self.kill):
					self.shutdown_flag = True
					pr('KeyMon: Shutdown',c='red')
					break
				if self.shutdown_flag: return None
		except KeyboardInterrupt:
			self.shutdown_flag = True
			pr('KeyMon: Interrupted by Ctrl+C', c='Background.red')

	def start(self):
		self.shutdown_flag = False
		t = self.threading.Thread(target=self.run, daemon=True)
		t.start()
		return t

	def stop(self):
		# print('stopped')
		self.shutdown_flag = True






	
def KeyWait(what='f1',p=True,strict=False):
	if type(what) == int or type(what) == bool: what = 'f1'
	__.WaitForThis = False
	def ThisStops():
		__.WaitForThis = True
	km = KeyMon({what:ThisStops},strict=strict)
	if p:
		pr('Waiting for:',what,c='Background.blue')
	try:
		while not __.WaitForThis:
			time.sleep(.1)
	except KeyboardInterrupt:
		pr('Interrupted by Ctrl+C', c='Background.red')
		return
	if p:
		pr('Waiting Complete',c='Background.blue')

WaitFor=KeyWait

class Skip:
	def __init__(self,what='f1',label='Skipped',p=True):
		self.skip = False
		self.label = label
		self.print = p
		self.KeyMon = KeyMon({what:self.onActivation},strict=True)

	def status(self):
		return self.skip
	
	def onActivation(self):
		self.skip = True
		if self.print and self.label:
			pr(self.label,c='red')




# _.KeyMon.listen = {
# 	'ctrl,z': test,
# }
# KeyMon.app()
##################################################
import time

winSound = None

class beep:
	def __init__(self, key=1, wait=.1, warmup=True, p=False, label=None, c='cyan'):
		self.key = key
		self.wait = wait
		self.warmup = warmup
		self.print = p
		self.label = label
		self.color = c
		self.freq = self.tones().get(str(key), 400)

		global winSound
		if winSound is None:
			import winsound
			winSound = winsound

		if self.warmup:
			self.preLoad()

	def preLoad(self):
		# Use a short, real beep to initialize the sound system
		try:
			winSound.Beep(440, 50)  # 440 Hz is reliably audible
			if self.wait:
				time.sleep(0.2)
		except RuntimeError:
			pr('Beep Error',c='red')

	def tones(self):
		return {
			'1': 500,
			'2': 600,
			'3': 700,
			'4': 800,
			'5': 900,
			'6': 1000,
			'7': 1100,
			'8': 1200,
			'9': 1300,
			'10': 1400,
		}


	def play(self, t=None, d=300, label=None,c=None):
		color = self.color
		if not c is None: color = c
		if label is None: label = self.label
		global winSound
		if winSound is None:
			import winsound
			winSound = winsound

		freq = self.freq
		if t is None:
			t = self.key
		freq = self.tones().get(str(t), freq)
		if not label is None and self.print:
			pr(label, t, c=color)
		elif not label is None:
			pr(label, c=color)
		elif self.print:
			pr(t, c=color)
		winSound.Beep(freq, d)
		if self.wait:
			time.sleep(self.wait)
	def multi(self,keys='234', d=300, label=None,c=None):
		if not self.wait: self.wait = .1
		for key in list(keys):
			self.play(key, d, label,c)
			



def Notify(label=None,c='yellow', Exit=False):
	global notify

	if Exit == 'Force':
		Exit = True
		if not notify.run: notify.run = True
		if not notify.run: notify.run = True

	if Exit and not notify.run: return None
	if Exit and notify.run:
		label = notify.message
		c = notify.color
	if label is None: label = 'Notification'
	bp = beep()
	if not label is None:
		pr(label,c=c)
	time.sleep(.1)
	bp.multi()

def Beep(waitToStart=1,wait=1):
	bp = beep(wait=.1, p=True)
	bp.play( 1 )
	bp.play( 2 )
	bp.play( 3 )
	bp.play( 4 )
	bp.play( 5 )
	bp.play( 6 )
	bp.play( 7 )
	bp.play( 8 )
	bp.play( 9 )
	bp.play( 10 )



##################################################
class ThreadManager:
	def __init__(self, threads=10, timeout=None, onDone=None, t=None):
		if not t is None: threads = t
		import threading
		import queue
		import time
		import traceback

		# Internalized modules
		self._threading = threading
		self._queue = queue
		self._time = time
		self._traceback = traceback

		self.max_threads = threads
		self.global_timeout = timeout
		self.onAllDone = onDone

		self._lock = threading.Lock()
		self._job_queue = queue.Queue()
		self._scheduled = []
		self._stop_flag = False

		# Runtime stats
		self.active_count = 0
		self.total_started = 0
		self.total_completed = 0
		self.total_killed = 0
		self.total_timeout = 0
		self.job_log = []
		self.report = []

		self._manager_thread = threading.Thread(target=self._manager_loop, daemon=True)
		self._manager_thread.start()

	def queue(self, fn, ak=None, timeout=None, onStart=None, onDone=None, onKill=None, onTimeout=None, label=None):
		argsKwargs = ak
		job = {
			"fn": fn,
			"start": self._time.time(),
			"args": argsKwargs if isinstance(argsKwargs, tuple) else (),
			"kwargs": argsKwargs if isinstance(argsKwargs, dict) else {},
			"timeout": timeout,
			"onStart": onStart,
			"onDone": onDone,
			"onKill": onKill,
			"onTimeout": onTimeout,
			"label": label or f"job-{self.total_started + 1}"
		}
		self._scheduled.append(job)
		self._job_queue.put(job)

	def _manager_loop(self):
		while not self._stop_flag:
			if self.active_count < self.max_threads:
				try:
					job = self._job_queue.get(timeout=0.1)
				except self._queue.Empty:
					if self._scheduled == [] and self.active_count == 0 and self.onAllDone:
						self.onAllDone()
					continue
				self._threading.Thread(target=self._run_job, args=(job,), daemon=True).start()
			else:
				self._time.sleep(0.01)

	def _run_job(self, job):
		label = job["label"]
		start_time = self._time.time()

		with self._lock:
			self.active_count += 1
			self.total_started += 1

		fn = job["fn"]
		args = job["args"]
		kwargs = job["kwargs"]
		timeout = job["timeout"] if job["timeout"] is not None else self.global_timeout

		start_cb = job["onStart"]
		done_cb = job["onDone"]
		kill_cb = job["onKill"]
		timeout_cb = job["onTimeout"]

		result = None
		error = None
		killed = False
		timed_out = False

		if start_cb:
			try:
				start_cb()
			except Exception:
				self._traceback.print_exc()

		def target_fn():
			nonlocal result, error
			try:
				result = fn(*args, **kwargs)
			except Exception as e:
				error = e

		t = self._threading.Thread(target=target_fn)
		t.start()
		t.join(timeout)

		status = "completed"

		if t.is_alive():
			timed_out = True
			killed = True
			status = "timeout"
			with self._lock:
				self.total_timeout += 1
			if timeout_cb:
				try:
					timeout_cb()
				except Exception:
					self._traceback.print_exc()
		elif error:
			killed = True
			status = "killed"
			with self._lock:
				self.total_killed += 1
			if kill_cb:
				try:
					kill_cb()
				except Exception:
					self._traceback.print_exc()
		else:
			with self._lock:
				self.total_completed += 1
			if done_cb:
				try:
					done_cb(result)
				except Exception:
					self._traceback.print_exc()

		duration = self._time.time() - start_time
		log_entry = {
			"label": label,
			"status": status,
			"result": str(result) if result is not None else None,
			"error": str(error) if error else None,
			"duration": round(duration, 3)
		}

		with self._lock:
			self.active_count -= 1
			self.job_log.append(log_entry)

		if self._scheduled:
			self._scheduled.pop(0)

		if self._scheduled == [] and self.active_count == 0 and self.onAllDone:
			self.onAllDone()

	def stats(self):
		with self._lock:
			return {
				"active": self.active_count,
				"total_started": self.total_started,
				"total_completed": self.total_completed,
				"total_killed": self.total_killed,
				"total_timeout": self.total_timeout,
				"log": list(self.job_log)
			}

	def stop(self):
		self._stop_flag = True

	# Threads = _.Threads(t=10, onDone=None)
	# def Done(result): pass  # other onFn have no args
	# Threads.queue(fn,  ak=None, timeout=None, onStart=None, onDone=Done, onKill=None, onTimeout=None, label=None)  # ak = args, kwargs
##################################################
def stack(name,download=False):
	def updateStack():
		import simplejson as json
		Json = _.URL( _v.fig['stack']+'load.php',{'api':_v.fig['stack-api']})
		if not Json.strip():
			_.pr('No stack found')
			sys.exit(0)
		saveTableDB(Json,'stack')
		return json.loads(Json)
	if download:
		updateStack()
	Stack = getTableDB('stack')
	if not Stack and not download:
		Stack = updateStack()
	if name in Stack:
		return Stack[name]
	else:
		return ''
##================================================
def getJsonYaml(path):
	contents = getText(path,raw=True).strip()
	if contents.startswith('{') or contents.startswith('['):
		return getTable2(path)
	return fromYML(contents)
##================================================
def cli(command):
	import subprocess
	result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return result.stdout.strip().splitlines()
CMD=cli
term=CMD
terminal=CMD
##================================================
def get_namespace_contents(namespace=None, path='', seen=None, dirty=False, d=None):
	if not d is None:
		dirty = d
	if namespace is None:
		namespace = globals()

	if type(namespace) == str:
		path = namespace
		namespace = eval(namespace)

	if seen is None:
		seen = set()

	if not isinstance(namespace, (dict, object)):
		return {path or '<root>': f'Invalid namespace: {namespace}'}

	if id(namespace) in seen:
		return {path or '<root>': 'Circular reference'}

	seen.add(id(namespace))
	result = {}

	try:
		keys = list(namespace.keys()) if isinstance(namespace, dict) else dir(namespace)
	except Exception:
		return {path or '<root>': 'uninspectable'}

	for key in keys:
		if isinstance(namespace, dict):
			try:
				value = namespace[key]
			except Exception:
				continue
		else:
			if key.startswith('__') and key.endswith('__'):
				continue
			try:
				value = getattr(namespace, key)
			except Exception:
				result_key = f'{path}.{key}' if path else key
				result[result_key] = 'unreachable'
				continue

		result_key = f'{path}.{key}' if path else key
		result[result_key] = type(value).__name__

		if isinstance(value, (dict, object)) and not isinstance(value, (str, int, float, bool, bytes, bytearray)):
			if not isinstance(value, (type, type(get_namespace_contents))):
				try:
					nested = get_namespace_contents(value, result_key, seen)
					result.update(nested)
				except Exception:
					result[f'{result_key}._error'] = 'recursion failed'
	if not dirty:
		cleaned = {}
		for k in result:
			pr = True
			for y in ['.__.','._v.']:
				if y in k:
					pr = False
			if pr:
				cleaned[k] = result[k]
		result = cleaned
	return result

ns=get_namespace_contents
def nsKeys(namespace=None, path='', seen=None, dirty=False, d=None):
	x=get_namespace_contents(namespace=namespace, path=path, seen=seen, dirty=dirty, d=d)
	# _.pv(x)
	for k in x:
		if showLine(k):
			pr(k)
nsKey=nsKeys
nsk=nsKeys
##================================================


def Import(path, module_name=None):
	"""
	Import a Python module from a full path.

	Args:
		path (str): Full path to .py file or package directory.
		module_name (str, optional): Name for the imported module.
									 If omitted, a unique hash will be used.

	Returns:
		module or None if failed
	"""

	import os
	import sys
	import importlib.util
	import hashlib

	if not os.path.isfile(path):
		return False

	try:
		path = os.path.abspath(path)

		# Resolve file from directory or auto-add .py
		if os.path.isdir(path):
			target = os.path.join(path, '__init__.py')
			if not os.path.isfile(target):
				return None
		else:
			if not path.endswith('.py'):
				path += '.py'
			if not os.path.isfile(path):
				return None
			target = path

		# Auto-generate a unique name if none given
		if not module_name:
			hash_name = hashlib.md5(target.encode()).hexdigest()
			module_name = f'module_{hash_name[:8]}'

		spec = importlib.util.spec_from_file_location(module_name, target)
		if spec is None or spec.loader is None:
			return None

		module = importlib.util.module_from_spec(spec)
		sys.modules[module_name] = module
		spec.loader.exec_module(module)

		return module

	except Exception:
		return None


##================================================
##================================================

import os
import time
import re


class Touch:
	base_dir = os.path.normpath(os.path.expanduser(os.path.expandvars('~/.rt/Scheduled/touch')))
	durations = {
		's': 1, 'sec': 1, 'secs': 1, 'second': 1, 'seconds': 1,
		'n': 60, 'mn': 60, 'min': 60, 'mins': 60, 'minute': 60, 'minutes': 60,
		'h': 3600, 'hr': 3600, 'hrs': 3600, 'hour': 3600, 'hours': 3600,
		'd': 86400, 'day': 86400, 'days': 86400,
		'w': 604800, 'week': 604800, 'weeks': 604800,
		'm': 2592000, 'mo': 2592000, 'month': 2592000, 'months': 2592000,
		'y': 31536000, 'yr': 31536000, 'yrs': 31536000, 'year': 31536000, 'years': 31536000,
	}

	@staticmethod
	def _get_path(name):
		os.makedirs(Touch.base_dir, exist_ok=True)
		return os.path.join(Touch.base_dir, f"{name}.touch")

	@staticmethod
	def touch(name):
		"""Create or update a touch file with current time."""
		path = Touch._get_path(name)
		with open(path, 'a'):
			os.utime(path, None)

	@staticmethod
	def read(name,path=None):
		"""Return last modified time as datetime, or None if missing."""
		from datetime import datetime, timedelta
		if path is None:
			path = Touch._get_path(name)
		if os.path.exists(path):
			ts = os.path.getmtime(path)
			return datetime.fromtimestamp(ts)
		return None

	@staticmethod
	def schedule(name, interval='3h'):
		"""Returns True if task is due to run based on interval."""
		from datetime import datetime, timedelta
		if os.path.isfile(name):
			path = name
			name = os.path.splitext(path)[0]
		name = name.replace(' ', '_')
		last = Touch.read(name, path)
		if last is None:
		
			Touch.touch(name)
			return True
		threshold = datetime.now() - timedelta(seconds=Touch.parse_duration(interval))
		if last < threshold:
			if path is None:
				Touch.touch(name)
			return True
		return False

	@staticmethod
	def parse_duration(s):
		"""Parses durations like '1d 3h' to total seconds."""
		s = s.lower().strip()
		total = 0
		matches = re.findall(r'([-+]?\d*\.?\d+)\s*([a-z]+)', s)
		for num, unit in matches:
			if unit in Touch.durations:
				total += float(num) * Touch.durations[unit]
		return int(total)



'''
_.Touch.touch('win_cron_3hr')

if _.Touch.schedule('backup', interval='3h'):
	print("Running backup task...")
	# Do your backup here
else:
	print("Skip — already ran recently.")


if _.Touch.schedule(path, interval='3h'):
	pass
'''

##================================================
##================================================
def y(yaml,p=False):
	while ' ||' in yaml:
		yaml = yaml.replace(' ||', '||')
	while '|| ' in yaml:
		yaml = yaml.replace('|| ', '||')
	yaml = yaml.replace('||','|')
	yaml = yaml.replace('|','\n')
	if p:
		print(yaml)
	return fromYML(yaml)


##================================================
##================================================

def defaultDics(appReg=None,info={},data={},path=None):
	if appReg is None:
		appReg = __.appReg
	file = _v.py+os.sep
	if not path is None:
		if os.sep in path:
			file = path
		else:
			file += path
	elif 'file' in info:
		file += info['file']
	else:
		file+='thisApp.py'
	if not file.endswith('.py'):
		file += '.py'
	global appInfo
	global appData
	appInfo[appReg] = {
		'file': 'thisApp.py',
		'liveAppName': __.thisApp( file ),
		'description': 'Changes the world',
		'categories': [],
		'usage': [],
		'relatedapps': [],
		'prerequisite': [],
		'examples': [],
		'columns': [],
		'aliases': [],
		'notes': [],
	}
	appData[appReg] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] },
					'table': {'sent': [], 'received': [] }, 
		},
	}
	for k in info: appInfo[k] = info[k]
	for k in data: appData[k] = data[k]


def psudoAppTriggers():
	global switches
	_default_triggers_()
	switches.trigger( 'Files',   isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	switches.trigger( 'DB', aliasesFi )
	switches.trigger( 'Folder', myFolderLocations )
	switches.trigger( 'Folders', myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = myFolder
	switches.trigger( 'OutputFolder', aliasesFo )

def psudoApp(appReg,dic):
	parent = __.appReg
	regApp = __.appName(appReg, parent)
	__.appReg = regApp
	info = dic.get('info',{})
	data = dic.get('data',{})
	path = dic.get('path',None)

	defaultDics(appReg,info,data,path)
	sw = dic.get('switches',{})
	global switches
	for k in sw:
		switches.register( k, 'd5d578c8')
	l_registerSwitches_vars()

	for k in sw:
		switches.fieldSet(k,'active', True)
		switches.fieldSet(k,'values', sw[k])
		switches.fieldSet(k,'value', ','.join(sw[k]))
	__.appReg = parent






##================================================
##================================================
def clear_screen():
	if sys.platform == "win32":
		os.system("cls")
	else:
		# Try 'clear', fallback to 'cls'
		if os.system("clear") != 0:
			os.system("cls")

def noWarnings():
	import warnings
	warnings.filterwarnings("ignore", category=DeprecationWarning)

def print_markdown(arg):
	if os.path.isfile(arg):
		document = getText(arg, raw=True)
	else:
		document = arg
	if not document:
		pr('No Markdown Document Found', c='red')
		return False
	# noWarnings()

	import warnings
	with warnings.catch_warnings():
		warnings.simplefilter("ignore", DeprecationWarning)
		from cgi import parse_header, parse_multipart

	from rich.console import Console # type: ignore
	from rich.markdown import Markdown # type: ignore
	console = Console()
	
	
	clear_screen()


	console.print(Markdown(document))
	return True

##================================================
##================================================

def _autoDate(data, fail=False):
	try:
		import datefinder # type: ignore
		matches = list(datefinder.find_dates(str(data)))
		if matches:
			return matches[0].timestamp()
	except Exception:
		pass

	if isinstance(data, (int, float)):
		if int(data) > 1000000000:
			if int(data) > 9999999999:
				return int(data) / 1000
			return int(data)
		else:
			return False

	try:
		s = str(data).strip()
		s = s.replace('T', ' ').split('+')[0].split('Z')[0].strip()
		if any(x in s.lower() for x in ['am', 'pm']):
			try:
				dt = datetime.datetime.strptime(s, '%Y-%m-%d %I:%M:%S %p')
				return dt.timestamp()
			except Exception:
				pass
			try:
				dt = datetime.datetime.strptime(s, '%Y-%m-%d %I:%M %p')
				return dt.timestamp()
			except Exception:
				pass

		# Try ISO standard
		try:
			dt = datetime.datetime.fromisoformat(s)
			return dt.timestamp()
		except Exception:
			pass

		# Try some common formats
		for fmt in [
			'%Y-%m-%d %H:%M:%S',
			'%Y-%m-%d %H:%M',
			'%Y-%m-%d',
			'%m/%d/%Y',
			'%m/%d/%y',
			'%d-%m-%Y',
			'%d/%m/%Y',
			'%b %d %Y',
			'%B %d %Y',
			'%b %d, %Y',
			'%B %d, %Y',
		]:
			try:
				dt = datetime.datetime.strptime(s, fmt)
				return dt.timestamp()
			except Exception:
				continue

		# If still looks numeric
		if s.isdigit():
			if len(s) > 10:
				return int(s) / 1000
			return int(s)

	except Exception as e:
		if fail:
			raise e
		return False

	if fail:
		raise Exception('Could not parse date')
	return False
##================================================

##================================================

def _ago(text, when=None):
	import datetime
	import time
	import re

	dt = _autoDate(text)
	if dt:
		return dt

	text = text.strip().lower()
	if when is None:
		when = time.time()
	now = when

	# Fast path: months
	if text.endswith('m') and text[:-1].isdigit():
		number = int(text[:-1])
		now_dt = datetime.datetime.fromtimestamp(now)
		year = now_dt.year
		month = now_dt.month - number  # subtract months for "ago"

		while month <= 0:
			month += 12
			year -= 1

		days_in_month = [
			31,
			29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
			31, 30, 31, 30, 31, 31, 30, 31, 30, 31
		]
		day = min(now_dt.day, days_in_month[month - 1])
		new_dt = datetime.datetime(year, month, day, now_dt.hour, now_dt.minute, now_dt.second)
		return int(new_dt.timestamp())

	units = {
		's': 1, 'sec': 1, 'secs': 1, 'second': 1, 'seconds': 1,
		'min': 60, 'mins': 60, 'minute': 60, 'minutes': 60,
		'h': 3600, 'hr': 3600, 'hrs': 3600, 'hour': 3600, 'hours': 3600,
		'd': 86400, 'day': 86400, 'days': 86400,
		'w': 604800, 'wk': 604800, 'wks': 604800, 'week': 604800, 'weeks': 604800,
		'y': 31536000, 'yr': 31536000, 'yrs': 31536000, 'year': 31536000, 'years': 31536000,
	}

	match = re.match(r'^(\d+)\s*([a-z]+)$', text)
	if not match:
		raise ValueError(f"Invalid format: {text}")

	number = int(match.group(1))
	unit = match.group(2)
	unit = unit.rstrip('s')  # normalize plurals

	if unit not in units:
		raise ValueError(f"Unknown time unit: {unit}")

	seconds = number * units[unit]
	return int(now - seconds)  # subtract for past


def _future(text, when=None):
	import datetime
	import time
	import re

	dt = _autoDate(text)
	if dt:
		return dt
	text = text.strip().lower()
	if when is None:
		when = time.time()
	now = when

	# Fast path: if it ends with 'm', assume month first
	if text.endswith('m') and text[:-1].isdigit():
		number = int(text[:-1])
		now_dt = datetime.datetime.fromtimestamp(now)
		year = now_dt.year
		month = now_dt.month + number

		while month > 12:
			month -= 12
			year += 1

		days_in_month = [
			31,
			29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
			31, 30, 31, 30, 31, 31, 30, 31, 30, 31
		]
		day = min(now_dt.day, days_in_month[month - 1])
		new_dt = datetime.datetime(year, month, day, now_dt.hour, now_dt.minute, now_dt.second)
		return int(new_dt.timestamp())

	units = {
		's': 1, 'sec': 1, 'secs': 1, 'second': 1, 'seconds': 1,
		'min': 60, 'mins': 60, 'minute': 60, 'minutes': 60,
		'h': 3600, 'hr': 3600, 'hrs': 3600, 'hour': 3600, 'hours': 3600,
		'd': 86400, 'day': 86400, 'days': 86400,
		'w': 604800, 'wk': 604800, 'wks': 604800, 'week': 604800, 'weeks': 604800,
		'y': 31536000, 'yr': 31536000, 'yrs': 31536000, 'year': 31536000, 'years': 31536000,
	}

	match = re.match(r'^(\d+)\s*([a-z]+)$', text)
	if not match:
		raise ValueError(f"Invalid format: {text}")

	number = int(match.group(1))
	unit = match.group(2)

	unit = unit.rstrip('s')  # allow plural forms like "hours", "minutes"

	if unit not in units:
		raise ValueError(f"Unknown time unit: {unit}")

	seconds = number * units[unit]
	return int(now + seconds)






##================================================
##================================================
#START-PALLETTS

ColorPallets = {
	"forest": {
		"primary": "#3CB371",
		"secondary": "#2E8B57",
		"success": "#00FA9A",
		"danger": "#CD5C5C",
		"warning": "#DAA520",
		"info": "#40E0D0"
	},
	"ocean": {
		"primary": "#1E90FF",
		"secondary": "#006994",
		"success": "#00CED1",
		"danger": "#FF6F61",
		"warning": "#FFA500",
		"info": "#00BFFF"
	},
	"desert": {
		"primary": "#D4A373",
		"secondary": "#8B5E34",
		"success": "#7CB342",
		"danger": "#C84B31",
		"warning": "#E0A106",
		"info": "#7AA6C2"
	},
	"sunset": {
		"primary": "#FF7F50",
		"secondary": "#D2691E",
		"success": "#98FB98",
		"danger": "#E63946",
		"warning": "#F4A261",
		"info": "#4CC9F0"
	},
	"glacier": {
		"primary": "#5DADE2",
		"secondary": "#2E86C1",
		"success": "#76D7C4",
		"danger": "#E74C3C",
		"warning": "#F1C40F",
		"info": "#85C1E9"
	},
	"ember": {
		"primary": "#FF6B35",
		"secondary": "#B23A25",
		"success": "#6ECB63",
		"danger": "#D90429",
		"warning": "#FFB703",
		"info": "#34A0A4"
	},
	"royal": {
		"primary": "#4169E1",
		"secondary": "#3B3B98",
		"success": "#2ECC71",
		"danger": "#C0392B",
		"warning": "#F39C12",
		"info": "#1ABC9C"
	},
	"neon": {
		"primary": "#00E5FF",
		"secondary": "#00BFA6",
		"success": "#39FF14",
		"danger": "#FF1744",
		"warning": "#FFD600",
		"info": "#18FFFF"
	},
	"vintage": {
		"primary": "#6B5B95",
		"secondary": "#355C7D",
		"success": "#7FB069",
		"danger": "#B56576",
		"warning": "#EAB464",
		"info": "#82A0BC"
	},
	"cyberpunk": {
		"primary": "#FF00A8",
		"secondary": "#00E5FF",
		"success": "#00FF9C",
		"danger": "#FF3659",
		"warning": "#FFEA00",
		"info": "#7DF9FF"
	},
	"solar": {
		"primary": "#268BD2",
		"secondary": "#6C71C4",
		"success": "#2AA198",
		"danger": "#DC322F",
		"warning": "#B58900",
		"info": "#93A1A1"
	},
	"mono": {
		"primary": "#7F8C8D",
		"secondary": "#95A5A6",
		"success": "#A3BE8C",
		"danger": "#D08770",
		"warning": "#EBCB8B",
		"info": "#88C0D0"
	},
	"citrus": {
		"primary": "#00A86B",
		"secondary": "#7CB518",
		"success": "#2DC653",
		"danger": "#FF4D6D",
		"warning": "#F9C74F",
		"info": "#56CFE1"
	},
	"berry": {
		"primary": "#9932CC",
		"secondary": "#8A2BE2",
		"success": "#66BB6A",
		"danger": "#D81B60",
		"warning": "#F48C06",
		"info": "#4DB6AC"
	},
	"lavender": {
		"primary": "#7C83FD",
		"secondary": "#6F5E76",
		"success": "#7BD389",
		"danger": "#D9534F",
		"warning": "#E9C46A",
		"info": "#A1C6EA"
	},
	"slate": {
		"primary": "#5C7C8A",
		"secondary": "#3E5361",
		"success": "#6DB193",
		"danger": "#E76F51",
		"warning": "#E9C46A",
		"info": "#74A3C7"
	},
	"moss": {
		"primary": "#6B8E23",
		"secondary": "#556B2F",
		"success": "#8FBC8F",
		"danger": "#B23A48",
		"warning": "#C9A227",
		"info": "#70A9A1"
	},
	"canyon": {
		"primary": "#C97D60",
		"secondary": "#8C4A32",
		"success": "#86A873",
		"danger": "#B25036",
		"warning": "#D9A441",
		"info": "#8BAFC8"
	},
	"aurora": {
		"primary": "#7DF9FF",
		"secondary": "#7B2CBF",
		"success": "#80ED99",
		"danger": "#FF4D6D",
		"warning": "#FFD166",
		"info": "#4EA8DE"
	},
	"storm": {
		"primary": "#5B7DB1",
		"secondary": "#3A506B",
		"success": "#79B791",
		"danger": "#C44536",
		"warning": "#E0A458",
		"info": "#5BC0EB"
	},
	"midnight": {
		"primary": "#2D5BFF",
		"secondary": "#1E3A8A",
		"success": "#10B981",
		"danger": "#EF4444",
		"warning": "#F59E0B",
		"info": "#38BDF8"
	},
	"sunrise": {
		"primary": "#FF9E2C",
		"secondary": "#FF7A59",
		"success": "#8CC084",
		"danger": "#E85D75",
		"warning": "#FDB813",
		"info": "#7AB8F5"
	},
	"dune": {
		"primary": "#C2B280",
		"secondary": "#8C7A6B",
		"success": "#7FB77E",
		"danger": "#B3541E",
		"warning": "#D4A017",
		"info": "#8AA6C1"
	},
	"tundra": {
		"primary": "#8DB9CA",
		"secondary": "#5B7C8D",
		"success": "#A8DADC",
		"danger": "#D1495B",
		"warning": "#E9C46A",
		"info": "#7FB3D5"
	},
	"rainforest": {
		"primary": "#2E7D32",
		"secondary": "#1B5E20",
		"success": "#66BB6A",
		"danger": "#C62828",
		"warning": "#F9A825",
		"info": "#26A69A"
	},
	"coral": {
		"primary": "#FF6F61",
		"secondary": "#FF8A65",
		"success": "#81C784",
		"danger": "#D32F2F",
		"warning": "#FFB74D",
		"info": "#4FC3F7"
	},
	"lagoon": {
		"primary": "#2BB2BB",
		"secondary": "#0F8B8D",
		"success": "#59CD90",
		"danger": "#D64550",
		"warning": "#F2C14E",
		"info": "#3AAFA9"
	},
	"eclipse": {
		"primary": "#5E60CE",
		"secondary": "#3A0CA3",
		"success": "#80FFDB",
		"danger": "#FF4D6D",
		"warning": "#FFD166",
		"info": "#72EFDD"
	},
	"blossom": {
		"primary": "#FF99C8",
		"secondary": "#C77DFF",
		"success": "#90BE6D",
		"danger": "#E76F51",
		"warning": "#F9C74F",
		"info": "#43AA8B"
	},
	"terracotta": {
		"primary": "#C3805A",
		"secondary": "#8C4A2F",
		"success": "#8DC07F",
		"danger": "#A23B32",
		"warning": "#D9A441",
		"info": "#7FA6C9"
	},
	"granite": {
		"primary": "#7D7C83",
		"secondary": "#5A5A66",
		"success": "#89B99B",
		"danger": "#C05C5C",
		"warning": "#E0B567",
		"info": "#8CA6BF"
	},
	"willow": {
		"primary": "#7AA874",
		"secondary": "#567568",
		"success": "#9CCC65",
		"danger": "#B23A48",
		"warning": "#CF9F4A",
		"info": "#6FB1BF"
	},
	"autumn": {
		"primary": "#D2691E",
		"secondary": "#8B4513",
		"success": "#9CCC65",
		"danger": "#C0392B",
		"warning": "#E67E22",
		"info": "#A1C6EA"
	},
	"spring": {
		"primary": "#62C370",
		"secondary": "#2D936C",
		"success": "#7EE081",
		"danger": "#F2545B",
		"warning": "#FFD166",
		"info": "#40C9A2"
	},
	"summer": {
		"primary": "#00A8E8",
		"secondary": "#007EA7",
		"success": "#2DD881",
		"danger": "#FF4B5C",
		"warning": "#FFC857",
		"info": "#17BEBB"
	},
	"winter": {
		"primary": "#7FB3D5",
		"secondary": "#5D6D7E",
		"success": "#A3E4D7",
		"danger": "#C0392B",
		"warning": "#F7DC6F",
		"info": "#76D7EA"
	},
	"espresso": {
		"primary": "#6F4E37",
		"secondary": "#4B3A2E",
		"success": "#97A97C",
		"danger": "#A23B3B",
		"warning": "#C4972F",
		"info": "#7A93AC"
	},
	"mint": {
		"primary": "#2EC4B6",
		"secondary": "#2A9D8F",
		"success": "#55D6A0",
		"danger": "#E76F51",
		"warning": "#E9C46A",
		"info": "#4CC9F0"
	},
	"sapphire": {
		"primary": "#2563EB",
		"secondary": "#1E40AF",
		"success": "#10B981",
		"danger": "#DC2626",
		"warning": "#F59E0B",
		"info": "#38BDF8"
	},
	"ruby": {
		"primary": "#C2185B",
		"secondary": "#8E0038",
		"success": "#66BB6A",
		"danger": "#E53935",
		"warning": "#FFC107",
		"info": "#29B6F6"
	},
	"amber": {
		"primary": "#FF8F00",
		"secondary": "#FF6F00",
		"success": "#7CB342",
		"danger": "#E53935",
		"warning": "#FFC400",
		"info": "#4FC3F7"
	},
	"amethyst": {
		"primary": "#9C27B0",
		"secondary": "#6A1B9A",
		"success": "#81C784",
		"danger": "#E57373",
		"warning": "#FFD54F",
		"info": "#64B5F6"
	},
	"charcoal": {
		"primary": "#3C3C3C",
		"secondary": "#2B2B2B",
		"success": "#80BFA5",
		"danger": "#D16060",
		"warning": "#D4A85F",
		"info": "#7FA6C9"
	},
	"steel": {
		"primary": "#5A7D9A",
		"secondary": "#3E5C76",
		"success": "#78C6A3",
		"danger": "#CF5C60",
		"warning": "#E0B44C",
		"info": "#6FA3D0"
	},
	"copper": {
		"primary": "#B87333",
		"secondary": "#7C4A33",
		"success": "#86C06C",
		"danger": "#B23A48",
		"warning": "#D99A36",
		"info": "#7FA6B8"
	},
	"teal": {
		"primary": "#00897B",
		"secondary": "#00695C",
		"success": "#26A69A",
		"danger": "#D84315",
		"warning": "#F9A825",
		"info": "#4DD0E1"
	},
	"orchid": {
		"primary": "#DA70D6",
		"secondary": "#A64CA6",
		"success": "#8DD3C7",
		"danger": "#E85D75",
		"warning": "#FFD166",
		"info": "#80B1D3"
	},
	"sandbar": {
		"primary": "#D4B483",
		"secondary": "#A0744B",
		"success": "#8BB174",
		"danger": "#B24C63",
		"warning": "#E0A458",
		"info": "#7FA6C2"
	},
	"pine": {
		"primary": "#2A6041",
		"secondary": "#184E36",
		"success": "#4E9F3D",
		"danger": "#C44536",
		"warning": "#D4A637",
		"info": "#4AA3A2"
	},
	"horizon": {
		"primary": "#5AA9E6",
		"secondary": "#2D6A8E",
		"success": "#7CCBA2",
		"danger": "#F25F5C",
		"warning": "#F2C14E",
		"info": "#70C1B3"
	},
	"twilight": {
		"primary": "#7C6AFA",
		"secondary": "#444E86",
		"success": "#8BD3A3",
		"danger": "#E76F51",
		"warning": "#F4D35E",
		"info": "#7FBEEB"
	}
}

def Pallet(name=None,color=None,cls=True):
	global ColorPallets

	fix = {
		'p': 'primary',
		's': 'secondary',
		'su': 'success',
		'd': 'danger',
		'w': 'warning',
		'i': 'info',
		'l': 'light',
		'dk': 'dark',
		'link': 'link',
	}

	if name is None:
		if cls:
			clear()
		x = []
		for p in ColorPallets:
			x.append(p)
	
		y = []
		y.append('')
		y.append('Abbreviations:')
		for a in fix:
			y.append( '  '+a+': '+fix[a] )



		# new = {}
		# for p in ColorPallets:
		# 	new[p] = {}
		# 	for c in ColorPallets[p]:
		# 		if not c in 'light dark link'.split(' '):
		# 			new[p][c] = ColorPallets[p][c]
		# pv(new)
		# return



		def fin():
			pr(line=1,c='yellow')
			pr()
			for n in y:
				pr(n,c='cyan')
			pr()
			pr(line=1,c='yellow')
		

		spent = []
		def cycle(pals,pa=True):

			for p in pals:
				if not cls:
					samples = []
					# samples.append(pr('',p, h=ColorPallets[p]['primary'],p=0))
					samples.append(pr(   Align(p,pals)  , h=ColorPallets[p]['primary'],p=0))
					for c in ColorPallets[p]:
						samples.append(pr(c, h=ColorPallets[p][c],p=0))
						
					pr( '  '.join(samples) )
		
					continue
				pr()
				pr()
				pr(p, h=ColorPallets[p]['primary'])

				for c in ColorPallets[p]:
					pr('\t',c, h=ColorPallets[p][c])
				
				if not pa:
					# pr(':')
					pass
				elif pa:
					ask = input(': ').strip()
					if not ask == '':
						if ask.lower() == 'y':
							ask=''
							if not p in tbl:
								tbl.append(p)
								saveTable(tbl,'base__ColorPallets__Favorites.list')
						if ask.lower() == 'r':
							ask=''
							if p in tbl:
								tbl.remove(p) 
								saveTable(tbl,'base__ColorPallets__Favorites.list')
						if ask:
							break
		tbl = getTable('base__ColorPallets__Favorites.list')
		pal = list(ColorPallets.keys())
		import random
		random.shuffle(pal)

		#   

		if tbl:
			if cls:
				pr(line=1,c='green')
			pr('Favorite _.Pallet:\n',c='yellow')
			cycle(tbl,0)
			if not cls:
				return
			for item in tbl:
				if item in pal:
					pal.remove(item)
			pr(line=1,c='green')
			if input(': ').strip(): fin(); return
		
		cycle(pal)
		fin()
		



		# e('Colors',x,y,label='i')
		return

	if color is None:
		for c in ColorPallets[name]:
			pr(c, h=ColorPallets[name][c])
		return

	if color in fix:
		color = fix[color]

	return ColorPallets[name][color]






#END-PALLETTS


##================================================
##================================================
def Align(s: str, items, align: str = "right") -> str:
	"""
	Return the string `s` padded with whitespace according to `align`.

	Args:
		s (str): The string to align.
		items (list[str] or int): A list of strings (align by longest) or an int (fixed width).
		align (str): "left", "right", or "center". Default is "right".

	Returns:
		str: The aligned string.
	"""
	if 'r' in align.lower():
		align = 'right'
	if 'l' in align.lower():
		align = 'left'
	if 'c' in align.lower():
		align = 'center'

	if isinstance(items, int):
		width = items
	elif isinstance(items, (list, tuple)):
		width = max(len(x) for x in items) if items else len(s)
	else:
		raise TypeError("Second argument must be a list of strings or an int")

	if align == "left":
		return s.ljust(width)
	elif align == "right":
		return s.rjust(width)
	elif align == "center":
		return s.center(width)
	else:
		raise ValueError("align must be 'left', 'right', or 'center'")



##================================================
##================================================

class RegID:

	def __init__(self):
		self.IDs = getTable('idResolution.json')

	def save(self):
		saveTable(self.IDs, 'idResolution.json', p=0)

	@classmethod
	def _get_ids(cls, obj=None):
		"""Helper: get IDs whether called as static or instance."""
		if isinstance(obj, cls):  
			return obj.IDs
		else:
			return getTable('idResolution.json')

	@classmethod
	def add(cls, obj_or_id, id=None, label=None, src=None, meta=None, p=False):
		"""
		Can be called as:
			regID.add(id, label)           # static usage
			myreg.add(id, label)           # instance usage
		"""
		if isinstance(obj_or_id, cls):  # instance call
			self = obj_or_id
		else:                           # static call
			self = cls()
			id, label = obj_or_id, id

		if meta is None or not isinstance(meta, dict):
			meta = {}
		if src is not None:
			meta['src'] = src
		meta['epoch'] = meta.get('epoch', time.time())

		rem = self.remove(id)
		if rem and p:
			pr('regID, Replaced:', rem, p='yellow')

		self.IDs.append({'id': id, 'name': label, 'meta': meta})
		saveTable(self.IDs, 'idResolution.json', p=0)
		return id

	@classmethod
	def remove(cls, obj_or_id, id=None):
		if isinstance(obj_or_id, cls):  
			self = obj_or_id
		else:
			self = cls()
			id = obj_or_id

		new = []
		old = {}
		for rec in self.IDs:
			if rec['id'] != id:
				new.append(rec)
			else:
				old = rec

		saveTable(new, 'idResolution.json', p=0)
		self.IDs = new
		return old

	@classmethod
	def strict(cls, obj_or_id, id=None):
		if isinstance(obj_or_id, cls):  
			self = obj_or_id
		else:
			self = cls()
			id = obj_or_id

		for rec in self.IDs:
			if rec['id'] == id:
				return rec
		return None

	@classmethod
	def resolve(cls, obj_or_line, line=None, name=True):
		if isinstance(obj_or_line, cls):  
			self = obj_or_line
		else:
			self = cls()
			line = obj_or_line

		for rec in self.IDs:
			if rec['id'] in line:
				return rec['name'] if name else rec
		return None
	
	@classmethod
	def r(cls, *args, **kwargs):
		return cls.resolve(*args, **kwargs)


##================================================
##================================================
# 9377                    if isFirst:
# 9545                    if isFirst:
# 9590                                                    if isFirst:
##================================================
##================================================
urlPipeActivated=False
def urlPipe(url):
	global appData
	global urlPipeActivated
	urlPipeActivated=True
	if type(url) == list:
		for u in url:
			urlPipe(u)
		return
			
	appData[__.appReg]['pipe'] = URL3(url).split('\n')
pipeUrl=urlPipe
##================================================
##================================================
nsfw=True

Threads=ThreadManager
T=ThreadManager

fd=friendlyDate

responsiveColumns = unixAutoColumns
rc = responsiveColumns

isFileAdvanced=myFileLocations
isFileSimple=isFile

al=aliasList
DB=getTableDB
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
pt=printt #pt==
getYAML2=getYML2
getYAML=getYML
saveYAML=saveYML
saveYAML2=saveYML2
imp=regImp
ago=timeAgo
agoThrow=timeAgoThrow
toBytes=to_bytes
yt=toYML
yf=fromYML
cl=colorList

yFig=_v.yFig
jFig=_v.jFig
__.ci = ci

aFi=aliasesFi
aFo=aliasesFo
pmd=print_markdown
pMD=print_markdown
__.aFi = aFi
__.aFo = aFo
P=Pallet

# ARG = ' '.join(ARG.strip().replace('\t',' ').split()).replace(' ', ',') #   <-------- DELIM




# Import=import_path

##================================================
##################################################
notify = dot()
notify.run = False
notify.message = 'Complete'
notify.color = 'yellow'
##################################################

if os.environ.get('autocls','0') == '1' or os.environ.get('autocls','0').lower() == 'true': os.system('cls')

########################################################################################
# bkExpire(_v.tt+os.sep+'fileBackup.json',_v.tt+os.sep+'fileBackup-bk.json',age='3h',cp=_v.tt+os.sep+'bk'+os.sep+'fileBackup')
# bkExpire(_v.tt+os.sep+'fileBackup.json',_v.tt+os.sep+'fileBackup-bk.json',age='3h',cp=_v.tt+os.sep+'bk'+os.sep+'fileBackup',force=True)
########################################################################################
# EOF