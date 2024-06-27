import webbrowser
from utils.commands import speak, fetchNews ,playAnime, playMusic

from utils.aichatmodel import get_response
from utils.startInterview import startInterview

def processCommand(command):
    if(command.lower() == "how are you"):
        speak("I am fine, thank you")

    elif("open google" == command.lower() ):
        webbrowser.open("https://www.google.com")

    elif("open youtube" in command.lower() ):
        webbrowser.open("https://www.youtube.com")

    elif("open linkedin" in command.lower() ):
        webbrowser.open("https://www.linkedin.com/in/vineet-raj-b96381257/")

    elif("open github" in command.lower() ):
        webbrowser.open("https://github.com/MrPriyanshuChamp")

    elif(command.startswith("play") ):
        if("music" in command.lower()):
            playMusic(command)
        elif("anime" in command.lower()):
            playAnime(command)

    elif("news" in command.lower()):
        fetchNews()

    elif ("start an interview" in command.lower() ):
        startInterview()
    else:
        print("Thinking...")
        response = get_response(command)
        print("speakIng...",response)
        speak(response)

