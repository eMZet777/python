
"""

JSONplaceholder - miejsce zastepcze na  Twoj przyszly json

"""
import requests
import json

r = requests.get("http://jsonplaceholder.typicode.com/todos")


#tasks = json.loads(r.text)

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("NiepopRAWNY FORMAT")
else:
    print("wszystko jest ok")
    print(tasks[0])




