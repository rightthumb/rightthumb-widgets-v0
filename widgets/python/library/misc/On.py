import os
import re
import sys
import json
import time
import pprint
import traceback
from typing import Any, Callable, Dict, Iterable, List, Optional, Union


Action = Union[
    Callable[..., Any],
    Dict[str, Any],  # action spec (see _run_actions)
]
ActionList = Union[Action, List[Action]]


def On(
    value: Any = None,
    *,
    # ---- triggers (WHEN) ----
    when: Optional[Union[str, List[str]]] = None,           # trigger needles; None => always
    argv: Optional[Iterable[Any]] = None,                   # haystack default sys.argv
    env: Optional[Union[str, List[str]]] = None,            # env var(s) as additional trigger
    enabled: Union[bool, ActionList] = True,                # gate: bool OR actions run to decide
    match: str = "eq",                                      # 'eq'|'contains'|'regex'|'startswith'|'endswith'
    any_all: str = "any",                                   # 'any' or 'all'
    icase: bool = False,                                    # case-insensitive comparisons
    invert: bool = False,                                   # invert trigger outcome

    # ---- actions (WHAT) ----
    do: Optional[ActionList] = None,                        # function / dict / list of either
    test: Optional[ActionList] = None,                      # pre-flight test actions (return truthy to proceed)
    label: Optional[str] = None,                            # label for default printer + for specs
    printer: Optional[Callable[..., Any]] = None,           # custom printer (fallback if do is None)
    pretty: bool = True,                                    # default printer pretty-format dict/list/json strings
    width: int = 120,                                       # pretty width
    prefix: str = "  ",                                     # default printer prefix
    stamp: bool = False,                                    # timestamp
    hr: bool = True,                                        # separator line around labeled output

    # ---- behavior ----
    once: bool = False,                                     # fire only once per unique key
    key: Optional[str] = None,                              # manual key for once
    state: Optional[dict] = None,                           # state dict (used for once + per-key storage)
    quiet: bool = False,                                    # suppress default printing/errors (still returns)
    exit: bool = False,                                     # sys.exit(0) after firing
    raise_errors: bool = False,                             # raise exceptions from actions
    on_error: Optional[ActionList] = None,                  # actions to run on error
    log_file: Optional[str] = None,                         # append final printed string and/or errors here

    # ---- event-ish sugar ----
    event: Optional[str] = None,                            # optional event name (for keying/labeling)
    ctx: Optional[dict] = None,                             # context passed into action specs
):
    """
    On(): a conditional "value/event" hook that triggers actions when conditions match.

    TL;DR:
      - Trigger with `when` against argv/env (or always if when=None)
      - Optional `test` actions decide whether it should fire (supports fn/dict/list)
      - `do` actions execute (supports fn/dict/list)
      - If `do` is None -> prints `value` using a built-in pretty printer (or your `printer`)
      - `enabled` can be bool OR action(s) that compute gating
      - `once` can prevent repeat firing (stores keys in `state`)

    ACTION SPEC formats (for dict items):
      1) {'fn': callable, 'kwargs': {...}}
         -> fn(value, **kwargs)

      2) {'fn': callable, 'args': [...], 'kwargs': {...}}
         -> fn(*args, value=value, ctx=ctx, **kwargs)   (see inject rules)

      3) {'print': True, 'label': 'x', ... printer options ...}
         -> uses built-in printer (useful in a list)

      4) {'set': {'some.key': 123}} or {'set': [('k', v), ...]}
         -> sets entries in `state` (simple flat keys)

      5) {'return': True/False/<anything>}
         -> short-circuit and return that (mainly for `test`/`enabled` pipelines)

    NOTE on injection:
      - For callable actions, we call: fn(value)
      - For dict actions with 'fn', we pass `value` as positional first arg by default,
        UNLESS you set kwargs['value']=... yourself.
      - If action spec includes 'inject': {'value': True, 'ctx': True}, it will add kwargs.

    Returns:
      dict with details:
        {
          'fired': bool,
          'triggered': bool,
          'allowed': bool,      # enabled + test passed
          'results': [...],     # action results
          'value': <original value>,
          'event': <event>,
          'key': <once key used>
        }
    """

    # ----------------------------
    # internal helpers
    # ----------------------------
    ANSI = {
        "reset": "\033[0m",
        "gray": "\033[90m",
    }

    def _safe_str(v: Any) -> str:
        try:
            return str(v)
        except Exception:
            return repr(v)

    def _listify(v: Any) -> List[Any]:
        if v is None:
            return []
        if isinstance(v, list):
            return v
        if isinstance(v, (tuple, set)):
            return list(v)
        return [v]

    def _norm(s: str) -> str:
        return s.lower() if icase else s

    def _write(path: str, text: str) -> None:
        try:
            d = os.path.dirname(path)
            if d:
                os.makedirs(d, exist_ok=True)
            with open(path, "a", encoding="utf-8") as f:
                f.write(text)
                if not text.endswith("\n"):
                    f.write("\n")
        except Exception:
            pass

    def _looks_like_json(s: str) -> bool:
        s2 = s.strip()
        return (s2.startswith("{") and s2.endswith("}")) or (s2.startswith("[") and s2.endswith("]"))

    def _pretty(v: Any) -> str:
        if not pretty:
            return _safe_str(v)

        if isinstance(v, str) and _looks_like_json(v):
            try:
                return json.dumps(json.loads(v), indent=4, ensure_ascii=False)
            except Exception:
                return v

        if isinstance(v, dict):
            try:
                return json.dumps(v, indent=4, ensure_ascii=False)
            except Exception:
                return _safe_str(v)

        if isinstance(v, (list, tuple, set)):
            try:
                return pprint.pformat(v, width=width, compact=False)
            except Exception:
                return _safe_str(v)

        return _safe_str(v)

    def _ts() -> str:
        return time.strftime("%Y-%m-%d %H:%M:%S")

    def _default_print(v: Any, *, label: Optional[str] = None) -> str:
        lines: List[str] = []
        if label:
            if hr:
                lines.append(f"{ANSI['gray']}{'-'*60}{ANSI['reset']}")
            head = f"{label}:"
            if stamp:
                head = f"[{_ts()}] {head}"
            lines.append(head)

        if isinstance(v, (list, tuple, set)):
            for item in v:
                block = _pretty(item).splitlines() or [""]
                for line in block:
                    lines.append(f"{prefix}{line}")
        else:
            block = _pretty(v).splitlines() or [""]
            for line in block:
                lines.append(f"{prefix}{line}")

        if label and hr:
            lines.append(f"{ANSI['gray']}{'-'*60}{ANSI['reset']}")
        out = "\n".join(lines)
        if not quiet:
            print(out)
        if log_file:
            _write(log_file, out)
        return out

    def _match_needles(needles: List[str], hay: List[str]) -> bool:
        if not needles:
            return True

        h_norm = [_norm(x) for x in hay]
        n_norm = [_norm(x) for x in needles]

        def one(n: str, h: str) -> bool:
            if match == "eq":
                return h == n
            if match == "contains":
                return n in h
            if match == "startswith":
                return h.startswith(n)
            if match == "endswith":
                return h.endswith(n)
            if match == "regex":
                flags = re.IGNORECASE if icase else 0
                try:
                    return re.search(n, h, flags=flags) is not None
                except re.error:
                    return n in h
            # default fallback
            return n in h

        if any_all == "all":
            return all(any(one(n, h) for h in h_norm) for n in n_norm)
        return any(one(n, h) for n in n_norm for h in h_norm)

    def _env_hit(env_keys: List[str], needles: Optional[List[str]]) -> bool:
        if not env_keys:
            return False
        # if no needles, treat presence/truthy as trigger
        truthy_off = {"0", "false", "no", "off", "null", "none", ""}
        for k in env_keys:
            val = os.getenv(str(k))
            if val is None:
                continue
            if needles is None:
                if val.strip().lower() not in truthy_off:
                    return True
            else:
                # env adds more hay surface
                if _match_needles(needles, [str(k), str(val)]):
                    return True
        return False

    def _action_list(actions: ActionList) -> List[Action]:
        items = _listify(actions)
        flat: List[Action] = []
        for it in items:
            if isinstance(it, list):
                flat.extend(it)
            else:
                flat.append(it)
        return flat

    def _run_actions(actions: ActionList, *, phase: str) -> List[Any]:
        results: List[Any] = []
        for act in _action_list(actions):
            try:
                # callable => fn(value)
                if callable(act):
                    results.append(act(value))
                    continue

                if not isinstance(act, dict):
                    results.append(act)  # literal passthrough
                    continue

                # short-circuit return
                if "return" in act:
                    results.append(act["return"])
                    continue

                # set into state
                if "set" in act:
                    if state is None:
                        raise TypeError("On(..., state=...) required for action {'set': ...}")
                    payload = act["set"]
                    if isinstance(payload, dict):
                        for k, v in payload.items():
                            state[str(k)] = v
                    else:
                        for k, v in payload:
                            state[str(k)] = v
                    results.append(True)
                    continue

                # built-in print action
                if act.get("print") is True:
                    lab = act.get("label", label)
                    # allow per-action overrides
                    old_prefix = prefix
                    old_stamp = stamp
                    old_hr = hr
                    try:
                        # local override via act keys if present
                        if "prefix" in act:
                            locals_prefix = act["prefix"]
                        else:
                            locals_prefix = old_prefix
                        if "stamp" in act:
                            locals_stamp = bool(act["stamp"])
                        else:
                            locals_stamp = old_stamp
                        if "hr" in act:
                            locals_hr = bool(act["hr"])
                        else:
                            locals_hr = old_hr

                        # print with overrides (temporarily)
                        # (we keep it simple: rebuild output with overrides)
                        out_lines: List[str] = []
                        if lab:
                            if locals_hr:
                                out_lines.append(f"{ANSI['gray']}{'-'*60}{ANSI['reset']}")
                            head = f"{lab}:"
                            if locals_stamp:
                                head = f"[{_ts()}] {head}"
                            out_lines.append(head)

                        block = _pretty(value).splitlines() or [""]
                        for line in block:
                            out_lines.append(f"{locals_prefix}{line}")

                        if lab and locals_hr:
                            out_lines.append(f"{ANSI['gray']}{'-'*60}{ANSI['reset']}")

                        out = "\n".join(out_lines)
                        if not quiet:
                            print(out)
                        if log_file:
                            _write(log_file, out)
                        results.append(out)
                    finally:
                        pass
                    continue

                # fn spec
                fn = act.get("fn")
                if not callable(fn):
                    raise TypeError(f"On() action dict missing callable 'fn' (phase={phase}).")

                kwargs = act.get("kwargs", {}) or {}
                args = act.get("args", []) or []
                inject = act.get("inject", {"value": True, "ctx": True})

                if not isinstance(kwargs, dict):
                    raise TypeError("On() action 'kwargs' must be a dict.")
                if not isinstance(args, list):
                    raise TypeError("On() action 'args' must be a list.")

                # injection
                if isinstance(inject, dict):
                    if inject.get("value") and "value" not in kwargs:
                        kwargs["value"] = value
                    if inject.get("ctx") and "ctx" not in kwargs:
                        kwargs["ctx"] = ctx or {}
                    if inject.get("label") and "label" not in kwargs:
                        kwargs["label"] = label
                    if inject.get("event") and "event" not in kwargs:
                        kwargs["event"] = event

                # call style:
                # - if kwargs includes 'value', many people want fn(value, **kw) OR fn(**kw)
                #   so we support:
                #     act.get('call') in {'pos', 'kw'}
                call_style = act.get("call", "pos")  # default positional value first
                if call_style == "kw":
                    results.append(fn(*args, **kwargs))
                else:
                    results.append(fn(value, *args, **kwargs))

            except Exception as e:
                if not quiet:
                    print(f"[On] error in {phase} action: {e}")
                if log_file:
                    _write(log_file, f"[On] error in {phase} action: {e}\n{traceback.format_exc()}")
                if on_error:
                    try:
                        _run_actions(on_error, phase="on_error")
                    except Exception:
                        pass
                if raise_errors:
                    raise
                results.append(e)
        return results

    def _bool_from_results(results: List[Any], *, default: bool = True) -> bool:
        # if results empty, default
        if not results:
            return default
        # if any result is explicitly bool, use last bool; else truthiness of last result
        last = results[-1]
        if isinstance(last, bool):
            return last
        return bool(last)

    # ----------------------------
    # init state + keying
    # ----------------------------
    if state is None:
        state = {}

    # default key used for once gating
    auto_key_parts = [
        "On",
        event or "",
        label or "",
        _safe_str(key or ""),
        _safe_str(when) if when is not None else "",
    ]
    used_key = key or "|".join([p for p in auto_key_parts if p != ""])

    if once:
        seen = state.setdefault("__On_once__", set())
        # allow persistence if user passes in a dict w/ set already
        if isinstance(seen, list):
            seen = set(seen)
            state["__On_once__"] = seen
        if used_key in seen:
            return {
                "fired": False,
                "triggered": False,
                "allowed": False,
                "results": [],
                "value": value,
                "event": event,
                "key": used_key,
            }

    # ----------------------------
    # enabled gate (bool or actions)
    # ----------------------------
    allowed = True
    if isinstance(enabled, bool):
        allowed = enabled
    else:
        enabled_results = _run_actions(enabled, phase="enabled")
        allowed = _bool_from_results(enabled_results, default=True)

    if not allowed:
        return {
            "fired": False,
            "triggered": False,
            "allowed": False,
            "results": [],
            "value": value,
            "event": event,
            "key": used_key,
        }

    # ----------------------------
    # trigger evaluate
    # ----------------------------
    hay = [_safe_str(x) for x in (list(argv) if argv is not None else sys.argv)]
    needles = [str(x) for x in _listify(when)] if when is not None else None
    env_keys = [str(x) for x in _listify(env)] if env is not None else []

    triggered = True if needles is None else (_match_needles(needles, hay) or _env_hit(env_keys, needles))
    if invert:
        triggered = not triggered

    if not triggered:
        return {
            "fired": False,
            "triggered": False,
            "allowed": True,
            "results": [],
            "value": value,
            "event": event,
            "key": used_key,
        }

    # ----------------------------
    # test phase (optional)
    # ----------------------------
    if test is not None:
        test_results = _run_actions(test, phase="test")
        ok = _bool_from_results(test_results, default=True)
        if not ok:
            return {
                "fired": False,
                "triggered": True,
                "allowed": False,
                "results": test_results,
                "value": value,
                "event": event,
                "key": used_key,
            }

    # ----------------------------
    # fire
    # ----------------------------
    if once:
        state.setdefault("__On_once__", set()).add(used_key)

    results: List[Any] = []

    if do is None:
        # default action is print
        fn = printer if callable(printer) else None
        if fn:
            try:
                results.append(fn(value, label=label, event=event, ctx=ctx or {}))
            except Exception as e:
                if not quiet:
                    print(f"[On] printer error: {e}")
                if log_file:
                    _write(log_file, f"[On] printer error: {e}\n{traceback.format_exc()}")
                if raise_errors:
                    raise
                results.append(e)
        else:
            # built-in
            lab = label or event
            results.append(_default_print(value, label=lab))
    else:
        results = _run_actions(do, phase="do")

    out = {
        "fired": True,
        "triggered": True,
        "allowed": True,
        "results": results,
        "value": value,
        "event": event,
        "key": used_key,
    }

    if exit:
        sys.exit(0)

    return out


# ----------------------------
# examples
# ----------------------------
if __name__ == "__main__":
    # 1) Simple CLI trigger: prints only when -v is present
    On({"a": 1, "b": 2}, when="-v", label="debug", match="eq")

    # 2) Substring trigger anywhere in argv: contains
    On("trace me", when="trace", match="contains", icase=True)

    # 3) Regex trigger: any arg matches pattern
    On("regex hit", when=r"^--debug(=.*)?$", match="regex")

    # 4) test as list of actions: require env DEBUG to be truthy
    def is_debug(_):
        val = os.getenv("DEBUG", "")
        return val.strip().lower() not in ("", "0", "false", "no", "off")

    On(
        "runs only if -v AND DEBUG env truthy",
        when="-v",
        test=[is_debug],
    )

    # 5) do as list mixing dict + function
    def pr_value(v, **kw):
        print("PR:", v, kw)
        return True

    On(
        {"hello": "world"},
        when="--cyan",
        do=[
            {"fn": pr_value, "kwargs": {"c": "cyan"}, "inject": {"value": False, "ctx": False}, "call": "pos"},
            {"print": True, "label": "also printed"},
        ],
    )

    # 6) enabled as actions: gate based on a computed condition
    def gate(_):
        return "--allow" in sys.argv

    On("only if --allow", when="--do", enabled=[gate])

    # 7) once per event
    st = {}
    On("fires once", event="startup", once=True, state=st)
    On("won't fire again", event="startup", once=True, state=st)
