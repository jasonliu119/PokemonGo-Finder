import json
from pushbullet import Pushbullet
from datetime import datetime

pushbullet_client = None
wanted_pokemon = None

# Initialize object
def init():
    global pushbullet_client, wanted_pokemon
    # load pushbullet key
    with open('config.json') as data_file:
        data = json.load(data_file)
        # get list of pokemon to send notifications for
        wanted_pokemon = _str( data["notify"] ) . split(",")
        # transform to lowercase
        wanted_pokemon = [a.lower() for a in wanted_pokemon]
        # get api key
        api_key = _str( data["pushbullet"] )
        if api_key:
            pushbullet_client = Pushbullet(api_key)


# Safely parse incoming strings to unicode
def _str(s):
  return s.decode('utf-8').strip()

def _f_str(f):
  return "{:.9f}".format(f)

# Notify user for discovered Pokemon
def pokemon_found(pokemon):
    # get name
    pokename = _str(pokemon["name"].encode('utf-8')).lower()
    # check array
    if not pushbullet_client or not pokename in wanted_pokemon: return
    # notify
    print "\n\n[****************] Notifier found pokemon:", pokename
    # Locate pokemon on GMAPS
    google_maps_link = "http://maps.google.com/maps?q=" + _f_str(pokemon["lat"]) + "," + _f_str(pokemon["lng"])
    notification_text = "Pokemon Finder found " + _str(pokemon["name"]) + "!"
    disappear_time = str(datetime.fromtimestamp(pokemon["disappear_time"]).strftime("%I:%M%p").lstrip('0'))+")"
    gMaps = _f_str(pokemon["lat"]) + "," + _f_str(pokemon["lng"])
    location_text = "Locate on Google Maps : " + gMaps + ". " + _str(pokemon["name"]) + " will be available until " + disappear_time + "."

    push = pushbullet_client.push_link(notification_text, google_maps_link, body=location_text)



init()
