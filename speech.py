import speech_recognition as sr
import pyttsx3
import requests
import implementation

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def input_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('tell me....')
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(voice).lower()
            print('this is the query that was made....', query)
            return query
        except Exception as ex:
            print('An exception occurred', ex)


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


def make_request(url):
  response = requests.get(url)
  return response.text

while True:
    implementation.implement_va(input_query, speak_va)