import synthesize, music, pyglet

def do():
    synthesize.say("Let's make things a little bit more cozy in here.  I'll be here if you need anything.  But I must warn you.  My camera is always on.")
    #dim the lights
    #play romantic music
    music.player = pyglet.media.Player()
    music.add_song_to_queue('romantic.wav')
    music.play_song()
