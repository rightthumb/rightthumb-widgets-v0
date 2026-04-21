import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Invalid', '-i,-invalid' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

email_list = '''
E-mail Address
DGoldstein@cbizgl.com
vpalma@berenfeldllp.com
tony@odcpa.com
sfriend@rachlin.com
SSTILWELL@DELOITTE.COM
dlain@lgt-cpa.com
Cthompson@lgt-cpa.com
avasquez@mdd.net
bmitchellette@larsonallen.com
apeiser@gppcpa.com
agmartin@weaverandtidwell.com
amoench@cbiz.com
andyp@savillecpa.com
angela.gilbert@us.pwc.com
becky.vela@wpcpa.com
bmorgan@hmpc.com
flyboy@guinnsmith.com
bobterada@mossadams.com
brhodes@roco-cpa.com
Braden@philipvogel.com
Dhenry@deloitte.com
ddbranch@weaverandtidwell.com
doug.dedrick@ey.com
edrews@kbagroupllp.com
edavidson@deloitte.com
fsmith@jtsco.com
gmayberry@deloitte.com
gregs@ppglc.com
hreckord@lemasterdaniels.com
hperkins@pdshcpas.com
jsiedhoff@kshd.com
jbovard@turnerstone.com
blue@kcoe.com
Jena.lysen@aghlc.com
jemonahan@deloitte.com
jworley@philipvogel.com
jerry.capps@aghlc.com
enystrom@traviswolff.com
Jdenny@coleandreed.com
jim.howard@jhcpa.com
jimh@haskinscpa.com
jgarvey@Taxsmart.com
jlitzler@lssmllp.com
jsteffes@bkd.com
john@sfcllp.com
jwagner@wencpa.com
jbraly@deloitte.com
jfry@salmonbeach.com
kelly.Haynie@ey.com
kkalsey@bkd.com
Dan Lain
lking@bkd.com
lvanhorn@bkd.com
laura.c.bruemmer@us.pwc.com
laurie.malecki@ey.com
lfry@dixon-hughes.com
Linda.harrison@foxbyrd.com
matrujillo@deloitte.com
mvs@houston-tx-cpa.com
mklepp@lgt-cpa.com
mstackowicz@bdo.com
mbe@eepb.com
mike@jaincpa.com
Email
LindquistN@millergrossbard.com
nwilner@cbiz.com
Omar.Ahmad@wpcpa.com
pmelton@melton-melton.com
pat.m@cpamurray.com
Michelle.Griffin@weaverllp.com
pgrossbard@millergrossbard.com
Paulaa@bh-co.com
dianem@bh-co.com
pdemartin@deloitte.com
portia@haggerty-cpa.com
rhea.windon@gt.com
Robert.E.Conrad@us.pwc.com
Ron.Simpson@mossadams.com
ronee.l.gawrych@us.pwc.com
rusty@pskcpa.com
scott@bbsbinc.com
svhenry@henryheld.com
snueno@bvccpa.com
srunkel@uhy-us.com
tbryant@deloitte.com
Teri.Linder@GT.com
eDrews@bkd.com
Tstephen@tvscompany.com
Tiffany@mossadams.com
tom.beers@rsmi.com
Tomc@cfllp.com
tom.montgomery@mcggroup.com
Trina.Kilpatrick@rsmi.com
trinakilpatrick@rsmi.com
veronica.n.strahan@us.pwc.com
mkane@kanecpas.com
rgoldberg@kglc.com
paula@hhcbfl.com
paulb@schweitzercpa.com
mikeb@bollenback.com
ebunch@spencemarston.com
JCarlstedt@cjnw.net
cgilman@lbrllc.com
bhans@crowncpas.com
cmoody@mslcpa.com
JSmethurst@cbizkrmt.com
bprice@pdr-cpa.com
pteal@drtcpa.com
sfullmer@brcpaweb.com
ghernandez@Larsonallen.com
MBrushwood@cbh.com
anash@cricpa.com
Kbowyer@osullivancreel.com
sheller@thegriggsgroup.com
hbg@hbgcpa.com
pdccpa@bellsouth.net
shealy@ralston.com
jayportnoy@portnoyshainbrown.com
ldk@purvisgray.com
jfs@mswcpa.com
jshelton@sdnllp.com
mshorstein@shorstein.com
ssimonic@simonic.net
john@stevens-powell-cpa.com
kwhite@thelbagroup.com
pbeauvie@bouvierassoc.com
pearkas@mossadams.com
npendell@mossadams.com
lkuehler@bkc-cpa.net
todd@baldwinaccountingcpa.com
lBierbrunner@bermanhopkins.com
jcross@cfrcpa.com
jrapp@grjoc.com
Mglickstein@glccpa.com
sdavis@krgg.com
bk@orlandocpa.net
Korsolits@larsonallen.com
don@lemastus.com
jlee@lfharris.com
kcanzoneri@mcdirmitdavis.com
ronperson@osburnhenning.com
petet@tattersall.com
vtaylor@tlh-cpa.com
jmartinez@moacpa.com
al@ruggieromartinez.com
dbolerjack@bkacpa.com
jaren@jbrauncpa.com
gkeyes@keyes-stange.com
olivaricpa@cfl.rr.com
gsmith@cohensmithcpas.com
lbalaban@bscpas.net
kbobbitt@bobbittpittenger.com
steve.brettholtz@mbcopa.com
Clh@cavanaugh-co.com
recpa@cpa-associates.com
levans@hbkcpa.com
gmarkham@markham-norton.com
mike@lbgcpa.com
rlane@kbgrp.com
jmercuiro@mbcpas.com
jwelch@purvisgray.com
norman@suplee-shea.com
byron@cpabiz.com
rstanell@cslcpa.com
johns@stroemercpa.com
thompson@hughessnell.com
kwalker@gewcpa.com
srwhitley@wwrecpa.com
Brian@BrammerandYeend.cpa.pro
jwarren@rcco.com
jcole@cepcpa.com
abragano@concannonmiller.com
schristie@gsscpa.com
foelgner@frscpa.com
lortiz@garciaOrtiz.com
hbrock@tbc-cpa.com
dhallock@thf-cpa.com
Alexam@jmco.com
mschaeffer@cricpa.com
AWhite@brcpaweb.com
KGardner@lbgcpa.com
KDouglass@Yostcpa.com
trobinson@cricpa.com
info@bca-cpa.com
lbassham@grosscollins.com
jabbey@metcalf-davis.com
CBell@pkm.com
nick.chafin@tcc-cpa.com
klynn@cricpa.com
Staylor@smith-howard.com
gail.white@reznickgroup.com
Diane.pippin@Reznickgroup.com
tjupille@gursey.com
rbelcher@singerlewak.com
cosaki@rbz.com
eharris@windes.com
m_figueroa@vasquezcpa.com
shillendahl@jhcohn.com
dianajones@bhjllp.com
dagoff@matson-isom.com
ogren@lymscpa.com
lmason@mswft.com
mgkaplan@millerkaplan.com
lchez@larsonallen.com
lbaerson@bwpbr.com
jarnol@koscpa.com
dfortman@weisscpa.com
Scoyle@coyleassociates.com
mdemarco@dklcpa.com
jmowery@msllc.com
waynesilv@aol.com
Lweitz@mannweitz.com
RP@pickercpa.com
mblanski@gbbcpa.com
vince@ekjllp.com
Wsc@ctm-cpa.com
jdahl@ecsfinancial.com
mjrobinson@rrpltd.com
dan.persico@mcgladrey.com
pmerkel@bk-cpa.com
tjordan@dhjj.com
DPerry@fhassoc.com
Jrobertson@bfr-cpa.com
aweatherhead@frronline.com
Marcc@kebcpa.com
bud@mhfa.net
sreed@meadenmoore.com
rmax@millercooper.com
swonnell@orba.com
vbutler@vbandc.org
mikeb@ssh-cpa.com
ken.masick@wolfco-fs.com
rsinger@gascpa.com
tweber@hwpc.com
Rrome@romeassoc.com
jvukas@rnco.com
jameshilljr@hilltaylorllc.com
bwrubel@marquetteassociates.com
mliccar@liccar.com
TMoreno@virchowkrause.com
mcarroll@lgt-cpa.com
pkaufman@traviswolff.com
rthomas@sstcpa.com
srogut@bnkj.com
nbach@bjmco.com
gellison@bfwcpa.com
cbrewington@bdo.com
bschimler@cbh.com
mperling@bmmcpa.com
rbrooks@bca-cpa.com
bcarmichael@cbtcpa.com
Bmcfadden@cricpa.com
MRP@Cavanaugh-co.com
kgrider@cmgccpa.com
winimust@gmail.com
dakridge@citadelwealthcare.com
rwilliams@ddfcpas.com
rgalanti@galanticpa.com
rgard@glcpas.net
nancy.gery@hawcpa.com
Chuck@hvs-cpas.com
charleshendry@decosimo.com
dhouston@houstoncompanycpa.com
amt@joneskolb.com
skirschner@kircpa.com
al.lindsey@lindseygroup.com
dmccollough@mallahfurman.com
tmarsh@mm-cpa.com
Charlie@MarshallJones.com
ewolf@mjcpa.com
Marni.Rozen@rsmi.com
carnone@moorecolson.com
astarnes@moorecolson.com
Jean@moore-cubb.com
searp@mstiller.com
ghayes@mstiller.com
Blee@mstiller.com
jerry@morehouse-cpa.com
danowens@owensandowens.net
dsessions@pkm.com
dan@postcpas.com
dieter.elsner@roedlusa.com
jlake@rms-cpas.com
dyoung@rybd.com
lee@Romecpa.com
jclements@dobbscpas.com
gpace@resjcpas.com
Roger@Santicpa.com
aclark@smithadcock.com
pobrien@smith-howard.com
junderwood@t-u.com
wendell.causey@tcc-cpa.com
cjones@wsmf.com
jmartinez@watskymartinez.com
don@wpg-inc.com
scott@wjrcpas.com
jburak@wblcpa.com
angelal@wilsonlewis.com
dconrad@deloitte.com
JEWEAVER@bkd.com
"cmeeks@uhy-us.com
mfields@pkftexas.com
soconnor@doz.net
tom@phfcpas.com
mstover@meridiancpas.com
roger@edcpa.com
lcrull@whitinger.com
lnunn@nunncpas.com
stevee@bgbc.com
eabel@blueandco.com
sdauby@doz.net
Bshepard@bcs-cpa.com
bgoelz@mslc.com
dbutler@somersetcpas.com
jwilliams@CWMCF.com
ndallas@dcs-cpa.com
simler@eicpa.com
bhufford@huffordfinancial.com
jschick@kbparrish.com
larry@khscpa.com
wmckinney@kcpag.com
mstover@muphycopc.com
Rlamberjack@noblecon.net
John@psw-cpa.com
choward@rjpile.com
Bschneider@titus-us.com
bob@teipencpa.com
rzurface@lmhcpa.com
abrosche@jaxcpa.com
pittman@ralston.com
chamilton@osullivancreel.com
Btsmith@dixon-hughes.com
g.massey@larsonallen.com
scook@hpg.com
LHill@CostelloHill.com
dham@boscpa.com
sbumpus@cricpa.com
ric@rrcoxcpa.com
acoleman@bdo.com
d.daniel@danielratliff.com
Sissy.Bennett@dhgllp.com
ed@elcpa.com
cgreer@gwllp.com
rvance@vfgcpa.com
ebarrow@elbarrow.com
felmore@frankelmorecpa.com
joan@blackmansloop.com
sbrendle@brendleshaffner.com
kennybrown@brownjenkinsco.com
Scott@butlerandburkecpa.com
mborden@cannon.bz
jsills@dpgcpa.com
kfalls@efrcpa.com
dsaunders@sstcpas.com
frobinson@brccpa.com
george.breslow@breslowstarling.com
mgillis@dmj.com
dleeper@Lkrcpa.com
cgporter@porterandco.com
hheavner@sharrardmcgee.com
ksmith@smithleonardcpas.com
jneal@nbt-cpa.com
shancock@tktk.com
diane.linfors@nelsonandcompany.com
Benh@jpspa.com
hcole@gk-cpa.com
pittman@atallencpa.com
froberts@btrcpa.com
Chris.Galazka@cliftoncpa.com
lyoquelet@hpg.com
dlambert@jlco.com
jmcmillan@mpcllp.com
hwhite@stancilcpa.com
cliff.thomas@tjtpa.com
janet@rrcoxcpa.com
debbie.dancy@resznickgroup.com
bsherbert@sherbertgroup.com
mimcdevitt@bdo.com
cFraiman@pwcpa.com
rmicera@mwellp.com
__ahart@markspaneth.com
Aschor@pnfwllp.com
rfisher@eisnerllp.com
JAgranoff@friedmanllp.com
rcho@gellerco.com
cbonocore@grassicpas.com
afrazia@hhrllp.com
alucrezia@weiserllp.com
Paul.sherman@mkllp.com
pwilson@nsllpcpa.com
adm@jrllc.com
peichler@rem-co.com
julie.becht@freedmaxick.com
dperri@lazarcpa.com
maroyo@pragerfenton.com
jwaters@sb-cpa.com
rreitman@cgscpa.com
lcurran@comdcpa.com
dnagle@constantinusa.com
jzimbalist@eisnerlubin.com
jroter@hechtcpa.com
irubenstein@ere-cpa.com
kmcgill@khhcpas.com
istrassberg@rogoff.com
portiz@tcbawatsonrice.com
glavin@wslco.com
lzamora@metisgroupllc.com
Herbert.Harriott@mitchelltitus.ey.com
knolan@avz.com
ktaylor@berdonllp.com
lbierbrunner@bermanhopkins.com
cottrill@gccpa.com
ronperson@awdoh-cpa.com
ceddy@cricpa.com
dgoode@hoyman.com
izzyjas1@verizon.net
mwhitehurst@purvisgray.com
rduncan@bgcllc.com
bjohnstone@jstonercpa.com
ken.martin@martinsmithcpas.com
tmckinley@mckinleycooper.com
dwking@psbkcpas.com
steve.cooper@roedlusa.com
cdavis@argypc.com
tcaruso@carusoandcompany.com
eberman@bermancpas.com
dgoldstein@goldsteinlewin.com
tony@graucpa.com
bende@rem-co.com
Madorno@sflcpa.com
andy@burtoncpa.com
michael.schwartz@jsw-cpa.com
stevek@kgacpa.com
sdavis@sdavis.com
Cfa@arazoza.com
jonathan@acc-cpa.com
lynnh@bsss-cpa.com
carlc@cbaj.com
stewart@appelrouth.com
bforshee@forsheelockwood.com
rgarcia@gemco-cpa.com
carlos.garcia@gsplh.com
ajordan@jordancastellon.com
Raymond.zomerfeld@vgzcpa.com
oaverdeja@v-dcpa.com
tfa@ahearncpa.com
recruiting@berenfeldllp.com
amezadieu@dbllp.com
dfalkins@falkinsandcompany.com
dzugman@gzwpcpa.com
kimberly@hackerjohnson.com
joe.leo@kmccpa.com
TWeintraub@bsss-cpa.com
LAG@AINGRUDA.COM
darty@acfm-cpa.com
abinstock@braae.com
bloom@bloomgettis.com
sdohan@uscpa.com
aalvarez@efacpa.com
rcp@gprco-cpa.com
gperez821@aol.com
lhubert@mallahfurman.com
nmckee@mpcf.com
Ajsilvercap@earthlink.com
jgutierrez@mbafcpa.com
hmuskat@psms-cpa.com
audit@skjnet.com
dks@sbccpa.com
gmitchell@cdlcpa.com
NMargagliano@cdlcpa.com
marty@casslevy.com
mmartin@dbmscpa.com
djthomas@holyfieldandthomas.com
chuckl@lkdcpa.com
ddiaz@rampell.com
stempleton@templetonco.com
Paul@smythhauckcpa.com
michael.kohner@wtas.com
tcole@smolin.com
hblakiston@jupitercpas.com
greggmccumber@bmctexas.com
bjr@hbacpa.com
ccascos@pbhcpa.com
jshephard@cjw-cpa.com
Robert_Fox@fieldsnemec.com
rpark@parkcpas.com
jim@rssco.com
jewing@elecpa.com
jharte@hartsilva-cpa.com
jls@sfvw.net
jroach@amdcpa.com
hrosen@connerash.com
bgilmore@bwtpcpa.com
ibergman@bergman-schraier.com
jfoster@bswllc.com
bob@hbclp.com
Ghannon@hrh-advantage.com
jmaloneyjr@kpmg.com
sengelbrecht@larsonallen.com
fflegel@lopataflegel.com
cluther@Maherco.com
mprost@mppw.com
bsoderstrom@wnnpc.com
jjabouri@sjcpa.com
jtreloar@stcpa.com
kmchugh@stonecarlie.com
wzielinski@zielinskico.com
aherron@frscpa.com
chollifield@rushtonandcompany.com
rbracell@batescarter.com
anast@cricpa.com
larry@shaubcpagroup.com
Marmbruster@s-a-cpa.com
mscott@cricpa.com
rgasiewicz@dopkins.com
tbonadio@bonadio.com
dberry@navintconsulting.com
jrotenberge@efprotenberg.com
JShehane@swlco.com
grady@houghcpa.com
vpetti@bgrcpas.com
jdavis@djkrcpa.com
hholton@afnw.com
emullen@mswspa.com
lpietras@gma-cpa.com
Lregan@s1services.com
Wross@stegman.com
lsacks@stkcpa.com
PSmith@swlco.com
lsilverstein@bgrcpas.com
kdavis@grfcpa.com
burdette@bsgpc.com
pburke@slacpa.com
andrew.calvert@calvertandcompany.com
ccocke@cst-cpa.com
Hgoldklang@gcacpas.com
shalt@cpas4you.com
mdm@rlmcpa.com
raj@sareentax.com
ns@kssacct.com
bes@tgccpa.com
pstefanou@rbsmllp.com
klarson@cottoncpa.com
jcovas@mcb-cpa.com
Jeff.Creskoff@kwccpa.com
richardf@rsfchart.com
mmickens@bertsmithco.com
howardr@rsfchart.com
ekearney@kearneyco.com
Peter.Regis@regiscpa.com
sjones@walkerllp.com
wvoorhees@calibrecpa.com
saguna.hitapot@bakertilly.com
gallender@cbiz.com
samgalloway@cpabizzness.com
shannon.lands@saltmarshcpa.com
rrosen@gerstlerosen.com
bgoldenberg@gerstlerosen.com
rgustason@rwhsgcpa.com
rswope@sloccpa.com
rmckinney@cricpa.com
Diane@harecpa.com
kstewart@sssj-cpa.com
darlene.hachmeister@cpagroup.com
kwaldrop@cbh.com
rthomas@brcpaweb.com
jbaumann@brcpaweb.com
percy@bashorlegendre.com
Donaldk@bbkm.com
ccrouse@tampacpa.com
jrybicki@larsonallen.com
sphifer@mpmpa.com
christi.zettel@pnccpa.com
mperez@dowellperez.com
crivero@rgcocpa.com
lee.bell@saltmarshcpa.com
ghernandez@vhcpa.com
RThomas@brcpaweb.com
mark@houghcpa.com
snell@hughessnell.com
recruiter@jmco.com
mKingery@tampacpa.com
sPeterson@markham-norton.com
jMarlar@mjcpa.com
KAlter@mslcpa.com
Recruiting@pnccpa.com
magda.crnkovich@pnccpa.com
Pittman@ralston.com
DHayob@bkd.com
slangston@hlb-cpa.com
bShamburger@jtsco.com
Siemers@kcoe.com
Fair@kcoe.com
cKoch@kshd.com
bRauber@kshd.com
bTerhaar@larsonallen.com
Jason.duffner@cliftonlarsonallen.com
kWilliamson@larsonallen.com
ajsmith@larsonallen.com
mAfrick@larsonallen.com
jBerens@larsonallen.com
jShaw@lssmllp.com
rBerry@melton-melton.com
sDrenth@melton-melton.com
Matt.Coscia@mcggroup.com
Kurtis.Abramson@mossadams.com
Annette.Ahlers@mossadams.com
mDexter@pdshcpas.com
Johng@ppglc.com
Bryan@pskcpa.com
cOsiek@roco-cpa.com
bMatlock@RKCO.com
TGoldman@RKCO.com
Paul@sfcllp.com
career@turnerstone.com
jSinuk@uhy-us.com
DEubank@wencpa.com
plmills@weavertidwell.com
Mark.Lund@weaverllp.com
dchenning@henningcpa.com
cClayton@bnkj.com
jMansour@bjmco.com
JWhite@bfwcpa.com
MBatts@nonprofitcpa.com
bMorgan@cmgccpa.com
mBohling@grosscollins.com
careers@houstoncompanycpa.com
mJohnson@mslc.com
gKordecki@kircpa.com
info@lindseygroup.com
mMcConnell@mm-cpa.com
Ronnie@MarshallJones.com
dluker@mjcpa.com
kcanzoneri@mcdirmitdavis.com
m.Crace@cgmcpa.com
d.McGrath@cgmcpa.com
cTurnbull@mstiller.com
lJordan@resjcpas.com
aWilliams@afnw.com
Lisa.Giordano@bakertilly.com
bsmith@bertsmithco.com
gWillie@bertsmithco.com
Michael.Wicks@kwccpa.com
sWimbish@mswspa.com
Gwen.Regis@regiscpa.com
joe@cpa-chicago.com
lee@romecpa.com
jollmann@wipfli.com
bBlaha@wipfli.com
cTunison@wipfli.com
kPinsky@waradydavis.com
jhufford@huffordfinancial.com
tAlmack@ksmcpa.com
jNestor@ksmcpa.com
dDolin@kbparrish.com
dSullivan@kbparrish.com
Mark@khscpa.com
kCarter@kcpag.com
dMarcer@londonwittegroup.com
kBuoy@mslc.com
mDinius@noblecon.net
sSeefeld@titus-us.com
jDressler@mslc.com
amt@joneskolb.com
tbuehrer@blackmankallick.com
ffenello@uhy-us.com
rob.babek@marcumllp.com
David.Appel@marcumllp.com
Marjorie.Bailey@marcumllp.com
grace.flora@mcggroup.com
brezina@hlb-cpa.com
LSinger@fgmk.net
MHartman@fgmk.net
jtaraboulos@ksdt-cpa.com
rbismeyer@gainerconnelly.com
kkrowczyk@portebrown.com
kburrows@moorecolson.com
blanigan@lanigancpa.com
MMangum@pyapc.com
Johnson@doeren.com
kwak@bellsouth.net
'''.strip().replace('\r','').split('\n')

import socket

def check_domain(domain):
	try:
		# Try to resolve the domain's IP address
		socket.gethostbyname(domain)
		return True
	except socket.error:
		return False

def process_emails(email_list):
	valid_domains = []
	invalid_domains = []
	error_domains = []
	index = _.getTable('validate-email-domains.index')
	if not index:
		index = {
			'valid': [],
			'invalid': [],
		}
	for email in email_list:
		try:
			fixedEmail = suffix_cleaner(email)
			domain = email.split('@')[1]
			domain2 = fixedEmail.split('@')[1]
			if domain in index['valid']:
				valid_domains.append({'email': email, 'domain': domain})
			elif domain in index['invalid']:
				invalid_domains.append({'email': email, 'domain': domain})
			else:
				if check_domain(domain) or check_domain(domain2):
					error = False
					if not domain2 == domain:
						domain1 = domain
						domain = domain2
						error = True
					
					if error:
						error_domains.append({'email': email, 'domain': domain, 'unfixed': domain1})
					else:
						valid_domains.append({'email': email, 'domain': domain})
					
					index['valid'].append(domain)
				else:
					invalid_domains.append({'email': email, 'domain': domain})
					index['invalid'].append(domain)
		except IndexError:
			# In case the email doesn't have a domain part
			invalid_domains.append({'email': email, 'domain': None})
	_.saveTable(index,'validate-email-domains.index',p=0)
	return valid_domains, invalid_domains, error_domains

# # Example usage
# email_list = [
#     'user1@example.com',
#     'user2@nonexistentdomain.com',
#     'user3@gmail.com',
#     'invalidemail.com'
# ]

# valid_domains, invalid_domains = process_emails(email_list)

# print("Valid domains:")
# for entry in valid_domains:
#     print(entry)

# print("\nInvalid domains:")
# for entry in invalid_domains:
#     print(entry)



def suffix_cleaner(line):
	if '.com' in line:
		line = line.split('.com')[0]+'.com'
	return line


def action():
	global email_list
	valid_domains, invalid_domains, error_domains = process_emails(email_list)
	if not _.switches.isActive('Invalid'):
		print("Valid domains:")
		for entry in valid_domains:
			print(entry)
		_.pr('',len(valid_domains))
		print("\nInvalid domains:")
		for entry in invalid_domains:
			print(entry)
		_.pr('',len(invalid_domains))
	else:
		for entry in invalid_domains: _.pr(entry['email'])
		_.pr('',len(invalid_domains))
		
		_.pr()
		spent = []; i=0
		for entry in invalid_domains:
			if not entry['domain'] in spent:
				i+=1
				spent.append(entry['domain'])
				_.pr(entry['domain'])
		_.pr()
		_.pr(line=1)
		_.pr()
		for entry in error_domains: _.pr(entry['email'])
		_.pr('',len(error_domains))
		_.pr()
		spent = []; i=0
		for entry in error_domains:
			if not entry['domain'] in spent:
				i+=1
				spent.append(entry['domain'])
				_.pr(entry['domain'])
		_.pr('',i)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);