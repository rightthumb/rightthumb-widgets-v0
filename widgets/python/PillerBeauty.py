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

import os
import sys
import time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str

import _rightThumb._encryptString as _blowfish

import requests
import cssselect
from lxml import html

from tkinter import *
from tkinter.ttk import *

import ftplib

import _rightThumb._dir as _dir
##################################################


def appSwitches():
	_.switches.register( 'Schedule-Path', '-schedule' )
	_.switches.register( 'Add', '-add' )
	_.switches.register( 'List', '-list' )
	_.switches.register( 'Edit', '-edit' )
	_.switches.register( 'Live', '-live' )
	_.switches.register( 'Ago', '-ago' )
	_.switches.register( 'QuickHelp', '-qHelp' )
	_.switches.register( 'Build', '-build' )
	_.switches.register( 'Test', '-test' )



_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'PillerBeauty.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Configure PillerBeauty.com website',
	'categories': [
						'website',
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
						'p PillerBeauty -add',
						'',
						'p PillerBeauty -qhelp -s cid',
						'',
						'',
						'\tp PillerBeauty -test',
						'\tp PillerBeauty -build',
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



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )

	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )


########################################################################################
# START



def isINT( iiii ):
	if type(iiii) == int:
		return True
	if type(iiii) == str:
		if len(iiii):
			iisInt = True
			for x in iiii:
				if not x in '0123456789':
					iisInt = False
			if iisInt:
				return True
	return False



class Documentation_Initial:

	def done( self ):
		return self.record

	def __init__( self, record ):

		self.record_pre = record

		self.after = 'id,label,end,graphic,promo_msg_post,shipping,pDiscount_cid,BOGO_IDs'



		window = Tk()
		window.title('promo documentation')

		self.spaces = {}
		self.spacer = {}

		
		self.record_raw = {}
		self.record_label = {}



		for key in record.keys():
			self.record_raw[key] = StringVar()

		for key in record.keys():
			self.record_raw[key].set( record[key] )


		for key in record.keys():
			self.record_label[key] = Label(window, text=key.replace('_',' '))
			self.spacer[ key ] = Label(window, text='   ')
			if key in self.after.split(','):
				self.spaces[ key ] = Label(window, text='   ')
		self.spaces[ 'DONE_BUTTON' ] = Label(window, text='   ')



		self.record_key = {}
		for key in record.keys():
			self.record_key[key] = Entry(window, textvariable=self.record_raw[key], justify=LEFT, width=40)



		def validate():
			self.record = {}
			for key in record.keys():
				self.record[key] = self.record_raw[key].get()


			window.destroy()
			window.quit()
			self.done()
			



		btn = Button(window, text='Done', command=validate)

		theRow = 0

		for key in record.keys():
			theRow +=1
			self.record_label[key].grid(column=0, row=theRow)
			self.record_key[key].grid(column=1, row=theRow)
			self.spacer[ key ].grid(column=3, row=theRow)
			if key in self.after.split(','):
				theRow +=1
				self.spaces[ key ].grid(column=0, row=theRow)

		theRow +=1
		self.spaces[ 'DONE_BUTTON' ].grid(column=0, row=theRow)
		btn.grid(column=1, row=theRow)

		window.mainloop()



def buildAll(schedule):
	global sections
	for config in schedule:
		if config['active'] and _.autoDate(config['end']) > time.time():
			build(config)

	THE_FILE = """

<?


if ( $registered_schedule_area === 'img' ) {

||IMG||

}



if ( $registered_schedule_area === 'js' ) {

||JS||

}



if ( $registered_schedule_area === 'promo' ) {
$freeItemCounter_ALL = 0;
||PROMO_ITEM_stuff||

||PROMO||

}



if ( $registered_schedule_area === 'promo_item' ) {

||PROMO_ITEM||

}

?>


	"""

	global table
	base = "$freeItemCounter = array( HERE );"
	
	array = []
	for x in table:
		array.append( "'"+x['cid']+"' => 0" )

	arrayCode = ' , '.join( array )
	code = base.replace('HERE',arrayCode)
	THE_FILE = THE_FILE.replace( '||PROMO_ITEM_stuff||', code )

	THE_FILE = THE_FILE.replace( '||IMG||', ''.join( sections['IMG'] ) )
	THE_FILE = THE_FILE.replace( '||JS||', ''.join( sections['JS'] ) )
	THE_FILE = THE_FILE.replace( '||PROMO||', ''.join( sections['PROMO'] ) )
	THE_FILE = THE_FILE.replace( '||PROMO_ITEM||', ''.join( sections['PROMO_ITEM'] ) )
	_.saveText( THE_FILE, 'D:\\websites\\PillerBeauty\\_THE_SCHEDULE.PHP' )
	_.pr( THE_FILE )
	return THE_FILE



def build(config):

	global sections


	section_img = """


		if ( strtotime('now') > strtotime('|start| 6:01:00') && strtotime('now') < strtotime('|end| 6:01:00') ) {
		?>
			<div style="margin: auto;max-width: 700px;">
				<img src="images/popup/|graphic|" id="ad" alt="" style="max-width: 700px;" />
			</div>
		<? }


	"""
	section_js = """


			if ( strtotime('now') > strtotime('|start| 6:01:00') && strtotime('now') < strtotime('|end| 6:01:00') ) {
			$PROMO_CODE = '|promo_code|';
			$PROMO_MSG_PRE = '|promo_msg_pre|';
			$PROMO_MSG_POST = '|promo_msg_post|';
			}


	"""
	section_promo = """


			if ( strtotime('now') > strtotime('|start| 6:01:00') && strtotime('now') < strtotime('|end| 6:01:00') ) {
				if ( $promo == '|promo_code|' ) {
						$promo_shipping="<input type='hidden' name='shipping_1' value='|shipping|' />";
						$promo_discount="|pDiscount|";
						$promo_shipping_affected=true;
				}
			}


	"""
	section_promo_item = """


			if ( strtotime('now') > strtotime('|start| 6:01:00') && strtotime('now') < strtotime('|end| 6:01:00') ) {
||PROMO_ITEMs||
			}


	"""

	section_promo_items = """

				if ($cid === '|BOGO_ID|' ) {
					$freeItemCounter[$cid]++;
					if ($freeItemCounter[$cid] % 2 == 0 ) {
						$label_add = '- FREE';
						if ( !strpos( $item_name, $label_add )  ) {
							$item_name = "$item_name $label_add";
						}
						$item_price = 0;
					}
				}

	"""

	section_promo_items_pDiscount = """

				if ($cid === '|pDiscount_ID|') {
					// pDiscount
					$label_add = '- |pDiscount|% OFF';
					$promo_price_affected=true;
					if ( !strpos( $item_name, $label_add )  ) {
						$item_name = "$item_name $label_add";
					}
				}

	"""

	section_promo_item_G = """


			if ( strtotime('now') > strtotime('|start| 6:01:00') && strtotime('now') < strtotime('|end| 6:01:00') ) {
				if (  |EACH|  ) {
					$freeItemCounter_ALL++;
					if ( $freeItemCounter_ALL % 2 == 0 ) { 
						$item_name = "$item_name FREE";
						$item_price = 0;
					}
				}
			}



	"""



	section_promo_items_pDiscount_LIST = []
	section_promo_items_LIST = []
	# 
	pass

						


	hasDis = False
	hasDis_item = False
	hasBOGO = False
	hasBOGO_grp = False

	for x in config.keys():
		section_promo_items_pDiscount = section_promo_items_pDiscount.replace( '|'+x+'|', config[x] )
		section_img = section_img.replace( '|'+x+'|', config[x] )
		section_js = section_js.replace( '|'+x+'|', config[x] )
		section_promo = section_promo.replace( '|'+x+'|', config[x] )
		section_promo_item = section_promo_item.replace( '|'+x+'|', config[x] )
		section_promo_item_G = section_promo_item_G.replace( '|'+x+'|', config[x] )


	if not isINT( config['shipping'] ):
		section_promo = section_promo.replace( '$promo_shipping', '// $promo_shipping' )

	if config['pDiscount_IDs'] == '*':
		hasDis = True
		_.pr( 8888 )

	if not config['pDiscount_IDs'] == '-' and not config['pDiscount_IDs'] == '*' and  not config['pDiscount_IDs'] == '':
		hasDis_item = True
		hasDis = True
		_.pr( 8888 )
		section_promo = section_promo.replace( '$promo_shipping_affected', '// $promo_shipping_affected' )
		for x in config['pDiscount_IDs'].split(','):
			section_promo_items_pDiscount_LIST.append( section_promo_items_pDiscount.replace( '|pDiscount_ID|', x ) )
		# if ',' in config['pDiscount_IDs']:
		# else:
		#     section_promo_items_pDiscount_LIST.append( section_promo_items_pDiscount.replace( '|pDiscount_ID|', config['pDiscount_IDs'] ) )

	if not config['BOGO_IDs'] == '-' and not config['BOGO_IDs'] == '*' and  not config['BOGO_IDs'] == '':
		hasBOGO = True
		for x in config['BOGO_IDs'].split(','):
			section_promo_items_LIST.append( section_promo_items.replace( '|BOGO_ID|', x ) )
	elif config['BOGO_IDs'] == '*':
		hasBOGO = True
		global table
		for x in table:
			section_promo_items_LIST.append( section_promo_items.replace( '|BOGO_ID|', x['cid'] ) )


	if not config['BOGO_IDs_grp'] == '-' and not config['BOGO_IDs_grp'] == '*' and  not config['BOGO_IDs_grp'] == '':
		hasBOGO_grp = True
		code = []
		for x in config['BOGO_IDs_grp'].split(','):
			code.append( "$cid === '"+x+"' " )

		section_promo_item_G = section_promo_item_G.replace( '|EACH|', ' || '.join( code ) )



	if hasBOGO:
		xXx = section_promo_item
		xXx = xXx.replace( '||PROMO_ITEMs||',  ''.join( section_promo_items_LIST )  )
		sections['PROMO_ITEM'].append( xXx )

	if hasDis_item:
		xXx = section_promo_item
		xXx = xXx.replace( '||PROMO_ITEMs||',  ''.join( section_promo_items_pDiscount_LIST )  )
		sections['PROMO_ITEM'].append( xXx )

	if hasDis:
		sections['PROMO'].append( section_promo )

	if hasBOGO_grp:
		sections['PROMO_ITEM'].append( section_promo_item_G )


	if not config['promo_code'] == '':
		sections['JS'].append( section_js )

	if not config['graphic'] == '':
		sections['IMG'].append( section_img )

	
	# _.pr( 'hasDis', hasDis )
	# _.pr( 'hasDis_item', hasDis_item )
	# _.pr( 'hasBOGO', hasBOGO )
	# _.pr( 'hasBOGO_grp', hasBOGO_grp )

	# _.printVarSimple( config )
	# sys.exit()



def theHelp():
	global table
	if not table:

		url = 'http://www.pillerbeauty.com/_The_Categories.php'
		page = requests.get(url)
		tree = html.fromstring(page.content)
		tables = tree.cssselect('.category')
		for t in tables:
			cidA = t.cssselect('.cid')
			cid = cidA[0].text_content()
			nameA = t.cssselect('.name')
			name = nameA[0].text_content()
			table.append({ 'cid': cid, 'name': name })
		_.tables.register('Auto',table)
		_.tables.print('Auto','cid,name')


def action():
	if _.switches.isActive('Schedule-Path'):
		_.getTableProject( 'PillerBeauty.Schedule', 'schedule.json', path=True )
		return None

	global schedule
	global upload

	schedule = _.getTableProject( 'PillerBeauty.Schedule', 'schedule.json' )
	upload = _.getTableProject( 'PillerBeauty.Configure', 'ftp.index' )

	# _.printVarSimple( schedule )
	# sys.exit()


	if _.switches.isActive('List'):
		_.tables.register('Auto',schedule)
		_.tables.print('Auto', ','.join(list(schedule[0].keys())) )

	if _.switches.isActive('Edit'):
		_.tables.register('Auto',schedule)
		_.tables.print('Auto', ','.join(list(schedule[0].keys())) )
		index = {}
		for i,x in enumerate(schedule):
			index[x['id']] = i
		theID = input(' ID: ')
		_.pr()
		if len(theID) and theID in index:
			form = Documentation_Initial(schedule[ index[theID] ])
			record = form.record
			schedule[ index[theID] ] = record
			_.saveTableProject( 'PillerBeauty.Schedule', schedule, 'schedule.json' )
			ftp_upload()
		else:
			_.colorThis( 'Record not found', 'red' )

	if _.switches.isActive('Test'):
		_.tables.register('Auto',schedule)
		_.tables.print('Auto', ','.join(list(schedule[0].keys())) )
		index = {}
		for i,x in enumerate(schedule):
			index[x['id']] = i
		theID = input(' ID: ')
		_.pr()
		test = []
		if len(theID) and theID in index:
			test.append( schedule[ index[theID] ] )
		today = _.friendlyDate( time.time() ).split(' ')[0]
		yesterday = _.dateSub( today, '-', 1 )
		tommorow = _.dateAdd( today, '-', 1 )
		# _.pr( 'today', today )
		# _.pr( 'yesterday', yesterday )
		# _.pr( 'tommorow', tommorow )
		# sys.exit()
		test[0]['start'] = _.friendlyDate( yesterday ).split(' ')[0]
		test[0]['end'] = _.friendlyDate( tommorow ).split(' ')[0]
		buildAll(test)
		ftp_upload()
		



	if _.switches.isActive('QuickHelp'):
		theHelp()


	elif _.switches.isActive('Build'):
		theHelp()
		file = buildAll(schedule)
		ftp_upload()

	elif _.switches.isActive('Add'):
		theHelp()

		
		rID = _.miniUUID().replace('}','').replace('{','').replace('-','_')
		new = {
					'id': rID,

					'label': '2021-01',

					'start': '2021-01-01',
					'end': '2021-02-01',

					'graphic': 'img.jpg',

					'promo_code': rID,
					'promo_msg_pre': 'Signup then receive ',
					'promo_msg_post': '',

					
					'shipping': '-',

					'pDiscount': '%',
					'pDiscount_IDs': '*',

					'BOGO_IDs_grp': '',
					'BOGO_IDs': '',


					'active': 'Y',
					


		}

		form = Documentation_Initial(new)
		record = form.record
		# _.pr(record)
		_.printVarSimple( record )
		schedule.append( record )
		_.saveTableProject( 'PillerBeauty.Schedule', schedule, 'schedule.json' )
		
		file = buildAll(schedule)
		ftp_upload()



def ftp_upload():

	global schedule
	global upload

	# _.pr( 'upload', upload )
	# sys.exit()

	userA = 'g9SudNvwJMrYzgbw8BrhrwA7+D2PXO8oxna7YruupJQ='
	passwordA = 'rkKGQqm6wNA+7RgKXwwXDsaqYxU+3tlRNbHc6yr8QxxRJTVodjRuNg=='

	userB = _blowfish.decrypt( userA )
	passwordB = _blowfish.decrypt( passwordA )

	userB = _str.cleanBE( userB, ' ' )
	passwordB = _str.cleanBE( passwordB, ' ' )


	# _.pr(  userA  ,  passwordA )
	# _.pr(  userB  ,  passwordB )
	# sys.exit()

	_.pr( 'Uploading Schedule' )
	session = ftplib.FTP('ftp.pillerbeauty.com',  userB  ,  passwordB  )
	file = open('D:\\websites\\PillerBeauty\\_THE_SCHEDULE.PHP','rb')
	session.storbinary('STOR _THE_SCHEDULE.PHP', file)
	file = open('D:\\websites\\PillerBeauty\\header.php','rb')
	session.storbinary('STOR header.php', file)
	file.close()
	session.cwd('images')
	session.cwd('popup')

	fld = 'D:\\websites\\PillerBeauty\\images\\popup'+_v.slash

	for record in schedule:
		file_path = fld + record['graphic']
		# _.pr(file_path)
		if os.path.isfile( file_path ):
			file_dir =  _dir.fileInfo( file_path )
			# _.printVarSimple( file_dir )
			# sys.exit()
			uploaded = False
			if not record['graphic'] in upload:
				uploaded = True
			elif record['graphic'] in upload:
				if upload[ record['graphic'] ] < file_dir['date_modified_raw']:
					uploaded = True

			if uploaded:
				_.pr( 'Uploading', record['graphic'] )
				upload[ record['graphic'] ] = time.time()
				file = open( file_path ,'rb')
				session.storbinary('STOR ' + record['graphic'], file)
				file.close()
				_.saveTableProject( 'PillerBeauty.Configure', upload, 'ftp.index' )



	session.quit()



# _.saveTableProject( 'PillerBeauty.Configure', upload, 'ftp.index' )
table = []
schedule = None
upload = None
sections = {
	'IMG': [],
	'JS': [],
	'PROMO': [],
	'PROMO_ITEM': [],
}

# Documentation_Initial

"""
||JS||
||PROMO||
	||PROMO_ITEM_stuff||
	||section_promo_shipping||
||PROMO_ITEM||
	||PROMO_ITEMs||



THE_FILE
	section_js
	section_promo
		section_promo_item_stuff
	section_promo_item
		section_promo_items

include('../functions.php');
"""



########################################################################################
if __name__ == '__main__':
	try:
		action()
	except Exception as e:
		pass