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
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')
##################################################

import re
import urllib.parse

# SECTION: Formatters

def format_phone(string, style='us-dash'):
    digits = re.sub(r'\D', '', string)
    if len(digits) == 10:
        if style == 'us-dash':
            return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
        elif style == 'us-dot':
            return f"{digits[:3]}.{digits[3:6]}.{digits[6:]}"
        elif style == 'us-parens':
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits.startswith('1'):
        return format_phone(digits[1:], style)
    return string

def format_url(url, encode=True):
    parts = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parts.query)
    base = f"{parts.scheme}://{parts.netloc}{parts.path}"
    if encode:
        encoded_query = urllib.parse.urlencode(query, doseq=True)
        return f"{base}?{encoded_query}"
    return base

def extract_url_params(url):
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.parse_qs(parsed.query)

# SECTION: Validator Class

class Validator:
    regex = {
        'email': re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$'),
        'phone': re.compile(r'^\+?[1-9]\d{1,14}$'),
        'url': re.compile(r'^(https?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[/#?]?.*$'),
        'ipv4': re.compile(r'^(\d{1,3}\.){3}\d{1,3}$'),
        'ipv6': re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'),
        'uuid': re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'),
        'date': re.compile(r'^\d{4}-\d{2}-\d{2}$'),
        'ssn': re.compile(r'^\d{3}-\d{2}-\d{4}$'),
        'hexcolor': re.compile(r'^#?[0-9a-fA-F]{6}$'),
        'zipcode_us': re.compile(r'^\d{5}(-\d{4})?$')
    }

    @classmethod
    def check(cls, kind, string):
        if kind in cls.regex:
            return bool(cls.regex[kind].match(string))
        raise ValueError(f"Unknown validator: {kind}")

    @classmethod
    def list_all(cls):
        return list(cls.regex.keys())

# SECTION: Safe Filename Utils

def make_filename_safe(name, platform='win'):
    bad_chars = {'win': r'[<>:"/\\|?*]', 'linux': r'[\\/]'}
    name = re.sub(bad_chars.get(platform, ''), '_', name)
    name = re.sub(r'\s+', '_', name)
    return name.strip('_')[:255]

# SECTION: Encode/Decode (Undoable)

def str_to_hex(string):
    return string.encode('utf-8').hex()

def hex_to_str(hex_string):
    return bytes.fromhex(hex_string).decode('utf-8', errors='ignore')

# Future expansion: add slugify, currency, hashtag, redaction, etc.

# Framework-Style Dispatcher

def fx(what, string, *args, **kwargs):
    if what == 'phone': return format_phone(string, *args, **kwargs)
    if what == 'url': return format_url(string, *args, **kwargs)
    if what == 'url-params': return extract_url_params(string)
    if what == 'safe-filename': return make_filename_safe(string, *args, **kwargs)
    if what == 'hex': return str_to_hex(string)
    if what == 'unhex': return hex_to_str(string)
    if what == 'validate': return Validator.check(*args)
    return string















# ════════════════════════════════════════════════════════════════════════════════
# URL and Crypto Utilities (JS to Python Translation)
# Provides: URL parsing, query manipulation, and salt-based XOR encryption
# ════════════════════════════════════════════════════════════════════════════════

import urllib.parse
import requests # type: ignore


class URLTools:
    def __init__(self, url=None, dic=None):
        self.url = url or ''
        self.data = dic or {}
        if self.url:
            parsed = urllib.parse.urlparse(self.url)
            self.data.update(dict(urllib.parse.parse_qsl(parsed.query)))

    def v(self, parameter=None, default=None, href=None):
        if parameter is None:
            return self.vars(href)
        return self.var(parameter, default, href)

    def vars(self, href=None):
        target = href or self.url
        parsed = urllib.parse.urlparse(target)
        return dict(urllib.parse.parse_qsl(parsed.query))

    def var(self, parameter, default=None, href=None):
        return self.vars(href).get(parameter, default)

    def add_param(self, url, param, value):
        parsed = list(urllib.parse.urlparse(url))
        query = dict(urllib.parse.parse_qsl(parsed[4]))
        query[param] = value
        parsed[4] = urllib.parse.urlencode(query)
        return urllib.parse.urlunparse(parsed)

    def dic(self, url=None):
        target = url or self.url
        parsed = urllib.parse.urlparse(target)
        protocol = parsed.scheme
        port = parsed.port or ('443' if protocol == 'https' else '80')
        host = parsed.hostname or ''
        domain = host.replace('www.', '').lower()

        params = dict(urllib.parse.parse_qsl(parsed.query))
        path = f"{host}{parsed.path}".replace('//', '/')
        folder = path.replace(domain, '')
        folder = '/'.join(folder.split('/')[:-1]).replace('//', '/')

        return {
            'href': target,
            'origin': f"{parsed.scheme}://{host}",
            'domain': domain,
            'host': host,
            'protocol': protocol,
            'folder': folder,
            'path': path,
            'port': str(port),
            'param': parsed.query,
            'params': params,
            'username': parsed.username,
            'password': parsed.password
        }

    def build_url(self):
        base = self.url.split('?')[0]
        query = urllib.parse.urlencode(self.data)
        return f"{base}?{query}" if query else base

    def get(self):
        response = requests.get(self.build_url())
        return response

    def post(self):
        response = requests.post(self.url.split('?')[0], data=self.data)
        return response


# ════════════════════════════════════════════════════════════════════════════════
# Encryption Utilities (Salt-based XOR, reversible)
# ════════════════════════════════════════════════════════════════════════════════

def crypt(salt, text):
    def text_to_chars(txt):
        return [ord(c) for c in txt]

    def byte_hex(n):
        return f"{n:02x}"

    def apply_salt(code):
        return text_to_chars(salt).__reduce__(lambda a, b: a ^ b, code)

    return ''.join(
        byte_hex(apply_salt(code))
        for code in text_to_chars(text)
    )

def decrypt(salt, encoded):
    def text_to_chars(txt):
        return [ord(c) for c in txt]

    def apply_salt(code):
        return text_to_chars(salt).__reduce__(lambda a, b: a ^ b, code)

    return ''.join(
        chr(apply_salt(int(encoded[i:i+2], 16)))
        for i in range(0, len(encoded), 2)
    )

# Example usage:
# url_tool = URLTools()
# url_tool.v("param", href="http://example.com?param=value")
# crypted = crypt('salt', 'secret')
# original = decrypt('salt', crypted)
