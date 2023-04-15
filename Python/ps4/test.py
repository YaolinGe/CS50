# import cowsay
# import pyttsx3

# engine = pyttsx3.init()
# this = input("What's this? ")
# cowsay.cow(this)
# engine.say(this)
# engine.runAndWait()

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
o = response.json()
for result in o["results"]:
    print(result["trackName"])