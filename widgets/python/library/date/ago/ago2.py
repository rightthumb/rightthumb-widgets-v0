import time
import re


# ------------------------------------
# Public wrapper (intentionally simple)
# ------------------------------------
def ago(text, delim='-', start_date=None):
    return _Ago.ago(text, delim=delim, start_date=start_date)


class _Ago:
    @staticmethod
    def ago(text, delim='-', start_date=None):
        # -------------------------------
        # 1) < / > duration-date handling
        # -------------------------------
        if text and ('<' in text or '>' in text):
            op = '<' if '<' in text else '>'
            left, right = text.split(op, 1)
            left = left.strip()
            right = right.strip()

            def is_date_side(s):
                return not re.search(r'[a-zA-Z]', s)

            date_str = None
            dur_str = None

            if is_date_side(left) and not is_date_side(right):
                date_str, dur_str = left, right
            elif is_date_side(right) and not is_date_side(left):
                date_str, dur_str = right, left

            if date_str and dur_str:
                # Parse date shorthand
                now = time.localtime()
                parts = date_str.split('-')

                if len(parts) == 3:
                    y, m, d = map(int, parts)
                elif len(parts) == 2:
                    y = now.tm_year
                    m, d = map(int, parts)
                elif len(parts) == 1:
                    y = now.tm_year
                    m = now.tm_mon
                    d = int(parts[0])
                else:
                    raise ValueError(f"Invalid date format: {date_str}")

                start_epoch = int(time.mktime((y, m, d, 0, 0, 0, 0, 0, -1)))

                # Force future-relative math
                dur = dur_str.strip()
                if not dur.startswith('+'):
                    dur = '+' + dur

                # Recurse using anchored start_date
                return _Ago.ago(dur, delim=delim, start_date=start_epoch)

        # -------------------------------
        # 2) Core logic (unchanged style)
        # -------------------------------
        if text is None:
            raise ValueError("Invalid ago format: None")

        raw = text.strip().lower()
        if not raw:
            raise ValueError("Invalid ago format: (empty)")

        base_time = start_date if start_date is not None else time.time()

        direction = -1
        if raw.startswith('+'):
            direction = 1
            raw = raw[1:].strip()

        if delim:
            raw = re.sub(re.escape(delim), '', raw)

        parts = re.findall(r'(\d+(?:\.\d+)?)([a-z<>\|]+)', raw)
        if not parts:
            raise ValueError(f"Invalid ago format: {text}")

        multipliers = {
            's': 1,
            'sec': 1,
            'm': 60,
            'min': 60,
            'h': 3600,
            'd': 86400,
            'w': 604800,
            'mo': 2592000,
            'y': 31536000,
        }

        total_seconds = 0.0

        for value_str, unit_raw in parts:
            value = float(value_str)
            unit = re.sub(r'[^\w]', '', unit_raw)

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
                raise ValueError(f"Unrecognized time unit in: {unit_raw}")

            total_seconds += seconds

        return int(base_time + direction * total_seconds)


