import camera

in_normal_mode = True

#Take a picture every 4 seconds.  Alarm if significant change detected.
def security_loop(parent):
    while True:
        if in_normal_mode:
            return
        #Turn on light
        #Take a picture
        #Compare to previous picture
        #If sig dif, notify, play alarm sound?
        #else sleep 4 seconds
