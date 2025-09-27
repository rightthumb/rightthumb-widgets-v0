
# __.KillOn = dot()
# __.KillOn.status = False
# __.KillOn.db = {}
# __.KillOn.id = 0
# __.Kill = False

# def KillOn(what='f1',p=True,strict=None,label='',l=None,help=False):
# 	if ',' in what and strict is None: strict = True
# 	if strict is None: strict = False
# 	if help:
# 		pr("KillOn: DOES NOT Kill the Python app")
# 		pr("  what: key to kill on 'f1' or multi 'f1, f2'")
# 		pr('  p: print')
# 		pr('  strict: strict mode')
# 		pr('  label: label (or l)')
# 		pr('  ')
# 		pr('  KillOn(what,p,strict,label)')
# 		pr('  ')
# 		pr('Usage:')
# 		pr('  while')
# 		pr('  for')
# 		pr('  ')
# 		pr('  ')
# 		pr('Example:')
# 		pr("  KillOn('f1',l='Files')")
# 		pr("  KillOn('f2',l='Folders')")
# 		pr("  KillOn('f5, f6',l='Folders')")
# 		pr("  if __.KillOn.db['f1'].status: return None")
# 		pr("  if __.KillOn.db['f2'].status: return None")
# 		pr("  if __.KillOn.db['f5, f6'].status: return None")
# 		pr(" if Single Usage:")
# 		pr("  if __.Kill: return None")
# 		pr("  if __.KillOn.status: return None")
# 		pr('  ')
# 		pr('Variable:')
# 		pr('  Options:')
# 		pr('    - __.Kill           <-- single usage         ')
# 		pr('    - __.KillOn.status  <-- single usage         ')
# 		pr("    - __.KillOn.db['f1'].status    <-- multi usage         ")
# 		pr("    - __.KillOn.db['f2'].status    <-- multi usage         ")
# 	if not l is None: label=l
# 	__.KillOn.id+=1
# 	id = __.KillOn.id
# 	if what in __.KillOn.db:
# 		__.KillOn.db[what].km.stop()
# 		del __.KillOn.db[what]

# 	__.KillOn.db[what] = dot()
# 	__.KillOn.db[what].status = False
# 	__.KillOn.db[what].label = label
# 	def ThisKills(key):
# 		__.Kill = True
# 		__.KillOn.status = True
# 		__.KillOn.db[what].status = True
# 		__.KillOn.db[what].km.stop()
# 		pr(key,__.KillOn.db[what].label,'Killed',c='Background.red')

# 	__.KillOn.db[what].km = KeyMon({what:lambda:ThisKills(what)},strict=strict)
# 	if p:
# 		pr(label,'Kills on:',what,c='Background.blue')
# 	return id