import os
from dotenv import load_dotenv

load_dotenv()
import speech_recognition as sr
import webbrowser
import pyttsx3 #text to speech
import musiclibrary
import requests
# from openai import OpenAI
import google.generativeai as genai

# pip install pocketsphinx

recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = os.getenv("NEWS_API_KEY")
apiKey = os.getenv("GOOGLE_API_KEY")
# def speak(text):
#     print("Speaking:", text)
#     engine.stop()
#     engine.say(text)
#     engine.runAndWait()

def speak(text):
    import pyttsx3
    engine = pyttsx3.init('sapi5') 
    engine.say(text)
    engine.runAndWait()
    
genai.configure(api_key=apiKey)

def aiprocess(command):
    model = genai.GenerativeModel("gemini-2.5-flash-native-audio-latest")
    response = model.generate_content(command)
    return response.text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # parse the json response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles',[])
            
            # print the headlines
            for article in articles:
                speak(article['title'])
    else:
        output = aiprocess(c)
        speak(output)
        
if __name__ == "__main__":
    speak("Initalizing Jarvis...")

    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
            
        # recognize speech using google
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                
        except Exception as e:
            print("Error; {0}".format(e))