import joke, weather, music, security
import os

class Command(object):

	def __init__(self, command_type,song=""):
		self.type = command_type
		self.song = song

	def get_type(self):
		return self.type

	def do(self):
		if self.get_type() == "joke":
			joke.get_joke_text()
		elif self.get_type() == "weather":
			weather.get_weather()
		elif self.get_type() == "play":
			if music.player.source == None:
				for song in os.listdir('./music'):
					print song
					music.add_song_to_queue(song)
			if not music.player.playing:
				music.play_song()
		elif self.get_type() == "pause":
			music.pause_song()
		elif self.get_type() == "skip":
			music.next_song()
		elif self.get_type() == "stop":
			music.stop_song()
		elif self.get_type() == "security":
			return security.toggle_security()
		return False;
