# rightthumb.com framework

## Platform Support
### The Framework is designed to work on the following platforms:
- Windows
- Linux
- macOS
- phone or tablets
    + Additionally, the framework can be used on mobile devices running Termux or similar environments.

## Hype
- I push 10 on my [mouse](https://www.amazon.com/dp/B088B3ZM76) to activate voice commands and say "Sally paste, convert this python to javascript" (using chatGPT). I then paste the results.
- The hotkeys.py app uses keyboard shortcuts. A programmable mouse can activate any of them.
- How to navigate to the Downloads folder'b dl'. How to create a new bookmark 'm name'.
- How to view all of the files and folders ' d ', to search for somthing ' d somthing '. Linked files and folders are yellow.
- How to register a document for encryption 'crypt pw.md'.
- How to open an important encrypted document 'n pw.md', if you are not in that folder 'fa pw'. how to create that alias 'fa pw pw.md'.
- How to close the terminal ' x ' (backs everything up that you opened since you started the terminal and encrypts registered encrypted files).
- How do you encrypt the file without closing the terminal 'p fileBackup -f pw.md'.
- Copy the CREATE TABLE sql, hit alt+win+c to automatically generate the create, read, update, delete of a table in php (crud), then paste the results.
- How to find a file that was modified within the last day 'p file -ago 1d', week 'p file -ago 1w', month 'p file -ago 1m', 10 minutes 'p file -ago 10min'.
- How to view all of the episodes of a tv show 'ee the flash'.
- How to do automated franchise research of everything from a franchise including video games 'p franchise -franchise marvel'. How to view the results 'p franchiseView -franchise marvel'.
- Checksum 'p checksum -f pop-os_20.10_amd64_nvidia_10.iso ' or 'p checksum -f pop-os_20.10_amd64_nvidia_10.iso -test 412c49dcdda20dfa69b574f255a63d10dcfe20aa'
- How to recursivly find a '.md' file modified in the last week with 'abc' in the file name without 'xyz' in file name with 'due 2025-12-25' inside the file 'p files + \*.md -ago 1w + abc - xyz -has "due 2025-12-25"'.
- How to scrape text from a webpage, copy the selector, tap 'shift shift w txt' (for me button 10 on my mouse then I say 'scrape text').
- How to find all emails, urls, mailing addresses, windows paths, linux paths in copied text 'ctrl win h', then paste the results.
- Thousands of features

## Installation
~~~
python3 -m pip install --upgrade pip
apt-get install python3  -y
apt-get install fonts-emojione  -y
apt-get install wget  -y
apt-get install unzip  -y
apt install iputils-ping  -y
apt-get install python3-pip -y

pip3 install -r require.txt
~~~

## How to install the framework
~~~
cd install
python3 installer.py -install h
python3 installer.py -rc.d h

add a default editor
    which nano | python3 installer.py -config.editor
    or
    python3 installer.py -config.editor "C:\Program Files\Sublime Text 3\sublime_text.exe"

How to open a file
    n file.txt

How to recover a file
    p fileRecover -f file.txt

How the installer works

in windows
    a file %USERPROFILE%\rr.bat
        i recommend copying it to %SYSTEMROOT%\System32\rr.bat
    when you open windows terminal type rr
    or
    in windows terminal
        "commandline": "cmd /k \"C:\\Users\\Scott\\rr.bat\"",
    
in linux
    the .bashrc is modified
    NOTHING IS REMOVED!!!
    variables and aliases between ## {E45D09D22184} ## and ## {AEC80B4D3338} ##
    bookmarks cd aliases between ## {42F74F699A95} ## and ## {6D2B143FF720} ##
    VERY EASY TO REMOVE
~~~


## Misc
### Have a movie drive?
### Auto franchise hirarchy
~~~
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
~~~    



## Create your own apps
~~~
in windows
    epyi base -build myApp
linux
    epyiBuild myApp

To edit the framework new app template
    epyi base -e

it will open a template in your editor
scroll down to '#n)--> start'


_.isData()
    Switch arguments
        _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
            To get the contents of the file isData='data' or isData='data,clean'
    OR PIPE
        cat paths.txt | p app
    OR PASTE copied text
        p app --pa
        or
        p -paste | p app

To ues the ' + ' and ' - ' switches: _.showLine(data)

# example:
    for path in _.isData():
        if _.showLine(path):
            process(path)

Don't forget to try this:
    os=__.imp('os.path.isfile')

~~~

## Note
### The use of '-' dashes in the file names is because framework apps are imported via class
~~~
example:
    _paste = _.regImp( __.appReg, '-paste' )
~~~

## Automatically profile every app in the framework (including ones you create)
~~~
first go to the python folder.

The FAST way:
   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p appInfo

The Accurate way
   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p line --c -make "echo {}| p appInfo" | p execute

it saves a json file here:
    widgets/databank/tables/appRegistration.hash
~~~

## Side note
### To install my scraping tool as a chrome link.
1 create a new link.
2 paste the bellow code as the url.
3 view the JavaScript console for instructions.
- example: copy and paste one of the suggestions "hackTool.help( {'tags': 'tables_w_labels'} )" then "copy(hackTool.helper)" and paste in the console.
~~~
javascript:{ var script = document.createElement('script');script.type = 'text/javascript'; if (location.protocol === 'https:') { script.src = 'https://eyeformeta.com/tools/tool.js'; } else { script.src = 'http://eyeformeta.com/tools/tool.js'; } document.head.appendChild(script);}
~~~

## About
~~~
What if magic existed?
What if a place existed where your every thought and dream come to life.
There is only one catch: it has to be written down.
Such a place exists, it is called programming.
    - Scott Taylor Reph, RightThumb.com
~~~
