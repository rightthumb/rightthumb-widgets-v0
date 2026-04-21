#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# String Toolkit

A modern rewrite of an older mixed string helper module.

## Goals
- Keep backward compatibility for grandfathered apps.
- Group related behavior into focused static classes.
- Make the file easier to read, extend, and maintain.
- Preserve old function names through compatibility wrappers.
- Add practical helpers commonly needed in real production apps.

## Design
The module is organized into static classes:

1. `StrConst`      - constants, char sets, regexes
2. `StrDetect`     - tests / predicates
3. `StrConvert`    - safe coercion / conversions
4. `StrTrim`       - edge cleanup / repeated token cleanup
5. `StrReplace`    - replace / remove helpers
6. `StrNormalize`  - normalization and text cleanup
7. `StrFilter`     - allowed-character filtering
8. `StrCase`       - case and naming-style transforms
9. `StrToken`      - token extraction / splitting helpers
10. `StrNamespace` - dotted namespace/path-like helpers
11. `StrLine`      - line-oriented parsing and extraction
12. `StrFormat`    - spacing / padding / presentation
13. `StrJson`      - JSON helpers and wrappers

## Backward Compatibility
Legacy function names remain available at the bottom of the file.
Each compatibility wrapper points to the new implementation and includes
an inline comment showing the old name.
'''

from __future__ import annotations

import json
import os
import platform
import random
import re
import unicodedata
from typing import Any, Iterable, Mapping, Optional, Sequence


# =============================================================================
# Constants
# =============================================================================

class StrConst:
    '''
    # StrConst

    Central home for reusable constants, character sets, and regex patterns.

    ## Why this class exists
    Older versions of this toolkit scattered globals across the module:
    `slash`, `printable`, `alphaChar`, `safeChar`, and more. This class gives
    every other helper a single source of truth.

    ## Diverse use cases
    - Build filename-safe filters.
    - Reuse visible / printable checks in validators.
    - Keep namespace matching consistent across apps.
    - Use a shared regex pattern library for performance and readability.
    '''

    SLASH = '\\' if platform.system() == 'Windows' else '/'
    NEWLINES = '\r\n'
    WHITESPACE = ' \t\n\r\x0b\x0c'

    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER = 'abcdefghijklmnopqrstuvwxyz'
    ALPHA = LOWER + UPPER
    DIGITS = '0123456789'
    ALNUM = ALPHA + DIGITS

    VISIBLE = DIGITS + ALPHA + r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    PRINTABLE = ' ' + VISIBLE + '\t\n\r\x0b\x0c'
    SAFE_CHAR = PRINTABLE  # old: safeChar
    ALPHANUMERIC = ' ' + ALNUM  # old: alphanumeric

    PRINTABLE2 = (
        PRINTABLE
        + '🧻🧪💀🦆🦉🥓🦄🦀🖕🍣🍤🍥🍡🥃🥞🐕👾🐉🐓🐋🐌🐢👽👿🥑🐡🐗💐🏹🎨🐔🐛🎯🌯📷'
        + '🛶🥕🍒🍸🍳🐲🎣🐟🦅👀🐸🤞💪💾👻🐊🍔🌭🍀🕓🦊🍟🥝🖕🐒🥞🐼📎🐧💩🍕🍍🦏🍗🌈'
        + '🐳🦑🚀🙈🙊🙉🌮🥒🐅🐯🍉🚽🍅👅🎩🍷'
    )

    NOT_FILENAME_SAFE = '/\\?%*:|"<>'  # old: notFilenameSafe
    FILENAME_SAFE = ALNUM + "-_.() "
    NAMESPACE_CHARS = ALNUM + '_.'
    SAFE = ALNUM + r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" + WHITESPACE + '¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿'
    SAFE2 = SAFE + 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'

    RX_WHITESPACE = re.compile(r'\s+')
    RX_MULTI_SPACE = re.compile(r' +')
    RX_INT = re.compile(r'^[+-]?\d+$')
    RX_FLOAT = re.compile(r'^[+-]?(?:\d+\.\d+|\d+\.\d*|\.\d+)$')
    RX_EMAIL = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$")
    RX_URL = re.compile(r'^(?:https?|ftp)://[^\s/$.?#].[^\s]*$', re.IGNORECASE)
    RX_IPV4 = re.compile(r'^(?:\d{1,3}\.){3}\d{1,3}$')
    RX_HEX = re.compile(r'^[0-9A-Fa-f]+$')
    RX_NAMESPACE = re.compile(r'^[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)+$')
    RX_WORD = re.compile(r'[A-Za-z0-9]+')
    RX_CAMEL_BREAK_1 = re.compile(r'(.)([A-Z][a-z]+)')
    RX_CAMEL_BREAK_2 = re.compile(r'([a-z0-9])([A-Z])')


# =============================================================================
# Detection
# =============================================================================

class StrDetect:
    '''
    # StrDetect

    Predicate and classification helpers.

    ## Why this class exists
    The older module mixed "check if string looks like X" functions with
    mutation functions. This class separates testing from transformation.

    ## Diverse use cases
    - Reject invalid IDs before saving.
    - Detect whether a scraped value is numeric.
    - Decide whether a field looks like an email, URL, MAC, or namespace.
    - Guard compatibility wrappers without mutating original data.
    '''

    @staticmethod
    def is_blank(value: Any) -> bool:
        return StrConvert.to_str(value).strip() == ''

    @staticmethod
    def has_alpha(value: Any) -> bool:  # old: hasAlpha
        return any(c in StrConst.ALPHA for c in StrConvert.to_str(value))

    @staticmethod
    def has_digit(value: Any) -> bool:
        return any(c.isdigit() for c in StrConvert.to_str(value))

    @staticmethod
    def has_visible(value: Any) -> bool:  # old: hasVisible
        return any(c in StrConst.VISIBLE for c in StrConvert.to_str(value))

    @staticmethod
    def has_upper(value: Any) -> bool:
        return any(c.isupper() for c in StrConvert.to_str(value))

    @staticmethod
    def has_lower(value: Any) -> bool:
        return any(c.islower() for c in StrConvert.to_str(value))

    @staticmethod
    def is_int(value: Any) -> bool:  # old: isInt
        if isinstance(value, bool):
            return False
        if isinstance(value, int):
            return True
        return bool(StrConst.RX_INT.match(StrConvert.to_str(value).strip()))

    @staticmethod
    def is_float(value: Any) -> bool:  # old: isFloat
        if isinstance(value, bool):
            return False
        if isinstance(value, float):
            return True
        text = StrConvert.to_str(value).strip()
        if StrDetect.is_int(text):
            return False
        return bool(StrConst.RX_FLOAT.match(text))

    @staticmethod
    def is_numeric_string(value: Any) -> bool:
        text = StrConvert.to_str(value).strip()
        return StrDetect.is_int(text) or StrDetect.is_float(text)

    @staticmethod
    def looks_like_email(value: Any) -> bool:
        return bool(StrConst.RX_EMAIL.match(StrConvert.to_str(value).strip()))

    @staticmethod
    def looks_like_url(value: Any) -> bool:
        return bool(StrConst.RX_URL.match(StrConvert.to_str(value).strip()))

    @staticmethod
    def looks_like_ipv4(value: Any) -> bool:
        text = StrConvert.to_str(value).strip()
        if not StrConst.RX_IPV4.match(text):
            return False
        try:
            return all(0 <= int(part) <= 255 for part in text.split('.'))
        except Exception:
            return False

    @staticmethod
    def looks_like_hex(value: Any, exact_len: Optional[int] = None) -> bool:
        text = StrConvert.to_str(value).strip()
        if exact_len is not None and len(text) != int(exact_len):
            return False
        return bool(text) and bool(StrConst.RX_HEX.match(text))

    @staticmethod
    def looks_like_mac(value: Any) -> bool:
        text = StrConvert.to_str(value).strip()
        stripped = re.sub(r'[^0-9A-Fa-f]', '', text)
        return len(stripped) == 12 and StrDetect.looks_like_hex(stripped, exact_len=12)

    @staticmethod
    def looks_like_namespace(value: Any) -> bool:
        return bool(StrConst.RX_NAMESPACE.match(StrConvert.to_str(value).strip()))


# =============================================================================
# Conversion
# =============================================================================

class StrConvert:
    '''
    # StrConvert

    Safe coercion and value conversion helpers.

    ## Why this class exists
    The older toolkit had conversion behavior scattered across utilities.
    This class provides a consistent place for "make this into a string/number/
    bool" logic.

    ## Diverse use cases
    - Coerce scraped numeric values.
    - Convert user input safely.
    - Zero-fill IDs.
    - Shuffle chars for quick randomized test strings.
    '''

    @staticmethod
    def to_str(value: Any, default: str = '') -> str:
        if value is None:
            return default
        if isinstance(value, bytes):
            try:
                return value.decode('utf-8')
            except Exception:
                try:
                    return value.decode('latin1')
                except Exception:
                    return default
        return str(value)

    @staticmethod
    def to_int(value: Any, default: Optional[int] = None) -> Optional[int]:
        if StrDetect.is_int(value):
            try:
                return int(StrConvert.to_str(value).strip())
            except Exception:
                return default
        return default

    @staticmethod
    def to_float(value: Any, default: Optional[float] = None) -> Optional[float]:
        if StrDetect.is_float(value) or StrDetect.is_int(value):
            try:
                return float(StrConvert.to_str(value).strip())
            except Exception:
                return default
        return default

    @staticmethod
    def to_number(value: Any, default: Any = None) -> Any:  # old: autoFloatInt
        if StrDetect.is_int(value):
            return int(StrConvert.to_str(value).strip())
        if StrDetect.is_float(value):
            return float(StrConvert.to_str(value).strip())
        return default if default is not None else value

    @staticmethod
    def to_bool(value: Any, default: Optional[bool] = None) -> Optional[bool]:
        if isinstance(value, bool):
            return value
        text = StrConvert.to_str(value).strip().lower()
        if text in {'1', 'true', 'yes', 'y', 'on'}:
            return True
        if text in {'0', 'false', 'no', 'n', 'off'}:
            return False
        return default

    @staticmethod
    def zero_fill(value: Any, count: int) -> str:  # old: padZeros
        return StrConvert.to_str(value).zfill(max(0, int(count)))

    @staticmethod
    def randomize_chars(chars: Any) -> str:  # old: randomStr
        items = list(StrConvert.to_str(chars))
        random.shuffle(items)
        return ''.join(items)


# =============================================================================
# Trimming
# =============================================================================

class StrTrim:
    '''
    # StrTrim

    Edge cleanup and repeated-token cleanup helpers.

    ## Why this class exists
    The old module heavily used `cleanFirst`, `cleanEnd`, `cleanBE`,
    and `replaceDuplicate`. These are core low-level tools and belong together.

    ## Diverse use cases
    - Strip repeated spaces from both ends.
    - Remove duplicated delimiters like `--`, `..`, `__`, or multiple tabs.
    - Normalize surrounding tokens before parsing.
    - Clean shell/script text line-by-line.
    '''

    @staticmethod
    def collapse_token_runs(text: Any, token: str) -> str:  # old: replaceDuplicate
        value = StrConvert.to_str(text)
        if not isinstance(token, str) or token == '':
            return value
        double = token + token
        while double in value:
            value = value.replace(double, token)
        return value

    @staticmethod
    def strip_prefix_repeat(text: Any, prefix: str) -> str:  # old: cleanFirst
        value = StrConvert.to_str(text)
        if not prefix:
            return value
        while value.startswith(prefix):
            value = value[len(prefix):]
        return value

    @staticmethod
    def strip_suffix_repeat(text: Any, suffix: str) -> str:  # old: cleanEnd / cleanLast
        value = StrConvert.to_str(text)
        if not suffix:
            return value
        while value.endswith(suffix):
            value = value[:-len(suffix)]
        return value

    @staticmethod
    def strip_both_repeated(text: Any, token: str) -> str:  # old: cleanBE
        return StrTrim.strip_prefix_repeat(
            StrTrim.strip_suffix_repeat(text, token),
            token,
        )

    @staticmethod
    def trim_whitespace_edges(text: Any) -> str:
        value = StrConvert.to_str(text)
        for ws in StrConst.WHITESPACE:
            value = StrTrim.strip_both_repeated(value, ws)
        return value

    @staticmethod
    def collapse_whitespace_runs(text: Any) -> str:
        value = StrConvert.to_str(text)
        value = re.sub(r'[ \t]+', ' ', value)
        return value


# =============================================================================
# Replacement
# =============================================================================

class StrReplace:
    '''
    # StrReplace

    General replace/remove helpers.

    ## Why this class exists
    Replacement is different from trimming. These are broad "change this to that"
    operations including regex-capable helpers.

    ## Diverse use cases
    - Replace tabs with spaces.
    - Remove many bad sequences at once.
    - Apply a cleanup map from imported config.
    - Use regex replacements for structured patterns.
    '''

    @staticmethod
    def replace_all(text: Any, old: str, new: str) -> str:  # old: replaceAll
        value = StrConvert.to_str(text)
        if not old:
            return value
        return value.replace(old, new)

    @staticmethod
    def clean_all(text: Any, old: str, new: str) -> str:  # old: cleanAll
        value = StrConvert.to_str(text)
        if not old:
            return value
        while old in value:
            value = value.replace(old, new)
        return value

    @staticmethod
    def remove_all(text: Any, old: str) -> str:  # old: removeAll
        return StrReplace.replace_all(text, old, '')

    @staticmethod
    def replace_many(text: Any, replacements: Mapping[str, str]) -> str:
        value = StrConvert.to_str(text)
        for old, new in (replacements or {}).items():
            value = value.replace(StrConvert.to_str(old), StrConvert.to_str(new))
        return value

    @staticmethod
    def remove_many(text: Any, items: Iterable[str]) -> str:
        value = StrConvert.to_str(text)
        for item in items or []:
            value = value.replace(StrConvert.to_str(item), '')
        return value

    @staticmethod
    def replace_map(text: Any, replacements: Mapping[str, str]) -> str:
        return StrReplace.replace_many(text, replacements)

    @staticmethod
    def regex_replace(text: Any, pattern: str, repl: str, flags: int = 0) -> str:
        return re.sub(pattern, repl, StrConvert.to_str(text), flags=flags)

    @staticmethod
    def regex_remove(text: Any, pattern: str, flags: int = 0) -> str:
        return re.sub(pattern, '', StrConvert.to_str(text), flags=flags)


# =============================================================================
# Normalization
# =============================================================================

class StrNormalize:
    '''
    # StrNormalize

    Higher-level normalization and cleanup helpers.

    ## Why this class exists
    The old module had many overlapping functions for weird text:
    latin-1, escaped bytes, odd punctuation, duplicated spaces, shell text,
    line stripping, and general cleanup. This class is the new central home
    for that behavior.

    ## Diverse use cases
    - Clean copied browser text.
    - Normalize shell/file content before processing.
    - Fix OCR-ish punctuation and smart quotes.
    - Collapse ugly whitespace in logs or scraped pages.
    - Sanitize line-oriented blocks before using `StrLine`.
    '''

    SMART_CHAR_MAP = {
        '\u2018': "'",
        '\u2019': "'",
        '\u201a': "'",
        '\u201b': "'",
        '\u2032': "'",
        '\u2033': '"',
        '\u201c': '"',
        '\u201d': '"',
        '\u201e': '"',
        '\u201f': '"',
        '\u00a0': ' ',
        '\u2010': '-',
        '\u2011': '-',
        '\u2012': '-',
        '\u2013': '-',
        '\u2014': '-',
        '\u2015': '-',
        '\u2026': '...',
    }

    UNDERSCORE_LIKE = ['\u005F', '\uFF3F', '\u2017', '\u203E', '\u0332', '_']  # old: underscore inputs

    @staticmethod
    def printable_only(text: Any) -> str:  # old: printClean
        value = StrConvert.to_str(text)
        return ''.join(c for c in value if c in StrConst.PRINTABLE)

    @staticmethod
    def minimal_clean(text: Any) -> str:  # old: minimalistClean
        value = StrConvert.to_str(text)
        result = ''.join(c if c in StrConst.PRINTABLE else ' ' for c in value)
        result = StrTrim.collapse_token_runs(result, ' ')
        return StrTrim.strip_both_repeated(result, ' ')

    @staticmethod
    def normalize_newlines(text: Any) -> str:
        value = StrConvert.to_str(text)
        value = value.replace('\r\n', '\n').replace('\r', '\n')
        return value

    @staticmethod
    def normalize_quotes(text: Any) -> str:
        value = StrConvert.to_str(text)
        for old, new in StrNormalize.SMART_CHAR_MAP.items():
            if old in {'\u2018', '\u2019', '\u201a', '\u201b', '\u2032', '\u2033', '\u201c', '\u201d', '\u201e', '\u201f'}:
                value = value.replace(old, new)
        return value

    @staticmethod
    def normalize_dashes(text: Any) -> str:
        value = StrConvert.to_str(text)
        for old, new in StrNormalize.SMART_CHAR_MAP.items():
            if old in {'\u2010', '\u2011', '\u2012', '\u2013', '\u2014', '\u2015'}:
                value = value.replace(old, new)
        return value

    @staticmethod
    def normalize_unicode(text: Any, form: str = 'NFKC') -> str:
        return unicodedata.normalize(form, StrConvert.to_str(text))

    @staticmethod
    def normalize_whitespace(text: Any, keep_newlines: bool = False) -> str:
        value = StrConvert.to_str(text)
        if keep_newlines:
            value = StrNormalize.normalize_newlines(value)
            lines = []
            for line in value.split('\n'):
                line = re.sub(r'[ \t]+', ' ', line).strip()
                lines.append(line)
            return '\n'.join(lines)
        value = StrConst.RX_WHITESPACE.sub(' ', value)
        return value.strip()

    @staticmethod
    def character_clean(text: Any) -> str:  # old: characterClean
        value = StrConvert.to_str(text)
        value = StrNormalize.normalize_quotes(value)
        value = StrNormalize.normalize_dashes(value)
        value = value.replace('\u2026', '...')
        return value

    @staticmethod
    def replace_underscore_like(text: Any, replacement: str = ' ') -> str:  # old: underscore
        value = StrConvert.to_str(text)
        for ch in StrNormalize.UNDERSCORE_LIKE:
            value = value.replace(ch, replacement)
        return value

    @staticmethod
    def clean_latin1(text: Any) -> str:  # old: clean_latin1
        value = StrConvert.to_str(text)
        if isinstance(text, bytes):
            try:
                return text.decode('latin1')
            except Exception:
                return StrConvert.to_str(text)
        try:
            raw = value.encode('latin1', 'ignore').decode('latin1')
        except Exception:
            raw = value
        return StrNormalize.character_clean(raw)

    @staticmethod
    def clean_char(text: Any) -> str:  # old: cleanChar
        return StrNormalize.clean_latin1(text)

    @staticmethod
    def char_fix(text: Any) -> str:  # old: charFix
        value = StrConvert.to_str(text)
        try:
            value = bytes(value, 'utf-8').decode('unicode_escape')
        except Exception:
            pass
        return StrNormalize.character_clean(value)

    @staticmethod
    def total_clean(text: Any) -> str:  # old: totalClean
        value = StrConvert.to_str(text).replace('\n', '').replace('\r', '')
        value = StrTrim.collapse_token_runs(value, ' ')
        value = StrTrim.collapse_token_runs(value, '\t')
        value = StrTrim.strip_both_repeated(value, ' ')
        value = StrTrim.strip_both_repeated(value, '\t')
        return value

    @staticmethod
    def remove_outer_spaces_around_token(text: Any, token: str) -> str:  # old: spaceba
        value = StrConvert.to_str(text)
        token = StrConvert.to_str(token)
        if not token:
            return value
        limit = 1000
        i = 0
        while (f' {token}' in value or f'{token} ' in value) and i < limit:
            i += 1
            value = value.replace(f' {token}', token)
            value = value.replace(f'{token} ', token)
        return value

    @staticmethod
    def make_printable(text: Any, replace_with: str = ' ', appropriate: Optional[str] = None) -> str:  # old: makePrintable
        value = StrConvert.to_str(text)
        allowed = appropriate if appropriate is not None else StrConst.PRINTABLE
        result = ''.join(c if c in allowed else replace_with for c in value)
        result = StrTrim.collapse_token_runs(result, replace_with)
        return StrTrim.strip_both_repeated(result, replace_with)

    @staticmethod
    def cleanup_string(text: Any, before_after: bool = True) -> str:  # old: cleanupString / cleanupString0
        value = StrConvert.to_str(text)
        value = value.replace('\n', ' ').replace('\t', ' ')
        value = StrTrim.collapse_token_runs(value, ' ')
        value = StrTrim.trim_whitespace_edges(value)
        value = StrNormalize.character_clean(value)
        if '(' in value:
            parts = value.split('(')
            value = parts[0] if before_after else parts[-1]
        if '/' in value:
            value = value.split('/')[0]
        return value.strip()

    @staticmethod
    def trim(text: Any) -> str:  # old: trim
        return StrTrim.trim_whitespace_edges(text)

    @staticmethod
    def no_whitespace(text: Any) -> str:  # old: nows
        value = StrConvert.to_str(text)
        for ws in StrConst.WHITESPACE:
            value = value.replace(ws, '')
        return value

    @staticmethod
    def shell_text(text: Any) -> str:  # old: sh
        value = StrConvert.to_str(text)
        if os.path.isfile(value):
            try:
                with open(value, 'r', encoding='utf-8', errors='ignore') as fh:
                    value = fh.read()
            except Exception:
                pass
        value = value.replace('\r', '').replace(chr(27), '')
        value = StrTrim.strip_both_repeated(value, '\n')
        lines = []
        for line in value.split('\n'):
            line = line.rstrip(' \t')
            if not line.replace(' ', '').replace('\t', ''):
                line = ''
            lines.append(line)
        value = '\n'.join(lines)
        value = StrTrim.strip_both_repeated(value, '\n')
        return value

    @staticmethod
    def shell_text_tabs(text: Any) -> str:  # old: sh2
        value = StrConvert.to_str(text)
        if os.path.isfile(value):
            try:
                with open(value, 'r', encoding='utf-8', errors='ignore') as fh:
                    value = fh.read()
            except Exception:
                pass
        value = value.replace('\r', '').replace(chr(27), '')
        value = value.replace('\t', '    ')
        value = value.replace('    ', '\t')
        value = value.replace(' \n', '\n')
        return StrTrim.strip_both_repeated(value, '\n')


# =============================================================================
# Filtering
# =============================================================================

class StrFilter:
    '''
    # StrFilter

    Allowed-character filtering and sanitization helpers.

    ## Why this class exists
    The old module had many variants like `totalStrip*`, `removeNonNumber`,
    `filenameSafe`, and `stripNonAlphaNumaric`. This class gathers those
    together into a predictable toolkit.

    ## Diverse use cases
    - Strip a value down to digits only.
    - Make a filename safe across platforms.
    - Keep only alpha or alpha+space characters.
    - Build slugs, safe namespace segments, and cleaned form data.
    '''

    @staticmethod
    def keep_chars(text: Any, allowed: str, replace_with: str = '') -> str:
        value = StrConvert.to_str(text)
        return ''.join(c if c in allowed else replace_with for c in value)

    @staticmethod
    def drop_chars(text: Any, blocked: str) -> str:
        value = StrConvert.to_str(text)
        return ''.join(c for c in value if c not in blocked)

    @staticmethod
    def keep_printable(text: Any, replace_with: str = ' ') -> str:
        return StrNormalize.make_printable(text, replace_with=replace_with, appropriate=StrConst.PRINTABLE)

    @staticmethod
    def keep_ascii(text: Any, replace_with: str = '') -> str:
        value = StrConvert.to_str(text)
        return ''.join(c if ord(c) < 128 else replace_with for c in value)

    @staticmethod
    def keep_digits(text: Any) -> str:  # old: removeNonNumber
        value = StrConvert.to_str(text)
        return ''.join(c for c in value if c.isdigit())

    @staticmethod
    def keep_digits_dash(text: Any) -> str:  # old: onlyDigits / onlyDigits2
        value = StrNormalize.character_clean(StrConvert.to_str(text)).replace('–', '-')
        return ''.join(c for c in value if c in '0123456789-')

    @staticmethod
    def keep_alpha(text: Any) -> str:  # old: removeNonAlpha
        value = StrConvert.to_str(text)
        return ''.join(c for c in value if c.isalpha())

    @staticmethod
    def keep_alpha_space(text: Any) -> str:  # old: removeNonAlpha2
        value = StrConvert.to_str(text)
        return ''.join(c for c in value if c.isalpha() or c == ' ')

    @staticmethod
    def keep_alnum(text: Any, also: str = '') -> str:  # old: stripNonAlphaNumaric
        value = StrConvert.to_str(text)
        allowed = StrConst.ALNUM + also
        result = ''.join(c if c in allowed else ' ' for c in value)
        result = StrTrim.collapse_token_runs(result, ' ')
        return StrTrim.strip_both_repeated(result, ' ')

    @staticmethod
    def keep_alnum_space(text: Any, also: str = '') -> str:
        return StrFilter.keep_alnum(text, also=' ' + also)

    @staticmethod
    def basic(text: Any) -> str:  # old: basic
        value = re.sub(r'([^\s\w]|_)+', '', StrConvert.to_str(text))
        value = StrTrim.collapse_token_runs(value, ' ')
        value = StrTrim.strip_both_repeated(value, ' ')
        return value

    @staticmethod
    def total_strip(text: Any, allowed: str) -> str:
        value = StrConvert.to_str(text)
        section = []
        for word in value.split():
            section.append(''.join(c for c in word if c in allowed))
        return ' '.join(x for x in section if x != '').strip()

    @staticmethod
    def total_strip_default(text: Any) -> str:  # old: totalStrip
        return StrFilter.total_strip(text, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:\'#"`')

    @staticmethod
    def total_strip_alnum(text: Any, add: str = '') -> str:  # old: totalStrip1b
        return StrFilter.total_strip(StrConvert.to_str(text), ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + add)

    @staticmethod
    def total_strip_dash(text: Any) -> str:  # old: totalStrip2
        return StrFilter.total_strip(text, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-')

    @staticmethod
    def total_strip_dash_underscore_space(text: Any) -> str:  # old: totalStrip2b
        return StrFilter.total_strip(text, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_ ')

    @staticmethod
    def total_strip_dash_comma(text: Any) -> str:  # old: totalStrip3
        return StrFilter.total_strip(text, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-,')

    @staticmethod
    def total_strip_digits(text: Any) -> str:  # old: totalStrip4
        return StrFilter.total_strip(text, '0123456789')

    @staticmethod
    def total_strip_extended(text: Any) -> str:  # old: totalStrip5 / totalStrip6 / totalStrip8
        value = StrNormalize.character_clean(StrReplace.remove_many(StrConvert.to_str(text), ['\n', '\r']))
        return StrFilter.total_strip(value, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:\'#"`()')

    @staticmethod
    def total_strip_dot_from_underscores(text: Any) -> str:  # old: totalStrip7 / totalStrip9
        value = StrReplace.remove_many(StrConvert.to_str(text), ['\n', '\r'])
        value = StrNormalize.replace_underscore_like(value)
        result = ''.join(c if c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.' else ' ' for c in value)
        result = StrTrim.strip_both_repeated(result, ' ')
        result = StrTrim.collapse_token_runs(result, ' ')
        return result

    @staticmethod
    def remove_unsafe(text: Any) -> str:  # old: removeUnsave
        value = StrConvert.to_str(text)
        return ''.join(c for c in value if c in StrConst.SAFE_CHAR)

    @staticmethod
    def filename_safe(
        filename: Any,
        collapse_spaces: bool = True,
        replace_invalid_with: str = ' ',
        whitelist: Optional[str] = None,
        char_limit: int = 255,
    ) -> str:  # old: filenameSafe / clean_filename
        value = StrConvert.to_str(filename)
        whitelist = whitelist or (StrConst.FILENAME_SAFE + "%")
        value = unicodedata.normalize('NFKD', value).encode('ASCII', 'ignore').decode()

        cleaned = []
        for c in value:
            if c in whitelist and c not in StrConst.NOT_FILENAME_SAFE:
                cleaned.append(c)
            else:
                cleaned.append(replace_invalid_with)

        value = ''.join(cleaned)
        if collapse_spaces:
            value = StrTrim.collapse_token_runs(value, replace_invalid_with)
        value = StrTrim.strip_both_repeated(value, replace_invalid_with)
        return value[:char_limit]

    @staticmethod
    def path_safe_segment(text: Any) -> str:
        return StrFilter.filename_safe(text, collapse_spaces=True, replace_invalid_with=' ')

    @staticmethod
    def slug(text: Any, sep: str = '-') -> str:
        value = StrNormalize.normalize_unicode(text)
        value = value.encode('ascii', 'ignore').decode('ascii')
        value = value.lower()
        value = re.sub(r'[^a-z0-9]+', sep, value)
        value = StrTrim.collapse_token_runs(value, sep)
        value = StrTrim.strip_both_repeated(value, sep)
        return value


# =============================================================================
# Case conversion
# =============================================================================

class StrCase:
    '''
    # StrCase

    Case and naming-style transformations.

    ## Why this class exists
    These helpers are useful across config systems, code generation, filenames,
    and internal keys. They were not strongly represented in the old module,
    but they belong in a serious string toolkit.

    ## Diverse use cases
    - Convert labels into config keys.
    - Turn user-facing titles into slugs or snake_case.
    - Normalize dynamic field names for generated code.
    '''

    @staticmethod
    def _split_words(text: Any) -> list[str]:
        value = StrConvert.to_str(text)
        value = StrConst.RX_CAMEL_BREAK_1.sub(r'\1 \2', value)
        value = StrConst.RX_CAMEL_BREAK_2.sub(r'\1 \2', value)
        value = re.sub(r'[^A-Za-z0-9]+', ' ', value)
        return [w for w in value.strip().split() if w]

    @staticmethod
    def snake(text: Any) -> str:
        return '_'.join(w.lower() for w in StrCase._split_words(text))

    @staticmethod
    def kebab(text: Any) -> str:
        return '-'.join(w.lower() for w in StrCase._split_words(text))

    @staticmethod
    def camel(text: Any) -> str:
        words = StrCase._split_words(text)
        if not words:
            return ''
        return words[0].lower() + ''.join(w.capitalize() for w in words[1:])

    @staticmethod
    def pascal(text: Any) -> str:
        return ''.join(w.capitalize() for w in StrCase._split_words(text))

    @staticmethod
    def title_words(text: Any) -> str:
        return ' '.join(w.capitalize() for w in StrCase._split_words(text))


# =============================================================================
# Token helpers
# =============================================================================

class StrToken:
    '''
    # StrToken

    Small token and substring extraction helpers.

    ## Why this class exists
    These are simple but common operations that do not belong buried inside
    other cleanup functions.

    ## Diverse use cases
    - Get the text before or after a delimiter.
    - Pull content between markers.
    - Split and clean user-entered CSV-ish values.
    - Chunk strings for display, grouping, or IDs.
    '''

    @staticmethod
    def before(text: Any, needle: str, default: str = '') -> str:
        value = StrConvert.to_str(text)
        return value.split(needle, 1)[0] if needle in value else default

    @staticmethod
    def after(text: Any, needle: str, default: str = '') -> str:
        value = StrConvert.to_str(text)
        return value.split(needle, 1)[1] if needle in value else default

    @staticmethod
    def between(text: Any, left: str, right: str, default: str = '') -> str:
        value = StrConvert.to_str(text)
        if left not in value or right not in value:
            return default
        try:
            return value.split(left, 1)[1].split(right, 1)[0]
        except Exception:
            return default

    @staticmethod
    def between_markers(text: Any, start: str, end: str, default: str = '') -> str:
        return StrToken.between(text, start, end, default=default)

    @staticmethod
    def split_and_clean(text: Any, sep: str = ',', keep_blank: bool = False) -> list[str]:
        value = StrConvert.to_str(text)
        out = []
        for part in value.split(sep):
            part = StrNormalize.normalize_whitespace(part)
            if part or keep_blank:
                out.append(part)
        return out

    @staticmethod
    def words(text: Any) -> list[str]:
        return StrConst.RX_WORD.findall(StrConvert.to_str(text))

    @staticmethod
    def unique_words(text: Any, lower: bool = True) -> list[str]:
        items = StrToken.words(text)
        if lower:
            items = [w.lower() for w in items]
        seen = set()
        out = []
        for item in items:
            if item not in seen:
                seen.add(item)
                out.append(item)
        return out

    @staticmethod
    def chunk(text: Any, size: int) -> list[str]:
        value = StrConvert.to_str(text)
        size = max(1, int(size))
        return [value[i:i + size] for i in range(0, len(value), size)]


# =============================================================================
# Namespace helpers
# =============================================================================

class StrNamespace:
    '''
    # StrNamespace

    Helpers for dotted namespaces and namespace-like tokens.

    ## Why this class exists
    You mentioned namespace path processing as a real use case. This class
    promotes it from a one-off helper into a supported part of the toolkit.

    ## Diverse use cases
    - Extract `app.module.func` tokens from raw text.
    - Match an exact namespace or a child namespace.
    - Check whether `abc.def` belongs under `abc`.
    - Normalize dotted references from logs, configs, and docs.
    '''

    @staticmethod
    def extract_namespace_token(app: Any, text: Any) -> Optional[str]:  # old: namespace
        prefix = StrConvert.to_str(app).rstrip('.') + '.'
        cleaned = StrNormalize.make_printable(text, replace_with=' ', appropriate=StrConst.NAMESPACE_CHARS)
        for token in cleaned.split():
            if token.startswith(prefix):
                return token
        return None

    @staticmethod
    def split_namespace(text: Any) -> list[str]:
        value = StrConvert.to_str(text).strip('.')
        return [part for part in value.split('.') if part]

    @staticmethod
    def namespace_depth(text: Any) -> int:
        return len(StrNamespace.split_namespace(text))

    @staticmethod
    def ensure_suffix_dot(text: Any) -> str:
        value = StrConvert.to_str(text).rstrip('.')
        return value + '.'

    @staticmethod
    def startswith_namespace(value: Any, parent: Any) -> bool:
        value_s = StrConvert.to_str(value).strip()
        parent_s = StrNamespace.ensure_suffix_dot(parent)
        return value_s.startswith(parent_s)

    @staticmethod
    def exact_or_child_namespace(value: Any, parent: Any) -> bool:
        value_s = StrConvert.to_str(value).strip().rstrip('.')
        parent_s = StrConvert.to_str(parent).strip().rstrip('.')
        return value_s == parent_s or StrNamespace.startswith_namespace(value_s, parent_s)

    @staticmethod
    def path_or_namespace_match(value: Any, root: Any, starts_with: bool = True) -> bool:
        value_s = StrConvert.to_str(value).strip()
        root_s = StrConvert.to_str(root).strip().rstrip('.')
        if starts_with:
            return value_s == root_s or value_s.startswith(root_s + '.')
        return value_s == root_s


# =============================================================================
# Line-based helpers
# =============================================================================

class StrLine:
    '''
    # StrLine

    Line-oriented processing and extraction helpers.

    ## Why this class exists
    This class merges the spirit of your newer line-based scraping helper into
    the larger string toolkit. It is useful for copied tickets, OCR, notes,
    logs, scraped text, and field extraction.

    ## Diverse use cases
    - Get the next non-empty line after "Address".
    - Pull blocks after "Job Info".
    - Extract field maps from copied work-order text.
    - Build quick parsers for semi-structured plain text.
    '''

    @staticmethod
    def lines(text: Any, keep_empty: bool = False, collapse_spaces: bool = True) -> list[str]:
        raw = StrNormalize.normalize_newlines(text)
        out = []
        for line in raw.split('\n'):
            val = StrConvert.to_str(line)
            if collapse_spaces:
                val = StrNormalize.normalize_whitespace(val, keep_newlines=False)
            else:
                val = val.strip()
            if keep_empty or val != '':
                out.append(val)
        return out

    @staticmethod
    def non_empty_lines(text: Any) -> list[str]:
        return StrLine.lines(text, keep_empty=False, collapse_spaces=True)

    @staticmethod
    def find_indexes(
        text_or_lines: Any,
        needle: str,
        case_sensitive: bool = False,
        exact: bool = False,
    ) -> list[int]:  # old: find_line_indexes
        lines = text_or_lines if isinstance(text_or_lines, list) else StrLine.lines(text_or_lines, keep_empty=False)
        result = []
        n = needle if case_sensitive else StrConvert.to_str(needle).lower()
        for i, line in enumerate(lines):
            x = line if case_sensitive else line.lower()
            if (x == n) if exact else (n in x):
                result.append(i)
        return result

    @staticmethod
    def first_index(
        text_or_lines: Any,
        needle: str,
        case_sensitive: bool = False,
        exact: bool = False,
    ) -> Optional[int]:
        indexes = StrLine.find_indexes(text_or_lines, needle, case_sensitive=case_sensitive, exact=exact)
        return indexes[0] if indexes else None

    @staticmethod
    def next_non_empty_after(
        text_or_lines: Any,
        needle: str,
        case_sensitive: bool = False,
        exact: bool = False,
        default: Any = None,
    ) -> Any:
        lines = text_or_lines if isinstance(text_or_lines, list) else StrLine.lines(text_or_lines, keep_empty=True, collapse_spaces=False)
        idx = StrLine.first_index(lines, needle, case_sensitive=case_sensitive, exact=exact)
        if idx is None:
            return default
        for i in range(idx + 1, len(lines)):
            val = StrNormalize.normalize_whitespace(lines[i])
            if val != '':
                return val
        return default

    @staticmethod
    def non_empty_after(
        text_or_lines: Any,
        needle: str,
        count: int = 1,
        case_sensitive: bool = False,
        exact: bool = False,
    ) -> list[str]:  # old: non_empty_lines_after
        lines = text_or_lines if isinstance(text_or_lines, list) else StrLine.lines(text_or_lines, keep_empty=True, collapse_spaces=False)
        idx = StrLine.first_index(lines, needle, case_sensitive=case_sensitive, exact=exact)
        if idx is None:
            return []
        result = []
        for i in range(idx + 1, len(lines)):
            val = StrNormalize.normalize_whitespace(lines[i])
            if val != '':
                result.append(val)
                if len(result) >= count:
                    break
        return result

    @staticmethod
    def line_offsets_after(
        text_or_lines: Any,
        start_string: str,
        offsets: Sequence[int],
        output: str = 'list',
        glue: str = '\n',
        case_sensitive: bool = False,
        exact: bool = False,
    ) -> Any:
        lines = text_or_lines if isinstance(text_or_lines, list) else StrLine.lines(text_or_lines, keep_empty=True, collapse_spaces=False)
        idx = StrLine.first_index(lines, start_string, case_sensitive=case_sensitive, exact=exact)
        if idx is None:
            return [] if output == 'list' else ''
        values = []
        for off in offsets:
            pos = idx + int(off)
            if 0 <= pos < len(lines):
                val = StrNormalize.normalize_whitespace(lines[pos])
                if val != '':
                    values.append(val)
        return glue.join(values) if output == 'string' else values

    @staticmethod
    def block_after_until_blank(
        text_or_lines: Any,
        start_string: str,
        include_start: bool = False,
        case_sensitive: bool = False,
        exact: bool = False,
    ) -> list[str]:  # old: all_after_until_blank
        lines = text_or_lines if isinstance(text_or_lines, list) else StrLine.lines(text_or_lines, keep_empty=True, collapse_spaces=False)
        idx = StrLine.first_index(lines, start_string, case_sensitive=case_sensitive, exact=exact)
        if idx is None:
            return []
        out = []
        start = idx if include_start else idx + 1
        for i in range(start, len(lines)):
            val = StrNormalize.normalize_whitespace(lines[i])
            if val == '':
                if out:
                    break
                continue
            out.append(val)
        return out

    @staticmethod
    def key_value_by_next_line(
        text_or_lines: Any,
        keys: Sequence[str],
        exact: bool = False,
        case_sensitive: bool = False,
    ) -> dict[str, Any]:
        result = {}
        for key in keys:
            result[key] = StrLine.next_non_empty_after(
                text_or_lines,
                key,
                case_sensitive=case_sensitive,
                exact=exact,
                default=None,
            )
        return result

    @staticmethod
    def collect_fields(text_or_lines: Any, field_map: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
        lines = text_or_lines if isinstance(text_or_lines, list) else StrLine.lines(text_or_lines, keep_empty=True, collapse_spaces=False)
        result: dict[str, Any] = {}

        for out_key, spec in (field_map or {}).items():
            mode = spec.get('mode', 'next')
            after = spec.get('after')
            exact = spec.get('exact', False)
            case_sensitive = spec.get('caseSensitive', False)
            val: Any = None

            if mode == 'next':
                val = StrLine.next_non_empty_after(
                    lines,
                    after,
                    case_sensitive=case_sensitive,
                    exact=exact,
                    default=spec.get('default'),
                )
            elif mode == 'offsets':
                val = StrLine.line_offsets_after(
                    lines,
                    after,
                    spec.get('offsets', []),
                    output=spec.get('output', 'list'),
                    glue=spec.get('glue', '\n'),
                    case_sensitive=case_sensitive,
                    exact=exact,
                )
            elif mode == 'block':
                val = StrLine.block_after_until_blank(
                    lines,
                    after,
                    include_start=spec.get('includeStart', False),
                    case_sensitive=case_sensitive,
                    exact=exact,
                )
                if spec.get('output') == 'string':
                    val = spec.get('glue', '\n').join(val)

            if spec.get('numeric') and val is not None:
                if not StrDetect.is_int(val):
                    val = spec.get('default')

            result[out_key] = val

        return result


# =============================================================================
# Formatting
# =============================================================================

class StrFormat:
    '''
    # StrFormat

    Presentation and spacing helpers.

    ## Why this class exists
    These functions are useful, but they do not belong mixed in with cleanup,
    parsing, or validation. They are display-oriented helpers.

    ## Diverse use cases
    - Pad text for tables.
    - Add margins to blocks.
    - Indent log output.
    - Keep backward compatibility for `sp` and `es`.
    '''

    @staticmethod
    def spaces(count: int, token: str = ' ') -> str:  # old: sp
        count = max(0, int(count))
        return token * count

    @staticmethod
    def indent(text: Any, count: int = 4, token: str = ' ') -> str:
        prefix = token * max(0, int(count))
        return '\n'.join(prefix + line for line in StrConvert.to_str(text).splitlines())

    @staticmethod
    def pad_left(text: Any, width: int, fill: str = ' ') -> str:
        return StrConvert.to_str(text).rjust(width, fill)

    @staticmethod
    def pad_right(text: Any, width: int, fill: str = ' ') -> str:
        return StrConvert.to_str(text).ljust(width, fill)

    @staticmethod
    def center_lines(text: Any, width: int, fill: str = ' ') -> str:
        return '\n'.join(StrConvert.to_str(line).center(width, fill) for line in StrConvert.to_str(text).splitlines())

    @staticmethod
    def margin_block(text: Any, margin: int | str = '', border: str = '') -> str:  # old: es
        value = text if isinstance(text, str) else '\n'.join(text) if isinstance(text, list) else StrConvert.to_str(text)
        margin_s = StrFormat.spaces(margin) if isinstance(margin, int) else StrConvert.to_str(margin)
        border_s = StrFormat.spaces(border) if isinstance(border, int) else StrConvert.to_str(border)
        lines = value.split('\n')
        width = max((len(line) for line in lines), default=0)
        out = []
        for line in lines:
            out.append(f'{border_s}{margin_s}{line.ljust(width)}{margin_s}{border_s}')
        return '\n'.join(out)


# =============================================================================
# JSON
# =============================================================================

class StrJson:
    '''
    # StrJson

    JSON parsing and convenience wrappers.

    ## Why this class exists
    Your older toolkit used lightweight wrapper classes around strings, dicts,
    and lists. This class modernizes JSON parsing while still allowing wrapper
    behavior for old code.

    ## Diverse use cases
    - Parse JSON blobs from scraped text or config files.
    - Pretty-print nested dict/list data.
    - Keep old `.string()` and `.inline()` patterns alive.
    '''

    @staticmethod
    def parse_json(text: Any, default: Any = None) -> Any:
        try:
            return json.loads(StrConvert.to_str(text))
        except Exception:
            return default

    @staticmethod
    def dumps_pretty(value: Any, sort_keys: bool = False) -> str:
        return json.dumps(value, indent=4, sort_keys=sort_keys, ensure_ascii=False)

    @staticmethod
    def dumps_inline(value: Any, sort_keys: bool = False) -> str:
        return json.dumps(value, sort_keys=sort_keys, ensure_ascii=False)

    class st(str):
        '''
        # StrJson.st

        Backward-compatible string wrapper.

        ## Use cases
        - Chain small legacy-style helpers.
        - Parse JSON into wrapper dict/list objects.
        - Keep grandfathered code working with minimal changes.
        '''

        def sh(self): return StrJson.st(StrNormalize.shell_text(self))
        def all(self, a, b): return StrJson.st(StrReplace.replace_all(self, a, b))
        def cleanAll(self, a, b): return StrJson.st(StrReplace.clean_all(self, a, b))
        def dup(self, a): return StrJson.st(StrTrim.collapse_token_runs(self, a))
        def be(self, a): return StrJson.st(StrTrim.strip_both_repeated(self, a))
        def b(self, a): return StrJson.st(StrTrim.strip_prefix_repeat(self, a))
        def e(self, a): return StrJson.st(StrTrim.strip_suffix_repeat(self, a))
        def alpha(self): return StrJson.st(StrFilter.keep_alpha(self))
        def num(self): return StrJson.st(StrFilter.keep_digits(self))
        def remove(self, a): return StrJson.st(StrReplace.remove_all(self, a))
        def ra(self, a): return StrJson.st(StrReplace.remove_all(self, a))
        def json(self):
            result = StrJson.parse_json(self)
            if isinstance(result, dict):
                return StrJson.dic(result)
            if isinstance(result, list):
                return StrJson.lis(result)
            return result

    class dic(dict):
        def string(self):
            return StrJson.st(StrJson.dumps_pretty(self, sort_keys=False))

        def inline(self):
            return StrJson.st(StrJson.dumps_inline(self, sort_keys=False))

    class lis(list):
        def string(self):
            return StrJson.st(StrJson.dumps_pretty(self, sort_keys=False))

        def inline(self):
            return StrJson.st(StrJson.dumps_inline(self, sort_keys=False))


# =============================================================================
# Compatibility Aliases / Legacy Globals
# =============================================================================

# old globals
slash = StrConst.SLASH
upperChar = StrConst.UPPER
lowerChar = StrConst.LOWER
alphaChar = StrConst.ALPHA
printable = StrConst.PRINTABLE
printable2 = StrConst.PRINTABLE2
alphanumeric = StrConst.ALPHANUMERIC
safeChar = StrConst.SAFE_CHAR
visibleChar = StrConst.VISIBLE
notFilenameSafe = StrConst.NOT_FILENAME_SAFE
safe = StrConst.SAFE
safe2 = StrConst.SAFE2


# =============================================================================
# Compatibility Functions
# =============================================================================

def randomStr(s): return StrConvert.randomize_chars(s)  # old: randomStr
def printClean(text): return StrNormalize.printable_only(text)  # old: printClean
def minimalistClean(row): return StrNormalize.minimal_clean(row)  # old: minimalistClean
def hasAlpha(row): return StrDetect.has_alpha(row)  # old: hasAlpha
def totalClean(row): return StrNormalize.total_clean(row)  # old: totalClean
def filenameSafe(data): return StrFilter.filename_safe(data)  # old: filenameSafe
def hasVisible(data): return StrDetect.has_visible(data)  # old: hasVisible
def removeUnsave(data): return StrFilter.remove_unsafe(data)  # old: removeUnsave
def spaceba(string, what): return StrNormalize.remove_outer_spaces_around_token(string, what)  # old: spaceba
def makePrintable(string, replaceWith=' ', appropriate=False): return StrNormalize.make_printable(string, replace_with=replaceWith, appropriate=None if appropriate is False else appropriate)  # old: makePrintable
def namespace(app, data): return StrNamespace.extract_namespace_token(app, data)  # old: namespace

def replaceAll(string, rWhat, rWith): return StrReplace.replace_all(string, rWhat, rWith)  # old: replaceAll
def removeAll(string, rWhat): return StrReplace.remove_all(string, rWhat)  # old: removeAll
def replaceDuplicate(string, rWhat): return StrTrim.collapse_token_runs(string, rWhat)  # old: replaceDuplicate
def cleanFirst(string, rWhat): return StrTrim.strip_prefix_repeat(string, rWhat)  # old: cleanFirst
def cleanEnd(string, rWhat): return StrTrim.strip_suffix_repeat(string, rWhat)  # old: cleanEnd
def cleanLast(string, rWhat): return StrTrim.strip_suffix_repeat(string, rWhat)  # old: cleanLast
def cleanBE(string, rWhat): return StrTrim.strip_both_repeated(string, rWhat)  # old: cleanBE
def cleanAll(string, rWhat, rWith): return StrReplace.clean_all(string, rWhat, rWith)  # old: cleanAll

def totalStrip(line): return StrFilter.total_strip_default(line)  # old: totalStrip
def totalStrip1b(line, add=''): return StrFilter.total_strip_alnum(line, add=add or '')  # old: totalStrip1b
def totalStrip2(line): return StrFilter.total_strip_dash(line)  # old: totalStrip2
def totalStrip2b(line): return StrFilter.total_strip_dash_underscore_space(line)  # old: totalStrip2b
def totalStrip3(line): return StrFilter.total_strip_dash_comma(line)  # old: totalStrip3
def totalStrip4(line): return StrFilter.total_strip_digits(line)  # old: totalStrip4
def totalStrip5(line): return StrFilter.total_strip_extended(line)  # old: totalStrip5
def totalStrip6(line): return StrFilter.total_strip_extended(line)  # old: totalStrip6
def totalStrip7(line): return StrFilter.total_strip_dot_from_underscores(line)  # old: totalStrip7
def totalStrip8(line): return StrFilter.total_strip_extended(line)  # old: totalStrip8
def totalStrip9(line): return StrFilter.total_strip_dot_from_underscores(line)  # old: totalStrip9
def underscore(line): return StrNormalize.replace_underscore_like(line)  # old: underscore

def isInt(data): return StrDetect.is_int(data)  # old: isInt
def isFloat(data): return StrDetect.is_float(data)  # old: isFloat
def autoFloatInt(data): return StrConvert.to_number(data)  # old: autoFloatInt
def onlyDigits(line): return StrFilter.keep_digits_dash(line)  # old: onlyDigits
def onlyDigits2(line): return StrFilter.keep_digits_dash(line)  # old: onlyDigits2
def removeNonAlpha(string): return StrFilter.keep_alpha(string)  # old: removeNonAlpha
def removeNonNumber(string): return StrFilter.keep_digits(string)  # old: removeNonNumber
def removeNonAlpha2(string): return StrFilter.keep_alpha_space(string)  # old: removeNonAlpha2
def padZeros(string, count): return StrConvert.zero_fill(string, count)  # old: padZeros

def characterClean(string): return StrNormalize.character_clean(string)  # old: characterClean
def cleanupString(string, beforeAfter=True): return StrNormalize.cleanup_string(string, before_after=beforeAfter)  # old: cleanupString
def clean_latin1(data): return StrNormalize.clean_latin1(data)  # old: clean_latin1
def cleanChar(data): return StrNormalize.clean_char(data)  # old: cleanChar
def charFix(string): return StrNormalize.char_fix(string)  # old: charFix
def stripNonAlphaNumaric(data, also=''): return StrFilter.keep_alnum(data, also=also)  # old: stripNonAlphaNumaric
def basic(string): return StrFilter.basic(string)  # old: basic

def sp(cnt, t=' '): return StrFormat.spaces(cnt, t)  # old: sp
def es(data, be='', margin='', m=None): return StrFormat.margin_block(data, margin if m is None else m, be)  # old: es
def nows(string): return StrNormalize.no_whitespace(string)  # old: nows
def trim(string): return StrNormalize.trim(string)  # old: trim
def sh2(string): return StrNormalize.shell_text_tabs(string)  # old: sh2
def sh(string=''): return StrNormalize.shell_text(string)  # old: sh

# line-helper compatibility aliases inspired by newer helper style
def clean_lines(text, keep_empty=False): return StrLine.lines(text, keep_empty=keep_empty, collapse_spaces=True)
def strip_lines(text): return StrLine.non_empty_lines(text)
def find_line_indexes(text_or_lines, needle, case_sensitive=False, exact=False): return StrLine.find_indexes(text_or_lines, needle, case_sensitive=case_sensitive, exact=exact)
def first_index(text_or_lines, needle, case_sensitive=False, exact=False): return StrLine.first_index(text_or_lines, needle, case_sensitive=case_sensitive, exact=exact)
def next_non_empty_after(text_or_lines, needle, case_sensitive=False, exact=False, default=None): return StrLine.next_non_empty_after(text_or_lines, needle, case_sensitive=case_sensitive, exact=exact, default=default)
def non_empty_lines_after(text_or_lines, needle, count=1, case_sensitive=False, exact=False): return StrLine.non_empty_after(text_or_lines, needle, count=count, case_sensitive=case_sensitive, exact=exact)
def line_offsets_after(text_or_lines, start_string, offsets, output='list', glue='\n', case_sensitive=False, exact=False): return StrLine.line_offsets_after(text_or_lines, start_string, offsets, output=output, glue=glue, case_sensitive=case_sensitive, exact=exact)
def all_after_until_blank(text_or_lines, start_string, include_start=False, case_sensitive=False, exact=False): return StrLine.block_after_until_blank(text_or_lines, start_string, include_start=include_start, case_sensitive=case_sensitive, exact=exact)
def key_value_by_next_line(text_or_lines, keys, exact=False, case_sensitive=False): return StrLine.key_value_by_next_line(text_or_lines, keys, exact=exact, case_sensitive=case_sensitive)
def collect_fields(text_or_lines, field_map): return StrLine.collect_fields(text_or_lines, field_map)


# =============================================================================
# Dispatcher
# =============================================================================

def do(what=None, string='', a=None, b=None, c=None, d=None):
    '''
    # Legacy Dispatcher

    Backward-compatible dispatcher for older apps.

    ## Supported legacy values
    - `an`, `alphan`
    - `file`
    - `trim`
    - `nows`
    - `all`
    - `cleanAll`
    - `dup`
    - `be`
    - `b`
    - `e`
    - `n`
    - `ra`, `remove`
    - `.sh`, `sh`, `bash`, `linux`, `fix`, `script`
    - `sh2`

    ## Notes
    New code should call the classes directly instead of using `do()`.
    '''
    if what in ('an', 'alphan'):
        return StrFilter.total_strip_alnum(string, add=a or '')
    if what == 'file':
        return StrFilter.filename_safe(string, collapse_spaces=bool(a) if a is not None else True, replace_invalid_with=b or ' ', whitelist=c)
    if what == 'trim':
        return StrNormalize.trim(string)
    if what == 'nows':
        return StrNormalize.no_whitespace(string)
    if what in ('sh2',):
        return StrNormalize.shell_text_tabs(string)
    if what in ('.sh', 'sh', 'bash', 'linux', 'fix', 'script', 'x', '+x'):
        return StrNormalize.shell_text(string)
    if what == 'all':
        return StrReplace.replace_all(string, a, b)
    if what == 'cleanAll':
        return StrReplace.clean_all(string, a, b)
    if what == 'dup':
        return StrTrim.collapse_token_runs(string, a)
    if what == 'be':
        return StrTrim.strip_both_repeated(string, a)
    if what == 'b':
        return StrTrim.strip_prefix_repeat(string, a)
    if what == 'e':
        return StrTrim.strip_suffix_repeat(string, a)
    if what == 'n':
        return StrFilter.keep_digits(string)
    if what in ('ra', 'remove'):
        return StrReplace.remove_all(string, a)
    if what is not None and 'alpha' in StrConvert.to_str(what) and 'nu' in StrConvert.to_str(what):
        return StrFilter.keep_alnum(string)
    return string


# =============================================================================
# Legacy Wrapper Classes
# =============================================================================

class st(StrJson.st):
    pass


class dic(StrJson.dic):
    pass


class lis(StrJson.lis):
    pass