import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level 0-1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the voice (0 for male, 1 for female)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to wish user based on the time of day
def wish_me():
    hour = datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Boss...")
    elif 12 <= hour < 17:
        speak("Good Afternoon Master...")
    else:
        speak("Good Evening Sir...")

# Function to process voice commands
def take_command(command):
    command = command.lower()

    if 'hey' in command or 'hello' in command:
        speak("Hello Sir, How May I Help You?")
    elif 'open google' in command:
        webbrowser.open("https://google.com")
        speak("Opening Google...")
    elif 'open youtube' in command:
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube...")
    elif 'open facebook' in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook...")
    elif 'what is' in command or 'who is' in command or 'what are' in command:
        query = command.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"This is what I found on the internet regarding {command}")
    elif 'wikipedia' in command:
        query = command.replace("wikipedia", "").strip()
        webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
        speak(f"This is what I found on Wikipedia regarding {command}")
    elif 'time' in command:
        time_str = datetime.now().strftime("%H:%M")
        speak(f"The current time is {time_str}")
    elif 'date' in command:
        date_str = datetime.now().strftime("%B %d")
        speak(f"Today's date is {date_str}")
    elif 'calculator' in command:
        webbrowser.open('Calculator:///')
        speak("Opening Calculator")
    else:
        query = command.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"I found some information for {command} on Google")

# Function to listen to user input via microphone
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  # Wait for 1 second of silence
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there seems to be a problem with the speech service.")
        return ""

# Initialize and wish the user when the script starts
if __name__ == "__main__":
    speak("Initializing Peter...")
    wish_me()

    while True:
        command = listen()
        if command:
            take_command(command)