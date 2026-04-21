import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
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



import socket
import yaml


def dig_short_yaml(text_domains):
    """
    Simulates: dig +short
    Input:  newline-delimited domains
    Output: YAML with:
            ip:
              - domain
              - domain2
    """
    domain_list = [d.strip() for d in text_domains.splitlines() if d.strip()]
    ip_map = {}

    for domain in domain_list:
        try:
            ip = socket.gethostbyname(domain)
        except Exception:
            continue  # skip unresolved domains

        ip_map.setdefault(ip, []).append(domain)

    # Sort for stable output
    formatted = {ip: sorted(domains) for ip, domains in sorted(ip_map.items())}

    return yaml.dump(formatted, sort_keys=True, default_flow_style=False)





domains = '''
thetattedgentleman.com
realtornearmeflorida.com
rejuvenatemassagetherapytampa.com
goddesscronerising.com
thetattedhusband.com
buildtest.xyz
offmarkettampabay.com
notarynearmetampabay.com
notaryremoteflorida.com
homehost.info
tampabayoffmarket.com
realtornearmetampabay.com
webuythathouse.com
jessicareph.com
stitchedheart.com
thetakentemptress.com
stitcheart.com
relaxthestaff.com
housetomyhomerealtor.com
sextica.com
mothercronerising.com
'''.strip().split()



def action():
    out = dig_short_yaml('\n'.join(domains))
    _.pr(out)

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)