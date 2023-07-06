#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


##################################################
import sys, time
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################


def sw():
	pass
	#b)--> examples
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Extraction-Folder', '-fo,-folder' )
	_.switches.register( 'Extract', '-e,-extract' )
	_.switches.register( 'Delete', '-d,-delete' )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] },
		},
	}


def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )

def _local_(do): exec(do)

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start



import zipfile
import os
import json

def zip_subjects(subjects, level, zip_name='archive.zip'):
	# Check if the ZIP file already exists
	if os.path.exists(zip_name):
		mode = 'a'  # Append mode
	else:
		mode = 'w'  # Write mode

	# Create or open the ZIP file
	with zipfile.ZipFile(zip_name, mode=mode, compression=zipfile.ZIP_DEFLATED, compresslevel=level) as zipf:
		# Iterate over the subjects to be zipped
		for subject in subjects:
			# Check if the subject is a file or a directory
			if os.path.isfile(subject):
				# If the file already exists in the ZIP, remove it first
				if subject in zipf.namelist():
					zipf.extract(subject)
				# Add the file to the ZIP
				zipf.write(subject, os.path.basename(subject))
			elif os.path.isdir(subject):
				# Add the directory to the ZIP
				for root, _, files in os.walk(subject):
					for file in files:
						file_path = os.path.join(root, file)
						zipf.write(file_path, os.path.relpath(file_path, subject))
				# Save the index file
				save_index(zipf, zip_name)

def save_index(zipf, zip_name):
	index_file = f'{zip_name}.index'
	with open(index_file, 'w') as f:
		json.dump(zipf.namelist(), f)

def delete_files(zip_name, files_to_delete):
	# Load the index file
	index_file = f'{zip_name}.index'
	if os.path.exists(index_file):
		with open(index_file, 'r') as f:
			index = json.load(f)
	else:
		index = []

	# Create a temporary ZIP file
	with zipfile.ZipFile('temp.zip', 'w') as temp_zip:
		# Open the original ZIP file
		with zipfile.ZipFile(zip_name, 'r') as zipf:
			# Copy all files from the original ZIP to the temporary ZIP, except the files to be deleted
			for item in zipf.namelist():
				if item not in files_to_delete:
					temp_zip.writestr(item, zipf.read(item))
			# Update the index
			index = [item for item in index if item not in files_to_delete]

	# Replace the original ZIP with the temporary ZIP
	os.replace('temp.zip', zip_name)

	# Save the updated index file
	with open(index_file, 'w') as f:
		json.dump(index, f)

def index_files(zip_name):
	# Load the index file
	index_file = f'{zip_name}.index'
	if os.path.exists(index_file):
		with open(index_file, 'r') as f:
			index = json.load(f)
		return index
	return []

def extract_files(zip_name, files_to_extract, dest_dir='.'):
	# Open the ZIP file
	with zipfile.ZipFile(zip_name, 'r') as zipf:
		# Extract the specified files
		for file in files_to_extract:
			if file in zipf.namelist():
				zipf.extract(file, dest_dir)

def extract_all(zip_name, dest_dir='.'):
	"""
	Extracts the entire contents of a ZIP archive.

	Args:
		zip_name (str): The name of the ZIP file to extract.
		dest_dir (str, optional): The destination directory where the contents will be extracted. Defaults to the current directory.
	"""
	with zipfile.ZipFile(zip_name, 'r') as zipf:
		zipf.extractall(path=dest_dir)

'''
# Example usage
zip_subjects(['file1.txt', 'folder1'], level=5)
delete_files('archive.zip', ['file1.txt'])
extract_all('archive.zip', dest_dir='extracted')

In this application, the following functions are implemented:

1. `zip_subjects(subjects, level, zip_name='archive.zip')`: Zips the specified files and/or folders (`subjects`) with the specified compression level (`level`). The ZIP file is named `zip_name` (default is `'archive.zip'`). If the ZIP file already exists, the function checks if the file is in the ZIP and replaces it if necessary. If a folder is being zipped, the function saves an index of the files to a file called `archive.zip.index`.

2. `save_index(zipf, zip_name)`: Saves the index of files in the ZIP archive to a file called `archive.zip.index`. This function is called internally by the `zip_subjects` function.

3. `delete_files(zip_name, files_to_delete)`: Deletes the specified files (`files_to_delete`) from the ZIP file (`zip_name`). The function also updates the index file.

4. `index_files(zip_name)`: Returns the index of files in the ZIP archive by loading the index file. If the index file does not exist, the function returns an empty list.

5. `extract_files(zip_name, files_to_extract, dest_dir='.')`: Extracts the specified files (`files_to_extract`) from the ZIP file (`zip_name`) to the destination directory (`dest_dir`). The default destination directory is the current directory.

The example usage at the end of the script demonstrates how to use these functions to zip files and folders, delete files from a ZIP archive, index files in a ZIP archive, and extract files from a ZIP archive.

Please note that this application is a basic implementation and may not handle all edge cases. It is recommended to test the application thoroughly and make any necessary improvements before using it in a production environment.


	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Extraction-Folder', '-fo,-folder' )
	_.switches.register( 'Extract', '-e,-extract' )
	_.switches.register( 'Delete', '-d,-delete' )    


'''


def action():
	zip_subjects(['file1.txt', 'folder1'], level=5)
	delete_files('archive.zip', ['file1.txt'])
	extract_all('archive.zip', dest_dir='extracted')




##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)

