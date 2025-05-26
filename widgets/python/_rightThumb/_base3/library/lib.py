
from _rightThumb._base3.library.tools.code.classes.index import  index

from _rightThumb._base3.library.tools.functions.os.file.bkExpire import  bkExpire

# p ic
# p ic
# p ic

intelligent_code = Meta_Namespace()
intelligent_code.functions = {}
intelligent_code.classes = {}

def create_backup_filename(*args, **kwargs):
	if not 'create_backup_filename' in intelligent_code.functions:
		from _rightThumb._base3.library.tools.functions.os.file.create_backup_filename import  create_backup_filename
		intelligent_code.functions['create_backup_filename'] = create_backup_filename
	return intelligent_code.functions['create_backup_filename'](*args, **kwargs)




class index:
	def __new__(cls, *args, **kwargs):
		if not 'index' in intelligent_code.classes:
			from _rightThumb._base3.library.tools.code.classes.index import  index as live
			intelligent_code.classes['index'] = live
		return intelligent_code.classes['index'](*args, **kwargs)



def intelligent_function(*args, **kwargs):
    global intelligent_function
    from my_module import actual_function
    intelligent_function = actual_function
    return intelligent_function(*args, **kwargs)


class index:
	_live_class = None
	def __new__(cls, *args, **kwargs):
		if cls._live_class is None:
			from _rightThumb._base3.library.tools.code.classes.index import  index as live
			intelligent_code.classes['index'] = live
			cls._live_class = live
		return cls._live_class(*args, **kwargs)