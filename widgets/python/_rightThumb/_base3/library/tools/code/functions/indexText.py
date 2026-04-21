def indexText(text):
    allowed_chars = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.')
    index = {}
    start = None

    for i, char in enumerate(text):
        if char in allowed_chars:
            if start is None:
                start = i
        else:
            if start is not None:
                index[start] = i
                start = None

    if start is not None:
        index[start] = len(text)

    return index