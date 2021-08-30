"# rightthumb-widgets-v0" 

DESCRIPTION

    collection of handy scripts
    p file -bin -r -ago 1d
        recursive binary files modified less than a day ago
    p file -ago 1d -ext video
        video files edited 1 day ago
            -ext switch includes all related extensions



FEATURES

    works on

        windows (cmd.exe)

        linux and mac (bash)

        powershell

    automatically install vnc on debian

    extensive file header database

    manage dnd spells

    p checksum -f pop-os_20.10_amd64_nvidia_10.iso -test 412c49dcdda20dfa69b574f255a63d10dcfe20aa

    p checksum -f pop-os_20.10_amd64_nvidia_10.iso -h md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512

    in windows, if you use the x command to close

        the history is backed up and associated with files edited using the command line

    in linux nice prompt

        random icon in every prompt, lol
        
        ┌──(scott🌭Vulcan)-[/mnt/c/Users/Scott].3.def
        └─$

    automatic franchise research
    cross reference 2 or more tv shows or movies
    list all episodes in a series

    around 1700 widgets in this












HOW TO INSTALL


    cd install
    python3 installer.py -install



    which nano | python3 installer.py -config.editor
    or
    python3 installer.py -config.editor "C:\Program Files\Sublime Text 3\sublime_text.exe"



How to open a file

    n file.txt

How to recover a file
    
    p fileRecover
        in windows it backs up the command line history
            the session id is associated with the files edited

Create new python widget with

    epyi base -build myApp
    (scroll to bottom)

    # example:
        def action():
            if _.switches.isActive('Files'):
                files= _.switches.values('Files')
            if _.switches.isActive('Folders'):
                files=[]
                for folder in _.switches.values('Folders'):
                    files.append( folder, r=_.switches.isActive('Recursive') )
                for path in files:
                    if _.showLine(path):
                        process(path)
    Notes
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

    epyi base -e


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
`
