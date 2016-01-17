#imports
import synthesize
import speech
import inputs
import time
import email
#import face

in_normal_mode = True


synthesize.say('My name is Jauffree.')
synthesize.say('Send me a command.')
#Here we begin the command waiting loop.
#speech.recognize() TODO: Make this work on the py

while True:
    command = inputs.next()
