import speech_recognition as sr
from gtts import gTTS
from utils.process_commands import processCommand
from utils.commands import speak

from dotenv import load_dotenv
load_dotenv()
from utils.aichatmodel import get_response

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    #? Listen for from the microphone

    while(True):
        r = sr.Recognizer()

        print("Listening...")
        try:
            with sr.Microphone() as source:
                audio = r.listen(source,timeout=5)
                print("Recognizing...")
            word = r.recognize_google(audio)
            print("You said: ", word)

            # tempWord = "jarvis";
            if (word.lower() == "hello"):
                speak("How can I help you?")
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source,timeout=5)
                    command = r.recognize_google(audio)
                processCommand(command)

            if ("google" in word.lower()):
                speak("Why calling me specially ?")
                with sr.Microphone() as source:
                    print("Gemini Listening...")
                    audio = r.listen(source,timeout=5)
                    command = r.recognize_google(audio)
                
                while("end this talk" not in command):
                    print("Gemini Thinking...")
                    response = get_response(command)
                    print("speakIng...",response)
                    speak(response)
                    with sr.Microphone() as source:
                        print("Gemini Listening...")
                        audio = r.listen(source,timeout=5)
                        command = r.recognize_google(audio)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

