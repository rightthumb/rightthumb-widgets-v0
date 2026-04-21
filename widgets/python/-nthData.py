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
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')
##################################################

# app_navigator: switches
def sw():
    pass
    #b)--> examples
    # _.switches.register( 'Input', '-i', group='Group Name' )
        ##  -->    p SwitchGroupsExamples   <--
    # #e)--> examples
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt  ||  folderAlias==FileInThatFolder.txt' )

    tabGroup = 0


    tabGroup += 1
    _.switches.register( 'Source', '-src,-source', '(optional) file.json  ||  file.csv  ||  pipe', group=[tabGroup,'What To Operate On',0,'(optional if imported and data is already loaded)'] )
    _.switches.register( 'Paths', '-p,-path,-paths', 'data.[*]  ||  data.[7]  ||  folder  ||  data.[*].name', group=[tabGroup,'What To Operate On'] )
    _.switches.register( 'Fields', '-fi,-field,-fields', 'name  bytes  ext  ||  url  title', group=[tabGroup,'What To Operate On'] )
    _.switches.register( 'Endpoint', '-e,-endpoint', 'data  ||  data.[0]  ||  records.[*]', group=[tabGroup,'What To Operate On'] )


    tabGroup += 1
    _.switches.register( 'Action', '-a,-action', 'index  ||  search  ||  data  ||  inject', group=[tabGroup,'Action / Behavior'] )
    _.switches.register( 'StopAtLists', '-sl,-stop-lists,-stop-at-lists', group=[tabGroup,'Action / Behavior'] )


    tabGroup += 1
    _.switches.register( 'SearchPaths', '-sp,-search-path,-search-paths', 'data.[*]  ||  records.[*]  ||  [*].notes', group=[tabGroup,'Search'] )
    _.switches.register( 'SearchWhat', '-sw,-search-what', 'all  ||  keys  ||  values  ||  paths', group=[tabGroup,'Search'] )
    _.switches.register( 'SearchDepth', '-sd,-search-depth,-depth', '0=all-depths  ||  1  ||  2  ||  3', group=[tabGroup,'Search'] )
    _.switches.register( 'Plus', '+', 'findThis  anotherThing', group=[tabGroup,'Search'] )
    _.switches.register( 'Minus', '-', 'omitThis  skipThat', group=[tabGroup,'Search'] )
    _.switches.register( 'StrictCase', '-case,-strict,-strictcase', group=[tabGroup,'Search'] )
    _.switches.register( 'Or', '-or', group=[tabGroup,'Search'] )


    tabGroup += 1
    _.switches.register( 'InjectPaths', '-ip,-inject-path,-inject-paths', 'data.[0].name  ||  data.[4].url  ||  data.[*]', group=[tabGroup,'Inject'] )
    _.switches.register( 'InjectValues', '-iv,-inject-value,-inject-values', 'newName  ||  https://new-url.com  ||  {"name":"new record"}', group=[tabGroup,'Inject'] )
    _.switches.register( 'AppendPath', '-ap,-append-path', 'data.[*]  ||  [*]', group=[tabGroup,'Inject'] )
    _.switches.register( 'AppendValue', '-av,-append-value', '{"name":"new record"}  ||  123  ||  some text', group=[tabGroup,'Inject'] )


    tabGroup += 1
    _.switches.register( 'Return', '-r,-return', 'paths  ||  content  ||  path-content', group=[tabGroup,'Output'] )
    _.switches.register( 'OutputPathStyle', '-ops,-output-path-style,-path-style', 'full  ||  endpoint', group=[tabGroup,'Output'] )
    _.switches.register( 'Print', '-pr,-print', group=[tabGroup,'Output'] )
    _.switches.register( 'JSON', '-json', group=[tabGroup,'Output'] )
    _.switches.register( 'YAML', '-yml,-yaml', group=[tabGroup,'Output'] )
    _.switches.register( 'CSV', '-csv', group=[tabGroup,'Output'] )


    tabGroup += 1
    _.switches.register( 'UseFrameworkSearch', '-ufs,-framework-search,-search-fn', 'use imported framework search function', group=[tabGroup,'Advanced / Hooks'] )
    _.switches.register( 'TriggerPreSearch', '-tps,-trigger-pre-search', 'data.[*].epoch==autoDate  ||  *.epoch==autoDate', group=[tabGroup,'Advanced / Hooks'] )
    _.switches.register( 'TriggerPreReturn', '-tpr,-trigger-pre-return', 'data.[*].where==cleanStoreName', group=[tabGroup,'Advanced / Hooks'] )


_._default_settings_()

# __.setting('pipe-cleaner',False)
# __.setting('pipe-cleaner', {'first': False})

# __.setting('omit-switch-triggers',['Ago'])
# __.setting('omit-functions',['myFolderLocations','aliasesFo'])
# if not 'Ago' in __.setting('omit-switch-triggers',d=[]): pass
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
    'description': 'Changes the world',
        # _.ail(1,'subject')+
        # _.aib('one')+
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p thisApp -file file.txt'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
                    # { 'name': 'name', 'abbreviation': 'n' },
                    # { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
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
    # _.switches.trigger( 'Files', _.isFileSimple )                 # No File Registration          (Fn Alias Resolves To: def isFile)
    
    _.switches.trigger( 'DB', _.aliasesFi )
    # _.switches.trigger( 'Ago', _.timeAgo )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
    # _.switches.trigger( 'URL', _.urlTrigger )
    # _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
    #n)--> _.Switches usage
        # Triggers = { 'Files': myFunc }
        # Help = { 'Files': 'Specify Files' }
        ## ---> Switches Method <---
        # Switches = { 'Files': '-json,-yaml' }; Triggers = { 'Files': _.isFileAdvanced }
        # sw = __.Switches(Switches, Triggers, Help, input(': '))
        ## ---> Switches Method <---
        # grouped = _.y("Files:|  In: -f,-in|  Out: -o,-out   ||   Utility:|  Clean: --c")
        ## ---> Switches Method <---
        # simple = _.y("Files: -json,-yaml || Clean: --c")
        ## ---> Switches Method <---
        # All_in_One=_.y('- n: Files|  s: -f|  h: Specify Files|  t: All_in_One    ||    - n: Clean|  s: --c|  h: Pretty Print')
        # def a1File(p): return '~~'+p
        # __.trig['All_in_One'] = a1File
        ## ---> Switches Method <---
        # p=1
        # Grouped_All_in_One=_.y('Os: || - n: Files|  s: -f|  h: Specify Files|  t: aFi    ||    - n: Folder|  s: -d|  h: Specify Folder    ||   Utility:|- n: Clean|  s: --c|  h: Pretty Print',p=p)
        # cmd = 'app -f test.txt -d test -h more'
        # sw = __.Switches(Grouped_All_in_One, {}, {}, cmd)
        
        
        # sw.isActive('Files')  sw.isActive('Files','-json')
        # sw.value('Files')  sw.values('Files')  sw.values('Files','-json')

        # sw.set('Files', '-f', ['in'],add=True)
        # sw.set('Files', 0, 'f.c')                      # switch id from set switches
        # sw.set('Files', 0.0, ['in.'],add=True)         # uses last switch used or first switch if no id is given
        
        # sw.unset('Files')

        # v = sw.data('data','Files')
        # v = sw.data('data','Files', '-f)

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

    #n)--> caseUnspecific
        # for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

    #n)--> webpage from url
        # requests=__.imp('requests.post')
        #!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

    #n)--> import and backup example
        # _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
        # _bk.switch( 'Input', path ); bkfi = _bk.action();
    
    #n)--> inline
        # for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)
        #     or
        # results = [rel for rel in [subject for subject in _.isData(r=0) if _.showLine(subject)]]


    #n)--> fields
        # data = []
        # for k in code.db: data.append({'name': k+'  ' })
        # _.fields.asset( 'data', data )
        # for k in code.db:
        # 	_.pr(   _.fields.value( 'data', 'name', k+':' )+'  '+str(len(code.db[k]))   )

    #n)--> banner
        # banner=_.Banner(app); goss=banner.goss;


    #n)--> gptbot
        # from  _rightThumb._gptbot import GPT4oBot
        # bot = GPT4oBot()
        # bot.init_goal(goal='build a calculator webpage')
        # while True:
        # 	task, result = bot.run_next_task()
        # 	if not task:
        # 		print(result)
        # 		break
        # 	print(f"\n✅ Completed: {task}\n{result}\n")
        # 	input("Press Enter to continue...")

## audit folder in backup log
# import os
# base = os.getcwd()+os.sep
# db = _.getTable('fileBackup.json')
# latest = {}
# record = {}
# for i, rec in enumerate(db):
#     file = rec['file']
#     epoch = rec['timestamp']
#     backup = rec['backup']
#     if not file == 'D:\\websites\\domains\\heimdall.softwaredevelopment.solutions\\public_html\\2\\api.php': continue
#     if 'function ask' in _.getText(backup, raw=True):
#         _.pr(backup,c='green')
#     else:
#         _.pr(backup,c='red')
#     if base in file:
#         if not file in latest:
#             latest[file] = epoch
#             record[file] = i
#         else:
#             if epoch > latest[file]:
#                 latest[file] = epoch
#                 record[file] = i
# for path in record:
#     _.pr(db[ record[path] ]['file'])



# data = _.getTable2('conversations.json')
# _.saveTable2(data,'conversations.json')


#e)--> examples
########################################################################################
#n)--> start

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'db', 'tools')))
from nthData import nthData   # type: ignore

def action():


    dic = {}

    # ---------------------------------
    # action
    # ---------------------------------
    if _.switches.isActive('Search'):
        dic['action'] = 'search'
    elif _.switches.isActive('Data'):
        dic['action'] = 'data'
    elif _.switches.isActive('Inject'):
        dic['action'] = 'inject'
    else:
        dic['action'] = 'index'


    # ---------------------------------
    # basic flags
    # ---------------------------------
    if _.switches.isActive('Print'):
        dic['print'] = True

    if _.switches.isActive('StopAtLists'):
        dic['stop_at_lists'] = True


    # ---------------------------------
    # paths / fields
    # ---------------------------------
    if _.switches.isActive('Path'):
        dic['paths'] = _.switches.values('Path')

    if _.switches.isActive('Field'):
        dic['fields'] = _.switches.values('Field')


    # ---------------------------------
    # return type
    # ---------------------------------
    if _.switches.isActive('PathContent'):
        dic['return'] = 'path-content'
    elif _.switches.isActive('Content'):
        dic['return'] = 'content'
    else:
        dic['return'] = 'paths'


    # ---------------------------------
    # output path style
    # ---------------------------------
    if _.switches.isActive('Endpoint'):
        dic['output_path_style'] = 'endpoint'
    else:
        dic['output_path_style'] = 'full'


    # ---------------------------------
    # search block
    # ---------------------------------
    dic['search'] = {}

    if _.switches.isActive('SearchPath'):
        dic['search']['paths'] = _.switches.values('SearchPath')

    if _.switches.isActive('Keys'):
        dic['search']['what'] = 'keys'
    elif _.switches.isActive('Values'):
        dic['search']['what'] = 'values'
    elif _.switches.isActive('PathsOnly'):
        dic['search']['what'] = 'paths'
    else:
        dic['search']['what'] = 'all'

    if _.switches.isActive('Plus'):
        dic['search']['plus'] = _.switches.values('Plus')

    if _.switches.isActive('Minus'):
        dic['search']['minus'] = _.switches.values('Minus')

    if _.switches.isActive('StrictCase'):
        dic['search']['case_sensitive'] = True

    if _.switches.isActive('Or'):
        dic['search']['mode'] = 'any'
    else:
        dic['search']['mode'] = 'all'

    if _.switches.isActive('Depth'):
        dic['search']['depth'] = int(_.switches.value('Depth'))


    # optional framework search
    if _.switches.isActive('FrameworkSearch'):
        dic['search']['fn'] = _.showLine


    # ---------------------------------
    # inject
    # ---------------------------------
    if _.switches.isActive('InjectPath'):
        dic['inject'] = {}

        paths = _.switches.values('InjectPath')
        values = _.switches.values('InjectValue') if _.switches.isActive('InjectValue') else []

        for i, p in enumerate(paths):
            v = values[i] if i < len(values) else None
            dic['inject'][p] = v


    # append shortcut
    if _.switches.isActive('AppendPath'):
        dic['action'] = 'inject'
        if 'inject' not in dic:
            dic['inject'] = {}

        dic['inject'][_.switches.value('AppendPath')] = _.switches.value('AppendValue')


    fi = _.switches.value('Files')
    data = _.getTable2(fi)
    # dimensionalDictTool(data, path=None, search=None, stop_at_lists=True, print_result=True)
    out = nthData(data)
    from pprint import pprint
    pprint(out)



    # _.isDataClip()
    
    # load(); global c3po;

    # Threads = _.Threads(t=10, onDone=None)
    # def Done(result): pass  # other onFn have no args
    # Threads.queue(fn,  ak=None, timeout=None, onStart=None, onDone=Done, onKill=None, onTimeout=None, label=None)  # ak = args, kwargs

    #n)--> iterate
    # for subject in _.isData(r=0): _.pr(subject)
    # for subject in _.myData(): _.pr(subject)
    

# def load():
# 	global c3po
# 	c3po = _.getTable( 'table' )
# 	#n)--> print table
# 	_.pt(c3po)


##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################
########################################################################################
# import requests # pip install requests
########################################################################################
if __name__ == '__main__':
    #b)--> examples

    # banner.pr()
    # if len(_.switches.all())==0: banner.gossip()
    
    #e)--> examples
    action(); _.isExit(__file__)

