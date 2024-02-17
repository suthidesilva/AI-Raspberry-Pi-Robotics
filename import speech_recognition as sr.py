import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to speak the given text"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen for user input"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_llama_llms(audio)  # Llama LLMs speech recognition
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Request error: {e}")
        return ""

def process_command(command):
    """Function to process user commands"""
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "goodbye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Starting voice assistant")
    while True:
        command = listen()
        process_command(command)
