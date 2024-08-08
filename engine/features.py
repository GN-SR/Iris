from playsound import playsound
import eel



# Playing Assistanst Start Sound
def playAssistantSound():
    music_dir = "www\\assets\\audio\\mixkit-machine-activation-short-3180.wav"
    playsound(music_dir)

@eel.expose
def playAssistantSound1():
    music_dir1 = "www\\assets\\audio\\wake-up-the-robot-84894.mp3"
    playsound(music_dir1)