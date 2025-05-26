import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Last', '-last' )
	_.switches.register( 'Record', '-r,-rec,-record' )
	_.switches.register( 'Records', '-recs,-records' )
	_.switches.register( 'ID', '-i,-id' )
	_.switches.register( 'Field', '-fld,-field', 'ClientInfoString' )
	_.switches.register( 'Has', '-has' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'PowerShellExchangeLogs.py',
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
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start



def SendEmail(path):
	records = _.csv(path)
	for rec in records:
		last = rec
		if _.switches.isActive('Record') or _.switches.isActive('Records'):
			_.pv(rec)
		if _.switches.isActive('Record'):
			_.isExit(__file__)
	if _.switches.isActive('Last'):
		_.pv(last)
		_.isExit(__file__)
	# 	if rec['FromIP'] == '47.203.240.24': _.pv(rec)

	if rec['SenderAddress'] == 'dennis@theperformersnetwork.com':
		_.pr(rec['FromIP'],c='cyan')

def MailboxAuditLogs(path):
	records = _.csv(path)
	if _.switches.isActive('ID'):
		try:
			_.pv( records[int(_.switches.value('ID'))] )
		except:
			_.e('ID not found')
		_.isExit(__file__)
	cnt=0
	for rec in records:
		shouldProcess = True
		if _.switches.isActive('Has'):
			shouldProcess = False
			Has = _.switches.values('Has')
			for h in Has:
				hf = h.split('=')[0]
				hv = h.split('=')[1]
				if h in rec[hf] == hv:
					shouldProcess = True
			
		if shouldProcess:
			cnt+=1
			if _.switches.isActive('Field'):
				if _.switches.value('Field') in rec:
					_.pr(rec[_.switches.value('Field')])
			else:
				ip1 = rec['ClientIPAddress']
				ip2 = rec['ClientIP']
				if ip1 == ip2:
					_.pr(ip1)
				else:
					_.pr(ip1)
					_.pr(ip2)
		# _.pv(rec); _.isExit(__file__)
	# 	if rec['FromIP'] == '47.203.240.24':
	# 		_.pv(rec)

		# if rec['SenderAddress'] == 'dennis@theperformersnetwork.com':
		# 	_.pr(rec['FromIP'],c='cyan')
	_.pr('',_.addComma(cnt),c='cyan')
def action():
	if _.switches.isActive('Files'):
		for path in _.switches.values('Files'):
			if 'MailboxAuditLogs' in path: MailboxAuditLogs(path)
			if 'SendEmail' in path: SendEmail(path)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);