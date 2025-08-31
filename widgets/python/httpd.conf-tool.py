import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
    _.switches.register( 'CheckPaths', '-p,-path,-paths' )
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

import os
import re

def scrape_and_check_paths1(text):
    """
    Extracts Linux file paths from text and checks if they exist.

    Args:
        text (str): Input text containing possible Linux file paths.
    
    Returns:
        dict: { "path": True/False } for each found path
    """
    # Regex: match absolute Linux paths like /home/user/file.txt
    pattern = r'(/(?:[A-Za-z0-9._-]+/)*[A-Za-z0-9._-]+)'
    
    matches = re.findall(pattern, text)
    unique_paths = list(set(matches))  # remove duplicates
    
    results = {}
    for path in unique_paths:
        results[path] = os.path.exists(path)
    
    return results



def scrape_and_check_paths(text):
    """
    Extracts Linux file paths from text and checks if they exist.
    Skips paths immediately following a '<' (e.g., <Directory /path>).
    """
    # Negative lookbehind ensures path is not preceded by '<'
    pattern = r'(?<!<)(/(?:[A-Za-z0-9._-]+/)*[A-Za-z0-9._-]+)'
    
    matches = re.findall(pattern, text)
    unique_paths = list(set(matches))  # remove duplicates
    
    results = {}
    for path in unique_paths:
        results[path] = os.path.exists(path)
    
    return results


def action():
    active = False
    last = ''
    lines = _.isData(2)
    lines.reverse()
    found = []
    sections = []
    section = []
    for i, line in enumerate(lines):
        line = line.rstrip()
        added=False
        if active and line.startswith(last):
            section.append(line)
            added=True
            sections.append(section)
            section = []
            active = False
            last = ''

        elif line.startswith('</'):
            # print(line)
            last = line.replace('</','<').strip().rstrip('>')
            # print(last);return
            active = True
        if not added:
            section.append(line)

    code = []
    sections.reverse()
    for section in sections:
        section.reverse()
        code.append('\n'.join(section))

    relevant = ''

    for section in code:
        if _.showLine(section):
            _.pr(line=1,c='yellow')
            _.pr(section)
            relevant += section
    if _.switches.isActive('CheckPaths'):
        results = scrape_and_check_paths(relevant)
        for path, exists in results.items():
            _.pr(f"Path: {path}, Exists: {exists}")

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)