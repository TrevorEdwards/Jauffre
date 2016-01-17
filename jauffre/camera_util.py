import time
import picamera
import synthesize
import emailio
camera = picamera.PiCamera()
# camera.capture('image.jpg')
# camera.hflip = True
camera.vflip = True
# camera.start_preview()
# camera.stop_preview()


# for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
#         print(filename)
#         time.sleep()
#         if i == 59:
#             break

def take_picture( file ):
    camera.capture(file)

def selfie():
	synthesize.say("It's time for a selfie!")
	time.sleep(2)
	synthesize.say('Say Cheese!')
	time.sleep(2)
	synthesize.say('Snip!')
	filename = ('image{}.jpg'.format(time.time()))
	take_picture('./selfies/' + filename)
	emailio.send_mail('jauffrebot@gmail.com', 'trevedwa@gmail.com', '', '', ['./selfies/' + filename])

