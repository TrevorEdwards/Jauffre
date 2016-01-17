#receives input from email
import emailio
import time

def next():
    while True:
        time.sleep(5)
        res = emailio.get()
        if res != "" and type(res) == str:
            return res[res.find("Content-Type: text/plain; charset=UTF-8"):]
