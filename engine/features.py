from playsound import playsound
import eel
import re
import os
import webbrowser
from engine.config import ASSISTANT_NAME
from engine.command import speak
from engine.db import cursor,conn
from engine.helper import extravt_yt_term
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
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").lower().strip()
    app_name = query

    if app_name:  # Ensure app_name is not empty
        try:
            # Fetch the path for the application
            cursor.execute('SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results = cursor.fetchall()

            if results:  # If results exist
                speak(f"Opening {app_name}")
                os.startfile(results[0][0])  # Open the file at the fetched path

            else:  # Check for URLs in the web_command table
                cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
                results = cursor.fetchall()

                if results:  # If a URL is found
                    speak(f"Opening {app_name}")
                    webbrowser.open(results[0][0])  # Open the fetched URL

                else:  # Handle case where neither path nor URL is found
                    speak(f"Opening {app_name}")
                    try:
                        os.system(f'start {query}')
                    except Exception as e:
                        speak(f"Not found: {str(e)}")

        except Exception as e:
            speak(f"Something went wrong: {str(e)}")

          

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)
