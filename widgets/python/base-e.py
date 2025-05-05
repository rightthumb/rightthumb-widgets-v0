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
import sys

class Switches:
    def __init__( self, command=None, Switches=None, Triggers=None ):
        if Switches is None:
            Switches = {}
        if Triggers is None:
            Triggers = {}

        self.defaultTriggers = {
            'Ago': _.ago
        }
        self.triggers = {}
        for key in self.defaultTriggers:
            self.triggers[key] = self.defaultTriggers[key]
        for key in Triggers:
            self.triggers[key] = Triggers[key]

        self.defaultSwitches = {}

        self.switchesRegister = {}
        for key in Switches:
            self.switchesRegister[key] = Switches[key]
        for key in self.defaultSwitches:
            if key not in self.switchesRegister:
                self.switchesRegister[key] = self.defaultSwitches[key]

        if not command:
            command = sys.argv
        self.app = command[0]
        self.args = command[1:]

        self.used = {}
        self._Values = {}
        self.usage = {}
        self.instances = {}

        # Clean up switchesRegister formatting
        for key in self.switchesRegister:
            self.used[key] = False
            text = self.switchesRegister[key]
            text = text.replace(',', ' ').replace('|', ' ').replace(';', ' ')
            while '  ' in text:
                text = text.replace('  ', ' ')
            self.switchesRegister[key] = text.strip().replace(' ', ',')

        # Initialize empty value holders
        for key in self.switchesRegister:
            self._Values[key] = []

        # Build a flag lookup
        self.flag_to_key = {}
        for key, flags in self.switchesRegister.items():
            for flag in flags.split(','):
                self.flag_to_key[flag] = key

        self.parse()

    def parse( self ):
        current_switch = None
        current_key = None
        i = 0

        while i < len(self.args):
            arg = self.args[i]
            if arg in self.flag_to_key:
                current_key = self.flag_to_key[arg]
                current_switch = arg

                # Initialize instances[current_key] if needed
                if current_key not in self.instances:
                    self.used[current_key] = True
                    self.instances[current_key] = {}

                # Initialize instances[current_key][current_switch] if needed
                if current_switch not in self.instances[current_key]:
                    self.instances[current_key][current_switch] = []

                # Initialize usage[current_key] as list
                if current_key not in self.usage:
                    self.usage[current_key] = []
                if current_switch not in self.usage[current_key]:
                    self.usage[current_key].append(current_switch)

                if self._Values[current_key] == []:
                    self._Values[current_key] = True  # Assume True first
            else:
                if current_key and current_switch:
                    if self._Values[current_key] is True:
                        self._Values[current_key] = []
                    if current_key in self.triggers:
                        value = self.triggers[current_key](arg)
                    else:
                        value = arg
                    self._Values[current_key].append(value)
                    self.instances[current_key][current_switch].append(value)
            i += 1

    def isActive( self, name ):
        if not name in self.used:
            return False
        return self.used[name]
    
    def Values( self, name, instance=None ):
        if not name in self.instances:
            return []
        if instance is not None:
            if instance in self.instances[name]:
                return self.instances[name][instance]
            else:
                return []
        else:
            return self.values(name)
        

    def values( self, name ):
        if not name in self._Values:
            return []
        if self._Values[name] == True:
            return []
        return self._Values[name]

    def validate( self) :
        import json

        print('\nApp:')
        print(self.app)

        print('\nUsed:')
        print(json.dumps(self.used, indent=4))

        print('\nValues:')
        print(json.dumps(self._Values, indent=4))
        if 'Ago' in self._Values:
            for ago in self._Values['Ago']:
                print('Ago:', _.friendlyDate(ago))

        print('\nUsage:')
        print(json.dumps(self.usage, indent=4))

        print('\nInstances:')
        print(json.dumps(self.instances, indent=4))
switches = {
    'Ago': '-ago',
    'Items': '-i, -items | -item ; -it',
    'Validation': '-on -off',
    'Toggle': '-t',
    'Blank': '-b',
}
Triggers = {
    'Ago': _.ago
}
switches = Switches(0,switches,Triggers)
switches.validate()
if switches.isActive('Toggle'):
    print('Toggle is active')
# if switches.isActive('Items'):
print('Items:', switches.values('Items'))
print('Validation Values instance -on:', switches.Values('Validation', '-on'))
print('Validation Values instance -off:', switches.Values('Validation', '-off'))
    


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

