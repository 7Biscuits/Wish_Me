import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour <= 12:
        speak("Good Morning sir!")
        speak("Hope you will have a great day!")

    elif hour >=12 and hour <= 18:
        speak("Good Afternoon sir!")
        speak("Hope you are having a good day")

    else:
        speak("Good Evening!")
        speak("Hope you are having a great day")
    
if __name__ == "__main__":
    wish()
    
