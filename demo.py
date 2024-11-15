import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Set voice to one that speaks in Gujarati
    for voice in voices:
        if 'gujarati' in voice.languages:  
            engine.setProperty('voice', voice.id)
            break

    engine.say(command)
    engine.runAndWait()

def live_speech_to_text():
    with sr.Microphone() as source:
        print("Listening for speech...")
        
        r.adjust_for_ambient_noise(source, duration=0.3)
        
        while True:
            try:
                # Listen for live audio
                audio = r.listen(source)
                
                MyText = r.recognize_google(audio, language='gu-IN')  
                MyText = MyText.lower() 
                
                return "Did you say:", MyText
                
            except sr.RequestError as e:
                return f"Could not request results; {0}".format(e)
            except sr.UnknownValueError:
                return "Could not understand the speech."
