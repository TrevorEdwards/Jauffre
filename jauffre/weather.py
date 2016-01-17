import json, urllib2, synthesize

units = 'm' # 'm' for metric, 'e' for English(imperial)
coords = (39.957, -75.192) # cuurently the location of Drexel University, change this to whatever location necessary
geocode = str(coords[0]) + '%2C' + str(coords[1])
language = 'en-US' # I don't think you need to change your language

# Gets weather data
def get_weather():
	authorize()
	url = "https://twcservice.mybluemix.net:443/api/weather/v2/observations/current?units={0}&geocode={1}&language={2}".format(units,geocode,language)
	resp = urllib2.urlopen(url = url).read()
	weather_obsv = json.JSONDecoder().decode(resp)

	url = "https://twcservice.mybluemix.net:443/api/weather/v2/forecast/daily/10day?units={0}&geocode={1}&language={2}".format(units,geocode,language)
	resp = urllib2.urlopen(url = url).read()
	weather_fcast = json.JSONDecoder().decode(resp)

	weather_desc = weather_obsv['observation']['phrase_22char']
	current_temp = weather_obsv['observation']['metric']['temp']
	feels_like = weather_obsv['observation']['metric']['feels_like']
	wind_speed = weather_obsv['observation']['metric']['wspd']
	humidity = weather_obsv['observation']['metric']['rh']
	precip_chance = weather_fcast['forecasts'][1]['day']['pop']
	precip_type = weather_fcast['forecasts'][1]['day']['precip_type']
	pressure = weather_obsv['observation']['metric']['altimeter']

	synthesize.say( "Today's weather is {}, with a temperature of {} degrees, but it feels like {} degrees.\
	The wind speed is {} kilometers per hour. \
	The humidity is {} percent. \
	There is a {} percent chance of {}. \
	The pressure is {} millibars.".format(weather_desc,current_temp,feels_like,wind_speed,humidity,precip_chance,precip_type,pressure) )

def authorize():
	# create a password manager
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

	# Add the username and password.
	# If we knew the realm, we could use it instead of None.
	top_level_url = "twcservice.mybluemix.net:443"
	password_mgr.add_password(None, top_level_url, "adb42adc-659d-4974-a1da-888884839cb7", "V3sKs0gQyp")

	handler = urllib2.HTTPBasicAuthHandler(password_mgr)

	# create "opener" (OpenerDirector instance)
	opener = urllib2.build_opener(handler)

	# Install the opener.
	# Now all calls to urllib2.urlopen use our opener.
	urllib2.install_opener(opener)
