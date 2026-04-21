


def pathImp(path, module_name=None, register=False):
    """
    Import a Python module from a full file path.

    Args:
        path (str): Full path to .py file
        module_name (str): Optional custom module name
        register (bool): If True, adds to sys.modules

    Returns:
        module object
    """
    import importlib.util
    import sys
    import os
    path = os.path.abspath(path)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Module path not found: {path}")

    if module_name is None:
        module_name = os.path.splitext(os.path.basename(path))[0]

    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for: {path}")

    module = importlib.util.module_from_spec(spec)

    if register:
        sys.modules[module_name] = module  # optional global registration

    spec.loader.exec_module(module)

    return module


hex = pathImp('D:\\.rightthumb-widgets\\widgets\\python\\library\\code\\functions\\hexColor_standalone.py','hexColor', True)

def pr(*args, **kwargs):
    if type(kwargs) == dict:
        if 'np' in kwargs:
            del kwargs['np']
        else:
            kwargs['p'] = True
        kwargs['sp'] = '\t'

    pretty = hex.hexColor(*args, **kwargs)
    # print(pretty)
    return pretty
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Called {self.count} times")
        return self.func(*args, **kwargs)
    def test1(self): print("Test method called")
    def test2(self): print("Test method called")

import inspect

@CountCalls
def say_hi():
    print("Hi")


data = {}
items = {}

def checkAll(ca):
    ca = ca.strip()
    ca = ca.replace('\n',' ').replace(',',' ').replace('\t',' ')
    while '  ' in ca:
        ca = ca.replace('  ',' ')
    for c in ca.split(' '):
        check(c)
checked = 0
def check(ca):
    if '__file__' in dir(eval(ca)): return
    global checked
    checked += 1

    global data
    data[ca] = {}
    # data[ca]['source'] = inspect.getsource(eval(ca))
    for d in dir(eval(ca)):
        if not d in items:
            items[d] = 0
        items[d] += 1
        
        if not d in '__globals__  __builtins__':
            data[ca][d] = str(eval(ca+'.'+d))
            # if d == '__code__.co_filename'
            if d == '__code__':
                data[ca]['**** -> path'] = str(eval(ca+'.'+d+'.co_filename'))
                data[ca]['**** -> line'] = str(eval(ca+'.'+d+'.co_firstlineno'))


def fn_info(fn):
    import inspect, dis, ast

    info = {}

    try:
        c = fn.__code__
    except Exception:
        c = None

    # --- basic ---
    info['name'] = getattr(fn, '__name__', None)
    info['qualname'] = getattr(fn, '__qualname__', None)
    info['module'] = getattr(fn, '__module__', None)
    info['doc'] = getattr(fn, '__doc__', None)

    # --- code object ---
    if c:
        info['file'] = c.co_filename
        info['line'] = c.co_firstlineno
        info['argcount'] = c.co_argcount
        info['kwonlyargcount'] = c.co_kwonlyargcount
        info['nlocals'] = c.co_nlocals
        info['varnames'] = c.co_varnames
        info['names'] = c.co_names
        info['constants'] = c.co_consts
        info['freevars'] = c.co_freevars
        info['cellvars'] = c.co_cellvars
        info['bytecode_len'] = len(c.co_code)
    else:
        info['file'] = None
        info['line'] = None

    # --- defaults ---
    info['defaults'] = getattr(fn, '__defaults__', None)
    info['kwdefaults'] = getattr(fn, '__kwdefaults__', None)
    info['annotations'] = getattr(fn, '__annotations__', None)

    # --- signature ---
    try:
        info['signature'] = str(inspect.signature(fn))
    except Exception:
        info['signature'] = None

    # --- source ---
    try:
        info['source'] = inspect.getsource(fn)
    except Exception:
        info['source'] = None

    # --- source lines ---
    try:
        lines, start = inspect.getsourcelines(fn)
        info['source_lines'] = lines
        info['source_start_line'] = start
    except Exception:
        info['source_lines'] = None
        info['source_start_line'] = None

    # --- globals used ---
    try:
        info['globals_used'] = list(c.co_names) if c else None
    except Exception:
        info['globals_used'] = None

    # --- closure values ---
    try:
        if fn.__closure__:
            info['closure'] = [cell.cell_contents for cell in fn.__closure__]
        else:
            info['closure'] = None
    except Exception:
        info['closure'] = None

    # --- AST ---
    try:
        src = info['source']
        if src:
            tree = ast.parse(src)
            info['ast'] = ast.dump(tree)
        else:
            info['ast'] = None
    except Exception:
        info['ast'] = None

    # --- disassembly ---
    try:
        info['dis'] = dis.Bytecode(fn).dis()
    except Exception:
        info['dis'] = None

    return info


def a(fn): pass

@a
def b(): pass


items = {}
def allItems(cnt):
    global items
    amount = 0
    for x in items:
        if items[x] == cnt:
            amount += 1
    if not amount:
        # print('No items with count', cnt)
        return False
    print()
    print()
    print()
    pr('------------------',c='yellow')
    pr(cnt,c='green')
    print()
    
    for x in items:
        if items[x] == cnt:
            has = []
            for y in data:
                if x in data[y]:
                    has.append(y)
            pr(' '.join(has),x,c='cyan')
            # pr(' '.join(has),x, items[x],c='cyan')

    return True



# check('say_hi')
# check('a')
# check('b')




# print(globals().keys())
def globe():
    print()
    print()
    print()
    pr('------------------',c='yellow')
    pr('Globals',c='green')
    print()
    keys = globals().keys()
    for x in keys:

        if '__file__' in dir(eval(x)):
            pr(x,'\t',eval(x+'.__file__'),c='red')
            # pr(dir(eval(x)),c='red')
        else:
            if not x.startswith('__'):
                pr(x,c='cyan')
                check(x)
            else:
                pr(x,c='yellow')
    # check(__name__)

def autoAllItems():
    global checked
    for i in range(1, checked+1):
        allItems(i)
        # if not allItems(i): break

# checkAll('say_hi a b')
CountCalls.test1 = hex.hexColor
checkAll('CountCalls.test1')
checkAll('CountCalls.test2')

import json
# for d in data:
import os; os.system('cls')

# globe()



def checkKey(key):
    global data
    for k in data:
        if key in data[k]:
            pr(k, key, data[k][key], c='cyan')


# print(json.dumps(data, indent=4))
# print(json.dumps(items, indent=4))


# checkKey('__call__')

# autoAllItems()
# pr('\n\n\n\n',c='green')
# pr('.   Checked   '+str(checked)+'   .', c='white,blue')
newData = {}
for d in data:
    newData[d] = {}
    for k in data[d]:
        
        if not data[d][k].startswith('<') and not data[d][k].startswith('[<'):
            if not k in 'modules stdlib_module_names path path_importer_cache orig_argv builtin_module_names' and not k.startswith('base_'):
                newData[d][k] = data[d][k]

# print(json.dumps(data, indent=4))


def fn_info(fn):
    import inspect
    import dis
    import ast

    info = {}

    def add(k, v):
        if v is None:
            return
        if v == '':
            return
        if v == () or v == [] or v == {}:
            return
        info[k] = v

    add('name', getattr(fn, '__name__', None))
    add('qualname', getattr(fn, '__qualname__', None))
    add('module', getattr(fn, '__module__', None))
    add('doc', getattr(fn, '__doc__', None))
    add('defaults', getattr(fn, '__defaults__', None))
    add('kwdefaults', getattr(fn, '__kwdefaults__', None))
    add('annotations', getattr(fn, '__annotations__', None))

    try:
        c = fn.__code__
    except Exception:
        c = None

    if c:
        add('file', c.co_filename)
        add('line', c.co_firstlineno)
        add('argcount', c.co_argcount)
        add('kwonlyargcount', c.co_kwonlyargcount)
        add('nlocals', c.co_nlocals)
        add('varnames', c.co_varnames)
        add('names', c.co_names)
        add('constants', c.co_consts)
        add('freevars', c.co_freevars)
        add('cellvars', c.co_cellvars)
        add('bytecode_len', len(c.co_code))

    try:
        add('signature', str(inspect.signature(fn)))
    except Exception:
        pass

    try:
        add('source', inspect.getsource(fn))
    except Exception:
        pass

    try:
        lines, start = inspect.getsourcelines(fn)
        add('source_lines', lines)
        add('source_start_line', start)
    except Exception:
        pass

    try:
        clo = getattr(fn, '__closure__', None)
        if clo:
            add('closure', [cell.cell_contents for cell in clo])
    except Exception:
        pass

    try:
        src = inspect.getsource(fn)
        add('ast', ast.dump(ast.parse(src)))
    except Exception:
        pass

    try:
        add('dis', dis.Bytecode(fn).dis())
    except Exception:
        pass

    return info


# info = fn_info(say_hi)
# print(info)
# for k in info:
#     info[k] = str(info[k])

# print( json.dumps(info, indent=4) )

# print(json.dumps(newData, indent=4))

# allItems(1)
# allItems(2)
# allItems(3)



import inspect
import sys


class ObjectInfo:
    @staticmethod
    def safe_repr(obj, max_len=200):
        try:
            r = repr(obj)
            if len(r) > max_len:
                r = r[:max_len] + '...'
            return r
        except Exception:
            return f'<unreprable {type(obj).__name__}>'

    @staticmethod
    def strip_empty(d):
        return {
            k: v for k, v in d.items()
            if v not in (None, '', (), [], {})
        }

    @staticmethod
    def detect_kind(obj):
        if isinstance(obj, (str, int, float, bool, type(None))):
            return 'scalar'
        if inspect.ismodule(obj):
            return 'module'
        if inspect.isclass(obj):
            return 'class'
        if inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isbuiltin(obj):
            return 'callable'
        if isinstance(obj, dict):
            return 'dict'
        if isinstance(obj, list):
            return 'list'
        if isinstance(obj, tuple):
            return 'tuple'
        if isinstance(obj, set):
            return 'set'
        return 'object'

    @staticmethod
    def should_recurse(recursive, depth, max_depth):
        if recursive:
            return True
        return depth < max_depth

    @staticmethod
    def get_size(obj, seen=None):
        if obj is None:
            return 0

        if seen is None:
            seen = set()

        obj_id = id(obj)
        if obj_id in seen:
            return 0
        seen.add(obj_id)

        try:
            size = sys.getsizeof(obj)
        except Exception:
            size = 0

        if isinstance(obj, dict):
            for k, v in list(obj.items()):
                size += ObjectInfo.get_size(k, seen)
                size += ObjectInfo.get_size(v, seen)

        elif hasattr(obj, '__dict__'):
            try:
                size += ObjectInfo.get_size(vars(obj), seen)
            except Exception:
                pass

        elif isinstance(obj, (list, tuple, set, frozenset)):
            for i in obj:
                size += ObjectInfo.get_size(i, seen)

        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
            try:
                for i in obj:
                    size += ObjectInfo.get_size(i, seen)
            except Exception:
                pass

        return size

    @staticmethod
    def get_file(obj):
        try:
            return inspect.getsourcefile(obj) or inspect.getfile(obj)
        except Exception:
            return None

    @staticmethod
    def get_line(obj):
        try:
            _, line = inspect.getsourcelines(obj)
            return line
        except Exception:
            return None

    @staticmethod
    def get_signature(obj):
        try:
            return str(inspect.signature(obj))
        except Exception:
            return None

    @staticmethod
    def get_source(obj):
        try:
            return inspect.getsource(obj)
        except Exception:
            return None

    @staticmethod
    def basic_info(obj, include_size=False, include_source=False):
        info = {
            'kind': ObjectInfo.detect_kind(obj),
            'type': type(obj).__name__,
            'callable': callable(obj),
            'repr': ObjectInfo.safe_repr(obj),
        }

        if include_size:
            info['size'] = ObjectInfo.get_size(obj)

        if isinstance(obj, (str, int, float, bool, type(None))):
            info['value'] = obj
            return ObjectInfo.strip_empty(info)

        if inspect.ismodule(obj):
            info['name'] = getattr(obj, '__name__', None)
            info['file'] = getattr(obj, '__file__', None)
            info['package'] = getattr(obj, '__package__', None)

        elif inspect.isclass(obj):
            info['name'] = getattr(obj, '__name__', None)
            info['qualname'] = getattr(obj, '__qualname__', None)
            info['module'] = getattr(obj, '__module__', None)
            info['file'] = ObjectInfo.get_file(obj)
            info['line'] = ObjectInfo.get_line(obj)

        elif inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isbuiltin(obj):
            info['name'] = getattr(obj, '__name__', None)
            info['qualname'] = getattr(obj, '__qualname__', None)
            info['module'] = getattr(obj, '__module__', None)
            info['signature'] = ObjectInfo.get_signature(obj)
            info['file'] = ObjectInfo.get_file(obj)
            info['line'] = ObjectInfo.get_line(obj)

        elif isinstance(obj, dict):
            info['len'] = len(obj)

        elif isinstance(obj, (list, tuple, set, frozenset)):
            info['len'] = len(obj)

        else:
            info['class'] = obj.__class__.__name__
            info['module'] = getattr(obj.__class__, '__module__', None)
            info['file'] = ObjectInfo.get_file(obj.__class__)
            info['line'] = ObjectInfo.get_line(obj.__class__)

        if include_source:
            info['source'] = ObjectInfo.get_source(obj)

        return ObjectInfo.strip_empty(info)

    @staticmethod
    def scan(obj, path='globals', results=None, seen=None, recursive=False, max_depth=2, depth=0, include_size=False, include_source=False):
        if results is None:
            results = {}
        if seen is None:
            seen = {}

        oid = id(obj)

        if oid in seen:
            results[path] = {
                'kind': 'duplicate',
                'type': type(obj).__name__,
                'repr': ObjectInfo.safe_repr(obj),
                'same_as': seen[oid],
            }
            return results

        seen[oid] = path
        results[path] = ObjectInfo.basic_info(obj, include_size=include_size, include_source=include_source)

        if not ObjectInfo.should_recurse(recursive, depth, max_depth):
            return results

        if isinstance(obj, dict):
            for k, v in list(obj.items()):
                try:
                    key = str(k)
                except Exception:
                    key = f'<key:{type(k).__name__}>'
                ObjectInfo.scan(
                    v,
                    path=f'{path}.{key}',
                    results=results,
                    seen=seen,
                    recursive=recursive,
                    max_depth=max_depth,
                    depth=depth + 1,
                    include_size=include_size,
                    include_source=include_source,
                )

        elif isinstance(obj, (list, tuple, set, frozenset)):
            for i, v in enumerate(list(obj)):
                ObjectInfo.scan(
                    v,
                    path=f'{path}[{i}]',
                    results=results,
                    seen=seen,
                    recursive=recursive,
                    max_depth=max_depth,
                    depth=depth + 1,
                    include_size=include_size,
                    include_source=include_source,
                )

        else:
            try:
                mapping = vars(obj)
                for k, v in list(mapping.items()):
                    if isinstance(k, str) and k.startswith('__') and k.endswith('__'):
                        continue
                    if k == '__builtins__':
                        continue
                    ObjectInfo.scan(
                        v,
                        path=f'{path}.{k}',
                        results=results,
                        seen=seen,
                        recursive=recursive,
                        max_depth=max_depth,
                        depth=depth + 1,
                        include_size=include_size,
                        include_source=include_source,
                    )
            except Exception:
                pass

        return results

    @staticmethod
    def scan_globals(globals_dict, recursive=False, max_depth=2, include_size=False, include_source=False):
        return ObjectInfo.scan(
            globals_dict,
            path='globals',
            recursive=recursive,
            max_depth=max_depth,
            include_size=include_size,
            include_source=include_source,
        )

    @staticmethod
    def summary(results):
        out = {
            'total': len(results),
            'kinds': {},
            'types': {},
            'duplicates': 0,
        }

        for _, info in results.items():
            kind = info.get('kind', 'unknown')
            typ = info.get('type', 'unknown')

            out['kinds'][kind] = out['kinds'].get(kind, 0) + 1
            out['types'][typ] = out['types'].get(typ, 0) + 1

            if kind == 'duplicate':
                out['duplicates'] += 1

        return out
    
# results = ObjectInfo.scan_globals(globals(), recursive=False, max_depth=2)
# results = ObjectInfo.scan_globals(globals(), recursive=False, max_depth=2, include_size=True)
# info = ObjectInfo.basic_info(os, include_size=True)

# results = ObjectInfo.scan_globals(globals(), recursive=True, include_size=True)

# print(  json.dumps(results, indent=4)   )

# summary = ObjectInfo.summary(results)
# print(  json.dumps(summary, indent=4)   )



import inspect


class ObjectInfo:
    @staticmethod
    def safe_repr(obj, max_len=200):
        try:
            r = repr(obj)
            if len(r) > max_len:
                r = r[:max_len] + '...'
            return r
        except Exception:
            return f'<unreprable {type(obj).__name__}>'

    @staticmethod
    def get_file(obj):
        try:
            return inspect.getsourcefile(obj) or inspect.getfile(obj)
        except Exception:
            return None

    @staticmethod
    def get_line(obj):
        try:
            _, line = inspect.getsourcelines(obj)
            return line
        except Exception:
            return None

    @staticmethod
    def get_end_line(obj):
        try:
            lines, line = inspect.getsourcelines(obj)
            return line + len(lines) - 1
        except Exception:
            return None

    @staticmethod
    def get_signature(obj):
        try:
            return str(inspect.signature(obj))
        except Exception:
            return None

    @staticmethod
    def get_source(obj):
        try:
            return inspect.getsource(obj)
        except Exception:
            return None

    @staticmethod
    def is_function_like(obj):
        return (
            inspect.isfunction(obj)
            or inspect.ismethod(obj)
            or inspect.isbuiltin(obj)
        )

    @staticmethod
    def function_info(obj, path=None, include_source=False):
        info = {
            'path': path,
            'kind': 'function',
            'type': type(obj).__name__,
            'name': getattr(obj, '__name__', None),
            'qualname': getattr(obj, '__qualname__', None),
            'module': getattr(obj, '__module__', None),
            'signature': ObjectInfo.get_signature(obj),
            'file': ObjectInfo.get_file(obj),
            'line_start': ObjectInfo.get_line(obj),
            'line_end': ObjectInfo.get_end_line(obj),
            'callable': callable(obj),
            'repr': ObjectInfo.safe_repr(obj),
        }
        if include_source:
            info['source'] = ObjectInfo.get_source(obj)
        return {k: v for k, v in info.items() if v not in (None, '', (), [], {})}

    @staticmethod
    def class_info(obj, path=None, include_source=False, include_methods=True):
        info = {
            'path': path,
            'kind': 'class',
            'type': type(obj).__name__,
            'name': getattr(obj, '__name__', None),
            'qualname': getattr(obj, '__qualname__', None),
            'module': getattr(obj, '__module__', None),
            'file': ObjectInfo.get_file(obj),
            'line_start': ObjectInfo.get_line(obj),
            'line_end': ObjectInfo.get_end_line(obj),
            'repr': ObjectInfo.safe_repr(obj),
        }

        if include_source:
            info['source'] = ObjectInfo.get_source(obj)

        if include_methods:
            methods = {}
            try:
                for name, value in inspect.getmembers(obj):
                    if name.startswith('__') and name.endswith('__'):
                        continue
                    if ObjectInfo.is_function_like(value):
                        methods[name] = ObjectInfo.function_info(
                            value,
                            path=f'{path}.{name}' if path else name,
                            include_source=False,
                        )
            except Exception:
                pass
            if methods:
                info['methods'] = methods

        return {k: v for k, v in info.items() if v not in (None, '', (), [], {})}

    @staticmethod
    def audit_loaded(namespace, include_source=False):
        results = {
            'functions': {},
            'classes': {},
        }
        seen = set()

        for path, obj in namespace.items():
            oid = id(obj)
            if oid in seen:
                continue
            seen.add(oid)

            if ObjectInfo.is_function_like(obj):
                results['functions'][path] = ObjectInfo.function_info(
                    obj,
                    path=path,
                    include_source=include_source,
                )
            elif inspect.isclass(obj):
                results['classes'][path] = ObjectInfo.class_info(
                    obj,
                    path=path,
                    include_source=include_source,
                    include_methods=True,
                )

        return results
    
# audit = ObjectInfo.audit_loaded(globals(), include_source=False, recursive=True)

# for path, info in audit['functions'].items():
#     print(path, info.get('file'), info.get('line_start'), info.get('line_end'))


import inspect


class ObjectInfo:
    @staticmethod
    def safe_repr(obj, max_len=200):
        try:
            r = repr(obj)
            if len(r) > max_len:
                r = r[:max_len] + '...'
            return r
        except Exception:
            return f'<unreprable {type(obj).__name__}>'

    @staticmethod
    def strip_empty(d):
        return {
            k: v for k, v in d.items()
            if v not in (None, '', (), [], {})
        }

    @staticmethod
    def get_file(obj):
        try:
            return inspect.getsourcefile(obj) or inspect.getfile(obj)
        except Exception:
            return None

    @staticmethod
    def get_line(obj):
        try:
            _, line = inspect.getsourcelines(obj)
            return line
        except Exception:
            return None

    @staticmethod
    def get_end_line(obj):
        try:
            lines, line = inspect.getsourcelines(obj)
            return line + len(lines) - 1
        except Exception:
            return None

    @staticmethod
    def get_signature(obj):
        try:
            return str(inspect.signature(obj))
        except Exception:
            return None

    @staticmethod
    def get_source(obj):
        try:
            return inspect.getsource(obj)
        except Exception:
            return None

    @staticmethod
    def get_module_name(obj):
        return getattr(obj, '__module__', None)

    @staticmethod
    def get_name(obj):
        return getattr(obj, '__name__', None)

    @staticmethod
    def get_qualname(obj):
        return getattr(obj, '__qualname__', None)

    @staticmethod
    def get_code_names(obj):
        try:
            return list(obj.__code__.co_names)
        except Exception:
            return None

    @staticmethod
    def is_function_like(obj):
        return (
            inspect.isfunction(obj)
            or inspect.ismethod(obj)
            or inspect.isbuiltin(obj)
            or inspect.ismethoddescriptor(obj)
        )

    @staticmethod
    def is_expandable(obj):
        return (
            inspect.ismodule(obj)
            or inspect.isclass(obj)
            or isinstance(obj, dict)
            or isinstance(obj, (list, tuple, set, frozenset))
            or hasattr(obj, '__dict__')
        )

    @staticmethod
    def file_matches(parent_file, child_file):
        if not parent_file or not child_file:
            return None
        return parent_file == child_file

    @staticmethod
    def mismatch_flags(parent_path=None, parent_file=None, obj=None):
        child_file = ObjectInfo.get_file(obj)
        same = ObjectInfo.file_matches(parent_file, child_file)

        flags = {
            'parent_path': parent_path,
            'parent_file': parent_file,
            'file': child_file,
            'file_matches_parent': same,
            'file_mismatch_flag': False,
        }

        if same is False:
            flags['file_mismatch_flag'] = True

        return ObjectInfo.strip_empty(flags)

    @staticmethod
    def function_info(obj, path=None, parent_path=None, parent_file=None, include_source=False):
        info = {
            'path': path,
            'kind': 'function',
            'type': type(obj).__name__,
            'name': ObjectInfo.get_name(obj),
            'qualname': ObjectInfo.get_qualname(obj),
            'module': ObjectInfo.get_module_name(obj),
            'signature': ObjectInfo.get_signature(obj),
            'file': ObjectInfo.get_file(obj),
            'line_start': ObjectInfo.get_line(obj),
            'line_end': ObjectInfo.get_end_line(obj),
            'callable': callable(obj),
            'repr': ObjectInfo.safe_repr(obj),
            'code_names': ObjectInfo.get_code_names(obj),
            'parent_path': parent_path,
            'parent_file': parent_file,
            'file_matches_parent': ObjectInfo.file_matches(parent_file, ObjectInfo.get_file(obj)),
        }

        if info['file_matches_parent'] is False:
            info['file_mismatch_flag'] = True

        if include_source:
            info['source'] = ObjectInfo.get_source(obj)

        return ObjectInfo.strip_empty(info)

    @staticmethod
    def class_info(obj, path=None, parent_path=None, parent_file=None, include_source=False):
        info = {
            'path': path,
            'kind': 'class',
            'type': type(obj).__name__,
            'name': ObjectInfo.get_name(obj),
            'qualname': ObjectInfo.get_qualname(obj),
            'module': ObjectInfo.get_module_name(obj),
            'file': ObjectInfo.get_file(obj),
            'line_start': ObjectInfo.get_line(obj),
            'line_end': ObjectInfo.get_end_line(obj),
            'repr': ObjectInfo.safe_repr(obj),
            'parent_path': parent_path,
            'parent_file': parent_file,
            'file_matches_parent': ObjectInfo.file_matches(parent_file, ObjectInfo.get_file(obj)),
        }

        if info['file_matches_parent'] is False:
            info['file_mismatch_flag'] = True

        if include_source:
            info['source'] = ObjectInfo.get_source(obj)

        return ObjectInfo.strip_empty(info)

    @staticmethod
    def module_info(obj, path=None, parent_path=None, parent_file=None):
        info = {
            'path': path,
            'kind': 'module',
            'type': type(obj).__name__,
            'name': getattr(obj, '__name__', None),
            'file': getattr(obj, '__file__', None),
            'package': getattr(obj, '__package__', None),
            'repr': ObjectInfo.safe_repr(obj),
            'parent_path': parent_path,
            'parent_file': parent_file,
            'file_matches_parent': ObjectInfo.file_matches(parent_file, getattr(obj, '__file__', None)),
        }

        if info['file_matches_parent'] is False:
            info['file_mismatch_flag'] = True

        return ObjectInfo.strip_empty(info)

    @staticmethod
    def object_info(obj, path=None, parent_path=None, parent_file=None):
        cls = getattr(obj, '__class__', None)
        cls_file = ObjectInfo.get_file(cls) if cls else None

        info = {
            'path': path,
            'kind': 'object',
            'type': type(obj).__name__,
            'class': getattr(cls, '__name__', None),
            'module': getattr(cls, '__module__', None) if cls else None,
            'file': cls_file,
            'line_start': ObjectInfo.get_line(cls) if cls else None,
            'line_end': ObjectInfo.get_end_line(cls) if cls else None,
            'repr': ObjectInfo.safe_repr(obj),
            'parent_path': parent_path,
            'parent_file': parent_file,
            'file_matches_parent': ObjectInfo.file_matches(parent_file, cls_file),
        }

        if info['file_matches_parent'] is False:
            info['file_mismatch_flag'] = True

        return ObjectInfo.strip_empty(info)

    @staticmethod
    def basic_info(obj, path=None, parent_path=None, parent_file=None, include_source=False):
        if ObjectInfo.is_function_like(obj):
            return ObjectInfo.function_info(
                obj,
                path=path,
                parent_path=parent_path,
                parent_file=parent_file,
                include_source=include_source
            )

        if inspect.isclass(obj):
            return ObjectInfo.class_info(
                obj,
                path=path,
                parent_path=parent_path,
                parent_file=parent_file,
                include_source=include_source
            )

        if inspect.ismodule(obj):
            return ObjectInfo.module_info(
                obj,
                path=path,
                parent_path=parent_path,
                parent_file=parent_file
            )

        if isinstance(obj, dict):
            return ObjectInfo.strip_empty({
                'path': path,
                'kind': 'dict',
                'type': type(obj).__name__,
                'len': len(obj),
                'repr': ObjectInfo.safe_repr(obj),
                'parent_path': parent_path,
                'parent_file': parent_file,
            })

        if isinstance(obj, (list, tuple, set, frozenset)):
            return ObjectInfo.strip_empty({
                'path': path,
                'kind': type(obj).__name__,
                'type': type(obj).__name__,
                'len': len(obj),
                'repr': ObjectInfo.safe_repr(obj),
                'parent_path': parent_path,
                'parent_file': parent_file,
            })

        if isinstance(obj, (str, int, float, bool, type(None))):
            return ObjectInfo.strip_empty({
                'path': path,
                'kind': 'scalar',
                'type': type(obj).__name__,
                'value': obj,
                'repr': ObjectInfo.safe_repr(obj),
                'parent_path': parent_path,
                'parent_file': parent_file,
            })

        return ObjectInfo.object_info(
            obj,
            path=path,
            parent_path=parent_path,
            parent_file=parent_file
        )

    @staticmethod
    def iter_children(obj):
        if isinstance(obj, dict):
            for k, v in list(obj.items()):
                yield str(k), v
            return

        if isinstance(obj, (list, tuple, set, frozenset)):
            for i, v in enumerate(list(obj)):
                yield f'[{i}]', v
            return

        try:
            for k, v in list(vars(obj).items()):
                if isinstance(k, str) and k.startswith('__') and k.endswith('__'):
                    continue
                if k == '__builtins__':
                    continue
                yield str(k), v
        except Exception:
            return

    @staticmethod
    def audit_loaded(namespace, include_source=False, recursive=False, max_depth=2):
        results = {}
        seen = {}

        def walk(obj, path, depth=0, parent_path=None, parent_file=None):
            oid = id(obj)

            if oid in seen:
                results[path] = {
                    'path': path,
                    'kind': 'duplicate',
                    'type': type(obj).__name__,
                    'repr': ObjectInfo.safe_repr(obj),
                    'same_as': seen[oid],
                    'parent_path': parent_path,
                    'parent_file': parent_file,
                }
                return

            seen[oid] = path

            info = ObjectInfo.basic_info(
                obj,
                path=path,
                parent_path=parent_path,
                parent_file=parent_file,
                include_source=include_source
            )
            results[path] = info

            if not recursive and depth >= max_depth:
                return

            if not recursive and depth < max_depth:
                pass
            elif recursive:
                pass

            if not ObjectInfo.is_expandable(obj):
                return

            current_file = info.get('file')

            for child_name, child in ObjectInfo.iter_children(obj):
                if child_name.startswith('['):
                    child_path = f'{path}{child_name}'
                else:
                    child_path = f'{path}.{child_name}'

                walk(
                    child,
                    child_path,
                    depth=depth + 1,
                    parent_path=path,
                    parent_file=current_file
                )

        walk(namespace, 'globals', 0, None, None)
        return results

    @staticmethod
    def flagged(results):
        return {
            path: info
            for path, info in results.items()
            if info.get('file_mismatch_flag')
        }

    @staticmethod
    def only_callables(results):
        return {
            path: info
            for path, info in results.items()
            if info.get('kind') in ('function', 'class')
        }

    @staticmethod
    def audit_report(results):
        rows = []
        for path, info in results.items():
            if info.get('kind') in ('function', 'class'):
                rows.append({
                    'path': path,
                    'kind': info.get('kind'),
                    'name': info.get('name'),
                    'qualname': info.get('qualname'),
                    'file': info.get('file'),
                    'line_start': info.get('line_start'),
                    'line_end': info.get('line_end'),
                    'parent_path': info.get('parent_path'),
                    'parent_file': info.get('parent_file'),
                    'file_matches_parent': info.get('file_matches_parent'),
                    'file_mismatch_flag': info.get('file_mismatch_flag', False),
                    'signature': info.get('signature'),
                })
        return rows
    
# audit = ObjectInfo.audit_loaded(
#     globals(),
#     include_source=True,
#     recursive=True
# )

# flagged = ObjectInfo.flagged(audit)
# import sys
# for path, info in flagged.items():
#     print(info.keys())
#     sys.exit()

#     print(path)
#     print('   file       :', info.get('file'))
#     print('   parent_file:', info.get('parent_file'))
#     print('   line       :', info.get('line_start'))
#     print()



import inspect
import sys


class ObjectInfo:
    @staticmethod
    def safe_repr(obj, max_len=200):
        try:
            r = repr(obj)
            if len(r) > max_len:
                r = r[:max_len] + '...'
            return r
        except Exception:
            return f'<unreprable {type(obj).__name__}>'

    @staticmethod
    def strip_empty(d):
        return {
            k: v for k, v in d.items()
            if v not in (None, '', (), [], {})
        }

    @staticmethod
    def detect_kind(obj):
        if isinstance(obj, (str, int, float, bool, type(None))):
            return 'scalar'
        if inspect.ismodule(obj):
            return 'module'
        if inspect.isclass(obj):
            return 'class'
        if inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isbuiltin(obj) or inspect.ismethoddescriptor(obj):
            return 'callable'
        if isinstance(obj, dict):
            return 'dict'
        if isinstance(obj, list):
            return 'list'
        if isinstance(obj, tuple):
            return 'tuple'
        if isinstance(obj, set):
            return 'set'
        if isinstance(obj, frozenset):
            return 'frozenset'
        return 'object'

    @staticmethod
    def should_recurse(recursive, depth, max_depth):
        if recursive:
            return True
        return depth < max_depth

    @staticmethod
    def is_function_like(obj):
        return (
            inspect.isfunction(obj)
            or inspect.ismethod(obj)
            or inspect.isbuiltin(obj)
            or inspect.ismethoddescriptor(obj)
        )

    @staticmethod
    def is_expandable(obj):
        return (
            inspect.ismodule(obj)
            or inspect.isclass(obj)
            or isinstance(obj, dict)
            or isinstance(obj, (list, tuple, set, frozenset))
            or hasattr(obj, '__dict__')
        )

    @staticmethod
    def get_size(obj, seen=None):
        if obj is None:
            return 0

        if seen is None:
            seen = set()

        obj_id = id(obj)
        if obj_id in seen:
            return 0
        seen.add(obj_id)

        try:
            size = sys.getsizeof(obj)
        except Exception:
            size = 0

        if isinstance(obj, dict):
            for k, v in list(obj.items()):
                size += ObjectInfo.get_size(k, seen)
                size += ObjectInfo.get_size(v, seen)

        elif hasattr(obj, '__dict__'):
            try:
                size += ObjectInfo.get_size(vars(obj), seen)
            except Exception:
                pass

        elif isinstance(obj, (list, tuple, set, frozenset)):
            for i in obj:
                size += ObjectInfo.get_size(i, seen)

        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
            try:
                for i in obj:
                    size += ObjectInfo.get_size(i, seen)
            except Exception:
                pass

        return size

    @staticmethod
    def get_shallow_size(obj):
        try:
            return sys.getsizeof(obj)
        except Exception:
            return None

    @staticmethod
    def get_file(obj):
        try:
            return inspect.getsourcefile(obj) or inspect.getfile(obj)
        except Exception:
            return None

    @staticmethod
    def get_line(obj):
        try:
            _, line = inspect.getsourcelines(obj)
            return line
        except Exception:
            return None

    @staticmethod
    def get_end_line(obj):
        try:
            lines, line = inspect.getsourcelines(obj)
            return line + len(lines) - 1
        except Exception:
            return None

    @staticmethod
    def get_signature(obj):
        try:
            return str(inspect.signature(obj))
        except Exception:
            return None

    @staticmethod
    def get_source(obj):
        try:
            return inspect.getsource(obj)
        except Exception:
            return None

    @staticmethod
    def get_module_name(obj):
        return getattr(obj, '__module__', None)

    @staticmethod
    def get_name(obj):
        return getattr(obj, '__name__', None)

    @staticmethod
    def get_qualname(obj):
        return getattr(obj, '__qualname__', None)

    @staticmethod
    def get_doc(obj):
        return getattr(obj, '__doc__', None)

    @staticmethod
    def get_defaults(obj):
        return getattr(obj, '__defaults__', None)

    @staticmethod
    def get_kwdefaults(obj):
        return getattr(obj, '__kwdefaults__', None)

    @staticmethod
    def get_annotations(obj):
        return getattr(obj, '__annotations__', None)

    @staticmethod
    def get_code_names(obj):
        try:
            return list(obj.__code__.co_names)
        except Exception:
            return None

    @staticmethod
    def get_varnames(obj):
        try:
            return list(obj.__code__.co_varnames)
        except Exception:
            return None

    @staticmethod
    def get_constants(obj):
        try:
            return list(obj.__code__.co_consts)
        except Exception:
            return None

    @staticmethod
    def get_freevars(obj):
        try:
            return list(obj.__code__.co_freevars)
        except Exception:
            return None

    @staticmethod
    def get_cellvars(obj):
        try:
            return list(obj.__code__.co_cellvars)
        except Exception:
            return None

    @staticmethod
    def get_argcount(obj):
        try:
            return obj.__code__.co_argcount
        except Exception:
            return None

    @staticmethod
    def get_kwonlyargcount(obj):
        try:
            return obj.__code__.co_kwonlyargcount
        except Exception:
            return None

    @staticmethod
    def get_nlocals(obj):
        try:
            return obj.__code__.co_nlocals
        except Exception:
            return None

    @staticmethod
    def file_matches(parent_file, child_file):
        if not parent_file or not child_file:
            return None
        return parent_file == child_file

    @staticmethod
    def iter_children(obj):
        if isinstance(obj, dict):
            for k, v in list(obj.items()):
                try:
                    key = str(k)
                except Exception:
                    key = f'<key:{type(k).__name__}>'
                yield key, v
            return

        if isinstance(obj, (list, tuple, set, frozenset)):
            for i, v in enumerate(list(obj)):
                yield f'[{i}]', v
            return

        try:
            for k, v in list(vars(obj).items()):
                if isinstance(k, str) and k.startswith('__') and k.endswith('__'):
                    continue
                if k == '__builtins__':
                    continue
                yield str(k), v
        except Exception:
            return

    @staticmethod
    def basic_info(
        obj,
        path=None,
        parent_path=None,
        parent_file=None,
        include_size=False,
        include_source=False,
        include_doc=False,
        include_code=False,
    ):
        info = {
            'path': path,
            'kind': ObjectInfo.detect_kind(obj),
            'type': type(obj).__name__,
            'type_full': str(type(obj)),
            'callable': callable(obj),
            'repr': ObjectInfo.safe_repr(obj),
            'parent_path': parent_path,
            'parent_file': parent_file,
        }

        if include_size:
            info['size'] = ObjectInfo.get_size(obj)
            info['size_shallow'] = ObjectInfo.get_shallow_size(obj)

        if isinstance(obj, (str, int, float, bool, type(None))):
            info['value'] = obj
            return ObjectInfo.strip_empty(info)

        if inspect.ismodule(obj):
            info['name'] = getattr(obj, '__name__', None)
            info['file'] = getattr(obj, '__file__', None)
            info['package'] = getattr(obj, '__package__', None)
            info['file_matches_parent'] = ObjectInfo.file_matches(parent_file, info.get('file'))
            if info.get('file_matches_parent') is False:
                info['file_mismatch_flag'] = True
            if include_doc:
                info['doc'] = ObjectInfo.get_doc(obj)
            return ObjectInfo.strip_empty(info)

        if inspect.isclass(obj):
            info['name'] = ObjectInfo.get_name(obj)
            info['qualname'] = ObjectInfo.get_qualname(obj)
            info['module'] = ObjectInfo.get_module_name(obj)
            info['file'] = ObjectInfo.get_file(obj)
            info['line_start'] = ObjectInfo.get_line(obj)
            info['line_end'] = ObjectInfo.get_end_line(obj)
            info['mro'] = [c.__name__ for c in getattr(obj, '__mro__', [])]
            info['file_matches_parent'] = ObjectInfo.file_matches(parent_file, info.get('file'))
            if info.get('file_matches_parent') is False:
                info['file_mismatch_flag'] = True
            if include_doc:
                info['doc'] = ObjectInfo.get_doc(obj)
            if include_source:
                info['source'] = ObjectInfo.get_source(obj)
            return ObjectInfo.strip_empty(info)

        if ObjectInfo.is_function_like(obj):
            info['name'] = ObjectInfo.get_name(obj)
            info['qualname'] = ObjectInfo.get_qualname(obj)
            info['module'] = ObjectInfo.get_module_name(obj)
            info['signature'] = ObjectInfo.get_signature(obj)
            info['file'] = ObjectInfo.get_file(obj)
            info['line_start'] = ObjectInfo.get_line(obj)
            info['line_end'] = ObjectInfo.get_end_line(obj)
            info['file_matches_parent'] = ObjectInfo.file_matches(parent_file, info.get('file'))
            if info.get('file_matches_parent') is False:
                info['file_mismatch_flag'] = True
            if include_doc:
                info['doc'] = ObjectInfo.get_doc(obj)
            if include_source:
                info['source'] = ObjectInfo.get_source(obj)
            if include_code:
                info['code_names'] = ObjectInfo.get_code_names(obj)
                info['varnames'] = ObjectInfo.get_varnames(obj)
                info['constants'] = ObjectInfo.get_constants(obj)
                info['freevars'] = ObjectInfo.get_freevars(obj)
                info['cellvars'] = ObjectInfo.get_cellvars(obj)
                info['argcount'] = ObjectInfo.get_argcount(obj)
                info['kwonlyargcount'] = ObjectInfo.get_kwonlyargcount(obj)
                info['nlocals'] = ObjectInfo.get_nlocals(obj)
                info['defaults'] = ObjectInfo.get_defaults(obj)
                info['kwdefaults'] = ObjectInfo.get_kwdefaults(obj)
                info['annotations'] = ObjectInfo.get_annotations(obj)
            return ObjectInfo.strip_empty(info)

        if isinstance(obj, dict):
            info['len'] = len(obj)
            return ObjectInfo.strip_empty(info)

        if isinstance(obj, (list, tuple, set, frozenset)):
            info['len'] = len(obj)
            return ObjectInfo.strip_empty(info)

        cls = getattr(obj, '__class__', None)
        cls_file = ObjectInfo.get_file(cls) if cls else None

        info['class'] = getattr(cls, '__name__', None)
        info['module'] = getattr(cls, '__module__', None) if cls else None
        info['file'] = cls_file
        info['line_start'] = ObjectInfo.get_line(cls) if cls else None
        info['line_end'] = ObjectInfo.get_end_line(cls) if cls else None
        info['file_matches_parent'] = ObjectInfo.file_matches(parent_file, cls_file)
        if info.get('file_matches_parent') is False:
            info['file_mismatch_flag'] = True
        if include_doc:
            info['doc'] = ObjectInfo.get_doc(obj)

        return ObjectInfo.strip_empty(info)

    @staticmethod
    def scan(
        obj,
        path='globals',
        results=None,
        seen=None,
        recursive=False,
        max_depth=2,
        depth=0,
        include_size=False,
        include_source=False,
        include_doc=False,
        include_code=False,
        only_expand=None,
        skip_paths=None,
        max_objects=None,
        parent_path=None,
        parent_file=None,
    ):
        if results is None:
            results = {}
        if seen is None:
            seen = {}
        if skip_paths is None:
            skip_paths = set()

        if max_objects is not None and len(results) >= max_objects:
            return results

        if path in skip_paths:
            return results

        oid = id(obj)

        if oid in seen:
            results[path] = {
                'path': path,
                'kind': 'duplicate',
                'type': type(obj).__name__,
                'repr': ObjectInfo.safe_repr(obj),
                'same_as': seen[oid],
                'parent_path': parent_path,
                'parent_file': parent_file,
            }
            return results

        seen[oid] = path

        info = ObjectInfo.basic_info(
            obj,
            path=path,
            parent_path=parent_path,
            parent_file=parent_file,
            include_size=include_size,
            include_source=include_source,
            include_doc=include_doc,
            include_code=include_code,
        )

        results[path] = info

        if not ObjectInfo.should_recurse(recursive, depth, max_depth):
            return results

        if only_expand is not None:
            try:
                if not only_expand(obj):
                    return results
            except Exception:
                return results
        else:
            if not ObjectInfo.is_expandable(obj):
                return results

        current_file = info.get('file')

        for child_name, child in ObjectInfo.iter_children(obj):
            if max_objects is not None and len(results) >= max_objects:
                return results

            if child_name.startswith('['):
                child_path = f'{path}{child_name}'
            else:
                child_path = f'{path}.{child_name}'

            ObjectInfo.scan(
                child,
                path=child_path,
                results=results,
                seen=seen,
                recursive=recursive,
                max_depth=max_depth,
                depth=depth + 1,
                include_size=include_size,
                include_source=include_source,
                include_doc=include_doc,
                include_code=include_code,
                only_expand=only_expand,
                skip_paths=skip_paths,
                max_objects=max_objects,
                parent_path=path,
                parent_file=current_file,
            )

        return results

    @staticmethod
    def scan_globals(
        globals_dict,
        recursive=False,
        max_depth=2,
        include_size=False,
        include_source=False,
        include_doc=False,
        include_code=False,
        only_expand=None,
        skip_paths=None,
        max_objects=None,
    ):
        return ObjectInfo.scan(
            globals_dict,
            path='globals',
            recursive=recursive,
            max_depth=max_depth,
            include_size=include_size,
            include_source=include_source,
            include_doc=include_doc,
            include_code=include_code,
            only_expand=only_expand,
            skip_paths=skip_paths,
            max_objects=max_objects,
        )

    @staticmethod
    def audit_loaded(
        namespace,
        include_source=False,
        recursive=False,
        max_depth=2,
        include_size=False,
        include_doc=False,
        include_code=True,
        only_expand=None,
        skip_paths=None,
        max_objects=None,
    ):
        return ObjectInfo.scan(
            namespace,
            path='globals',
            recursive=recursive,
            max_depth=max_depth,
            include_size=include_size,
            include_source=include_source,
            include_doc=include_doc,
            include_code=include_code,
            only_expand=only_expand,
            skip_paths=skip_paths,
            max_objects=max_objects,
        )

    @staticmethod
    def summary(results):
        out = {
            'total': len(results),
            'kinds': {},
            'types': {},
            'duplicates': 0,
            'mismatches': 0,
            'with_file': 0,
            'callables': 0,
            'classes': 0,
            'modules': 0,
        }

        for _, info in results.items():
            kind = info.get('kind', 'unknown')
            typ = info.get('type', 'unknown')

            out['kinds'][kind] = out['kinds'].get(kind, 0) + 1
            out['types'][typ] = out['types'].get(typ, 0) + 1

            if kind == 'duplicate':
                out['duplicates'] += 1
            if info.get('file_mismatch_flag'):
                out['mismatches'] += 1
            if info.get('file'):
                out['with_file'] += 1
            if info.get('callable'):
                out['callables'] += 1
            if kind == 'class':
                out['classes'] += 1
            if kind == 'module':
                out['modules'] += 1

        return out

    @staticmethod
    def flagged(results):
        return {
            path: info
            for path, info in results.items()
            if info.get('file_mismatch_flag')
        }

    @staticmethod
    def only_kind(results, kind):
        return {
            path: info
            for path, info in results.items()
            if info.get('kind') == kind
        }

    @staticmethod
    def only_callables(results):
        return {
            path: info
            for path, info in results.items()
            if info.get('callable')
        }

    @staticmethod
    def only_with_file(results):
        return {
            path: info
            for path, info in results.items()
            if info.get('file')
        }

    @staticmethod
    def search_paths(results, text):
        text = str(text).lower()
        return {
            path: info
            for path, info in results.items()
            if text in path.lower()
        }

    @staticmethod
    def flatten_audit(results):
        rows = []
        for path, info in results.items():
            rows.append({
                'path': path,
                'kind': info.get('kind'),
                'type': info.get('type'),
                'callable': info.get('callable'),
                'name': info.get('name'),
                'qualname': info.get('qualname'),
                'class': info.get('class'),
                'module': info.get('module'),
                'file': info.get('file'),
                'line_start': info.get('line_start'),
                'line_end': info.get('line_end'),
                'signature': info.get('signature'),
                'parent_path': info.get('parent_path'),
                'parent_file': info.get('parent_file'),
                'file_matches_parent': info.get('file_matches_parent'),
                'file_mismatch_flag': info.get('file_mismatch_flag', False),
                'same_as': info.get('same_as'),
            })
        return rows
    
# results = ObjectInfo.scan_globals(
#     globals(),
#     recursive=True,
#     include_source=True,
#     include_doc=True,
#     include_code=True,
#     include_size=True,
#     max_objects=5000
# )





# # safer
# results = ObjectInfo.scan_globals(
#     globals(),
#     recursive=False,
#     include_source=False,
#     include_doc=False,
#     include_code=True,
#     include_size=False,
#     max_objects=5000
# )

# # print(json.dumps(results, indent=4))

results = ObjectInfo.scan(CountCalls, recursive=True, path='CountCalls')



from pprint import pprint
pprint(results)