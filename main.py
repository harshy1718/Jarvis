import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from groq import Groq

recognizer = sr.Recognizer()
engine = pyttsx3.init()
# newsapi = your api key

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    # client = Groq(api_key = your api key)
    completion = client.chat.completions.create(
        model = "llama3-8b-8192",
        messages= [
            { "role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud." },
            { "role": "user","content": command}
        ]
    )

    return completion.choices[0].message.content
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=apple&from=2024-09-12&to=2024-09-12&sortBy=popularity&apiKey={newsapi}")
        print("news")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])
    
    else:
        output = aiProcess(c)
        speak(output)
    

if __name__ == "__main__":
    speak("Intializing Jarvis.....")
    while True:
        r = sr.Recognizer()
        
            
        print("Recognizing....")
            
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                    
        except Exception as e:
            print(f"Error; {e}")
