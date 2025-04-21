import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import os

import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

def speak(text):
    os.system(f"speak {text}")
    engine.say(text)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<15:
        speak("Good Afternoon!")
    elif hour>=21 and hour<=24:
        speak("Its Night!")
    else:
        speak("Good Evening!")

    speak("I'm a Personal A.I., how can i help u..")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"You Said: {query}")
            return query
        except Exception as e:
            return "Some thing went wrong, please try again!"

if __name__ == "__main__":
    greeting()
    while True:
        print("Hearing...")
        query = takeCommand()
        sites = [["Youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
                 ["google", "https://google.com"], ["Music", "https://music.youtube.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]}....")
                webbrowser.open_new_tab(site[1])

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strfTime}")

        if "what is" in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia....")
            print(results)
            speak(results)
