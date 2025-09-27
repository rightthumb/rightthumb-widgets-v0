import sys, os

try:
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'code', 'classes')))
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'os', 'file')))
except:
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'library', 'code', 'classes')))
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'library', 'os', 'file')))


from index import index
from bkExpire import bkExpire


# p ic
# p ic
# p ic

intelligent_code = Meta_Namespace()
intelligent_code.functions = {}
intelligent_code.classes = {}

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




class index:
	def __new__(cls, *args, **kwargs):
		import importlib.util
		if 'index' not in intelligent_code.classes:
			import importlib.util
			path = os.path.normpath(_v.w+'/widgets/python/library/code/classes/index.py')
			spec = importlib.util.spec_from_file_location('index', path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			intelligent_code.classes['index'] = module.index
		return intelligent_code.classes['index'](*args, **kwargs)



def intelligent_function(*args, **kwargs):
    global intelligent_function
    from my_module import actual_function
    intelligent_function = actual_function
    return intelligent_function(*args, **kwargs)


