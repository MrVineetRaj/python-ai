import speech_recognition as sr
import webbrowser
import utils.musicLibrary as musicLibrary
from gtts import gTTS

from utils.commands import speak, fetchNews

from utils.aichatmodel import get_response
from dotenv import load_dotenv
load_dotenv()


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
    elif(command.startswith("play")):
        music =  musicLibrary.music[command.lower().split(" ")[1]]
        print("Playing: ", command.lower().split(" ")[1])
        webbrowser.open(music)
    elif("news" in command.lower()):
        fetchNews()
    else:
        print("Thinking...")
        response = get_response(command)
        print("speakIng...")
        speak(response)

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    #? Listen for from the microphone

    while(True):
        r = sr.Recognizer()

        print("Listening...")
        try:
            with sr.Microphone() as source:
                print("Recognizing...")
                audio = r.listen(source,timeout=5)
            word = r.recognize_google(audio)
            print("You said: ", word)
            if (word.lower() == "jarvis"):
                speak("How can I help you?")
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source,timeout=5)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

