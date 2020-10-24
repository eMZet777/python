"""
break

continue - pracuje   w oparciu o  while 


wynik = 0

for  i in  range(3):
    x = int(input("Podaj dodatnia liczbe: "))
    if (x>0):
        wynik += x
    else:
        print("miala byc liczba dodatnia, konczymy")
        break
    print("Aktualny  wynik  wynosi", wynik)




wynik = 0

for  i in  range(3):
    x = int(input("Podaj dodatnia liczbe: "))
    if (x>0):
        wynik += x
    else:
        print("miala byc liczba dodatnia, konczymy")
        continue
    print("Aktualny  wynik  wynosi", wynik)


"""

wynik = 0

i = 0

while  i < 3:
    x = int(input("Podaj  dodatnia liczbe: "))
    if (x>0):
        wynik += x
    else:
        print("miala byc  liczba  dodatnia; ")
        continue
    print("aktualny wynik  dodawania to: ", wynik)
    i +=1
    
