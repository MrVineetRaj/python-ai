import speech_recognition as sr
from gtts import gTTS
from utils.commands import speak
from utils.interviewer import get_question
from utils.data.resume import resume

def startInterview():
    speak("Starting Interview... Please provide the following details to start the interview.")
    details ={
        "jobProfile" : "",
        "company" : "",
        "duration" : "",
        "resume":str(resume),
    }

    interview_label = ""
    main_qus = ["jobProfile","company","duration","interview_label"]
    for qus in main_qus:
        speak(qus)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,timeout=5)
            detail = r.recognize_google(audio)
            if(qus == "interview_label"):
                interview_label = detail
            else:
                details[qus] = detail
            
    speak("Going to start your resume in few seconds")
    print("Thinking...")

    response = get_question("starting",details)
    print("speakIng...",response)
    speak(response)

    while(True):
        if("Ending this interview" not in response):
            r = sr.Recognizer()
            try:
                with sr.Microphone() as source:
                    print("Interviewer is Listening...")
                    audio = r.listen(source,timeout=60)
                    print("Recognizing...")
                    ans = r.recognize_google(audio)
                    print("You said: ", ans)
                    response = get_question("continue",ans)
                    print("speakIng...",response)
                    speak(response)
            except sr.UnknownValueError:
                print("Could not understand audio can you please repeat?")
        else:
            response = get_question("ending","")
            break
    print("Interviewer is speakIng...")

    with open(f"Interview_Analysis/{interview_label}.txt","w") as f:
        f.write(response)
    speak(response)
    speak("Interview Ended")

    

