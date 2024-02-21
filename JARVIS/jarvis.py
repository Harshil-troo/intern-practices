import speech_recognition as sr
import pyttsx3
import sounddevice

def say(str):
    speaker = pyttsx3.init()
    speaker.say(str)
    speaker.runAndWait()
say("Hello and welcome!!!")

def listen():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening... Sir!")
            audio = r.listen(mic)
            text = r.recognize_google(audio)
            print(text)
            return text.lower()

    except Exception:
        print("Sorry Sir! Please Say Again")


listen()


