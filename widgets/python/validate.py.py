import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
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
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

import re

class PythonScriptValidator:
    def __init__(self, code):
        self.code = code
        self.assets = {
            'commands': [],
            'urls': [],
            'domains': [],
            'files': [],
            'aliases': [],
            'functions': [],
            'variables': []
        }
        self.index = []  # Stores open/close index pairs for constructs
        self.kind = {}   # Stores kind of construct (quote, comment, etc.)
        self.select = {} # Tracks symbols encountered
        self.dex = {}    # Detailed report of code constructs
        self.processed_code = self.code
        self.regex_shortcodes = {}
        self.regex_list = []
        self.stack = []

        self.extract_and_replace_regex()
        self.process_code()
        self.parse_assets()

    def extract_and_replace_regex(self):
        # Python uses regex, so we can handle special cases
        regex_pattern = r'\[[^\]]*\]'  # Example pattern to detect regex-like constructs in shell scripts
        self.processed_code = re.sub(regex_pattern, self.replace_regex, self.processed_code)

    def replace_regex(self, match):
        shortcode = self.generate_shortcode()
        self.regex_shortcodes[shortcode] = match.group(0)
        self.regex_list.append(match.group(0))
        return shortcode

    def generate_shortcode(self):
        return f"<regex-{len(self.regex_shortcodes)}>"

    def process_code(self):
        length = len(self.code)
        i = 0

        while i < length:
            char = self.code[i]
            if self.is_comment_start(i):
                # Handle comments
                if self.code[i:i+2] == '#':
                    close_index = self.code.find('\n', i)
                    self.index.append([i, close_index])
                    self.kind[i] = 'comment'
                    i = close_index
                    continue
            elif self.is_quote_start(char):
                # Handle quotes
                quote_type = char
                open_index = i
                self.select[open_index] = quote_type
                i += 1
                while i < length:
                    if self.code[i] == quote_type and self.code[i - 1] != '\\':
                        self.index.append([open_index, i])
                        self.kind[open_index] = 'quote'
                        self.select[i] = quote_type
                        break
                    i += 1
            elif '([{'.find(char) >= 0:
                # Handle opening brackets
                self.stack.append((char, i))
                self.select[i] = char
                self.kind[i] = 'bracket'
            elif ')]}'.find(char) >= 0:
                # Handle closing brackets
                if self.stack:
                    open_char, open_index = self.stack.pop()
                    self.index.append([open_index, i])
                    self.kind[open_index] = 'bracket'
                    self.select[i] = char
            i += 1

    def parse_assets(self):
        # Extract commands, aliases, functions, variables, etc.
        self.assets['commands'] = re.findall(r'^\s*(\w+)\s*', self.code, re.MULTILINE)
        self.assets['aliases'] = re.findall(r'alias\s+(\w+)=', self.code)
        self.assets['functions'] = re.findall(r'def\s+(\w+)\s*\(', self.code)
        self.assets['variables'] = re.findall(r'^\s*(\w+)=', self.code, re.MULTILINE)
        self.assets['urls'] = re.findall(r'(https?://[^\s]+)', self.code)
        self.assets['files'] = re.findall(r'(\./[^\s]+)', self.code)
        self.assets['domains'] = [url.split('/')[2] for url in self.assets['urls']]
        self.assets['commands'] = list(set(self.assets['commands']))
        self.assets['variables'] = list(set(self.assets['variables']))

    def is_comment_start(self, i):
        return self.code[i:i+1] == '#'

    def is_quote_start(self, char):
        return char in ['"', "'"]

    def snip(self, start, end=None):
        if end is None:
            end = self.dex.get(start, start)
        return self.code[start:end+1]

    def validate(self):
        # Here we can implement validation logic for Python syntax, regex, and other constructs
        return True




def action():
	for path in _.isData(r=1):
		code = _.getText(path,raw=True).replace('\r','')
		validator = PythonScriptValidator(code)
		_.pv(validator.assets)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);