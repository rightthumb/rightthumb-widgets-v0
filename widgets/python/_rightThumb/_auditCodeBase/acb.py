def acb(code, lan='javascript', labels=False):
	out = Meta_Namespace()
	import _rightThumb._auditCodeBase as _code # type: ignore
	_code.validator.createIndex( code, lan, skipLoad=True, simple=False, B=True )
	oc = {}
	label = {}
	for x in _code.validator.identity['identity']:
		o = x
		c = _code.validator.identity['location']['open'][o]
		oc[o] = c
		l = _code.validator.getLabel( o, string=True )
		label[o] = l
	out.oc = oc
	out.label = label
	if labels:
		return out
	return oc

class Meta_Namespace():
	def __init__( self ): pass