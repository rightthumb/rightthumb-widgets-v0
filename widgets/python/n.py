import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Project', '-p,-pro,-project', 'Site/Toolbox.Menu' )
	_.switches.register( 'Documentation', '-d,-doc,-documentation', 'Public/Instructions' )
	_.switches.register( 'Note', '-n,-note', 'Snippets of this file to search for in file' )
	_.switches.register( 'EncryptNote', '-e,-en,-encrypt', '' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Folders', '-fo,-folder,-folders','Subscriptions Products' )
	_.switches.register( 'URLS', '-u,-url,-urls', 's snip' )
	_.switches.register( 'Notifications', '-notify', 'on, off' )
	_.switches.register( 'DisplayAliasesTables', '-t,table,-tables', 'Documentation Note' )
	_.switches.register( 'Settings', '-settings', '[]' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'n.py',
	'description': 'Notes that may me associated with files',
	'categories': [
						'notes',
				],
	'examples': [
						_.hp('p n -project tb -file tb.home -note tb.home.scrap=Scrap Pad of text snippets to search for in file and find any relevant areas in the file'),
						_.hp('p n -project -n tb.home.scrap'),
						_.hp('p n -project tb=Site/Toolbox.Menu -documentation tb.pi=Public/Instructions -file tb.prod=products.php -note tb.prod.pi.h.p=How to Purchase.md'),
						_.hp('p n -encrypt -n gmail.pw=Gmail Username and Password -url "https://mail.google.com/mail/u/0/#inbox"'),
						_.hp('p n -p tb=Site/Toolbox.Menu -d tb.pi=Public/Instructions -file tb.prod=products.php -n tb.prod.pi.h.p=How to Purchase'),
						_.hp('p n -p tb -d tb.pi -file tb.prod -n tb.prod.pi.h.p=How to Purchase '),
						_.hp('p n -n tb.prod.pi.h.p'),
						_.hp('p n -project tb=Site/Toolbox.Menu -documentation tb.iib=Internal/Products -folders tb.sp=Subscriptions Products -note tb.ppp.prod.w=Product IDs To Watch -notify on'),
						_.hp('p n -project sg=Site/Global -documentation sg.bp.p=Billing/Processing/Paypal -note Paypal.basics=Payment Processing Paypal Basics'),
						_.hp('p n -p tb -d tb.iib -fo tb.sp -n Paypal.basics=Payment Processing Paypal Basics'),
						_.hp('p n -n Paypal.basics'),
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

def action():
	_open = _.regImp( __.appReg, 'file-open' )
	_open.switch('Backup')

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);