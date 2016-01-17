#receives input from email
import emailio
import time
import speech


def next():
    emailcount = 6
    while True:
        emailcount = emailcount + 1
        if emailcount > 5:
            emailcount = 0
            res = emailio.get()
            if res != "" and type(res) == str:
                return res[res.find("Content-Type: text/plain; charset=UTF-8"):]
        rect = speech.recognize()
        print type(rect)
        if rect != "" and type(rect) == unicode:
            return rect

def scan_email():
    res = emailio.get()
    if res != "" and type(res) == str:
        return res[res.find("Content-Type: text/plain; charset=UTF-8"):]
    else:
        return ""
