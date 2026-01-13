#!/usr/bin/python3

# 694a3f0e-4e58-8331-b6d2-d7f5b40969c6

NOT_SPECIFIED = "*NOT_SPECIFIED*"

def askYesNo(
    question: str,
    default=NOT_SPECIFIED,
    *,
    forceAnswer: bool = True,
    fullWord: bool = False,
    caseSensitive: bool = False,
    values=None,          # mapping: {True: 'Yes', False: 'No', None: ''} or alias lists
    on: dict | None = None
):
    """
    Returns by default:
      - True/False for Yes/No
      - None for blank when no default (unless you map blank as an alias intentionally)

    values examples:
      {True:'Yes', False:'No'}
      {True:['Yes','Y'], False:['No','N'], None:''}
      {True:['Yes','Y',''], False:'No'}  # allows blank -> True (not recommended unless intentional)
    """

    # ---------- helpers ----------
    def norm(s: str) -> str:
        return s if caseSensitive else s.lower()

    def call_cb(cb, result_key, raw_text=None):
        if cb is None:
            return
        # Try (key, raw) then (key) then ()
        try:
            return cb(result_key, raw_text)
        except TypeError:
            try:
                return cb(result_key)
            except TypeError:
                return cb()

    # ---------- normalize values ----------
    if values is None:
        values = {True: "Yes", False: "No"}  # default

    # Build:
    #   display_labels: for prompt
    #   alias_to_key: map of normalized alias -> key (True/False/None/etc)
    display_order = []
    alias_to_key = {}

    def add_key_aliases(key, spec):
        # spec can be a string or list/tuple/set of strings
        if spec is None:
            return
        if isinstance(spec, (list, tuple, set)):
            aliases = [str(x) for x in spec]
        else:
            aliases = [str(spec)]

        # First alias is treated as the display label (unless key is None and alias == '')
        if key not in display_order:
            display_order.append(key)

        for a in aliases:
            alias_to_key[norm(a)] = key

    for k, spec in values.items():
        add_key_aliases(k, spec)

    # Display labels
    def display_label_for(key):
        spec = values.get(key, "")
        if isinstance(spec, (list, tuple, set)):
            # first item is display label
            return str(next(iter(spec), ""))
        return "" if spec is None else str(spec)

    # Determine which key represents blank input if defined
    # - If values includes None: '' then blank display exists (still maps to None unless you add '' alias elsewhere)
    blank_display = display_label_for(None) if None in values else ""

    # Build prompt string from display labels (ignore empty labels)
    labels = []
    for k in display_order:
        lab = display_label_for(k)
        if lab != "":
            labels.append(lab)
    opts_display = "/".join(labels) if labels else "Yes/No"

    if default is NOT_SPECIFIED:
        prompt = f"{question} [{opts_display}]: "
    else:
        prompt = f"{question} [{opts_display}] (default: {default}): "

    # ---------- matching ----------
    def match_input_to_key(user_in: str):
        u = user_in.strip()
        if u == "":
            # blank input handled outside (so we can apply default logic)
            return None, ""

        u_cmp = norm(u)

        # full word match: must equal one of the aliases exactly
        if fullWord:
            if u_cmp in alias_to_key:
                return alias_to_key[u_cmp], u
            return None, u

        # first-char match: match against display labels + aliases
        first = u_cmp[0]
        hits = set()

        # include aliases
        for alias_norm, key in alias_to_key.items():
            if alias_norm and alias_norm[0] == first:
                hits.add(key)

        if len(hits) == 1:
            return next(iter(hits)), u

        # ambiguous or none
        return None, u

    # ---------- loop ----------
    while True:
        raw = input(prompt)

        # blank
        if raw.strip() == "":
            if default is NOT_SPECIFIED:
                # If user *explicitly* included '' as an alias for some key, honor it.
                # Otherwise blank maps to None (and we loop if forceAnswer).
                if norm("") in alias_to_key:
                    result_key = alias_to_key[norm("")]
                    if on:
                        call_cb(on.get(result_key), result_key, raw)
                    return result_key

                # normal blank behavior -> None
                result_key = None
                if on:
                    # special: allow '' handler for "blank w/out default" if you prefer that key
                    call_cb(on.get("", on.get(None)), "" if "" in on else None, raw)

                if forceAnswer:
                    continue
                return result_key

            # default specified -> interpret it
            d = str(default)
            # If default matches an alias exactly, use it
            d_norm = norm(d)
            if d_norm in alias_to_key:
                result_key = alias_to_key[d_norm]
            else:
                # Try match by first letter unless fullWord is on (then it's invalid)
                if fullWord:
                    result_key = None
                else:
                    result_key, _ = match_input_to_key(d)

            if result_key is None:
                # default couldn't be interpreted
                if forceAnswer:
                    continue
                return None

            if on:
                call_cb(on.get(result_key), result_key, raw)
            return result_key

        # non-blank
        result_key, _raw = match_input_to_key(raw)
        if result_key is None:
            if on:
                call_cb(on.get(None), None, raw)
            if forceAnswer:
                continue
            return None

        if on:
            call_cb(on.get(result_key), result_key, raw)
        return result_key
