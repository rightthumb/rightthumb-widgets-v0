"# rightthumb-widgets-v0"


Description

    collection of handy scripts ( over 1700 )

    p file -bin -r -ago 1d
        recursive binary files modified less than a day ago

    p file -ago 1d -ext video --c
        video files edited 1 day ago
            -ext switch includes all related extensions
            --c does not print totals (works in all apps)
            -ago accepts epoch date, 1min, 1h, 1d, 1m, 1y
    p ls -ago 1d -ext video
        displays a table of meta
    p ls -?
        full help menu
    p ls --??
        smaller help menu with global switches removed
    p ls --?? c
        lists examples then copies the selected help item to clipboard
    p ls --c | p -copy
        copies list of files
    p cat -f 555-index.htm + eyeformeta. | p pipe-split -dirty + eyeformeta --c | p sortThis | p -copy
        scan javascript global namespace report
    p cat -f 555-index.htm + "var " "(" - "{" "[" "'"
        scan javascript for variables set with a function
    p inFunc -f mf.py + self.
        proper python class and function search tool
    cat D:\.rightthumb-widgets\widgets\python\_rightThumb\_auditCodeBase\__init__.py | p pipe-split -dirty + self. -a "("
        dirty python class variable and function dump



Features

    works on
        windows (cmd.exe)
        linux and mac (bash)
        powershell
        termux

    automatically install vnc on debian
    extensive file header database
    manage dnd spells

    p checksum -f pop-os_20.10_amd64_nvidia_10.iso -test 412c49dcdda20dfa69b574f255a63d10dcfe20aa

    p checksum -f pop-os_20.10_amd64_nvidia_10.iso -h md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512

    in windows, if you use the x command instead of EXIT
        the history is backed up and associated with files edited using the command line

    in windows, if you use the c command instead of CLS
        if you close out without x command by accident
            open a new terminal run r.t command then EXIT
                ALL missing history will be documented


    in linux nice prompt
        random icon in every prompt, lol
        
        ┌──(scott🌭Vulcan)-[/mnt/c/Users/Scott].3.def
        └─$

    automatic franchise research
    cross reference 2 or more tv shows or movies
    list all episodes in a series

    in windows
        p history -ago 2d + "cd clients"
            you can search through terminal history

    have a movie drive?
        auto franchise hierarchy!!
    Marvel                      Avengers                   2019 Avengers: Endgame
                                                           2018 Avengers: Infinity War
                                                           2015 Avengers: Age of Ultron
                                Spiderman                  2018 Spider-Man: Into the Spider-Verse
                                                           2017 Spider-Man: Homecoming
                                                           2014 The Amazing Spider-Man 2
                                                           2007 Spider-Man 3
                                                           2004 Spider-Man 2
                                                           2002 Spider-Man
                                Ant-Man                    2018 Ant-Man and the Wasp
                                                           2015 Ant-Man
                                Wolverine                  2017 Logan
                                                           2013 The Wolverine
                                                           2009 X-Men Origins: Wolverine
                                Thor                       2017 Thor: Ragnarok
                                                           2013 Thor: The Dark World
                                                           2011 Thor
        











How to install


    cd install
    python3 installer.py -install
        or 
            python3 installer.py -install h
                the h replaces the HISTSIZE and HISTFILESIZE to make the history larger
        *NOT* python3 install/installer.py -install

    which nano | python3 installer.py -config.editor
    or
    python3 installer.py -config.editor "C:\Program Files\Sublime Text 3\sublime_text.exe"

How to open a file

    n file.txt

How to recover a file
    
    p fileRecover
        in windows it backs up the command line history
            the session id is associated with the files edited


How the installer works

    in windows
        a file %USERPROFILE%\rr.bat
            i recommend copying it to %SYSTEMROOT%\System32\rr.bat
        when you open windows terminal type rr ENTER and the widgets are loaded it just loads folders to the path and sets a few variables (they are simple to read)
        
    
    in linux
        the .bashrc is modified
        NOTHING IS REMOVED!!!
        variables and aliases between ## {E45D09D22184} ## and ## {AEC80B4D3338} ##
        bookmarks cd aliases between ## {42F74F699A95} ## and ## {6D2B143FF720} ##
        VERY EASY TO REMOVE


Recommended python modules

    sudo python3 -m ensurepip
    python3 -m pip install --upgrade pip
    apt-get install python3
    apt-get install python3-pip
    apt-get install fonts-emojione
    apt-get install wget
    apt-get install unzip

    pip3 install simplejson
    pip3 install datefinder
    pip3 install xtarfile
    pip3 install binaryornot
    pip3 install cssselect
    pip3 install colorama
    pip3 install arrow
    if termux
        pip3 install setuptools-rust
    pip3 install pymysql
    pip3 install Crypto
    pip3 install tzlocal
    pip3 install termcolor
    pip3 install datetime
    pip3 install pyAesCrypt
    pip3 install zipfile36
    pip3 install pywin32
    pip3 install stickytape
    pip3 install dnspython
    pip3 install pymongo
    pip3 install mycloudhome
    pip3 install pyperclip
    pip3 install pyAesCrypt
    pip3 install pycrypto
    pip3 install sshtunnel
    pip3 install gtts
    pip3 install emoji
    pip3 install pyreadline
    pip3 install ping
    pip3 install netaddr
    pip3 install getmac
    pip3 install native_web_app
    pip3 install psutil
    pip3 install forward
    pip3 install num2word
    pip3 install -e git+https://github.com/izderadicka/unistego#egg=unistego


Create new python widget with

    in windows
        epyi base -build myApp
    linux
        epyiBuild myApp
    (scroll to bottom)

    # example:
        def action():
            files=_.isData()
            if _.switches.isActive('Files'):
                for file in _.switches.values('Files'):
                    files.append(file)
            if _.switches.isActive('Folders'):
                for folder in _.switches.values('Folders'):
                    files.append( folder, r=_.switches.isActive('Recursive') )
            for path in files:
                if _.showLine(path):
                    process(path)
    Notes
        _.isData()
            pipe or Files switch depending on switch registration
        _.switches.values
            list
        _.showLine
            by default is True
            is related to switches:
                + - -or +close +duplicate -strictcase
                    +close and +duplicate, use a pattern recognition algorithm I cooked up






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

    all python widgets are imported as an instantiated object
        all interaction are profiled and reports are available

    _copy = _.regImp( __.appReg, '-copy' )
    _copy.imp.copy(  )



Edit python template

    in windows
        epyi base -e
    in linux
        n widgets\python\_rightThumb\_base3\_base3_init_example.py




Notes
    
    epyi base -file notes

   


Before you share a problem the below command will tell you everything I am already aware of



                b py
                Fast ▽
                   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p appInfo

                   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p line --c -make "echo {}| p appInfo" | p execute
                Accurate △

            n widgets/databank/tables/appRegistration.hash


Entertainment
    
    List every episode of a tv show
        ee the flash

    Cross reference 2 tv show
        p imdb -ent stargate atlantis and when calls the heart -xref

    Automatic franchise research
        p franchise -franchise marvel
        p franchise -franchise dc
        p franchise -franchise hallmark

    When you look up a show
        p imdb -ent the big bang theory
            type f
                type hallmark
                    It cross references franchises
                        marvel, dc, hallmark

Code Note

    I code a little weird because it is backwards compatible and organized
        Example:
            Used the command: p inFunc -f hotkeys.py
                Generated this:
                     class HOTKEYS
                         def __init__
                         def release_key
                         def process_keystroke
                     class BEEPS
                         def __init__
                         def play_note
                         def simple_beep
                         def simple_beep2
                     class CLIP
                         def toLower
                         def toUpper
                         def reverse_lines
                         def builder
                         def builder2
                             def build_helper
                         def range_first
                             def spliter
                         def first
                         def php_var
                         def SQL_to_crud
                             def field_data
                         def win_path
                         def implode
                         def implode3
                         def prefix
                         def combine_make
                         def suffix
                         def number
                         def number_a
                         def number_b
                         def number_ba
                         def explode
                         def math
                         def dic
                         def add_slash
                         def del_activate
                         def del_run
                     class TYPING
                         def __init__
                         def ty
                         def ty_h
                         def ty_a
                         def keyboard_typing
                     class LOADER
                         def __init__
                         def autoText
                         def flip_table_test
                         def add_text
                         def build_table    
    I instantiate everything
        Hotkeys=HOTKEYS()
        Typing=TYPING()
        Loader=LOADER()
        Clip=CLIP()
    and execute:
        Loader.build_table()
            in the code
    If del __init__ it is not backwards compatable

Hotkey example

~~~
   copy
        1
        2
        3
    cmd+alt+i (implode: works with text AND json)
    paste
    1, 2, 3

    copy
        [1, 2, 3]
    cmd+alt+x (explode: works with text AND json)
    paste
        [
            1,
            2,
            3
        ]

    HOW TO FIND ALL COMMANDS:

        run command: epy hotkeys
            then scroll to the bottom of the app to see a list of hotkeys

        config file 1: widgets/databank/tables/hotkeys-AutoText.dex
            (there is an app called AutoText that can be imported into this system)

        config file 2: widgets/databank/tables/hotkeys-Text.dex

~~~

Creating your own apps using this system?

    ALL python apps have have documentation and categorical tags
        if creating a new app with this system; documentation tag tense is inconsequential
            i extract the word stems when using documentation ( with nltk.stem )

About

    What if magic existed?
    What if a place existed where your every thought and dream come to life.
    There is only one catch: it has to be written down.
    Such a place exists, it is called programming.
        - Scott Taylor Reph, RightThumb.com, EyeForMeta.com
