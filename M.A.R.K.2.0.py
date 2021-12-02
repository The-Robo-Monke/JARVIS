import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=0 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Mark. Please tell me how may I help you")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_ibm(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print (e)
     print ("say that again please...") 
     return"None"
     return query

if__name___=="___main___":
    wishme()
    while True:
     #if 1:
           query=takecommand().lower()

           if 'wikipedia' in query:
               speak('Searhing Wikipedia...')
               query= query.replace("wikipedia,"")   
               results= wikipedia.summary(query, sentences=2)
               speak("According to wikipedia")
               print(results)
               speak(results)

               elif 'open youtube' in query:
                   webbrowser.open("youtube.com")

               elif 'open google' in query:
                   webbrowser.open('google.com')

                elif 'open stack overflow' in query:
                    webbrowser.open("stackoverflow.com") 

                elif 'open new tab' in query:
                    webbrowser.open_new_tab

                elif "what's the time?" in query:
                    strTime= datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir the time is {strTime}")

                elif 'open chrome' in query:
                    chromepath= "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(chromepath)

                 elif 'Mark you up?' in query:
                     speak("always at your call sir")

                    