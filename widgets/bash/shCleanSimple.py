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

import os
import sys
# import _rightThumb._vars as _v

def getText( theFile ):
    lines = None
    if os.path.isfile(theFile):
        try:
            f = open(theFile, 'r', encoding='utf-8')
            lines = f.readlines()
            f.close()
        except Exception as e:
            try:
                f = open(theFile, 'r', encoding='latin-1')
                lines = f.readlines()
                f.close()
            except Exception as e:
                f = open(theFile, 'r')
                lines = f.readlines()
                f.close()
    else:
        if not e:
            return None
        print('(getText) Error: No File')
        sys.exit()
    if type(lines) == list:
        lines = ''.join( lines )
    return lines

def saveText( rows, theFile, errors=True ):
    # print(type(rows))
    try:
        if type(rows) == bytes:
            rows = str(rows,'utf-8')
        f = open(theFile,'w', encoding='utf-8')
        # if type(rows) == str:

        # print(type(rows))
        # f.write(str(rows))
        # rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
        # f.write(rows)
        # f.write(rows.encode("iso-8859-1", "replace"))

        # print(type(rows))
        if type(rows) == str:
            # print(rows)
            f.write(rows)
        else:
            for i,row in enumerate(rows):
                # f.write(str(row) + os.linesep)
                if i == 0:
                    if len(str(row)) > 0:
                        f.write(str(row) + '\n')
                else:
                    f.write(str(row) + '\n')
        f.close()
    except Exception as e:
        if type(rows) == list:
            result = ''
            for i,row in enumerate(rows):
                # f.write(str(row) + os.linesep)
                if i == 0:
                    if len(str(row)) > 0:
                        result += str(row) + '\n'
                else:
                    result += str(row) + '\n'

            rows = result
        open(theFile, 'wb').write(rows)
        if errors:
            print( 'Auto correction when saving text' )

def getFolder(folder):
    dirList = os.listdir(folder)
    # i = 0

    for item in dirList:
        path = folder + os.sep + item
        if os.path.isfile(path):
            if path.endswith('.sh'):
                print( path )
                file = getText( path )
                file = file.replace( chr(10), '\n' )
                file = file.replace( '\r', '\n' )
                file = file.replace( '\n\n', '\n' )
                file = file.replace( 'src', 'src' )
                file = file.replace( '\r', '\n' )
                saveText( file, path )
        if os.path.isdir(path):
            try:
                getFolder(path)
            except Exception as e:
                pass

def action():
    folder = os.getcwd()
    getFolder(folder)


if __name__ == '__main__':
    action()


