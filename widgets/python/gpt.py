import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    _.switches.register('-Help-', '-h')
    _.switches.register('Prompt', '-p,-prompt')
    _.switches.register('Model', '-m,-model')
    _.switches.register('Mode', '-mode', 'chat, prompt, vision, transcribe, translate, speech, embed')
    _.switches.register('SystemPrompt', '--s,-sp,-system')
    _.switches.register('File', '-f,-file')
    _.switches.register('Voice', '-voice')
    _.switches.register('Image', '-img,-image')
    _.switches.register('Audio', '-a,-audio')
    _.switches.register('Embed', '-e,-embed')
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
_._default_settings_()



_.appInfo[focus()] = {
    'file': 'gpt.py',
    'description': 'CLI app to interact with OpenAI GPT API',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp(''),
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














def help():
    gpt = GPT()
    _.pr(_.pr(line=1), c='yellow')
    _.pr('GPT Assistant: CLI Help', c='green')
    _.pr(line=1, c='yellow')
    _.pr()

    _.pr('USAGE:', c='cyan')
    _.pr('  p gpt -p no quote prompt -m gpt-4o -mode prompt', c='white')
    _.pr('  p gpt -p prompt.txt  -m gpt-4o -mode prompt', c='white')
    _.pr('  p gpt -p instructions.txt examples.txt "prompt text in quotes if files" -m gpt-4o -mode prompt', c='white')
    _.pr()

    _.pr('MODES:', c='cyan')
    _.pr('  prompt       ', 'One-shot prompt (no memory)', c='white')
    _.pr('  chat         ', 'Conversation memory prompt', c='white')
    _.pr('  vision       ', 'Image + text input (requires -img)', c='white')
    _.pr('  transcribe   ', 'Audio-to-text transcription (requires -audio)', c='white')
    _.pr('  translate    ', 'Audio-to-translated text (requires -audio)', c='white')
    _.pr('  speech       ', 'Text-to-speech synthesis (requires -p)', c='white')
    _.pr('  embed        ', 'Get embeddings (requires -e)', c='white')
    _.pr('  models       ', 'Print available models and prices', c='white')
    _.pr()

    _.pr('SWITCHES:', c='cyan')
    _.pr('  -p,  --prompt        ', 'Input prompt text or file path', c='white')
    _.pr('  -m,  --model         ', 'Model name (e.g., gpt-4o, gpt-4o-mini)', c='white')
    _.pr('  -sp, --system        ', 'System prompt override', c='white')
    _.pr('  -img, --image        ', 'Path to image file for vision mode', c='white')
    _.pr('  -a,  --audio         ', 'Path to audio file for transcribe/translate', c='white')
    _.pr('  -voice               ', 'Voice for text-to-speech (e.g., shimmer)', c='white')
    _.pr('  -e,  --embed         ', 'String to embed using OpenAI embeddings', c='white')
    _.pr()

    _.pr('AVAILABLE MODELS:', c='cyan')
    _.pr(gpt.list_supported_models(), c='cyan')
    _.pr()
    _.pr(gpt.terminal_line('-'), c='yellow')
    _.pr('GPT class powered by OpenAI API.', c='green')
    _.pr(gpt.terminal_line('-'), c='yellow')
    _.pr('Save api key to ~/.rt/openai.key', c='purple')
    _.isExit(__file__)
















import os
# try:
#     from library.ai.gpt import  GPT # type: ignore
#except:
# from GPT import  GPT # type: ignore
# GPT = _.Import(_v.GPT,'__init__.py')
# GPT= GPT.GPT

def action():
    if _.switches.isActive('-Help-') or _.switches.isActive('Help') or len(_.switches.all()) == 0:
        help()
        return


    prompt_text = _.switches.values('Prompt') if _.switches.isActive('Prompt') else 'Share a history fact.'
    model = _.switches.value('Model') if _.switches.isActive('Model') else 'gpt-4o'
    if prompt_text == 'Share a history fact.':
        _.pr('Share a history fact.\n',c='cyan')
        model = 'gpt-4o-mini'  # Default to a smaller model for simple prompts
    mode = _.switches.value('Mode') if _.switches.isActive('Mode') else 'prompt'
    system_prompt = _.switches.value('SystemPrompt') if _.switches.isActive('SystemPrompt') else 'You are a helpful assistant.'

    # Instantiate GPT class
    gpt = _.GPT(model=model)

    if mode == 'chat':
        if prompt_text:
            _.pr(gpt.chat(prompt_text, system_prompt))
        else:
            _.pr("No prompt provided for chat mode.")
    elif mode == 'prompt':
        if prompt_text:
            # print(prompt_text)
            # return 1
            _.pr(gpt.prompt(prompt_text, system_prompt),c='yellow')
        else:
            _.pr("No prompt provided.")
    elif mode == 'vision':
        if _.switches.isActive('Image') and prompt_text:
            image_path = _.switches.value('Image')
            _.pr(gpt.vision(prompt_text, image_path))
        else:
            _.pr("-img and -prompt required for vision mode")
    elif mode == 'transcribe':
        if _.switches.isActive('Audio'):
            audio_path = _.switches.value('Audio')
            _.pr(gpt.transcribe(audio_path))
        else:
            _.pr("-audio required for transcribe mode")
    elif mode == 'translate':
        if _.switches.isActive('Audio'):
            audio_path = _.switches.value('Audio')
            _.pr(gpt.translate(audio_path))
        else:
            _.pr("-audio required for translate mode")
    elif mode == 'speech':
        if prompt_text:
            voice = _.switches.value('Voice') if _.switches.isActive('Voice') else 'alloy'
            _.pr("Output File:", gpt.speech(prompt_text, voice=voice))
        else:
            _.pr("-prompt required for speech mode")
    elif mode == 'embed':
        if _.switches.isActive('Embed'):
            text = _.switches.value('Embed')
            _.pr(gpt.embed(text))
        else:
            _.pr("-embed string required")
    else:
        _.pr("Unsupported mode. Use -mode chat|prompt|vision|transcribe|translate|speech|embed")

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)