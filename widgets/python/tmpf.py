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

#b)--> load
from _rightThumb._base3 import template; exec(  template.header()  ); exec(  template.setting()  );
#e)--> load

def sw():
    pass

_.appInfo[focus()] = {
    'file': 'tmpf.py',
    'liveAppName': __.thisApp( __file__ ),
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p tmpf -file file.txt'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'created': 1658773060.0103693,
    'tested': 1658773060.0103693,
}

#b)--> registration
template.info(focus()); exec(  template.triggers()  ); _.l.sw.register( triggers, sw ); _.l.conf('clean-pipe',False);
#e)--> registration

########################################################################################
#n)--> start

def action():
    load(); global c3po;
    #--> iterate
    for subject in _.isData(r=0): _.pr(subject)

def load():
    global c3po
    c3po = _.getTable( 'table' )
    #--> print table
    _.pt(c3po)

########################################################################################
if __name__ == '__main__':
    action()
    _.isExit(__file__)
