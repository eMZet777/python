class Rocket:
    def __init__(self):
        self.altitude = 0

    def moveUp(self):
        self.altitude +=1



rockets = [Rocket() for  x in range(5)]

print(rockets)