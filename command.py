class Command(object):

	def __init__(self):
		self.type = ''

	def get_type(self):
		return self.type

	def set_type(self, value):
		self.type = value

	def do(self):
		print 'Yikes!'
