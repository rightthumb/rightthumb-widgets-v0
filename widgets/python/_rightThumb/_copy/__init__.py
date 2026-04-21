# import _rightThumb._copy as _copy

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


# _copy.copy( data )
# _copy.paste()

def formatData( result ):
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	return result

def clip_set_0(data,end=''):
	global win32clipboard
	if win32clipboard is None:
		import win32clipboard
	# set clipboard data
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	try:
		win32clipboard.SetClipboardText( cleanString(data)+end )
	except Exception as e:
		win32clipboard.EmptyClipboard()
		_.colorThis(  [ 'Unable to set clipboard data' ], 'red'  )
	win32clipboard.CloseClipboard()


def clip_set_2(data,end=''):
	import pyperclip
	pyperclip.copy( cleanString(data)+end )

def clip_set_3(data,end=''):
	import subprocess
	if _.isWin:
		_.cp( 'Error: clipboard error', 'red' )
		return None

	tmpA = _v.stmp +_v.slash+ 'cryptString-A.txt'
	tmpB = _v.stmp +_v.slash+ 'cryptString-B.txt'
	if os.path.isfile(tmpA):
		os.unlink(tmpA)
	if os.path.isfile(tmpB):
		os.unlink(tmpB)
	
	_.saveText( cleanString(data)+end, tmpA )
	time.sleep(.2)
	if not os.path.isfile(tmpA):
		print( 'no file' )
		return None

	# cmd = ["cat", tmpA, "|",  "xsel", "--clipboard", "--input"  ]
	# mycmd=subprocess.getoutput( ' '.join(cmd) )
	from subprocess import Popen, PIPE
	p = Popen(['xsel','-pi'], stdin=PIPE)
	p.communicate(input= formatData(data) )

	p = Popen(['xsel', '-bi'], stdin=PIPE)
	p.communicate(input= formatData(data) )
	# p.communicate(input=data)


	result = None
	try:
		result = clip_get_3()
	except Exception as e:
		result = None

	if not result:
		# print( ' '.join(cmd) )
		_.cp( 'Error: unable to copy', 'red' )
		print(data)

	# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

	# p1 = subprocess.Popen(["cat", tmpA], stdout=subprocess.PIPE)
	# p2 = subprocess.Popen(["xsel", "--clipboard", "--input"], stdin=p1.stdout, stdout=subprocess.PIPE)
	# p2.communicate()


	time.sleep(.2)
	if os.path.isfile(tmpA):
		return _.getText( tmpA, raw=True, clean=2 )
	return None


def clip_set_1(data,end=''):
	from tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append( cleanString(data)+end )
	# r.destroy()

def clip_set( data, end='' ):
	# clip_set_3(data)
	try:
		clip_set_2(data,end)
	except Exception as e:
		try:
			clip_set_1(data,end)
		except Exception as e:
			try:
				clip_set_3(data,end)
			except Exception as e:
				_.cp( 'Error: clipboard error', 'red' )
				sys.exit()


def clip_get():
	result = 'error'
	try:
		result = clip_get_2()
	except Exception as e:
		_.cp( '\tpython3 -m pip install pyperclip', 'yellow' )
		try:
			result = clip_get_1()
		except Exception as e:
			try:
				result = clip_get_3()
			except Exception as e:
				_.cp( 'Error: clipboard error', 'red' )
				_.cp( '\tpython3 -m pip install pyperclip', 'yellow' )

	if not result:
		_.cp( 'Error: clipboard error', 'red' )
		_.cp( '\tpython3 -m pip install pyperclip', 'yellow' )
		sys.exit()
	# print( result )
	# sys.exit()
	return result


def clip_get_1():
	from tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	return r.clipboard_get()


def clip_get_3():
	import subprocess
	# print('_.isWin:',_.isWin)
	if _.isWin:
		_.cp( 'Error: clipboard error', 'red' )
		return None

	tmpA = _v.stmp +_v.slash+ 'cryptString-A.txt'
	tmpB = _v.stmp +_v.slash+ 'cryptString-B.txt'
	if os.path.isfile(tmpA):
		os.unlink(tmpA)
	if os.path.isfile(tmpB):
		os.unlink(tmpB)
	if not _.which('xsel'):
		if not _.isWin:
			print( '\tsudo apt install xclip xsel' )
			return None

	cmd = ["xsel", "--clipboard", "--output", ">", tmpA ]
	# print( ' '.join(cmd) )
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	if os.path.isfile(tmpA):
		return _.getText( tmpA, raw=True, clean=2 )
	return None
	# return _.which('xsel')
	# return _.which('xclip')
	# return _.which('python3')

	# return 'test'

def clip_get_2():
	import pyperclip
	return cleanString( pyperclip.paste() )

	# global win32clipboard
	# if win32clipboard is None:
	#     import win32clipboard
	# # get clipboard data
	# win32clipboard.OpenClipboard()
	# data = win32clipboard.GetClipboardData()
	# win32clipboard.CloseClipboard()
	# return data

win32clipboard = None

def cleanString(data):
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	return data

def cleanStringA(data):
	data = _str.cleanBE(data, _v.default_powershell)
	data = _str.cleanBE(data,'\r')
	data = _str.cleanBE(data,'\n')
	data = _str.cleanBE(data,'\r')
	data = _str.cleanBE(data,'\t')
	data = _str.cleanBE(data,' ')
	return data

copy = clip_set
paste = clip_get

win32clipboard = None


