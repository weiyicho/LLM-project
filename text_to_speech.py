import speech_recognition as sr
import pyttsx3
import requests
from PIL import Image

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait() 
    engine.stop()  # Stop the engine after speaking