import requests
import json
import pprint
import webbrowser
from pprint import pprint


params = {
    "amount" : 5,
    "animal_type": "dog"
    
    }

r = requests.get("https://purr.objects-us-east-1.dream.io/i/bs3vdvb.jpg")



try:
    file = r.json()
  
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
     webbrowser.open_new_tab(file['url'])


