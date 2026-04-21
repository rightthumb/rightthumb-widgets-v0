import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
_._default_settings_()

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ))
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

import sys
import os
def action():
	base = _v.myBookmarks + '\\BM-'
	bm = {
		'labels': {},
		'paths': {},
	}
	for path in _.fo(_v.myBookmarks):
		cl = path.replace(base,'').replace('.txt','')
		# print(path); sys.exit();
		try:
			if path.endswith('.txt') and '\\BM-' in path:
				data = _.getText2(path,'text')
				data2 = _v.resolveFolderIDs(data)
				data = _v.sanitizeFolder(data2)
			else:
				continue
		except Exception as e:
			continue
		if os.path.isdir(data2):
			bm['labels'][cl]=data
			if not data in bm['paths']: bm['paths'][data] = []
			bm['paths'][data].append(cl)

	_.pv(bm)
	_.saveTable(bm,'bookmarks.index')
	# _.pr('saved',c='green')


# bookmarks.index

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);