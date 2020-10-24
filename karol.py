from random import randint

class Rocket:
    def __init__(self, speed):
        self.altitude = 0
        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed

# Rocket(randint(1, 5)) for  i in  range(5):
#     [Rocket(randint(1, 5)) for _ in range(5)]

rockets = []
for i in range(5):
    rocket = Rocket(randint(1,5))
    rockets.append(rocket)

for i in range(10):
    rockets[randint(0,4)].moveUp()

print(rockets)

for _ in range(10):
   rocketIndexToMove = randint(0, 4)
   rockets[rocketIndexToMove].moveUp()

for rocket in rockets:
   print(rocket.altitude, rocket.speed)
