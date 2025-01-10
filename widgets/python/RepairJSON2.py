import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'File', '-f,-file','fileBackup-corrupt.json' )
	_.switches.register( 'Save', '-save','fileBackup.json' )
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
#N)--> START


import orjson
import jsonlines

def repair_json(input_file, output_file):
    """
    Repair a large corrupted JSON file while keeping key integrity.
    """
    repaired_data = []
    error_count = 0
    try:
        with open(input_file, 'r') as infile:
            for line in infile:
                try:
                    data = orjson.loads(line)
                    repaired_data.append(data)
                except orjson.JSONDecodeError:
                    error_count += 1
                    continue
        with jsonlines.open(output_file, mode='w') as outfile:
            for item in repaired_data:
                outfile.write(item)
        print(f"Repair complete! Errors encountered: {error_count}")
        print(f"Repaired file saved as: {output_file}")
    except Exception as e:
        print(f"Error: {e}")


def action():
    input_file = _.switches.value('File')
    output_file = _.switches.value('Save')
    repair_json(input_file, output_file)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);