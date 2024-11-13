#!/usr/bin/python3


import os,sys
# print(sys.argv)
# print(sys.argv[-1])
# sys.exit()
_START_OVER=0
_cols_thresh=20
_cols={}
_all_docs={}
_dump=[]
_omit={}


_col1=[]
_col1i={}
_col1_i={}
_blacklist={}
_ids=[]
_folder='C3P0'
mod0=None

def _valid_(mod):
	global _omit
	global _dump
	global _col1
	global _cols_thresh
	global _col1_i
	global _blacklist
	global _ids
	if not '.' in mod: return  True
	if '.' in mod and mod.split('.')[1] in _col1:
		return False
	_m3=mod.split('.')
	_m4=set(_m3)
	_d=len(_m3)-len(_m4)
	if _d > 2:
		for i,foo in enumerate(_m3):
			if i:
				if not i in _cols: _cols[i]={}
				if not foo in _cols[i]: _cols[i][foo]=0
				_cols[i][foo]+=1
				if _cols[i][foo] > _cols_thresh:
					_blacklist[foo]=1
					_omit['.'.join([_m3[0],_m3[1]])]=1
					return False
		_o=[]
		for _m in _m3:
			if mod.count(_m) > 2: _o.append(_m)
		bad=[]
		ii=None
		for i,_po in enumerate(_m3):
			ii=i
			if not _po in _o: bad.append(_po); break;
		if len(_m3) >=ii+1: exec("try:bad.append(_m3[ii+1])\nexcept:pass")

		
		bad_='.'.join(bad)
		if not bad_ in _omit: _omit[bad_]=1
		_ddocs={}
		global _all_docs
		for k in _all_docs:
			if not k == bad_ and not k.startswith(bad_+'.'): _ddocs[k]=_all_docs[k]
			# else: print('-cl-',k)
		_all_docs=_ddocs
	if not _omit: return True
	for k in _omit:
		if k == mod and k.startswith(mod+'.'): return False
	return True




def _audit(mod):
	global _omit
	global _dump
	global _cols
	global _START_OVER
	global _col1
	global _col1i
	global mod0
	global _cols_thresh
	if len(_dump) > 4000:
		_m3=mod.split('.')
		if _START_OVER > 2:
			# for x in _dump: print(x)
			# print('----------------------------')
			# os.system('cls')
			for xx in _all_docs:
				print(xx)
			print(len(_all_docs.keys()))
			sys.exit()
			#################################################################
		_START_OVER+=1
		print('_START_OVER:',_START_OVER)
		one=1
		if not  1 in _cols and '1' in _cols: one='1'
		if one in _cols:
			for ol in _cols[one]:
				if _cols[one][ol] > _cols_thresh:
					_omit['.'.join([_m3[0],_m3[1]])]=1
					if not ol in _col1: _col1.append(ol)
		_cols={}
		# _all_docs={}
		_dump=[]
		mod=mod0
		mod0=None
	return mod





def _doc_(mod):
	mod=_audit(mod)
	global _all_docs
	global _omit
	global _dump
	global _cols
	global mod0
	global _START_OVER
	global _folder
	global _ids
	global _blacklist
	if mod.startswith(tuple(list(_omit.keys()))): return None
	if '.os.' in mod:  return None
	if '.sys.' in mod:  return None
	_m3=mod.split('.')
	if '.'+_m3[0] in mod: return None
	for mo in _m3:
		if mo in _blacklist: return  None
	if mod0 is None: mod0=mod
	children=[]

	if not '.' in mod:
		try:
			exec('_folder='+mod+'.__file__'.split(os.sep)[-1])
			if 'python' in _folder.lower(): _folder='C3P0'
		except: _folder='C3P0'
	elif '.' in mod and not _folder == 'C3P0':
		_fo='R2D2'
		try:
			exec('_folder='+mod+'.__file__'.split(os.sep)[-1])
			if 'python' in _folder.lower(): _folder='R2D2'
		except: _folder='R2D2'
		if not _folder in _fo: _blacklist[mod.split('.')[-1]]=1
	for ww in [ mod+'.'+x+'.__doc__' for x in dir(eval(mod)) if not x.startswith('__')]:
		exec("try:doc="+ww+"\nexcept:pass")

		nm=ww[:-len('.__doc__')]
		if not _valid_(nm): continue
		_iid=-1
		_iid=eval("id("+nm+")")
		_ids.append(_iid)
		#b)--> kill on duplicate id
		# if _iid in _ids: return None
		# else: _ids.append(_iid)
		#e)--> kill on duplicate id

		_dump.append(nm)
		# print(_START_OVER,nm)
		children.append(nm)
		doc=eval(ww)
		# exec("try:doc="+ww+"\nexcept:pass")
		if doc:
			_all_docs[ww]=doc
			# print(_START_OVER,nm)
	for child in children:
		if _valid_(child): _doc_(child)


# exec('import '+sys.argv[-1])
try:eval(sys.argv[-1])
except Exception as e:
	import importlib
	globals()[sys.argv[-1]]=importlib.import_module(sys.argv[-1])
# print( eval(sys.argv[-1]+'.__doc__') )

_omit[sys.argv[-1]+'.os']=1
_omit[sys.argv[-1]+'.sys']=1
_doc_(sys.argv[-1])
# print('_all_docs',_all_docs)
# print('_dump',_dump)
_clean={}
_IDs=[]



for dt in 'str int float complex list tuple range dict set frozenset bool bytes bytearray memoryview None'.split(' '):
	for yy in dir(eval(dt)):
		_IDs.append(id(eval(dt+'.'+yy)))

for mpath in _all_docs:
	nm=mpath[:-len('.__doc__')]
	mi=id(eval(nm))
	try:
		if eval(sys.argv[-1]+'.__doc__'):
			_clean[sys.argv[-1]+'.__doc__']=eval(sys.argv[-1]+'.__doc__')
	except Exception as e: pass
	if not mi in _IDs:
		_IDs.append(mi)
		_clean[mpath]=_all_docs[mpath]

if '-ask' in sys.argv or '-a' in sys.argv:

			# for xx in _all_docs:
			#     print(xx)
			# print(len(_all_docs.keys()))

	ask=''
	while True:
		os.system('cls')
		for mpath in _clean:
			print(mpath[:-len('.__doc__')])
		print(len(_clean))
		ask=ask.replace(' ','')
		if not len(ask):
			ask=input(' : ')
		ask=ask.replace(' ','')
		if not len(ask): ask=''; break;
		if not ask.startswith(sys.argv[-1]):
			gold=''
			found=[]
			dirty=[]

			for mpath in _clean:
				if mpath.endswith('.'+ask+'.__doc__'):
					gold=mpath
					# print(mpath[:-len('.__doc__')])

				if '.'+ask+'.' in mpath:
					found.append(mpath)
				if ask.lower() in mpath.lower():
					dirty.append(mpath)


					# print(mpath[:-len('.__doc__')])
			if not found:
				print('\nnot found')
				sys.exit()
			for mpath in found:
				print(mpath[:-len('.__doc__')])

			print()
			print(len(found))
			print()
			print()
			if gold:
				print()
				print(gold[:-len('.__doc__')])
				print()
				print(eval(gold))
				
			ask=input(' : ')
			ask=''
			continue
		if not '.__doc__' in ask: print(eval(ask+'.__doc__'))
		else: print(eval(ask))
		print()
		ask=input(' : ')
	sys.exit()


md=[]
md.append('# '+sys.argv[-1]+' documentation')
md.append('#### found '+str(len(_clean.keys()))+' __doc__ ' )
for mpath in _clean:
	md.append('')
	md.append('___')
	md.append('## '+mpath[:-len('.__doc__')])
	md.append('')
	# md.append('~~~')
	for docl in _clean[mpath].split('\n'): md.append('    '+docl)
	# md.append('~~~')
	md.append('')
bottom='list'

md.append('___')
md.append('## items with __doc__')
md.append('')
if bottom=='check':
	for mpath in _clean: md.append('- [ ] '+mpath[:-len('.__doc__')])
if bottom=='list':
	for mpath in _clean: md.append('    '+mpath[:-len('.__doc__')])
md.append('')
md.append('___')
md.append('#### found '+str(len(_clean.keys()))+' __doc__ ' )
md.append('')

for line in md: print(line)
# print(sys.argv)
# print('-ask' in sys.argv)
# if 1:
