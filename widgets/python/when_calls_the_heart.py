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
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

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
						_.hp('cat when_calls_the_heart--transcripts.md | p when_calls_the_heart'),
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

import requests
import os
from threading import Thread, Semaphore
from bs4 import BeautifulSoup
import re

MAX_THREADS = 10
semaphore = Semaphore(MAX_THREADS)

class DownloaderThread(Thread):
	def __init__(self, url):
		super().__init__()
		self.url = url

	def run(self):
		try:
			response = requests.get(self.url)
			if response.status_code == 200:
				soup = BeautifulSoup(response.content, 'html.parser')
				h2_tags = soup.find_all('h2')
				if h2_tags:
					# Extract the topic title from the first <h2> tag
					topic_title = h2_tags[0].text.strip()
					# Sanitize the filename by removing invalid characters
					sanitized_title = re.sub(r'[<>:"/\\|?*]', '', topic_title)

					# Save the response content as .topic-title.txt
					file_path = f"{sanitized_title}.txt"
					with open(file_path, "wb") as file:
						file.write(response.content)
					print(f"File saved as: {file_path}")

					# Save the response content body as .postbody
					body_path = f"{sanitized_title}.postbody"
					with open(body_path, "w", encoding='utf-8') as body_file:
						body_text = soup.find(class_="postbody").get_text(separator="\n")
						body_file.write(body_text)
					print(f"Body content saved as: {body_path}\n")
				else:
					print(f"No <h2> tag found in URL: {self.url}\n")
			else:
				print(f"Failed to download URL: {self.url}\n")
		except requests.exceptions.RequestException as e:
			print(f"An error occurred while downloading URL: {self.url}\nError: {e}\n")
		finally:
			semaphore.release()

def download_urls(urls):
	for url in urls:
		semaphore.acquire()
		downloader_thread = DownloaderThread(url)
		downloader_thread.start()




def action():
	download_urls(_.pp())


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

'''
https://transcripts.foreverdreaming.org/viewtopic.php?p=146264&sid=86ef9dc9f9fb6be57917accea46a3204#p146264
https://transcripts.foreverdreaming.org/viewtopic.php?p=146264&sid=86ef9dc9f9fb6be57917accea46a3204#p146264
https://transcripts.foreverdreaming.org/viewtopic.php?p=187459&sid=86ef9dc9f9fb6be57917accea46a3204#p187459
https://transcripts.foreverdreaming.org/viewtopic.php?p=187459&sid=86ef9dc9f9fb6be57917accea46a3204#p187459
https://transcripts.foreverdreaming.org/viewtopic.php?p=187002&sid=86ef9dc9f9fb6be57917accea46a3204#p187002
https://transcripts.foreverdreaming.org/viewtopic.php?p=187002&sid=86ef9dc9f9fb6be57917accea46a3204#p187002
https://transcripts.foreverdreaming.org/viewtopic.php?p=186578&sid=86ef9dc9f9fb6be57917accea46a3204#p186578
https://transcripts.foreverdreaming.org/viewtopic.php?p=186578&sid=86ef9dc9f9fb6be57917accea46a3204#p186578
https://transcripts.foreverdreaming.org/viewtopic.php?p=186147&sid=86ef9dc9f9fb6be57917accea46a3204#p186147
https://transcripts.foreverdreaming.org/viewtopic.php?p=186147&sid=86ef9dc9f9fb6be57917accea46a3204#p186147
https://transcripts.foreverdreaming.org/viewtopic.php?p=185015&sid=86ef9dc9f9fb6be57917accea46a3204#p185015
https://transcripts.foreverdreaming.org/viewtopic.php?p=185015&sid=86ef9dc9f9fb6be57917accea46a3204#p185015
https://transcripts.foreverdreaming.org/viewtopic.php?p=183743&sid=86ef9dc9f9fb6be57917accea46a3204#p183743
https://transcripts.foreverdreaming.org/viewtopic.php?p=183743&sid=86ef9dc9f9fb6be57917accea46a3204#p183743
https://transcripts.foreverdreaming.org/viewtopic.php?p=183737&sid=86ef9dc9f9fb6be57917accea46a3204#p183737
https://transcripts.foreverdreaming.org/viewtopic.php?p=183737&sid=86ef9dc9f9fb6be57917accea46a3204#p183737
https://transcripts.foreverdreaming.org/viewtopic.php?p=183161&sid=86ef9dc9f9fb6be57917accea46a3204#p183161
https://transcripts.foreverdreaming.org/viewtopic.php?p=183161&sid=86ef9dc9f9fb6be57917accea46a3204#p183161
https://transcripts.foreverdreaming.org/viewtopic.php?p=183160&sid=86ef9dc9f9fb6be57917accea46a3204#p183160
https://transcripts.foreverdreaming.org/viewtopic.php?p=183160&sid=86ef9dc9f9fb6be57917accea46a3204#p183160
https://transcripts.foreverdreaming.org/viewtopic.php?p=182035&sid=86ef9dc9f9fb6be57917accea46a3204#p182035
https://transcripts.foreverdreaming.org/viewtopic.php?p=182035&sid=86ef9dc9f9fb6be57917accea46a3204#p182035
https://transcripts.foreverdreaming.org/viewtopic.php?p=181146&sid=86ef9dc9f9fb6be57917accea46a3204#p181146
https://transcripts.foreverdreaming.org/viewtopic.php?p=181146&sid=86ef9dc9f9fb6be57917accea46a3204#p181146
https://transcripts.foreverdreaming.org/viewtopic.php?p=180537&sid=86ef9dc9f9fb6be57917accea46a3204#p180537
https://transcripts.foreverdreaming.org/viewtopic.php?p=180537&sid=86ef9dc9f9fb6be57917accea46a3204#p180537
https://transcripts.foreverdreaming.org/viewtopic.php?p=171866&sid=86ef9dc9f9fb6be57917accea46a3204#p171866
https://transcripts.foreverdreaming.org/viewtopic.php?p=171866&sid=86ef9dc9f9fb6be57917accea46a3204#p171866
https://transcripts.foreverdreaming.org/viewtopic.php?p=171865&sid=86ef9dc9f9fb6be57917accea46a3204#p171865
https://transcripts.foreverdreaming.org/viewtopic.php?p=171865&sid=86ef9dc9f9fb6be57917accea46a3204#p171865
https://transcripts.foreverdreaming.org/viewtopic.php?p=171864&sid=86ef9dc9f9fb6be57917accea46a3204#p171864
https://transcripts.foreverdreaming.org/viewtopic.php?p=171864&sid=86ef9dc9f9fb6be57917accea46a3204#p171864
https://transcripts.foreverdreaming.org/viewtopic.php?p=171863&sid=86ef9dc9f9fb6be57917accea46a3204#p171863
https://transcripts.foreverdreaming.org/viewtopic.php?p=171863&sid=86ef9dc9f9fb6be57917accea46a3204#p171863
https://transcripts.foreverdreaming.org/viewtopic.php?p=171862&sid=86ef9dc9f9fb6be57917accea46a3204#p171862
https://transcripts.foreverdreaming.org/viewtopic.php?p=171862&sid=86ef9dc9f9fb6be57917accea46a3204#p171862
https://transcripts.foreverdreaming.org/viewtopic.php?p=171763&sid=86ef9dc9f9fb6be57917accea46a3204#p171763
https://transcripts.foreverdreaming.org/viewtopic.php?p=171763&sid=86ef9dc9f9fb6be57917accea46a3204#p171763
https://transcripts.foreverdreaming.org/viewtopic.php?p=171762&sid=86ef9dc9f9fb6be57917accea46a3204#p171762
https://transcripts.foreverdreaming.org/viewtopic.php?p=171762&sid=86ef9dc9f9fb6be57917accea46a3204#p171762
https://transcripts.foreverdreaming.org/viewtopic.php?p=171761&sid=86ef9dc9f9fb6be57917accea46a3204#p171761
https://transcripts.foreverdreaming.org/viewtopic.php?p=171761&sid=86ef9dc9f9fb6be57917accea46a3204#p171761
https://transcripts.foreverdreaming.org/viewtopic.php?p=171760&sid=86ef9dc9f9fb6be57917accea46a3204#p171760
https://transcripts.foreverdreaming.org/viewtopic.php?p=171760&sid=86ef9dc9f9fb6be57917accea46a3204#p171760
https://transcripts.foreverdreaming.org/viewtopic.php?p=171759&sid=86ef9dc9f9fb6be57917accea46a3204#p171759
https://transcripts.foreverdreaming.org/viewtopic.php?p=171759&sid=86ef9dc9f9fb6be57917accea46a3204#p171759
https://transcripts.foreverdreaming.org/viewtopic.php?p=171758&sid=86ef9dc9f9fb6be57917accea46a3204#p171758
https://transcripts.foreverdreaming.org/viewtopic.php?p=171758&sid=86ef9dc9f9fb6be57917accea46a3204#p171758
https://transcripts.foreverdreaming.org/viewtopic.php?p=171757&sid=86ef9dc9f9fb6be57917accea46a3204#p171757
https://transcripts.foreverdreaming.org/viewtopic.php?p=171757&sid=86ef9dc9f9fb6be57917accea46a3204#p171757
https://transcripts.foreverdreaming.org/viewtopic.php?p=171756&sid=86ef9dc9f9fb6be57917accea46a3204#p171756
https://transcripts.foreverdreaming.org/viewtopic.php?p=171756&sid=86ef9dc9f9fb6be57917accea46a3204#p171756
https://transcripts.foreverdreaming.org/viewtopic.php?p=171755&sid=86ef9dc9f9fb6be57917accea46a3204#p171755
https://transcripts.foreverdreaming.org/viewtopic.php?p=171755&sid=86ef9dc9f9fb6be57917accea46a3204#p171755
https://transcripts.foreverdreaming.org/viewtopic.php?p=171754&sid=86ef9dc9f9fb6be57917accea46a3204#p171754
https://transcripts.foreverdreaming.org/viewtopic.php?p=171754&sid=86ef9dc9f9fb6be57917accea46a3204#p171754
https://transcripts.foreverdreaming.org/viewtopic.php?p=171753&sid=86ef9dc9f9fb6be57917accea46a3204#p171753
https://transcripts.foreverdreaming.org/viewtopic.php?p=171753&sid=86ef9dc9f9fb6be57917accea46a3204#p171753
https://transcripts.foreverdreaming.org/viewtopic.php?p=171752&sid=86ef9dc9f9fb6be57917accea46a3204#p171752
https://transcripts.foreverdreaming.org/viewtopic.php?p=171752&sid=86ef9dc9f9fb6be57917accea46a3204#p171752
https://transcripts.foreverdreaming.org/viewtopic.php?p=171751&sid=86ef9dc9f9fb6be57917accea46a3204#p171751
https://transcripts.foreverdreaming.org/viewtopic.php?p=171751&sid=86ef9dc9f9fb6be57917accea46a3204#p171751
https://transcripts.foreverdreaming.org/viewtopic.php?p=171750&sid=86ef9dc9f9fb6be57917accea46a3204#p171750
https://transcripts.foreverdreaming.org/viewtopic.php?p=171750&sid=86ef9dc9f9fb6be57917accea46a3204#p171750
https://transcripts.foreverdreaming.org/viewtopic.php?p=171749&sid=86ef9dc9f9fb6be57917accea46a3204#p171749
https://transcripts.foreverdreaming.org/viewtopic.php?p=171749&sid=86ef9dc9f9fb6be57917accea46a3204#p171749
https://transcripts.foreverdreaming.org/viewtopic.php?p=171748&sid=86ef9dc9f9fb6be57917accea46a3204#p171748
https://transcripts.foreverdreaming.org/viewtopic.php?p=171748&sid=86ef9dc9f9fb6be57917accea46a3204#p171748
https://transcripts.foreverdreaming.org/viewtopic.php?p=171747&sid=86ef9dc9f9fb6be57917accea46a3204#p171747
https://transcripts.foreverdreaming.org/viewtopic.php?p=171747&sid=86ef9dc9f9fb6be57917accea46a3204#p171747
https://transcripts.foreverdreaming.org/viewtopic.php?p=171746&sid=86ef9dc9f9fb6be57917accea46a3204#p171746
https://transcripts.foreverdreaming.org/viewtopic.php?p=171746&sid=86ef9dc9f9fb6be57917accea46a3204#p171746
https://transcripts.foreverdreaming.org/viewtopic.php?p=171745&sid=86ef9dc9f9fb6be57917accea46a3204#p171745
https://transcripts.foreverdreaming.org/viewtopic.php?p=171745&sid=86ef9dc9f9fb6be57917accea46a3204#p171745
https://transcripts.foreverdreaming.org/viewtopic.php?p=171744&sid=86ef9dc9f9fb6be57917accea46a3204#p171744
https://transcripts.foreverdreaming.org/viewtopic.php?p=171744&sid=86ef9dc9f9fb6be57917accea46a3204#p171744
https://transcripts.foreverdreaming.org/viewtopic.php?p=171459&sid=86ef9dc9f9fb6be57917accea46a3204#p171459
https://transcripts.foreverdreaming.org/viewtopic.php?p=171459&sid=86ef9dc9f9fb6be57917accea46a3204#p171459
https://transcripts.foreverdreaming.org/viewtopic.php?p=171458&sid=86ef9dc9f9fb6be57917accea46a3204#p171458
https://transcripts.foreverdreaming.org/viewtopic.php?p=171458&sid=86ef9dc9f9fb6be57917accea46a3204#p171458
https://transcripts.foreverdreaming.org/viewtopic.php?p=171457&sid=86ef9dc9f9fb6be57917accea46a3204#p171457
https://transcripts.foreverdreaming.org/viewtopic.php?p=171457&sid=86ef9dc9f9fb6be57917accea46a3204#p171457
https://transcripts.foreverdreaming.org/viewtopic.php?p=171456&sid=86ef9dc9f9fb6be57917accea46a3204#p171456
https://transcripts.foreverdreaming.org/viewtopic.php?p=171456&sid=86ef9dc9f9fb6be57917accea46a3204#p171456
https://transcripts.foreverdreaming.org/viewtopic.php?p=171455&sid=86ef9dc9f9fb6be57917accea46a3204#p171455
https://transcripts.foreverdreaming.org/viewtopic.php?p=171455&sid=86ef9dc9f9fb6be57917accea46a3204#p171455
https://transcripts.foreverdreaming.org/viewtopic.php?p=171454&sid=86ef9dc9f9fb6be57917accea46a3204#p171454
https://transcripts.foreverdreaming.org/viewtopic.php?p=171454&sid=86ef9dc9f9fb6be57917accea46a3204#p171454
https://transcripts.foreverdreaming.org/viewtopic.php?p=171453&sid=86ef9dc9f9fb6be57917accea46a3204#p171453
https://transcripts.foreverdreaming.org/viewtopic.php?p=171453&sid=86ef9dc9f9fb6be57917accea46a3204#p171453
https://transcripts.foreverdreaming.org/viewtopic.php?p=171452&sid=86ef9dc9f9fb6be57917accea46a3204#p171452
https://transcripts.foreverdreaming.org/viewtopic.php?p=171452&sid=86ef9dc9f9fb6be57917accea46a3204#p171452
https://transcripts.foreverdreaming.org/viewtopic.php?p=171451&sid=86ef9dc9f9fb6be57917accea46a3204#p171451
https://transcripts.foreverdreaming.org/viewtopic.php?p=171451&sid=86ef9dc9f9fb6be57917accea46a3204#p171451
https://transcripts.foreverdreaming.org/viewtopic.php?p=158786&sid=86ef9dc9f9fb6be57917accea46a3204#p158786
https://transcripts.foreverdreaming.org/viewtopic.php?p=158786&sid=86ef9dc9f9fb6be57917accea46a3204#p158786
https://transcripts.foreverdreaming.org/viewtopic.php?p=158675&sid=86ef9dc9f9fb6be57917accea46a3204#p158675
https://transcripts.foreverdreaming.org/viewtopic.php?p=158675&sid=86ef9dc9f9fb6be57917accea46a3204#p158675
https://transcripts.foreverdreaming.org/viewtopic.php?p=158527&sid=86ef9dc9f9fb6be57917accea46a3204#p158527
https://transcripts.foreverdreaming.org/viewtopic.php?p=158527&sid=86ef9dc9f9fb6be57917accea46a3204#p158527
https://transcripts.foreverdreaming.org/viewtopic.php?p=158324&sid=86ef9dc9f9fb6be57917accea46a3204#p158324
https://transcripts.foreverdreaming.org/viewtopic.php?p=158324&sid=86ef9dc9f9fb6be57917accea46a3204#p158324
https://transcripts.foreverdreaming.org/viewtopic.php?p=158160&sid=86ef9dc9f9fb6be57917accea46a3204#p158160
https://transcripts.foreverdreaming.org/viewtopic.php?p=158160&sid=86ef9dc9f9fb6be57917accea46a3204#p158160
https://transcripts.foreverdreaming.org/viewtopic.php?p=158103&sid=86ef9dc9f9fb6be57917accea46a3204#p158103
https://transcripts.foreverdreaming.org/viewtopic.php?p=158103&sid=86ef9dc9f9fb6be57917accea46a3204#p158103
https://transcripts.foreverdreaming.org/viewtopic.php?p=157760&sid=86ef9dc9f9fb6be57917accea46a3204#p157760
https://transcripts.foreverdreaming.org/viewtopic.php?p=157760&sid=86ef9dc9f9fb6be57917accea46a3204#p157760
https://transcripts.foreverdreaming.org/viewtopic.php?p=157631&sid=86ef9dc9f9fb6be57917accea46a3204#p157631
https://transcripts.foreverdreaming.org/viewtopic.php?p=157631&sid=86ef9dc9f9fb6be57917accea46a3204#p157631
https://transcripts.foreverdreaming.org/viewtopic.php?p=157443&sid=86ef9dc9f9fb6be57917accea46a3204#p157443
https://transcripts.foreverdreaming.org/viewtopic.php?p=157443&sid=86ef9dc9f9fb6be57917accea46a3204#p157443
https://transcripts.foreverdreaming.org/viewtopic.php?p=157442&sid=86ef9dc9f9fb6be57917accea46a3204#p157442
https://transcripts.foreverdreaming.org/viewtopic.php?p=157442&sid=86ef9dc9f9fb6be57917accea46a3204#p157442
https://transcripts.foreverdreaming.org/viewtopic.php?p=157441&sid=86ef9dc9f9fb6be57917accea46a3204#p157441
https://transcripts.foreverdreaming.org/viewtopic.php?p=157441&sid=86ef9dc9f9fb6be57917accea46a3204#p157441
https://transcripts.foreverdreaming.org/viewtopic.php?p=157440&sid=86ef9dc9f9fb6be57917accea46a3204#p157440
https://transcripts.foreverdreaming.org/viewtopic.php?p=157440&sid=86ef9dc9f9fb6be57917accea46a3204#p157440
https://transcripts.foreverdreaming.org/viewtopic.php?p=157299&sid=86ef9dc9f9fb6be57917accea46a3204#p157299
https://transcripts.foreverdreaming.org/viewtopic.php?p=157299&sid=86ef9dc9f9fb6be57917accea46a3204#p157299
https://transcripts.foreverdreaming.org/viewtopic.php?p=157298&sid=86ef9dc9f9fb6be57917accea46a3204#p157298
https://transcripts.foreverdreaming.org/viewtopic.php?p=157298&sid=86ef9dc9f9fb6be57917accea46a3204#p157298
https://transcripts.foreverdreaming.org/viewtopic.php?p=157297&sid=86ef9dc9f9fb6be57917accea46a3204#p157297
https://transcripts.foreverdreaming.org/viewtopic.php?p=157297&sid=86ef9dc9f9fb6be57917accea46a3204#p157297
https://transcripts.foreverdreaming.org/viewtopic.php?p=157191&sid=86ef9dc9f9fb6be57917accea46a3204#p157191
https://transcripts.foreverdreaming.org/viewtopic.php?p=157191&sid=86ef9dc9f9fb6be57917accea46a3204#p157191
https://transcripts.foreverdreaming.org/viewtopic.php?p=157190&sid=86ef9dc9f9fb6be57917accea46a3204#p157190
https://transcripts.foreverdreaming.org/viewtopic.php?p=157190&sid=86ef9dc9f9fb6be57917accea46a3204#p157190
https://transcripts.foreverdreaming.org/viewtopic.php?p=157189&sid=86ef9dc9f9fb6be57917accea46a3204#p157189
https://transcripts.foreverdreaming.org/viewtopic.php?p=157189&sid=86ef9dc9f9fb6be57917accea46a3204#p157189
https://transcripts.foreverdreaming.org/viewtopic.php?p=157077&sid=86ef9dc9f9fb6be57917accea46a3204#p157077
https://transcripts.foreverdreaming.org/viewtopic.php?p=157077&sid=86ef9dc9f9fb6be57917accea46a3204#p157077
https://transcripts.foreverdreaming.org/viewtopic.php?p=155423&sid=86ef9dc9f9fb6be57917accea46a3204#p155423
https://transcripts.foreverdreaming.org/viewtopic.php?p=155423&sid=86ef9dc9f9fb6be57917accea46a3204#p155423
https://transcripts.foreverdreaming.org/viewtopic.php?p=145260&sid=86ef9dc9f9fb6be57917accea46a3204#p145260
https://transcripts.foreverdreaming.org/viewtopic.php?p=145260&sid=86ef9dc9f9fb6be57917accea46a3204#p145260
https://transcripts.foreverdreaming.org/viewtopic.php?p=140683&sid=86ef9dc9f9fb6be57917accea46a3204#p140683
https://transcripts.foreverdreaming.org/viewtopic.php?p=140683&sid=86ef9dc9f9fb6be57917accea46a3204#p140683
https://transcripts.foreverdreaming.org/viewtopic.php?p=140526&sid=86ef9dc9f9fb6be57917accea46a3204#p140526
https://transcripts.foreverdreaming.org/viewtopic.php?p=140526&sid=86ef9dc9f9fb6be57917accea46a3204#p140526
https://transcripts.foreverdreaming.org/viewtopic.php?p=140392&sid=86ef9dc9f9fb6be57917accea46a3204#p140392
https://transcripts.foreverdreaming.org/viewtopic.php?p=140392&sid=86ef9dc9f9fb6be57917accea46a3204#p140392
https://transcripts.foreverdreaming.org/viewtopic.php?p=140287&sid=86ef9dc9f9fb6be57917accea46a3204#p140287
https://transcripts.foreverdreaming.org/viewtopic.php?p=140287&sid=86ef9dc9f9fb6be57917accea46a3204#p140287
https://transcripts.foreverdreaming.org/viewtopic.php?p=140147&sid=86ef9dc9f9fb6be57917accea46a3204#p140147
https://transcripts.foreverdreaming.org/viewtopic.php?p=140147&sid=86ef9dc9f9fb6be57917accea46a3204#p140147
https://transcripts.foreverdreaming.org/viewtopic.php?p=139927&sid=86ef9dc9f9fb6be57917accea46a3204#p139927
https://transcripts.foreverdreaming.org/viewtopic.php?p=139927&sid=86ef9dc9f9fb6be57917accea46a3204#p139927
https://transcripts.foreverdreaming.org/viewtopic.php?p=139794&sid=86ef9dc9f9fb6be57917accea46a3204#p139794
https://transcripts.foreverdreaming.org/viewtopic.php?p=139794&sid=86ef9dc9f9fb6be57917accea46a3204#p139794
https://transcripts.foreverdreaming.org/viewtopic.php?p=139793&sid=86ef9dc9f9fb6be57917accea46a3204#p139793
https://transcripts.foreverdreaming.org/viewtopic.php?p=139793&sid=86ef9dc9f9fb6be57917accea46a3204#p139793
https://transcripts.foreverdreaming.org/viewtopic.php?p=138529&sid=86ef9dc9f9fb6be57917accea46a3204#p138529
https://transcripts.foreverdreaming.org/viewtopic.php?p=138529&sid=86ef9dc9f9fb6be57917accea46a3204#p138529
https://transcripts.foreverdreaming.org/viewtopic.php?p=133202&sid=86ef9dc9f9fb6be57917accea46a3204#p133202
https://transcripts.foreverdreaming.org/viewtopic.php?p=133202&sid=86ef9dc9f9fb6be57917accea46a3204#p133202
https://transcripts.foreverdreaming.org/viewtopic.php?p=132816&sid=86ef9dc9f9fb6be57917accea46a3204#p132816
https://transcripts.foreverdreaming.org/viewtopic.php?p=132816&sid=86ef9dc9f9fb6be57917accea46a3204#p132816
https://transcripts.foreverdreaming.org/viewtopic.php?p=146264#p146264
https://transcripts.foreverdreaming.org/viewtopic.php?p=146264#p146264
https://transcripts.foreverdreaming.org/viewtopic.php?p=132710#p132710
https://transcripts.foreverdreaming.org/viewtopic.php?p=132710#p132710
https://transcripts.foreverdreaming.org/viewtopic.php?p=132599#p132599
https://transcripts.foreverdreaming.org/viewtopic.php?p=132599#p132599
https://transcripts.foreverdreaming.org/viewtopic.php?p=132542#p132542
https://transcripts.foreverdreaming.org/viewtopic.php?p=132542#p132542
https://transcripts.foreverdreaming.org/viewtopic.php?p=132175#p132175
https://transcripts.foreverdreaming.org/viewtopic.php?p=132175#p132175
https://transcripts.foreverdreaming.org/viewtopic.php?p=132090#p132090
https://transcripts.foreverdreaming.org/viewtopic.php?p=132090#p132090
https://transcripts.foreverdreaming.org/viewtopic.php?p=132089#p132089
https://transcripts.foreverdreaming.org/viewtopic.php?p=132089#p132089
https://transcripts.foreverdreaming.org/viewtopic.php?p=132088#p132088
https://transcripts.foreverdreaming.org/viewtopic.php?p=132088#p132088
https://transcripts.foreverdreaming.org/viewtopic.php?p=132087#p132087
https://transcripts.foreverdreaming.org/viewtopic.php?p=132087#p132087
https://transcripts.foreverdreaming.org/viewtopic.php?p=132086#p132086
https://transcripts.foreverdreaming.org/viewtopic.php?p=132086#p132086
https://transcripts.foreverdreaming.org/viewtopic.php?p=132085#p132085
https://transcripts.foreverdreaming.org/viewtopic.php?p=132085#p132085
https://transcripts.foreverdreaming.org/viewtopic.php?p=132084#p132084
https://transcripts.foreverdreaming.org/viewtopic.php?p=132084#p132084
https://transcripts.foreverdreaming.org/viewtopic.php?p=132083#p132083
https://transcripts.foreverdreaming.org/viewtopic.php?p=132083#p132083
https://transcripts.foreverdreaming.org/viewtopic.php?p=132082#p132082
https://transcripts.foreverdreaming.org/viewtopic.php?p=132082#p132082
https://transcripts.foreverdreaming.org/viewtopic.php?p=132081#p132081
https://transcripts.foreverdreaming.org/viewtopic.php?p=132081#p132081
https://transcripts.foreverdreaming.org/viewtopic.php?p=132080#p132080
https://transcripts.foreverdreaming.org/viewtopic.php?p=132080#p132080
https://transcripts.foreverdreaming.org/viewtopic.php?p=132079#p132079
https://transcripts.foreverdreaming.org/viewtopic.php?p=132079#p132079
https://transcripts.foreverdreaming.org/viewtopic.php?p=132078#p132078
https://transcripts.foreverdreaming.org/viewtopic.php?p=132078#p132078
'''
