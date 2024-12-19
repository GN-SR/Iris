import re

def extravt_yt_term(command):
    pattern = r'play\s+.on\s+youtube'

    match = re.search(pattern, command, re.IGNORECASE)

    return match.group(1) if match else None

def PlayYoutube(query):
    search_term = extravt_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)