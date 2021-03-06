import joke, weather, music, security, name, creators, having_date, camera_util
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
			if music.channel1.get_queue() == None:
				for song in os.listdir('./music'):
					print song
					music.add_song_to_queue(song)
		elif self.get_type() == "pause":
			music.pause_song()
		elif self.get_type() == "resume":
			music.resume_song()
		elif self.get_type() == "skip":
			music.next_song()
		elif self.get_type() == "stop":
			music.stop_song()
		elif self.get_type() == "name":
			name.do()
		elif self.get_type() == "created":
			creators.do()
		elif self.get_type() == "mood":
			having_date.do()
		elif self.get_type() == "security":
			return security.toggle_security()
		elif self.get_type() == "selfie":
			camera_util.selfie()	
		return False;
