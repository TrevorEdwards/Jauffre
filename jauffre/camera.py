import time
import picamera
# camera = picamera.PiCamera()
# camera.capture('image.jpg')
# camera.hflip = True
# camera.vflip = True
# camera.start_preview()
# camera.stop_preview()


for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
        print(filename)
        time.sleep()
        if i == 59:
            break
