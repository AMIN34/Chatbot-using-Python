import pyttsx3
import random
import winsound
from time import sleep
import speech_recognition as sr
import datetime
import wikipedia
from playsound import playsound
import os
import webbrowser
import tkinter
import re
import shutil
import requests
import json

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)


root = tkinter.Tk()


root.title('Chatbot')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greeting
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 11:
        speak("Good Morning Sir.")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening Sir.")
    
    speak("How may I Help you?")


# Quering
def takecommand():    
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)
        
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"You said: {query}\n")
        if 'youtube' in query:
                webbrowser.open('www.youtube.com') 
                
        elif "search" in query:
                speak("Fetching Results")
                query = query.replace("search", " ")
                results = wikipedia.summary(query, sentences=3)
                speak('According to Wikipedia.com')
                
                print(results)
                speak(results) 
                    

        elif 'open youtube' in query:
                        webbrowser.open("www.youtube.com")
                
        elif 'open reddit' in query:
                        webbrowser.open("https://www.reddit.com/")
                
        elif 'open news' in query:
                        webbrowser.open("https://project-news-app.herokuapp.com/")
                
        elif 'open cricket' in query:
                        webbrowser.open("https://www.cricbuzz.com/")

        elif 'open google' in query:
                        webbrowser.open("www.google.com")
                
        elif 'time' in query:
                        time  = datetime.datetime.now().strftime("%H:%M")
                        speak(time)
                
        elif 'open browser' in query:
                        os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

        """
		elif 'arrange' in query and 'files' in query:
		path = tkinter.filedialog.askdirectory()
        #This populates a list with the filenames in the directory
		list_ = os.listdir(path)
		#Traverses every file
        for file_ in list_:
			name,ext = os.path.splitext(file_)
            print(name)
            #Stores the extension type
            ext = ext[1:]
            #If it is directory, it forces the next iteration
            if ext == '':
				continue
                #If a directory with the name 'ext' exists, it moves the file to that directory
                if os.path.exists(path+'/'+ext):
                    shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
                #If the directory does not exist, it creates a new directory
                else:
                    os.makedirs(path+'/'+ext)
                    shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
		"""
        
        elif 'joke' in query or 'laugh' in query:
            r2 = requests.get("https://v2.jokeapi.dev/joke/Any")
            j2=r2.json()

            if j2["type"] == "single": # Print the joke
                speak(j2["joke"])
            else:
                speak(j2["setup"])
                speak(j2["delivery"])

        elif 'roll a dice' in query:
            dice = random.randint(1, 6)
            speak(f"The Dice is rolling................. It's a {dice}")

        elif 'flip a coin' in query:
            results = ['Heads', 'Tails']
            result = random.choice(results)
            speak(f"{result}")
        elif 'google' in query:
            message = query
            newlist = message.split()
            newlist.remove('google')
            li = []
            for item in newlist:
                li.append(item+"+")
            final_query = ''.join([str(elem) for elem in li]) 
            print(final_query)
            webbrowser.open(f"https://www.google.com/search?q="+final_query)

        else:
            speak("Sorry couldn't get you...")
                
    except Exception as e:
      print(e)
      return "None"
    return query

if __name__ == "__main__":
    wishme()
    button = tkinter.Button(text="Click to Speak",height=20, width=50, command = lambda : takecommand())

    button.pack()

root.mainloop()
