import pyglet
player = pyglet.media.Player()

def add_song_to_queue(song):
	song = pyglet.media.load('./music/' + song)
	#song.play()
	#song.pause()
	player.queue(song)

def play_song():
	player.play()
	
def pause_song():
	player.pause()

def next_song():
	player.next_source()

def stop_song():
	while(player.source != None):
		player.next_source()