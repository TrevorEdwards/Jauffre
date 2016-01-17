import synthesize, music, pygame 

def do():
    synthesize.say("Let's make things a little bit more cozy in here.  I'll be here if you need anything.  But I must warn you.  My camera is always on.")
    #dim the lights
    #play romantic music
    pygame.mixer.init()
    channel1 = pygame.mixer.Channel(1)
    channel1.play(pygame.mixer.Sound('./music/romantic.wav'))
