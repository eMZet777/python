szukanaLiczba = 40
podanaLiczba = 0

while szukanaLiczba != podanaLiczba:
    
    podanaLiczba = int(input("podaj liczbe: "))
    if (podanaLiczba > szukanaLiczba):
        print("podaj mniejsza wartosc")
    elif(podanaLiczba < szukanaLiczba):
        print("podaj wieksza wartosc")
    else:
        print("dobra robota")
