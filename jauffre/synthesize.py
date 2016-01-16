import pyttsx
engine = pyttsx.init()

engine.setProperty('rate', 140)

voices = engine.getProperty('voices')
myvoice = voices[15]

print myvoice

engine.setProperty('voice',myvoice.id)

def say(text):
    print text #debug
    engine.say(text)
    engine.runAndWait()
