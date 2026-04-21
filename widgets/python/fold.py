import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

# 694a436b-a248-832a-b479-cca787979306

# fold.py  (folder counterpart to files)
# default: relative output + NOT recursive
# note: -f is reserved for Has-Files in fold (per your spec), so Folder uses -d/-dir

def sw():
    swGrp = 1

    # ----------------------------
    # Folder Settings
    # ----------------------------
    _.switches.trigger('Folder', _.myFolderLocations)  # if you have a location helper like files
    _.switches.register('Recursive', '-r,-recursive', group=[swGrp, 'Folder Settings'])
    _.switches.register('Folder', '-d,-dir,-folder', group=[swGrp, 'Folder Settings'])
    _.switches.register('MaxDepth', '-depth', '3', group=[swGrp, 'Folder Settings'])
    _.switches.register('No-Linked-Folders', '-nl,-nolinks', group=[swGrp, 'Folder Settings'])

    swGrp += 1

    # ----------------------------
    # Formatting and Output
    # ----------------------------
    _.switches.register('Count', '-c,-count,--c', group=[swGrp, 'Formatting and Output'])
    _.switches.register('Full-Path', '-p,-full,--fullpath', group=[swGrp, 'Formatting and Output'])
    _.switches.register('Blank', '-blank', group=[swGrp, 'Formatting and Output'])
    _.switches.register('Clean', '-clean', group=[swGrp, 'Formatting and Output'])

    swGrp += 1

    # ----------------------------
    # Folder File Filters
    # ----------------------------
    # Requires folder contains ALL specified files (exact names or wildcards)
    _.switches.register('Has-Files', '-f,-fi,-file,-files', group=[swGrp, 'Folder File Filters'])

    # Folder contains files by name pattern OR substring:
    #   - "*.py" matches by glob
    #   - "index.php" matches "index.php.backup"
    _.switches.register('File-Has', '-filehas,-fh', group=[swGrp, 'Folder File Filters'])

    swGrp += 1

    # ----------------------------
    # File Contents Filters
    # ----------------------------
    # Searches for text inside files (binary files skipped).
    # If used alone => scans ALL non-binary files in each folder.
    # If used with Has-Files and/or File-Has => scans ONLY matching files.
    _.switches.register('File-Contains', '-has,-contains,-content,-contents,-cont', group=[swGrp, 'File Contents Filters'])

_._default_settings_()

_.appInfo[focus()] = {
    'file': 'fold.py',
    'description': 'List and analyze folders with advanced filters for filenames, filename patterns, and file contents. Defaults to relative paths and non-recursive traversal.',
    'categories': [
        'DEFAULT',
        'FILES',
        'FOLDERS',
        'SEARCH',
    ],
    'examples': [
        _.hp('p fold'),
        _.linePrint(label='default (relative paths, not recursive)', p=0),
        '',

        _.hp('p fold -r'),
        _.linePrint(label='recursive folder traversal', p=0),
        '',

        _.hp('p fold -p'),
        _.linePrint(label='show full paths instead of relative', p=0),
        '',

        _.hp('p fold -d /var/www'),
        _.linePrint(label='start from a specific folder', p=0),
        '',

        _.hp('p fold -f index.php -f .htaccess'),
        _.linePrint(label='only folders containing index.php AND .htaccess', p=0),
        '',

        _.hp('p fold -filehas "*.py"'),
        _.linePrint(label='only folders containing files matching a name or pattern', p=0),
        '',

        _.hp('p fold -has "RewriteEngine On"'),
        _.linePrint(label='folders where ANY non-binary file contains a string', p=0),
        '',

        _.hp('p fold -f index.php -has "RewriteEngine On"'),
        _.linePrint(label='search for content only inside specific files', p=0),
        '',

        _.hp('p fold -filehas "*.py" -has "import requests"'),
        _.linePrint(label='search content only inside matching filename patterns', p=0),
        '',

        _.hp('p fold -blank'),
        _.linePrint(label='show empty folders', p=0),
        '',

        _.hp('p fold -blank -clean'),
        _.linePrint(label='delete empty folders (use with care)', p=0),
        '',

        _.hp('p fold -c'),
        _.linePrint(label='count only (no folder listing)', p=0),
        '',
    ],
    'aliases': [
        'foldr',
        'folders',
    ],
    'relatedapps': [
        'files',
        'grep',
    ],
    'prerequisite': [
        'Read access to target folders',
    ],
    'notes': [
        'Relative paths are shown by default; use -p to force full paths.',
        'Traversal is non-recursive unless -r is specified.',
        'Has-Files (-f) requires all specified filenames to exist in the folder.',
        'File-Has filters by filename pattern or substring.',
        'File-Contains (-has) searches file contents; binary files are skipped automatically.',
        'When -has is used alone, all non-binary files are scanned.',
        'When -has is combined with -f or -filehas, only matching files are scanned.',
        'Use -blank with -clean carefully; folders are deleted using os.rmdir().',
    ],
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
import fnmatch

# ----------------------------
# SWITCHES (modified defaults)
#   - default: relative path output
#   - default: NOT recursive
# ----------------------------




# ----------------------------
# Globals
# ----------------------------
activeFolders = {}
allFolders = []
baseDepth = 0
base_path = ''
i = 0


# ----------------------------
# Helpers
# ----------------------------
def _list_dir_safe(folder):
    try:
        return os.listdir(folder)
    except Exception:
        return None


def _is_nonbinary_file(path, sniff_bytes=4096):
    try:
        with open(path, 'rb') as f:
            chunk = f.read(sniff_bytes)
        if b'\x00' in chunk:
            return False
        return True
    except Exception:
        return False


def _read_text_loose(path, max_bytes=2_000_000):
    """
    Best-effort text read (no hard encoding assumptions).
    """
    try:
        with open(path, 'rb') as f:
            data = f.read(max_bytes)
        # decode loosely; errors ignored so “weird” encodings won't blow up
        return data.decode('utf-8', errors='ignore')
    except Exception:
        return ''


def _files_in_folder(folder, dir_list):
    # filenames only
    return [name for name in dir_list if os.path.isfile(os.path.join(folder, name))]


def _match_has_files(files, required):
    """
    Has-Files:
      - wildcard tokens (* ? [) => fnmatch
      - else exact filename match
    """
    for req in required:
        if not req:
            continue
        if any(ch in req for ch in ['*', '?', '[', ']']):
            if not any(fnmatch.fnmatch(name, req) for name in files):
                return False
        else:
            if req not in files:
                return False
    return True


def _match_file_has(files, patterns):
    """
    File-Has:
      - wildcard => fnmatch
      - else substring match (index.php matches index.php.backup)
    All patterns must be satisfied (AND), matching your old behavior style.
    """
    for pat in patterns:
        if not pat:
            continue
        if any(ch in pat for ch in ['*', '?', '[', ']']):
            if not any(fnmatch.fnmatch(name, pat) for name in files):
                return False
        else:
            if not any(pat in name for name in files):
                return False
    return True


def _candidate_files_for_content_scan(folder, dir_list):
    """
    If File-Contains is used:
      - If Has-Files and File-Has are NOT used => scan ALL non-binary files
      - Else => scan only the corresponding files (i.e., constrained by Has-Files and/or File-Has)
    """
    files = _files_in_folder(folder, dir_list)

    has_files_active = _.switches.isActive('Has-Files') and len(_.switches.values('Has-Files')) > 0
    file_has_active = _.switches.isActive('File-Has') and len(_.switches.values('File-Has')) > 0

    # No filename constraints => scan everything (non-binary filtering happens later)
    if not has_files_active and not file_has_active:
        return [os.path.join(folder, name) for name in files]

    # Constrained scan: build list of files that satisfy the active constraints
    required = _.switches.values('Has-Files') if has_files_active else []
    patterns = _.switches.values('File-Has') if file_has_active else []

    def ok_name(name):
        ok = True
        if has_files_active:
            # For Has-Files, it’s “folder must have reqs”, but for scanning we only scan files that match
            # the req tokens. If multiple req tokens exist, we scan the union of those matches.
            # We'll handle union outside this function.
            pass
        if file_has_active:
            # For File-Has, scan files that match ALL file-has patterns (intersection)
            for pat in patterns:
                if not pat:
                    continue
                if any(ch in pat for ch in ['*', '?', '[', ']']):
                    if not fnmatch.fnmatch(name, pat):
                        ok = False
                        break
                else:
                    if pat not in name:
                        ok = False
                        break
        return ok

    selected = set()

    # If Has-Files is active: select files that match ANY of the Has-Files tokens (union),
    # but still respect File-Has constraints if also active.
    if has_files_active:
        for req in required:
            if not req:
                continue
            if any(ch in req for ch in ['*', '?', '[', ']']):
                for name in files:
                    if fnmatch.fnmatch(name, req) and ok_name(name):
                        selected.add(os.path.join(folder, name))
            else:
                if req in files and ok_name(req):
                    selected.add(os.path.join(folder, req))
    else:
        # Only File-Has active: scan all files that satisfy File-Has (intersection)
        for name in files:
            if ok_name(name):
                selected.add(os.path.join(folder, name))

    return list(selected)


def _folder_passes_filename_filters(folder, dir_list):
    """
    Applies Has-Files and File-Has as folder-level filters.
    (If you specify these, only folders that satisfy them count/print.)
    """
    files = _files_in_folder(folder, dir_list)

    if _.switches.isActive('Has-Files'):
        required = _.switches.values('Has-Files')
        if required and not _match_has_files(files, required):
            return False

    if _.switches.isActive('File-Has'):
        patterns = _.switches.values('File-Has')
        if patterns and not _match_file_has(files, patterns):
            return False

    return True


def _folder_passes_content_filter(folder, dir_list):
    """
    File-Contains:
      - if not active => True
      - if active => any provided needle appears in any eligible file's content
    """
    if not _.switches.isActive('File-Contains'):
        return True

    needles = _.switches.values('File-Contains')
    needles = [n for n in needles if n]
    if not needles:
        return True

    candidates = _candidate_files_for_content_scan(folder, dir_list)
    for path in candidates:
        if not _is_nonbinary_file(path):
            continue
        txt = _read_text_loose(path)
        if not txt:
            continue
        for n in needles:
            if n in txt:
                return True

    return False


def _folder_matches_all_filters(folder, dir_list):
    if not _folder_passes_filename_filters(folder, dir_list):
        return False
    if not _folder_passes_content_filter(folder, dir_list):
        return False
    return True


# ----------------------------
# Core
# ----------------------------
def process(folder):
    if folder.startswith('/proc'):
        return None

    global activeFolders
    global allFolders
    global i
    global baseDepth
    global base_path

    if not os.path.isdir(folder):
        return None

    if _.switches.isActive('No-Linked-Folders'):
        if os.path.islink(folder):
            return None

    folder = os.path.abspath(folder)

    # Depth guard only matters if we're going to recurse
    if _.switches.isActive('Recursive') and _.switches.isActive('MaxDepth'):
        if len(_.switches.value('MaxDepth')):
            maxDepth = int(_.switches.values('MaxDepth')[0])
        else:
            maxDepth = 4

        if len(folder.split(_v.slash)) - baseDepth >= maxDepth:
            if len(_.switches.values('MaxDepth')) > 1 and 'p' in _.switches.values('MaxDepth')[1]:
                _.pr(folder)
            return None

    dirList = _list_dir_safe(folder)
    if dirList is None:
        return None

    folder_matches = _folder_matches_all_filters(folder, dirList)

    for item in dirList:
        path = folder + _v.slash + item
        path = path.replace(_v.slash + _v.slash, _v.slash).replace(_v.slash + _v.slash, _v.slash)

        if os.path.isfile(path):
            # Only mark activeFolders for matching folders
            if folder_matches:
                if folder.lower() not in activeFolders:
                    activeFolders[folder.lower()] = 1

                pathParts = folder.split(_v.slash)
                while len(pathParts):
                    pathParts.pop(len(pathParts) - 1)
                    pp = _v.slash.join(pathParts)
                    if pp and pp.lower() not in activeFolders:
                        activeFolders[pp.lower()] = 1

        elif os.path.isdir(path):
            if _.showLine(path):
                # Only count/print folders that match filters
                if folder_matches:
                    allFolders.append(path)
                    i += 1
                    if not _.switches.isActive('Blank'):
                        if _.switches.isActive('Full-Path'):
                            _.pr(path, c='cyan')
                        else:
                            pAth = path.replace(base_path, '')[1:]
                            _.pr(pAth, c='cyan')

            # Default is NOT recursive; recurse only if switch enabled
            if _.switches.isActive('Recursive'):
                process(path)

    return None


def del_folder(folder):
    try:
        os.rmdir(folder)
        _.pr(folder, c='red')
        return True
    except OSError:
        _.pr(folder, c='green')
        return False


def action():
    global activeFolders
    global allFolders
    global i
    global baseDepth
    global base_path

    if _.switches.isActive('Clean'):
        _.switches.fieldSet('Blank', 'active', True)

    activeFolders = {}
    allFolders = []
    i = 0

    if not _.switches.isActive('Count'):
        _.pr()
        _.colorThis(['Folders:\n'], 'green')

    # Walk start folders
    if _.switches.isActive('Folder'):
        for folder in _.switches.values('Folder'):
            baseDepth = len(folder.split(_v.slash))
            base_path = folder
            process(folder)
            allFolders.append(folder)
    else:
        folder = os.getcwd()
        baseDepth = len(folder.split(_v.slash))
        base_path = folder
        process(folder)
        allFolders.append(folder)

    # If Blank: identify folders with no files (per your existing behavior)
    if _.switches.isActive('Blank'):
        allFolders.reverse()
        ii = 0
        for f in allFolders:
            if f.lower() not in activeFolders:
                if _.switches.isActive('Clean'):
                    if del_folder(f):
                        ii += 1

    # Summary
    if _.switches.isActive('Blank'):
        if not _.switches.isActive('Count'):
            if i == ii:
                _.colorThis(['', i], 'yellow')
            else:
                _.colorThis(['', ii, 'of', i, 'are blank'], 'yellow')
    else:
        if not _.switches.isActive('Count'):
            _.colorThis(['', i], 'yellow')

    if not _.switches.isActive('Count'):
        _.pr()
        _.colorThis([base_path], 'darkcyan')




########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)