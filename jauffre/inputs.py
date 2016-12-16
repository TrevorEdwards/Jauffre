#receives input from email
import emailio
import time
import speech
import urllib2


def next():
    while True:
        time.sleep(2)
	ugh=urllib2.urlopen("https://putget.herokuapp.com/").read()
	return ugh
        rect = speech.recognize()
        print type(rect)
        if rect != "" and type(rect) == unicode:
            return rect
        time.sleep(5)

def scan_email():
	ugh=urllib2.urlopen("https://putget.herokuapp.com/").read()
	return ugh
