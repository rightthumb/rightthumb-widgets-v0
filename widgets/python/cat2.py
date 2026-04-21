import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'File', '-f,-fi,-file,-files','file.txt' )
	_.switches.register( 'Part', '-p,-pi,-part,-parts',':' )
	_.switches.register( 'LineNumber', '-ln,-line,-linenumber',':' )
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
	# _.switches.trigger( 'Plus', _.ci )
	# _.switches.trigger( 'Minus', _.ci )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start










from typing import Iterator, TextIO, Optional

def stream_lines(path: str,
				encoding: str = "utf-8",
				errors: str = "replace",
				chunk_size: int = 1024 * 1024) -> Iterator[str]:
	"""
	Stream a text file line-by-line using fixed-size chunks.

	- Does not read the whole file into memory.
	- Handles arbitrarily long lines (longer than chunk_size).
	- Replaces decode errors by default so bad bytes don't crash the read.

	Args:
		path: Path to the file.
		encoding: Text encoding used to decode bytes.
		errors: Error handling for decoding (e.g., 'strict', 'ignore', 'replace').
		chunk_size: Number of bytes to read per chunk.

	Yields:
		Decoded lines WITHOUT the trailing newline.
	"""
	buffer = ""
	# newline='' + encoding/errors ensures universal-newline handling without double translation
	with open(path, "rb", buffering=chunk_size) as raw:
		while True:
			b = raw.read(chunk_size)
			if not b:
				break
			buffer += b.decode(encoding, errors=errors)

			# Split on newlines; keep the last (possibly partial) line in buffer
			*lines, buffer = buffer.splitlines(keepends=False)
			for line in lines:
				yield line

	# Flush any remaining partial line (file did not end with newline)
	if buffer:
		yield buffer


def print_file_lines(path: str,
					encoding: str = "utf-8",
					errors: str = "replace",
					chunk_size: int = 1024 * 1024,
					callback=print
					
					) -> None:
	"""
	Convenience wrapper that prints each line as it streams.
	"""

	if _.switches.isActive('Plus'):
		has = _.ci(_.switches.values('Plus'))
		# print(has)
	else:
		has = None
	if _.switches.isActive('Minus'):
		omit = _.ci(_.switches.values('Minus'))
	else:
		omit = None
	if _.switches.isActive('Part'):
		part = _.ci(_.switches.value('Part'))
	else:
		part = None
	# print(part); return
	ln = _.switches.isActive('LineNumber')
	lnOnly = len(_.switches.value('LineNumber'))
	if lnOnly > 1:
		lnCNT = int(_.switches.value('LineNumber'))
	i = 0
	lastSearch = 'conversation_id'
	lastSearch = '"title":'
	lastSearch = None
	last = None
	for line in stream_lines(path, encoding=encoding, errors=errors, chunk_size=chunk_size):
		i += 1
		if lastSearch and lastSearch in line:
			last = line.strip().replace('"','').strip(',')
		if _.validLine(line, has=has, omit=omit):
			if part:
				line = line.split(part)[0]
			if ln:
				if lnOnly:
					if last: _.pr('\n',last, c='yellow'); last = None
					if lnOnly > 1:
						_.pr(f"{i}:   {line.strip()[:lnCNT]}", c='cyan')
					else:
						_.pr(f"{i}", c='cyan')
				else:
					print(f"{i}: {line}")
			else:
				print(line)
		


# Example usage:
# for line in stream_lines("/var/log/secure"):
#     process(line)
#
# print_file_lines("huge.txt")













def action():
	for path in _.switches.values('File'):
		print_file_lines(path, encoding='utf-8', errors='replace', chunk_size=1024 * 1024)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)