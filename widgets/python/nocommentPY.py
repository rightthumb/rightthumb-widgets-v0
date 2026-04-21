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
    _.switches.register( 'Clean', '--c' )


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

import io
import token
import tokenize


def strip_python_comments_and_multiline_strings(source: str):
    """
    Strip Python comments and standalone multiline string blocks
    (docstrings / multiline-comment style strings), while keeping
    real strings such as:

        x = "" "hello"" "
        data = '''world'''

    Returns:
        {
            'code': <cleaned_source>,
            'removed': [
                {
                    'kind': 'comment' | 'multiline_string',
                    'start': <absolute_char_start>,
                    'end': <absolute_char_end>,
                    'text': <removed_text>,
                    'start_row': <line>,
                    'start_col': <col>,
                    'end_row': <line>,
                    'end_col': <col>,
                },
                ...
            ]
        }
    """

    def build_line_offsets(text: str):
        offsets = [0]
        running = 0
        for line in text.splitlines(True):
            running += len(line)
            offsets.append(running)
        return offsets

    def abs_index(line_offsets, row, col):
        return line_offsets[row - 1] + col

    def is_triple_quoted_string(s: str):
        # Handles prefixes like r, u, f, b, rf, fr, rb, br, etc.
        i = 0
        while i < len(s) and s[i] in "rRuUbBfF":
            i += 1
        body = s[i:]
        return (
            body.startswith("'''") or body.startswith('"""')
        )

    def is_standalone_multiline_string(tok, prev_sig_tok, next_sig_tok):
        """
        True when STRING token looks like a docstring / multiline comment:
        - triple quoted
        - appears by itself as a statement
        """
        tok_type, tok_str, start, end, _ = tok

        if tok_type != token.STRING:
            return False

        if not is_triple_quoted_string(tok_str):
            return False

        # Must stand alone logically, not be part of assignment/call/etc.
        prev_type = prev_sig_tok.type if prev_sig_tok else None
        prev_str = prev_sig_tok.string if prev_sig_tok else None

        next_type = next_sig_tok.type if next_sig_tok else None

        prev_allows_standalone = (
            prev_sig_tok is None
            or prev_type in {
                tokenize.INDENT,
                tokenize.DEDENT,
                tokenize.NEWLINE,
                tokenize.NL,
                tokenize.ENCODING,
            }
        )

        next_allows_standalone = next_type in {
            tokenize.NEWLINE,
            tokenize.NL,
            tokenize.DEDENT,
            tokenize.ENDMARKER,
        }

        # If previous significant token is "=", "(", ",", etc., keep it.
        # That means it is being used as a real value.
        if not prev_allows_standalone:
            return False

        if not next_allows_standalone:
            return False

        return True

    def preserve_newlines_only(text: str):
        return ''.join('\n' if ch == '\n' else '' for ch in text)

    line_offsets = build_line_offsets(source)

    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))

    # Find previous/next significant token for each token index.
    significant_types_to_skip = {
        tokenize.NL,
        tokenize.NEWLINE,
        tokenize.INDENT,
        tokenize.DEDENT,
        tokenize.ENCODING,
    }

    prev_sig = [None] * len(tokens)
    next_sig = [None] * len(tokens)

    last = None
    for i, tok in enumerate(tokens):
        prev_sig[i] = last
        if tok.type not in significant_types_to_skip:
            last = tok

    nxt = None
    for i in range(len(tokens) - 1, -1, -1):
        next_sig[i] = nxt
        if tokens[i].type not in significant_types_to_skip:
            nxt = tokens[i]

    removals = []

    for i, tok in enumerate(tokens):
        tok_type, tok_str, start, end, _ = tok

        # Remove normal comments
        if tok_type == tokenize.COMMENT:
            start_abs = abs_index(line_offsets, start[0], start[1])
            end_abs = abs_index(line_offsets, end[0], end[1])

            removals.append({
                'kind': 'comment',
                'start': start_abs,
                'end': end_abs,
                'text': source[start_abs:end_abs],
                'start_row': start[0],
                'start_col': start[1],
                'end_row': end[0],
                'end_col': end[1],
            })
            continue

        # Remove standalone triple-quoted blocks (docstrings / multiline comments)
        if is_standalone_multiline_string(tok, prev_sig[i], next_sig[i]):
            start_abs = abs_index(line_offsets, start[0], start[1])
            end_abs = abs_index(line_offsets, end[0], end[1])

            removals.append({
                'kind': 'multiline_string',
                'start': start_abs,
                'end': end_abs,
                'text': source[start_abs:end_abs],
                'start_row': start[0],
                'start_col': start[1],
                'end_row': end[0],
                'end_col': end[1],
            })

    # Apply removals from end to start so indexes stay valid
    removals.sort(key=lambda x: x['start'], reverse=True)

    cleaned = source
    for item in removals:
        original = cleaned[item['start']:item['end']]
        replacement = preserve_newlines_only(original)
        cleaned = cleaned[:item['start']] + replacement + cleaned[item['end']:]

    # Return removals in forward order for readability
    removals.reverse()

    return {
        'code': cleaned,
        'removed': removals,
    }

def clean(text):
    if not _.switches.isActive('Clean'):
        return text
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        if not line.strip(): continue
        if 'print' in _.switches.value('Clean') and ( line.strip().replace(' ','') == 'print()' or line.strip().replace(' ','') == '_.pr()' ): continue
        cleaned_lines.append(line)
    return '\n'.join(cleaned_lines)
def action():
    if _.switches.isActive('Files'):
        file = _.switches.value('Files')
        source = _.getText(file)
    else:
        source = '\n'.join(_.isData(2))
    result = strip_python_comments_and_multiline_strings(source)
    print( clean(result['code'])  )


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

