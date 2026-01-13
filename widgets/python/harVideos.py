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
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

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
# columns used for
# 	- abbreviation in switches
#		- ex: -column n s
#			- instead of: -column name size
#		- ex: -sort n
#		- ex: -group n
# 	- sort is used for things like size sort by bytes
# 	- responsiveness to terminal width
# 		- order is important
# 		- most important on top
		
		# this is used for personal usage to programmatically generate columns
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

import simplejson as json

# def extract_ts_data_from_har(har_file_path):
#     with open(har_file_path, 'r', encoding='utf-8') as file:
#         har_data = json.load(file)

#     ts_data = []

#     for entry in har_data['log']['entries']:
#         url = entry['request']['url']
#         if url.endswith('.ts'):  # assuming the chunk files end with .ts
#             response = entry['response']['content']['text']
#             ts_data.append(response)

#     return ts_data

# def save_video_from_chunks(ts_data_list, output_file):
#     with open(output_file, 'wb') as out_file:
#         for data in ts_data_list:
#             out_file.write(data)

# # Assuming HAR file has raw binary data saved as base64
# def decode_base64(data):
#     return base64.b64decode(data)

# def action():
# 	har_path = _.pp()[0]
# 	ts_data_list = [decode_base64(data) for data in extract_ts_data_from_har(har_path)]
# 	save_video_from_chunks(ts_data_list, 'output_video.ts')


# import json
# import os
# import requests
# import hashlib

# def md5_hash(text):
#     return hashlib.md5(text.encode('utf-8')).hexdigest()

# def save_video_from_har(har_path):
#     with open(har_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         entries = data['log']['entries']
		
#         for entry in entries:
#             mime_type = entry['response']['content']['mimeType']
#             url = entry['request']['url']
#             if mime_type == 'video/mp4':
#                 print(f"Downloading {url}")
#                 try:
#                     response = requests.get(url, stream=True)
#                     if response.status_code == 200:
#                         filename = f"{har_path}--{md5_hash(url)}.ts"
#                         with open(filename, 'wb') as video_file:
#                             for chunk in response.iter_content(chunk_size=8192):
#                                 video_file.write(chunk)
						
#                         # Convert to mp4 using ffmpeg
#                         output_filename = filename.replace('.ts', '.mp4')
#                         command = f"ffmpeg -i {filename} {output_filename}"
#                         try:
#                             os.system(command)
#                             print(f"Converted {filename} to {output_filename}")
#                         except Exception as e:
#                             print(f"Error converting {filename} to mp4: {e}")
#                 except Exception as e:
#                     print(f"Error downloading {url}: {e}")




# def action():
#     har_file_path = _.pp()[0]
#     save_video_from_har(har_file_path)

import json
import hashlib
import requests
import os

def extract_mp4_urls_from_har(har_file_path):
	with open(har_file_path, 'r', encoding='utf-8') as file:
		har_data = json.load(file)

	video_urls = []

	for entry in har_data['log']['entries']:
		mime_type = entry['response']['content']['mimeType']
		if mime_type == 'video/mp4':
			video_urls.append(entry['request']['url'])

	return video_urls

def compute_md5(text):
	return hashlib.md5(text.encode('utf-8')).hexdigest()

# def stream_download_video(url, save_path):
#     try:
#         print(f"Starting download from {url}")
#         response = requests.get(url, stream=True)
#         response.raise_for_status()

#         with open(save_path, 'wb') as file:
#             for chunk in response.iter_content(chunk_size=8192):
#                 file.write(chunk)
#         print(f"Saved video to {save_path}")
#     except Exception as e:
#         print(f"Error downloading {url}. Error: {e}")
##########################################################################
# def download_video(url, save_path):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()

#         with open(save_path, 'wb') as file:
#             file.write(response.content)
#         print(f"Saved video to {save_path}")
#     except Exception as e:
#         print(f"Error downloading {url}. Error: {e}")


def convert_to_mp4(input_path, output_path):
	try:
		# os.system(f'ffmpeg -i {input_path} -c:v copy -c:a copy {output_path}')
		os.system(f'ffmpeg -err_detect ignore_err -i {input_path} -c copy {output_path}')
		print(f"Converted to: {output_path}")
	except Exception as e:
		print(f"Error converting {input_path} to mp4. Error: {e}")

# # def convert_to_mp4(input_path, output_path):
# #     try:
# #         os.system(f'ffmpeg -i {input_path} -c:v copy -c:a copy {output_path}')
# #         print(f"Converted to: {output_path}")
# #     except Exception as e:
# #         print(f"Error converting {input_path} to mp4. Error: {e}")

# def action():
#     har_path = _.pp()[0]
#     video_urls = extract_mp4_urls_from_har(har_path)

#     if not video_urls:
#         print("No 'video/mp4' MIME type found in the provided HAR file.")
#     else:
#         print(f"Found {len(video_urls)} potential .mp4 URLs.")
#         for url in video_urls:
#             file_name = f"{har_path}--{compute_md5(url)}.mp4"
#             download_video(url, file_name)
#             convert_to_mp4(file_name, file_name.replace('.mp4', '_converted.mp4'))
##########################################################################################################
import youtube_dl
import os
import hashlib
import json

def md5(text):
	return hashlib.md5(text.encode('utf-8')).hexdigest()

def convert_to_mp42(input_path, output_path):
	try:
		os.system(f'ffmpeg -i {input_path} {output_path}')
		print(f"Converted to: {output_path}")
	except Exception as e:
		print(f"Error converting {input_path} to mp4. Error: {e}")

def download_and_convert_from_har(har_path):
	with open(har_path, 'r', encoding='utf-8') as file:
		har_data = json.load(file)

	for entry in har_data['log']['entries']:
		url = entry['request']['url']
		mime_type = entry['response']['content']['mimeType']

		if 'video/mp4' in mime_type:
			try:
				ydl_opts = {
					'format': 'best',
					'outtmpl': f"{har_path}--{md5(url)}.mp4",
					'postprocessors': [{
						'key': 'FFmpegVideoConvertor',
						'preferedformat': 'mp4'
					}],
				}

				with youtube_dl.YoutubeDL(ydl_opts) as ydl:
					ydl.download([url])
			except Exception as e:
				print(f"Error downloading {url}. Error: {e}")

def action():
	download_and_convert_from_har(_.pp()[0])


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