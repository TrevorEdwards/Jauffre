import joke

class Command(object):

	def __init__(self,type):
		self.type = type

	def get_type(self):
		return self.type

	def do(self):
		if self.get_type() == "joke":
			joke.get_joke_text()

