import speech_recognition as sr
from gtts import gTTS
from utils.process_commands import processCommand
from utils.commands import speak

from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    #? Listen for from the microphone

    while(True):
        r = sr.Recognizer()

        print("Listening...")
        try:
            with sr.Microphone() as source:
                audio = r.listen(source,timeout=10)
                print("Recognizing...")
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


