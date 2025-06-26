# rightthumb.com framework

___

## Almost 3,000 Apps

___

## Just sharing how I customized my terminal

### Efficiently accomplish a wide range of tasks in a short amount of time

#### with a few thousand apps I made over my 20+ year career

___

## Platform Support

### The Framework is designed to work on the following

- Windows
- Linux
- macOS
- iOS
- Android
- Other:  PowerShell, etc

## Hype

- I push 10 on my [mouse](https://www.amazon.com/dp/B088B3ZM76) to activate voice commands and say "Sally paste, convert this python to javascript" (ai). I then paste the results.
  - The hotkeys.py app manages keyboard shortcuts. A programmable mouse can activate any of them.
    - View all keyboard shortcuts 'p hotkeys -k'
- Generate PHP code
  - Copy the CREATE TABLE sql, hit alt+win+c to automatically generate the create, read, update, delete of a table in php (crud), then paste the results.
- Tasklist
  - Grouped memory usage subtotals and grand total
    - ' task -report '
  - Search tasklist
    - ' task + chrome '
      - try 'kill chrome'
- Folder Navigation
  - How to navigate to the Downloads folder 'b dl'. How to create a new bookmark 'm name'.
  - How to view files and folders ' d ', to search for something  'd something'. Linked items are yellow.
- List all python apps ' list '
  - Search for an app that does something with json ' list json ' or ' py json '
- Responsive tables
  - Make the terminal full screen
  - Run ' p ls '
  - Resize the terminal smaller
  - Run ' p ls '
  - Resize the terminal smaller
  - Run ' p ls '
  - Resize the terminal smaller
  - Run ' p ls '
- Auto Backup, Auto Encryption, Auto save terminal history, Index every app and switch used associated with a history ID.
  - How to close the terminal ' x ' (backs everything up that you opened since you started the terminal and encrypts registered encrypted files).
- How to logout 'p logout'
  - Login is automatic when a password is needed, it will ask, or you can use 'p login'
- Encryption
  - How to register a document for encryption 'crypt file.md'.
  - How to open a document a text file, including encrypted, 'n file.md'
    - if you are not in that folder 'fa label'.
      - How to create that alias 'fa label file.md'.
  - How do you encrypt the file without closing the terminal 'p fileBackup -f file.md'.
- Search in files even if they are Zipped or Encrypted
  - How to view content of a file 'p cat -f file.md + <user@domain.com>'
    - How to zip a file in a way it can be searched 'p zzip -f file.md'
- File Search
  - How to find a file that was modified within the last day 'p file -ago 1d', week 'p file -ago 1w', month 'p file -ago 1m', 10 minutes 'p file -ago 10min'.
  - How to recursively find a '.md' file modified in the last week with 'abc' in the file name without 'xyz' in file name with 'due 2025-12-25' inside the file 'p files + \*.md -ago 1w + abc - xyz -has "due 2025-12-25"'.
- Checksum 'p checksum -f pop-os_20.10_amd64_nvidia_10.iso ' or 'p checksum -f pop-os_20.10_amd64_nvidia_10.iso -test 412c49dcdda20dfa69b574f255a63d10dcfe20aa'
- Entertainment
  - How to view all of the episodes of a tv show 'ee the flash'.
  - How to do automated franchise research of everything from a franchise including video games 'p franchise -franchise marvel'. How to view the results 'p franchiseView -franchise marvel'.
- Mine the clipboard
  - How to find all emails, urls, mailing addresses, Windows paths, Linux paths in copied text 'ctrl win h', then paste the results.
    - I just hit 7 on my mouse
- Windows terminal
  - List all keyboard shortcuts 'p wt -key actions'
  - List all profiles 'p wt -key profiles' (displays index for keyboard shortcuts)
  - List all keyboard shortcuts associated with a profile 'p wt -key actions + index'

## Thousands of apps with many features

## Anecdote

When covid began, I created an app called harResearch to identify how websites communicate with the server. I then use their data sources in my apps for Realtime covid research. (why I write apps securely)

## Installation

~~~sh
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

~~~md
Windows:
    cd /d %USERPROFILE%
Linux:
    cd /opt

git clone https://github.com/rightthumb/rightthumb-widgets-v0
cd rightthumb-widgets-v0
cd install

python3 installer.py -install

After that if you are running Linux
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

in Windows
    a file %USERPROFILE%\rr.bat
        i recommend copying it to %SYSTEMROOT%\System32\rr.bat
    when you open Windows terminal type rr
    or
    in Windows terminal
        "commandline": "cmd /k \"C:\\Users\\Scott\\rr.bat\"",
    
in Linux
    the .bashrc is modified
    NOTHING IS REMOVED!!!
    variables and aliases between ## {E45D09D22184} ## and ## {AEC80B4D3338} ##
    bookmarks cd aliases between ## {42F74F699A95} ## and ## {6D2B143FF720} ##
    VERY EASY TO REMOVE
~~~

## Help

~~~md
Every app has multiple switches per registerd switch.
    Help Switches
        -?, -??, --??, ?, ??, /?, /??, /h, /help, -help, --help

Help that includes global switches (included in all apps).
    p ls ?
Help that is just for that app.
    p ls ??
~~~

## Have a movie drive?

### Auto franchise hierarchy

~~~md
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

~~~md
in Windows
    epyi base -build myApp
Linux
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

To use the ' + ' and ' - ' switches: _.showLine(data)

# example:
    for path in _.isData():
        if _.showLine(path):
            process(path)

Don't forget to try this:
    os=__.imp('os.path.isfile')

~~~

## Note

### The use of '-' dashes in the file names is because framework apps are imported via class

~~~md
example:
    _paste = _.regImp( __.appReg, '-paste' )
~~~

## Automatically profile every app in the framework (including ones you create)

~~~md
first go to the python folder.

The FAST way:
   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p appInfo

The Accurate way
   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p line --c -make "echo {}| p appInfo" | p execute

it saves a json file here:
    widgets/databank/tables/appRegistration.hash
~~~

___

## Website management

To upload a file 'u. index.htm' or 'p site -f index.htm -u' (automatically creating entire necessary folder structure) then if displays the full url to a file (unless it is an index file which it displays cleanly)

- To accomplish this add a file called '.folder.meta' in the site root.
  - It accepts json or yaml
- To encrypt the password, copy it then 'p cryptString -clip' and paste

~~~md
url: https://domain.com
sftp:
  server: domain.com
  user: admin
  password: Uebt27i4dLAT8VxdwcJRd3MWdcdYN2+t2uVNPWnT8sIqeJB4IsJPsQ==
  path: /home/user/public_html
~~~

___
___

## Misc

___
___

## How do I extract stuff from a website?

- method 1
  - Hit 10 on my [mouse](https://www.amazon.com/dp/B088B3ZM76)
  - Say 'scrape table'
- method 2
  - Copy the selector
  - Hit 10 on my [mouse](https://www.amazon.com/dp/B088B3ZM76)
  - Say 'auto text'
- method 3 (beta)
  - Put my mouse over it.
  - Hit 10 on my [mouse](https://www.amazon.com/dp/B088B3ZM76)
  - Say 'auto scrape'
- method 4
  - Use my auto injecting scraping tool (see bellow)

### How to install my scraping tool

- create a new link.
- paste the bellow code as the url.

~~~md
javascript:{ var script = document.createElement('script');script.type = 'text/javascript'; if (location.protocol === 'https:') { script.src = 'https://eyeformeta.com/tools/tool.js'; } else { script.src = 'http://eyeformeta.com/tools/tool.js'; } document.head.appendChild(script);}
~~~

- view the JavaScript console for instructions.
  - example: copy and paste one of the suggestions "hackTool.help( {'tags': 'tables_w_labels'} )" then "copy(hackTool.helper)" and paste in the console.
- Note: I also created a chrome extension that scrapes data from webpages in a variety of formats for instant access in apps. That is what the databank app does.
- Note: Voice commands are managed by using the hotkeys.py app that talks to the listen.py app.

## Dungeons and Dragons app (dnd.py)

Created this when I was learning dnd and python. I have learned a lot since I created this app.

- Manage sorcerer spells
- Categorizes spells as Heal, Hurt, and Help <--
  - Having a battle
    - Look for Hurt, Distance, and Hit Dice <--
- Check a DND website I just started [icosahedron.quest](https://icosahedron.quest/)

## About

~~~md
What if magic existed?
What if a place existed where your every thought and dream come to life.
There is only one catch: it has to be written down.
Such a place exists, it is called programming.
    - Scott Taylor Reph, https://softwaredevelopment.solutions
~~~

[Software Development Solutions](https://softwaredevelopment.solutions/)
