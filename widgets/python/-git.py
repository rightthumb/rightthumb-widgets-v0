import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    _.switches.register( 'Scan', '-scan' )
    _.switches.register( 'Recursive', '-r', '3 (depth)' )
    _.switches.register( 'ShowFolders', '-f' )
_._default_settings_()

_.appInfo[focus()] = {
    'file': '-git.py',
    'description': 'Rebuilds git clone command from meta',
    'categories': [
                        'reverse-engineer',
                        'git',
                        'cli',
                ],
    'examples': [

                        _.hp('p -git.py'),
                        _.hp('p -git.py -scan'),
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


cnt = 0

import os

def get_git_clone_command(folder_path):
    global cnt
    git_config_path = os.path.join(folder_path, '.git', 'config')
    if os.path.isfile(git_config_path):
        try:
            with open(git_config_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if 'url = ' in line:
                        url = line.split('url = ')[1].strip()
                        folder_name = os.path.basename(folder_path)
                        cnt += 1
                        return f'git clone {url} {folder_name}'
        except Exception as e:
            return f'# Error reading config: {e}'
    return None


def scan_git_folders(base_dir='.'):
    results = {}
    for name in os.listdir(base_dir):
        path = os.path.join(base_dir, name)
        if os.path.isdir(path):
            cmd = get_git_clone_command(path)
            if cmd:
                results[path] = cmd
    return results


def scan_git_folders_recursive(base_dir='.', max_depth=0):
    results = {}

    def walk(current_path, current_depth):
        if max_depth and current_depth > max_depth:
            return
        cmd = get_git_clone_command(current_path)
        if cmd:
            results[current_path] = cmd
        try:
            for item in os.listdir(current_path):
                item_path = os.path.join(current_path, item)
                if os.path.isdir(item_path):
                    walk(item_path, current_depth + 1)
        except Exception as e:
            pass

    walk(base_dir, 0)
    return results


import re

def getPackage(cmd):
    cmd = cmd.strip()
    cmd = cmd.replace('git clone ', '')
    cmd = cmd.split(' ')[0]
    # Remove possible token-authenticated GitHub URLs
    cmd = re.sub(r'https://[^@]+@github\.com/', '', cmd)
    cmd = cmd.replace('https://github.com/', '')
    cmd = cmd.replace('.git', '')
    return cmd


from collections import defaultdict

def action():
    commands = []
    folder_rows = []
    seen = set()
    global cnt
    cnt = 0

    if _.switches.isActive('Recursive'):
        if len(_.switches.value('Recursive')):
            depth = int(_.switches.value('Recursive'))
        else:
            depth = 0  # unlimited
        results = scan_git_folders_recursive('.', depth)
    elif _.switches.isActive('Scan'):
        results = scan_git_folders()
    else:
        cmd = get_git_clone_command(os.getcwd())
        if cmd:
            folder_name = os.path.basename(os.getcwd())
            folder_rows.append({'package': getPackage(cmd), 'folder': os.getcwd(), 'command': cmd})
            if not _.switches.isActive('ShowFolders'):
                _.pr(cmd, c='cyan')
            return
        else:
            _.pr('Error: Not inside a Git clone folder.', c='red')
            return

    for folder, cmd in results.items():
        cnt += 1
        package = os.path.basename(folder.rstrip('/'))

        row = {'package': getPackage(cmd), 'folder': folder, 'command': cmd}
        folder_rows.append(row)

        if not _.switches.isActive('ShowFolders') and cmd not in seen:
            seen.add(cmd)
            commands.append(cmd)

    # Show plain commands
    if not _.switches.isActive('ShowFolders'):
        for cmd in commands:
            _.pr(cmd, c='cyan')

        if len(commands) > 3:
            _.pr('\n# Unique: ', len(commands), c='yellow')

        if cnt != len(commands):
            _.pr('# Total:  ', cnt, c='yellow')

    # Show folder table
    if _.switches.isActive('ShowFolders'):
        def clean(path):
            return path.rstrip('/')

        _.switches.set('Long', 'active', True)
        show_cols = 'package,folder'
        _.pt(folder_rows, show_cols, t={'folder': clean})




########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)