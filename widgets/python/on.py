import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
    pass
    _.switches.register( 'Session', '-ss,-se,-sess,-session' )
    _.switches.register( 'Folder', '-f,-folder' )
    _.switches.register( 'Stop', '-stop' )
    _.switches.register( 'Delete', '-del,-delete,-stop,-kill' )
    _.switches.register( 'RemoveIdleFlag', '-notIdle' )
    _.switches.register( 'Test', '-test' )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'onSave.py',
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p onSave'),
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
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


statuses = {}
stop_event = {}
thread = {}
folders = {}
sleepFor = {}
isOmit = {}
my_observer = {}
sessionsStopped = []

def monitor(folder, session):
    global statuses, stop_event, thread, sessionsStopped, tag
    global my_observer

    # Initialize statuses if needed
    if 'statuses' not in globals() or not statuses:
        statuses = {}

    # Initialize other variables
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True



    # tag['triggers']['fileFolders'] and not folder in tag['triggers']['files']
    

    triggerList = []

    try:
        pass
        tag['triggers']['folders'][folder]['expires']
        import _Triggers
        pr(line=1,c='cyan')
        pr('start expires',c='yellow')
        for path in _.fo(folder,r=0):
            if _Triggers.expires(path,tag['triggers']['folders'][folder]['expires']):
                pr('Expired:',path,c='red')
            else:
                pr('Not Expired:',path,c='green')
        pr('end expires',c='yellow')
        pr(line=1,c='cyan')
    except:
        pass

    triggerList.append(f'''
        try:
            tag['triggers']['files'][__.path(event.src_path)]['expires']
            run = True
        except:
            run = False

        if run:
            # print(event.src_path)
            # print('tag:::',tag['triggers']['files'][__.path(event.src_path)])
            print(_Triggers.expires(event.src_path,tag['triggers']['files'][__.path(event.src_path)]['expires']))
''')
    triggerList.append(f'''
        global my_observer
        global statuses
        global stop_event
        if __.path(event.src_path) in tag['triggers']['files']:
        #try:
            print('kill',event.src_path)
            tag['triggers']['files'][__.path(event.src_path)]['kill']
            __.KeyboardInterrupt = 1
            for sess in my_observer:
                my_observer[sess].stop()
                my_observer[sess].join()
                unregister(sess,'trigger')
                statuses[sess] = False
                stop_event[sess].set()

                if thread[sess] is not threading.current_thread(): thread[sess].join()
                sessionsStopped.append(sess)
            import sys
            sys.exit()
            print('killed',event.src_path)
        #except Exception as e:
        #    print('no kill',e,event.src_path)
''')
    


    # Dynamically create the event handler using exec
    includeTriggers = '\n\n'.join(triggerList)
    isOpen = '{'
    isClose = '}'
    fn = f'''
#def t{session}(event):
def t(event):
    try:
        global tag
        global statuses
        import _Triggers
{includeTriggers}
        pr(__.longSpace,r=1)
        pr(f"modified, {isOpen}event.src_path{isClose} has been modified", c='purple')
    except Exception as e:
        # print(e)
        print('Killed_101')
    '''
    exec(fn, globals())
    # Define the pattern matching event handler dynamically using exec

    


    # Ensure that patterns and ignore_patterns are valid
    patterns_value = f"'{patterns}'" if patterns else "None"
    ignore_patterns_value = f"'{ignore_patterns}'" if ignore_patterns else "None"

    # Safely generate the event handler code
    """
    exec(f'''
global my_event_handler
my_event_handler = PatternMatchingEventHandler({patterns_value}, {ignore_patterns_value}, {ignore_directories}, {case_sensitive})
my_event_handler.on_modified = t{session}
statuses["{session}"] = True
''', globals())
    """

    global my_event_handler
    my_event_handler = PatternMatchingEventHandler(
        patterns=patterns_value, 
        ignore_patterns=ignore_patterns_value, 
        ignore_directories=ignore_directories, 
        case_sensitive=case_sensitive
    )

    my_event_handler.on_modified = t
    statuses[session] = True


    # Set up the observer
    go_recursively = False
    my_observer[session] = Observer()
    my_observer[session].schedule(my_event_handler, folder, recursive=go_recursively)
    my_observer[session].start()

    # Logic for monitoring session status dynamically with exec
    code = f'''
try:
    cnt = 0
    err = 1

    def whileLoop(err):
        def whileLoopTest(err):
            ep = endpoint('Get', "{session}")
            if not ep.strip() == 'Active':
                pr('Session {session} has closed', c='Background.green')
                if "{session}" in statuses:
                    statuses["{session}"] = False
                return False
            return err
        global cnt
        try:
            if "{session}" not in statuses or "{session}" not in stop_event or "{session}" not in thread or "{session}" not in sleepFor:
                raise KeyError(f'Session "{session}" is missing from one of the required dictionaries.')

            while statuses["{session}"]:
                cnt += 1
                if _.switches.isActive('Test') and ('dump' in _.switches.value('Test') or False):
                    pr('monitor loop', cnt, c='Background.blue')
                time.sleep(sleepFor["{session}"])
                if not whileLoopTest(err):
                    err += 1
                else:
                    err = 1

            if err < 3:
                if _.switches.isActive('Test') and ('dump' in _.switches.value('Test') or False):
                    pr('err', err, c='Background.light_blue')
                whileLoop(err)

        except KeyError as e:
            __.monitorError = 'KeyError'
            pr(f"KeyError: {isOpen}str(e){isClose}", c='red')
            raise ValueError("KeyError")

        except KeyboardInterrupt:
            # whileLoop(err)
            __.monitorError = 'KeyboardInterrupt'
            pr("Session {session} has stopped by keyboard", c='red')
            __.KeyboardInterrupt = True
            raise ValueError("KeyboardInterrupt")

        finally:
            # whileLoop(err)
            if "{session}" in statuses and statuses["{session}"]:
                whileLoop(err)
            else:
                __.monitorError = 'finally'
                raise ValueError("finally")
                if _.switches.isActive('Test') and ('dump' in _.switches.value('Test') or False):
                    pr("Session {session} has stopped by finally", c='red')
                
                if _.switches.isActive('Test') and ('dump' in _.switches.value('Test') or False):
                    pr("Observer stopped")
                time.sleep(2)

    if statuses["{session}"]:
        whileLoop(err)
except Exception as e:
    if __.KeyboardInterrupt: raise ValueError("KeyboardInterrupt")
    '''
    
    __.monitorError = ''
    cnt2 = 0
    total = 0
    while cnt2 < 5:
        total += 1
        # print('while',cnt2,total,__.monitorError)
        if __.KeyboardInterrupt:
            break
        try:
            exec(code, globals())
        except KeyboardInterrupt:
            pr("Caught KeyboardInterrupt. Exiting gracefully...",c='red')
            __.KeyboardInterrupt = True

        except Exception as e:
            pass

        ep = endpoint('Get', session)
        if not ep.strip() == 'Active':
            cnt2 += 1
        else:
            cnt2 = 0
        # time.sleep(.7)





    my_observer[session].stop()
    my_observer[session].join()
    unregister(session,'monitor')
    statuses[session] = False
    stop_event[session].set()

    if thread[session] is not threading.current_thread(): thread[session].join()
    sessionsStopped.append(session)

    pr(__.longSpace,r=1)
    pr(f"Session stopped by URL {session} {folder}", c='red')

__.KeyboardInterrupt = False


def endpoint(theAction='Get', session='None', folder=None, json=False):
    # session = os.getenv('Session_ID')
    url = f'https://terminal.softwaredevelopment.solutions/on/?machine={urllib.parse.quote(_v.getMachineID())}&session={session}&status=Active&on=Save&action={theAction}'
    
    if folder is not None:
        # Ensure folder is a string before quoting
        if isinstance(folder, list):
            folder = ' '.join(folder)
        folder = str(folder)
        folder = urllib.parse.quote(folder)
        url += f'&folder={folder}'
    if _.switches.isActive('Test') and 'url' in  _.switches.value('Test'):
        test = True
    else:
        test = False
    if test: print(url)

    try:
        if json:
            result = requests.get(url.replace('_action_', theAction)).json()
        else:
            result = requests.get(url.replace('_action_', theAction)).text
        if test: print(result)
        return result
    except:
        pass

    pr('endpoint error', c='red')
    return 'Nope'


# requests.get(url).text
# response = requests.get(url).json()
def unregister(session,where):
    if _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or False):
        pr('unregister', session, where, c='yellow')
    global statuses
    global folders
    if session in statuses:
        del statuses[session]
    if session in folders:
        del folders[session]
lS = {
    'iter': 0,

    'while': 3,
    'empty': 0,
    'groups': 0,

    'max': 6,
    'thresh': 2,
    'reset': 3,

    'same': 0,
    'len': 0,
    'threshSame': 3,
}


def loadSessions():
    pr('Checking',c='green',r=1)
    global lS
    global statuses
    global folders
    global stop_event, thread, sleepFor, sessionsStopped
    global tag
    load()
    dump = endpoint('Dump', json=True)
    test = False
    if _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or 'url' in  _.switches.value('Test')):
        test = True
    if test:
        _.pv(dump)
    lS['iter'] += 1
    tmp = []
    for rec in dump:
        session = rec['session']
        folder = rec['folder']
        if not folder:
            continue
        tmp.append(rec)
    dump = tmp
    # if not len(dump):
    pr('Waiting',c='green',r=1)
    if lS['len'] == len(dump):
        lS['same'] += 1
    else:
        lS['same'] = 0
    lS['len'] = len(dump)
    same = False
    if lS['same'] > lS['threshSame']:
        same = True
        if _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or 'thresh' in  _.switches.value('Test')):
            if lS['same'] % lS['threshSame'] == 0:
                pr('same:', lS['same'],c='Background.purple')

    if len(dump) and same:
        if lS['while'] > 2 and  _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or 'thresh' in  _.switches.value('Test')):
            pr()
            pr('iter:', lS['iter'])
            pr('while:', lS['while'])
            pr('groups:', lS['groups'])
            pr()
        lS['while'] = 2
    if not len(dump):
        lS['empty'] += 1
        if _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or 'thresh' in  _.switches.value('Test')):
            pr('empty:', lS['empty'] % lS['thresh'],c='cyan')
    if lS['empty'] % lS['thresh'] == 0:
        lS['while'] += 1
        if lS['while'] > lS['max']:
            lS['while'] = lS['max']
            lS['groups'] += 1
            if _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or 'thresh' in  _.switches.value('Test')):
                pr('groups:', lS['groups'] % lS['thresh'],c='yellow')
            if lS['groups'] % lS['thresh'] == 0:
                lS['while'] = lS['reset']
                if _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or 'thresh' in  _.switches.value('Test')):
                    pr()
                    pr('iter:', lS['iter'])
                    pr('while:', lS['while'])
                    pr('groups:', lS['groups'])
                    pr()
            
        else:
            if _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or 'thresh' in  _.switches.value('Test')):
                pr('while:', lS['while'])

    records = {}
    sessionsToAdd = []
    sessionsToStop = []
    for rec in dump:
        session = rec['session']
        folder = rec['folder']
        if os.path.isdir(folder):
            shouldAdd = False
            if session in statuses:
                err = False
                if not session in folders:
                    err = True
                if folder is None or err or not folders[session] == folder or rec['status'] == 'Active':
                    statuses[session] = False
                    sleepFor[session] = .005
                    sessionsToStop.append(session)
                    if not session in folders or folders[session] == folder:
                        shouldAdd = True
            elif session not in statuses:
                shouldAdd = True
            if session in statuses: shouldAdd = False
            if shouldAdd:
                sessionsToAdd.append(session)
                records[session] = rec
    # print('sessionsToAdd:',sessionsToAdd)
    if not len(sessionsToAdd):
        shouldWait = False
    else:
        shouldWait = True
    if not shouldWait: return
    pr(__.longSpace,r=1)
    spent = []
    start = int(time.time())
    i = 0
    sessionsToAddCnt = 0
    sessionsAdded = []
    while shouldWait or sessionsToAddCnt > 10:
        sessionsToAddCnt += 1
        i += 1
        sessionsToAdd = list(set(sessionsToAdd))
        cnt = 0
        if not session in statuses: sessionsStopped.append(session)
        for session in sessionsToAdd:
            if session in sessionsStopped: cnt += 1
            if not session in spent:
                # unregister(session,'loadSessions')
                spent.append(session)
                diff = int(time.time()) - start
                if _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or False):
                    pr('here-101',i,session,diff,'\t',records[session]['folder'], c='cyan')
            sessionsAdded.append(session)
        # pr('sessionsToAdd:',sessionsToAddCnt, sessionsToAdd,c='darkcyan')
        if len(sessionsAdded) == len(sessionsToAdd): shouldWait = False
        if cnt == len(sessionsToAdd): shouldWait = False
    # print('records:',records)
    for session in records:
        # print(tag['triggers']['fileFolders'])
        if not folder in tag['triggers']['fileFolders'] and not folder in tag['triggers']['folders']:
            if not folder in isOmit: isOmit[folder] = 0
            if isOmit[folder] > 5:
                isOmit[folder] = 0
                pr(f"Folder not found in trigger tag: {folder}",c='red')
            isOmit[folder] += 1
            if _.switches.isActive('Test') and ( 'dump' in  _.switches.value('Test') or False):
                pr(f"Folder not found in trigger tag: {folder}",c='red')
            continue
        folder = records[session]['folder']
        if not records[session]['folder']: continue
        statuses[session] = True
        sleepFor[session] = 1
        folders[session] = folder
        
        stop_event[session] = threading.Event()
        thread[session] = threading.Thread(target=monitor, args=(folder, session))
        thread[session].start()
        global spentPrint
        if session in spentPrint and folder in spentPrint[session]:
            pass
        else:
            pr(session,folder, c='yellow')
            if session not in spentPrint: spentPrint[session] = []
            spentPrint[session].append(folder)

    # loadSessions
    

    # _.pv(dump)
    # _.isExit(__file__)

def pr(*args,c='Color.bold',r=0):
    args = list(args)
    if len(args) > 0 and args[0] == __.longSpace:
        # _.pr(__.longSpace,r=1)
        return

    _.pr(__.longSpace,r=1)
    _.pr(args,c=c,r=r)


spentPrint = {} 



 

def action():
    # print(__.appReg)
    appReg = __.appReg
    tagReg = _.regImp( __.appReg, 'tag' )
    tagReg.imp.action({
        'Clean': False,
        'Trigger': 'kill,all',
        'Files': _v.tt+os.sep+'tag.json',
    })
    __.appReg=appReg
    # tagReg.switch('Trigger','kill,all')
    # tagReg.switch('Files',_v.tt+os.sep+'tag.json')
    # tagReg.action()

    if _.switches.isActive('Test') and not len(_.switches.values('Test')): pr('\n\nTest:','thresh', 'url', 'dump\n\n',c='green')
    if _.switches.isActive('Session') and _.switches.isActive('Folder'):
        if not len(_.switches.values('Folder')):
            folder = os.getcwd()
        else:
            folder = _.switches.value('Folder')
        endpoint('Set', _.switches.value('Session'), os.path.abspath(folder))
        return
    elif _.switches.isActive('Session') and _.switches.isActive('Delete'):
        endpoint('Delete', _.switches.value('Session'), _.switches.values('Folder'))
        return
    elif _.switches.isActive('Session'):
        endpoint('Set', _.switches.value('Session'), os.path.abspath('.'))
        return
    global lS

    _.pr(line=1,c='yellow')
    try:
        while not __.KeyboardInterrupt:
            try:
                loadSessions()
            except:
                time.sleep(5)
                import sys
                sys.exit()    
            time.sleep(lS['while'])
    except KeyboardInterrupt:
        pr("Caught KeyboardInterrupt. Exiting gracefully...",c='red')
        __.KeyboardInterrupt = True

    except Exception as e:
        pr(f"action error {e}",c='red')
        if 'dictionary changed size during iteration' in str(e):
            __.KeyboardInterrupt = 1
            _.isExit(__file__)


__.longSpace = '                                                                                               '

loadCount = 0
tag = False
def load():
    global tag
    global loadCount
    if loadCount % 3 == 0 or not tag:
        # tag = _.getTable('tag.json')
        tag = _.getTable2(_v.tt+os.sep+'tag.json')
        if not tag:
            # Initialize tag
            tag = {
                'folders': {},
                'files': {},
                'related': {},
                'tags': {'files': {}, 'folders': {}},
                'triggers': {'files': {}, 'folders': {}, 'fileFolders': {}},
                'transactions': []
            }
        pr("Tag loaded.", c='darkcyan',r=1)
    loadCount += 1

########################################################################################
# To Do:
# - Connect to trigger db
# - Monitor db for changes once a minute
# - Build out offline version
# - Create a repo of code snippets to inject in generated functions
# - Manage recursion settings in file and folder records
# - Build out settings section for recursion and other settings
# - Create a .idle file and log its location
#     indicating that a terminal is idle
#     delete with bookmark usage and iterate log on terminal close
# - .on-recursion   # on r or on -r
# - .on-idle        # on b (for bump, like bump the mouse)
# - b
# - cdf
# - oo
# - on usage of above register folder, del .on-idle keep .on-recursion

########################################################################################

import os
import time
import requests
import threading
import urllib.parse
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
########################################################################################
if __name__ == '__main__': action(); _.isExit(__file__);