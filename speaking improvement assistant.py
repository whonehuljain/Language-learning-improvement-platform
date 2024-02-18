import speech_recognition as sr
import openai
from gtts import gTTS
import os

import pyttsx3
import re

openai.api_key = 'USE YOUR OPENAI GPT API KEY'

def take_speech_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)  

    try:
        print("Processing...")
        text = recognizer.recognize_google(audio)  
        return text
    except sr.UnknownValueError:
        print("Sorry, can you please repeat this again")
    except sr.RequestError as e:
        print("Sorry, can you please repeat this again")

def process_with_openai(prompt):
    try:
        prompt = f" give a more polished version of this sentence '{prompt}' and also give response to that polished version "
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        gpt3_response = response['choices'][0]['message']['content'].strip()
        gpt3_response = re.sub(r'\b\w+\s*:\s*', '', gpt3_response)
        return gpt3_response
    except Exception as e:
        return "can you please repeat what you just said"

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
while(True):
    speech_text = take_speech_input()
    if speech_text:
        print("You said:", speech_text)
        processed_text = process_with_openai(speech_text)
        if processed_text:
            print("OpenAI Processed Output:", processed_text)
            text_to_speech(processed_text)






















































































































































































































# while(True):
#     speech_text = take_speech_input()
#     if speech_text:
#         print("You said:", speech_text)
#         processed_text = process_with_openai(speech_text)
#         if processed_text:
#             print("OpenAI Processed Output:", processed_text)
#             text_to_speech(processed_text)
