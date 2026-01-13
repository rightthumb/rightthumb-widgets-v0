import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
    _.switches.register( 'IP', '-ip' )
    _.switches.register( 'Ports', '-p,-port,-ports' )
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
    'relatedapps': [],
    'prerequisite': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()
    _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
    _.switches.trigger( 'DB', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

# ssa.gov

string = '''
sudo iptables -t nat -A PREROUTING -p tcp -d 40.160.53.101 --dport [port] -j DNAT --to-destination 192.168.122.50:[port]
sudo iptables -t nat -A POSTROUTING -p tcp -d 192.168.122.50 --dport [port] -j SNAT --to-source 40.160.53.101
'''.strip()

def action():
    global string
# 2077, 2078, 2079, 2080, 3306, 111, 5355

    ports = [ 22, 25, 443, 993, 2082, 2083, 995, 2086, 2087, 2091, 587, 110, 143, 80, 465 ]
    out = []
    for port in ports:
        s = string.replace('[port]',str(port))
        out.append(s)
    out = '\n\n'.join(out)
    _.pr(out)
########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)