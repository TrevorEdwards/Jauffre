# #import pyglet
# #player = pyglet.media.Player()

# def add_song_to_queue(song):
# #	song = pyglet.media.load('./music/' + song)
# 	#song.play()
# 	#song.pause()
# #	player.queue(song)
# 	pass
# def play_song():
# #	player.play()
# 	pass
# def pause_song():
# #	player.pause()
# 	pass
# def next_song():
# #	player.next_source()
# 	pass
# def stop_song():
# #	while(player.source != None):
# #		player.next_source()
# 	pass

# #TODO: Pyglet doesn't work with pi


import pygame

pygame.mixer.init()
channel1 = pygame.mixer.Channel(1)
channel1.set_volume(1)

def add_song_to_queue(song):
	sound = pygame.mixer.Sound('/home/pi/jauffre/Jauffre/jauffre/music/' + song)
	#print sound
	channel1.queue(sound)

# def play_song():
# 	if channel1.get_busy() == False:
# 		channel1.play()

def pause_song():
	channel1.pause()

def resume_song():
	channel1.unpause()

def next_song():
	next_sound = channel1.get_queue()
	#print next_sound
	# if next_sound == None:
	# 	channel1.stop()
	# else:
	channel1.play(next_sound)

def stop_song():
	channel1.stop()
