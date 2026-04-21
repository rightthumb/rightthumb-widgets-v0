import copy
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