pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer() 

while True: 
    try:
        with speech_recognition.Microphone() as source: 
            print("listening...........")
            recognizer.adjust_for_ambient_noise(source, duration=0.2) 
            audio = recognizer.listen(source) 
            text = recognizer.recognize_google(audio) 
            text = text.lower() 
            print(f"Recognized {text}") 
            
            if "close" in text:
                print("Closing the program.")
                break  # Exit the loop and terminate the program
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer() 
        continue