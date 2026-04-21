import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
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

defaultPythonModules = '''
__future__
abc
aifc
argparse
array
ast
asynchat
asyncio
asyncore
base64
bdb
binascii
binhex
bisect
builtins
bz2
calendar
cgi
cgitb
chunk
cmath
cmd
code
codecs
codeop
collections
colorsys
compileall
concurrent
configparser
contextlib
copy
copyreg
crypt
csv
ctypes
curses
dataclasses
datetime
dbm
decimal
difflib
dis
doctest
email
encodings
ensurepip
enum
filecmp
fileinput
fnmatch
fractions
ftplib
functools
gc
getopt
getpass
gettext
glob
graphlib
gzip
hashlib
heapq
hmac
html
http
imaplib
imghdr
importlib
inspect
io
ipaddress
json
keyword
lib2to3
linecache
locale
logging
lzma
mailbox
mailcap
marshal
math
mimetypes
modulefinder
msilib (Windows)
multiprocessing
netrc
nntplib
numbers
operator
optparse
os
pathlib
pdb
pickle
pickletools
pipes (Unix only)
pkgutil
platform
plistlib
poplib
posixpath
pprint
profile
pstats
pty
pwd (Unix)
py_compile
pyclbr
pydoc
queue
quopri
random
re
readline (Unix)
reprlib
resource (Unix)
rlcompleter
runpy
sched
secrets
select
selectors
shelve
shlex
shutil
signal
site
smtpd
smtplib
sndhdr
socket
socketserver
sqlite3
ssl
stat
statistics
string
stringprep
struct
subprocess
sunau
symtable
sys
sysconfig
tabnanny
tarfile
telnetlib
tempfile
termios (Unix)
textwrap
threading
time
timeit
tkinter (if installed)
token
tokenize
trace
traceback
tracemalloc
tty (Unix)
turtle
types
typing
unicodedata
unittest
urllib
uu
uuid
venv
warnings
wave
weakref
webbrowser
wsgiref
xdrlib
xml
xmlrpc
zipapp
zipfile1
zipimport
zlib
zoneinfo
'''.strip().split('\n')

def action():
	for line in _.isData(2):
		line=line.strip()
		if all(word not in line for word in defaultPythonModules):
			_.pr(line)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)