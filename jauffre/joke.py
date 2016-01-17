import json, urllib2, synthesize

#Gets a random chuck norris joke
def get_joke_text():
	url = "http://api.icndb.com/jokes/random"

	resp = urllib2.urlopen(url = url).read()
	decoded_resp = json.JSONDecoder().decode(resp)
	joke = decoded_resp['value']['joke']

	synthesize.say(joke)
