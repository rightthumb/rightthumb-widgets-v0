import re


def nthData(data, path=None, search=None, stop_at_lists=True, print_result=True):
    """
    Browse nested dict/list paths without printing contents.

    # can be used with json or csv or nth dimensional

    Search__Trigger__Inject_Fields_Records

    Args:
        data: Any nested Python structure (dict/list/etc).
        path: Optional path string like:
              'a.b.c'
              '[1].name'
              'a.[0].address'
              'a.b.[2].c'
        search: Optional string to search against full paths.
                When used, traverses everything and returns matching full paths.
        stop_at_lists: When indexing without a path, stop recursion once a list is hit.
        print_result: Print the path list when True.

    Returns:
        If search is used:
            list of full matching paths
        If path is used:
            list of child/indexable paths under that node
        If neither is used:
            list of indexable paths from root
    """

    def parse_path(path_str):
        """
        Convert:
            a.b.[0].name
            [1].name
            a[0].name
        into:
            ['a', 'b', 0, 'name']
        """
        if path_str is None:
            return []

        path_str = str(path_str).strip()
        if not path_str:
            return []

        tokens = []
        i = 0
        buff = ""

        while i < len(path_str):
            ch = path_str[i]

            if ch == ".":
                if buff:
                    tokens.append(buff)
                    buff = ""
                i += 1
                continue

            if ch == "[":
                if buff:
                    tokens.append(buff)
                    buff = ""

                end = path_str.find("]", i)
                if end == -1:
                    raise ValueError(f"Invalid path, missing ] in: {path_str}")

                idx_text = path_str[i + 1:end].strip()

                if not re.fullmatch(r"-?\d+", idx_text):
                    raise ValueError(f"Invalid list index in path: [{idx_text}]")

                tokens.append(int(idx_text))
                i = end + 1
                continue

            buff += ch
            i += 1

        if buff:
            tokens.append(buff)

        return tokens

    def tokens_to_path(tokens):
        """
        Convert ['a', 'b', 0, 'name'] -> 'a.b.[0].name'
        """
        out = []
        for token in tokens:
            if isinstance(token, int):
                out.append(f"[{token}]")
            else:
                out.append(str(token))

        result = ""
        for part in out:
            if part.startswith("["):
                if result:
                    result += "." + part
                else:
                    result = part
            else:
                if result:
                    result += "." + part
                else:
                    result = part
        return result

    def get_node(obj, tokens):
        current = obj
        for token in tokens:
            if isinstance(token, int):
                if not isinstance(current, list):
                    raise TypeError(f"Expected list before index [{token}]")
                current = current[token]
            else:
                if not isinstance(current, dict):
                    raise TypeError(f"Expected dict before key '{token}'")
                current = current[token]
        return current

    def index_paths(obj, base_tokens=None):
        """
        Build a path index.
        - Recurses through dicts
        - Stops at lists by default
        - Does not print or return values, only paths
        """
        if base_tokens is None:
            base_tokens = []

        results = []

        if isinstance(obj, dict):
            for key, value in obj.items():
                new_tokens = base_tokens + [key]
                results.append(tokens_to_path(new_tokens))

                if isinstance(value, dict):
                    results.extend(index_paths(value, new_tokens))
                elif isinstance(value, list):
                    if not stop_at_lists:
                        results.extend(index_paths(value, new_tokens))

        elif isinstance(obj, list):
            for i, value in enumerate(obj):
                new_tokens = base_tokens + [i]
                results.append(tokens_to_path(new_tokens))

                if isinstance(value, dict):
                    results.extend(index_paths(value, new_tokens))
                elif isinstance(value, list):
                    if not stop_at_lists:
                        results.extend(index_paths(value, new_tokens))

        return results

    def traverse_all_paths(obj, base_tokens=None):
        """
        Traverse everything and return every path.
        Useful for search mode.
        """
        if base_tokens is None:
            base_tokens = []

        results = []

        if isinstance(obj, dict):
            for key, value in obj.items():
                new_tokens = base_tokens + [key]
                results.append(tokens_to_path(new_tokens))
                results.extend(traverse_all_paths(value, new_tokens))

        elif isinstance(obj, list):
            for i, value in enumerate(obj):
                new_tokens = base_tokens + [i]
                results.append(tokens_to_path(new_tokens))
                results.extend(traverse_all_paths(value, new_tokens))

        return results

    # -------------------------
    # SEARCH MODE
    # -------------------------
    if search is not None:
        all_paths = traverse_all_paths(data)
        needle = str(search).lower().strip()
        result = [p for p in all_paths if needle in p.lower()]

        if print_result:
            for item in result:
                print(item)

        return result

    # -------------------------
    # PATH MODE
    # -------------------------
    if path is not None:
        tokens = parse_path(path)
        node = get_node(data, tokens)
        result = index_paths(node, tokens)

        if print_result:
            for item in result:
                print(item)

        return result

    # -------------------------
    # ROOT INDEX MODE
    # -------------------------
    result = index_paths(data)

    if print_result:
        for item in result:
            print(item)

    return result