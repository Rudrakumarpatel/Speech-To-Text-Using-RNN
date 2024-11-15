import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment
import numpy as np
import random

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech (Gujarati response)
def SpeakText(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Set voice to one that speaks in Gujarati
    for voice in voices:
        if 'gujarati' in voice.languages:  # Search for a Gujarati voice
            engine.setProperty('voice', voice.id)
            break

    engine.say(command)
    engine.runAndWait()

# Function to degrade the quality of the audio file
def degrade_audio_quality(file_path):
    # Load the audio file using pydub
    audio = AudioSegment.from_wav(file_path)
    
    # Reduce sample rate to lower quality
    audio = audio.set_frame_rate(8000)  # Lower sample rate for worse quality
    
    
    audio = audio.set_channels(1).set_sample_width(2) 
    
   
    samples = np.array(audio.get_array_of_samples())
    noise = np.random.normal(0, 1000, samples.shape[0])  
    noisy_samples = samples + noise.astype(np.int16)
    

    noisy_samples = np.clip(noisy_samples, -2**15, 2**15 - 1)

    noisy_audio = audio._spawn(noisy_samples.tobytes())

    # Save the degraded audio
    degraded_file = file_path.replace('.wav', '_degraded.wav')
    noisy_audio.export(degraded_file, format="wav")
    
    return degraded_file


def introduce_error(text, error_probability=0.3):
    words = text.split()
    
    # Add random changes to simulate errors
    for i in range(len(words)):
        rand_val = random.random()
        
       
        if rand_val < error_probability:
            word = words[i]
            if len(word) > 2:
                # Swap two random characters in the word
                idx1, idx2 = random.sample(range(len(word)), 2)
                word = list(word)
                word[idx1], word[idx2] = word[idx2], word[idx1]
                words[i] = ''.join(word)
                    
        
        elif rand_val < 3 * error_probability:
            if random.random() < 0.25:  
                words[i] = ""

   
    return ' '.join(word for word in words if word != "")  # Remove empty words


def file_speech_to_text(file_path):
    degraded_file = degrade_audio_quality(file_path)
    print(f"Processing degraded file: {degraded_file}")

    with sr.AudioFile(degraded_file) as source:
        
        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            # Listen to the audio file
            audio = r.record(source)

        
            MyText = r.recognize_google(audio, language='gu-IN')  
            MyText = MyText.lower()  

           
            MyText_with_error = introduce_error(MyText, error_probability=0.3)  
            print("Did you say:", MyText_with_error)

        except sr.RequestError as e:
            print(f"Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Could not understand the speech.")



