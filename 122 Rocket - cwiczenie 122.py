from random import randint

class Rocket:
    def __init__(self, speed):
        self.altitude = 0
        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed



#rocketIndex = Rocket(randint(1, 5))
#rockets =  [rocketIndex for _ in range(5)]

#for _ in range(10):
#    rocketIndexToMove = randint(0, 4)
#    rockets[rocketIndexToMove].moveUp()

#for rocket in rockets:
#    print(rocket.altitude, rocket.speed)
