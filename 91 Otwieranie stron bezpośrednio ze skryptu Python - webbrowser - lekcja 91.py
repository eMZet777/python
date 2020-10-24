import requests
import json
import pprint
import webbrowser
"""

API - Application Programming Interface

Inter - pmiędzy
face - twarz

bankomat

pytania
minimalnie 15  punktow
posegregowane  malejaco
z  ostaniego tygodnia
kategorii python

"""

params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate": "2020-10-01",
    "tagged": "python",
    "min": 15,
    
    }

r = requests.get("https://api.stackexchange.com/2.2/questions/", params)


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
