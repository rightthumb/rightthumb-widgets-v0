def switchDict(switches, argv=None):
    """
    switches : string or list of allowed switches
               ex: '--f --a --v + -'
    argv     : command input (string or list)
               default = sys.argv[1:]

    returns dict:
        {
            '--f': ['file1.txt', 'file2.txt'],
            '+': ['inFile'],
            '-': ['notInFile']
        }
    """
    if isinstance(argv, str):
        while '  ' in argv:
            argv = argv.replace('  ', ' ')
        argv = argv.split(' ')
    
    import sys

    # ---- normalize allowed switches ----
    if isinstance(switches, str):
        s = switches.replace(',', ' ')
        while '  ' in s:
            s = s.replace('  ', ' ')
        allowed = set(s.split())
    else:
        allowed = set(switches)

    # ---- normalize argv ----
    if argv is None:
        argv = sys.argv[1:]

    if isinstance(argv, str):
        a = argv.replace(',', ' ')
        while '  ' in a:
            a = a.replace('  ', ' ')
        argv = a.split()

    out = {}
    current = None

    for token in argv:
        if token in allowed:
            current = token
            out.setdefault(current, [])
        elif current is not None:
            out[current].append(token)

    return out

'''
cmd = 'app --f file1.txt file2.txt + inFile - notInFile'
sw = switchDict('--f --a --v + -')
# out 
{
    '--f': ['file1.txt', 'file2.txt'],
    '+': ['inFile'],
    '-': ['notInFile']
}
'''
