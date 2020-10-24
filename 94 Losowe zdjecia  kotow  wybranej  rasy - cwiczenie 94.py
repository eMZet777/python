import requests
import json
import webbrowser
 
catBreedType  = input("Please input  breed Id: ")
pictureAmount = int(input("How many pictures? ")) 

params = {
    "Id" : catBreedType,
    "limit" : pictureAmount
        }
 
r = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=", params)
 
try:
    cats = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for picture in cats:
        webbrowser.open_new_tab(picture["url"])
 
