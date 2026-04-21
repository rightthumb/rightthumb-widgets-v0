import _rightThumb._base3 as _

def printVarSimpleFake2(data):
    import re
    arguments = []
    def has_alphanumeric_around_equal(s):
        for i in range(1, len(s) - 1):
            if s[i] == '=' and s[i - 1].isalnum() and s[i + 1].isalnum():
                return True
        return False
    def show_ansi_codes(s):
        return s.replace('\x1b', '\\033')
    def colorize_quotes(s, quote_color='darkcyan', content_color='cyan'):
        s = re.sub('\\033\\[\\d+m', '', s)
        s = re.sub('\\b(TABLE_PUT)\\b', Color.cyan + '\\1' + Color.end, s)
        s = colorize_quotes2(s, quote_color, content_color)
        return s
    def colorize_quotes2(s, quote_color='darkcyan', content_color='cyan'):
        pattern = '([\'\\"])(.*?)(?<!\\\\033)\\1'
        offset = 0
        for match in re.finditer(pattern, s):
            start_quote = match.start(1) + offset
            end_quote = start_quote + len(match.group(1))
            start_content = match.start(2) + offset
            end_content = start_content + len(match.group(2))
            s = s[:start_content] + eval(f'Color.{content_color}') + s[start_content:end_content] + Color.end + s[end_content:]
            offset += len(Color.end) + len(eval(f'Color.{content_color}'))
            s = s[:start_quote] + eval(f'Color.{quote_color}') + s[start_quote:end_quote] + Color.end + s[end_quote:]
            offset += len(Color.end) + len(eval(f'Color.{quote_color}'))
            end_quote = match.end(2) + offset
            s = s[:end_quote] + eval(f'Color.{quote_color}') + s[end_quote:end_quote + len(match.group(1))] + Color.end + s[end_quote + len(match.group(1)):]
            offset += len(Color.end) + len(eval(f'Color.{quote_color}'))
        return s
    def find_all_function_names(s):
        pattern = '\\b[A-Za-z]\\w*(?=\\()'
        matches = [m for m in re.finditer(pattern, s)]
        indices = []
        for match in matches:
            start = match.start()
            end = match.end() - 1
            indices.append((start, end))
        return indices
    def find_arguments(s):
        pattern = '\\(([^)]*)\\)'
        matches = list(re.finditer(pattern, s))
        all_indices = []
        for match in matches:
            args_str = match.group(1)
            split_indices = [0] + [m.end() for m in re.finditer('(?<!["\\\']),', args_str)]
            arg_strings = [args_str[i:j] for i, j in zip(split_indices, split_indices[1:] + [None])]
            start_index = match.start(1)
            indices = [(start_index + i, start_index + i + len(arg) - 1) for i, arg in enumerate(arg_strings)]
            all_indices.extend(indices)
        return all_indices
    def find_arguments_words(s):
        pattern = '\\(([^)]*)\\)'
        matches = list(re.finditer(pattern, s))
        all_args = []
        for match in matches:
            args_str = match.group(1)
            split_indices = [0] + [m.end() for m in re.finditer('(?<!["\\\']),', args_str)]
            arg_strings = [args_str[i:j].strip() for i, j in zip(split_indices, split_indices[1:] + [None])]
            for arg in arg_strings:
                if not arg.startswith('"') and (not arg.startswith("'")):
                    all_args.append(arg)
        return all_args
    def colorize_indices(s, indices, color):
        if not indices:
            return s
        if not isinstance(indices, list):
            indices = [indices]
        offset = 0
        for start, end in indices:
            try:
                colored_string = eval('Color.' + color + '+ s[start+offset:end+offset+1] + Color.end')
            except Exception:
                continue
            s = s[:start + offset] + colored_string + s[end + offset + 1:]
            offset += len(colored_string) - (end - start + 1)
        return s
    def colorize_chars(result, dic):
        i = 0
        while i < len(result):
            if result[i:i + 2] == '\\033':
                color_code_end = result.find('m', i)
                i = color_code_end + 1
                continue
            for k, color in dic.items():
                if result[i] in k:
                    result = result[:i] + eval('Color.' + color) + result[i] + Color.end + result[i + 1:]
                    i += len(eval('Color.' + color)) + len(Color.end)
                    break
            i += 1
        return result
    def colorize_words(result, dic):
        i = 0
        while i < len(result):
            if result[i:i + 2] == '\\033':
                color_code_end = result.find('m', i)
                i = color_code_end + 1
                continue
            matched = False
            for word, color in dic.items():
                pattern = f'\\b{re.escape(word)}\\b' if word.isidentifier() else re.escape(word)
                match = re.search(pattern, result[i:])
                if match:
                    matched_text = match.group(0)
                    colored_text = eval(f'Color.{color}') + matched_text + Color.end
                    result = result[:i + match.start()] + colored_text + result[i + match.end():]
                    i += len(colored_text)
                    matched = True
                    break
            if not matched:
                i += 1
        return result
    def find_argument_usage(s, color='CYAN'):
        args_match = re.search('Usage.*?\\(([^)]*)\\)', s, re.DOTALL)
        if not args_match:
            return s
        args_str = args_match.group(1)
        arguments = [arg.strip() for arg in re.split('(?<!["\\\']),', args_str)]
        i = 0
        while i < len(s):
            if s[i:i + 2] == '\\033':
                color_code_end = s.find('m', i)
                i = color_code_end + 1
                continue
            found = False
            for arg in arguments:
                pattern = f'(?<=[\\s(])({re.escape(arg)})(?=[\\s,).])'
                match = re.search(pattern, s[i:])
                if match:
                    matched_text = match.group(1)
                    colored_text = eval(f'Color.{color}') + matched_text + Color.end
                    s = s[:match.start() + i] + colored_text + s[match.end() + i:]
                    i += len(colored_text)
                    found = True
                    break
            if not found:
                i += 1
        return s
    variables = []
    clean = []
    for line in data.split('\n'):
        if '=' in line and has_alphanumeric_around_equal(line):
            line = line.replace('=', ' = ')
        clean.append(line)
    result = '\n'.join(clean)
    arguments = find_arguments_words(result)
    dic = {'[]': 'purple'}
    for line in result.split('\n'):
        if ' = ' in line:
            variables.append(line.split(' = ')[0].strip())
    result = colorize_indices(result, find_all_function_names(result), 'cyan')
    result = colorize_indices(result, find_arguments(result), 'darkcyan')
    result = colorize_chars(result, dic)
    result = colorize_quotes(result)
    result = find_argument_usage(result, 'darkcyan')
    dic = {'!': 'yellow', '(){}': 'purple', '-=/': 'red'}
    result = colorize_chars(result, dic)
    dic = {'RETURN': 'blue', 'IF': 'purple', 'THEN': 'purple', 'ELSE': 'purple'}
    spentV = []
    spentA = []
    for v in variables:
        v = v.strip()
        if v in spentV:
            continue
        spentV.append(v)
        if v in arguments:
            dic[' ' + v + ' '] = 'darkcyan'
            dic['\n' + v + ' '] = 'darkcyan'
        else:
            dic['\n' + v + ' '] = 'green'
            dic[' ' + v + ' '] = 'green'
    for v in arguments:
        if v in spentA:
            continue
        spentA.append(v)
        dic[' ' + v + ' '] = 'darkcyan'
        dic['\n' + v + ' '] = 'darkcyan'
    result = colorize_words(result, dic)
    _.print_(result)