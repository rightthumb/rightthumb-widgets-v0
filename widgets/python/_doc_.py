#!/usr/bin/python3

import sys
import os
import importlib
import inspect
import pkgutil
from types import ModuleType
from typing import Any, Dict, List, Optional, Set


def is_private(name: str, include_private: bool = False) -> bool:
    if include_private:
        return False
    return name.startswith("_")


def safe_getdoc(obj: Any) -> str:
    try:
        return inspect.getdoc(obj) or ""
    except Exception:
        return ""


def safe_signature(obj: Any) -> str:
    try:
        return str(inspect.signature(obj))
    except Exception:
        return ""


def safe_getmembers(obj: Any):
    try:
        return inspect.getmembers(obj)
    except Exception:
        return []


def safe_is_package(mod: ModuleType) -> bool:
    return hasattr(mod, "__path__")


def safe_file(obj: Any) -> str:
    try:
        return inspect.getfile(obj)
    except Exception:
        try:
            return getattr(obj, "__file__", "") or ""
        except Exception:
            return ""


def object_kind(obj: Any) -> str:
    try:
        if inspect.ismodule(obj):
            return "module"
        if inspect.isclass(obj):
            return "class"
        if inspect.ismethod(obj):
            return "method"
        if inspect.isfunction(obj):
            return "function"
        if inspect.isbuiltin(obj):
            return "builtin"
        if isinstance(obj, property):
            return "property"
        return type(obj).__name__
    except Exception:
        return "unknown"


def should_recurse_into(
    obj: Any,
    root_name: str,
    current_depth: int,
    max_depth: int,
    include_submodules: bool,
) -> bool:
    if current_depth >= max_depth:
        return False

    try:
        if inspect.ismodule(obj):
            mod_name = getattr(obj, "__name__", "")
            if include_submodules and mod_name.startswith(root_name):
                return True
            return False

        if inspect.isclass(obj):
            return True

        return False
    except Exception:
        return False


def member_belongs_to_root(obj: Any, root_name: str) -> bool:
    """
    Avoid diving deep into foreign imported objects unless they belong
    to the target module/package namespace.
    """
    try:
        mod = getattr(obj, "__module__", "") or ""
        name = getattr(obj, "__name__", "") or ""
        full = f"{mod}.{name}".strip(".")
        return mod.startswith(root_name) or full.startswith(root_name)
    except Exception:
        return False


def expand_package_submodules(module: ModuleType, root_name: str) -> List[ModuleType]:
    found = []
    if not safe_is_package(module):
        return found

    try:
        for modinfo in pkgutil.iter_modules(module.__path__, module.__name__ + "."):
            try:
                submod = importlib.import_module(modinfo.name)
                if getattr(submod, "__name__", "").startswith(root_name):
                    found.append(submod)
            except Exception:
                continue
    except Exception:
        pass

    return found


def scan_object(
    obj: Any,
    display_name: str,
    root_name: str,
    max_depth: int = 4,
    current_depth: int = 0,
    include_private: bool = False,
    include_submodules: bool = False,
    seen: Optional[Set[int]] = None,
    out: Optional[Dict[str, Dict[str, Any]]] = None,
) -> Dict[str, Dict[str, Any]]:
    if seen is None:
        seen = set()
    if out is None:
        out = {}

    oid = id(obj)
    if oid in seen:
        return out
    seen.add(oid)

    kind = object_kind(obj)
    doc = safe_getdoc(obj)
    sig = safe_signature(obj)
    file_path = safe_file(obj)

    out[display_name] = {
        "kind": kind,
        "signature": sig,
        "doc": doc,
        "file": file_path,
        "depth": current_depth,
    }

    if current_depth >= max_depth:
        return out

    # Special handling for package submodules
    if inspect.ismodule(obj) and include_submodules:
        for submod in expand_package_submodules(obj, root_name):
            subname = getattr(submod, "__name__", "")
            if subname and subname not in out:
                scan_object(
                    submod,
                    subname,
                    root_name=root_name,
                    max_depth=max_depth,
                    current_depth=current_depth + 1,
                    include_private=include_private,
                    include_submodules=include_submodules,
                    seen=seen,
                    out=out,
                )

    # Inspect members
    for name, value in safe_getmembers(obj):
        if is_private(name, include_private=include_private):
            continue

        member_name = f"{display_name}.{name}"

        try:
            if inspect.ismodule(value):
                if not include_submodules:
                    continue
                if not getattr(value, "__name__", "").startswith(root_name):
                    continue

            elif inspect.isclass(value) or inspect.isfunction(value) or inspect.ismethod(value) or inspect.isbuiltin(value):
                if not member_belongs_to_root(value, root_name):
                    continue
            else:
                # Skip plain data unless it has a doc and is interesting
                if not safe_getdoc(value):
                    continue

            if member_name not in out:
                scan_object(
                    value,
                    member_name,
                    root_name=root_name,
                    max_depth=max_depth,
                    current_depth=current_depth + 1,
                    include_private=include_private,
                    include_submodules=include_submodules,
                    seen=seen,
                    out=out,
                )
        except Exception:
            continue

    return out


def render_markdown(module_name: str, docs: Dict[str, Dict[str, Any]]) -> List[str]:
    lines: List[str] = []

    items = sorted(docs.items(), key=lambda x: (x[1]["depth"], x[0]))

    lines.append(f"# {module_name} documentation")
    lines.append("")
    lines.append(f"Found **{len(items)}** documented/inspectable items.")
    lines.append("")

    # TOC
    lines.append("## Items")
    lines.append("")
    for name, meta in items:
        lines.append(f"- `{name}` — {meta['kind']}")
    lines.append("")

    # Details
    for name, meta in items:
        lines.append("---")
        lines.append("")
        lines.append(f"## `{name}`")
        lines.append("")

        lines.append(f"- **Kind:** {meta['kind']}")
        if meta["signature"]:
            lines.append(f"- **Signature:** `{meta['signature']}`")
        if meta["file"]:
            lines.append(f"- **File:** `{meta['file']}`")
        lines.append(f"- **Depth:** {meta['depth']}")
        lines.append("")

        if meta["doc"]:
            lines.append("### Doc")
            lines.append("")
            for line in meta["doc"].splitlines():
                lines.append(f"    {line}")
            lines.append("")
        else:
            lines.append("### Doc")
            lines.append("")
            lines.append("    No docstring.")
            lines.append("")

    return lines


def interactive_lookup(docs: Dict[str, Dict[str, Any]], root_name: str):
    names = sorted(docs.keys())

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Items in {root_name}")
        print("-" * 80)
        for name in names:
            print(name)
        print("-" * 80)
        print(f"Count: {len(names)}")
        print("Enter a full name or partial text. Blank = quit.")
        ask = input(" : ").strip()
        if not ask:
            break

        exact = docs.get(ask)
        if exact:
            print()
            print(ask)
            print("-" * len(ask))
            if exact["signature"]:
                print("signature:", exact["signature"])
            print("kind:", exact["kind"])
            if exact["file"]:
                print("file:", exact["file"])
            print()
            print(exact["doc"] or "No docstring.")
            input("\nenter to continue...")
            continue

        found = [n for n in names if ask.lower() in n.lower()]
        if not found:
            print("\nnot found")
            input("\nenter to continue...")
            continue

        print()
        for name in found:
            print(name)
        print()
        if len(found) == 1:
            meta = docs[found[0]]
            print("-" * 80)
            if meta["signature"]:
                print("signature:", meta["signature"])
            print("kind:", meta["kind"])
            if meta["file"]:
                print("file:", meta["file"])
            print()
            print(meta["doc"] or "No docstring.")
        input("\nenter to continue...")


def parse_args(argv: List[str]) -> Dict[str, Any]:
    args = {
        "module": None,
        "max_depth": 4,
        "include_private": False,
        "include_submodules": False,
        "interactive": False,
        "output": None,
    }

    i = 0
    positional = []
    while i < len(argv):
        arg = argv[i]

        if arg in ("-a", "-ask"):
            args["interactive"] = True
        elif arg in ("-p", "-private"):
            args["include_private"] = True
        elif arg in ("-s", "-submodules"):
            args["include_submodules"] = True
        elif arg in ("-d", "-depth") and i + 1 < len(argv):
            i += 1
            try:
                args["max_depth"] = int(argv[i])
            except Exception:
                pass
        elif arg in ("-o", "-out") and i + 1 < len(argv):
            i += 1
            args["output"] = argv[i]
        else:
            positional.append(arg)

        i += 1

    if positional:
        args["module"] = positional[-1]

    return args


def main():
    args = parse_args(sys.argv[1:])
    module_name = args["module"]

    if not module_name:
        print("usage:")
        print("    script.py [-a] [-p] [-s] [-d 4] [-o output.md] module_name")
        sys.exit(1)

    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        print(f"failed to import '{module_name}': {e}")
        sys.exit(1)

    docs = scan_object(
        module,
        display_name=module_name,
        root_name=module_name,
        max_depth=args["max_depth"],
        current_depth=0,
        include_private=args["include_private"],
        include_submodules=args["include_submodules"],
    )

    if args["interactive"]:
        interactive_lookup(docs, module_name)
        return

    md = render_markdown(module_name, docs)
    output = args["output"]

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write("\n".join(md))
        print(output)
    else:
        print("\n".join(md))


if __name__ == "__main__":
    main()



































# #!/usr/bin/python3








# def recursive_dir(obj, max_depth=3, include_private=False, _seen=None):
#     """
#     Recursively inspect attributes of an object (e.g. a module) without
#     listing the "standard" attributes inherited from its type (like all
#     the usual string methods, function attributes, etc.).

#     Returns a nested dict:
#         { attr_name: subtree_or_type_string }
#     """
#     if _seen is None:
#         _seen = set()

#     oid = id(obj)
#     if oid in _seen or max_depth < 0:
#         return "...(seen or max_depth reached)..."

#     _seen.add(oid)

#     # Safely get attribute names
#     try:
#         names = dir(obj)
#     except Exception:
#         return {}

#     # Attributes that come from the *type* of this object
#     try:
#         base_names = set(dir(type(obj)))
#     except Exception:
#         base_names = set()

#     result = {}

#     for name in names:
#         # Optionally skip private / dunder-like attributes
#         if not include_private and name.startswith("_"):
#             continue

#         # Skip attributes that are already provided by the type;
#         # these are the "redundant var type properties" (e.g. str methods)
#         if name in base_names:
#             continue

#         try:
#             value = getattr(obj, name)
#         except Exception:
#             # Some attributes may raise on access, just skip them
#             continue

#         # Decide whether to recurse or stop here
#         leaf_types = (
#             int, float, complex, bool, str, bytes, bytearray, memoryview,
#             tuple, list, dict, set, frozenset, type(None)
#         )

#         if max_depth > 0 and not isinstance(value, leaf_types):
#             # Recurse into non-trivial objects
#             result[name] = recursive_dir(value, max_depth=max_depth - 1,
#                                          include_private=include_private,
#                                          _seen=_seen)
#         else:
#             # Just record the type, no redundant dir() on basic values
#             result[name] = f"<{type(value).__name__}>"

#     return result


# run = False
# run = True

# if run:
# 	import pytermgui

# 	tree = recursive_dir(pytermgui, max_depth=2)
# 	for k, v in list(tree.items())[:10]:
# 		print(k, "->", v)




# 	import sys
# 	sys.exit()


















# import os,sys
# # print(sys.argv)
# # print(sys.argv[-1])
# # sys.exit()
# _START_OVER=0
# _cols_thresh=20
# _cols={}
# _all_docs={}
# _dump=[]
# _omit={}


# _col1=[]
# _col1i={}
# _col1_i={}
# _blacklist={}
# _ids=[]
# _folder='C3P0'
# mod0=None

# def _valid_(mod):
# 	global _omit
# 	global _dump
# 	global _col1
# 	global _cols_thresh
# 	global _col1_i
# 	global _blacklist
# 	global _ids
# 	if not '.' in mod: return  True
# 	if '.' in mod and mod.split('.')[1] in _col1:
# 		return False
# 	_m3=mod.split('.')
# 	_m4=set(_m3)
# 	_d=len(_m3)-len(_m4)
# 	if _d > 2:
# 		for i,foo in enumerate(_m3):
# 			if i:
# 				if not i in _cols: _cols[i]={}
# 				if not foo in _cols[i]: _cols[i][foo]=0
# 				_cols[i][foo]+=1
# 				if _cols[i][foo] > _cols_thresh:
# 					_blacklist[foo]=1
# 					_omit['.'.join([_m3[0],_m3[1]])]=1
# 					return False
# 		_o=[]
# 		for _m in _m3:
# 			if mod.count(_m) > 2: _o.append(_m)
# 		bad=[]
# 		ii=None
# 		for i,_po in enumerate(_m3):
# 			ii=i
# 			if not _po in _o: bad.append(_po); break;
# 		if len(_m3) >=ii+1: exec("try:bad.append(_m3[ii+1])\nexcept:pass")

		
# 		bad_='.'.join(bad)
# 		if not bad_ in _omit: _omit[bad_]=1
# 		_ddocs={}
# 		global _all_docs
# 		for k in _all_docs:
# 			if not k == bad_ and not k.startswith(bad_+'.'): _ddocs[k]=_all_docs[k]
# 			# else: print('-cl-',k)
# 		_all_docs=_ddocs
# 	if not _omit: return True
# 	for k in _omit:
# 		if k == mod and k.startswith(mod+'.'): return False
# 	return True




# def _audit(mod):
# 	global _omit
# 	global _dump
# 	global _cols
# 	global _START_OVER
# 	global _col1
# 	global _col1i
# 	global mod0
# 	global _cols_thresh
# 	if len(_dump) > 4000:
# 		_m3=mod.split('.')
# 		if _START_OVER > 2:
# 			# for x in _dump: print(x)
# 			# print('----------------------------')
# 			# os.system('cls')
# 			for xx in _all_docs:
# 				print(xx)
# 			print(len(_all_docs.keys()))
# 			sys.exit()
# 			#################################################################
# 		_START_OVER+=1
# 		print('_START_OVER:',_START_OVER)
# 		one=1
# 		if not  1 in _cols and '1' in _cols: one='1'
# 		if one in _cols:
# 			for ol in _cols[one]:
# 				if _cols[one][ol] > _cols_thresh:
# 					_omit['.'.join([_m3[0],_m3[1]])]=1
# 					if not ol in _col1: _col1.append(ol)
# 		_cols={}
# 		# _all_docs={}
# 		_dump=[]
# 		mod=mod0
# 		mod0=None
# 	return mod





# def _doc_(mod):
# 	mod=_audit(mod)
# 	global _all_docs
# 	global _omit
# 	global _dump
# 	global _cols
# 	global mod0
# 	global _START_OVER
# 	global _folder
# 	global _ids
# 	global _blacklist
# 	if mod.startswith(tuple(list(_omit.keys()))): return None
# 	if '.os.' in mod:  return None
# 	if '.sys.' in mod:  return None
# 	_m3=mod.split('.')
# 	if '.'+_m3[0] in mod: return None
# 	for mo in _m3:
# 		if mo in _blacklist: return  None
# 	if mod0 is None: mod0=mod
# 	children=[]

# 	if not '.' in mod:
# 		try:
# 			exec('_folder='+mod+'.__file__'.split(os.sep)[-1])
# 			if 'python' in _folder.lower(): _folder='C3P0'
# 		except: _folder='C3P0'
# 	elif '.' in mod and not _folder == 'C3P0':
# 		_fo='R2D2'
# 		try:
# 			exec('_folder='+mod+'.__file__'.split(os.sep)[-1])
# 			if 'python' in _folder.lower(): _folder='R2D2'
# 		except: _folder='R2D2'
# 		if not _folder in _fo: _blacklist[mod.split('.')[-1]]=1
# 	for ww in [ mod+'.'+x+'.__doc__' for x in dir(eval(mod)) if not x.startswith('__')]:
# 		exec("try:doc="+ww+"\nexcept:pass")

# 		nm=ww[:-len('.__doc__')]
# 		if not _valid_(nm): continue
# 		_iid=-1
# 		_iid=eval("id("+nm+")")
# 		_ids.append(_iid)
# 		#b)--> kill on duplicate id
# 		# if _iid in _ids: return None
# 		# else: _ids.append(_iid)
# 		#e)--> kill on duplicate id

# 		_dump.append(nm)
# 		# print(_START_OVER,nm)
# 		children.append(nm)
# 		doc=eval(ww)
# 		# exec("try:doc="+ww+"\nexcept:pass")
# 		if doc:
# 			_all_docs[ww]=doc
# 			# print(_START_OVER,nm)
# 	for child in children:
# 		if _valid_(child): _doc_(child)


# # exec('import '+sys.argv[-1])
# try:eval(sys.argv[-1])
# except Exception as e:
# 	import importlib
# 	globals()[sys.argv[-1]]=importlib.import_module(sys.argv[-1])
# # print( eval(sys.argv[-1]+'.__doc__') )

# _omit[sys.argv[-1]+'.os']=1
# _omit[sys.argv[-1]+'.sys']=1
# _doc_(sys.argv[-1])
# # print('_all_docs',_all_docs)
# # print('_dump',_dump)
# _clean={}
# _IDs=[]



# for dt in 'str int float complex list tuple range dict set frozenset bool bytes bytearray memoryview None'.split(' '):
# 	for yy in dir(eval(dt)):
# 		_IDs.append(id(eval(dt+'.'+yy)))

# for mpath in _all_docs:
# 	nm=mpath[:-len('.__doc__')]
# 	mi=id(eval(nm))
# 	try:
# 		if eval(sys.argv[-1]+'.__doc__'):
# 			_clean[sys.argv[-1]+'.__doc__']=eval(sys.argv[-1]+'.__doc__')
# 	except Exception as e: pass
# 	if not mi in _IDs:
# 		_IDs.append(mi)
# 		_clean[mpath]=_all_docs[mpath]

# if '-ask' in sys.argv or '-a' in sys.argv:

# 			# for xx in _all_docs:
# 			#     print(xx)
# 			# print(len(_all_docs.keys()))

# 	ask=''
# 	while True:
# 		os.system('cls')
# 		for mpath in _clean:
# 			print(mpath[:-len('.__doc__')])
# 		print(len(_clean))
# 		ask=ask.replace(' ','')
# 		if not len(ask):
# 			ask=input(' : ')
# 		ask=ask.replace(' ','')
# 		if not len(ask): ask=''; break;
# 		if not ask.startswith(sys.argv[-1]):
# 			gold=''
# 			found=[]
# 			dirty=[]

# 			for mpath in _clean:
# 				if mpath.endswith('.'+ask+'.__doc__'):
# 					gold=mpath
# 					# print(mpath[:-len('.__doc__')])

# 				if '.'+ask+'.' in mpath:
# 					found.append(mpath)
# 				if ask.lower() in mpath.lower():
# 					dirty.append(mpath)


# 					# print(mpath[:-len('.__doc__')])
# 			if not found:
# 				print('\nnot found')
# 				sys.exit()
# 			for mpath in found:
# 				print(mpath[:-len('.__doc__')])

# 			print()
# 			print(len(found))
# 			print()
# 			print()
# 			if gold:
# 				print()
# 				print(gold[:-len('.__doc__')])
# 				print()
# 				print(eval(gold))
				
# 			ask=input(' : ')
# 			ask=''
# 			continue
# 		if not '.__doc__' in ask: print(eval(ask+'.__doc__'))
# 		else: print(eval(ask))
# 		print()
# 		ask=input(' : ')
# 	sys.exit()


# md=[]
# md.append('# '+sys.argv[-1]+' documentation')
# md.append('#### found '+str(len(_clean.keys()))+' __doc__ ' )
# for mpath in _clean:
# 	md.append('')
# 	md.append('___')
# 	md.append('## '+mpath[:-len('.__doc__')])
# 	md.append('')
# 	# md.append('~~~')
# 	for docl in _clean[mpath].split('\n'): md.append('    '+docl)
# 	# md.append('~~~')
# 	md.append('')
# bottom='list'

# md.append('___')
# md.append('## items with __doc__')
# md.append('')
# if bottom=='check':
# 	for mpath in _clean: md.append('- [ ] '+mpath[:-len('.__doc__')])
# if bottom=='list':
# 	for mpath in _clean: md.append('    '+mpath[:-len('.__doc__')])
# md.append('')
# md.append('___')
# md.append('#### found '+str(len(_clean.keys()))+' __doc__ ' )
# md.append('')

# for line in md: print(line)
# # print(sys.argv)
# # print('-ask' in sys.argv)
# # if 1:
