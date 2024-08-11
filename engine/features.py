from playsound import playsound
import eel
import re
import os
from engine.config import ASSISTANT_NAME
from engine.command import speak
import pywhatkit as kit

# Playing Assistanst Start Sound
def playAssistantSound():
    music_dir = "www\\assets\\audio\\mixkit-machine-activation-short-3180.wav"
    playsound(music_dir)

@eel.expose
def playAssistantSound1():
    music_dir1 = "www\\assets\\audio\\wake-up-the-robot-84894.mp3"
    playsound(music_dir1)


def openCommand(query):
    
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").strip().lower()

    if query!="":
        speak("Opening "+query)
        os.system('start '+query)
    else:
        speak("Not found or Unable to open , sorry for the inconveniance")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    # defining a regular expression pattern
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # using re.search to find the match
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None