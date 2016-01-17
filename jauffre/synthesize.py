import pyttsx
engine = pyttsx.init('espeak')

engine.setProperty('rate', 140)

voices = engine.getProperty('voices')
#myvoice = voices[15]

#engine.setProperty('voice',myvoice.id)

def say(text):
    print text #debug
    if text == "":
        return
    #engine.say(text)
    #engine.runAndWait()
