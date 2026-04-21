import time
import re

def ago(text):
    """
    Convert strings like '10d', '5min', '1y', '25h<', '6mo' into an epoch time
    that represents 'now - [duration]'.

    Supported suffixes:
        s / sec    -> seconds
        m / min    -> minutes
        h          -> hours
        d          -> days
        w          -> weeks
        mo / m     -> months (30 days avg)
        y          -> years (365 days)

    Suffixes like '5minp', '25h<', etc. are also parsed correctly.
    """
    now = time.time()

    # Normalize input
    text = text.strip().lower()

    # Extract numeric and suffix parts
    match = re.match(r'(\d+)([a-z<>\|]*)', text)
    if not match:
        raise ValueError(f"Invalid ago format: {text}")

    value, unit = match.groups()
    value = int(value)

    # Clean up suffixes like 25h< or 5minp
    unit = re.sub(r'[^\w]', '', unit)

    # Map to seconds
    multipliers = {
        's': 1,
        'sec': 1,
        'm': 60,
        'min': 60,
        'h': 3600,
        'd': 86400,
        'w': 604800,
        'mo': 2592000,  # 30 days
        'y': 31536000,  # 365 days
    }

    # Try multiple match attempts
    if unit in multipliers:
        seconds = value * multipliers[unit]
    elif unit.startswith('min'):
        seconds = value * 60
    elif unit.startswith('mo'):
        seconds = value * 2592000
    elif unit.startswith('sec') or unit.startswith('s'):
        seconds = value
    elif unit.startswith('m') and not unit.startswith('mo'):
        seconds = value * 60
    else:
        raise ValueError(f"Unrecognized time unit in: {text}")

    return int(now - seconds)
