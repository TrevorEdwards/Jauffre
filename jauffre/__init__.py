#imports
import synthesize
import speech
import inputs
import time
import interpreter
import camera_util, light, shutil, emailio
#import face

in_normal_mode = True
check_email_count = 0

synthesize.say('My name is Jauffree.')
synthesize.say('Send me a command.')
#Here we begin the command waiting loop.
#speech.recognize() TODO: Make this work on the py

while True:
    if in_normal_mode:
        command = inputs.next()
        interpreter.interpret(command)
    else:
        check_email_count += 1
        light.turn_on(True)
        #Take a picture
        camera_util.take_picture("pictures/current.jpg")
        #Compare to previous picture
        if compare_photos("pictures/current.jpg, pictures/last.jpg"):
            #Store current photo
            shutil.copyfile('pictures/kept/current.jpg','pictures/kept/sec_'+time.time())
            if not in_alarm:
                in_alarm = True
                #Email current photo to Trevor
                emailio.send_file('trevedwa@gmail.com','Possible security breach detected','pictures/current.jpg')
            time.sleep(.5) #We want a video-like history
        else:
            in_alarm = False
            if check_input_count > 25:
                check_input_count = 0
                command = inputs.scan_email()
                interpreter.interpret(command)
            light.turn_on(False)
            time.sleep(4)
        shutil.copyfile('pictures/current.jpg','pictures/last.jpg')


#Compares two photos, returning true if they are significantly different (motion detection levels)
#Reduced threshold if in an alarm?
def compare_photos( path1, path2, in_alarm):
    pass
