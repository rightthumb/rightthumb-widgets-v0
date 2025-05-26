import _rightThumb._construct as __
class dot():
	def __init__(self): pass;
def dots(path):
	def _dots_(pth):
		try: exec(pth); return True;
		except Exception as e: return False;
	rts=path.split('.'); exec('global '+rts[0]);
	if _dots_(path): return eval(rts[0])
	pre=[]; thp=[];
	for i,seg in enumerate(rts):
		pre=thp.copy(); thp.append(seg); npre='.'.join(pre); npath='.'.join(thp)
		if i == len(rts)-1:
			exec('from 1 import 2'.replace('1',npre).replace('2',rts[-1]))
			f='3=2'.replace('1',npre).replace('2',rts[-1]).replace('3',path)
		else: f='1=_.dot()'.replace('1',npath);

		if not _dots_(npath):
			exec(f)
			if i == len(rts)-1: return eval(rts[0]);
os=dots('os.sep')
os=dots('os.path.isfile')
os=dots('os.path.isdir')

