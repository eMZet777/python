
"""
ratings1 = {
    "Arkadiusz": (2,1,2,3,2,3),
    "Agness": (4,2,1,3,4)
    }

for  name in  ratings1:
    print(name, ratings1[name])
    
people3  = ["Arkadiusz", " Wiola", "Kuba"]

for  name in  people3:
            print(name)
            
people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
          ]

for  value in  people2:
    for key in value:
        print(key, value[key])

        """

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }

""""
[('IcFDG2bO9AYDF651DoyH', {'name': 'John', 'age': 27, 'sex': 'Male'}),
('KcD9ntE6IRM59vkVta1k', {'name': 'Marie', 'age': 22, 'sex': 'Female'}),
('yDlgcn99xPc19mYXcRmy', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
('cpQh6GiAbBdGv35NDoTk', {'name': 'Nabeel', 'age': 17, 'sex': 'Male'}),
('12BifzWxCQySKgLhgahC', {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'}),
('QLnmg0pzlLj9x7c7DlLv', {'name': 'Ruby', 'age': 55, 'sex': 'Female'}),
('To47urX0DUznWmOxGZ6H', {'name': 'Lori', 'age': 27, 'sex': 'Male'}),
('KQ4bir3y4tlkbG69I7zq', {'name': 'Marie', 'age': 42, 'sex': 'Female'}),
('94cp4hsyZP2BnCh4D34z', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
('Vr4wRdkljeEs46Czxo54', {'name': 'Chiara', 'age': 17, 'sex': 'Male'})]


""""

"""

for key in people:
    for secondaryKey in people[key]:
        print(secondaryKey, people[key][secondaryKey])

# metoda szybsza  za  pomoca  komendy items  - dzial  tylko dla  slownika

# print(people.items())
""""

for  id, dictionay in people.items():
    print("ID", id)
    for key in dictionary:
        print (key, dictionary(key))


"""

ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]

for name, age, sex in ppllist2:
    print(name)

    """"


