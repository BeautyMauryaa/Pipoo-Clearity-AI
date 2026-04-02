# test_mic.py
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = False

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source, timeout=10, phrase_time_limit=10)
    
try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except Exception as e:
    print(f"Error: {e}")