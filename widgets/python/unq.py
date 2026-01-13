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
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )

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


#e)--> examples
########################################################################################
#n)--> start



import cmd
import json
import jmespath
import signal
import sys
from unqlite import UnQLite  # type: ignore

class UnQLiteShell(cmd.Cmd):
    prompt = 'unqlite> '

    def __init__(self, db_path='data.db'):
        super().__init__()
        self.db_path = db_path
        self.db = UnQLite(db_path)

    def do_use(self, db_path):
        """use <filename.db> — switch database file"""
        try:
            self.db = UnQLite(db_path)
            self.db_path = db_path
            print(f'Switched to {db_path}')
        except Exception as e:
            print(f'Failed to open {db_path}: {e}')

    def do_get(self, key):
        """get <key> — Retrieve and pretty-print a key's JSON value"""
        try:
            val = self.db[key]
            print(json.dumps(json.loads(val), indent=4))
        except KeyError:
            print(f'Key "{key}" not found.')
        except Exception as e:
            print(f'Error: {e}')

    def do_set(self, arg):
        """set <key> <json> — Set key to JSON data"""
        try:
            key, json_str = arg.split(' ', 1)
            self.db[key] = json.loads(json_str)
            print(f'Set key "{key}"')
        except Exception as e:
            print(f'Error: {e}')

    def do_delete(self, key):
        """delete <key> — Delete a key"""
        try:
            del self.db[key]
            print(f'Deleted key "{key}"')
        except Exception as e:
            print(f'Error: {e}')

    def do_keys(self, _):
        """keys — List all keys"""
        try:
            for key in self.db:
                print(key)
        except Exception as e:
            print(f'Error: {e}')

    def do_filter(self, line):
        """filter <key> <jmespath> — Apply JMESPath query to a key's JSON"""
        try:
            key, expr = line.split(' ', 1)
            data = json.loads(self.db[key])
            result = jmespath.search(expr.strip(), data)
            print(json.dumps(result, indent=4))
        except Exception as e:
            print(f'Error: {e}')

    def do_dump(self, _):
        """dump — Dump all keys and values as JSON"""
        output = {}
        try:
            for key in self.db:
                try:
                    output[key] = json.loads(self.db[key])
                except:
                    output[key] = self.db[key].decode('utf-8', errors='replace')
            print(json.dumps(output, indent=4))
        except Exception as e:
            print(f'Error: {e}')

    def do_export(self, filename):
        """export <file.json> — Save DB to a JSON file"""
        output = {}
        try:
            for key in self.db:
                try:
                    output[key] = json.loads(self.db[key])
                except:
                    output[key] = self.db[key].decode('utf-8', errors='replace')
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=4)
            print(f'Exported to {filename}')
        except Exception as e:
            print(f'Error: {e}')

    def do_exit(self, _): return True
    def do_EOF(self, _): return True

    def do_help(self, arg):
        """Show help for commands"""
        help_text = {
            'help':      'Show this help menu',
            'use':       'use <file.db>       — switch database file',
            'set':       'set <key> <json>    — set key to JSON data',
            'get':       'get <key>           — retrieve and pretty-print JSON',
            'delete':    'delete <key>        — delete a key',
            'keys':      'List all keys in the current database',
            'dump':      'Dump all keys and values as JSON',
            'export':    'export <file.json>  — save DB as JSON file',
            'filter':    'filter <key> <jmes> — apply JMESPath to JSON',
            'exit':      'Exit the shell',
            'EOF':       'Alias for exit (Ctrl+D)'
        }

        for cmd, desc in sorted(help_text.items()):
            print(f'{cmd:<10} {desc}')

# Ctrl+C exit handler
def handle_sigint(signum, frame):
    print("\nExiting (Ctrl+C)")
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_sigint)
    dbfile = sys.argv[1] if len(sys.argv) > 1 else 'data.db'
    UnQLiteShell(dbfile).cmdloop()





def action():
    
    pass

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

