import webbrowser
import wikipedia
import pyjokes
import pyautogui
import datetime

def implement_va(input_query, speak_va):
    user_query = input_query()
    print('user query ....', user_query)

    def report_time():
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        return current_time

    if 'close' in user_query or 'exit' in user_query:
        exit()

    elif 'time' in user_query or 'what is the time' in user_query or 'whats the time' in user_query:
        current_time = report_time()
        print(f"the current time is {current_time}")
        speak_va(f"the current time is {current_time}")

    elif 'hi' in user_query or 'hello' in user_query:
        speak_va("Greetings")

    elif 'what is your name' in user_query:
        speak_va("I am Jarvis")

    elif 'who are you' in user_query:
        speak_va("I am your Assistant")

    elif 'open website' in user_query:  
        speak_va(
            "Please type the name of the website that you want to open (specify the full url) \n")
        website_name = input()
        print(website_name)
        webbrowser.open(website_name)
        speak_va(f"{website_name} opened.")

    elif 'wikipedia' in user_query:
        speak_va("Searching on Wikipedia")
        user_query = user_query.replace('wikipedia', ' ')
        result = wikipedia.summary(user_query, sentences=4)
        print(result)
        speak_va(result)

    elif 'joke' in user_query or 'tell me a joke' in user_query or 'crack a joke' in user_query:
        random_joke = pyjokes.get_joke()
        print(random_joke)
        speak_va(random_joke) 

    elif 'screenshot' in user_query or 'take a screenshot' in user_query:
        image = pyautogui.screenshot()
        image.save('screenshot.png')
        speak_va('Screenshot taken.')

    elif 'what is the weather' in user_query or 'weather' in user_query or 'whats the weather' in user_query:
        webbrowser.open('https://www.google.com/search?q=weather')

    elif 'search' in user_query:
        speak_va("What do you want me to search for (please type) ? ")
        search_term = input()
        search_url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(search_url)
        speak_va(f"here are the results for the search term: {search_term}")

    else:
        speak_va("This is not implemented yet. Searching on google...");
        webbrowser.open(f"https://www.google.com/search?q={user_query}")