import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'OverwriteWith', '-w,-with','/opt/a_large_shred_file_to_overwrite_with_before_delete' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

import shutil
import os

def create_shred_templates(folder_path):
    sizes = [1, 10, 500, 1024, 5120, 10240]  # Sizes in MB: 1MB, 10MB, 500MB, 1GB, 5GB, 10GB
    for size in sizes:
        file_path = os.path.join(folder_path, f"shred_{size}MB")
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(os.urandom(size * 1024 * 1024))
            print(f"Created shred template: {file_path}")

def get_shred_template(size_in_bytes, folder_path):
    size_in_mb = size_in_bytes // (1024 * 1024)
    sizes = [1, 10, 500, 1024, 5120, 10240]
    best_match = min(sizes, key=lambda x: abs(x - size_in_mb))
    return os.path.join(folder_path, f"shred_{best_match}MB")

def overwrite_file(path, shred_template):
    with open(path, 'wb') as f:
        with open(shred_template, 'rb') as shred_file:
            shutil.copyfileobj(shred_file, f)

def action():
    shred_template_folder = _v.stmp
    create_shred_templates(shred_template_folder)
    
    for path in _.isData():
        if os.path.exists(path):
            try:
                file_size = os.path.getsize(path)
                template = get_shred_template(file_size, shred_template_folder)
                overwrite_file(path, template)
                os.remove(path)
                print(f"Securely deleted: {path}")
            except Exception as e:
                print(f"Error processing {path}: {e}")
        else:
            print(f"File not found: {path}")






########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);