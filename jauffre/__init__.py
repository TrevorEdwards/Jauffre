#imports
import synthesize
import speech
import inputs
import time
#import face

in_normal_mode = True


synthesize.say('My name is Jauffree.')
synthesize.say('Get ready to be impressed.')
#Here we begin the command waiting loop.
#speech.recognize() TODO: Make this work on the py

while True:
    synthesize.say('What is your command?')
    command = inputs.next()
    synthesize.say('You want me to execute command: ' + command)
