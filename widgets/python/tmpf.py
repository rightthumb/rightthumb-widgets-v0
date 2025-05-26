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

# def action():
#     # import subprocess
#     # print(subprocess.getoutput(''))
#     # print(subprocess.getoutput('doskey /history'))
#     # import os
#     # os.system('doskey /history')
#     if _.isWin:
#         import subprocess
#         cmd_history = subprocess.check_output(["doskey", "/history"])
#         print(str(cmd_history,'iso-8859-1'))
#     else:
#         # import readline; print('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))
#         import readline
#         for i in range(readline.get_current_history_length()):
#             print (readline.get_history_item(i + 1))
#     # for line in dir(cmd_history):
#     # print(cmd_history.encode('latin1', 'ignore'))
#     # print(str(cmd_history))
#     # for line in cmd_history:
#     #     print(line)







# print( key() )

def action(): pass

########################################################################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)
