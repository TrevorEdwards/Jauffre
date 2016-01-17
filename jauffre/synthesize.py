import pyttsx
import time
from threading import Thread

engine = pyttsx.init()
# engine.startLoop(False)
engine.setProperty('rate', 140)
voices = engine.getProperty('voices')
myvoice = voices[15]
engine.setProperty('voice',myvoice.id)

q = []

def shit_loop(myq):
    while True:
        print "shit"
        if len(myq) > 0:
            pop = myq.pop(0)
            print pop #debug
            if pop == "":
                return
            engine.say(pop)
        time.sleep(1)

thread = Thread(target = shit_loop, args = (q,))
thread.start()
# thread.join()
print "thread finished...exiting"



def say(text):
    q.append(text)
