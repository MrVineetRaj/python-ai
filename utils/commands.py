import speech_recognition as sr
import pyttsx3
import os
import requests
from gtts import gTTS
import pygame 

from utils.softwares import brave_browser
from utils.musicLibrary import music
from dotenv import load_dotenv
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text, lang='en')
    tts.save('temp.mp3')
    pygame.mixer.init() 
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def fetchNews():
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
    res = res.json()
    titles = [article["title"] for article in res["articles"]]
    print("Extracted Titles:")
    for i in range(5):
        speak(f"news {i+1} is here {titles[i]}")

def playAnime(command):
    tempLst = command.lower().split(" ")
    anime_name_lst = []
    for i in range(1,len(tempLst)):
        if(tempLst[i] != "play" and tempLst[i] != "anime"):
            anime_name_lst.append(tempLst[i])
    anime_name = "+".join(anime_name_lst)
    brave_browser.open(f"https://hianime.to/search?keyword={anime_name}")

def playMusic(command):
    musicToPlay =  music[command.lower().split(" ")[2]]
    print("Playing: ", command.lower().split(" ")[2])
    brave_browser.open(musicToPlay)
