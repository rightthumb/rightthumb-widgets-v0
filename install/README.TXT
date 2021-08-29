"# rightthumb-widgets-v0" 
FEATURES
    automatically install vnc on debian
    works on
        windows (cmd.exe)
        linux and mac (bash)
        powershell




HOW TO INSTALL

    python3 installer.py -install

    which nano | python3 installer.py -config.editor
    or
    python3 installer.py -config.editor "C:\Program Files\Sublime Text 3\sublime_text.exe"


Create new python widget with
    epyi base -build myApp
    (scroll to bottom)


Edit python widget
    epy myApp

Execute python widget
    p myApp

Bookmark System
    m command makes a bookmark
    b command goes to bookmark
    cd $HOME/Downloads
    m dl
        in windows and powershell
            b dl
            bookmark is available immediately

        in bash
            b.dl
            it modifies the .bashrc file with a bookmark
            the bookmark is available on next terminal
                alias b.dl='cd "$HOME/Downloads"'



IF you manually edit the config file $HOME/.rt/.config.hash
    AFTER RUN
        python3 installer.py -bash.vars

Auto build bookmarks
    p bm-dirty|bash

How to import another python widget
    all python widget is imported as an instantiated object
        all interaction is profiled and reports are available

    _copy = _.regImp( __.appReg, '-copy' )
    _copy.imp.copy(  )

Edit python template
    epyi base -e
   

Before you share a problem the below command will tell you everything I am already aware of

                b py
                Fast ▽
                   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p appInfo

                   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p line --c -make "echo {}| p appInfo" | p execute
                Accurate △
            n widgets/databank/tables/appRegistration.hash