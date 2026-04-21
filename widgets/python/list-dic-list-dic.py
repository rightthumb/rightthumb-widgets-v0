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
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob', description='Files', isRequired=False )
	_.switches.register( 'Table', '-t,-tbl,-table' )
	_.switches.register( 'NoTable', '-notable' )
	_.switches.register( 'Table-Not', '-not,-tnot,-nott' )
	_.switches.register( 'Fields', '-fd,-fld,-field,-fields' )
	_.switches.register( 'Split', '-split' )
	_.switches.register( 'ALL', '-all' )

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
						_.hp(''),
						_.hp('p list-dic-list-dic --json'),
						_.hp('p list-dic-list-dic --json -fd extension -split " or " " and "'),
						_.hp('p list-dic-list-dic --json -all'),
						_.hp(''),
						_.hp('p list-dic-list-dic -f %tmpf7% -all'),
						_.hp('p list-dic-list-dic -f %tmpf7%'),
						_.hp('p list-dic-list-dic -f %tmpf7% -t audio -fd extension -split " or "'),
						_.hp('p list-dic-list-dic -f %tmpf7% -fd extension -split " or " " and "'),
						_.hp('p list-dic-list-dic -f %tmpf7% -fd extension -split " or " " and " -notable'),
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

def fieldg(ldld):
	fields=[]
	for ld in ldld:
		for table in ld:
			for fld in list(ld[table][0].keys()):
				if not fld in fields: fields.append(fld)
	for fld in fields:
		_.fields.register( 'ldld', 'fields', fld )
	return fields
def process(ldld):
	# print(ldld)
	# print(type(ldld))
	tbl = _.switches.values('Table')
	nott  = _.switches.values('Table-Not')
	fields  = _.switches.values('Fields')
	split  = _.switches.values('Split')
	ALL  = _.switches.isActive('ALL')
	if not tbl and not nott and not fields and not ALL:
		for ld in ldld:
			for table in ld:
				_.pr(table,c='yellow')
				for fld in list(ld[table][0].keys()):
					if not fld in fields: fields.append(fld)
		_.pr()
		_.pr()
		for fld in fields: _.pr(fld,c='cyan')
	else:
		flds=fieldg(ldld)
		for ld in ldld:
			for table in ld:
				tablel=table.lower()
				good=True
				for tab in tbl:
					if not tab.lower() in tablel: good=False

				for nt in nott:
					if nt.lower() in tablel: good=False


				if good:
					if not _.switches.isActive('NoTable'):
						_.pr(line=True,c='green')
						_.pr(table,c='yellow')
					recs=[]
					for rec in ld[table]:

						if fields and len(fields)==1:
							for fd in rec:
								if fd.lower() in fields:
									fld = _.fields.value( 'ldld', 'fields', fd , right=True )
									if split:
										fdr = rec[fd]
										for sp in split:
											fdr=fdr.replace(sp,'3f582e69')
											# if sp in rec[fd]:
										for rfd in fdr.split('3f582e69'):
											_.pr( rfd.strip() )
									else:
										_.pr( rec[fd] )
						else:
							# for fd in rec: _.pr( _.fields.value( 'ldld', 'fields', fd , right=True ),'  ',rec[fd] )
							if not fields: fields=flds
							fx=[]
							for f1 in fields:
								for f2 in flds:
									if f1.lower()==f2.replace(' ','_').lower(): fx.append(f2)
							fields=fx
							rrec={}
							for fz in fields: rrec[fz]=rec[fz]
							recs.append(rrec)
					if fields and len(fields)==1:pass
					else:
						_.pt(recs)




def action():
	if _.isData() and type(_.isData()) == list and _.isData()[0] and not type(_.isData()[0])==str: process(_.isData())
	elif _.isData():
		for path in _.isData():
			process( _.getTable2(path) )

	#n)--> iterate
	# for subject in _.isData(r=0): _.pr(subject)
	

_.switches.fieldSet( 'Long', 'active', True )

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


"""
// https://www.computerhope.com/issues/ch001789.htm

hackTool.hack.instructions = [
	{
		"name": "ext",
		"location": {
			"parent": "ul",
			"children": [
				{
					"name": "label",
					"location": "li",
					"type": "list",
					"settings": { "delim_fields": " - ", "fields": [ "extension", "description" ] }
				}
			]
		},
		"type": "records",
		"settings": {
			"labels": "h2"
		}
	}
]
hackTool.autoHack();
copy(  hackTool.payload.ext  )
"""