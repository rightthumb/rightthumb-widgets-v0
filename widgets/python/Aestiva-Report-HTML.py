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
# import sys, time
##################################################
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');
##################################################


def sw():
    pass
    #b)--> examples
    # _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
    #e)--> examples
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
    _.switches.register( 'Sections', '-sections', '"New Request" "Site Visit" "Load Calcs"' )
    _.switches.register( 'tr2', '-tr2' )

_._default_settings_()
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
# __.setting('receipt-log',True)
# __.setting('receipt-file',True)
# __.setting('myFileLocations-skip-validation',False)
# __.setting('require-pipe',False)
# __.setting('require-pipe||file',False)
# __.setting('pre-error',False)
# __.setting('switch-raw',[])


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
                        _.hp('ae.r -sections "New Request" "Site Visit" "Load Calcs" -f report.htm -tr2 | cp'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
                    # { 'name': 'name', 'abbreviation': 'n' },
# columns used for
#   - abbreviation in switches
#       - ex: -column n s
#           - instead of: -column name size
#       - ex: -sort n
#       - ex: -group n
#   - sort is used for things like size sort by bytes
#   - responsiveness to terminal width
#       - order is important
#       - most important on top
        
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
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def triggers():
    _._default_triggers_()
    # _.switches.trigger( 'Files', _.myFileLocations, vs=True )
    # _.switches.trigger( 'Ago', _.timeAgo )
    # _.switches.trigger( 'Folder', _.myFolderLocations )
    # _.switches.trigger( 'URL', _.urlTrigger )
    # _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',False); _.l.sw.register( triggers, sw );

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

def genColors(line):
    global header
    colors=[]
    for cline in header.split('\n'):
        if '=' in cline and not '""' in cline:
            colors.append(cline.split('=')[0].strip())
    return colors
def process(line,TheSectionHere='',TheTableID=''):
    if TheSectionHere:
        line = line.replace('TheSectionHere',TheSectionHere)
        line = line.replace('TheTableID',TheTableID)
    separator = '^'
    colors = [
                'the_section_color',
                'the_job_color',
                'the_project_color',
                'the_contact_color',
    ]
    code=separator+"""
+'"'+
""".strip()+separator
    code=code.strip()
    # line = line.replace('"',code)
    line = line.replace('sectionID',separator+'+sectionID+'+separator)
    hasColor=False
    for color in colors:
        if color in line:
            hasColor=True
            line=line.replace(color,code.replace("""'"'""",color))
    if not hasColor and 'section' in line and not 'sectionID' in line:
        line = line.replace('section',separator+'+section+'+separator)
    if 'TheRow' in line:
        line = line.replace('TheRow',separator+'+TheRow')
        line = line.replace(']',']+'+separator)
    line = 'html += ^'+line+'\\n^'
    return line

def processLines(lines,TheSectionHere='',TheTableID=''):
    global header
    global before
    global after
    output=[]
    countB=0
    countA=0
    for line in lines.split('\n'):
        skip=False
        # print(line.strip())
        if line.strip() in before:
            countB+=1
            if _.switches.isActive('tr2'):
                if countB==2:
                    skip=True
                    output.append(before[line.strip()])
            else:
                skip=True
                output.append(before[line.strip()])
        if line.strip() in after:
            countA+=1
            if _.switches.isActive('tr2'):
                if countA==2:
                    skip=True
            else:
                skip=True
        if not skip:
            output.append(process(line,TheSectionHere,TheTableID))
        if line.strip() in after:
            if _.switches.isActive('tr2'):
                if countA==2:
                    skip=True
                    output.append(after[line.strip()])
            else:
                skip=True
                output.append(after[line.strip()])
    return '\n'.join(output)
def action():
    global header
    global before
    global after
    global TheSection
    _.pr()
    _.pr()
    _.pr(header)
    lines='\n'.join(_.myData())
    sections1=lines.split('<!-- table-start -->')
    sections2=sections1[1].split('<!-- table-end -->')
    head=sections1[0]
    body=sections2[0]
    footer=sections2[1]
    html=''
    html+=processLines(head)
    if not _.switches.isActive('Sections'):
        html+=processLines(body)
    else:
        for i,section in enumerate(_.switches.values('Sections')):
            ii=str(i+1)
            html+=TheSection.replace('TheSectionHere',section).replace('TheTableID',ii)
            html+=processLines(body,section,ii)
    html+=processLines(footer)
    _.pr(html)
    

    _.pr('HD=html')


header = '''
section_bg_grey = "#d3d3d3"
section_bg_dark_purple = "#815caf"
section_bg_light_purple = "#eb7ffc"
section_bg_dark_green = "#198045"
section_bg_light_green = "#5fed2f"
section_bg_dark_blue = "#0c31f9"

job_bg_pink = "#ff3f81"
job_bg_purple = "#7b4cff"

project_bg_white = "#ffffff"
project_bg_green = "#2bcd6e"
project_bg_dark_purple = "#bf54eb"
project_bg_light_purple = "#eb7ffc"
project_bg_light_blue = "#abcbff"
project_bg_teal = "#76d2e2"

contact_bg_yellow = "#f9d901"
contact_bg_purple = "#b934b1"
contact_bg_dark_green = "#17bc9c"
contact_bg_dark_light = "#48ea0f"
html = ""

'''
TheSection='''
sectionID = "TheTableID"
section = "TheSectionHere"
IF section = "New Request" THEN
    the_section_color = section_bg_grey
/IF
IF section = "Site Visit" THEN
    the_section_color = section_bg_light_purple
/IF
IF section = "Load Calcs" THEN
    the_section_color = section_bg_dark_purple
/IF
IF section = "" THEN
    the_section_color = section_bg_dark_green
/IF
'''
'''
"New Request" "Site Visit" "Load Calcs"
'''
after = {
    '<tr>': '''

MyOut=FIND("52834.1001.1002","")
TheRecords=GETCOLEQ(MyOut,16,section)
FOR NAME=TheRecords ROWNAME=TheRow DO
IF TheRow[18,1] = "" THEN
    the_project_color = project_bg_green
/IF
IF TheRow[18,1] = "Manual J" THEN
    the_project_color = project_bg_green
/IF
IF TheRow[18,1] = "Energy" THEN
    the_project_color = project_bg_dark_purple
/IF
IF TheRow[18,1] = "Design" THEN
    the_project_color = project_bg_light_purple
/IF
IF TheRow[18,1] = "On-Site" THEN
    the_project_color = project_bg_light_blue
/IF
IF TheRow[18,1] = "Other" THEN
    the_project_color = project_bg_teal
/IF

IF TheRow[17,1] = "" THEN
    the_contact_color = contact_bg_yellow
/IF
IF TheRow[17,1] = "Website" THEN
    the_contact_color = contact_bg_yellow
/IF
IF TheRow[17,1] = "Engineer" THEN
    the_contact_color = contact_bg_purple
/IF
IF TheRow[17,1] = "Builder/Contractor" THEN
    the_contact_color = contact_bg_dark_green
/IF
IF TheRow[17,1] = "Homeowner" THEN
    the_contact_color = contact_bg_dark_light
/IF
html+="<tr>"
''',
}
'''
# MyOut Columns:
#  1 - Document ID (DOCID)
#  2 - Date Created (WD)
#  3 - Doc ID (AG)
#  4 - Bill To Name / Company (AK)
#  5 - Bill To Address (AM)
#  6 - Bill To Email (AO)
#  7 - Job Name (AQ)
#  8 - Services (AY)
#  9 - Services Other (AZ)
# 10 - Residential/Commercial? (BA)
# 11 - Project Type (BB)
# 12 - Project Type Other (BD)
# 13 - Living Area (SF) (BH)
# 14 - Company Name (AE)
# 15 - Contact Name (AF)
# 16 - Status (GY)
# 17 - Contact Type (HF)
# 18 - Services2 (HG)
# /#
'''

before = {
    '</tr>': '''
html+="</tr>"

/FOR


''',
}

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
    action(); _.isExit(__file__);

