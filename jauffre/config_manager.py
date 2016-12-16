import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

def get(section,key):
	return config.get(section,key)
