import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

# 694a436b-a248-832a-b479-cca787979306

def sw():
	# fold.py switches (NO registration of framework-wide + / - / -or / -strictcase stuff;
	# those are handled automatically by _.showLine(...))

	# , group=[swGrp,'A Group'] )
	swGrp = 1

	# If you have the same folder-locations helper as files:
	_.switches.trigger('Folder', _.myFolderLocations)

	# ----------------------------
	# Folder Settings
	# ----------------------------
	_.switches.register('Recursive', '-r,-recursive', group=[swGrp,'Folder Settings'])
	_.switches.register('Folder', '-d,-dir,-folder', group=[swGrp,'Folder Settings'])
	_.switches.register('MaxDepth', '-depth', '3', group=[swGrp,'Folder Settings'])
	_.switches.register('No-Linked-Folders', '-nl,-nolinks', group=[swGrp,'Folder Settings'])


	swGrp += 1

	# ----------------------------
	# Formatting and Output
	# ----------------------------
	_.switches.register('Count', '-c,-count,--c', group=[swGrp,'Formatting and Output'])
	_.switches.register('Full-Path', '-p,-full,--fullpath', group=[swGrp,'Formatting and Output'])
	_.switches.register('Reverse', '-rev,-reverse', group=[swGrp,'Formatting and Output'])

	# Blank/Clean behavior (your existing logic: Blank lists empties; Clean deletes empties)
	_.switches.register('Blank', '-blank', group=[swGrp,'Formatting and Output'])
	_.switches.register('Clean', '-clean', group=[swGrp,'Formatting and Output'])


	swGrp += 1

	# ----------------------------
	# Folder File Filters
	# ----------------------------
	# Has-Files: folder must contain ALL specified files (exact or wildcard)
	_.switches.register('Has-Files', '-f,-fi,-file,-files', group=[swGrp,'Folder File Filters'])

	# File-Has: wildcard or substring match; substring allows index.php.backup when given index.php
	_.switches.register('File-Has', '-fh,-filehas', group=[swGrp,'Folder File Filters'])


	swGrp += 1

	# ----------------------------
	# File Contents Filters
	# ----------------------------
	# File-Contains: searches inside files (binary skipped)
	# - if used alone => scans ALL non-binary files in folder
	# - if used with Has-Files and/or File-Has => scans ONLY corresponding files
	_.switches.register('File-Contains', '-has,-contains,-content,-contents,-cont', group=[swGrp,'File Contents Filters'])


	swGrp += 1

	# ----------------------------
	# Intelligence / Defaults
	# ----------------------------
	# Matches files-app behavior: if active, do NOT hide __pycache__ etc.
	_.switches.register('Disable-Intelligence', '-showall', group=[swGrp,'Intelligence / Defaults'])

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
import fnmatch

# =====================================================================================
# fold.py core (NO switch registration)
#
# Goals:
# - mirror the structure of files app (getFolder -> add -> recursion gate)
# - hardcode omit folders (like __pycache__) unless user disables intelligence
# - integrate cleanly with framework search grammar via _.showLine(...)
# - keep your new semantics:
#     Has-Files      -> requires ALL specified filenames/patterns exist in folder
#     File-Has       -> requires ALL patterns match at least one filename (wildcard or substring)
#     File-Contains  -> searches inside files (skips binary)
#         - if File-Contains used alone: scans all non-binary files in folder
#         - if used with Has-Files and/or File-Has: scans only matching files
# - default output is relative unless Full-Path is active (switches exist elsewhere)
# - default traversal is NOT recursive unless Recursive is active (switches exist elsewhere)
# =====================================================================================


# ----------------------------
# Globals
# ----------------------------
activeFolders = {}
allFolders = []
baseDepth = 0
base_path = ''
i = 0


# ----------------------------
# Hardcoded folder omissions
# ----------------------------
DEFAULT_OMIT_FOLDERS = {
    '__pycache__',
    '.git',
    '.svn',
    '.hg',
    'node_modules',
}


# ----------------------------
# Helpers
# ----------------------------
def _list_dir_safe(folder):
    try:
        return os.listdir(folder)
    except Exception:
        return None


def _display_path(path):
    # matches what you print (and what users tend to search for)
    if _.switches.isActive('Full-Path'):
        return path
    rel = path.replace(base_path, '')
    if rel.startswith(os.sep):
        rel = rel[1:]
    return rel


def _omit_folder_name(name):
    # follow files-app behavior: allow disable intelligence to show __pycache__ etc.
    try:
        if getattr(_.v, 'do_not_hide__pycache', False):
            return False
    except Exception:
        pass
    return name.lower() in DEFAULT_OMIT_FOLDERS


def _is_nonbinary_file(path, sniff_bytes=4096):
    try:
        with open(path, 'rb') as f:
            chunk = f.read(sniff_bytes)
        return b'\x00' not in chunk
    except Exception:
        return False


def _read_text_loose(path, max_bytes=2_000_000):
    try:
        with open(path, 'rb') as f:
            data = f.read(max_bytes)
        return data.decode('utf-8', errors='ignore')
    except Exception:
        return ''


def _files_in_folder(folder, dir_list):
    return [name for name in dir_list if os.path.isfile(os.path.join(folder, name))]


def _req_match(files, req):
    # Has-Files token: exact or wildcard
    if any(ch in req for ch in ['*', '?', '[', ']']):
        return any(fnmatch.fnmatch(name, req) for name in files)
    return req in files


def _pat_match(files, pat):
    # File-Has token: wildcard => fnmatch, else substring match
    if any(ch in pat for ch in ['*', '?', '[', ']']):
        return any(fnmatch.fnmatch(name, pat) for name in files)
    return any(pat in name for name in files)


def _folder_passes_filename_filters(folder, dir_list):
    files = _files_in_folder(folder, dir_list)

    # Has-Files: ALL required must exist
    if _.switches.isActive('Has-Files'):
        required = _.switches.values('Has-Files')
        if required:
            for req in required:
                if req and not _req_match(files, req):
                    return False

    # File-Has: ALL patterns must be satisfied
    if _.switches.isActive('File-Has'):
        patterns = _.switches.values('File-Has')
        if patterns:
            for pat in patterns:
                if pat and not _pat_match(files, pat):
                    return False

    return True


def _candidate_files_for_content_scan(folder, dir_list):
    """
    File-Contains behavior:
      - if Has-Files and File-Has are NOT used => scan ALL non-binary files
      - else => scan only the corresponding files (union from Has-Files refined by File-Has)
    """
    files = _files_in_folder(folder, dir_list)

    has_files_active = _.switches.isActive('Has-Files') and len(_.switches.values('Has-Files')) > 0
    file_has_active = _.switches.isActive('File-Has') and len(_.switches.values('File-Has')) > 0

    if not has_files_active and not file_has_active:
        return [os.path.join(folder, name) for name in files]

    required = _.switches.values('Has-Files') if has_files_active else []
    patterns = _.switches.values('File-Has') if file_has_active else []

    def ok_for_file_has(name):
        if not file_has_active:
            return True
        for pat in patterns:
            if not pat:
                continue
            if any(ch in pat for ch in ['*', '?', '[', ']']):
                if not fnmatch.fnmatch(name, pat):
                    return False
            else:
                if pat not in name:
                    return False
        return True

    selected = set()

    if has_files_active:
        # union of Has-Files matches, optionally refined by File-Has
        for req in required:
            if not req:
                continue
            if any(ch in req for ch in ['*', '?', '[', ']']):
                for name in files:
                    if fnmatch.fnmatch(name, req) and ok_for_file_has(name):
                        selected.add(os.path.join(folder, name))
            else:
                if req in files and ok_for_file_has(req):
                    selected.add(os.path.join(folder, req))
    else:
        # only File-Has active => all files that satisfy File-Has intersection
        for name in files:
            if ok_for_file_has(name):
                selected.add(os.path.join(folder, name))

    return list(selected)


def _folder_passes_content_filter(folder, dir_list):
    if not _.switches.isActive('File-Contains'):
        return True

    needles = [n for n in _.switches.values('File-Contains') if n]
    if not needles:
        return True

    candidates = _candidate_files_for_content_scan(folder, dir_list)

    for fpath in candidates:
        if not _is_nonbinary_file(fpath):
            continue
        txt = _read_text_loose(fpath)
        if not txt:
            continue
        for n in needles:
            if n in txt:
                return True

    return False


def _folder_matches_filters(folder, dir_list):
    if not _folder_passes_filename_filters(folder, dir_list):
        return False
    if not _folder_passes_content_filter(folder, dir_list):
        return False
    return True


def _passes_showline(path, name=None):
    """
    Your framework handles + / - / -or / -strictcase etc inside _.showLine().
    We just feed it useful strings.
    """
    try:
        disp = _display_path(path)
        if name and _.showLine(name):
            return True
        if _.showLine(disp):
            return True
        if _.showLine(path):
            return True
    except Exception:
        # if showLine isn't available or errors, don't block output
        return True
    return False


# ----------------------------
# Traversal (files-style)
# ----------------------------
def getFolder(folder, r=True):
    # normalize
    while os.sep + os.sep in folder:
        folder = folder.replace(os.sep + os.sep, os.sep)

    if not os.path.isdir(folder):
        return None

    # omit folders (unless intelligence disabled)
    if _omit_folder_name(os.path.basename(folder)):
        return None

    # (optional) symlink exclusion
    if _.switches.isActive('No-Linked-Folders') and os.path.islink(folder):
        return None

    global baseDepth
    if _.switches.isActive('MaxDepth') and r:
        if len(_.switches.value('MaxDepth')):
            maxDepth = int(_.switches.values('MaxDepth')[0])
        else:
            maxDepth = 4
        if len(folder.split(_v.slash)) - baseDepth >= maxDepth:
            return None

    dirList = _list_dir_safe(folder)
    if dirList is None:
        return None

    # optional reverse (if you have it later; harmless if absent)
    try:
        if _.switches.isActive('Reverse'):
            dirList.reverse()
    except Exception:
        pass

    for item in dirList:
        path = folder + _v.slash + item
        while _v.slash + _v.slash in path:
            path = path.replace(_v.slash + _v.slash, _v.slash)
        add(path, r=r)

    return None


def add(path, r=False):
    global activeFolders
    global allFolders
    global i

    path = path.replace(_v.slash + _v.slash, _v.slash).strip()

    if os.path.isfile(path):
        # mark folder as active if any file exists (used for -blank / -clean logic)
        folder = os.path.dirname(path)
        if folder and folder.lower() not in activeFolders:
            activeFolders[folder.lower()] = 1

        # mark parents as active (matches your old behavior)
        parts = folder.split(_v.slash)
        while len(parts):
            parts.pop()
            pp = _v.slash.join(parts)
            if pp and pp.lower() not in activeFolders:
                activeFolders[pp.lower()] = 1
        return None

    if not os.path.isdir(path):
        return None

    folder = path
    name = os.path.basename(folder)

    # hard omit
    if _omit_folder_name(name):
        return None

    # symlink exclusion
    if _.switches.isActive('No-Linked-Folders') and os.path.islink(folder):
        return None

    dirList = _list_dir_safe(folder)
    if dirList is None:
        return None

    # Evaluate folder filters (Has-Files / File-Has / File-Contains)
    passes_filters = _folder_matches_filters(folder, dirList)

    # Evaluate showLine search (framework query system)
    passes_search = _passes_showline(folder, name=name)

    # Print/count only when the folder qualifies
    if passes_filters and passes_search:
        allFolders.append(folder)
        i += 1

        if not _.switches.isActive('Blank') and _.showLine(folder):
            # allow showLine to be the final arbiter too (matches files app vibe)
            _.pr(_display_path(folder), c='cyan')

    # Recurse only if enabled
    if r and _.switches.isActive('Recursive'):
        getFolder(folder, r=r)

    return None


# ----------------------------
# Deletion (blank folders)
# ----------------------------
def del_folder(folder):
    try:
        os.rmdir(folder)
        _.pr(folder, c='red')
        return True
    except OSError:
        _.pr(folder, c='green')
        return False


# ----------------------------
# Action entry
# ----------------------------
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

    # recursion flag: default off unless switch active
    r = _.switches.isActive('Recursive')

    if _.switches.isActive('Folder'):
        for folder in _.switches.values('Folder'):
            folder = os.path.abspath(folder)
            baseDepth = len(folder.split(_v.slash))
            base_path = folder
            getFolder(folder, r=r)
            allFolders.append(folder)
    else:
        folder = os.getcwd()
        folder = os.path.abspath(folder)
        baseDepth = len(folder.split(_v.slash))
        base_path = folder
        getFolder(folder, r=r)
        allFolders.append(folder)

    # Blank/Clean pass
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