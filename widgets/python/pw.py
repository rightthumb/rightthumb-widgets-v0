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


##################################################
import sys, time
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
    global appDBA;f=__.appName(appDBA,parentApp,childApp);
    if reg:__.appReg=f;
    return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################


def sw():
    pass
    #b)--> examples
    # _.switches.register( 'Input', '-i' )
    #e)--> examples
    # _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
    # 'app': '8facG-jo0Cxk',
    'file': 'pw-gen.py',
    'liveAppName': __.thisApp( __file__ ),
    'description': 'Changes the world',
        # _.ail(1,'subject')+
        # _.aib('one')+
    'categories': [
                        'DEFAULT',
                ],
    'usage': [
                        # 'epy another',
                        # 'e nmap',
                        # '',
    ],
    'relatedapps': [
                        # 'p another -file file.txt',
                        # '',
    ],
    'prerequisite': [
                        # 'p another -file file.txt',
                        # '',
    ],
    'examples': [
                        _.hp('p pw-gen'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
                       # { 'name': 'name', 'abbreviation': 'n' },
                       # { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
    ],
    'aliases': [
                       # 'this',
                       # 'app',
    ],
    'notes': [
                       # {},
    ],
}

_.appData[focus()] = {
        'start': __.startTime,
        'uuid': '',
        'audit': [],
        'pipe': False,
        'data': {
                    'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
                    'table': {'sent': [], 'received': [] },
        },
    }


def triggers():
    _.switches.trigger( 'Files', _.myFileLocations, vs=True )
    _.switches.trigger( 'Ago', _.timeAgo )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'URL', _.urlTrigger )
    _.switches.trigger( 'Duration', _.timeFuture )

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
    #n)--> inline examples
        # if _.switches.isActive('Test'): test(); return None;
        # result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
        # bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
        # a=(1 if True else 0) <--#
        #!)--> m=[[row[i] for row in matrix] for i in range(4)]

    #n)--> python globals
        # for k in globals(): print(k, eval(k) )

    #n)--> webpage from url
        # requests=__.imp('requests.post')
        #!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

    #n)--> import and backup example
        # _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
        # _bk.switch( 'Input', path ); bkfi = _bk.action();

    #n)--> inline
        # for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

    #n)--> banner
        # banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

def load():
    global verbs
    global nouns
    global adjectives
    verbs = ['abandon','abash','abate','abide','absorb','accept','accompany','ache','achieve','acquire','act','add','address','adjust','admire','admit','advise','afford','agree','alight','allow','animate','announce','answer','apologize','appear','applaud','apply','approach','approve','argue','arise','arrange','arrest','ask','assert','assort','astonish','attack','atten','attract','audit','avoid','awake','bang','banish','bash','bat','be','bear','beat','beautify','become','befall','beg','begin','behave','behold','believe','belong','bend','bereave','beseech','bet','betray','bid','bind','bite','bleed','bless','blossom','blow','blur','blush','board','boast','boil','bow','box','bray','break','breathe','breed','bring','broadcast','brush','build','burn','burst','bury','bust','buy','buzz','calculate','call','canvass','capture','caress','carry','carve','cash','cast','catch','cause','cease','celebrate','challenge','change','charge','chase','chat','check','cheer','chew','chide','chip','choke','choose','classify','clean','cleave','click','climb','cling','close','clothe','clutch','collapse','collect','colour','come','comment','compare','compel','compete','complain','complete','conclude','conduct','confess','confine','confiscate','confuse','congratulate','connect','connote','conquer','consecrat','consen','conserve','consider','consign','consist','console','consort','conspire','constitute','constrain','construct','construe','consult','contain','contemn','contend','contest','continue','contract','contradict','contrast','contribute','contrive','control','convene','converge','convers','convert','convey','convict','convince','coo','cook','cool','co-operate','cope','copy','correct','correspon','corrod','corrupt','cost','cough','counsel','count','course','cover','cower','crack','crackle','crash crashed crashed crashes crashing','crave','create','creep','crib','cross','crowd','crush','cry','curb','cure','curve','cut','cycle','damage','damp','dance','dare','dash','dazzle','deal','decay','decide','declare','decorate','decrease','dedicate','delay','delete','deny','depend','deprive','derive','describe','desire','destroy','detach','detect','determine','develop','die','differ','dig','digest','dim','diminish','dine','dip','direct','disappear','discover','discuss','disobey','display','dispose','distribute','disturb','disuse','dive','divide','do','donate','download','drag','draw','dream','dress','drill','drink','drive','drop','dry','dump','dwell','dye','earn','eat','educat','empower','empty','encircle','encourage','encroach','endanger','endorse','endure','engrave','enjoy','enlarge','enlighten','enter','envy','erase','escape','evaporate','exchange','exclaim','exclude','exist','expand','expect','explain','explore','express','extend','eye','face','fail','faint','fall','fan','fancy','favour','fax','feed','feel','ferry','fetch','fight','fill','find','finish','fish','fit','fix','fizz','flap','flash','flee','fling','float','flop','fly','fold','follow','forbid','force','forecast','foretell','forget','forgive','forlese','form','forsake','found','frame','free','freeze','frighten','fry','fulfil','gag','gain','gainsay','gash','gaze','get','give','glance','glitter','glow','go','google','govern','grab','grade','grant','greet','grind','grip','grow','guard','guess','guide','handle','hang','happen','harm','hatch','hate','have','heal','hear','heave','help','hew','hide','hinder','hiss','hit','hoax','hold','hop','hope','horrify','hug','hum','humiliate','hunt','hurl','hurry','hurt','hush','hustle','hypnotize','idealize','identify','idolize','ignite','ignore','ill-treat','illuminate','illumine','illustrate','imagine','imbibe','imitate','immerse','immolate','immure','impair','impart','impeach','impede','impel','impend','imperil','impinge','implant','implicate','implode','implore','imply','import','impose','impress','imprint','imprison','improve','inaugurate','incise','include','increase','inculcate','indent','indicate','induce','indulge','infect','infest','inflame','inflate','inflect','inform','infringe','infuse','ingest','inhabit','inhale','inherit','initiate','inject','injure','inlay','innovate','input','inquire','inscribe','insert','inspect','inspire','install','insult','insure','integrate','introduce','invent','invite','join','jump','justify','keep','kick','kid','kill','kiss','kneel','knit','knock','know','lade','land','last','latch','laugh','lay','lead','leak','lean','leap','learn','leave','leer','lend','let','lick','lie','lift','light','like','limp','listen','live','look','lose','love','magnify','maintain','make','manage','march','mark','marry','mash','match','matter','mean','measure','meet','melt','merge','mew','migrate','milk','mind','mislead','miss','mistake','misuse','mix','moan','modify','moo','motivate','mould','moult','move','mow','multiply','murmur','nail','nap','need','neglect','nip','nod','note','notice','notify','nourish','nurse','obey','oblige','observe','obstruct','obtain','occupy','occur','offer','offset','omit','ooze','open','operate','opine','oppress','opt','optimize','orde','organize','originate','output','overflow','overtake','owe','own','pacify','paint','pardon','part','partake','participate','pass','paste','pat','patch','pause','pay','peep','perish','permit','persuade','phone','place','plan','play','plead','please','plod','plot','pluck','ply','point','polish','pollute','ponder','pour','pout','practise','praise','pray','preach','prefer','prepare','prescribe','present','preserve','preset','preside','press','pretend','prevent','print','proceed','produce','progress','prohibit','promise','propose','prosecute','protect','prove','provide','pull','punish','purify','push','put','qualify','quarrel','question','quit','race','rain','rattle','reach','read','realize','rebuild','recall','recast','receive','recite','recognize','recollect','recur','redo','reduce','refer','reflect','refuse','regard','regret','relate','relax','rely','remain','remake','remove','rend','renew','renounce','repair','repeat','replace','reply','report','request','resell','resemble','reset','resist','resolve','respect','rest','restrain','retain','retch','retire','return','reuse','review','rewind','rid','ride','ring','rise','roar','rob','roll','rot','rub','rule','run','rush','sabotage','sack','sacrifice','sadden','saddle','sag','sail','sally','salute','salvage','salve','sample','sanctify','sanction','sap','saponify','sash','sashay','sass','sate','satiate','satirise','satisfy','saturate','saunter','save','savor','savvy','saw','say','scab','scabble','scald','scale','scam','scan','scant','scar','scare','scarify','scarp','scat','scatter','scold','scorch','scowl','scrawl','scream','screw','scrub','search','seat','secure','see','seek','seem','seize','select','sell','send','sentence','separate','set','sever','sew','shake','shape','share','shatter','shave','shear','shed','shine','shirk','shit','shiver','shock','shoe','shoot','shorten','shout','show','shrink','shun','shut','sight','signal','signify','sing','sink','sip','sit','ski','skid','slam','slay','sleep','slide','slim','sling','slink','slip','slit','smash','smell','smile','smite','smooth','smother','snap','snatch','sneak','sneeze','sniff','soar','sob','solicit','solve','soothe','sort','sow','sparkle','speak','speed','spell','spend','spill','spin','spit','split',' spoil','spray','spread','spring','sprout','squeeze','stand','stare','start','state','stay','steal','steep','stem','step','sterilize','stick','stimulate','sting','stink','stir','stitch','stoop','stop','store','strain','stray','stress','stretch','strew','stride','strike','string','strive','study','submit','subscribe','subtract','succeed','suck','suffer','suggest','summon','supply','support','suppose','surge','surmise','surpass','surround','survey','survive','swallow','sway','swear','sweat','sweep','swell','swim','swing','swot','take','talk','tap','taste','tax','teach','tear','tee','tell','tempt','tend','terminate','terrify','test','thank','think','thrive','throw','thrust','thump','tie','tire','toss','touch','train','trampl','transfer','transform','translate','trap','travel','tread','treasure','treat','tree','tremble','triumph','trust','try','turn','type','typeset','understand','undo','uproot','upset','urge','use','utter','value','vanish','vary','verify','vex','vie','view','violate','vomit','wake','walk','wander','want','warn','waste','watch','water','wave','wax','waylay','wear','weave','wed','weep','weigh','welcome','wet','whip','whisper','win','wind','wish','withdraw','work','worry','worship','wring','write','yawn','yell','yield','zinc','zoom']
    nouns = ['account','achiever','acoustics','act','action','activity','actor','addition','adjustment','advertisement','advice','aftermath','afternoon','afterthought','agreement','air','airplane','airport','alarm','amount','amusement','anger','angle','animal','answer','ant','ants','apparatus','apparel','apple','apples','appliance','approval','arch','argument','arithmetic','arm','army','art','attack','attempt','attention','attraction','aunt','authority','babies','baby','back','badge','bag','bait','balance','ball','balloon','balls','banana','band','base','baseball','basin','basket','basketball','bat','bath','battle','bead','beam','bean','bear','bears','beast','bed','bedroom','beds','bee','beef','beetle','beggar','beginner','behavior','belief','believe','bell','bells','berry','bike','bikes','bird','birds','birth','birthday','bit','bite','blade','blood','blow','board','boat','boats','body','bomb','bone','book','books','boot','border','bottle','boundary','box','boy','boys','brain','brake','branch','brass','bread','breakfast','breath','brick','bridge','brother','brothers','brush','bubble','bucket','building','bulb','bun','burn','burst','bushes','business','butter','button','cabbage','cable','cactus','cake','cakes','calculator','calendar','camera','camp','can','cannon','canvas','cap','caption','car','card','care','carpenter','carriage','cars','cart','cast','cat','cats','cattle','cause','cave','celery','cellar','cemetery','cent','chain','chair','chairs','chalk','chance','change','channel','cheese','cherries','cherry','chess','chicken','chickens','children','chin','church','circle','clam','class','clock','clocks','cloth','cloud','clouds','clover','club','coach','coal','coast','coat','cobweb','coil','collar','color','comb','comfort','committee','company','comparison','competition','condition','connection','control','cook','copper','copy','cord','cork','corn','cough','country','cover','cow','cows','crack','cracker','crate','crayon','cream','creator','creature','credit','crib','crime','crook','crow','crowd','crown','crush','cry','cub','cup','current','curtain','curve','cushion','dad','daughter','day','death','debt','decision','deer','degree','design','desire','desk','destruction','detail','development','digestion','dime','dinner','dinosaurs','direction','dirt','discovery','discussion','disease','disgust','distance','distribution','division','dock','doctor','dog','dogs','doll','dolls','donkey','door','downtown','drain','drawer','dress','drink','driving','drop','drug','drum','ducks','dust','ear','earth','earthquake','edge','education','effect','egg','eggnog','eggs','elbow','end','engine','error','event','example','exchange','existence','expansion','experience','expert','eye','eyes','face','fact','fairies','fall','family','fan','fang','farm','farmer','father','father','faucet','fear','feast','feather','feeling','feet','fiction','field','fifth','fight','finger','finger','fire','fireman','fish','flag','flame','flavor','flesh','flight','flock','floor','flower','flowers','fly','fog','fold','food','foot','force','fork','form','fowl','frame','friction','friend','friends','frog','frogs','front','fruit','furniture','alley','game','garden','gate','geese','ghost','giants','giraffe','girl','girls','glass','glove','glue','goat','gold','goldfish','good-bye','goose','government','governor','grade','grain','grandfather','grandmother','grape','grass','grip','ground','group','growth','guide','guitar','gun','hair','haircut','hall','hammer','hand','hands','harbor','harmony','hat','hate','head','health','hearing','heart','heat','help','hen','hill','history','hobbies','hole','holiday','home','honey','hook','hope','horn','horse','horses','hose','hospital','hot','hour','house','houses','humor','hydrant','ice','icicle','idea','impulse','income','increase','industry','ink','insect','instrument','insurance','interest','invention','iron','island','jail','jam','jar','jeans','jelly','jellyfish','jewel','join','joke','journey','judge','juice','jump','K','','kettle','key','kick','kiss','kite','kitten','kittens','kitty','knee','knife','knot','knowledge','laborer','lace','ladybug','lake','lamp','land','language','laugh','lawyer','lead','leaf','learning','leather','leg','legs','letter','letters','lettuce','level','library','lift','light','limit','line','linen','lip','liquid','list','lizards','loaf','lock','locket','look','loss','love','low','lumber','lunch','lunchroom','machine','magic','maid','mailbox','man','manager','map','marble','mark','market','mask','mass','match','meal','measure','meat','meeting','memory','men','metal','mice','middle','milk','mind','mine','minister','mint','minute','mist','mitten','mom','money','monkey','month','moon','morning','mother','motion','mountain','mouth','move','muscle','music','nail','name','nation','neck','need','needle','nerve','nest','net','news','night','noise','north','nose','note','notebook','number','nut','oatmeal','observation','ocean','offer','office','oil','operation','opinion','orange','oranges','order','organization','ornament','oven','owl','page','pail','pain','paint','pan','pancake','paper','parcel','parent','park','part','partner','party','passenger','paste','patch','payment','peace','pear','pen','pencil','person','pest','pet','pets','pleasure','plot','plough','pocket','point','poison','police','polish','pollution','popcorn','porter','position','pot','potato','powder','power','price','print','prison','process','produce','profit','property','prose','protest','pull','pump','punishment','purpose','push','quarter','quartz','queen','question','quicksand','quiet','quill','quilt','quince','quiver','rabbit','rabbits','rail','railway','rain','rainstorm','rake','range','rat','rate','ray','reaction','reading','reason','receipt','recess','record','regret','relation','religion','representative','request','respect','rest','reward','rhythm','rice','riddle','rifle','ring','rings','river','road','robin','rock','rod','roll','roof','room','root','rose','route','rub','rule','run','sack','sail','salt','sand','scale','scarecrow','scarf','scene','scent','school','science','scissors','screw','sea','seashore','seat','secretary','seed','selection','self','sense','servant','shade','shake','shame','shape','sheep','sheet','shelf','ship','shirt','shock','shoe','shoes','shop','show','side','sidewalk','sign','silk','silver','sink','sister','sisters','size','skate','skin','skirt','sky','slave','sleep','sleet','slip','slope','smash','smell','smile','smoke','snail','snails','snake','snakes','sneeze','snow','soap','society','sock','soda','sofa','son','song','songs','sort','sound','soup','space','spade','spark','spiders','sponge','spoon','spot','spring','spy','square','squirrel','stage','stamp','star','start','statement','station','steam','steel','stem','step','stew','stick','sticks','stitch','stocking','stomach','stone','stop','store','story','stove','stranger','straw','stream','street','stretch','string','structure','substance','sugar','suggestion','suit','summer','sun','support','surprise','sweater','swim','swing','system','table','tail','talk','tank','taste','tax','team','teeth','temper','tendency','tent','territory','test','texture','theory','thing','things','thought','thread','thrill','throat','throne','thumb','thunder','ticket','tiger','time','tin','title','toad','toe','toes','tomatoes','tongue','tooth','toothbrush','toothpaste','top','touch','town','toy','toys','trade','trail','train','trains','tramp','transport','tray','treatment','tree','trees','trick','trip','trouble','trousers','truck','trucks','tub','turkey','turn','twig','twist','umbrella','uncle','underwear','unit','use','vacation','value','van','vase','vegetable','veil','vein','verse','vessel','vest','view','visitor','voice','volcano','volleyball','voyage','walk','wall','war','wash','waste','watch','water','wave','waves','wax','way','wealth','weather','week','weight','wheel','whip','whistle','wilderness','wind','window','wine','wing','winter','wire','wish','woman','women','wood','wool','word','work','worm','wound','wren','wrench','wrist','writer','writing','yam','yard','yarn','year','yoke','zebra','zephyr','zinc','zipper','zoo']
    adjectives = ['aback','abaft','abandoned','abashed','aberrant','abhorrent','abiding','abject','ablaze','able','abnormal','aboard','aboriginal','abortive','abounding','abrasive','abrupt','absent','absorbed','absorbing','abstracted','absurd','abundant','abusive','acceptable','accessible','accidental','accurate','acid','acidic','acoustic','acrid','actually','ad hoc','adamant','adaptable','addicted','adhesive','adjoining','adorable','adventurous','afraid','aggressive','agonizing','agreeable','ahead','ajar','alcoholic','alert','alike','alive','alleged','alluring','aloof','amazing','ambiguous','ambitious','amuck','amused','amusing','ancient','angry','animated','annoyed','annoying','anxious','apathetic','aquatic','aromatic','arrogant','ashamed','aspiring','assorted','astonishing','attractive','auspicious','automatic','available','average','awake','aware','awesome','awful','axiomatic','bad','barbarous','bashful','bawdy','beautiful','befitting','belligerent','beneficial','bent','berserk','best','better','bewildered','big','billowy','bite-sized','bitter','bizarre','black','black-and-white','bloody','blue','blue-eyed','blushing','boiling','boorish','bored','boring','bouncy','boundless','brainy','brash','brave','brawny','breakable','breezy','brief','bright','bright','broad','broken','brown','bumpy','burly','bustling','busy','cagey','calculating','callous','calm','capable','capricious','careful','careless','caring','cautious','ceaseless','certain','changeable','charming','cheap','cheerful','chemical','chief','childlike','chilly','chivalrous','chubby','chunky','clammy','classy','clean','clear','clever','cloistered','cloudy','closed','clumsy','cluttered','coherent','cold','colorful','colossal','combative','comfortable','common','complete','complex','concerned','condemned','confused','conscious','cooing','cool','cooperative','coordinated','courageous','cowardly','crabby','craven','crazy','creepy','crooked','crowded','cruel','cuddly','cultured','cumbersome','curious','curly','curved','curvy','cut','cute','cute','cynical','daffy','daily','damaged','damaging','damp','dangerous','dapper','dark','dashing','dazzling','dead','deadpan','deafening','dear','debonair','decisive','decorous','deep','deeply','defeated','defective','defiant','delicate','delicious','delightful','demonic','delirious','dependent','depressed','deranged','descriptive','deserted','detailed','determined','devilish','didactic','different','difficult','diligent','direful','dirty','disagreeable','disastrous','discreet','disgusted','disgusting','disillusioned','dispensable','distinct','disturbed','divergent','dizzy','domineering','doubtful','drab','draconian','dramatic','dreary','drunk','dry','dull','dusty','dusty','dynamic','dysfunctional','eager','early','earsplitting','earthy','easy','eatable','economic','educated','efficacious','efficient','eight','elastic','elated','elderly','electric','elegant','elfin','elite','embarrassed','eminent','empty','enchanted','enchanting','encouraging','endurable','energetic','enormous','entertaining','enthusiastic','envious','equable','equal','erect','erratic','ethereal','evanescent','evasive','even','excellent','excited','exciting','exclusive','exotic','expensive','extra-large','extra-small','exuberant','exultant','fabulous','faded','faint','fair','faithful','fallacious','false','familiar','famous','fanatical','fancy','fantastic','far','far-flung','fascinated','fast','fat','faulty','fearful','fearless','feeble','feigned','female','fertile','festive','few','fierce','filthy','fine','finicky','first','five','fixed','flagrant','flaky','flashy','flat','flawless','flimsy','flippant','flowery','fluffy','fluttering','foamy','foolish','foregoing','forgetful','fortunate','four','frail','fragile','frantic','free','freezing','frequent','fresh','fretful','friendly','frightened','frightening','full','fumbling','functional','funny','furry','furtive','future','futuristic','fuzzy','gabby','gainful','gamy','gaping','garrulous','gaudy','general','gentle','giant','giddy','gifted','gigantic','glamorous','gleaming','glib','glistening','glorious','glossy','godly','good','goofy','gorgeous','graceful','grandiose','grateful','gratis','gray','greasy','great','greedy','green','grey','grieving','groovy','grotesque','grouchy','grubby','gruesome','grumpy','guarded','guiltless','gullible','gusty','guttural','habitual','half','hallowed','halting','handsome','handsomely','handy','hanging','hapless','happy','hard','hard-to-find','harmonious','harsh','hateful','heady','healthy','heartbreaking','heavenly','heavy','hellish','helpful','helpless','hesitant','hideous','high','highfalutin','high-pitched','hilarious','hissing','historical','holistic','hollow','homeless','homely','honorable','horrible','hospitable','hot','huge','hulking','humdrum','humorous','hungry','hurried','hurt','hushed','husky','hypnotic','hysterical','icky','icy','idiotic','ignorant','ill','illegal','ill-fated','ill-informed','illustrious','imaginary','immense','imminent','impartial','imperfect','impolite','important','imported','impossible','incandescent','incompetent','inconclusive','industrious','incredible','inexpensive','infamous','innate','innocent','inquisitive','insidious','instinctive','intelligent','interesting','internal','invincible','irate','irritating','itchy','jaded','jagged','jazzy','jealous','jittery','jobless','jolly','joyous','judicious','juicy','jumbled','jumpy','juvenile','kaput','keen','kind','kindhearted','kindly','knotty','knowing','knowledgeable','known','labored','lackadaisical','lacking','lame','lamentable','languid','large','last','late','laughable','lavish','lazy','lean','learned','left','legal','lethal','level','lewd','light','like','likeable','limping','literate','little','lively','living','lonely','long','longing','long-term','loose','lopsided','loud','loutish','lovely','loving','low','lowly','lucky','ludicrous','lumpy','lush','luxuriant','lying','lyrical','macabre','macho','maddening','madly','magenta','magical','magnificent','majestic','makeshift','male','malicious','mammoth','maniacal','many','marked','massive','married','marvelous','material','materialistic','mature','mean','measly','meaty','medical','meek','mellow','melodic','melted','merciful','mere','messy','mighty','military','milky','mindless','miniature','minor','miscreant','misty','mixed','moaning','modern','moldy','momentous','motionless','mountainous','muddled','mundane','murky','mushy','mute','mysterious','naive','nappy','narrow','nasty','natural','naughty','nauseating','near','neat','nebulous','necessary','needless','needy','neighborly','nervous','new','next','nice','nifty','nimble','nine','nippy','noiseless','noisy','nonchalant','nondescript','nonstop','normal','nostalgic','nosy','noxious','null','numberless','numerous','nutritious','nutty','oafish','obedient','obeisant','obese','obnoxious','obscene','obsequious','observant','obsolete','obtainable','oceanic','odd','offbeat','old','old-fashioned','omniscient','one','onerous','open','opposite','optimal','orange','ordinary','organic','ossified','outgoing','outrageous','outstanding','oval','overconfident','overjoyed','overrated','overt','overwrought','painful','painstaking','pale','paltry','panicky','panoramic','parallel','parched','parsimonious','past','pastoral','pathetic','peaceful','penitent','perfect','periodic','permissible','perpetual','petite','petite','phobic','physical','picayune','pink','piquant','placid','plain','plant','plastic','plausible','pleasant','plucky','pointless','poised','polite','political','poor','possessive','possible','powerful','precious','premium','present','pretty','previous','pricey','prickly','private','probable','productive','profuse','protective','proud','psychedelic','psychotic','public','puffy','pumped','puny','purple','purring','pushy','puzzled','puzzling','quack','quaint','quarrelsome','questionable','quick','quickest','quiet','quirky','quixotic','quizzical','rabid','racial','ragged','rainy','rambunctious','rampant','rapid','rare','raspy','ratty','ready','real','rebel','receptive','recondite','red','redundant','reflective','regular','relieved','remarkable','reminiscent','repulsive','resolute','resonant','responsible','rhetorical','rich','right','righteous','rightful','rigid','ripe','ritzy','roasted','robust','romantic','roomy','rotten','rough','round','royal','ruddy','rude','rural','rustic','ruthless','sable','sad','safe','salty','same','sassy','satisfying','savory','scandalous','scarce','scared','scary','scattered','scientific','scintillating','scrawny','screeching','second','second-hand','secret','secretive','sedate','seemly','selective','selfish','separate','serious','shaggy','shaky','shallow','sharp','shiny','shivering','shocking','short','shrill','shut','shy','sick','silent','silent','silky','silly','simple','simplistic','sincere','six','skillful','skinny','sleepy','slim','slimy','slippery','sloppy','slow','small','smart','smelly','smiling','smoggy','smooth','sneaky','snobbish','snotty','soft','soggy','solid','somber','sophisticated','sordid','sore','sore','sour','sparkling','special','spectacular','spicy','spiffy','spiky','spiritual','spiteful','splendid','spooky','spotless','spotted','spotty','spurious','squalid','square','squealing','squeamish','staking','stale','standing','statuesque','steadfast','steady','steep','stereotyped','sticky','stiff','stimulating','stingy','stormy','straight','strange','striped','strong','stupendous','stupid','sturdy','subdued','subsequent','substantial','successful','succinct','sudden','sulky','super','superb','superficial','supreme','swanky','sweet','sweltering','swift','symptomatic','synonymous','taboo','tacit','tacky','talented','tall','tame','tan','tangible','tangy','tart','tasteful','tasteless','tasty','tawdry','tearful','tedious','teeny','teeny-tiny','telling','temporary','ten','tender','tense','tense','tenuous','terrible','terrific','tested','testy','thankful','therapeutic','thick','thin','thinkable','third','thirsty','thirsty','thoughtful','thoughtless','threatening','three','thundering','tidy','tight','tightfisted','tiny','tired','tiresome','toothsome','torpid','tough','towering','tranquil','trashy','tremendous','tricky','trite','troubled','truculent','true','truthful','two','typical','ubiquitous','ugliest','ugly','ultra','unable','unaccountable','unadvised','unarmed','unbecoming','unbiased','uncovered','understood','undesirable','unequal','unequaled','uneven','unhealthy','uninterested','unique','unkempt','unknown','unnatural','unruly','unsightly','unsuitable','untidy','unused','unusual','unwieldy','unwritten','upbeat','uppity','upset','uptight','used','useful','useless','utopian','utter','uttermost','vacuous','vagabond','vague','valuable','various','vast','vengeful','venomous','verdant','versed','victorious','vigorous','violent','violet','vivacious','voiceless','volatile','voracious','vulgar','wacky','waggish','waiting','wakeful','wandering','wanting','warlike','warm','wary','wasteful','watery','weak','wealthy','weary','well-groomed','well-made','well-off','well-to-do','wet','whimsical','whispering','white','whole','wholesale','wicked','wide','wide-eyed','wiggly','wild','willing','windy','wiry','wise','wistful','witty','woebegone','womanly','wonderful','wooden','woozy','workable','worried','worthless','wrathful','wretched','wrong','wry','xenophobic','yellow','yielding','young','youthful','yummy','zany','zealous','zesty','zippy','zonked']


def ranUp(text):
    'random single uppercase char'
    r=random.randint(1, len(text)-1)
    while not text[r] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        r=random.randint(1, len(text)-1)
    result=''
    for i, ch in enumerate(text):
        if i == r:
            result+=ch.upper()
        else:
            result+=ch
    return result


def gen():
    global verbs
    global nouns
    global adjectives
    return ranUp(random.choice(verbs)+'_'+random.choice(nouns)+'_'+random.choice(adjectives))+random.choice(list('0123456789'))+random.choice(list('0123456789'))+random.choice(list('!@#$%'))

def action():
    load()
    i=0
    while not i == 100:
        i+=1
        _.pr( gen() )
        



import random

##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
    #b)--> examples

    # banner.pr()
    # if len(_.switches.all())==0: banner.gossip()

    #e)--> examples
    action()
    _.isExit(__file__)


