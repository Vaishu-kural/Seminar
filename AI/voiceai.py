import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

print("Voice Bot Ready! Say 'stop' to exit")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You:", text)

        if "stop" in text.lower():
            engine.say("Goodbye")
            engine.runAndWait()
            break

        reply = "You said " + text
        print("Bot:", reply)

        engine.say(reply)
        engine.runAndWait()

    except:
        print("Sorry, I didn't catch that")