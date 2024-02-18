import time
import google.generativeai as genai

GOOGLE_GEMINI_API_KEY = "USE YOUR GEMINI API KEY"
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

def provide_reading_text():
     response = chat.send_message("Give a reading comprehension to test the reading ability. Do not give questions, or headings, just simple comprehension.")
     print(response.text)
     return response.text


def calculate_reading_speed(text_length):
    input("Press Enter to start the timer.")
    start_time = time.time()

    input("Press Enter to stop the timer after you finish reading.")
    end_time = time.time()

    reading_time = (end_time - start_time) / 60  

    if reading_time > 0:
        reading_speed = text_length / reading_time
    else:
        print("Reading time must be greater than 0.")
        return None

    return reading_speed

text_length = len(provide_reading_text())  
reading_speed = calculate_reading_speed(text_length)

def reading_feedback():
    response = chat.send_message(f"the reading speed is {reading_speed} w.p.m., give feedback on reading based on the speed.")
    return response.text


print(reading_feedback())
