import sys, time
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;

def focus(parentApp='',childApp='',reg=True):
    global appDBA;f=__.appName(appDBA,parentApp,childApp);
    if reg:__.appReg=f;
    return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')

def sw():
    pass
    _.switches.register( 'Prompt', '-prompt' )
    _.switches.register( 'JustPrompt', '-j,-jp' )
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])

_.appInfo[focus()] = {
    'file': 'thisApp.py',
    'liveAppName': __.thisApp( __file__ ),
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'usage': [
    ],
    'relatedapps': [
    ],
    'prerequisite': [
    ],
    'examples': [
                        _.hp('p thisApp -file file.txt'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
    ],
    'aliases': [
    ],
    'notes': [
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
def _local_(do): exec(do)
_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import subprocess

interact = _.getTable('ai-bot-interaction.index')
if not 'success' in interact: interact = {'success':[],'failure':[],'chat':[]}
if not 'ai' in interact: interact['ai'] = []
_keychain = _.regImp(__.appReg, 'keychain')
import openai
import time

def install_missing_packages(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}. Error: {str(e)}")

def ai(prompt):
    max_tokens = 1024 * 2
    try:
        openai.api_key = _keychain.imp.key('open-ai-api',0)
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replaced with the newer model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            max_tokens=max_tokens,
            stop=None,
        )
        # _copy = _.regImp(__.appReg, '-copy')
        # _copy.imp.copy(response["choices"][0]["message"]["content"])
        _.pr(response["choices"][0]["message"]["content"])
        global interact
        interact['ai'].append({'epoch': time.time(), 'prompt': prompt, 'response': response["choices"][0]["message"]["content"]})
        _.saveTable(interact, 'ai-bot-interaction.index', p=0)
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error occurred: {str(e)}")
        interact['failure'].append({'epoch': time.time(), 'prompt': prompt, 'error': str(e)})
        _.saveTable(interact, 'ai-bot-interaction.index', p=0)
        print("Attempting to update OpenAI package...")
        try:
            install_missing_packages('openai')
            print("Update complete. Try again.")
        except Exception as install_error:
            print(f"Failed to update or install OpenAI package. Error: {str(install_error)}")

def action():
    prompt = ''
    if _.switches.isActive('Prompt'):
        Prompt = ' '.join(_.switches.values('Prompt'))
        Prompt = Prompt.strip()
        if not Prompt.endswith(':'): Prompt += ':'
        Prompt += '\n'
        prompt += Prompt
    if not _.switches.isActive('JustPrompt'):
        prompt += '\n'.join(_.pp())
    
    # Wrap ai execution in try-catch to handle errors and attempt installation if needed
    try:
        ai(prompt)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        print("Attempting to install any missing packages...")
        try:
            install_missing_packages('openai')
            print("Retrying after package installation...")
            ai(prompt)
        except Exception as install_error:
            print(f"Failed to install required packages. Error: {str(install_error)}")


########################################################################################
if __name__ == '__main__':
    action()
    _.isExit(__file__)