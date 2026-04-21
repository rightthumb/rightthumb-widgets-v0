import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Module', '-t,-m,-mod,-module,-template', 'gallery ' )
	_.switches.register( 'ListModules', '-list' )
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
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

templates={}

templates['0']='''
include_once($_SERVER['DOCUMENT_ROOT'].'/.re/manager.php');
$sds=new sds();
'''.strip()
templates['manager']='''
<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/.re/manager.php');
$sds=new sds();
'''.strip()
templates['gallery']='''
<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/.re/manager.php');
$sds=new sds();
$sds->mod('gallery');
'''.strip()
templates['Scrolls']='''
<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/.re/apps/Scrolls/3/index.php');
'''.strip()
templates['Arcanum']='''
<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/.re/apps/Arcanum/1/index.php');
'''.strip()
templates['OdinKey']='''
<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/.re/apps/OdinKey/1/index.php');
'''.strip()
templates['GlyphBox']='''
<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/.re/apps/GlyphBox/1/index.php');
'''.strip()
templates['ephemeralLinkManager']='''
$sds->mod('ephemeralLinkManager');
'''.strip()
templates['sdsEmail']='''
$sds->mod('sdsEmail');
$email=[
	'email'=>$phone,
	'subject'=>'Authorization pin',
	'body'=>'Your login pin is: <b>'.$pin.'</b>'
];
// sdsEmail($email);

$text=[
	'phone'=>$phone,
	'subject'=>'',
	'body'=> $pin
];
// sdsEmail($text);
'''.strip()
templates['Heimdall']='''
ini_set('display_errors', 0);
eval(file_get_contents('https://heimdall.softwaredevelopment.solutions/2/HeimdallClientAPI.php?H=1&t='.file_get_contents('https://keys.sds.sh/?id=sds-api'))); if(class_exists('HeimdallClientAPI',true)){$heimdall=new HeimdallClientAPI($_SERVER['SCRIPT_URI'],['813-690-1260'=>['admin'=>1,'view'=>1,'fo'=>['/opt','/home']]],file_get_contents('https://keys.sds.sh/?id=sds-api'),'view',['dir'=>[]]);}else{echo'api key revoked';exit;}
'''.strip()
templates['curlMe']='''
$sds->re('curlMe');
'''.strip()

templates['cookie']='''
$cookie = $sds->load('c');
'''.strip()
templates['raw']='''
$sds->raw($subject);
'''.strip()

templates['KeyAuth']='''
$sds->re('KeyAuth');
'''.strip()
templates['tmi']='''
$sds->re('tmi3');
'''.strip()
templates['gpt']='''
echo $sds->gpt($_REQUEST['prompt']);
'''.strip()
templates['yaml']='''
$sds->re('yaml');
'''.strip()
templates['json']='''
$sds->re('json');
'''.strip()
templates['fi']='''
$sds->re('fi');
'''.strip()
templates['keychain']='''
$sds->re('keychain');
'''.strip()
templates['keys']='''
file_get_contents('https://keys.sds.sh/?id=KEY');
'''.strip()
templates['JSONkeys']='''
$keys = json_decode( file_get_contents('https://keys.sds.sh/?dic=1&id=KEY') , true);
'''.strip()
templates['gpt4_split']='''
$sds->mod('gpt4_split');
echo gpt4_split($_REQUEST['prompt']);
'''.strip()
templates['php-vars']='''
<?php
header('Content-Type: application/json');
$arr =[];
$arr['SERVER'] = $_SERVER;
$arr['COOKIE'] = $_COOKIE;
$arr['FILES'] = $_FILES;
$arr['ENV'] = $_ENV;
$arr['GET'] = $_GET;
$arr['POST'] = $_POST;

echo json_encode($arr, JSON_PRETTY_PRINT);
'''.strip()
alias = {
			'base': 'manager',
			'm': 'manager',
			'man': 'manager',
			'g': 'gallery',
			'scrolls': 'Scrolls',
			'arcanum': 'Arcanum',
			'odinkey': 'OdinKey',
			'glyphbox': 'GlyphBox',
			'eph': 'ephemeralLinkManager',
			'email': 'sdsEmail',
			'heimdall': 'Heimdall',
			'api': 'Heimdall',
			'curl': 'curlMe',
			'c': 'cookie',
			'keyauth': 'KeyAuth',
			'security': 'KeyAuth',
			'ka': 'KeyAuth',
			'yml': 'yaml',
			'jkeys': 'JSONkeys',
			'server': 'php-vars',

}

def action():
	global templates
	global alias
	if _.switches.isActive('ListModules'):
		_.pr()
		_.pr('Modules:',c='Background.blue')
		for key in templates: _.pr('\t',key)
		_.pr()
		_.pr('Aliases:',c='Background.blue')
		for key in alias:
			_.pr('\t',key,'->',alias[key],c='cyan')
		return None
	if _.switches.isActive('Module'):
		if not len(_.switches.value('Module')): _.e('missing Module','deny access basic')
		template = _.switches.values('Module')[0]
		if template in alias: template=alias[template]
		if not template in templates:  _.e('invalid Module','gallery Scrolls')
		_.pr(templates[template])
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);