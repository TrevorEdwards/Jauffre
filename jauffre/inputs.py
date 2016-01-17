#receives input from email
import emailio
import time

def next():
    while True:
        time.sleep(5)
        res = emailio.get()
        if res != "":
            return res
