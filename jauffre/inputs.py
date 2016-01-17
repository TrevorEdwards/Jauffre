#receives input from email
import emailio
import time
import speech


def next():
    while True:
        res = emailio.get()
        if res != "" and type(res) == str:
            return res[res.find("Content-Type: text/plain; charset=UTF-8"):]
        time.sleep(5)
       # rect = speech.recognize()
       # print type(rect)
       # if rect != "" and type(rect) == unicode:
        #    return rect

def scan_email():
    res = emailio.get()
    if res != "" and type(res) == str:
        return res[res.find("Content-Type: text/plain; charset=UTF-8"):]
    else:
        return ""
