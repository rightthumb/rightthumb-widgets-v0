

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'beta')))
from app_code_export_import import EcoNamespaceCollector, globals_to_code,     callable_kinds,       export_globals_from_file, build_bundle_code   # type: ignore




exp = export_globals_from_file(r"D:\\.rightthumb-widgets\\widgets\\python\\ls.py")
print("functions:", len(exp["functions"]))
print("classes:", len(exp["classes"]))
print("assignments:", len(exp["assignments"]))
print("skipped:", len(exp["skipped"]))

bundle_text = build_bundle_code(exp)
open(r"D:\\.rightthumb-widgets\\widgets\\python\\library\\beta\\bundle.all.py, "w", encoding="utf-8").write(bundle_text)


sys.exit()



ck = callable_kinds(globals())
_.pv(ck)
sys.exit()








# 1) Grab everything from current module (mostly)
res = globals_to_code(globals(), recurse=False)
print(res["code"])

# 2) Grab only a few names, recurse 2 levels into their referenced globals
res = globals_to_code(globals(), names=["action", "addFile"], recurse=True, max_depth=2)
open("bundle.py", "w", encoding="utf-8").write(res["code"])

# 3) See what didn’t serialize cleanly
print("missing source:", res["missing_source"])
print("skipped:", res["skipped"])
