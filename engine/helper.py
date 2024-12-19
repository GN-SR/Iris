import re

def extravt_yt_term(command):
    pattern = r'play\s+.on\s+youtube'

    match = re.search(pattern, command, re.IGNORECASE)

    return match.group(1) if match else None

