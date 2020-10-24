
import requests
import json


"""
{

}
"""

r = requests.get("https://jsonplaceholder.typicode.com/todos")


#tasks = json.loads(r.text)

def count_Task_Frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1

    return completedTaskFrequencyByUser

"""""

#finkcja do  zwaracnia najwiekszej  wartosci 

def get_keys_with_top_values(my_dict):
    return [
        key
    for (key, value) in my_dict.items()
    if value == max(my_dict.values())

    ]

"""""

def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    userIdWithCompletedAmounthOfTasks = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())

    #przetwarzanie krotki (klucz : wartosc) poprzez funkcje for ponizej 
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            userIdWithCompletedAmounthOfTasks.append(userId)

    return  userIdWithCompletedAmounthOfTasks


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny FORMAT")
else:
    completedTaskFrequencyByUser = count_Task_Frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
    print("Wreczamy ciasteczko mistrza dyscypliny uzytkownikowi o id: ",  usersWithTopCompletedTasks)
"""
#sposob 1

r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()

for user in  users:
    if(user["id"] in usersWithTopCompletedTasks):
        print("Wreczamy ciasteczko mistrza dyscypliny uzytkownikowi o imieniu: ", user["name"])

#sposob 2

for userId in usersWithTopCompletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users", params="id="+str(userId))
    user = r.json()
    print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o imieniu: ", user[0]["name"])
"""

#sposob 3

def change_list_into_conj_of_param(my_list, key="id"):
    conj_param = key + "="
    
    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIteration):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="
    
    return conj_param
    
#conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks, "id")
conj_param = change_list_into_conj_of_param([2,7,4])
r = requests.get("https://jsonplaceholder.typicode.com/users", params=conj_param)   

users = r.json()
for user in users:
    print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o imieniu: ", user["name"])
