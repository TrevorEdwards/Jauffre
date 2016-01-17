import sys
sys.path.append('/music')
import pygame.mixer
import pygame.mixer_music as musicplayer
pygame.mixer.init()

def play(song):
	musicplayer.load(song)
	musicplayer.play()

def queue(song):
	musicplayer.queue(song)

def stop():
	musicplayer.stop()

def pause():
	musicplayer.pause()

def unpause():
	musicplayer.unpause()

if __name__ == '__main__':
	song = "romantic.wav"
	play(song)
