import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');
import os
def sw():
	_.switches.register( 'Status', '-is','', isRequired=False )
	_.switches.register( 'Compress', '-co,-do,-en','', isRequired=False )
	_.switches.register( 'Decompress', '-de,-un','', isRequired=False )
	_.switches.register( 'Compression', '--c','gzip zip bz2', isRequired=False )
	_.switches.register( 'LocalFunctions', '-lf','', isRequired=False )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'DestinationFile', '-d,-dest,-destination','data.json', isRequired=False )
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
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	pass
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start





def compress_zip(original_file_path, compressed_file_path):
	if _.IS(original_file_path,'50 4B 03 04 14'):
		print('zip already compressed')
		return False
	from zipfile import ZipFile
	try:
		with ZipFile(compressed_file_path, 'w') as zipf:
			zipf.write(original_file_path, arcname=original_file_path.split("/")[-1])
		print(f"Compressed zip {compressed_file_path}")
	except:
		return 'Error'

def decompress_zip(compressed_file_path, destination=None):
	if destination is None:
		destination = __.path(compressed_file_path,fo=True)
		# destination = os.path.splitext(compressed_file_path)[0]
	if not _.IS(compressed_file_path,'50 4B 03 04 14'):
		print('zip decompressed')
		return False
	import os
	from zipfile import ZipFile
	
	try:
		with ZipFile(compressed_file_path, 'r') as zipf:
			# List of all files and directories in the zip file
			zip_contents = zipf.namelist()
			
			# Destination handling
			if os.path.isdir(destination):
				#_.pr(11,c='cyan')
				# If destination is a directory, extract files into this directory
				extract_path = destination
			elif len(zip_contents) == 1:
				#_.pr(22,c='cyan')
				# If there's only one file in the zip and destination is not a directory, use the destination as the filename
				extract_path = os.path.dirname(destination)
				destination_filename = destination
			else:
				#_.pr(33,c='cyan')
				# If there are multiple files and destination is specified as a filename, use the directory of the destination
				extract_path = os.path.dirname(destination)
			
			# Extract files
			for file in zip_contents:
				# Extract each file
				file_path = zipf.extract(file, extract_path)
				# If there's only one file and a specific destination filename is provided, rename it
				if len(zip_contents) == 1 and not os.path.isdir(destination):
					#_.pr(44,c='cyan')
					os.rename(file_path, destination_filename)
					os.removedirs(os.path.dirname(file_path))
				else:
					#_.pr(55,c='cyan')
					# Move file to the correct directory if it was nested
					correct_path = os.path.join(extract_path, os.path.basename(file_path))
					if file_path != correct_path:
						#_.pr(66,c='cyan')
						os.rename(file_path, correct_path)
						# Remove nested directories if they were created
						os.removedirs(os.path.dirname(file_path))
					
		return 'Decompressed'
	except Exception as e:
		return f'Error: {str(e)}'



def compress_bz2(original_file_path, compressed_file_path):
	if _.IS(original_file_path,'42 5A 68 39 31'):
		print('bz2 already compressed')
		return False
	import bz2
	import shutil
	try:
		with open(original_file_path, 'rb') as original_file:
			with bz2.open(compressed_file_path, 'wb') as compressed_file:
				shutil.copyfileobj(original_file, compressed_file)
		print(f"Compressed bz2 {compressed_file_path}")
	except:
		return 'Error'

def decompress_bz2(compressed_file_path, decompressed_file_path):
	if not _.IS(compressed_file_path,'42 5A 68 39 31'):
		print('bz2 decompressed')
		return False
	import bz2
	import shutil
	try:
		with bz2.open(compressed_file_path, 'rb') as compressed_file:
			with open(decompressed_file_path, 'wb') as decompressed_file:
				shutil.copyfileobj(compressed_file, decompressed_file)
		print(f"Decompressed bz2 {decompressed_file_path}")
	except:
		return 'Error'





def compress2(original_file_path, compressed_file_path):
	import gzip
	import shutil
	try:
		if _.IS(original_file_path,'gzip'):
			shutil.copyfile(original_file_path, compressed_file_path)
			return 'Skipped'
		with open(original_file_path, 'rb') as original_file:
			with gzip.open(compressed_file_path, 'wb') as compressed_file:
				shutil.copyfileobj(original_file, compressed_file)
		print(f"Compressed gzip {compressed_file_path}")
	except:
		return 'Error'

def decompress2(compressed_file_path, decompressed_file_path):
	import gzip
	import shutil
	try:
		if not _.IS(compressed_file_path,'gzip'):
			shutil.copyfile(compressed_file_path, decompressed_file_path)
			return 'Skipped'
		with gzip.open(compressed_file_path, 'rb') as compressed_file:
			with open(decompressed_file_path, 'wb') as decompressed_file:
				shutil.copyfileobj(compressed_file, decompressed_file)
		print(f"Decompressed gzip {decompressed_file_path}")
	except:
		return 'Error'

def compress(path):
	import gzip
	import shutil
	if _.IS(path,'gzip'): return False
	path = __.path(path)
	compressed_file_path = path
	original_file_path = path+'_temp'
	os.rename(path, original_file_path)
	with open(original_file_path, 'rb') as original_file:
		with gzip.open(compressed_file_path, 'wb') as compressed_file:
			shutil.copyfileobj(original_file, compressed_file)
	print(f"Compressed gzip {path}")
	os.unlink(original_file_path)

def decompress(path):
	import gzip
	import shutil
	if not _.IS(path,'gzip'): return False
	path = __.path(path)
	decompressed_file_path = path
	compressed_file_path = path+'_temp'
	os.rename(path, compressed_file_path)
	with gzip.open(compressed_file_path, 'rb') as compressed_file:
		with open(decompressed_file_path, 'wb') as decompressed_file:
			shutil.copyfileobj(compressed_file, decompressed_file)
	print(f"Decompressed gzip {path}")
	os.unlink(compressed_file_path)
def BYTES(path): os.stat(  path  ).st_size




import os

def action():
	if _.switches.isActive('Files'):
		paths = _.switches.values('Files')
	else:
		paths = _.isData()
	for path in paths:
		if _.switches.isActive('Decompress'):
			if not _.switches.isActive('Compression'):
				try:
					if _.switches.isActive('DestinationFile'):
						if _.IS(path,'42 5A 68 39 31'):
							decompress_bz2(path, _.switches.values('DestinationFile')[0])
						elif _.IS(path,'50 4B 03 04 14'):
							decompress_zip(path, _.switches.values('DestinationFile')[0])
						elif _.IS(path,'gzip'):
							decompress2(path, _.switches.values('DestinationFile')[0])
						# return None
					elif not _.switches.isActive('DestinationFile'):
						# path = __.path(path)
						path2 = path+'_temp'
						ran = False
						if _.IS(path,'42 5A 68 39 31'):
							ran = True
							os.rename(path, path2)
							decompress_bz2(path2, path)
						elif _.IS(path,'50 4B 03 04 14'):
							# ran = True
							# os.rename(path, path2)
							decompress_zip(path)
						elif _.IS(path,'gzip'):
							ran = True
							os.rename(path, path2)
							decompress2(path2, path)
						if ran:
							os.unlink(path2)
						# return None
				except:
					if not os.path.isfile(path) and os.path.isfile(path+'_temp'):
						print('renaming')
						os.rename(path+'_temp', path)
					_.pr('Error decompressing', path)
		if _.switches.isActive('Compression'):
			compression = _.switches.value('Compression')
		else:
			compression = 'gzip'
		if False:
			pass
		elif compression == 'bz2':
			if _.switches.isActive('DestinationFile'):
				dest = _.switches.values('DestinationFile')[0]
				if _.switches.isActive('Compress'):
					compress_bz2(path, dest)
				elif _.switches.isActive('Decompress'):
					decompress_bz2(path, dest)
				else:
					if _.IS(path, '42 5A 68 39 31'):
						decompress_bz2(path, dest)
					else:
						compress_bz2(path, dest)
				# return None
			elif not _.switches.isActive('DestinationFile'):
				import shutil
				path = __.path(path)
				path2 = path+'_temp'
				os.rename(path, path2)
				if _.switches.isActive('Compress'):
					compress_bz2(path2, path)
				elif _.switches.isActive('Decompress'):
					decompress_bz2(path2, path)
				else:
					if _.IS(path, '42 5A 68 39 31'):
						decompress_bz2(path2, path)
					else:
						compress_bz2(path2, path)
				os.unlink(path2)
				# return None
		elif compression == 'zip':
			if _.switches.isActive('DestinationFile'):
				dest = _.switches.values('DestinationFile')[0]
				if _.switches.isActive('Compress'):
					compress_zip(path, dest)
				elif _.switches.isActive('Decompress'):
					decompress_zip(path, dest)
				else:
					if _.IS(path, '50 4B 03 04 14'):
						decompress_zip(path, dest)
					else:
						compress_zip(path, dest)
				# return None
			elif not _.switches.isActive('DestinationFile'):
				import shutil
				path = __.path(path)
				path2 = path+'_temp'
				os.rename(path, path2)
				if _.switches.isActive('Compress'):
					compress_zip(path2, path)
				elif _.switches.isActive('Decompress'):
					decompress_zip(path2, path)
				else:
					if _.IS(path, '50 4B 03 04 14'):
						decompress_zip(path2, path)
					else:
						compress_zip(path2, path)
				os.unlink(path2)
				# return None
		elif compression == 'gzip':
			if _.switches.isActive('DestinationFile'):
				dest = _.switches.values('DestinationFile')[0]
				if _.switches.isActive('Compress'):
					if _.switches.isActive('LocalFunctions'):
						compress2(path, dest)
					else:
						_.compress2(path, dest)
				elif _.switches.isActive('Decompress'):
					if _.switches.isActive('LocalFunctions'):
						decompress2(path, dest)
					else:
						_.decompress2(path, dest)
				else:
					if _.IS(path, 'gzip'):
						if _.switches.isActive('LocalFunctions'):
							decompress2(path, dest)
						else:
							_.decompress2(path, dest)
					else:
						if _.switches.isActive('LocalFunctions'):
							compress2(path, dest)
						else:
							_.compress2(path, dest)

				# return None

			if _.switches.isActive('Status'):
				if len(_.isData()) == 1:
					multi = False
				else:
					multi = True
				for path in _.isData():
					path = path.strip()
					if not os.path.isfile(path): continue
					if multi:
						_.pr(path, c='cyan')
					if _.IS(path, 'gzip'):
						_.pr('is gzip compressed:', path, c='green')
					elif _.IS(path, '50 4B 03 04 14'):
						_.pr('is zip compressed:', path, c='green')
					elif _.IS(path, '42 5A 68 39 31'):
						_.pr('is bz2 compressed:', path, c='green')
					else:
						_.pr()
						_.pr('Notice: --> not one of the compression formats that this app uses', c='yellow')
						_header = _.regImp(__.appReg, 'fileHeader')
						_header.switch('Files', path)
						_header.action()
						_.pr()
				# return None
			if len(_.isData()) == 1 and not _.switches.isActive('Compress') and not _.switches.isActive('Decompress'):
				for path in _.isData():
					path = path.strip()
					if not os.path.isfile(path): continue
					if _.IS(path, 'gzip'):
						_.decompress(path)
					else:
						_.compress(path)

			elif _.switches.isActive('Compress'):
				for path in _.isData():
					path = path.strip()
					if not os.path.isfile(path): continue
					if _.switches.isActive('LocalFunctions'):
						compress(path)
					else:
						_.compress(path)
			elif _.switches.isActive('Decompress'):
				for path in _.isData():
					path = path.strip()
					if not os.path.isfile(path): continue
					# _.decompress(path)
					if _.switches.isActive('LocalFunctions'):
						decompress(path)
					else:
						_.decompress(path)
			else:
				_.e('action not specified', '-en or -de')


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);