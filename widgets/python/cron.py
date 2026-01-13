import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'cron.py',
    'description': 'Beautifully print cron jobs',
    'categories': [
                        'cron',
                ],
    'examples': [
                        _.hp('crontab -l | p cron'),
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




import os

# NEON_80S_THEME
NEON = {
    "start-end": "dark_orchid",
    "line":      "lawn_green",
    "warning":   "#FFEA00",
    "oc":        "#FF00A8",
    "sub":       "khaki",
    "cron":      "spring_green",
}

def action():
    global NEON
    cron = _.cmd('crontab -l')

    color = NEON['start-end']
    _.pr(line=1, h=color)

    section = False
    for line in cron.split('\n'):
        if not _.showLine(line): continue
        lineColor = NEON['line']  # default line color -> 'line'
        if line.strip().startswith('#'):
            pr = True
            lineColor = NEON['line']   # <-- changed: default comment color is now 'line'
            isOC = False
            if '<' in line:
                color = NEON['oc']
            if '</' in line:
                isOC = True
                pr = False
                _.pr()
                section = False
                lineColor = NEON['oc']
                # color = NEON['sub']
            elif '<' in line:
                isOC = True
                lineColor = NEON['oc']
                section = True
                # color = NEON['secondary_section']
            if section and not '<' in line:
                pr = False
                lineColor = NEON['oc']
            if pr:
                _.pr()
                _.pr(line=1, h=color)
                _.pr()
            if not isOC:
                lineColor = NEON['line']
            if section and not isOC:
                # lineColor = NEON['line']
                lineColor = NEON['sub']

        if '*' in line:
            _.pr()
            _.pr()

        schedule = ''
        if line.strip() and not line.strip().startswith("#"):
            parts = line.split(maxsplit=5)
            if len(parts) >= 6:
                schedule = " ".join(parts[:5])
                line  = parts[5]
                schedule = _.pr(schedule, p=0, h=NEON['cron'])
                schedule += '   '

        if not line.strip().startswith('#'):
            line = line.replace('&&', '\n  && ')
            line = line.replace(' -', '\n    -')
        _.pr(schedule + line, h=lineColor)

        if line.strip().startswith('#'):
            pr = False
            if '</' in line:
                color = NEON['oc']
                pr = True
            elif '<' in line:
                pr = False
                # color = NEON['secondary_section']
            if pr:
                _.pr()
                _.pr(line=1, h=color)
                _.pr()

    color = NEON['start-end']
    _.pr(line=1, h=color)


########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)