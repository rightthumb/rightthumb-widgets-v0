import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'tasklist2table.py',
    'description': 'Converts windows tasklist.exe output to a table',
    'categories': [
                        'tasklist',
						'table',
						'convert',
						'json',
                ],
    'examples': [
                        _.hp('tasklist | p tasklist2table'),
						_.hp('tasklist | p tasklist2table - svchost + .exe %*  -int MemUsage -s Name MemUsage -g Name -gt MemUsage -aggregate " eot?mem-total=add( int(MemUsage) )); format(eot?mem-total,?size,??kb);"'),
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
    _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
    _.switches.trigger( 'DB', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


'''
# old task.bat
tasklist | p tasklist2table - svchost + .exe %*  -int MemUsage -s Name MemUsage -g Name -gt MemUsage -aggregate " eot?mem-total=add( int(MemUsage) )); format(eot?mem-total,?size,??kb);"


'''


import re

def parse_tasklist(raw_text):
    """
    Convert Windows 'tasklist' output into a list of dicts.
    Memory usage is converted to integer (KB).
    """
    lines = raw_text.strip().splitlines()
    result = []

    # Skip until after the separator line (===...)
    data_started = False
    for line in lines:
        if re.match(r"^=+", line):
            data_started = True
            continue
        if not data_started:
            continue

        # Split into columns based on fixed widths from tasklist
        image_name = line[0:25].strip()
        pid        = line[25:34].strip()
        session    = line[34:51].strip()
        session_no = line[51:64].strip()
        mem_usage  = line[64:].strip()

        # Clean memory usage: remove commas, spaces, 'K'
        mem_int = int(re.sub(r"[^\d]", "", mem_usage))



        if _.isValid(image_name)                           or   False  :
        
        
            result.append({
                "Name": image_name,
                "PID": int(pid),
                "SessionName": session,
                "Session#": int(session_no),
                "MemUsage": mem_int
            })
        

    return result





def action():
    task = parse_tasklist( '\n'.join(_.isData(2))   )
    _.pt(task)

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)