"""
Napisz funkcję, która zasymuluje jak działa lotto,
tzn. wybiersz 6 UNIKALNYCH liczb z 49

sample - próbka/przykład

"""
"""

import random

"""
"""
cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]


random.shuffle(cardList)

print(cardList)

karta = cardList.pop()
karta = cardList.pop()
karta = cardList.pop()
karta = cardList.pop()
karta = cardList.pop()

print(karta)

"""
"""
import random
 
wyniki = set()
amount = int(input("Ile liczb losowac ? : "))
total = int(input("Z ilu liczb losowac ? : "))
 
def totolotek(total):
   wyniki.add(random.randint(1, total))
 
 
while len(wyniki) < amount:
    totolotek(total)
    
else:

print("Wyniki losowania to:", wyniki)

"""
"""
import random

def losowanie(amount, total_amount):
    listaLosowania = []    
    for liczba in range(amount):
        wynikLosowania = random.randint(0, total_amount)
        if wynikLosowania not in listaLosowania:
            listaLosowania.append(wynikLosowania)
            liczba += 1
        else:
            continue
    return listaLosowania
 
print(losowanie(6,49)
"""
"""

import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]


random.shuffle(cardList)

"""
"""
print(random.sample(set(cardList),5))
print(random.sample(set(cardList),5))

"""

"""
print(cardList)



karta1 = cardList.pop()
karta2 = cardList.pop()
karta3 = cardList.pop()
karta4 = cardList.pop()
karta5 = cardList.pop()

print(karta1)
print(karta2)

gracz1  = [karta1, karta2, karta3, karta4, karta5]
print(gracz1)

karta6 = cardList.pop()
karta7 = cardList.pop()
karta8 = cardList.pop()
karta9 = cardList.pop()
karta10 = cardList.pop()

gracz2  = [karta6, karta7, karta8, karta9, karta10]
print(gracz2)

"""
"""
import random


cardList = ['9', '9', '9', '9',
            '10', '10', '10', '10',
            'J', 'J', 'J', 'J',
            'Q', 'Q', 'Q', 'Q',
            'K', 'K', 'K', 'K',
            'A', 'A', 'A', 'A',
            'Joker', 'Joker']



for player in range (2):
    
 
    def carddraw(playerCards):
            for card in range(5):
                random.shuffle(cardList)
                playerCards.append(cardList.pop())
            return playerCards




print(carddraw(playerCards))

return player


"""

import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]


CardsPlayer1 = []
CardsPlayer2 = []


random.shuffle(cardList)
 
def rozdanie(CardsPlayer1, CardsPlayer2):
    for i in range(5):
        CardsPlayer1.append(cardList.pop())
        CardsPlayer2.append(cardList.pop())
    return CardsPlayer1, CardsPlayer2
 

 
print(rozdanie(CardsPlayer1, CardsPlayer2))

