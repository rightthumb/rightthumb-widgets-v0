import os,sys
if sys.platform[0] == 'w': _rt=os.getenv('USERPROFILE') +os.sep+'.rt'
else: _rt=os.getenv('HOME') +os.sep+'.rt'

sys.path.append(_rt); import micro; exec(micro.loader);
