import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]


random.shuffle(cardList)

for  CardsPlayer in  range (2):

    CardsPlayer = []



 
def rozdanie(CardsPlayer):
    for i in range(5):
        CardsPlayer.append(cardList.pop())
        
    return CardsPlayer
 

 
print(rozdanie(CardsPlayer))


