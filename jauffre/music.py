
s = Sound() #Define one sound so we don't have overlap

#plays a song in the music folder
def play_song(name):
    s.read(name)
    s.play()

def stop_song():
    s.stop()
