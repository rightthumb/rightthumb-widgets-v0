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
import sys, time
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
    global appDBA;f=__.appName(appDBA,parentApp,childApp);
    if reg:__.appReg=f;
    return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################


def sw():
    pass
    #b)--> examples
    _.switches.register( 'Requests', '-r' )
    _.switches.register( 'Print', '-print' )
    #e)--> examples
    # _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



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
                        _.hp('p thisApp -file file.txt'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
                       # { 'name': 'name', 'abbreviation': 'n' },
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

_.appData[focus()] = {
        'start': __.startTime,
        'uuid': '',
        'audit': [],
        'pipe': False,
        'data': {
                    'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
                    'table': {'sent': [], 'received': [] },
        },
    }


def triggers():
    _.switches.trigger( 'Files', _.myFileLocations, vs=True )
    _.switches.trigger( 'Ago', _.timeAgo )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'URL', _.urlTrigger )
    _.switches.trigger( 'Duration', _.timeFuture )

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

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

try: import speech_recognition as sr
except: pass


def _listener_():
    global hk
    # hkr.do("beepy.note('d',3,'dotted_eigth')") # (:g e:) c,    c#, d, d#, e, f, f#, g, g#, a, a#
    # sys.exit()
    hk.beepy.note('d',3,'dotted_eigth')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if _.switches.isActive('Print'):
            print("Talk")
        # audio = r.listen(source,timeout=1)
        audio = r.listen(source)
    try:
        # beepy.note('f')
        _translate_(r.recognize_google(audio))
        # hk.beepy.note('d')
        # beepy.note('a')

    except Exception as e:
        print(e)
        pass
        if _.switches.isActive('Print'):
            print('translate failure')
        hk.beepy.note('d',4,'dotted_eigth')

def _translate_(speech):
    global hk
    if speech.lower().replace(' ','')=='andcode': speech='encode'
    # os.system('say '+speech)
    if _.switches.isActive('Print'):
        print('said:',speech)
    _.v.prompt=speech
    subject=None
    def check(tst): return tst if not subject and len(tst.split(' ')) == sum(1 for y in tst.split(' ') if ' ' + y + ' ' in ' ' + speech + ' ') else None
    def checkAll(dic):
        subject=None
        for sub in dic:
            if not subject:
                if check(sub):
                    if _.switches.isActive('Print'):
                        print(0,dic[sub])
                    subject = sub
                    if not sub in _.v.local:
                        hkr.do(dic[sub])
                    else:
                        exec(dic[sub])
                    if _.switches.isActive('Print'):
                        print(1,dic[sub])
            # if subject: print(dic[sub])
        return subject

    global dic


    subject = checkAll(dic)
    if subject:
        # hkr.do("beepy.note('d',3,'dotted_eigth')")
        run='say '+subject
        if _.switches.isActive('Print'):
            print(run)
        # os.system(run)
        hk.beepy.note('d',3,'whole')
    else:
        print('no subject')
        hk.beepy.note('d',2,'half')
        # hkr.do("beepy.note('d',2,'dotted_eigth')")
        # print('no subject')

# sub='explode'
# elif check(sub):
#     subject=sub
#     Clip.explode()

# sub='implode'
# if check(sub):
#     subject=sub
#     Clip.implode()




        
    # print(speech)




def action():
    if _.switches.isActive('Requests'):
        global dic
        table=[]
        for k in dic:
            rec={ 'request': k, 'action': dic[k] }
            if _.showLine(str(rec)):
                table.append(rec)
        _.pt(table)
    else:
        _listener_()

import os
hkr = _.regImp( __.appReg, 'hotkeys' )
hk=hkr.imp
# print(1)
# hkr.do('_test_()')
# print(2)
# sys.exit()
# import hotkeys as hk


def ai():
    global interact
    # Sally paste  convert the folling python to a single line
    prompt = _.v.prompt.replace('Sally','')
    if 'paste' in prompt:
        prompt=prompt.replace('paste','')
        _paste = _.regImp( __.appReg, '-paste' )
        lines=[]
        lines.append(prompt.strip()+': ')
        for line in _paste.imp.paste().replace('\r','').split('\n'):
            if 'python' in prompt.lower(): line=line.split('#')[0]
            if 'javascript' in prompt.lower(): line=line.split('//')[0]
            line=line.replace('    ','\t').rstrip()
            if line: lines.append(line)
        prompt = '\n'.join(lines)
    import openai

    if _.switches.isActive('Print'):
        print('_________________')
        print(prompt)
        print('_________________')
    # Apply the API key
    openai.api_key = _blowfish.decrypt('+WDUtsrHiXMJ2Rk2Z7QMSyoo+xzLW/BhSw/kTcUwPmZGQBDpZs7LcGpy2hm+rAWQ+ZtzKKLFVO8=', _vault.key() )

    # Define your prompt
    # prompt = "Write a short story about a person who finds a treasure."

    # Request a response from the API
    response = openai.Completion.create(
        # https://platform.openai.com/docs/models/codex
        # engine="code-davinci-002",
        # engine="text-davinci-002",
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the response

    interact['listen'].append({'epoch': time.time(), 'prompt': prompt, 'response': response["choices"][0]["text"]})
    _.saveTable(interact,'ai-bot-interaction.index',p=0)
    print(response["choices"][0]["text"])
    _copy = _.regImp( __.appReg, '-copy' )
    _copy.imp.copy( response["choices"][0]["text"] )


##################################################
dic = {
            'Sally': 'ai()',

            'explode': 'Clip.explode()',
            'implode': 'Clip.implode()',
            'first': 'Clip.first()',
            'lower case': 'Clip.toLower()',
            'upper case': 'Clip.toUpper()',
            'randomize case': 'Clip.toRandomCase()',

            'scrape text': 'Clip.browser_f12_tooljs_text()',
            'extract text': 'Clip.browser_f12_tooljs_text()',

            'extract table': 'Clip.browser_f12_tooljs_table()',
            'scrape table': 'Clip.browser_f12_tooljs_table()',

            'scrape table no header': 'Clip.browser_f12_tooljs_table0()',
            'extract table no header': 'Clip.browser_f12_tooljs_table0()',

            'remove duplicate spaces': 'Clip.dup_space()',

            'convert': 'Clip.auto_yaml_json_converter()',
            # 'yaml to json': 'Clip.yaml2json()',
            # 'json to yaml': 'Clip.json2yaml()',

            'strip': 'Clip.strip1()',
            'clean up': 'Clip.strip2()',

            'space to underscore': 'Clip.space_2_underscore_text()',

            'reverse lines': 'Clip.reverse_lines()',

            'double space': 'Clip.space_double()',
            'single space': 'Clip.space_single()',

            'invert quotes': 'Clip.quote_inverter()',

            'dirty eval': 'Clip.dirty_eval()',

            'build app': 'Clip.SQL_to_crud()',

            'decrypt': 'Clip.decrypt_lines()',
            'encrypt lines': 'Clip.encrypt_lines()',
            'encrypt': 'Clip.encrypt_all()',

            'remove comments and spaces': 'Clip.remove_py_comments_spaces()',
            'remove comments': 'Clip.remove_py_comments()',
            'encode': 'Clip.base64_encode()',
            'decode': 'Clip.base64_decode()',

            'math': 'Clip.math()',


}
_.v.local=['Sally']

##################################################

# Sally paste  convert the folling python to a single line


##################################################
import _rightThumb._vault as _vault
import _rightThumb._encryptString as _blowfish
interact=_.getTable('ai-bot-interaction.index')
if not 'success' in interact: interact = {'success':[],'failure':[],'chat':[]}
if not 'listen' in interact: interact['listen']=[]
########################################################################################
if __name__ == '__main__':
    #b)--> examples

    # banner.pr()
    # if len(_.switches.all())==0: banner.gossip()
    
    #e)--> examples
    action()
    _.isExit(__file__)



