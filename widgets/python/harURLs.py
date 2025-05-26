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
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'SaveVideo', '-save', 'file.mp4' )
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


def save_binary_to_file(binary_data, output_file_path):
    with open(output_file_path, 'wb') as f:
        f.write(binary_data)



import base64

def save_base64_as_file(encoded_string, output_file_path):
    """
    Decode a base64 encoded string and save it as a file.
    
    :param encoded_string: Base64 encoded string.
    :param output_file_path: Path for the output file.
    """
    decoded_bytes = base64.b64decode(encoded_string)

    with open(output_file_path, 'wb') as f:
        f.write(decoded_bytes)


videos=[]

def extract_urls(data, key="url"):
	global videos
	urls = []

	if isinstance(data, list):
		for item in data:
			urls.extend(extract_urls(item, key))

	elif isinstance(data, dict):
		
		# if 'mimeType' in data:
			# print(data)
		if _.switches.isActive('SaveVideo'):
			if 'mimeType' in data and data['mimeType'] == 'video/mp4' and 'text' in data:
				# print(__.lasturl,data.keys())
				videos.append({ 'len': len(data['text']), 'text': data['text'], 'url': __.lasturl })
		else:
			for k, v in data.items():
				if k == key:
					urls.append(v)
		for k, v in data.items():
			if k == key:
				__.lasturl=v
			urls.extend(extract_urls(v, key))


	return urls

def main():
	global videos
	spent=[]
	cnt=0
	# print(_.pp())
	for path in _.pp():
		if __.os.path.isfile(path):
			_.pr(path,c='green')
		urls = extract_urls(_.getTable2(path))
		for url in urls:
			if not url in spent:
				spent.append(url)
				if _.showLine(url):
					cnt+=1
					_.cr(url)
	if cnt and not _.switches.isActive('Clean'): _.pr('',_.addComma(cnt),c='yellow')
	if videos:
		video=''
		vids={}
		for v in videos:
			if not v['url'] in vids:
				vids[ v['url'] ] = base64.b64decode(v['text'])
			else:
				vids[ v['url'] ] += base64.b64decode(v['text'])
				# save_binary_to_file(base64.b64decode(v['text']),_.switches.values('SaveVideo')[0])
		VIDs=[]
		for k in vids:
			VIDs.append({ 'url': k, 'file': vids[k], 'size': len(vids[k]) })
		VIDs=_.sort(VIDs,'size')
		file=None
		for fi in VIDs:
			# file=fi
			_.cr(fi['url'])
			# webbrowser.open(fi['url'], new=2)
		# save_binary_to_file(file['file'],_.switches.values('SaveVideo')[0])


def action():
	main()

import webbrowser

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

