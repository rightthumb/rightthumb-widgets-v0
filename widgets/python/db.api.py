#!/usr/bin/env python3
# import requests; exec(requests.get('https://sds.sh/micro.py/').text); exec(loader); _=globals().get('_')



import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    _.switches.register( 'Action', '-a,-action','find | findOne | insert | update | delete | count' )
    _.switches.register( 'Collection', '-c,-collection', 'urls | notes' )
    _.switches.register( 'Backend', '-b,-backend', 'json | mongo' )
    _.switches.register( 'Where', '-w,-where', isData='json,keyvalue', description='Filter criteria for find/update/delete' )
    _.switches.register( 'Data/Fields', '-d,-data', isData='data.name Scott data.type basic', description='Data for insert/update' )
    # _.switches.register( 'Options', '-o,-options', isData='json,keyvalue', description='Additional options for update (e.g. upsert)' )
    # _.switches.register( 'Meta', '-m,-meta', isData='json,keyvalue', description='Meta information for the request' )
    # _.switches.register( 'APIURL', '-u,-url', 'https://sds.sh/db/api/master_api_scaffold/api/' )



def normalizeAction(action):
    dic = {
        'f': 'find',
        's': 'find', 
        'search': 'find', 
        'r': 'find',


        'findone': 'findOne',
        'o': 'findOne',
        'one': 'findOne', 
        'fo': 'findOne',


        'i': 'insert',
        'add': 'insert', 
        'a': 'insert', 
        'c': 'insert', 
        'create': 'insert',

        'u': 'update',
        'up': 'update',

        'd': 'delete',
        'del': 'delete',

        'count': 'count',
        'cnt': 'count',
    }
    return dic.get(action, action)

def normalizeCollection(collection):
    dic = {
        'u': 'urls',
        'url': 'urls',
        'urls': 'urls',

        'n': 'notes',
        'note': 'notes',
        'notes': 'notes',
    }
    return dic.get(collection, collection)

def normalizeBackend(backend):
    dic = {
        'j': 'json',
        'json': 'json',

        'm': 'mongo',
        'mongo': 'mongo',
    }
    return dic.get(backend, backend)

def normalizeFields(field):
    if field.startswith('data.'):
        return field
    if field.startswith('d.'):
        return field.replace('d.', 'data.')

    if field.startswith('d.r.'):
        return field.replace('d.r.', 'data.record.')

    if field.startswith('r.'):
        return 'data.record.' + field[2:]
    if field.startswith('.'):
        return 'data.record' + field
    return 'data.record.' + field

def normalizeWhere(where):
    if where.startswith('where.'):
        return where
    if where.startswith('w.'):
        return where.replace('w.', 'where.')
    if where.startswith('.'):
        return 'where' + where
    return 'where.' + where




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
    'relatedapps': [],
    'prerequisite': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()



    _.switches.trigger( 'Action', normalizeAction )
    _.switches.trigger( 'Collection', normalizeCollection )
    _.switches.trigger( 'Backend', normalizeBackend )
    _.switches.trigger( 'Data/Fields', normalizeFields )
    _.switches.trigger( 'Where', normalizeWhere )




    _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)

    _.switches.trigger( 'DB', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start






# import copy
import os
import pickle
import re
from typing import Any, Callable, Dict, List, Optional, Tuple, Union


class LazyDic:
    """
    LazyDic = lazy nested-dict builder / mutator / shorthand tool.

    This class builds dict inputs for other systems such as a switch manager.
    It does NOT parse CLI args or execute triggers/callbacks.

    Short names:
        sh  = shorthand
        eq  = exact set
        mod = search + modify/attach/merge
    """

    def __init__(
        self,
        data: Any = None,
        mode: Optional[str] = None,
        switch_mode: bool = False,
        child_keys: Optional[List[str]] = None,
        auto_promote: bool = True,
    ):
        self.mode = mode or ("switch" if switch_mode else None)
        self.switch_mode = switch_mode or self.mode == "switch"
        self.auto_promote = auto_promote
        self.child_keys = child_keys or ["Children", "children", "Switches", "switches", "Items", "items"]

        self.dic: Dict[str, Any] = {}

        if data is None or data == "":
            self.dic = {}
        elif isinstance(data, LazyDic):
            self.dic = copy.deepcopy(data.dic)
        elif isinstance(data, dict):
            self.dic = copy.deepcopy(data)
        elif isinstance(data, str):
            s = data.strip()
            if s:
                if self._looks_like_shorthand(s):
                    self.sh(s)
                else:
                    # Allow passing a file path to a pickle/dill if wanted later by caller
                    # but do not auto-load here.
                    self.dic = {}
            else:
                self.dic = {}
        else:
            raise TypeError(f"Unsupported init data type: {type(data)}")

        if self.switch_mode and self.auto_promote:
            self._normalize_switch_tree(self.dic)

    # ------------------------------------------------------------
    # basic helpers
    # ------------------------------------------------------------

    def copy(self) -> "LazyDic":
        return LazyDic(
            data=copy.deepcopy(self.dic),
            mode=self.mode,
            child_keys=copy.deepcopy(self.child_keys),
            auto_promote=self.auto_promote,
        )

    def deepCopy(self) -> "LazyDic":
        return self.copy()

    def dump(self) -> Dict[str, Any]:
        return self.dic

    def clear(self) -> "LazyDic":
        self.dic = {}
        return self

    # ------------------------------------------------------------
    # shorthand
    # ------------------------------------------------------------

    def sh(self, text: str, dic: Optional[Dict[str, Any]] = None, under: Optional[Union[str, List[str], Tuple[str, ...]]] = None) -> "LazyDic":
        """
        sh = shorthand

        Parse compact pipe shorthand into nested dicts and merge it in.

        Example:
            ld.sh('Files:|  In: -f,-in|  Out: -o,-out || Utility:|  Clean: --c')
        """
        target = dic if dic is not None else self.dic
        built = self._parse_shorthand(text)

        if self.switch_mode and self.auto_promote:
            self._normalize_switch_tree(built)

        if under:
            path = self._coerce_path(under)
            node = self._ensure_path(path, dic=target)
            self._deep_merge(node, built)
        else:
            self._deep_merge(target, built)

        return self

    # ------------------------------------------------------------
    # path operations
    # ------------------------------------------------------------

    def ensure(
        self,
        path: Union[str, List[str], Tuple[str, ...]],
        dic: Optional[Dict[str, Any]] = None,
        leaf_default: Optional[Any] = None,
    ) -> Any:
        """
        Ensure a path exists and return the leaf node.

        Example:
            ld.ensure('Files.Switches.-in')
        """
        target = dic if dic is not None else self.dic
        parts = self._coerce_path(path)
        node = self._ensure_path(parts, dic=target, leaf_default=leaf_default)
        return node

    def eq(
        self,
        path: Union[str, List[str], Tuple[str, ...]],
        value: Any = None,
        sh: Optional[str] = None,
        dic: Optional[Dict[str, Any]] = None,
    ) -> "LazyDic":
        """
        eq = exact set

        Set a value on an exact path, lazily creating missing parents.

        Example:
            ld.eq('Files.trigger', my_fn)
            ld.eq('Files.Children', sh='Ago: -ago|Size: -size')
        """
        target = dic if dic is not None else self.dic
        parts = self._coerce_path(path)

        if sh is not None:
            frag = self._parse_shorthand(sh)
            if self.switch_mode and self.auto_promote:
                self._normalize_switch_tree(frag)
            value = frag

        if not parts:
            raise ValueError("eq() requires a non-empty path")

        if len(parts) == 1:
            key = parts[0]
            if isinstance(value, LazyDic):
                target[key] = copy.deepcopy(value.dic)
            else:
                target[key] = copy.deepcopy(value)
        else:
            parent = self._ensure_path(parts[:-1], dic=target)
            key = parts[-1]
            if isinstance(value, LazyDic):
                parent[key] = copy.deepcopy(value.dic)
            else:
                parent[key] = copy.deepcopy(value)

        if self.switch_mode and self.auto_promote:
            self._normalize_switch_tree(self.dic)

        return self

    def update(
        self,
        path: Union[str, List[str], Tuple[str, ...]],
        data: Any,
        dic: Optional[Dict[str, Any]] = None,
    ) -> "LazyDic":
        """
        Merge/update data into an exact path.

        Example:
            ld.update('Files.Children', {'Contacts': {'Switches': {'-email': {}}}})
        """
        target = dic if dic is not None else self.dic
        parts = self._coerce_path(path)
        node = self._ensure_path(parts, dic=target)

        incoming = self._normalize_incoming(data)

        if isinstance(node, dict) and isinstance(incoming, dict):
            self._deep_merge(node, incoming)
        else:
            raise TypeError("update() target must resolve to a dict")

        if self.switch_mode and self.auto_promote:
            self._normalize_switch_tree(self.dic)

        return self

    # ------------------------------------------------------------
    # search
    # ------------------------------------------------------------

    def search(
        self,
        query: str,
        out: str = "path",
        under: Optional[Union[str, List[str], Tuple[str, ...]]] = None,
        data: Optional[Dict[str, Any]] = None,
        first: bool = True,
    ) -> Any:
        """
        Recursively search for a key name.

        query:
            'Files'
            'Switches'
            '-in'

        out:
            'path'   -> 'Files.Children.Contacts'
            'node'   -> dict/value
            'match'  -> {'path': ..., 'key': ..., 'value': ...}
            'all'    -> list of match dicts

        under:
            Limit search to descendants under one or more child container names,
            e.g. under='Children'
        """
        target = data if data is not None else self.dic
        results: List[Dict[str, Any]] = []

        under_keys = None
        if under is not None:
            if isinstance(under, (list, tuple)):
                under_keys = set(str(x) for x in under)
            else:
                under_keys = {str(under)}

        def _walk(node: Any, path_parts: List[str], allow_collect: bool = True):
            if isinstance(node, dict):
                for key, value in node.items():
                    new_path = path_parts + [str(key)]

                    if allow_collect and str(key) == query:
                        results.append({
                            "path_parts": new_path,
                            "path": ".".join(new_path),
                            "key": str(key),
                            "value": value,
                        })
                        if first:
                            return True

                    next_allow_collect = allow_collect
                    if under_keys is not None:
                        next_allow_collect = str(key) in under_keys

                    if isinstance(value, (dict, list)):
                        stop = _walk(value, new_path, allow_collect=next_allow_collect or allow_collect)
                        if stop and first:
                            return True

            elif isinstance(node, list):
                for idx, item in enumerate(node):
                    new_path = path_parts + [str(idx)]
                    if isinstance(item, (dict, list)):
                        stop = _walk(item, new_path, allow_collect=allow_collect)
                        if stop and first:
                            return True

            return False

        _walk(target, [])

        if out == "all":
            return results

        if not results:
            return [] if out == "all" else None

        rec = results[0] if first else results

        if out == "path":
            return rec["path"] if isinstance(rec, dict) else [r["path"] for r in rec]
        if out == "node":
            return rec["value"] if isinstance(rec, dict) else [r["value"] for r in rec]
        if out == "match":
            return rec

        return rec

    def find(self, *args, **kwargs) -> Any:
        return self.search(*args, **kwargs)

    def searchEq(
        self,
        path: Union[str, List[str], Tuple[str, ...]],
        value: Any = None,
        under: Optional[Union[str, List[str], Tuple[str, ...]]] = None,
        data: Optional[Dict[str, Any]] = None,
        create_anchor: bool = False,
        sh: Optional[str] = None,
    ) -> "LazyDic":
        """
        Search for the first anchor key, then lazily set the remaining tail.

        Example:
            ld.searchEq('Files.trigger', my_fn)
            ld.searchEq('Files.meta.help', 'input files')
            ld.searchEq('Files.Children', sh='Ago: -ago|Size: -size')
        """
        target = data if data is not None else self.dic
        parts = self._coerce_path(path)

        if not parts:
            raise ValueError("searchEq() requires a non-empty path")

        anchor = parts[0]
        tail = parts[1:]

        anchor_path = self.search(anchor, out="path", under=under, data=target)

        if anchor_path is None:
            if not create_anchor:
                return self
            anchor_parts = self._coerce_path(anchor)
            self._ensure_path(anchor_parts, dic=target)
            anchor_path = ".".join(anchor_parts)

        full_parts = self._coerce_path(anchor_path) + tail

        return self.eq(full_parts, value=value, sh=sh, dic=target)

    # ------------------------------------------------------------
    # modify / attach / merge
    # ------------------------------------------------------------

    def mod(
        self,
        anchor: str,
        data: Any = None,
        sh: Optional[str] = None,
        under: Optional[Union[str, List[str], Tuple[str, ...]]] = None,
        create_anchor: bool = False,
        out: str = "self",
    ) -> Any:
        """
        Search for an anchor key, then attach/merge incoming data there
        or under a child path such as 'Children'.

        Examples:
            ld.mod('Files', {'Contacts': {}}, under='Children')
            ld.mod('Files', sh='Ago: -ago|Size: -size', under='Children')
        """
        incoming = self._normalize_incoming(data=data, sh=sh)

        anchor_path = self.search(anchor, out="path")
        if anchor_path is None:
            if not create_anchor:
                return self if out == "self" else None
            self.ensure(anchor)
            anchor_path = anchor

        if under:
            dest_parts = self._coerce_path(anchor_path) + self._coerce_path(under)
        else:
            dest_parts = self._coerce_path(anchor_path)

        node = self._ensure_path(dest_parts)

        if not isinstance(node, dict):
            raise TypeError("mod() destination must resolve to a dict")

        if not isinstance(incoming, dict):
            raise TypeError("mod() incoming data must normalize to a dict")

        self._deep_merge(node, incoming)

        if self.switch_mode and self.auto_promote:
            self._normalize_switch_tree(self.dic)

        if out == "path":
            return ".".join(dest_parts)
        if out == "node":
            return node
        return self

    def add(
        self,
        data: Any = None,
        sh: Optional[str] = None,
        under: Optional[Union[str, List[str], Tuple[str, ...]]] = None,
    ) -> "LazyDic":
        """
        Universal add/merge entry point.

        Accepts:
            - dict
            - LazyDic
            - shorthand string
            - callable(ld) -> None|dict|LazyDic|str
            - list/tuple of the above
        """
        incoming = self._normalize_incoming(data=data, sh=sh)

        if isinstance(incoming, list):
            for item in incoming:
                self.add(item, under=under)
            return self

        if not isinstance(incoming, dict):
            raise TypeError("add() incoming data must normalize to a dict or list")

        if under:
            node = self._ensure_path(self._coerce_path(under))
            self._deep_merge(node, incoming)
        else:
            self._deep_merge(self.dic, incoming)

        if self.switch_mode and self.auto_promote:
            self._normalize_switch_tree(self.dic)

        return self

    # ------------------------------------------------------------
    # persistence
    # ------------------------------------------------------------

    def save(self, path: str, kind: Optional[str] = None) -> str:
        """
        Save LazyDic by extension:
            .dill   -> dill
            .pickle -> pickle
            .pkl    -> pickle
        """
        kind = self._serializer_kind(path, kind)

        payload = {
            "__class__": "LazyDic",
            "__version__": 1,
            "mode": self.mode,
            "switch_mode": self.switch_mode,
            "auto_promote": self.auto_promote,
            "child_keys": self.child_keys,
            "dic": self.dic,
        }

        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        if kind == "dill":
            import dill  # type: ignore
            with open(path, "wb") as f:
                dill.dump(payload, f)
        elif kind == "pickle":
            with open(path, "wb") as f:
                pickle.dump(payload, f, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            raise ValueError(f"Unsupported serializer kind: {kind}")

        return path

    @classmethod
    def load(cls, path: str, kind: Optional[str] = None) -> "LazyDic":
        kind = cls._serializer_kind(path, kind)

        if kind == "dill":
            import dill  # type: ignore
            with open(path, "rb") as f:
                payload = dill.load(f)
        elif kind == "pickle":
            with open(path, "rb") as f:
                payload = pickle.load(f)
        else:
            raise ValueError(f"Unsupported serializer kind: {kind}")

        obj = cls(
            data=payload.get("dic", {}),
            mode=payload.get("mode"),
            switch_mode=payload.get("switch_mode", False),
            child_keys=payload.get("child_keys"),
            auto_promote=payload.get("auto_promote", True),
        )
        return obj

    @staticmethod
    def _serializer_kind(path: str, kind: Optional[str] = None) -> str:
        if kind:
            return kind.lower()

        ext = os.path.splitext(path)[1].lower()
        if ext == ".dill":
            return "dill"
        if ext in [".pickle", ".pkl"]:
            return "pickle"
        return "pickle"

    # ------------------------------------------------------------
    # internal normalization
    # ------------------------------------------------------------

    def _normalize_incoming(self, data: Any = None, sh: Optional[str] = None) -> Any:
        if sh is not None:
            built = self._parse_shorthand(sh)
            if self.switch_mode and self.auto_promote:
                self._normalize_switch_tree(built)
            return built

        if data is None:
            return {}

        if isinstance(data, LazyDic):
            return copy.deepcopy(data.dic)

        if isinstance(data, dict):
            incoming = copy.deepcopy(data)
            if self.switch_mode and self.auto_promote:
                self._normalize_switch_tree(incoming)
            return incoming

        if isinstance(data, (list, tuple)):
            out = []
            for item in data:
                out.append(self._normalize_incoming(item))
            return out

        if callable(data):
            result = data(self)
            if result is None:
                return {}
            return self._normalize_incoming(result)

        if isinstance(data, str):
            s = data.strip()
            if self._looks_like_shorthand(s):
                built = self._parse_shorthand(s)
                if self.switch_mode and self.auto_promote:
                    self._normalize_switch_tree(built)
                return built
            return {}

        return data

    def _ensure_path(
        self,
        parts: List[str],
        dic: Optional[Dict[str, Any]] = None,
        leaf_default: Optional[Any] = None,
    ) -> Any:
        target = dic if dic is not None else self.dic
        if not parts:
            return target

        node = target
        for i, part in enumerate(parts):
            is_last = i == len(parts) - 1

            if isinstance(node, dict):
                if part not in node:
                    node[part] = copy.deepcopy(leaf_default) if is_last and leaf_default is not None else {}
                elif is_last and leaf_default is not None and node[part] is None:
                    node[part] = copy.deepcopy(leaf_default)

                node = node[part]
            else:
                raise TypeError(f"Cannot ensure path through non-dict node at segment: {part}")

        return node

    @staticmethod
    def _coerce_path(path: Union[str, List[str], Tuple[str, ...], None]) -> List[str]:
        if path is None:
            return []
        if isinstance(path, (list, tuple)):
            return [str(x) for x in path if str(x) != ""]
        s = str(path).strip()
        if not s:
            return []
        return [p for p in s.split(".") if p != ""]

    @staticmethod
    def _deep_merge(base: Dict[str, Any], incoming: Dict[str, Any]) -> Dict[str, Any]:
        for key, value in incoming.items():
            if (
                key in base
                and isinstance(base[key], dict)
                and isinstance(value, dict)
            ):
                LazyDic._deep_merge(base[key], value)
            else:
                base[key] = copy.deepcopy(value)
        return base

    @staticmethod
    def _looks_like_shorthand(text: str) -> bool:
        if "|" in text:
            return True
        if ":" in text and "\n" in text:
            return True
        if ":" in text and not text.startswith("/") and not text.startswith("./") and not text.startswith("../"):
            return True
        return False

    # ------------------------------------------------------------
    # shorthand parser
    # ------------------------------------------------------------

    def _parse_shorthand(self, text: str) -> Dict[str, Any]:
        text = self._normalize_pipe_text(text)
        lines = [line.rstrip() for line in text.split("\n") if line.strip()]

        root: Dict[str, Any] = {}
        stack: List[Tuple[int, Dict[str, Any]]] = [(-1, root)]

        for raw in lines:
            indent = len(raw) - len(raw.lstrip(" "))
            line = raw.strip()

            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
            else:
                key = line.strip()
                value = ""

            while stack and indent <= stack[-1][0]:
                stack.pop()

            parent = stack[-1][1]

            if value == "":
                parent[key] = {}
                stack.append((indent, parent[key]))
            else:
                parent[key] = value

        return root

    @staticmethod
    def _normalize_pipe_text(text: str) -> str:
        while " ||" in text:
            text = text.replace(" ||", "||")
        while "|| " in text:
            text = text.replace("|| ", "||")
        text = text.replace("||", "|")
        return text.replace("|", "\n")

    # ------------------------------------------------------------
    # switch-friendly promotion
    # ------------------------------------------------------------

    def _normalize_switch_tree(self, node: Any) -> Any:
        if isinstance(node, dict):
            for key in list(node.keys()):
                value = node[key]

                # If parent value is a switch shorthand string like '-in -out'
                if isinstance(value, str) and self._looks_like_switch_string(value):
                    node[key] = {
                        "Switches": self._switch_string_to_dict(value)
                    }
                    value = node[key]

                # If a node already has Switches as a string, promote it
                if isinstance(value, dict):
                    if "Switches" in value and isinstance(value["Switches"], str):
                        value["Switches"] = self._switch_string_to_dict(value["Switches"])

                    # If Switches dict values are plain strings, treat them as help
                    if "Switches" in value and isinstance(value["Switches"], dict):
                        fixed_switches = {}
                        for sw_key, sw_val in value["Switches"].items():
                            if isinstance(sw_val, str):
                                fixed_switches[sw_key] = {"help": sw_val}
                            elif isinstance(sw_val, dict):
                                fixed_switches[sw_key] = sw_val
                            else:
                                fixed_switches[sw_key] = {"value": sw_val}
                        value["Switches"] = fixed_switches

                    # Convenience: fold triggers/callbacks dicts into Switches[*]
                    if "triggers" in value and isinstance(value["triggers"], dict):
                        value.setdefault("Switches", {})
                        for sw_key, trig_val in value["triggers"].items():
                            value["Switches"].setdefault(sw_key, {})
                            if not isinstance(value["Switches"][sw_key], dict):
                                value["Switches"][sw_key] = {}
                            value["Switches"][sw_key]["trigger"] = trig_val

                    if "callbacks" in value and isinstance(value["callbacks"], dict):
                        value.setdefault("Switches", {})
                        for sw_key, cb_val in value["callbacks"].items():
                            value["Switches"].setdefault(sw_key, {})
                            if not isinstance(value["Switches"][sw_key], dict):
                                value["Switches"][sw_key] = {}
                            value["Switches"][sw_key]["callback"] = cb_val

                self._normalize_switch_tree(node[key])

        elif isinstance(node, list):
            for item in node:
                self._normalize_switch_tree(item)

        return node

    @staticmethod
    def _looks_like_switch_string(text: str) -> bool:
        s = text.strip()
        if not s:
            return False
        return bool(re.match(r"^(-{1,2}[A-Za-z0-9_][^\s,]*)([\s,]+-{1,2}[A-Za-z0-9_][^\s,]*)*$", s))

    @staticmethod
    def _switch_string_to_dict(text: str) -> Dict[str, Dict[str, Any]]:
        parts = re.split(r"[\s,]+", text.strip())
        out: Dict[str, Dict[str, Any]] = {}
        for part in parts:
            if part:
                out[part] = {}
        return out


# ------------------------------------------------------------
# quick examples
# ------------------------------------------------------------
from pprint import pprint

if __name__ == "__main__":
    ld = LazyDic()

    ld.eq('user.name', 'Scott')
    ld.eq('user.contact.email', 'test@email.com')
    ld.eq('user.contact.phone', '555-1234')

    pprint(ld.dic)



if __name__ == "__main__":
    ld = LazyDic("", mode="switch")

    ld.sh("Files:|  In: -f,-in|  Out: -o,-out || Utility:|  Clean: --c")
    print("after sh:")
    pprint(ld.dump())

    ld.eq("Files.trigger", "myTriggerFn")
    ld.eq("Files.meta.help", "handles files")
    print("\nafter eq:")
    pprint(ld.dump())

    p = ld.search("Files", out="path")
    print("\nsearch path for Files:", p)

    ld.mod("Files", {"Contacts": {"Switches": "-email -phone"}}, under="Children", create_anchor=True)
    print("\nafter mod under Children:")
    pprint(ld.dump())

    sw = LazyDic({"Files": "-in -out"}, mode="switch")
    print("\nswitch-mode promotion:")
    pprint(sw.dump())

    sw.searchEq("Files.trigger", "finalFn")
    sw.searchEq("Files.meta.kind", "files")
    print("\nafter searchEq:")
    pprint(sw.dump())



import json
import sys
from typing import Any, Dict, Optional

try:
    import requests # type: ignore
except ImportError:
    print("This app requires: pip install requests")
    sys.exit(1)


def build_payload(
    action: str,
    collection: str,
    where: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    many: Optional[list] = None,
    projection: Optional[Dict[str, Any]] = None,
    options: Optional[Dict[str, Any]] = None,
    meta: Optional[Dict[str, Any]] = None,
    backend: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Build a clean CRUD payload dict.
    Only includes keys that have values.
    """
    payload: Dict[str, Any] = {
        "action": action,
        "collection": collection,
    }

    if backend:
        payload["backend"] = backend
    if where:
        payload["where"] = where
    if data:
        payload["data"] = data
    if many:
        payload["many"] = many
    if projection:
        payload["projection"] = projection
    if options:
        payload["options"] = options
    if meta:
        payload["meta"] = meta

    return payload


def parse_json_input(text: str, default: Any = None) -> Any:
    text = text.strip()
    if not text:
        return default
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"\nInvalid JSON:\n{e}\n")
        return default


def prompt_json(label: str, default: Any = None) -> Any:
    print(f"\n{label}")
    print("Enter JSON. Leave blank for default.")
    raw = input("> ").strip()
    return parse_json_input(raw, default)


def prompt_key_value_dict(label: str) -> Dict[str, Any]:
    print(f"\n{label}")
    print("Enter key=value pairs. Blank key to stop.")
    print("Values are auto-parsed as JSON when possible.")
    result: Dict[str, Any] = {}

    while True:
        key = input("key: ").strip()
        if not key:
            break

        value_raw = input("value: ").strip()

        # Try JSON parse first, fallback to string
        try:
            value = json.loads(value_raw)
        except Exception:
            value = value_raw

        result[key] = value

    return result


class APITester:
    def __init__(self, api_url: str, timeout: int = 20) -> None:
        self.api_url = api_url
        self.timeout = timeout

    def send(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        if 'collection' in payload and not payload['collection'].startswith('_api_'):
            payload['collection'] = '_api_' + payload['collection']
        try:
            response = requests.post(
                self.api_url,
                json=payload,
                timeout=self.timeout,
                headers={"Content-Type": "application/json"},
            )
        except requests.RequestException as e:
            return {
                "ok": False,
                "error": f"Request failed: {e}",
                "status_code": None,
                "text": None,
            }

        try:
            body = response.json()
        except Exception:
            body = {
                "raw_text": response.text
            }

        return {
            "ok": response.ok,
            "status_code": response.status_code,
            "response": body,
        }

    def print_payload(self, payload: Dict[str, Any]) -> None:
        print("\n=== REQUEST PAYLOAD ===")
        print(json.dumps(payload, indent=4, ensure_ascii=False))

    def print_result(self, result: Dict[str, Any]) -> None:
        print("\n=== RESPONSE ===")
        print(json.dumps(result, indent=4, ensure_ascii=False))


def choose_action() -> str:
    actions = [
        "insert",
        "find",
        "findOne",
        "update",
        "delete",
        "count",
        "custom",
        "quit",
    ]

    print("\nChoose action:")
    for i, action in enumerate(actions, 1):
        print(f"  {i}. {action}")

    while True:
        choice = input("> ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(actions):
                return actions[idx]
        elif choice in actions:
            return choice

        print("Invalid choice.")


def build_interactive_payload() -> Optional[Dict[str, Any]]:
    action = choose_action()

    if action == "quit":
        return None

    if action == "custom":
        print("\nPaste full JSON payload:")
        raw = input("> ").strip()
        payload = parse_json_input(raw, None)
        if not isinstance(payload, dict):
            print("Custom payload must be a JSON object.")
            return {}
        return payload

    collection = input("\ncollection: ").strip()
    if not collection:
        print("Collection is required.")
        return {}

    backend = input("backend (blank = none): ").strip() or None

    if action == "insert":
        mode = input("Data input mode? [1=json, 2=key=value] ").strip()
        if mode == "2":
            data = prompt_key_value_dict("Insert data")
        else:
            data = prompt_json("Insert data JSON", {})
        return build_payload(
            action=action,
            collection=collection,
            data=data,
            backend=backend,
        )

    if action in ("find", "findOne", "count", "delete"):
        mode = input("Where input mode? [1=json, 2=key=value] ").strip()
        if mode == "2":
            where = prompt_key_value_dict("Where clause")
        else:
            where = prompt_json("Where JSON", {})
        return build_payload(
            action=action,
            collection=collection,
            where=where,
            backend=backend,
        )

    if action == "update":
        where_mode = input("Where input mode? [1=json, 2=key=value] ").strip()
        if where_mode == "2":
            where = prompt_key_value_dict("Where clause")
        else:
            where = prompt_json("Where JSON", {})

        data_mode = input("Data input mode? [1=json, 2=key=value] ").strip()
        if data_mode == "2":
            data = prompt_key_value_dict("Update data")
        else:
            data = prompt_json("Update data JSON", {})

        options = prompt_json('Options JSON (example: {"upsert": false})', {})

        return build_payload(
            action=action,
            collection=collection,
            where=where,
            data=data,
            options=options,
            backend=backend,
        )

    print("Unsupported action.")
    return {}




def list_to_kv_dict(lst):
    """
    Convert flat list into key/value dict.

    Example:
        ["data.name", "Scott", "data.type", "basic"]
        ->
        {
            "data.name": "Scott",
            "data.type": "basic"
        }
    """
    if len(lst) % 2 != 0:
        raise ValueError("List must contain even number of elements (key/value pairs)")

    result = {}

    for i in range(0, len(lst), 2):
        key = lst[i]
        value = lst[i + 1]
        result[key] = value

    return result

def build_examples():
    examples = {}

    # -------------------------------
    # INSERT BASIC
    # -------------------------------
    ld = LazyDic()
    ld.eq('action', 'insert')
    ld.eq('backend', 'json')
    ld.eq('collection', 'test')
    ld.eq('data.name', 'Scott')
    ld.eq('data.type', 'basic')
    examples['insert_basic'] = ld

    # -------------------------------
    # INSERT MONGO
    # -------------------------------
    ld = LazyDic()
    ld.eq('action', 'insert')
    ld.eq('backend', 'mongo')
    ld.eq('collection', 'users')
    ld.eq('data.name', 'Scott')
    ld.eq('data.email', 'test@example.com')
    examples['insert_mongo'] = ld

    # -------------------------------
    # FIND ALL
    # -------------------------------
    ld = LazyDic()
    ld.eq('action', 'find')
    ld.eq('collection', 'test')
    examples['find_all'] = ld

    # -------------------------------
    # FIND WHERE
    # -------------------------------
    ld = LazyDic()
    ld.eq('action', 'find')
    ld.eq('collection', 'test')
    ld.eq('where.name', 'Scott')
    examples['find_where'] = ld

    # -------------------------------
    # FIND ONE
    # -------------------------------
    ld = LazyDic()
    ld.eq('action', 'findOne')
    ld.eq('collection', 'test')
    ld.eq('where.name', 'Scott')
    examples['find_one'] = ld

    # -------------------------------
    # COUNT
    # -------------------------------
    ld = LazyDic()
    ld.eq('action', 'count')
    ld.eq('collection', 'test')
    examples['count'] = ld

    # -------------------------------
    # UPDATE
    # -------------------------------
    ld = LazyDic()
    ld.eq('action', 'update')
    ld.eq('collection', 'test')
    ld.eq('where.name', 'Scott')
    ld.eq('data.status', 'updated')
    examples['update_basic'] = ld

    # -------------------------------
    # DELETE
    # -------------------------------
    ld = LazyDic()
    ld.eq('action', 'delete')
    ld.eq('collection', 'test')
    ld.eq('where.name', 'Scott')
    examples['delete_basic'] = ld

    # -------------------------------
    # INSERT COMPLEX
    # -------------------------------
    ld = LazyDic()
    ld.eq('action', 'insert')
    ld.eq('collection', 'test')
    ld.eq('data.name', 'Scott')
    ld.eq('data.active', True)
    ld.eq('data.count', 1)
    ld.eq('data.meta.source', 'cli')
    ld.eq('data.meta.env', 'local')
    ld.eq('data.tags', ['dev', 'api'])
    examples['insert_complex'] = ld

    return examples










def main() -> None:
    print("\nCRUD API Terminal Tester\n")

    if len(sys.argv) > 1:
        api_url = sys.argv[1]
    else:
        api_url = input("API URL: ").strip()

    if not api_url:
        print("API URL is required.")
        sys.exit(1)

    tester = APITester(api_url=api_url)

    while True:
        payload = build_interactive_payload()

        if payload is None:
            print("\nBye.")
            break

        if not payload:
            continue

        tester.print_payload(payload)

        confirm = input("\nSend request? [y/N]: ").strip().lower()
        if confirm != "y":
            print("Canceled.")
            continue

        result = tester.send(payload)
        tester.print_result(result)

        again = input("\nAnother request? [Y/n]: ").strip().lower()
        if again == "n":
            print("\nBye.")
            break


# if __name__ == "__main__": main()












    # _.switches.register( 'Action', '-a,-action','find | findOne | insert | update | delete | count' )
    # _.switches.register( 'Collection', '-c,-collection', 'urls | notes' )
    # _.switches.register( 'Backend', '-b,-backend', 'json | mongo' )
    # _.switches.register( 'Where', '-w,-where', isData='json,keyvalue', description='Filter criteria for find/update/delete' )
    # _.switches.register( 'Data/Fields', '-d,-data', isData='data.name Scott data.type basic', description='Data for insert/update' )
 

def action():

    url = 'https://sds.sh/db/api/master_api_scaffold/api/'
    ld = LazyDic()

    # ld.eq('action', 'insert')
    # ld.eq('action', 'find')
    # ld.eq('action', 'findOne')
    # ld.eq('action', 'count')
    # ld.eq('action', 'update')
    # ld.eq('action', 'delete')
    
    

    if _.switches.isActive('Action'):
        ld.eq('action', _.switches.values('Action')[0])
    else:
        ld.eq('action', 'find')
    
    
    if _.switches.isActive('backend'):
        ld.eq('backend', _.switches.values('Backend')[0])
    else:
        ld.eq('backend', 'mongo')
        
    if _.switches.isActive('Collection'):
        ld.eq('collection', _.switches.values('Collection')[0])
    else:
        ld.eq('collection', 'test')

    data = list_to_kv_dict( _.switches.values('Data/Fields') )
    for key in data:
        ld.eq(key, data[key])

    if _.switches.isActive('Where') and not 'find' in ld.dic.get('action'):
        ld.eq('action', 'find')


    if _.switches.isActive('Where'):
        data = list_to_kv_dict( _.switches.values('Where') )
        for key in data:
            ld.eq(key, data[key])    
    
    print()
    print()
    print(ld.dic.get('action'))
    print()
    print()

    _.pv(ld.dic)
    return
    tester = APITester(api_url=url)
    result = tester.send(data)
    tester.print_result(result)

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)