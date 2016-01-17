#imports
import synthesize
import speech
import inputs
import time
import interpreter
import camera_util, light, shutil, emailio
from PIL import Image
#import face

in_normal_mode = True
check_email_count = 0

synthesize.say('Hello. I am Jauffre: Your friendly neighborhood house bot!')
time.sleep(3)
#Here we begin the command waiting loop.

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
        if False:#compare_photos("pictures/current.jpg", "pictures/last.jpg", in_alarm):
            #Store current photo
            shutil.copyfile('pictures/kept/current.jpg','pictures/kept/sec_'+time.time())
            if not in_alarm:
                in_alarm = True
                #Email current photo to Trevor
                emailio.send_file('trevedwa@gmail.com','Possible security breach detected','pictures/current.jpg')
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
            time.sleep(4)
        #shutil.copyfile('pictures/current.jpg','pictures/last.jpg') TODO


#Compares two photos, returning true if they are significantly different (motion detection levels)
#Reduced threshold if in an alarm?
def compare_photos( path1, path2, in_alarm):
    imga = Image.open(path1)
    imgb = Image.open(path2)
    error_thresh = .2
    if (in_alarm):
        error_thresh = .1
    return mse(imga, imgb) > error_thresh


#Source: http://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
