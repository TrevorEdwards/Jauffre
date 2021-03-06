#imports
import math
import operator
import numpy as np
import synthesize
import cv2
import speech
import inputs
import time
import interpreter
import camera_util, light, shutil, emailio
from PIL import Image
#import face

in_normal_mode = True
check_email_count = 0
pic_count = 0

synthesize.say('Hello. I am Jauffre: Your friendly neighborhood house bot!')
time.sleep(3)
#Here we begin the command waiting loop.


def compare_photos(path1, path2, in_alarm):
    imga = Image.open(path1)
    imgb = Image.open(path2)
    error_thresh = 12200
    val = mse(imga, imgb)
    if (val > error_thresh):
        print(val)
    return val > error_thresh


#Source: http://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
def mse(imageA, imageB):
    h1 = imageA.histogram()
    h2 = imageB.histogram()
    rms = math.sqrt(reduce(operator.add,
                           map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms
in_alarm = False
while True:
    if in_normal_mode:
        command = inputs.next()
        if interpreter.interpret(command):
            in_normal_mode = not in_normal_mode
            emailio.send_mail('jauffreebot@gmail.com','trevedwa@gmail.com','Security mode has been enabled','Security mode has been enabled. Yikes!')
            synthesize.say('Security Mode Activated.  Yikes!')
    else:
        check_email_count += 1
        light.turn_on(True)
        #Take a picture
        camera_util.take_picture("pictures/current.jpg")
        #Compare to previous picture
        if (compare_photos("/home/pi/jauffre/Jauffre/jauffre/pictures/current.jpg", "/home/pi/jauffre/Jauffre/jauffre/pictures/last.jpg", in_alarm) == True) and pic_count > 3:
            #Store current photo
            shutil.copyfile('/home/pi/jauffre/Jauffre/jauffre/pictures/current.jpg','/home/pi/jauffre/Jauffre/jauffre/pictures/kept/sec_'+str(time.time()))
            if not in_alarm:
                in_alarm = True
                #Email current photo to Trevor
		synthesize.say("You shouldn't be snooping around here at this time.  Someone might think you're... up to something.")
                emailio.send_mail('jauffrebot@gmail.com','trevedwa@gmail.com','Uh oh...','Possible security breach detected',['/home/pi/jauffre/Jauffre/jauffre/pictures/current.jpg','/home/pi/jauffre/Jauffre/jauffre/pictures/last.jpg'])
            time.sleep(.5) #We want a video-like history
        else:
            in_alarm = False
            if check_email_count > 3:
                check_email_count = 0
                command = inputs.scan_email()
                if interpreter.interpret(command):
                    in_normal_mode = not in_normal_mode
                    synthesize.say('Security Mode Deactivated.  Chill!')
                    emailio.send_mail('jauffreebot@gmail.com','trevedwa@gmail.com','Security mode has been turned off','Security mode has been turned off. Phew!')
            light.turn_on(False)
            pic_count += 1
            time.sleep(3)
        shutil.copyfile('/home/pi/jauffre/Jauffre/jauffre/pictures/current.jpg','/home/pi/jauffre/Jauffre/jauffre/pictures/last.jpg') 


