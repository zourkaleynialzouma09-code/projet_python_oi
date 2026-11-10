import pyttsx3


def parler(phrase):
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()

