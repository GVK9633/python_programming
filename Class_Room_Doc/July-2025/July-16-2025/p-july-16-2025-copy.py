import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening = sr.Recognizer()
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    try:
        with sr.Microphone() as mic:
            print('Listening...')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'kodi' in cmd:
                cmd = cmd.replace('kodi', '').strip()
                print(f"Command after 'kodi': {cmd}")
                return cmd
            else:
                print("Trigger word 'kodi' not found.")
                return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

def run():
    cmd = hear()
    if cmd and 'play' in cmd:
        song = cmd.replace('play', '').strip()
        speak('Playing ' + song)
        pk.playonyt(song)
    elif cmd:
        speak("Sorry, I can only play songs right now.")
    else:
        print("No command received.")

run()
