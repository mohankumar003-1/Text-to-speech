import pyttsx3

def func(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def textspeech(text):
    func(text)

