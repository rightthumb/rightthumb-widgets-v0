import _rightThumb._base3 as _

def vindex(code, i=0, esc='\\', n='', v=True, r=False, both=True, sort=True, isArg=False, comment='//'):
    ari = i
    if isArg:
        a_ = '-+'
    else:
        a_ = ''
    def _sort(sort, dic):
        if not sort:
            return dic
        ks = list(dic.keys())
        ks.sort()
        new = {}
        for k in ks:
            new[k] = dic[k]
        return new
    if type(code) == list:
        code = ''.join(code)
    at = i
    table = {}
    table['brackets'] = {}
    table['brackets']['i'] = 0
    table['brackets']['open'] = {}
    table['braces'] = {}
    table['braces']['i'] = 0
    table['braces']['open'] = {}
    table['par'] = {}
    table['par']['i'] = 0
    table['par']['open'] = {}
    index = {}
    i -= 1
    while True:
        i += 1
        if i >= len(code):
            break
        c = code[i]
        try:
            c2 = c + code[i + 1]
        except Exception as e:
            c2 = ''
        try:
            c3 = c2 + code[i + 2]
        except Exception as e:
            c3 = ''
        try:
            c4 = c3 + code[i + 3]
        except Exception as e:
            c4 = ''
        try:
            c5 = c4 + code[i + 4]
        except Exception as e:
            c5 = ''
        if len(esc) == 1 and c == esc:
            i += 1
        else:
            if len(esc) == 1 and c == esc:
                i += 1
            if n == '\n' and r:
                ii = i
                c = code[i]
                while not ii == 0 and c == '\n':
                    ii -= 1
                    c = code[ii]
                    if ii == 0:
                        return 0
                    elif c == '\n':
                        return ii
            elif len(n) == 1 and c == n:
                return i
            elif len(n) == 2 and c2 == n:
                return i + 1
            elif len(n) == 3 and c3 == n:
                return i + 2
            elif len(n):
                pass
            elif not n and c in '0123456789.':
                cx = c
                ii = i - 1
                while cx in '0123456789.':
                    ii += 1
                    try:
                        cx = code[ii]
                    except Exception as e:
                        ii -= 1
                        index[i] = ii
                        if both:
                            index[ii] = i
                        break
                index[i] = ii
                if both:
                    index[ii] = i
                i = ii
            elif not n and c in a_ + 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                cx = c
                ii = i - 1
                while cx in a_ + '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._':
                    ii += 1
                    try:
                        cx = code[ii]
                    except Exception as e:
                        ii -= 1
                        index[i] = ii
                        if both:
                            index[ii] = i
                        break
                index[i] = ii
                if both:
                    index[ii] = i
                i = ii
            elif not n and c3 == '"""':
                ss = _.vindex(code, i + 3, esc, n='"""', v=0, isArg=isArg, comment=comment)
                if type(ss) == int or i in ss:
                    if type(ss) == int:
                        s = ss
                    else:
                        s = ss[i]
                    index[i] = s
                    if both:
                        index[s] = i
                    i = s + 2
            elif not n and c3 == "'''":
                ss = _.vindex(code, i + 3, esc, n="'''", v=0, isArg=isArg, comment=comment)
                if type(ss) == int or i in ss:
                    if type(ss) == int:
                        s = ss
                    else:
                        s = ss[i]
                    index[i] = s
                    if both:
                        index[s] = i
                    i = s + 2
            elif not n and c == "'":
                ss = _.vindex(code, i + 1, esc, n="'", v=0, isArg=isArg, comment=comment)
                if type(ss) == int or i in ss:
                    if type(ss) == int:
                        s = ss
                    else:
                        s = ss[i]
                    index[i] = s
                    if both:
                        index[s] = i
                    i = s
            elif not n and c == '"':
                ss = _.vindex(code, i + 1, esc, n='"', v=0, isArg=isArg, comment=comment)
                if type(ss) == int or i in ss:
                    if type(ss) == int:
                        s = ss
                    else:
                        s = ss[i]
                    index[i] = s
                    if both:
                        index[s] = i
                    i = s
            elif not n and c2 == '/*':
                i = _.vindex(code, i + 2, esc, n='*/', v=0, isArg=isArg, comment=comment)
            elif not n and len(comment) == 1 and (c == comment) and (not code[ari] in '`"' + "'"):
                i = _.vindex(code, i + 1, esc, n='\n', v=0, isArg=isArg, comment=comment) + 1
            elif not n and len(comment) == 2 and (c2 == comment) and (not code[ari] in '`"' + "'"):
                i = _.vindex(code, i + 2, esc, n='\n', v=0, isArg=isArg, comment=comment) + 1
            elif not n and c == '{':
                table['brackets']['i'] += 1
                table['brackets']['open'][table['brackets']['i']] = i
            elif not n and c == '}':
                try:
                    s = table['brackets']['open'][table['brackets']['i']]
                except Exception as e:
                    return _sort(sort, index)
                index[s] = i
                if both:
                    index[i] = s
                table['brackets']['i'] -= 1
                if s == at:
                    return _sort(sort, index)
            elif not n and c == '[':
                table['braces']['i'] += 1
                table['braces']['open'][table['braces']['i']] = i
            elif not n and c == ']':
                try:
                    s = table['braces']['open'][table['braces']['i']]
                except Exception as e:
                    return _sort(sort, index)
                index[s] = i
                if both:
                    index[i] = s
                table['braces']['i'] -= 1
                if s == at:
                    return _sort(sort, index)
            elif not n and c == '(':
                table['par']['i'] += 1
                table['par']['open'][table['par']['i']] = i
            elif not n and c == ')':
                try:
                    s = table['par']['open'][table['par']['i']]
                except Exception as e:
                    return _sort(sort, index)
                index[s] = i
                if both:
                    index[i] = s
                table['par']['i'] -= 1
                if s == at:
                    return _sort(sort, index)
    return _sort(sort, index)