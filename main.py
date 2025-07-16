import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="api key here",  base_url="https://api.deepseek.com"
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ]
    )

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")  
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music.music[song]
        webbrowser.open(link)
    else:
         output = aiProcess(c)
         speak(output) 
        

 
if __name__ == "__main__":
    speak("Initializing ethan......")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
                word = recognizer.recognize_google(audio)
                print(f"Heard:{word}")
                if (word.lower() == "hello"):
                    speak("Yes sir")
                # Listen for command
                    with sr.Microphone() as source:
                     print("ethan Active...")
                     audio = recognizer.listen(source)
                     command = recognizer.recognize_google(audio)

                     processCommand(command)


        except Exception as e:
            print(f"Error:{e}")
            speak("Sorry, I couldn't understand.")