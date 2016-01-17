import time
from subprocess import call

def say(text):
    print text #debug
    if text == "":
        return
    call(["say", text])
    time.sleep(1)
