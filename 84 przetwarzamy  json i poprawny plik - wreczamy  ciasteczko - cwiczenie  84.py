
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
